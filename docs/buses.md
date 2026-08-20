# Buses and peripherals

The panel speaks Modbus on RS485 and Ethernet, raw CAN frames, MQTT for
telemetry — and drives local chips over I2C and SPI. Every bus ends in
the same place: the tag table. A value that arrived over Modbus looks
exactly like one measured on a local pin, and the logic does not care
which it was.

- [Modbus](modbus.md) — RTU and TCP, master and slave, with a catalog of
  ready-made devices
- [Raw CAN](rawcan.md) — mapping CAN frames straight onto tags
- [MQTT](mqtt.md) — telemetry into ThingsBoard, OpenRemote or Home
  Assistant
- [Peripherals and services](peripherals-and-services.md) — expanders,
  converters, RTC time and the other on-board services
- [Adding a peripheral](adding-peripherals.md) — the two-minute
  click-through, recorded
