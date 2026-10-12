# Финальный всёобъемлющий хронологический список систем для эмуляции

## Метаданные и методология

- **Источники**: оригинальные ответы шести моделей ИИ (ChatGPT, Claude, DeepSeek, Gemini, GLM, Qwen) из директории `1.2_AI_Answers`.
- **Подход**: из каждой модели извлечён раздел с хронологическим списком, объединены все упомянутые системы, устранены дубликаты, зафиксированы различия в названиях и датах.
- **Обозначения моделей**:
  - `GPT` – ChatGPT
  - `CLN` – Claude
  - `DS` – DeepSeek
  - `GEM` – Gemini
  - `GLM` – GLM
  - `QWN` – Qwen
- **Формат записи**: для каждой системы указано каноническое название, год (или диапазон при разногласиях), тип, ключевая архитектура/CPU, модели, упомянувшие систему, и заметка о расхождениях.

## Легенда

| Аббревиатура | Модель |
|---|---|
| GPT | ChatGPT |
| CLN | Claude |
| DS  | DeepSeek |
| GEM | Gemini |
| GLM | GLM |
| QWN | Qwen |

---

## Основной хронологический список

### Эпоха 0: Теоретические модели и учебные архитектуры (вне времени)
| Система | Год | Тип | Архитектура/CPU | Упомянули модели | Примечание |
|---|---|---|---|---|---|
| CHIP‑8 (вымышленный/учебный) | — | Виртуальная машина | — | GPT, CLN, DS, GEM, GLM, QWN | Появляется в начале списка как «вне времени» |
| Von Neumann Machine | — | Теоретическая модель | — | GPT, CLN, DS, GEM, GLM, QWN | — |
| SAP‑1/2/3 | — | Учебные процессоры | — | GPT, CLN, DS, GEM, GLM, QWN | — |
| LC‑3 | — | Учебный процессор | — | GPT, CLN, DS, GEM, GLM, QWN | — |
| Hack (Nand2Tetris) | — | Учебный процессор | — | GPT, CLN, DS, GEM, GLM, QWN | — |
| RISC‑V (RV32I) | — | Открытая ISA | — | GPT, CLN, DS, GEM, GLM, QWN | — |

### Эпоха 1: 1940‑е — Пионеры (ламповые ЭВМ)
| Система | Год | Тип | Архитектура/CPU | Упомянули модели | Примечание |
|---|---|---|---|---|---|
| Zuse Z3 | 1941 | ЭВМ | Электромеханическая | GPT, CLN, DS, GEM, GLM, QWN | — |
| Harvard Mark I | 1944 | ЭВМ | Электромеханическая | GPT, CLN, DS, GEM, GLM, QWN | — |
| ENIAC | 1945 | ЭВМ | Электронная лампа | GPT, CLN, DS, GEM, GLM, QWN | — |
| Manchester Baby (SSEM) | 1948 | ЭВМ | Электронная лампа | GPT, CLN, DS, GEM, GLM, QWN | — |
| EDVAC | 1949 | ЭВМ | Ламповая | GPT, CLN, DS, GEM, GLM, QWN | — |
| EDSAC | 1949 | ЭВМ | Ламповая | GPT, CLN, DS, GEM, GLM, QWN | — |
| Manchester Mark 1 | 1949 | ЭВМ | Ламповая | GPT, CLN, DS, GEM, GLM, QWN | — |
| UNIVAC I | 1951 | ЭВМ | Ламповая | GPT, CLN, DS, GEM, GLM, QWN | — |

### Эпоха 2: 1950‑е — Коммерческие мейнфреймы
| Система | Год | Тип | Архитектура/CPU | Упомянули модели | Примечание |
|---|---|---|---|---|---|
| IBM 701 | 1952 | Мейнфрейм | — | GPT, CLN, DS, GEM, GLM, QWN | — |
| IBM 650 | 1954 | Мейнфрейм | — | DS | Единственная модель, добавляющая эту систему |
| IBM 704 | 1954 | Мейнфрейм | — | GPT, CLN, DS, GEM, GLM, QWN | — |
| IBM 709 | 1957‑1958 | Мейнфрейм | — | GPT, CLN, GEM, GLM, QWN (1958) / DS (1957) | Разница в годе объявления/доставки |
| IBM 7090 | 1958‑1959 | Мейнфрейм | — | GPT, CLN, GEM, GLM, QWN (1959) / DS (1958) | Разница в годе |
| IBM 1401 | 1959 | Мейнфрейм | — | DS | Уникальная упоминание |
| UNIVAC II | 1958 | Мейнфрейм | — | GPT, CLN, DS, GEM, GLM, QWN | — |
| DEC PDP‑1 | 1960 | Миникомпьютер | — | GPT, CLN, DS, GEM, GLM, QWN | — |

### Эпоха 3: 1960‑е — Семейства мейнфреймов и миникомпьютеры
| Система | Год | Тип | Архитектура/CPU | Упомянули модели | Примечание |
|---|---|---|---|---|---|
| IBM 7094 | 1962 | Мейнфрейм | — | GPT, CLN, DS, GLM | GEM и QWN опускают её |
| DEC PDP‑4 | 1962 | Миникомпьютер | — | GPT, CLN, DS, GEM, GLM, QWN | — |
| DEC PDP‑5 | 1963 | Миникомпьютер | — | GPT, CLN, DS, GEM, GLM, QWN | — |
| DEC PDP‑7 | 1964‑1965 | Миникомпьютер | — | CLN (1964) / QWN (1965) | Диапазон лет |
| DEC PDP‑8 | 1965 | Миникомпьютер | — | GPT, CLN, DS, GEM, GLM, QWN | — |
| CDC 6600 | 1964 | Минисуперкомпьютер | — | DS | Единственное упоминание |
| HP 2116 | 1966 | Миникомпьютер | — | DS | — |
| Apollo Guidance Computer (AGC) | 1966 | Специальный | — | CLN | Единственное упоминание |
| БЭСМ‑6 | 1968 | Советская миниЭВМ | — | CLN | — |
| DEC PDP‑9 | 1969 | Миникомпьютер | — | GPT, CLN, DS, GEM, GLM, QWN | — |
| DEC PDP‑10 | 1969 | Миникомпьютер | — | GPT, CLN, DS, GEM, GLM, QWN | — |

### Эпоха 4: 1970‑1975 — PDP‑11 и рождение микропроцессоров
| Система | Год | Тип | Архитектура/CPU | Упомянули модели | Примечание |
|---|---|---|---|---|---|
| PDP‑11 | 1970 | Миникомпьютер | 16‑битная | GPT, CLN, DS, GEM, GLM, QWN | — |
| Intel 4004 | 1971 | Микропроцессор | 4‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |
| Kenbak‑1 | 1971 | Миникомпьютер | 4‑бит | DS | Уникальное упоминание |
| Intel 8008 | 1972 | Микропроцессор | 8‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |
| Pong (аркада) | 1972 | Игровая система | — | CLN | Единственное упоминание |
| Intel 8080 | 1973‑1974 | Микропроцессор | 8‑бит | DS (1973) / остальные (1974) | Разница в годе |
| Motorola 6800 | 1974 | Микропроцессор | 8‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |
| Altair 8800 | 1975 | Миникомпьютер | Intel 8080 | GPT, CLN, DS, GEM, GLM, QWN | — |
| MOS 6502 | 1975 | Микропроцессор | 8‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |

### Эпоха 5: 1976‑1979 — Золотая эра 8‑битных систем
| Система | Год | Тип | Архитектура/CPU | Упомянули модели | Примечание |
|---|---|---|---|---|---|
| KIM‑1 | 1976 | Миникомпьютер | MOS 6502 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Apple I | 1976 | Миникомпьютер | MOS 6502 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Z80 | 1976 | Микропроцессор | 8‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |
| RCA CDP1802 | 1976 | Микропроцессор | 8‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |
| TMS9900 | 1976 | Микропроцессор | 16‑бит | DS | Единственное упоминание |
| CHIP‑8 (реальная VM) | 1977 | Виртуальная машина | — | GPT, CLN, DS, GEM, GLM, QWN | — |
| Apple II | 1977 | Персональный компьютер | MOS 6502 | GPT, CLN, DS, GEM, GLM, QWN | — |
| PET | 1977 | Персональный компьютер | MOS 6502 | GPT, CLN, DS, GEM, GLM, QWN | — |
| TRS‑80 | 1977 | Персональный компьютер | Z80 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Atari 2600 (VCS) | 1977‑1978 | Консоль | 6507 | GPT, CLN, DS, GEM, GLM, QWN | Требует cycle‑accurate эмуляции |
| Motorola 6809 | 1978 | Микропроцессор | 8‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |
| Space Invaders (аппарат) | 1978 | Аркада | — | GPT, CLN, DS, GEM, GLM, QWN | — |
| Intel 8086 | 1978 | Микропроцессор | 16‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |
| Intel 8088 | 1979 | Микропроцессор | 16‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |
| Motorola 68000 | 1979 | Микропроцессор | 16‑/32‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |
| Atari 400/800 | 1979 | Персональный компьютер | 6502 | GPT, CLN, DS, GEM, GLM, QWN | — |
| TI‑99/4A | 1979 | Консоль | TMS9900 | DS | Единственное упоминание |

### Эпоха 6: 1980‑1983 — Расцвет 8‑битных ПК и первые консоли
| Система | Год | Тип | Архитектура/CPU | Упомянули модели | Примечание |
|---|---|---|---|---|---|
| VIC‑20 | 1980 | Персональный компьютер | MOS 6502 | GPT, CLN, DS, GEM, GLM, QWN | — |
| ZX80 | 1980 | Персональный компьютер | Z80 | GPT, DS | — |
| Pac‑Man (аркада) | 1980 | Аркада | — | GPT, CLN, DS, GEM, GLM, QWN | — |
| ZX81 | 1981 | Персональный компьютер | Z80 | GPT, CLN, DS, GEM, GLM, QWN | — |
| IBM PC 5150 | 1981 | Персональный компьютер | 8088 | GPT, CLN, DS, GEM, GLM, QWN | — |
| BBC Micro | 1981 | Персональный компьютер | 6502 | GPT, CLN, DS, GEM, GLM, QWN | — |
| ZX Spectrum | 1982 | Персональный компьютер | Z80 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Commodore 64 | 1982 | Персональный компьютер | 6510 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Intel 80186 | 1982 | Микропроцессор | 16‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |
| Intel 80286 | 1982 | Микропроцессор | 16‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |
| ColecoVision | 1982 | Консоль | Z80 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Atari 5200 | 1982 | Консоль | 6502 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Vectrex | 1982 | Консоль | 6809 | GPT, CLN, DS, GEM, GLM, QWN | — |
| NES / Famicom | 1983 | Консоль | 6502 (Ricoh 2A03) | GPT, CLN, DS, GEM, GLM, QWN | — |
| Sega SG‑1000 | 1983 | Консоль | Z80 | GPT, CLN, DS, GEM, GLM, QWN | — |
| MSX | 1983 | Персональный компьютер | Z80 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Apple Lisa | 1983 | Персональный компьютер | Motorola 68000 | GPT, CLN, DS, GEM, GLM, QWN | — |

### Эпоха 7: 1984‑1988 — 16‑битные ПК и начало 16‑битных консолей
| Система | Год | Тип | Архитектура/CPU | Упомянули модели | Примечание |
|---|---|---|---|---|---|
| Macintosh 128K | 1984 | Персональный компьютер | Motorola 68000 | GPT, CLN, DS, GEM, GLM, QWN | — |
| IBM PC/AT | 1984 | Персональный компьютер | 80286 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Amstrad CPC | 1984 | Персональный компьютер | Z80 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Commodore C128 | 1985 | Персональный компьютер | 8502 (6502‑совместимый) | GPT, CLN, DS, GEM, GLM, QWN | — |
| Amiga 1000 | 1985 | Персональный компьютер | Motorola 68000 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Atari ST | 1985 | Персональный компьютер | Motorola 68000 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Intel 80386 | 1985 | Микропроцессор | 32‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |
| Sega Master System | 1985 | Консоль | Z80 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Acorn ARM2 (Archimedes) | 1987 | Персональный компьютер | ARM2 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Apple IIGS | 1986 | Персональный компьютер | 65C816 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Atari 7800 | 1986 | Консоль | 6502 | GPT, CLN, DS, GEM, GLM, QWN | — |
| PC Engine / TurboGrafx‑16 | 1987 | Консоль | HuC6280 (6502‑совм) | GPT, CLN, DS, GEM, GLM, QWN | — |
| Sharp X68000 | 1987 | Персональный компьютер | Motorola 68000 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Sega Mega Drive / Genesis | 1988 | Консоль | Motorola 68000 | GPT, CLN, DS, GEM, GLM, QWN | — |

### Эпоха 8: 1989‑1993 — Game Boy, 486, SNES и первые 32‑битные консоли
| Система | Год | Тип | Архитектура/CPU | Упомянули модели | Примечание |
|---|---|---|---|---|---|
| Game Boy (DMG) | 1989 | Портативная консоль | Sharp LR35902 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Intel 80486 | 1989 | Микропроцессор | 32‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |
| Atari Lynx | 1989 | Портативная консоль | 65C02 | GPT, CLN, DS, GLM | — |
| Super Nintendo (SNES) | 1990 | Консоль | 65816 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Neo Geo AES / MVS | 1990 | Консоль | 68000 | GPT, CLN, DS, GLM | — |
| Sega Game Gear | 1990 | Портативная консоль | Z80 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Sega CD | 1991 | Устройство CD‑ROM | — | GPT, CLN, GLM | — |
| Sega 32X | 1994 | Аддон‑консоль | 68000 | GPT, CLN, GLM | — |
| Intel Pentium | 1993 | Микропроцессор | 32‑бит | GPT, CLN, DS, GEM, GLM, QWN | — |
| 3DO | 1993 | Консоль | ARM60 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Atari Jaguar | 1993 | Консоль | 64‑бит 6502‑производный | GPT, CLN, DS, GEM, GLM, QWN | — |

### Эпоха 9: 1994‑1999 — 3D‑революция и новые 32‑битные консоли
| Система | Год | Тип | Архитектура/CPU | Упомянули модели | Примечание |
|---|---|---|---|---|---|
| Sony PlayStation (PS1) | 1994 | Консоль | MIPS R3000A | GPT, CLN, DS, GEM, GLM, QWN | — |
| Sega Saturn | 1994 | Консоль | Dual‑CPU SH‑2 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Virtual Boy | 1995 | Консоль | 32‑бит | DS, GLM | — |
| Nintendo 64 | 1996 | Консоль | MIPS R4300i | GPT, CLN, DS, GEM, GLM, QWN | — |
| Dreamcast | 1998 | Консоль | SH‑4 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Game Boy Color | 1998 | Портативная консоль | Sharp LR35902 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Neo Geo Pocket / WonderSwan | 1998‑1999 | Портативные консоли | 68000 | GLM | Единственное упоминание |

### Эпоха 10: 2000‑2006 — Шестое поколение (PS2, GameCube, Xbox, GBA, DS, PSP)
| Система | Год | Тип | Архитектура/CPU | Упомянули модели | Примечание |
|---|---|---|---|---|---|
| PlayStation 2 (PS2) | 2000 | Консоль | Emotion Engine (MIPS) | GPT, CLN, DS, GEM, GLM, QWN | — |
| Game Boy Advance (GBA) | 2001 | Портативная консоль | ARM7TDMI | GPT, CLN, DS, GEM, GLM, QWN | — |
| Nintendo GameCube | 2001 | Консоль | IBM PowerPC Gekko | GPT, CLN, DS, GEM, GLM, QWN | — |
| Xbox (Original) | 2001 | Консоль | Intel Pentium III | GPT, CLN, DS, GEM, GLM, QWN | — |
| Nintendo DS | 2004 | Портативная консоль | ARM9/7 | GPT, CLN, DS, GEM, GLM, QWN | — |
| PlayStation Portable (PSP) | 2004 | Портативная консоль | MIPS R4000 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Xbox 360 | 2005 | Консоль | PowerPC Xenon | GPT, CLN, DS, GEM, GLM, QWN | — |
| PlayStation 3 (PS3) | 2006 | Консоль | Cell BE | GPT, CLN, DS, GEM, GLM, QWN | — |
| Wii | 2006 | Консоль | PowerPC Broadway | GPT, CLN, DS, GEM, GLM, QWN | — |

### Эпоха 11: 2011‑2017 — Поколения 7‑8 (3DS, Vita, Wii U, PS4, Xbox One, Switch)
| Система | Год | Тип | Архитектура/CPU | Упомянули модели | Примечание |
|---|---|---|---|---|---|
| Nintendo 3DS | 2011 | Портативная консоль | ARM11 | GPT, CLN, DS, GEM, GLM, QWN | — |
| PlayStation Vita | 2011 | Портативная консоль | ARM Cortex‑A9 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Wii U | 2012 | Консоль | IBM PowerPC | CLN, DS | — |
| PlayStation 4 (PS4) | 2013 | Консоль | x86‑64 (AMD Jaguar) | GPT, CLN, DS, GEM, GLM, QWN | — |
| Xbox One | 2013 | Консоль | x86‑64 | GPT, CLN, DS, GEM, GLM, QWN | — |
| Nintendo Switch | 2017 | Консоль | ARM Cortex‑A57 | GPT, CLN, DS, GEM, GLM, QWN | — |

### Эпоха 12: 2020‑2025 — Поколение 9 и перспективы
| Система | Год | Тип | Архитектура/CPU | Упомянули модели | Примечание |
|---|---|---|---|---|---|
| PlayStation 5 (PS5) | 2020 | Консоль | AMD Zen 2 + RDNA 2 GPU | CLN, DS | — |
| Xbox Series X/S | 2020 | Консоль | AMD Zen 2 + RDNA 2 GPU | CLN, DS | — |
| Nintendo Switch 2 (или «Switch Pro») | 2025 | Консоль | ARM Cortex‑X2 | CLN | — |

## Таблица расхождений между моделями

| Система | Год (модели) | Отличия в названиях | Заметки |
|---|---|---|---|
| IBM 709 | 1957 (DS) vs 1958 (остальные) | — | Разница в объявлении vs поставке |
| IBM 7090 | 1958 (DS) vs 1959 (остальные) | — | — |
| Intel 8080 | 1973 (DS) vs 1974 (остальные) | — | — |
| PDP‑7 | 1964 (CLN) vs 1965 (QWN) | — | — |
| Kenbak‑1 | 1971 (только DS) | — | Единственное упоминание |
| IBM 650, IBM 1401, CDC 6600, HP 2116, AGC, БЭСМ‑6, TMS9900, TI‑99/4A | Уникальные для отдельных моделей | — | Добавлены в финальный список как редкие, но важные этапы |

---

*Файл готов к использованию в учебном проекте.*
