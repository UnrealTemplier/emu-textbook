#!/usr/bin/env sh
# Изображение с Wikimedia Commons → media/ урока и credits.toml (аргументы — как у scripts/commons_fetch.py или по запросу)
. "$(dirname "$0")/_lib.sh"
if [ $# -eq 0 ]; then
  printf "%s: " "Файл Commons (File:… или URL страницы)"; read -r SRC
  printf "%s: " "Урок (.md) или каталог урока"; read -r DST
  printf "%s: " "Имя файла латиницей без расширения (Enter — из имени на Commons)"; read -r NAME
  printf "%s: " "Подпись (Enter — без подписи)"; read -r CAP
  set -- "$SRC" "$DST"
  [ -n "$NAME" ] && set -- "$@" --name "$NAME"
  [ -n "$CAP" ] && set -- "$@" --caption "$CAP"
fi
$PY scripts/commons_fetch.py "$@"
