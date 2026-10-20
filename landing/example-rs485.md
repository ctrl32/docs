---
title: RS-485 system, one master
source: docs/example-rs485.md
hero: img/rt-zones.webp
---

# A Modbus RTU network where the order of the variables is the register map

One master reads and writes two slaves over a single RS-485 pair, with a frequency drive on its CAN beside it - three devices in one system project, deployed as one from the editor.

## Who it is for
- Builders who distribute I/O over RS-485 and Modbus RTU
- Integrators tired of maintaining register maps by hand on both sides
- Projects combining a Linux panel with ESP32 controllers
- Anyone who wants several devices in one file, deployed together

## What you get
- A system project: three devices in one file, each with its own program and screens, deployed as one from the editor's system page
- The slave says what it exposes, the master says what it reads - nothing else
- No register map to maintain: numeric variables take two holding registers each, in the order listed; boolean variables one coil each
- Writes from the master: `access: rw` on a Modbus variable - the screen field, the program and a phone write all land in the slave's register
- The master reads the slave's value first and writes only on change, so a restart never pushes a stale setpoint over the slave's own
- A heartbeat (`master_beat`) the slave can watch to know the line is alive
- A Lenze i550 on the master's CAN, watched but not moved - downloading starts nothing
- An RS-485 status lamp (`SYS.MB_OK`)

## How it works
1. `master`: a reTerminal + E10-1, Modbus RTU master of units 1 and 2 on `ttyS0`, CANopen master of the i550 (node 2), with a 1280×720 screen and a phone page.
2. `zones`: an inoCORE32-TM8.6, slave unit 1 - three RTD temperatures over its MAX31865 converters, a thermostat per zone, setpoints the master writes.
3. `panel_a`: an inoCORE32-TM1.1, slave unit 2 - the small application of the TM1.1 example, which the master starts, reading its counter and its inputs.
4. The master's program is three lines: a heartbeat written to the panel once a second, the average of the three zones, and a limit that lights the panel's lamp.
5. The serial port and the RS-485 transceiver driving are settings of the device, written from the editor's board window - the same project runs on a Raspberry Pi with a USB-RS485 dongle without a change.

## Pictures
- ![The master's screen: both slaves, their values and the commands written back](img/rt-zones.webp) - The master's screen: every slave on one picture, values and commands written back

## Runs on
- Master: Seeed reTerminal with the E10-1 expansion (Linux); also a Raspberry Pi with a USB-RS485 dongle
- Slaves: inoCORE32-TM8.6 and inoCORE32-TM1.1
- One A/B pair, 19200 8N1, a termination at each end
- Optional: Lenze i550 on the E10-1's CAN terminal (its lamps stay dark without it)
- The slaves run without the master; the master's screen shows what answers

## Facts to keep exact
- Line: 19200 8N1, termination at each end
- Zones slave (unit 1): holding 0-1, 2-3, 4-5 = `temp_a`, `temp_b`, `temp_c` (read); holding 6-7, 8-9, 10-11 = `sp_a`, `sp_b`, `sp_c` (read and written); coil 0, 1, 2 = `heat_a`, `heat_b`, `heat_c` (read)
- Panel slave (unit 2): holding 0-1 `pieces` (read); holding 2-3 `master_beat` (written, the master's seconds, one a second); coil 0 `running` (read); coil 1 `run_cmd` (written, the master starts it); coils 2, 3, 4 `in_start`, `in_stop`, `in_sensor` (read); coil 5 `lamp` (written, lit while a zone is over the limit); coils 6, 7 `out_user1`, `out_user2` (written)
- Slave variables are read-only unless `writable: true`
- i550 on CAN: node 2; the statusword and the speed are two more variables; no command variable
- A third slave is one more block of variables naming `unit: 3`
- One line, one role: a serial line is either the master's or the slave's; a device can master one line and answer on another, never both on the same pair; two masters on one pair talk over each other
- Try: change a setpoint on the master and watch the heater lamp follow on the slave's phone page; pull A/B from one slave (`SYS.MB_OK` lamp goes out, the other slave keeps answering, `master_beat` stops on the panel); give the zones slave solid-state relays (a `gpio` source with `access: rw` is an output)

## Call to action
Download the ctrl32 editor and open the shipped system project `examples\rs485_system.prj32`.
