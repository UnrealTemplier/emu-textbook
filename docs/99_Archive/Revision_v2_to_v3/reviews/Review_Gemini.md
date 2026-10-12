# Анализ пересечений и дублирований между разделами М0, М1 и М2 в Final_Progression_v3.md

В текущей версии документа [Final_Progression_v3.md](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md) между разделами **М0**, **М1** и **М2** присутствуют серьёзные тематические пересечения, концептуальные дублирования и прямой конфликт версий.

Основная причина коллизий — **асинхронное обновление модулей**:
* **М0** был развёрнут в масштабную энциклопедическую базу из 15 подразделов (собственная история с древности до XXI века, подробная архитектура, схемотехника, практика ALU и старт встроенного отладчика).
* **М1** получил обновлённую расширенную структуру: вобрал в себя не только учебные виртуальные машины (CHIP-8, SAP-1..3, Hack, LC-3, RV32I) и темы памяти (бывший `Memory Lab`), но и полноценную эмуляцию первых исторических stored-program ЭВМ (Manchester Baby, EDSAC, IAS).
* **М2** при этом остался в старой версии (v2), из-за чего оказался фактически «поглощён» и продублирован модулем М1.

---

## 1. Критический конфликт: М1 vs М2 (Прямое дублирование систем)

Это самое сильное противоречие в документе: машины, полноценно эмулируемые в М1, в М2 объявляются заново.

1. **Manchester Baby (SSEM, 1948)**:
   - В [М1.7](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1190) выделен отдельный подраздел из **7 практических уроков** с детальной разработкой эмулятора (история, архитектура, ISA, память Williams tube, цикл выполнения, эмуляция, тесты, сравнение с SAP).
   - В [М2.1](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1851) машина заявлена заново: *«Трубка Уильямса как оперативная память, 7 инструкций, первая программа с хранением в памяти, простейший реальный fetch/execute»*.

2. **EDSAC (1949)**:
   - В [М1.8](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1257) выделен отдельный подраздел из **7 уроков** с разработкой эмулятора (история, архитектура, ISA, delay-line memory, Initial Orders, подпрограммы, эмуляция).
   - В [М2.3](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1860) машина объявляется снова: *«EDSAC (1949), EDVAC (1949) — первые двоичные хранимые программы, сравнение с Manchester Baby»*.

3. **ENIAC, EDVAC, Manchester Mark 1**:
   - В [М1.1 (урок 06)](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L817) они подробно разбираются концептуально в уроке *«06. Первые электронные реализации.md»*.
   - В [М2.2, М2.3, Д2а](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1856-L1864) они повторно идут как основные и факультативные темы модуля М2.

4. **Смысловой разрыв на стыке М1 → М2**:
   - В финальном уроке М1 ([М1.15, урок 08 «Переход к M2.md»](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1834)) заявлено: *«От учебных машин к реальным процессорам: усложнение ISA, реальные периферийные устройства, тайминг, interrupts, DMA...»*. То есть урок явно готовит читателя к **микропроцессорам** (уровня Intel 8080 / MOS 6502).
   - Однако следующий за ним раздел [М2](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1847) возвращает читателя назад к ламповым машинам конца 1940-х годов, которые в М1 студент **уже написал**.

5. **Анахронизм в `LAB: CPU Lab` (между М2 и М3)**:
   - В [LAB: CPU Lab](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1870) предлагается практика: *«рефакторинг CHIP‑8 интерпретатора: switch → func-table, сравнение производительности через testing.B»*.
   - К этому моменту читатель уже написал CHIP-8 (М1.2), генератор декодера на `go:generate` (М1.3) и ещё 8 эмуляторов (SAP-1..3, Baby, EDSAC, IAS, Hack, LC-3, RV32I). Возвращаться к рефакторингу первого CHIP-8 после М2 нелогично.
   - Кроме того, правило М1 прямо гласит: *«Никаких LAB как самостоятельного уровня. Практика интегрирована непосредственно в соответствующие уроки»*.

---

## 2. Пересечения: М0 vs М1 (Теоретическая база vs Вводная часть практики)

1. **История Бэббиджа, Тьюринга и Поста**:
   - **М0.1** ([уроки 09, 10, 11, 14](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L104)): подробно разобраны Бэббидж, Лавлейс, Аналитическая машина, перфокарты, машина Тьюринга, машина Поста, фон Нейман.
   - **М1.1** ([уроки 01, 02, 03](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L751)): снова идут уроки «01. Механические вычислительные машины.md» (Бэббидж, перфокарты), «02. Абстрактная машина Тьюринга.md», «03. Пост и формальные системы.md».
   - *Разница*: В М0 это исторический контекст, а в М1.1 — вводная цепочка к понятию виртуальной машины. Но фактологический материал полностью дублируется.

2. **Модель фон Неймана и цикл Fetch / Decode / Execute**:
   - **М0.5** ([уроки 01, 03](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L250)): модель фон Неймана, память, АЛУ, УУ, PC, SP, регистры, цикл команды (Fetch, Decode, Execute), адресация.
   - **М1.1** ([уроки 04, 05](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L785)): идея хранимой программы, Fetch/Decode/Execute, абстрактная фон-неймановская машина (АЛУ, УУ, PC, IR, цикл выполнения инструкции).
   - **М1.4** ([SAP-1, уроки 02, 05](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L947)): снова тот же фон-неймановский цикл и узлы: ALU, Accumulator, PC, IR, Controller.

3. **Классификация архитектур (Аккумуляторная / Регистровая / Стековая)**:
   - В [М0.5.01](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L252) даются основы архитектуры и регистров.
   - В [М1.1.05](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L804) разбираются: *«Аккумуляторная архитектура, Регистровая архитектура, Стековая архитектура»*.
   - В [LAB: CPU Lab](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1873) тема звучит в третий раз: *«Аккумуляторная, регистровая, стековая архитектуры — сравнение»*.

4. **Память, Endianness, Memory Map, MMIO и Bus**:
   - В [М0.5](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L264) (уроки 02, 04): организация шин, MMIO vs Port I/O, Little-endian vs Big-endian, выравнивание данных, виртуальная память.
   - В [М1.10](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1393) («Память как часть архитектуры»): уроки 01–07 подробно разбирают адресацию, Endianness, Memory Map, mirroring, open bus, bank switching, MMIO и Bus.
   - *Разница*: В М0 это вводная теория, а в М1.10 — обобщение практического опыта эмуляции предыдущих машин (SAP, Baby, EDSAC, IAS). Темы концептуально идентичны.

5. **ALU и флаги**:
   - В [М0.4.03](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L240) и [М0.14](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L663) (практика): проектирование 8-битного ALU, операции сложения/вычитания/логики, флаги Z/N/C/V, табличные тесты.
   - В [М1.4 (SAP-1)](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L947) и [М1.11 (Hack)](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1460): аналогичные блоки ALU и флаги снова эмулируются программно.
   - В [LAB: CPU Lab](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1877): снова пункт *«Флаги АЛУ: Z, N, C, V/O — точная семантика в разных ISA»*.

6. **Отладчик (Debugger)**:
   - В [М0.15](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L703): проект-спутник стартует с дампа регистров, дампа памяти (hex+ASCII), истории инструкций и трейса.
   - В [М1.2 (урок 08)](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L893): подраздел называется *«Первый отладчик»* и формулирует те же темы (*Register dump, Memory dump, Hex + ASCII, Step execution, Instruction trace, Breakpoints, Почему отладчик нужен уже на первом эмуляторе*), как будто в М0 отладчика ещё не было.
   - В [М1.14 (урок 06)](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1739): тема повторяется как *«Debugger как сквозной инструмент»*.

7. **Теория ассемблера**:
   - В [М0.8](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L364): синтаксис assembly, двухпроходный ассемблер, таблицы символов, метки.
   - В [М1.11.06](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1508) и [М1.12.07](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1596): те же концепции двухпроходного ассемблера разбираются для Hack и LC-3.

---

## 3. Пересечения: М0 vs М2 (История ранних машин)

- В [М0.1.11](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L123) («XX век») и [М0.1.14](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L159) («Великие люди эпох»): упоминаются ENIAC, EDVAC, Zuse Z3, Уилкс (EDSAC), Уильямс и Килберн (Baby).
- В [М2](file:///home/ut/work/emu-textbook/docs/Ideas/1.3_Final_Results/Final_Progression_v3.md#L1847) даётся краткая историческая справка по тем же самым машинам.

---

## Сводная таблица коллизий и рекомендации

| Узел коллизии | Где встречается | Характер проблемы | Рекомендованное решение |
|---|---|---|---|
| **Baby, EDSAC, IAS** | М1.7, М1.8, М1.9 **vs** М2.1, М2.3 | **Прямой дубль эмуляторов.** В М2 они заявлены так, будто ещё не изучались. | При обновлении М2 полностью исключить Baby и EDSAC (так как они уже в М1). Пересобрать М2 под другие ранние/специфичные ЭВМ (например, ENIAC, Z3, Harvard Mark I, Whirlwind) либо перенумеровать модули. |
| **Переход М1 → М2** | М1.15.08 **vs** М2 | **Рассинхрон траектории.** Урок М1.15.08 готовит к реальным CPU (8080/6502), а М2 даёт ламповые машины 40-х. | Синхронизировать содержание М2 с анонсом в М1.15.08 (либо сделать микропроцессоры следующим шагом). |
| **`LAB: CPU Lab`** | Между М2 и М3 | **Анахронизм.** Рефакторинг CHIP-8 и сравнение типов ISA после того, как в М1 написано 9 эмуляторов. | Убрать отдельный LAB (согласно структурному правилу М1), а сравнение диспетчеризации опкодов перенести в М1.3 / М1.14 или на реальные CPU в М3. |
| **История (Бэббидж/Тьюринг)** | М0.1 **vs** М1.1 | **Дублирование контекста.** М1.1 пересказывает историю из М0.1. | В М1.1 убрать общеисторический пересказ и сосредоточиться исключительно на формальной модели вычислений и переходе от абстрактной модели к программной. |
| **Отладчик** | М0.15 **vs** М1.2.08 **vs** М1.14.06 | **Терминологический рассинхрон.** В М1.2 он назван «первым», хотя в М0.15 уже был создан. | Скорректировать акцент в М1.2.08: не «создание первого отладчика с нуля», а «адаптация отладчика из М0 к CPU/памяти CHIP-8». |
| **Память и MMIO** | М0.5.02/04 **vs** М1.10 | **Дублирование понятий.** | В М0.5 оставить только высокоуровневые определения, а всю детальную механику (open bus, mirroring, bank switching, MMIO dispatch) закрепить за М1.10 на практике. |
