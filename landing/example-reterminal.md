---
title: reTerminal drive and pair
source: docs/example-reterminal.md
hero: img/example-reterminal-0.webp
---

# A drive, an RS-485 pair and the device itself - on one Linux panel

One Seeed reTerminal drives a Lenze i550 over CANopen, masters two Modbus RTU slaves, watches its own UPS and sensors and raises alarms - on a 1280×720 glass and on a phone.

## Who it is for
- Builders who want one Linux panel to control a drive and talk to remote I/O at once
- Integrators using Lenze i550 drives on CANopen
- Projects that need Modbus RTU slaves on RS-485 beside a drive
- Installations where the panel's own power supply and sensors matter

## What you get
- The whole motor on one screen: speed dial, START/STOP with confirmation, setpoint by keypad or slider, direction, ramps
- Live current, torque, DC link, output frequency and the drive's error code - CANopen objects from the drive's PDOs, each a variable with a gain
- CiA 402 lamps (ready, running, fault, warning) from bits of the statusword
- A two-minute trend
- Two Modbus RTU slaves on the E10-1's RS-485 port: three temperature zones with setpoints written from the panel, and a panel slave that this screen starts
- The device itself: UPS (on battery, charging, pack and supply voltage), accelerometer and light sensor - both as system facts and as chips read over I2C - and the cycle (time, worst, overruns)
- Alarms: drive fault, a zone over its limit, the supply gone, the pair or the CAN interface silent

## How it works
1. The supplied `DRIVE_i550` block runs the CiA 402 state machine over the axis; the screen only reads and writes variables.
2. Diagnostics (`current`, `torque`, `dc_voltage`, `frequency`, `error_code`) are plain variables with a CANopen source and a `gain`; the PDO mapping under `can_devices` says which objects travel.
3. `drive_sw.3`, the statusword's fault bit, goes through an AND block into the `fault` variable that the lamp and the alarm read.
4. The RS-485 pair masters a TM8.6 (three temperature zones) and a TM1.1 panel - the same slaves and registers as the RS-485 system example.
5. The device's serial port, its RS-485 transceiver driving and its CAN interface are settings of the device, written from the editor's board window - not lines in the project.

## Pictures
- ![The drive screen on the reTerminal's glass: the dial, START, the setpoint, the numbers, the trend](img/example-reterminal-0.webp) - One screen, the whole motor
- ![The Zones screen: the three zones of the TM8.6, their setpoints written from here](img/rt-zones.webp) - Zones: the TM8.6's three zones with setpoints written from the panel
- ![The Device screen: the UPS, the chips read twice, and the cycle](img/rt-device.webp) - Device: the UPS, the sensors read twice, the cycle

## Runs on
- Seeed reTerminal (CM4) with the reTerminal E10-1 expansion, 1280×720
- Lenze i550 on the E10-1's CAN terminal (node 2, 500 kbit/s)
- Two Modbus RTU slaves on the RS-485 terminal: inoCORE32-TM8.6 and inoCORE32-TM1.1
- Runs without them: the screens work, the lamps stay dark
- Phone page via WEBview
- The same project family runs on four buses: CANopen, EtherCAT, an RS-485 pair, a SIMATIC over ethernet

## Facts to keep exact
- Safety: the drive starts ONLY after START is pressed AND confirmed - never as a side effect of downloading. Stopping over CANopen is NOT a safety function; the emergency stop belongs on the i550's STO terminals, hard-wired
- i550: node 2, 500 kbit/s
- `confirm: true` on START - a false touch next to a drive happens
- System facts named: `SYS.ON_BATTERY`, `SYS.TILT`, `SYS.LIGHT`
- The system facts cost nothing (the runtime reads them anyway); the project's driver is for values a program needs at full rate
- Try: change a zone setpoint and watch the TM8.6 heater lamp follow; pull the supply plug (battery takes over, alarm appears); add a third slave with one block of variables naming `unit: 3`

## Call to action
Download the ctrl32 editor and open the shipped project `examples\reterminal_example.prj32`.
