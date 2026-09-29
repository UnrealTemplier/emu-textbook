Привет! Проект у тебя получается не просто “учебник по эмуляторам”, а почти полноценная академия: архитектура ЭВМ, микропроцессоры, шины, прерывания, DMA, видео- и звуковые чипы, тайминги, обратная инженерия, тестирование, документация, производительность, Go-инжиниринг. Это действительно может быть многотомная работа на годы.

Ниже я даю:

1. **Большой хронологический каталог систем и процессоров** — примерно от механических концептов до современных консолей и SoC.
2. **Отдельную сортировку “от простого к сложному”** — не хронологическую, а учебную.
3. **Мой анализ проекта**: как это лучше устроить, что стоит сделать первым, какие есть ловушки, какие альтернативы проектирования стоит показывать, где брать документацию и как учить читателя думать как инженер.

Важно: я буду использовать слово **“система”** широко — процессор, плата, компьютер, консоль, аркадный автомат, SoC, игровая приставка, микроконтроллер. Годы указываю приблизительно, потому что у многих систем были версии, ревизии, региональные релизы и разные поколения.

---

# 1. Хронологический каталог систем, процессоров и платформ

## 1830–1945: механика, логика, первые электронные машины

- **1837, 1840-е — Difference Engine / Analytical Engine**
  Чарльз Бэббидж. Не цифровой процессор в современном смысле, но отличная отправная точка для понимания вычислительной машины, хранения команд, арифметики, ввода/вывода.

- **1936 — Абстрактная машина Тьюринга**
  Теоретическая основа: лента, состояния, переходы, детерминированность/недетерминированность, вычислимость.

- **1936–1938 — Post-Turing machine / Post’s canonical system**
  Альтернативная модель вычислений. Полезно для учебной абстрактной машины.

- **1937–1942 — Atanasoff–Berry Computer, ABC**
  Ранняя электронная вычислительная машина. Не универсальная в современном смысле, но важна исторически.

- **1941 — Zuse Z3**
  Конрад Цузе. Электромеханический компьютер, программируемый, с плавающей точкой. Хорош как “компьютер до эпохиStored-program в классическом виде”.

- **1943 — Colossus**
  Электронная машина для криптоанализа. Не универсальный компьютер в привычном смысле, но полезная задача для эмулятора/симулятора.

- **1945 — ENIAC**
  Одна из первых электронных универсальных машин. Программировалась кабелями и переключателями. Отличный пример “не-software-first” архитектуры.

- **1945/1949 — EDVAC**
  Архитектура фон Неймана, stored-program. Очень важна для теоретической части учебника.

- **1948 — Manchester Baby / Small-Scale Experimental Machine, SSEM**
  Один из первых stored-program компьютеров. Отличный кандидат для абстрактной учебной машины.

- **1949 — EDSAC**
  Cambridge. Stored-program, инструкции, память, ввод/вывод. Очень хорош для ранней учебной эмуляции.

- **1949 — BINAC**
  Ранняя электронная машина, интересна как историческая система.

---

## 1950–1965: mainframes, первые коммерческие машины, minicomputers

- **1950 — Manchester Mark 1**
  Развитие SSEM, индексы, память, более практичная архитектура.

- **1951 — Ferranti Mark 1**
  Первый коммерческий stored-program компьютер.

- **1951 — UNIVAC I**
  Первый массовый коммерческий компьютер США.

- **1952 — IAS machine / Von Neumann machine**
  Архитектура, повлиявшая на многие последующие машины.

- **1952 — ILLIAC I**
  Университетская машина, наследник IAS.

- **1952 — CSIRAC**
  Австралийская ранняя машина.

- **1953 — IBM 701**
  Первый научный компьютер IBM.

- **1953 — UNIVAC 1103**
  Научный компьютер.

- **1954 — IBM 704**
  Очень важная машина: индексы, floating point, ассемблер, FORTRAN. Отличный проект для учебника.

- **1958 — IBM 709**
  Продолжение 704. Важна для истории batch-систем, tape, punch cards.

- **1959 — IBM 7090**
  Транзисторная версия 709. Хороша для изучения “большой машины” с периферией.

- **1959 — IBM 1401**
  Буквенно-цифровая машина, очень популярная в бизнесе. Архитектура сильно отличается от классической “числовой”.

- **1959 — IBM 1620**
  Упрощенная научная машина, decimal, “no arithmetic unit” в некоторых конфигурациях. Интересная архитектурная задача.

- **1960 — PDP-1**
  DEC. Интерактивная машина, графика, Spacewar! Хороша для изучения interactive computing.

- **1960 — CDC 1604**
  Научный компьютер, важен для CDC-линии.

- **1961 — Burroughs B5000**
  Stack-ориентированная архитектура, ALGOL, виртуальная память. Очень интересна как альтернатива классическому фон-неймановскому CPU.

- **1962 — IBM 7094**
  Развитие 709/7090.

- **1963 — CDC 3600**
  Научная машина, предшественник CDC 6600.

- **1963 — PDP-4**
  DEC, 18-bit машина, интересна для изучения.

- **1963 — PDP-5**
  12-bit minicomputer, предшественник PDP-8.

- **1963 — Honeywell 200**
  Важная линия.

- **1964 — CDC 6600**
  Supercomputer, один из первых “суперкомпьютеров”, интересен для изучения параллельных периферийных процессоров и производительности.

- **1964 — IBM System/360**
  Огромная архитектурная линия. Команда/семейство совместимых машин. Очень важна для истории совместимости, ISA, микросхем, периферии.

- **1964 — PDP-7**
  DEC. 18-bit, 12-bit word? Очень важна для тебя: PDP-7 связана с Unix. Отличный проект, но требует понимания периферии.

- **1964 — GE-225**
  Важна для истории времени-разделения, Dartmouth BASIC.

- **1965 — PDP-8**
  Одна из самых успешных и простых minicomputer-архитектур. Отличный кандидат для учебника: 12-bit, малая система, реальная история, много документации.

- **1965 — IBM 1130**
  Small scientific/business computer.

- **1965 — Honeywell 2200**
  Продолжение линии.

---

## 1965–1975: minicomputers, начало микропроцессоров

- **1966 — PDP-10**
  DEC, 36-bit, очень важна для истории операционных систем, TOPS-10, Lisp, Time-Sharing.

- **1966 — SDS 940**
  Time-sharing machine, важна для истории ОС.

- **1966 — HP 2100**
  Minicomputer, интересна для изучения I/O и реальных систем.

- **1966 — Honeywell DDP-224**
  Minicomputer.

- **1967 — Burroughs B6700**
  Stack-машина, виртуальная память, история ОС.

- **1967 — PDP-9**
  DEC.

- **1968 — CDC 7600**
  Supercomputer, интересна для изучения производительности, конвейеров, памяти.

- **1968 — PDP-15**
  DEC, 18-bit.

- **1969 — Data General Nova**
  Очень важная minicomputer-линия. Простая архитектура, много документации.

- **1969 — PDP-11/20**
  Начало PDP-11.

- **1970 — PDP-11**
  Одна из важнейших архитектур для учебника. 16-bit, UNIBUS/UNIBUS-like, прерывания, DMA, регистры, память, периферия. Отличная база.

- **1970 — IBM System/370**
  Развитие System/360, виртуальная память, channel architecture.

- **1971 — Intel 4004**
  Первый микропроцессор. Отличный учебный проект: 4-bit, ограниченная память, простая система.

- **1971 — PDP-11/45**
  Важная версия PDP-11.

- **1972 — Intel 8008**
  8-bit, 14-bit адрес, интересна как предшественник 8080.

- **1972 — Magnavox Odyssey**
  Первая домашняя консоль. Нет CPU, дискретная логика. Хороша для понимания “системы без процессора”.

- **1972 — HP 3000**
  Minicomputer, интересна для истории.

- **1973 — Micral**
  Один из первых микрокомпьютеров на 8008.

- **1974 — Motorola 6800**
  8-bit CPU, важен для истории, много машин на 6800/6809.

- **1974 — Intel 8080**
  Один из самых важных учебных CPU. Много документации, много клонов, много тестов.

- **1975 — Altair 8800**
  8080-based. Отличный проект: простой bus, front panel, память, переключатели.

- **1975 — IMSAI 8080**
  Клон/развитие Altair.

- **1975 — MOS 6502**
  Легендарный 8-bit CPU. Один из лучших стартовых проектов для учебника.

- **1975 — Intel 8085**
  Развитие 8080.

- **1976 — Apple I**
  6502, простая плата, память, видеотерминал. Отличный проект.

- **1976 — Zilog Z80**
  Один из важнейших 8-bit CPU. Отличная документация, много систем.

- **1976 — Fairchild Channel F**
  Первая картриджная консоль, CPU F8.

- **1976 — Intel 8048**
  Микроконтроллер, важен для embedded.

- **1977 — Atari 2600 / Atari VCS**
  6507 + TIA. Очень важная учебная система: CPU простой, но видеочип и тайминги — отдельный мир.

- **1977 — Apple II**
  6502, память, видео, диск, расширяемость. Один из лучших учебных компьютеров.

- **1977 — Commodore PET**
  6502, CRT, клавиатура, память. Хорош для домашней машины.

- **1977 — Tandy TRS-80**
  Z80, домашний компьютер, много клонов.

- **1977 — Intel 8086**
  16-bit x86. Начальная точка для всей PC-линии.

- **1977 — DEC VAX-11/780**
  32-bit, виртуальная память, важная архитектура для истории ОС.

- **1978 — Motorola 6809**
  Очень элегантный 8-bit CPU. Отличен для учебника, много документации, много систем.

- **1978 — Intel 8086**
  Повторно, как начало x86.

- **1979 — Intel 8088**
  16-bit CPU с 8-bit шиной данных, основа IBM PC.

- **1979 — Motorola 68000**
  Одна из важнейших архитектур для учебника. 32-bit регистры, 24-bit адрес, много систем: Mac, Amiga, Atari ST, Mega Drive, arcade.

- **1979 — Atari 800 / Atari 400**
  6502 + ANTIC/GTIA/POKEY. Очень интересная система: CPU простой, но графика и звук сложные.

- **1979 — TI-99/4A**
  TMS9900-based. Важна для истории home computers.

- **1979 — Zilog Z8000**
  16-bit Z80-family, интересна для изучения сегментации и памяти.

- **1979 — Motorola 68HC05**
  Микроконтроллер, важен для embedded.

- **1979 — Zilog Z8**
  Микроконтроллер.

- **1980 — Commodore VIC-20**
  6502 + VIC + SID. Хороший учебный домашний компьютер.

- **1980 — Pac-Man arcade hardware**
  Z80 + видео/звук. Отличная аркадная учебная система.

- **1980 — Intel 8051**
  Один из важнейших микроконтроллеров.

- **1980 — Tandy Color Computer / CoCo**
  6809. Отличная система для изучения 6809.

---

## 1980–1990: home computers, 8-bit консоли, начало 16-bit

- **1981 — IBM PC**
  8088, ISA, BIOS, видео, клавиатура, диск. Один из важнейших проектов в учебнике.

- **1981 — BBC Micro**
  6502, сложный ULA, графика, сеть, память. Отличная учебная система.

- **1981 — NEC PC-8801**
  Японский home computer, Z80, VDP.

- **1981 — Acorn Atom**
  6502, предшественник BBC Micro.

- **1982 — Commodore 64**
  6510 + VIC-II + SID. Одна из самых важных учебных систем для cycle-accurate эмуляции.

- **1982 — ZX Spectrum**
  Z80 + ULA, память, клавиатура, видео. Очень важна для изучения contention, ULA, tape.

- **1982 — Sega SG-1000**
  Z80 + VDP, Sega home console.

- **1982 — MSX**
  Z80 + VDP + PSG. Отличная стандартизированная система.

- **1982 — Atari 5200**
  6502C + ANTIC/GTIA/POKEY. Интересная эволюция Atari 8-bit.

- **1982 — Intel 80286**
  Protected mode, важная веха x86.

- **1982 — Intel 80186 / 80188**
  Интегрированный 8086, периферия, embedded.

- **1982 — IBM PC/XT**
  Развитие IBM PC.

- **1983 — Nintendo Famicom / NES**
  2A03: 6502 + PPU/APU. Один из лучших учебных проектов: CPU простой, но PPU, APU, mapper, scanline timing — огромная инженерная школа.

- **1983 — IBM PC/XT**
  Повторно, как массовая линия.

- **1983 — Apple Lisa**
  68000, GUI, память, диск. Важна для истории Mac.

- **1983 — Rockwell 65C02**
  Важная эволюция 6502.

- **1983 — Acorn Electron**
  Упрощенный BBC Micro, 6502.

- **1983 — NEC PC-9801**
  Огромная японская линия, x86, VDP, звук, DOS. Важна для эмуляции.

- **1984 — Apple Macintosh**
  68000, Mac Toolbox, ROM, floppy, framebuffer. Отличный проект.

- **1984 — IBM PC/AT**
  80286, AT bus, BIOS.

- **1984 — Amstrad CPC**
  Z80 + CRTC + ASIC. Хорош для изучения видео и memory mapping.

- **1984 — Sinclair QL**
  68008, память, networking, QDOS. Интересная система.

- **1984 — IBM PCjr**
  8088, graphics, sound. Интересный клон/эксперимент IBM.

- **1984 — Tandy 1000**
  PC-compatible, graphics, sound.

- **1985 — Commodore Amiga**
  68000 + OCS/ECS/AGA, Agnus, Denise, Paula, CIA. Один из лучших учебных проектов для 16-bit home computer.

- **1985 — Atari ST**
  68000 + Shifter + MMU + YM2149. Отличная учебная система.

- **1985 — Sega Master System**
  Z80 + VDP + PSG. Хороша как эволюция SG-1000 и база для Game Gear.

- **1985 — NES в США**
  Повторно, как массовая линия.

- **1985 — Intel 80386**
  32-bit x86, paging, protected mode. Очень важная веха.

- **1985 — Commodore 128**
  8502 + VDC + SID + C64 compatibility. Очень интересная система.

- **1986 — Atari 7800**
  6502C + MARIA. Важна для понимания видеочипа и совместимости с Atari 2600.

- **1986 — Apple IIgs**
  65C816 + видео/звук. Важная эволюция Apple II.

- **1986 — WDC 65C816**
  16-bit расширение 6502, важно для SNES.

- **1986 — Motorola 68010**
  Развитие 68000, virtual memory support.

- **1987 — NEC PC Engine / TurboGrafx-16**
  HuC6280 + VDC + C6290. Интересная 8/16-bit гибридная система.

- **1987 — IBM PS/2**
  Micro Channel, VGA, OS/2. Важна для PC-линии.

- **1987 — Sharp X68000**
  68000 + MOS graphics + custom chips. Отличная японская учебная система.

- **1987 — Acorn Archimedes**
  ARM, RISC, память, видеочип. Важна для ARM-линии.

- **1987 — SPARC**
  RISC-линия, Sun. Важна для архитектуры.

- **1988 — Sega Mega Drive / Genesis**
  68000 + Z80 + VDP + YM2612. Один из важнейших проектов для учебника.

- **1988 — Motorola 68020**
  Развитие 68000, coprocessor interface.

- **1989 — Nintendo Game Boy**
  LR35902 + PPU + APU. Отличный учебный проект: CPU похож на Z80/8080, но PPU, LCD, interrupts, audio — отдельная наука.

- **1989 — Intel 80486**
  x86 с FPU, cache, pipeline.

- **1989 — Sega Genesis в США**
  Повторно, как массовая линия.

- **1989 — Atari Lynx**
  65C02 + Suzy + Mikey. Интересная портативная система.

- **1989 — FM Towns**
  68000, CD-ROM, звук, видео. Хороша для изучения CD-систем.

- **1989 — NEC PC Engine в США**
  TurboGrafx-16.

---

## 1990–2000: 16-bit консоли, 32-bit, аркадные платы, начало 3D

- **1990 — Nintendo SNES / Super Famicom**
  65C816 + SPC700 + PPU + DMA + coprocessors. Один из самых сложных 16-bit проектов, но очень полезный.

- **1990 — SNK Neo Geo AES / MVS**
  68000 + Z80 + видеочипы. Отличная учебная система для arcade/home hybrid.

- **1990 — Sega Game Gear**
  Z80 + VDP + PSG. Развитие Master System.

- **1990 — Motorola 68030**
  MMU, cache, pipeline.

- **1991 — Sega CD / Mega-CD**
  68000 + ASIC + PCM + CD. Важна для изучения CD-ROM, DMA, аудио.

- **1991 — Super FX / Super FX2**
  Coprocessor для SNES. Отличная тема для “как ускорить эмулируемую систему”.

- **1991 — Intel 80486**
  Повторно, как массовая линия.

- **1991 — NEC SuperGrafx**
  PC Engine с дополнительным видео.

- **1992 — Atari Falcon**
  68030 + DSP + видео. Интересная домашняя машина.

- **1992 — Motorola 68040**
  68030 с FPU, cache, pipeline.

- **1992 — Alpha AXP**
  DEC 64-bit RISC. Важна для архитектуры.

- **1993 — Atari Jaguar**
  Tom, Jerry, GPU, Blitter, DSP. Очень сложная и интересная система.

- **1993 — Sega Model 1**
  PowerPC + custom 3D GPU. Важна для 3D arcade.

- **1993 — PowerPC 601**
  Начало PowerPC-линии.

- **1993 — MIPS R4000**
  Важная RISC-архитектура, база для N64 и многих embedded/SGI.

- **1993 — Motorola DSP56000**
  DSP, важен для Dreamcast AICA и других систем.

- **1993 — NEC PC-9821**
  Развитие PC-98.

- **1993 — Sharp X68030**
  Развитие X68000.

- **1994 — Sega Saturn**
  2× SH-2 + VDP1 + VDP2 + SCD68000 + Motorola 68EC000 + звук. Одна из самых сложных 32-bit систем для эмуляции.

- **1994 — Sony PlayStation**
  R3000A + GTE + GPU + SPU + CDROM controller + DMA. Один из важнейших учебных проектов.

- **1994 — NEC PC-FX**
  68000 + видео/звук, интересная японская система.

- **1994 — Sega 32X**
  2× SH-2 + 68000 + VDP + Genesis. Важна для изучения add-on архитектуры.

- **1994 — Neo Geo CD**
  Neo Geo + CD.

- **1995 — Sega Saturn в США**
  Повторно.

- **1995 — Sony PlayStation в США**
  Повторно.

- **1995 — Nintendo Virtual Boy**
  RISC-like CPU + стерео-LED-дисплей. Интересная система.

- **1995 — Intel Pentium Pro**
  Microarchitecture, out-of-order, важная веха x86.

- **1995 — AMD K5**
  x86-линия.

- **1996 — Nintendo 64**
  NEC VR4300 + RDP + RSP + Reality Coprocessor. Очень сложная, но важная система.

- **1996 — Sega Model 3**
  PowerPC + 3D GPU. Важна для arcade.

- **1996 — Apple Pippin**
  PowerPC + CD + Mac OS. Интересная нишевая система.

- **1996 — Sega Saturn / PlayStation массовая линия**
  Повторно.

- **1997 — PowerPC G3**
  Apple, IBM/Motorola. Важна для Mac-линии.

- **1997 — Motorola 68060**
  Развитие 68040.

- **1997 — ARM7TDMI**
  Очень важная архитектура для GBA, embedded, DS.

- **1998 — Sega Dreamcast**
  SH-4 + PowerVR + AICA ARM7 + DSP + GD-ROM. Один из важнейших 128-bit/32-bit переходных проектов.

- **1998 — Nintendo Game Boy Color**
  LR35902 + цветной PPU. Развитие Game Boy.

- **1998 — Intel Pentium II**
  Slot-based, MMX, microarchitecture.

- **1998 — AMD K7 / Athlon**
  Важная x86-линия.

- **1999 — Bandai WonderSwan**
  NEC V30-like CPU + LCD. Интересная портативная система.

- **1999 — SNK Neo Geo Pocket Color**
  Z80 + цветной экран.

- **1999 — PowerVR / Sega Dreamcast GPU**
  Повторно, как отдельная архитектура.

- **1999 — Intel Pentium III**
  SSE, MMX, microarchitecture.

---

## 2000–2010: 64-bit, портативные консоли, современные SoC

- **2000 — Sony PlayStation 2**
  Emotion Engine + Graphics Synthesizer + IOP + SPU2 + CD/DVD. Очень сложная, важная система.

- **2000 — Bandai WonderSwan Color**
  ARM7 + LCD. Развитие WonderSwan.

- **2000 — Sega Dreamcast в Европе/США массовая линия**
  Повторно.

- **2000 — Intel Pentium 4**
  NetBurst, SSE, сложная microarchitecture.

- **2001 — Nintendo GameCube**
  IBM Gekko PowerPC + ATI Flipper GPU. Важна для 3D home console.

- **2001 — Microsoft Xbox**
  Pentium III + NV2A GPU + I/O. Важна для PC-подобной консоли.

- **2001 — Nintendo Game Boy Advance**
  ARM7TDMI + BIOS + PPU + APU + DMA. Отличный учебный проект.

- **2001 — PowerPC G4**
  Apple, AltiVec.

- **2001 — NEC PC Engine / TurboGrafx-16 эмуляция массовая**
  Повторно.

- **2004 — Sony PSP**
  MIPS Allegrex + GPU + media engines. Важна для изучения 3D handheld.

- **2004 — Nintendo DS**
  ARM9 + ARM7 + 2D/3D GPU + WiFi + touch. Отличная multi-CPU система.

- **2004 — Intel Pentium 4 Prescott**
  x86-линия.

- **2004 — Taito Type X**
  Arcade PC-based. Интересна как “arcade на PC”.

- **2005 — Microsoft Xbox 360**
  Xenon PowerPC + Xenos GPU + multicore. Очень сложная система.

- **2005 — Nintendo DS Lite**
  Развитие DS.

- **2005 — AMD Athlon 64**
  x86-64, важная веха.

- **2006 — Sony PlayStation 3**
  Cell BE + RSX GPU. Одна из самых сложных систем для эмуляции.

- **2006 — Nintendo Wii**
  Broadway PowerPC + Hollywood GPU. Важна для GameCube-совместимости и motion controls.

- **2006 — Intel Core 2**
  Важная x86-линия.

- **2007 — Apple iPhone**
  ARM + PowerVR + touch. Не классическая ретро-система, но важна для ARM/GPU.

- **2008 — Nintendo DSi**
  Развитие DS.

- **2008 — Intel Atom**
  x86 для low-power.

- **2009 — ARM Cortex-A8**
  Важная мобильная архитектура.

---

## 2010–2025: современные SoC, x86-64, ARM64, GPU

- **2010 — ARM Cortex-A9**
  Мобильная/встроенная архитектура.

- **2011 — Nintendo 3DS**
  ARM11 + ARM9 + GPU + стереоскопический экран. Важна для изучения 3D handheld.

- **2011 — Sony PS Vita**
  ARM Cortex-A9 + GPU + touch. Важна для handheld.

- **2011 — AMD Bulldozer / FX**
  x86 microarchitecture.

- **2012 — Nintendo Wii U**
  Espresso PowerPC + GPU. Важна для Wii/GameCube lineage.

- **2012 — ARM Cortex-A15**
  Важная мобильная архитектура.

- **2013 — Sony PlayStation 4**
  AMD Jaguar x86-64 + GCN GPU. Важна, но очень сложна.

- **2013 — Microsoft Xbox One**
  AMD Jaguar + GCN. Важна.

- **2013 — ARM Cortex-A53**
  ARM64, очень важна для Android/embedded.

- **2014 — ARM Cortex-M4 / M7**
  Микроконтроллеры, важны для embedded-эмуляции.

- **2015 — Intel Skylake**
  x86 microarchitecture.

- **2016 — ARM Cortex-A72**
  Мобильная/встроенная архитектура.

- **2017 — Nintendo Switch**
  NVIDIA Tegra X1, ARM Cortex-A57, GPU. Важна, но сложна.

- **2017 — AMD Ryzen / Zen**
  Современная x86-64.

- **2018 — ARM Cortex-A75 / Cortex-M**
  Мобильные/встроенные.

- **2019 — AMD RDNA GPU**
  Важна для PS5/Xbox Series.

- **2020 — Sony PlayStation 5**
  AMD Zen 2 + RDNA 2. Очень сложная система.

- **2020 — Microsoft Xbox Series X / Series S**
  AMD Zen 2 + RDNA 2.

- **2020 — Apple M1**
  ARM64 + GPU + unified memory. Важна для ARM64-эмуляции.

- **2021 — ARM Cortex-X1**
  Высокопроизводительные ARM.

- **2022 — Apple M2**
  ARM64.

- **2022 — Valve Steam Deck**
  x86-64 handheld, AMD Zen 2 + RDNA 2. Не ретро-консоль, но интересна как PC-подобная система.

---

## Отдельная линия: аркадные платы

Аркадные платы — отдельный огромный пласт. Многие из них проще консолей, но с уникальными видеочипами.

- **1978 — Space Invaders**
  8080 + видеочип. Отличная учебная аркадная система.

- **1980 — Pac-Man**
  Z80 + видео/звук.

- **1981 — Galaga**
  Z80 + видео/звук.

- **1981 — Donkey Kong**
  Z80 + видео/звук.

- **1983 — Dragon’s Lair / LaserDisc games**
  Не классический эмулятор CPU, а симулятор laser-disc + microcontroller.

- **1985 — Bubble Bobble**
  68000 + кастомная графика.

- **1986 — Out Run**
  68000 + кастомная графика.

- **1990 — Neo Geo MVS**
  68000 + Z80 + видеочипы.

- **1991 — Street Fighter II CPS-1**
  68000 + кастомная графика.

- **1993 — CPS-2**
  68000 + кастомная графика.

- **1993 — Sega Model 1**
  PowerPC + 3D GPU.

- **1993 — Namco System 22**
  3D arcade.

- **1996 — Sega Model 3**
  PowerPC + 3D GPU.

- **2004 — Taito Type X**
  PC-based arcade.

---

## Отдельная линия: микроконтроллеры и embedded

Если учебник “всеобъемлющий”, стоит включить embedded-линию. Она часто проще, чем консоли, но учит работе с регистрами, прерываниями, таймерами, UART, SPI, I2C.

- **1976 — Intel 8048**
  Микроконтроллер, много игровых контроллеров.

- **1979 — Zilog Z8**
  Микроконтроллер.

- **1979 — Motorola 68HC05**
  Микроконтроллер.

- **1980 — Intel 8051**
  Один из важнейших микроконтроллеров.

- **1984 — Motorola 68HC11**
  Микроконтроллер.

- **1996 — Atmel AVR**
  AVR, Arduino, много документации.

- **2000 — TI MSP430**
  Low-power MCU.

- **2004 — ARM Cortex-M3**
  Важнейшая embedded-линия.

- **2010 — ARM Cortex-M4**
  DSP instructions.

- **2014 — ARM Cortex-M7**
  Высокопроизводительные MCU.

---

# 2. От простого к сложному: учебная лестница

Это не строго хронологический порядок. Это порядок, в котором я бы рекомендовал изучать системы.

Важно: **“простой CPU” не означает “простая система”**.
Например, NES имеет очень простой CPU, но PPU, APU, mapper и scanline timing делают её непростой.
Mega Drive имеет относительно понятный 68000, но VDP, YM2612, Z80, DMA и тайминги — отдельная инженерная школа.

---

## Уровень 0. Абстрактные машины и концепты

**Цель:** понять, что вообще такое вычислительная машина, инструкция, память, регистры, флаги, цикл выполнения.

- Машина Тьюринга
- Post-Turing machine
- Register machine
- Random-access machine, RAM model
- Simpletron
- Baby Machine
- MiniVM
- Учебная “фон-неймановская игрушка”
- PDP-8 как реальная, но очень простая машина

**Почему сначала:**
Здесь нет консолей, BIOS, прерываний, таймингов, видео. Можно сосредоточиться на fetch-decode-execute, памяти, тестировании, сериализации состояния.

**Пример учебного проекта:**
Своя абстрактная машина в Go: память, регистры, инструкции, флаги, ассемблер, дизассемблер, trace, тесты.

---

## Уровень 1. Простые CPU / ISA без сложной периферии

**Цель:** научиться писать ядро процессора.

- MOS 6502
- MOS 65C02
- WDC 65C816
- Intel 8008
- Intel 8080
- Intel 8085
- Zilog Z80
- Intel 8086
- Intel 8088
- Motorola 68000
- Motorola 6809
- MIPS R3000
- ARM7TDMI

**Почему:**
Это чистые архитектуры, много документации, много тестов. Можно не сразу эмулировать целую систему, а сначала просто CPU + bus.

**Что важно изучать:**
- адресация;
- флаги;
- прерывания;
- reset/NMI;
- self-modifying code;
- cycle timing;
- bus contention;
- endianness;
- signed/unsigned;
- overflow;
- decimal mode;
- instruction encoding.

---

## Уровень 2. Минимальные компьютеры и простые шины

**Цель:** перейти от CPU к машине: память, шина, ввод/вывод, загрузка.

- PDP-8
- PDP-11/34
- PDP-11/40
- Altair 8800
- IMSAI 8080
- Apple I
- простая учебная плата на 6502
- простая учебная плата на Z80
- простая учебная плата на 8086

**Почему:**
Здесь уже есть реальная система, но нет сложной графики и звука. Отлично для изучения:

- memory map;
- I/O ports;
- interrupts;
- DMA;
- boot;
- ROM/RAM;
- console output;
- simple device bus.

---

## Уровень 3. Простые 8-bit компьютеры и консоли

**Цель:** добавить видео, звук, память, ввод, тайминги.

- NES / Famicom
- Game Boy
- Apple II
- Commodore VIC-20
- Commodore 64
- Atari 2600
- Sega Master System
- ZX Spectrum
- BBC Micro
- Pac-Man arcade hardware
- Space Invaders arcade hardware
- Fairchild Channel F

**Почему:**
Это уже “настоящие” системы, но многие из них остаются учебными. NES и Game Boy особенно хороши: CPU простой, но система уже требует понимания scanline, interrupts, audio, video.

**Что важно изучать:**
- frame timing;
- scanline;
- hblank/vblank;
- tilemap;
- sprites;
- palette;
- OAM;
- audio mixing;
- memory banking;
- mappers;
- LCD emulation;
- input polling.

---

## Уровень 4. Продвинутые 8-bit и ранние 16-bit системы

**Цель:** сложные видеочипы, DMA, память, coprocessors.

- Atari 8-bit: 400/800/XL/XE
- Commodore 128
- Apple IIgs
- Commodore Amiga
- Atari ST
- Sega Mega Drive / Genesis
- SNES / Super Famicom
- NEC PC Engine / TurboGrafx-16
- Sega CD
- Neo Geo AES/MVS
- MSX / MSX2
- Sharp X68000
- Sega Game Gear
- Atari 7800

**Почему:**
Здесь уже появляется настоящая инженерная сложность: VDP, DMA, blitter, sound synthesis, coprocessors, memory modes, raster effects.

**Что важно изучать:**
- DMA;
- blitter;
- VDP;
- palette;
- scroll;
- raster interrupts;
- FM synthesis;
- PSG;
- YM2612;
- SPC700;
- coprocessors;
- Super FX;
- SA1;
- DSP1;
- memory banking;
- bus arbitration.

---

## Уровень 5. 32-bit системы

**Цель:** MMU, protected mode, 3D-подобная графика, CD-ROM, сложные SoC.

- Sony PlayStation
- Sega Saturn
- Nintendo 64
- Sega Dreamcast
- Intel 80386
- Intel 80486
- Apple Mac II / Quadra
- Acorn Archimedes
- Amiga 1200 / Amiga 4000
- Atari Falcon
- Sharp X68000
- NEC PC-9801
- FM Towns
- SGI Indigo / Indy / Indigo2
- DEC VAX
- MIPS-based systems
- PowerPC-based systems

**Почему:**
Здесь уже появляются:

- виртуальная память;
- MMU;
- TLB;
- cache;
- 3D geometry;
- CD-ROM;
- DVD;
- сложное аудио;
- многопроцессорные системы;
- GPU pipeline.

**Что важно изучать:**
- GTE;
- RDP;
- RSP;
- PowerVR;
- VDP1/VDP2;
- CD-ROM timing;
- DMA;
- interrupts;
- cache;
- paging;
- FPU;
- 3D rasterization;
- texture mapping;
- z-buffer.

---

## Уровень 6. 64-bit, портативные 3D, современные консоли

**Цель:** сложные SoC, GPU, память, много процессоров, драйверы, JIT.

- Game Boy Advance
- Nintendo DS
- Sony PSP
- Nintendo GameCube
- Microsoft Xbox
- Sony PlayStation 2
- Nintendo Wii
- Microsoft Xbox 360
- Nintendo Wii U

**Почему:**
Эти системы уже требуют понимания производительности, GPU, memory bandwidth, многопоточности, sometimes JIT, security, BIOS, hardware quirks.

**Что важно изучать:**
- ARM9/ARM7;
- MIPS;
- PowerPC;
- x86;
- GPU;
- DMA;
- cache;
- memory protection;
- BIOS;
- security;
- JIT;
- dynamic recompiler;
- audio DSP;
- 3D pipeline;
- texture cache;
- framebuffer;
- state save/load.

---

## Уровень 7. Современные системы и “почти невозможные” проекты

**Цель:** изучать архитектуру, но не обещать полной эмуляции.

- Sony PlayStation 3
- Sony PlayStation 4
- Sony PlayStation 5
- Microsoft Xbox One
- Microsoft Xbox Series X/S
- Nintendo Switch
- Apple M1/M2
- ARM64 SoC
- x86-64 SoC
- Cell BE
- AMD Jaguar
- AMD Zen
- AMD GCN/RDNA
- NVIDIA Tegra
- PowerVR / Mali / Adreno

**Почему это сложно:**
- много ядер;
- GPU-архитектуры;
- проприетарные драйверы;
- безопасность;
- виртуальные машины;
- JIT;
- память;
- кэши;
- синхронизация;
- сетевые функции;
- огромный объём документации.

**Учебная рекомендация:**
Не делать “полный эмулятор PS3” первым или даже пятым проектом. Лучше делать:

- эмулятор одного CPU;
- эмулятор одного GPU-блока;
- эмулятор одного SoC-компонента;
- архитектурную модель;
- partial emulator;
- educational simulator.

---

# 3. Мой рекомендуемый стартовый набор проектов

Если бы я строил такой учебник на годы, я бы рекомендовал примерно такую последовательность:

1. **ToyVM** — абстрактная машина фон Неймана.
2. **6502** — первый реальный CPU.
3. **Z80 / 8080** — второй 8-bit CPU.
4. **8086** — начало x86.
5. **68000** — начало 16/32-bit.
6. **PDP-11** — реальная minicomputer-архитектура.
7. **NES** — первый полноценный игровой эмулятор.
8. **Game Boy** — второй игровой эмулятор.
9. **Apple II** — первый домашний компьютер.
10. **Commodore 64** — cycle-accurate школа.
11. **Mega Drive** — 68000 + VDP + YM2612.
12. **SNES** — 65C816 + SPC700 + DMA + coprocessors.
13. **PlayStation** — MIPS + GTE + GPU + CD.
14. **N64** — MIPS + RDP/RSP.
15. **Dreamcast** — SH-4 + PowerVR + AICA.
16. **GBA / DS** — ARM + multi-CPU.
17. **PS2** — Emotion Engine + GS + IOP.
18. **GameCube / Xbox** — PowerPC / x86 + GPU.
19. **PS3 / PS4 / Xbox 360 / Xbox One / Switch** — архитектурные проекты, не обязательно full accuracy.

---

# 4. Анализ проекта: что важно понять заранее

## 4.1. Проект огромный, но он реален как учебная траектория

Полностью эмулировать все перечисленные системы с высокой точностью — это не проект одного человека за несколько лет. Это десятки профессиональных проектов: MAME, Mednafen, PCSX2, RPCS3, Dolphin, PPSSPP, mGBA, melonDS, Citra, Flycast, VICE, Stella, Mesen, Genesis Plus GX, BlastEm и т.д.

Но как **учебник** проект абсолютно реален.

Нужно не ставить цель “эмулировать всё”, а ставить цель:

> Научить читателя самостоятельно выбрать систему, найти документацию, спроектировать архитектуру, написать CPU, добавить устройства, протестировать, отладить и довести до рабочего состояния.

Тогда 5000 страниц — это не проблема, а преимущество.

---

## 4.2. Нужно разделить уровни эмуляции

Это критически важно.

Я бы в учебнике явно определил уровни:

### 1. Instruction-level emulation

Эмулируется только набор инструкций.

- CPU;
- память;
- регистры;
- флаги.

Подходит для:

- CPU-учебников;
- архитектуры;
- тестов;
- быстрых прототипов.

### 2. Cycle-level emulation

Каждый такт синхронизируется с устройствами.

- CPU;
- bus;
- interrupt;
- DMA;
- video timing;
- audio timing.

Подходит для:

- NES;
- C64;
- ZX Spectrum;
- Game Boy;
- Mega Drive;
- SNES.

### 3. Scanline-level emulation

Синхронизация по строкам растра.

- PPU;
- VDP;
- raster effects;
- midframe changes.

Подходит для:

- NES;
- SNES;
- Mega Drive;
- Master System;
- Game Boy.

### 4. Event-driven emulation

События: прерывание, DMA, vblank, hblank, audio sample.

Подходит для:

- быстрых эмуляторов;
- сложных SoC;
- систем, где cycle-accurate слишком дорого.

### 5. Device-level emulation

Эмулируются отдельные чипы: CPU, GPU, APU, DMA, timer, controller.

Подходит для:

- PSX;
- N64;
- Dreamcast;
- PSP;
- GBA;
- DS.

### 6. Signal-level / transistor-level emulation

Транзисторы, логические вентили, тайминги сигналов.

Подходит для:

- исторических CPU;
- глубокого reverse engineering;
- академических проектов.

Это очень дорого и не нужно для большинства учебных задач.

---

## 4.3. Нужно проектировать “emulator core”, а не набор отдельных эмуляторов

Для огромного учебника важно с самого начала учить архитектуре.

Хорошая структура:

- `cpu` — ядра процессоров;
- `bus` — адресное пространство;
- `memory` — RAM/ROM/MMIO;
- `devices` — чипы;
- `video` — PPU/VDP/GPU;
- `audio` — APU/PSG/FM/PCM;
- `input` — контроллеры;
- `storage` — floppy/hard disk/CD/SD;
- `timing` — event queue, cycle counter;
- `state` — save/load;
- `debug` — trace, breakpoints, memory viewer;
- `frontend` — GUI, SDL, WebAssembly, CLI.

Пример Go-скелета:

```go
package emulator

type Bus interface {
    Read(addr uint32) byte
    Write(addr uint32, val byte)
}

type CPU interface {
    Step() uint64
}

type Emulator struct {
    CPU    CPU
    Bus    Bus
    Cycles uint64
}

func (e *Emulator) RunFor(cycles uint64) {
    for e.Cycles < cycles {
        e.Cycles += e.CPU.Step()
    }
}
```

Для 6502 лучше использовать `uint16` адрес.
Для 68000 — `uint32`.
Для x86-64 — `uint64`.
Не стоит везде использовать `int`, потому что размер `int` платформозависимый, а эмулятор должен быть детерминированным.

---

## 4.4. Go хорош, но нужно понимать его ограничения

Go — отличный язык для учебника:

- простой;
- строгий;
- хороший стандартный пакет `testing`;
- хороший `pprof`;
- хороший `race detector`;
- удобен для CLI, WebAssembly, GUI через cgo;
- хорошо подходит для учебных эмуляторов.

Но для эмуляторов есть нюансы.

### Что в Go хорошо

- чистые CPU-интерпретаторы;
- 8-bit и 16-bit системы;
- NES, Game Boy, 6502, Z80, 68000;
- тесты;
- инструменты;
- frontend;
- WebAssembly;
- save states;
- отладочные утилиты.

### Что в Go сложнее

- динамическая рекомпиляция / JIT;
- очень производительный x86-64 эмулятор;
- GPU-эмуляция;
- многопоточная синхронизация;
- низкие тайминги;
- SIMD;
- тонкая оптимизация горячих путей.

Go позволяет писать производительные эмуляторы, но для PS3/PS4/x86-64 full accuracy Go не будет идеальным выбором без сложных решений.

В учебнике стоит прямо сказать:

> Go — основной язык обучения.
> Для некоторых современных систем мы будем использовать Go как архитектурную модель, frontend, тестовый harness и интерпретатор, а не как идеальный язык для финального высокоскоростного эмулятора.

---

## 4.5. Детерминизм — это закон

Эмулятор должен быть предсказуемым.

В Go важно:

- не использовать `map` там, где важен порядок;
- не использовать `time.Now()` в ядре;
- не использовать `rand` без seed;
- не гонять ядро в нескольких горутинах без явной архитектуры;
- не хранить состояние в глобальных переменных;
- не полагаться на порядок инициализации;
- аккуратно использовать `goroutine` только во frontend.

Ядро эмулятора лучше делать однопоточным.

Frontend может быть многопоточным:

- один поток — эмулятор;
- один — рендеринг;
- один — аудио;
- один — UI;
- один — debug.

Но ядро должно быть детерминированным.

---

## 4.6. Тестирование должно быть частью учебника

Эмулятор без тестов — это хобби-код, который разваливается на второй неделе.

В учебнике нужно подробно показывать:

### Unit tests

Пример: тест ADC, SBC, LDA, STA.

```go
func TestADC(t *testing.T) {
    cpu := NewCPU()
    cpu.A = 0x90
    cpu.Bus.Write(0x0002, 0x69)
    cpu.Bus.Write(0x0001, 0x00)
    cpu.Bus.Write(0x0000, 0x00)

    cpu.Step()

    if cpu.A != 0xF9 {
        t.Fatalf("expected A=0xF9, got 0x%02X", cpu.A)
    }
}
```

### Golden tests

Запуск ROM, сравнение состояния, кадров, звуковых буферов.

### Test ROMs

Для 6502, Z80, x86, NES, Game Boy, PSX и т.д.

### Fuzzing

`go test -fuzz` для bus, memory, disassembler, save/load.

### Race detector

`go test -race` для frontend и многопоточных частей.

### Benchmarks

`go test -bench`.

### Profiling

`go tool pprof`.

### Snapshot tests

Состояние после N циклов, после interrupt, после DMA.

---

## 4.7. Нужно учить читателя читать документацию

Это отдельная глава.

Источники:

- datasheets;
- service manuals;
- schematics;
- netlists;
- BIOS dumps;
- disassemblies;
- community docs;
- open-source emulators;
- errata;
- application notes;
- patents;
- conference papers;
- old magazines;
- forum threads;
- MAME source;
- Mednafen source;
- RetroArch cores.

Важные источники по темам:

### 6502

- MOS 6502 datasheets;
- 6502.org;
- WDC docs;
- Rockwell docs;
- cycle-by-cycle docs;
- 6502 functional test ROMs.

### NES

- nesdev.com;
- NESdev Wiki;
- PPU documentation;
- mapper documentation;
- test ROMs;
- Mesen, FCEUX, Nesten, RetroArch cores.

### Game Boy

- gbdev.io;
- Pandocs;
- GB hardware docs;
- mGBA, Gambatte, SameBoy.

### Z80

- z80.info;
- Zilog docs;
- ZEXALL / ZEXDOC;
- ZX Spectrum docs;
- MSX docs;
- Z80 test suites.

### 68000

- Motorola docs;
- 68k.org;
- 68000 test suites;
- Amiga docs;
- Atari ST docs;
- Mega Drive docs;
- BlastEm, Genesis Plus GX, Picodrive.

### x86

- Intel SDM;
- AMD manuals;
- OSDev Wiki;
- QEMU docs;
- Bochs docs;
- KVM docs;
- test suites.

### PSX

- psx-spx;
- psxdev;
- Mednafen docs;
- PCSX2 docs;
- PlayStation hardware docs.

### N64

- Ultra64 docs;
- RDP/RSP docs;
- Project64 source;
- Mupen64Plus docs.

### Dreamcast

- Dreamcast docs;
- Flycast / Reicast source;
- PowerVR docs;
- SH-4 docs.

### GBA / DS

- gbatek;
- GBA docs;
- melonDS docs;
- mGBA docs;
- Citra docs.

---

## 4.8. Юридический аспект

Это обязательно должно быть в учебнике.

Эмуляторы обычно легальны.

Но:

- BIOS часто защищён авторским правом;
- ROM часто защищён авторским правом;
- “abandonware” не всегда легален;
- распространение чужих ROM/BIOS — опасная зона.

В учебнике нужно учить:

- использовать homebrew;
- использовать public domain;
- использовать ROMs, которые пользователь легально извлёк из собственного оборудования;
- не распространять BIOS/ROM;
- делать тестовые ROMs самому;
- использовать открытые лицензии для своих тестов.

---

# 5. Как учить “мыслить как инженер”: пример проектирования

В каждом уроке должно быть не просто “вот код”, а “вот варианты, вот компромиссы”.

## Пример: как реализовать декодирование инструкций CPU

### Вариант 1: `switch` по opcode

Плюсы:

- просто;
- легко читать;
- хорошо для учебника.

Минусы:

- может быть медленным;
- много кода;
- легко ошибиться в покрытии opcode.

### Вариант 2: таблица обработчиков

Плюсы:

- быстрый dispatch;
- удобно для тестов;
- хорошо масштабируется.

Минусы:

- сложнее отлаживать;
- нужно аккуратно обрабатывать недокументированные режимы.

### Вариант 3: сгенерированный код

Плюсы:

- можно покрыть все инструкции;
- меньше ручных ошибок;
- удобно для больших ISA.

Минусы:

- нужна кодогенерация;
- сложнее читать.

### Вариант 4: микрокод-подобная таблица

Плюсы:

- хорошо для сложных CPU;
- удобно для архитектурных экспериментов.

Минусы:

- медленнее;
- сложнее.

### Вариант 5: JIT / dynamic recompiler

Плюсы:

- быстро;
- подходит для x86, ARM, MIPS.

Минусы:

- сложно;
- безопасность;
- кэш;
- self-modifying code;
- Go не очень удобен для JIT.

В учебнике нужно показывать все варианты и объяснять:

- для 6502 лучше таблица или switch;
- для 68000 таблица;
- для x86 — таблица + оптимизации;
- для ARM — таблица + Thumb/Thumb2;
- для PS3/PS4 — уже нужна сложная архитектура.

---

## Пример: как проектировать тайминг

### Вариант 1: run-to-interrupt

CPU выполняется до прерывания.

Плюсы:

- быстро.

Минусы:

- не подходит для scanline-эффектов.

### Вариант 2: cycle-by-cycle

Каждый такт проверяет устройства.

Плюсы:

- точность.

Минусы:

- медленно.

### Вариант 3: scanline

CPU выполняется до конца строки.

Плюсы:

- хорошо для консолей.

Минусы:

- не всегда достаточно для midframe effects.

### Вариант 4: event queue

События планируются на будущее.

Плюсы:

- гибко;
- подходит для DMA, interrupts, audio.

Минусы:

- сложнее.

### Вариант 5: hybrid

Для CPU — run-to-interrupt, для PPU — scanline, для audio — sample events.

Плюсы:

- реалистичный компромисс.

Минусы:

- нужно аккуратно синхронизировать.

---

## Пример: как проектировать видео

### Вариант 1: framebuffer

Просто рисуем кадр.

Плюсы:

- быстро;
- просто.

Минусы:

- нет scanline-эффектов;
- нет CRT-эффектов.

### Вариант 2: scanline renderer

Рендерим по строкам.

Плюсы:

- хорошо для консолей;
- поддерживает midframe changes.

Минусы:

- сложнее.

### Вариант 3: analog video simulation

Сигнал, color burst, NTSC/PAL, CRT.

Плюсы:

- аутентичность.

Минусы:

- медленно;
- сложно.

### Вариант 4: GPU pipeline emulation

Триангуляция, текстуры, z-buffer, fog, lighting.

Плюсы:

- реалистично для 3D.

Минусы:

- очень сложно.

---

# 6. Подводные камни эмуляторов

В учебнике нужно специально выделить “узкие и скользкие места”.

## CPU

- флаги;
- signed overflow;
- unsigned overflow;
- decimal mode;
- BCD;
- interrupts;
- NMI;
- reset;
- halt;
- self-modifying code;
- cache invalidation;
- pipeline;
- out-of-order;
- FPU;
- NaN;
- denormals;
- rounding modes;
- MMU;
- TLB;
- paging;
- alignment faults;
- endianness;
- undefined opcodes;
- reserved opcodes;
- privilege levels;
- security exceptions.

## Bus и память

- memory map;
- ROM/RAM overlap;
- MMIO;
- banking;
- DMA;
- bus arbitration;
- wait states;
- refresh;
- contention;
- power-on state;
- battery-backed RAM;
- RTC;
- CMOS;
- NVRAM;
- shadow RAM;
- ROM patching;
- save state compatibility.

## Video

- scanline;
- hblank;
- vblank;
- overscan;
- aspect ratio;
- interlace;
- palette;
- tilemap;
- sprites;
- OAM;
- sprite priority;
- sprite limit;
- scroll;
- raster effects;
- DMA;
- framebuffer;
- double buffering;
- CRT;
- NTSC/PAL;
- color artifacts;
- dithering;
- gamma.

## Audio

- sample rate;
- DAC;
- PSG;
- FM;
- PCM;
- LFSR;
- envelope;
- mixing;
- clipping;
- interpolation;
- latency;
- sample-accurate;
- resampling;
- audio events;
- audio DMA.

## Storage

- floppy timing;
- hard disk geometry;
- BIOS disk calls;
- CD-ROM seek;
- CD-ROM read;
- CD-ROM error correction;
- DVD;
- GD-ROM;
- SD;
- flash;
- file systems;
- save states;
- battery save;
- RTC.

## Modern systems

- multicore;
- synchronization;
- GPU drivers;
- shader JIT;
- memory protection;
- hypervisor;
- security;
- cache coherency;
- TLB shootdown;
- virtualization;
- network;
- Bluetooth;
- Wi-Fi;
- online services;
- anti-cheat;
- DRM.

---

# 7. Что я бы добавил в учебник сверх классического плана

## 7.1. Модуль “Обратная инженерия”

Очень важно.

Читатель должен уметь:

- загрузить ROM;
- найти entry point;
- дизассемблировать;
- искать строки;
- искать таблицы;
- искать memory writes;
- делать watchpoints;
- сравнивать состояния;
- диффить кадры;
- писать собственные тестовые ROM;
- читать MAME source;
- читать чужие эмуляторы;
- находить расхождения.

Инструменты:

- Ghidra;
- radare2 / rizin;
- objdump;
- IDA Free;
- custom disassembler;
- MAME debugger;
- Mednafen debugger;
- custom trace tools.

---

## 7.2. Модуль “Аналоговый видеосигнал”

Большинство старых систем — это не просто framebuffer.

Нужно понимать:

- NTSC;
- PAL;
- SECAM;
- RGB;
- YUV;
- composite;
- color burst;
- scanlines;
- interlace;
- aspect ratio;
- CRT phosphor;
- gamma;
- shaders.

Это можно делать не сразу, но в учебнике должно быть.

---

## 7.3. Модуль “Аудио и DSP”

Звук — это не “просто PCM”.

Нужно понимать:

- PSG;
- FM;
- wavetable;
- PCM;
- LFSR;
- envelope;
- DAC;
- mixing;
- sample rate;
- latency;
- resampling;
- audio DMA;
- audio events;
- audio state.

Для Mega Drive — YM2612.
Для SNES — SPC700.
Для NES — 2A03 APU.
Для Game Boy — PPU/APU.
Для PSX — SPU.
Для PS2 — SPU2.

---

## 7.4. Модуль “Сохранение и загрузка состояния”

Save state — это не просто сериализовать struct.

Нужно:

- версия состояния;
- миграция;
- детерминированность;
- таймеры;
- очереди событий;
- audio buffers;
- video state;
- CPU state;
- memory state;
- devices state;
- RNG state;
- RTC state;
- battery save.

---

## 7.5. Модуль “Производительность”

Даже учебный эмулятор должен быть быстрым.

Нужно учить:

- профилирование;
- benchmarks;
- pprof;
- allocation;
- escape analysis;
- interface overhead;
- hot loops;
- lookup tables;
- caching;
- memory access;
- dynamic recompiler;
- JIT;
- multithreading.

---

## 7.6. Модуль “Frontend и инструменты”

Эмулятор без отладчика — это почти бесполезная штука.

Нужно делать:

- CPU trace;
- memory viewer;
- disassembler;
- breakpoint;
- watchpoint;
- palette viewer;
- tile viewer;
- sprite viewer;
- scanline viewer;
- audio waveform;
- input viewer;
- save state;
- rewind;
- cheat;
- game database.

---

## 7.7. Модуль “Многоядерность и SoC”

Для современных систем нужно учить:

- несколько CPU;
- shared memory;
- locks;
- atomics;
- message passing;
- event queue;
- GPU command queue;
- DMA engine;
- cache coherency;
- virtual memory.

Но делать это нужно постепенно.

---

# 8. Рекомендуемая структура учебника

Я бы предложил такую крупную структуру.

## Часть 0. Инженерные основы

- Go для эмуляторов
- детерминизм
- тестирование
- документация
- лицензирование
- работа с ROM и тестами
- инструменты
- pprof
- reverse engineering basics

## Часть 1. Абстрактная машина

- фон Неймановская модель
- память
- регистры
- флаги
- fetch-decode-execute
- ассемблер
- дизассемблер
- тесты
- save/load

## Часть 2. 8-bit CPU

- 6502
- 65C02
- 65C816
- Z80
- 8080
- 8085
- 8086
- 6809

## Часть 3. 16/32-bit CPU

- 68000
- 68010
- 68020
- 68030
- 68040
- 80286
- 80386
- 80486
- Pentium
- MIPS R3000/R4000
- ARM7/ARM9
- PowerPC 601/603/604
- SuperH SH-2/SH-4

## Часть 4. Шины, память, устройства

- bus
- MMIO
- interrupts
- DMA
- timers
- RTC
- banking
- MMU
- cache
- TLB

## Часть 5. 8-bit компьютеры

- Altair 8800
- Apple I
- Apple II
- Commodore PET/VIC-20/C64/C128
- Atari 8-bit
- ZX Spectrum
- BBC Micro
- MSX

## Часть 6. 8-bit консоли

- Atari 2600
- NES
- Game Boy
- Master System
- Game Gear
- Atari 7800

## Часть 7. 16-bit системы

- Mega Drive
- SNES
- Amiga
- Atari ST
- PC Engine
- Neo Geo
- Sega CD
- Apple IIgs

## Часть 8. 32-bit системы

- PlayStation
- Saturn
- N64
- Dreamcast
- x86 PC
- Mac
- Amiga 1200/4000
- Sharp X68000
- PC-98

## Часть 9. Портативные и 64-bit системы

- GBA
- DS
- PSP
- NDS
- 3DS
- PS2
- GameCube
- Xbox
- Wii
- Xbox 360

## Часть 10. Современные системы

- PS3
- PS4
- PS5
- Xbox One
- Xbox Series
- Switch
- ARM64
- x86-64
- Cell
- AMD Jaguar
- AMD Zen
- GPU architectures

## Часть 11. Специальные темы

- GPU emulation
- audio DSP
- analog video
- CD/DVD/GD-ROM
- floppy
- hard disk
- state save/load
- JIT/dynamic recompiler
- multicore
- security
- reverse engineering
- performance
- frontend tools

---

# 9. Что я бы рекомендовал как “ядро” первых двух лет

Если не распыляться, первые два года я бы строил вокруг пяти проектов:

1. **ToyVM**
2. **6502**
3. **NES**
4. **Game Boy**
5. **Mega Drive**

Почему именно так:

- ToyVM даёт абстракцию.
- 6502 даёт первый CPU.
- NES даёт первый полный игровой эмулятор.
- Game Boy даёт второй полный эмулятор, но с другой архитектурой.
- Mega Drive даёт переход к 68000, DMA, VDP, FM-синтезу.

Потом:

6. **Apple II**
7. **Commodore 64**
8. **SNES**
9. **PlayStation**
10. **N64**
11. **Dreamcast**
12. **GBA/DS**
13. **PS2/GameCube/Xbox**

---

# 10. Что я бы не рекомендовал делать рано

Не стоит рано браться за:

- PlayStation 3;
- PlayStation 4;
- PlayStation 5;
- Xbox 360;
- Xbox One;
- Xbox Series;
- Nintendo Switch;
- полный x86-64 эмулятор;
- современный ARM64 с GPU и драйверами;
- Cell BE;
- Xenos GPU;
- RSX GPU;
- RDNA GPU;
- Tegra GPU.

Это не потому, что “нельзя”, а потому что они могут убить мотивацию.

Их лучше изучать как:

- архитектурные обзоры;
- отдельные CPU-ядра;
- отдельные GPU-блоки;
- partial emulators;
- educational simulators;
- сравнительные главы.

---

# 11. Важное дополнение: эмулятор ≠ симулятор

В учебнике нужно чётко разделить:

### Эмулятор

Повторяет поведение системы.

Пример:
6502 читает ROM, выполняет инструкции, пишет в PPU.

### Симулятор

Моделирует систему, но не обязательно на уровне инструкций.

Пример:
ENIAC, Babbage, laser-disc arcade, некоторые аналоговые устройства.

### Архитектурная модель

Повторяет архитектуру, но не точное поведение.

Пример:
упрощённый GPU, упрощённый CPU, учебный SoC.

### Динамический рекомпилятор

Переводит код целевой системы в код хост-системы.

Это уже отдельная дисциплина.

---

# 12. Мой итоговый совет по учебнику

Я бы делал учебник не как “каталог эмуляторов”, а как **школу инженерного мышления**.

Каждая глава должна содержать:

1. **Теория**
   - что такое архитектура;
   - почему так сделано;
   - исторический контекст.

2. **Проектирование**
   - какие есть варианты;
   - компромиссы;
   - что выбрать для учебника;
   - что выбрать для производительности;
   - что выбрать для точности.

3. **Подготовка**
   - где брать документацию;
   - какие тесты использовать;
   - какие открытые эмуляторы посмотреть;
   - что легально, а что нет;
   - как выбрать ROM.

4. **Практика**
   - пошаговая реализация;
   - сначала простой CPU;
   - потом bus;
   - потом interrupts;
   - потом timing;
   - потом devices;
   - потом тесты;
   - потом оптимизации.

5. **Отладка**
   - trace;
   - breakpoints;
   - watchpoints;
   - diff state;
   - golden frames;
   - audio tests.

6. **Альтернативы**
   - как это сделано в MAME;
   - как это сделано в Mednafen;
   - как это сделано в специализированном эмуляторе;
   - почему они отличаются.

7. **Узкие места**
   - undefined behavior;
   - timing;
   - DMA;
   - cache;
   - self-modifying code;
   - state compatibility.

8. **Задания**
   - реализовать инструкцию;
   - добавить interrupt;
   - добавить DMA;
   - добавить save state;
   - написать тест;
   - найти расхождение;
   - оптимизировать горячий цикл.

---

# 13. Короткий вывод

Твой проект абсолютно возможен, если воспринимать его как **многолетнюю инженерную академию**, а не как попытку быстро написать эмуляторы всего.

Наиболее удачная стратегия:

1. Начать с абстрактной машины.
2. Сделать несколько CPU: 6502, Z80/8080, 8086, 68000.
3. Сделать PDP-11 как реальную мини-ЭВМ.
4. Сделать NES и Game Boy как первые игровые системы.
5. Сделать Apple II и C64 как домашние компьютеры.
6. Сделать Mega Drive и SNES как большие 16-bit проекты.
7. Сделать PlayStation, N64, Dreamcast как 32-bit/3D переход.
8. Потом переходить к GBA/DS, PS2, GameCube, Xbox.
9. Современные системы изучать как архитектурные проекты, а не как “полный эмулятор за месяц”.

Go — отличный основной язык для такого учебника, особенно если ты хочешь учить и практиковаться одновременно. Главное — с самого начала учить читателя не копировать код, а проектировать систему, тестировать её, документировать и думать о компромиссах: точность, скорость, сложность, переносимость, расширяемость и юридическая чистота.
