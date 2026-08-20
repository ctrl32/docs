# Roadmap

What is being worked on and what is planned. The order reflects current
priorities and may change; nothing here is a dated promise — a feature
ships when it is solid, and then it appears in [What's new](changelog.md).

## In progress

- **Rung comments** in the ladder editor, and the FBD canvas visually
  divided into numbered networks with comments — the layout every
  PLC programmer expects.
- **Live values in the FBD view while online** — the wires and pins of
  the block diagram showing what the machine is really doing, the same
  way the ladder page already shows power flow.
- The new widget properties (trend curves, gauge thickness and needle,
  alarm-table text size) editable directly in the inspector.

## Planned

- **Motion**: CANopen drive control with a ready-made Lenze i550
  profile — `DRIVE_402` wraps the CiA 402 state machine, `POS_AXIS`
  and `HOME` follow PLCopen naming, ramp positioning with delay
  compensation. EDS import already works; the drive blocks are the
  missing piece.
- **Editor over the network**: online monitoring and diagnostics over
  Ethernet/WiFi, not only over the USB cable (pack upload over the
  network already works today).
- **Production security**: secure boot and flash encryption switched on
  for production panels, so a deployed machine cannot be cloned or
  reflashed by a third party.
- **Retentive data on FRAM** as a turnkey service — microsecond writes,
  practically unlimited endurance, nothing for the project to
  configure.
- **Custom block libraries**: distributing your own FB/FC packages in
  compiled form with versioning and dependency checks — share the
  know-how, keep the source.
- **Editor localization** — the user interface in more languages.

## Under consideration

- Trend history persisted to storage and browsable from the WEBview.
- More display controllers besides the SSD1963 and MIPI-DSI panels.