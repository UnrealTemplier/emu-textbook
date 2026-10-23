#!/usr/bin/env python3
"""
scripts/commons_fetch.py — изображение с Wikimedia Commons в media/ урока (инструмент автора).

Берёт имя файла Commons или URL его страницы, через API Commons
(action=query&prop=imageinfo&iiprop=url|extmetadata) получает автора, лицензию, ссылку на лицензию
и описание, скачивает файл, уменьшает до --max-side по длинной стороне, переводит фото в WebP
(схемы — PNG без потерь, SVG — как есть), кладёт в media/ урока и дописывает media/credits.toml.

Это не зависимость сборки: сеть нужна только при работе автора, сайт собирается без неё.
Нужен Pillow (requirements-dev.txt) — кроме SVG и --format keep.

Примеры (из корня репозитория):
    python3 scripts/commons_fetch.py File:Eniac.jpg "sources/0. …/01. Урок.md" --name eniac \\
        --caption "ENIAC в Школе Мура, 1946"
    python3 scripts/commons_fetch.py https://commons.wikimedia.org/wiki/File:MOS_6502AD_4585_top.jpg \\
        "sources/…/media" --name mos6502 --dry-run

Лицензия проверяется по [media] allowed_licenses из book.toml (PD, CC0, CC BY, CC BY-SA, OGL, OGL-C,
Licence Ouverte, dl-de, FAL, own).
Подробности — раздел «Иллюстрации» в docs/03_Final/Final_Progression_v3_Claude/00_Общая_часть.md.
"""

import argparse
import io
import json
import os
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from engine.config import load_config  # noqa: E402
from engine.media import MediaError, image_size, license_allowed, load_credits, normalize_license  # noqa: E402
from engine.scanner import slugify  # noqa: E402

API = "https://commons.wikimedia.org/w/api.php"
# Правила Wikimedia требуют осмысленный User-Agent со ссылкой для связи
USER_AGENT = "emu-textbook-commons-fetch/1.0 (https://github.com/UnrealTemplier/emu-textbook; author tool)"
RASTER_MIME = {"image/jpeg": "jpg", "image/png": "png", "image/gif": "gif", "image/webp": "webp"}
MAX_ORIGINAL_BYTES = 30 * 1024 * 1024       # больше — берём миниатюру, которую рисует Commons
MAX_ORIGINAL_PIXELS = 60_000_000
UNKNOWN_AUTHORS = {"unknown", "unknown author", "anonymous", "неизвестен", "неизвестно",
                   "неизвестный автор", "аноним"}


class FetchError(Exception):
    pass


# ---------------------------------------------------------------------------
# Commons: имя файла, запрос метаданных, загрузка
# ---------------------------------------------------------------------------
def file_title(source: str) -> str:
    """«File:X.jpg», «X.jpg», URL страницы файла (в т. ч. #/media/File:…) или upload.wikimedia.org → «File:X.jpg»."""
    s = source.strip()
    if s.startswith(("http://", "https://")):
        u = urllib.parse.urlsplit(s)
        frag = urllib.parse.unquote(u.fragment)
        path = urllib.parse.unquote(u.path)
        query = urllib.parse.parse_qs(u.query)
        if "/media/" in frag:
            s = frag.split("/media/", 1)[1]
        elif u.netloc == "upload.wikimedia.org":
            # …/commons/d/d3/Name.jpg или …/commons/thumb/d/d3/Name.jpg/800px-Name.jpg
            parts = path.split("/")
            s = parts[parts.index("thumb") + 3] if "thumb" in parts else parts[-1]
        elif "title" in query:
            s = query["title"][0]
        elif "/wiki/" in path:
            s = path.split("/wiki/", 1)[1]
        else:
            raise FetchError(f"не понял URL: {source}")
    s = s.replace("_", " ").strip()
    m = re.match(r"^(file|image|файл|изображение)\s*:\s*", s, re.I)
    if m:
        s = s[m.end():]
    if not s:
        raise FetchError(f"пустое имя файла: {source}")
    return "File:" + s


def http_get(url: str, timeout: int = 120) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except urllib.error.URLError as e:
        raise FetchError(f"{url}: {e}")


def query_imageinfo(title: str, max_side: int) -> dict:
    params = {
        "action": "query", "format": "json", "formatversion": "2", "redirects": "1",
        "titles": title, "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata",
        "iiextmetadatalanguage": "ru", "iiurlwidth": str(max_side), "iiurlheight": str(max_side),
    }
    data = json.loads(http_get(API + "?" + urllib.parse.urlencode(params), timeout=60))
    pages = data.get("query", {}).get("pages", [])
    if not pages or pages[0].get("missing") or not pages[0].get("imageinfo"):
        raise FetchError(f"на Commons нет файла {title}")
    page = pages[0]
    info = page["imageinfo"][0]
    info["title"] = page["title"]
    return info


class _Text(HTMLParser):
    """Текст из HTML extmetadata; скрытые элементы (display:none) пропускаются."""

    VOID = {"br", "img", "hr", "meta", "link", "input", "wbr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.stack = [], []

    def handle_starttag(self, tag, attrs):
        if tag in self.VOID:
            if tag == "br":
                self.out.append(" ")
            return
        style = (dict(attrs).get("style") or "").replace(" ", "").lower()
        self.stack.append("display:none" in style)

    def handle_endtag(self, tag):
        if tag not in self.VOID and self.stack:
            self.stack.pop()

    def handle_data(self, data):
        if not any(self.stack):
            self.out.append(data)


def html_text(value) -> str:
    p = _Text()
    p.feed(str(value or ""))
    p.close()
    return re.sub(r"\s+", " ", "".join(p.out)).strip()


def meta(info: dict, key: str) -> str:
    return html_text(info.get("extmetadata", {}).get(key, {}).get("value", ""))


def book_license(info: dict) -> str:
    """Лицензия для credits.toml: PD, CC0, «CC BY 4.0», «CC BY-SA 3.0 DE» или короткое имя Commons как есть."""
    code = meta(info, "License").lower()
    short = meta(info, "LicenseShortName")
    if code.startswith("pd") or short.lower().startswith(("public domain", "pd")):
        return "PD"
    if code == "cc0" or short.upper().startswith("CC0"):
        return "CC0"
    m = re.match(r"^cc-(by(?:-[a-z]+)*)-(\d+(?:\.\d+)*)(?:-([a-z]{2,5}))?$", code)
    if m:
        lic = f"CC {m.group(1).upper()} {m.group(2)}"
        return lic + (f" {m.group(3).upper()}" if m.group(3) else "")
    return short or code


def author_of(info: dict) -> str:
    artist = meta(info, "Artist")
    credit = meta(info, "Credit")
    if artist and artist.lower().strip(" .") not in UNKNOWN_AUTHORS:
        return artist
    if credit and not credit.lower().startswith(("own work", "собственная работа", "http")):
        return credit
    return artist


# ---------------------------------------------------------------------------
# Обработка изображения
# ---------------------------------------------------------------------------
def need_pillow():
    try:
        from PIL import Image, ImageOps  # noqa: F401
    except ImportError:
        raise FetchError("нужен Pillow: python3 -m pip install -r requirements-dev.txt "
                         "(или --format keep, чтобы сохранить файл без обработки)")
    from PIL import Image, ImageOps
    return Image, ImageOps


def convert(data: bytes, fmt: str, max_side: int, quality: int, max_kb: int):
    """(байты, расширение, описание изменений). fmt: auto, webp, png."""
    Image, ImageOps = need_pillow()
    im = Image.open(io.BytesIO(data))
    if getattr(im, "n_frames", 1) > 1:
        raise FetchError("анимированное изображение: сохраните его без обработки (--format keep)")
    src_format = im.format
    icc = im.info.get("icc_profile")
    im = ImageOps.exif_transpose(im)
    changes = []
    w, h = im.size
    if max(w, h) > max_side:
        im.thumbnail((max_side, max_side), Image.Resampling.LANCZOS)
        changes.append(f"уменьшено до {max(im.size)} px по длинной стороне")
    if fmt == "auto":
        # Рисунок с палитрой (схема, чертёж) — PNG без потерь, остальное — WebP
        drawing = src_format in ("PNG", "GIF") and im.convert("RGBA").getcolors(256) is not None
        fmt = "png" if drawing else "webp"
    if im.mode not in ("RGB", "RGBA"):
        has_alpha = im.mode in ("LA", "PA") or (im.mode == "P" and "transparency" in im.info)
        im = im.convert("RGBA" if has_alpha else "RGB")
    out = io.BytesIO()
    if fmt == "png":
        im.save(out, "PNG", optimize=True, icc_profile=icc)
        if src_format != "PNG":
            changes.append("PNG")
        return out.getvalue(), "png", ", ".join(changes)
    q = quality
    while True:
        out = io.BytesIO()
        im.save(out, "WEBP", quality=q, method=6, icc_profile=icc)
        if not max_kb or out.tell() <= max_kb * 1024 or q <= 50:
            break
        q -= 10
    changes.append(f"WebP (качество {q})")
    return out.getvalue(), "webp", ", ".join(changes)


# ---------------------------------------------------------------------------
# media/ и credits.toml
# ---------------------------------------------------------------------------
def media_dir_for(target: str, dir_name: str) -> str:
    """Урок (.md), каталог урока или сама папка media/ → путь папки media/."""
    path = os.path.abspath(target)
    if path.endswith(".md"):
        if not os.path.isfile(path):
            raise FetchError(f"нет урока {target}")
        return os.path.join(os.path.dirname(path), dir_name)
    if os.path.basename(path) == dir_name:
        if not os.path.isdir(os.path.dirname(path)):
            raise FetchError(f"нет каталога {os.path.dirname(target)}")
        return path
    if not os.path.isdir(path):
        raise FetchError(f"нет каталога {target}")
    return os.path.join(path, dir_name)


def default_name(title: str) -> str:
    stem = os.path.splitext(title.split(":", 1)[1])[0]
    ascii_stem = unicodedata.normalize("NFKD", stem).encode("ascii", "ignore").decode()
    return slugify(ascii_stem or stem, max_length=40)


def toml_str(value: str) -> str:
    s = value.replace("\\", "\\\\").replace('"', '\\"')
    s = re.sub(r"[\x00-\x1f\x7f]", lambda m: "\\u%04x" % ord(m.group()), s)
    return f'"{s}"'


def credits_block(name: str, entry: dict, comments: list) -> str:
    lines = [f"[{toml_str(name)}]"]
    lines += [f"# {c}" for c in comments]
    for key in ("caption", "alt", "author", "license", "license_url", "source", "modified"):
        if entry.get(key):
            lines.append(f"{key} = {toml_str(entry[key])}")
    if entry.get("invert_dark"):
        lines.append("invert_dark = true")
    return "\n".join(lines) + "\n"


def write_credits(path: str, name: str, block: str) -> None:
    """Дописывает запись; при замене удаляет прежнюю таблицу ["name"] (до следующего заголовка)."""
    text = ""
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fp:
            text = fp.read()
    header = f"[{toml_str(name)}]"
    lines = text.splitlines(keepends=True)
    start = next((i for i, ln in enumerate(lines) if ln.strip() == header), None)
    if start is not None:
        end = next((i for i in range(start + 1, len(lines)) if lines[i].lstrip().startswith("[")), len(lines))
        lines[start:end] = []
        text = "".join(lines)
    text = text.rstrip("\n")
    text = (text + "\n\n" if text else "") + block
    with open(path, "w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)


# ---------------------------------------------------------------------------
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Изображение с Wikimedia Commons → media/ урока и запись в credits.toml.")
    ap.add_argument("source", help="File:Имя.jpg, Имя.jpg или URL страницы файла на Commons")
    ap.add_argument("target", help="урок (.md), каталог урока или папка media/")
    ap.add_argument("--name", help="имя файла без расширения, латиницей (по умолчанию — из имени на Commons)")
    ap.add_argument("--caption", help="подпись по умолчанию (по-русски)")
    ap.add_argument("--alt", help="альтернативный текст, если отличается от подписи")
    ap.add_argument("--author", help="автор вместо взятого с Commons")
    ap.add_argument("--license", help="лицензия вместо взятой с Commons (например, одна из нескольких у файла)")
    ap.add_argument("--format", choices=["auto", "webp", "png", "keep"], default="auto",
                    help="auto: фото → WebP, схема с палитрой → PNG, SVG → как есть; keep — без обработки")
    ap.add_argument("--max-side", type=int, default=1600, help="длинная сторона, px (по умолчанию 1600)")
    ap.add_argument("--quality", type=int, default=80, help="качество WebP (по умолчанию 80)")
    ap.add_argument("--invert-dark", action="store_true", help="чёрно-белая схема: инвертировать в тёмных темах")
    ap.add_argument("--force", action="store_true", help="заменить существующий файл и запись")
    ap.add_argument("--dry-run", action="store_true", help="только показать метаданные и что будет сделано")
    args = ap.parse_args(argv)
    sys.stdout.reconfigure(line_buffering=True)

    try:
        cfg = load_config(os.path.join(ROOT, "book.toml"))
        m = cfg.media
        title = file_title(args.source)
        info = query_imageinfo(title, args.max_side)
        mime = info.get("mime", "")
        license_ = args.license or book_license(info)
        author = args.author or author_of(info)
        source_url = info["descriptionurl"]
        print(f"Commons:   {info['title']} ({mime}, {info.get('width')}×{info.get('height')}, "
              f"{info.get('size', 0) // 1024} КБ)")
        print(f"Страница:  {source_url}")
        print(f"Автор:     {author or '—'}   (Artist: {meta(info, 'Artist') or '—'}; "
              f"Credit: {meta(info, 'Credit') or '—'})")
        print(f"Лицензия:  {license_}   (Commons: {meta(info, 'LicenseShortName') or '—'}, "
              f"{meta(info, 'LicenseUrl') or 'без ссылки'})")
        description = meta(info, "ImageDescription")
        if description:
            print(f"Описание:  {description[:300]}")
        restrictions = meta(info, "Restrictions")
        if restrictions:
            print(f"⚠ Ограничения Commons: {restrictions} (товарный знак, права на изображение человека и т. п.)")

        if normalize_license(license_) == "OWN":
            raise FetchError("own — для собственных иллюстраций книги, не для файлов Commons")
        if not license_allowed(license_, m.allowed_licenses):
            raise FetchError(f"лицензия «{license_}» не из allowed_licenses {m.allowed_licenses}; "
                             "если у файла есть и подходящая лицензия, укажите её через --license")
        if not author:
            raise FetchError("автор на Commons не указан — задайте --author (например, «Неизвестный автор»)")

        name = args.name or default_name(info["title"])
        if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", name):
            raise FetchError(f"--name: только строчная латиница, цифры, «-», «_», «.»: {name!r}")
        media_dir = media_dir_for(args.target, m.dir_name)

        # Что скачивать: SVG и обычные растры — оригинал; TIFF, PDF, огромные файлы — миниатюру Commons
        is_svg = mime == "image/svg+xml"
        too_big = (info.get("size", 0) > MAX_ORIGINAL_BYTES
                   or (info.get("width") or 0) * (info.get("height") or 0) > MAX_ORIGINAL_PIXELS)
        use_original = is_svg or args.format == "keep" or (mime in RASTER_MIME and not too_big)
        url = info["url"] if use_original else info.get("thumburl")
        if not url:
            raise FetchError("Commons не отдал миниатюру этого файла")
        if args.format == "keep":
            ext = "svg" if is_svg else RASTER_MIME.get(mime)
            if not ext:
                raise FetchError(f"--format keep: формат {mime} не годится для сайта")
        elif is_svg:
            ext = "svg"
        else:
            ext = "?"
        print(f"Скачать:   {'оригинал' if use_original else 'миниатюру Commons'} — {url.split('?')[0]}")

        # Файл с этим именем (любое расширение) или его запись — до скачивания
        credits_path = os.path.join(media_dir, m.credits_file)
        credits = load_credits(credits_path) if os.path.exists(credits_path) else {}
        taken = sorted({f for f in (os.listdir(media_dir) if os.path.isdir(media_dir) else []) if f.startswith(name + ".")}
                       | {f for f in credits if f.startswith(name + ".")})
        taken = [f for f in taken if f != m.credits_file]
        if taken and not args.force:
            raise FetchError(f"в {os.path.relpath(media_dir, ROOT)} уже есть {', '.join(taken)} (--force — заменить)")

        if args.dry_run:
            print(f"Положить:  {os.path.relpath(media_dir, ROOT)}/{name}.{ext if ext != '?' else '…'} (--dry-run: ничего не записано)")
            return 0

        data = http_get(url)
        modified = ""
        if args.format == "keep" or is_svg:
            out = data
            if is_svg and args.format not in ("auto", "keep"):
                print("SVG сохраняется как есть: --format игнорируется")
        else:
            out, ext, modified = convert(data, args.format, args.max_side, args.quality, m.max_file_kb)

        filename = f"{name}.{ext}"
        if ext not in m.extensions:
            raise FetchError(f"расширение {ext} не из [media] extensions {m.extensions}")
        dest = os.path.join(media_dir, filename)
        rel = os.path.relpath(dest, ROOT).replace(os.sep, "/")
        if cfg.audit.path_max and len(rel) > cfg.audit.path_max:
            raise FetchError(f"путь длиннее [audit] path_max = {cfg.audit.path_max}: {rel}")

        os.makedirs(media_dir, exist_ok=True)
        with open(dest, "wb") as fp:
            fp.write(out)

        entry = {"caption": args.caption, "alt": args.alt, "author": author, "license": license_,
                 "license_url": meta(info, "LicenseUrl"), "source": source_url, "modified": modified,
                 "invert_dark": args.invert_dark}
        comments = [f"Commons: {info['title']}; лицензия там: {meta(info, 'LicenseShortName') or '—'}"]
        if description and not args.caption:
            comments.append("Описание Commons (для подписи): " + description[:300])
        if restrictions:
            comments.append("Ограничения Commons: " + restrictions)
        write_credits(credits_path, filename, credits_block(filename, entry, comments))
        load_credits(credits_path)      # запись должна читаться движком

        size = image_size(dest)
        kb = len(out) / 1024
        print(f"Записано:  {rel} — {size[0]}×{size[1]} px, {kb:.0f} КБ" if size else f"Записано:  {rel} — {kb:.0f} КБ")
        print(f"Атрибуция: {os.path.relpath(credits_path, ROOT)}")
        if m.max_file_kb and kb > m.max_file_kb:
            print(f"⚠ больше max_file_kb = {m.max_file_kb} КБ: уменьшите --max-side или --quality")
        if size and m.max_dimension_px and max(size) > m.max_dimension_px:
            print(f"⚠ сторона больше max_dimension_px = {m.max_dimension_px}")
        if ext == "svg" and not size:
            print("⚠ у SVG нет width/height и viewBox: движок не узнает размеры")
        stale = [f for f in taken if f != filename]
        if stale:
            print(f"⚠ прежние файлы и записи с другим расширением остались: {', '.join(stale)} — удалите их, если не нужны")
        if not args.caption:
            print("⚠ подписи нет: задайте caption в credits.toml или подпись в тексте урока")
        print(f'В уроке:   ![{args.alt or args.caption or "…"}]({m.dir_name}/{filename}) или ![[{filename}]]')
        return 0
    except (FetchError, MediaError) as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
