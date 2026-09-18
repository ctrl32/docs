# RS-485 system — one master, two slaves

One Modbus RTU master reading and writing two slaves over a single
RS-485 pair, with a frequency drive on the master's CAN beside it. A
**system project**: three devices in one file, deployed as one from the
editor's system page, each device keeping its own program and its own
screens.

**Project:** `examples\rs485_system.prj32`
**Boards:** a reTerminal with the E10-1 expansion (the master), an
inoCORE32-TM8.6 and an inoCORE32-TM1.1 (the slaves)
**Needs:** the three boards on one A/B pair (19200 8N1, a termination
at each end) — the slaves run without the master, the master's screen
shows what answers; the Lenze i550 on the E10-1's CAN terminal is
optional (its lamps simply stay dark)

---

## What it shows

How a Modbus RTU network is written in ctrl32: **the slave says what it
exposes, the master says what it reads** — and nothing else. A slave
lists the variables it puts on the wire; numeric variables take two
holding registers each, in the order listed, and boolean variables one
coil each. A master's variable names the unit, the function and the
register. Every value on the master's screen is a variable like any
other: the setpoint field writes the slave's holding register, the
switch writes its coil, the lamp reads it.

The master is a Linux device. Its serial port and the way its RS-485
transceiver is driven are **settings of the device**, written from the
editor's board window, not lines in the project — the same project
would run on a Raspberry Pi with a USB-RS485 dongle without a change.

---

## The devices

| Device | Board | Role |
|:---|:---|:---|
| `master` | reTerminal + E10-1 | Modbus RTU master of units 1 and 2 on `ttyS0`; CANopen master of the i550 (node 2) on the E10-1's CAN; a 1280×720 screen and a phone page |
| `zones` | inoCORE32-TM8.6 | slave unit 1: three RTD temperatures over its MAX31865 converters, a thermostat per zone, setpoints the master writes |
| `panel_a` | inoCORE32-TM1.1 | slave unit 2: the [TM1.1 example's](examples.md) little machine — the master starts it, reads its counter and its inputs |

### What travels over the pair

The zones slave (unit 1):

| Register | Variable | Direction |
|:---|:---|:---|
| holding 0–1, 2–3, 4–5 | `temp_a`, `temp_b`, `temp_c` | read |
| holding 6–7, 8–9, 10–11 | `sp_a`, `sp_b`, `sp_c` | read and **written** by the master |
| coil 0, 1, 2 | `heat_a`, `heat_b`, `heat_c` | read |

The panel slave (unit 2):

| Register | Variable | Direction |
|:---|:---|:---|
| holding 0–1 | `pieces` | read |
| holding 2–3 | `master_beat` | **written** — the master's seconds, one a second |
| coil 0 | `running` | read |
| coil 1 | `run_cmd` | **written** — the master starts the machine |
| coil 2, 3, 4 | `in_start`, `in_stop`, `in_sensor` | read — the panel's inputs |
| coil 5 | `lamp` | **written** — lit while a zone is over the limit |
| coil 6, 7 | `out_user1`, `out_user2` | **written** |

The master's program is three lines: a heartbeat it writes to the
panel once a second, the average of the three zones, and a limit
that lights the panel's lamp. Everything else is wiring — variables
that name a unit and a register, widgets that name a variable. A third
slave is one more block of variables naming `unit: 3`; nothing else
changes.

---

## Worth copying

- **The slave table.** Listing the variables in the order the master
  expects them, read-only unless `writable: true`, is the whole
  slave. There is no register map to maintain by hand: the order is
  the map.
- **A written variable on the master.** `access: rw` on a variable
  with a Modbus source makes it a write: the field on the screen, the
  program's assignment and a write from a phone all land in the
  slave's register. The master reads the slave's value first and
  writes only on change — a restart never pushes a stale setpoint
  over the slave's own.
- **A heartbeat the slave can watch.** `master_beat` changes once a
  second while the master lives; a slave program that sees it stop
  knows what happened to the line.
- **The drive beside it.** The same device is the CANopen master of
  the i550 — the statusword and the speed are two more variables. The
  drive is watched, not moved: there is no command variable, so
  downloading the project starts nothing.

---

## Something to try

- Change a setpoint on the master's screen and watch the zone's heater
  lamp follow on the slave's phone page.
- Pull the A/B wire from one slave: the master's RS-485 lamp goes out
  (`SYS.MB_OK`), the other slave keeps answering, and the panel's
  `master_beat` stops if it was the panel.
- Give the zones slave its solid-state relays: the project says which
  pins they are (a `gpio` source with `access: rw` is an output).

!!! note "One line, one role"
    A serial line is either the master's or the slave's. A device can
    master one line and answer on another, but never both on the same
    pair — and two masters on one pair talk over each other.
