# Roadmap

What is being worked on and what is planned. The order reflects current
priorities and may change; nothing here is a dated promise — a feature
ships when it is solid, and then it appears in [What's new](changelog.md).

## In progress

- **STM32 targets.** The runtime is no longer tied to Espressif: the
  same VM, variables, Modbus, CANopen, rasteriser and pack format run on an
  STM32F7, and the editor writes the board over SWD. The F7 is running;
  the rest of the family follows, and nothing below 64 kB of RAM will be
  supported.
- **Motion on a real drive.** The blocks exist — `MC_POWER`,
  `MC_MOVEABS`, `MC_HOME` and the rest, with `CO_CIA402` underneath them
  and EDS import to generate the variables. What remains is commissioning
  against a physical Lenze i550: measuring the bus delay, the creep
  phase, and the numbers only a bench can give you. See [Motion
  blocks](blocks-motion.md).

## Planned

- **Production security**: secure boot and flash encryption switched on
  for production boards, so a deployed unit cannot be cloned or
  reflashed by a third party.
- **Compiled block libraries**: your own blocks and libraries exist
  today ([your own function block](own-block.md), *Add library* with the
  drive library that ships). What is planned is distributing them in
  compiled form with versioning and dependency checks — share the
  know-how, keep the source.
- **More editor languages** — the editor speaks English and Slovak
  today (*View → Language*); further languages follow.

## Under consideration

- Trend history persisted to storage and browsable from the WEBview.
- More display controllers besides the SSD1963 and MIPI-DSI boards.

## Recently finished

Moved here out of *In progress* and *Planned*; details in
[What's new](changelog.md).

- **Every function block in pictures**: each block on a rung, in
  Structured Text and on a WEBview screen, drawn from one library
  project that ships with the examples. See [Function
  blocks](blocks.md).
- **+7 — the S7 PLC client**: a panel replaces the operator panel on
  an existing S7 installation over ethernet, the PLC untouched.
  See [+7 (S7 PLC)](plus7.md).
- **The Linux runtime** shipped: Seeed reTerminal and the
  STM32MP157C-DK2 are catalogue devices, with OPC UA on top. See
  [The Linux runtime](linux-runtime.md).
- **Retentive data on FRAM** as a turnkey service — stored
  automatically by what the board has fitted, nothing configured.
- **Rung comments** in the ladder editor, and the FBD canvas divided
  into numbered networks with comments.
- **Live values in the FBD view while online** — wires and pins showing
  what the board is really doing, as the ladder view already did.
- **States and motion on any widget**: three-state colours driven by a
  variable or by one bit of an integer, and a widget that travels a path
  as a value sweeps its range.
- **Vector icons** — sharp at any size, in the board, the editor and the
  browser alike.
- **Online control from the editor canvas**: a button on a screen now
  reaches the running board, not just the editor's own copy of the
  values.
