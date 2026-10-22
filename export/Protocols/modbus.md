---
title: "Modbus"
slug: modbus
section: "Protocols"
order: 305
sidebar_position: 305
generator: tools/docs_export.py
---

# Modbus in ctrl32

!!! tip "New to Modbus itself?"
    Registers, function codes, why `40001` and address 0 are the same
    thing — the protocol has its own page:
    [What Modbus is](/docs/buses/modbus-basics/). This page is the
    configuration reference.

The board is a Modbus **master** — it cyclically reads (and writes) the
registers of the connected devices into the variable table. Two transports
are supported, both at the same time:

| Transport | Physical layer | When |
|:---|:---:|:---|
| **RTU** | RS485 terminals of the board | I/O modules, drives, sensors on a cable |
| **TCP** | Ethernet or WiFi | energy meters with a LAN module, RTU↔TCP gateways, cabinet devices with LAN |

Both directions are covered: the board reads devices as a **master**,
and the *Modbus slave* section further down this page shows it
answering a supervisory system as a server.

## A variable with a Modbus source

Every Modbus variable has: `unit` (device address), `fc` (coil / discrete /
holding / input), `address` (0-based, **not** the 3xxxx/4xxxx notation),
`word_order` (big/little — the word order of 32-bit values) and
optionally `transport: tcp` + `ip` + `port`.

- Without `transport` (or with `transport: rtu`) the variable goes over
  RS485 — the behaviour of older projects does not change.
- `f32`, `u32`, `i32` and `TIME` variables are read from **two**
  registers, and the pair travels in one request. The word order
  differs from vendor to vendor and is the most common source of
  nonsensical values — when importing from the catalog it is set
  correctly for you. A wrong order gives values that are wildly wrong
  rather than slightly wrong, which is how you recognise it.
- Scaling: `value = raw × gain + offset`. Analog variables need a
  **deadband** — without one a noisy value repaints the screen for
  nothing.

### Writing to a device

A variable that has a Modbus source **and** `access: rw` is a
*write-through* variable: when the program, a screen field or a
WEBview page changes it, the board writes the new value to the
device — a coil write for a `bool`, a register write for a number
(both registers in one request for a 32-bit value). A variable
without `access: rw` only displays what the device holds.

- **The master reads before it writes.** At start-up the device is
  the source of truth: a setpoint kept in the device is read first and
  never overwritten by the board's boot value.
- **Writes go out on change**, not on every poll.
- **The cyclic read keeps it honest.** If the device refuses or
  overrides a written value, the next read brings the device's value
  back into the variable, so a screen does not keep showing a number
  the device did not accept.

```yaml
tags:
  - name: cmd_a                     # written TO the device on change
    datatype: bool
    access: rw
    source: { modbus: { transport: tcp, ip: 192.168.0.233, unit: 1,
                        fc: coil, address: 0 } }
  - name: heat_a                    # read only: what the device really does
    datatype: bool
    source: { modbus: { transport: tcp, ip: 192.168.0.233, unit: 1,
                        fc: coil, address: 3 } }
```

## The RS485 line

Modbus RTU runs on the board's RS485 line. In the device tree:

1. Click the **RS485** node and set what the devices on the pair use:
   **baud rate**, **parity** and **stop bits** — every device on one
   pair must agree on all three. The **timeout** is how long the
   master waits for an answer before it counts the device as silent.
2. Right-click **RS485** → add **Modbus RTU master**. The tree grows a
   node for it; every device you add hangs under it.
3. Add one device per slave and give it the **unit address** the
   slave answers to — the address set on the slave itself (a DIP
   switch or its own menu). Two devices on one pair never share a
   unit.

![The line's parameters: baud, parity, stop bits, timeout](img/rs485-page.webp){: .sb-center}

![The Modbus RTU master page: the line it uses and the devices on it](img/rtu-master-page.webp){: .sb-center}

A further slave is simply more variables naming its `unit`; nothing
else changes.

**On a Linux device** the serial port is not a pin of a board but a
setting of the device, and so is the way its RS485 transceiver is
driven. *Online › Prepare a Linux device* writes them: pick the
expansion board and its port comes with it. The same window releases the
port from the login console — a login shell on the same serial port
takes the line away from your devices. Because the port lives in the
device, the same project runs unchanged on a built-in RS485 port or a
USB adapter. See [Buses on a Linux device](/docs/hardware/linux-runtime/#buses-on-a-linux-device).

**One line, one role.** A serial line belongs either to the master or
to the slave. A board can master one line and answer as a slave on
another, but never both on the same pair.

```yaml
tags:
  - name: voltage_l1
    datatype: f32
    source: { modbus: { transport: tcp, ip: 192.168.0.50, port: 502,
                        unit: 1, fc: input, address: 0, word_order: big } }
```

## Limits and behaviour

| Limit | Value | Why |
|:---|:---:|:---|
| Distinct TCP targets (IP:port) per project | **4** | ~6–8 kB of RAM per connection on the ESP32-S3 |
| Variables in total | 512 (an ESP32-P4 board 4 096, a Linux device 20 480) | product limit |

- Variables on the **same IP:port share a single connection** — 20 variables from
  one energy meter is still just 1 target. Different `unit` values on
  the same IP (an RTU↔TCP gateway with several devices behind it) also
  count as 1 target.
- The editor enforces the limit both on import and at compile time — a
  project over the limit is rejected on your desk, not as a stuttering
  board on the equipment.
- **Target outage:** variables hold their last value, one event goes into the
  diagnostic buffer when the target drops out and one when it returns.
  The board reconnects automatically (1 s backoff); polling of the other
  targets keeps running.
- The poller runs outside the PLC cycle — a slow or unreachable Modbus
  device **never extends the logic cycle**.
- The master reports on the device console and in the diagnostic
  buffer what it found and what it did not; a unit that never answers
  is named there with its address.

### Supervising the link

- **`SYS.MB_OK`** (BOOL) is true while every polled Modbus device
  answers — bind a lamp to it, or use it in the program. When one
  device drops out it goes false, and the other devices keep being
  polled. See [Variables](/docs/editor-overview/variables/).
- Because a lost device leaves its variables at their **last value**,
  a program that must react to a dead link uses a **heartbeat**: one
  side toggles a bit (a coil or a register) once a second, the other
  side retriggers a timer on each change. When the timer runs out the
  link is dead — the side at the process drops its outputs to a safe
  state on its own, the panel shows a banner. A lamp bound to the
  heartbeat is itself the proof that data flows: blinking, it does;
  frozen, it does not.

### Modbus TCP addressing

- The master addresses a TCP device **by its IP address**. A device
  that takes its address from DHCP needs a **DHCP reservation** on the
  router — a changed lease, typically after a router restart,
  silently breaks the link.
- When two boards talk over one board's **own access point**, let the
  slave host it: the access-point side of the network is always
  `192.168.4.1`, so the address the master polls can never go stale.

## Catalog of Modbus devices

An "EDS for Modbus": the directory `devices/modbus/*.yaml`, one file =
one device (vendor, model, datasheet, `word_order`) plus a register map
(address, fc, data type, scale, unit, description). The catalog is
curated by ctrl32 and is signed like all the other catalogs.

**Using it in the editor:** the *Modbus RTU master* or *Modbus TCP
master* page → *Add Modbus device…* → pick from the catalog → tick the
registers → choose the transport (RS485 / TCP + IP) → *Import variables*.
The variables get a prefix derived from the model (`sdm630_voltage`), the
right data type, word order and scaling.

In the catalogue today, all with register maps taken from the
official vendor documents:

| Vendor | Meter | Connection |
|:---|:---|:---|
| Eastron | SDM120, SDM630 | 1-ph 45 A / 3-ph 100 A direct |
| WAGO | 879-3000 (4PU/4PS), 879-3040 (2PU CT) | 3-ph 65 A direct / 1A-5A CT, MID |
| inepro | PRO1-Mod, PRO2-Mod | 1-ph 45 A / 100 A direct, MID |
| Schrack | MGX20400 | 3-ph 100 A direct, MID |
| IME | Conto D4-Pd MID (CE4DMID31) | 3-ph 63 A direct, MID |
| F&F | LE-03MQ CT | 3-ph via CT, MID |
| Lumel | NMID33 | 3-ph 100 A direct, MID |
| Selec | EM4M-3P-C-100A | 3-ph 100 A direct |
| Tense | TPM-04SH-DL | 3-ph analyzer via CT |
| YTL | 5299 (DTS353F) | 3-ph 80 A direct, MID |

Each entry's header comments carry the traps the datasheet buries:
which meters report power in **kW** instead of W, whose word order is
unverified, which family has two incompatible register-map
generations. Verify the first physical unit before an installation
depends on it.

### Your own device

A device that is not in the catalog does not have to be written by hand:

1. *Add Modbus device…* → in the right-hand pane (while nothing is
   selected) fill in **vendor** and **model** → *New device*. This
   creates the file `devices/modbus/<vendor>_<model>.yaml` with one
   sample register.
2. In the device window → the **Registers** tab → tick *Edit register
   map*. The row below the table adds registers (name, address, class,
   data type, unit); the `x` on a row deletes a register.
3. *Save to catalog* writes the map back into the `.yaml`.
4. **Create/update variables** makes the variables: one for every
   register that has none (named `prefix_register`), and bindings
   refreshed from the map for the ones that exist — safe to press
   again any time the map changes. The `+` on a row creates just that
   one; typing a name into the *Variable* column names it your way,
   and a renamed variable keeps its name on later updates.

![The register map: the variable column, the prefix and the create button](img/modbus-registers.webp){: .sb-center}

The file is the single source of truth — the project only keeps the
path to it, so the entry appears on disk right away, not only when the
project is saved.

| Rule | Why |
|:---|:---|
| file name `<vendor>_<model>.yaml`, lower-case ASCII | the catalog is versioned in git and must be readable on every OS |
| `uid: 0x0000` for customer entries | the numbered space belongs to the curator, otherwise uids would clash |
| one register per line | the parser reads line by line; a flow map wrapped onto two lines loses everything after the first line |
| renaming a model creates a NEW file | the old one may be used in another project, so it is not deleted |

The manual route remains: copy `devices/modbus/_template.yaml` and fill
in the register map from the device manual.

## Modbus slave — the board answers

The board is not only a master. It can also be a **slave**: a
supervisory SCADA, PLC or Home Assistant reads its state and sends
setpoints. The board still runs **fully without them** — SCADA is a
window to the outside, not a condition for operation.

```yaml
modbus_slave:
  rtu: false        # answer on the RS485 line
  tcp: true         # answer over TCP
  unit: 9           # unit ID of the board
  port: 502
  word_order: big   # word order of 32-bit values
  tags:
    - { tag: boiler_temp }                     # 4x 0-1, read-only
    - { tag: temp_setpoint, writable: true }   # 4x 2-3
    - { tag: pump }                            # 0x 0, bit
```

In the editor: **RS485 → Modbus RTU slave** or **Ethernet → Modbus TCP
slave**. The page shows exactly the map the integrator will read — both
the protocol address and the number from the manual.

### How addresses are assigned

Automatically, in list order: `bool` → coils (0x) from 0, everything
else → holding registers (4x) from 0, where `i32`/`u32`/`f32` take up
**two registers** and the 64-bit kinds (`LINT`, `ULINT`, `LREAL`) **four**. The address goes into the pack **explicitly**, so
reordering variables in the editor does not shift the map. The order in the
list can be changed with the arrow — it is part of the configuration,
not cosmetics.

### Designing the map

- **The board at the process owns its outputs.** Expose a writable
  *command* (a coil) for the master, let the slave's own program
  decide whether the real output follows (interlocks, a sensor
  check), and expose the **real output** read-only beside it. The
  master can show "what I asked" and "what is happening" side by
  side; the gap between them is the interlock speaking, and the slave
  keeps its interlocks when the link dies.
- Mark `writable` only what the master is meant to change — the map
  itself then enforces who owns what.
- There is no separate register map to maintain: the order of the
  list **is** the map.

### A write is a command

A variable without `writable` ticked answers a write with **exception
0x02**; it never passes silently. The same rule as with WebSocket and
MQTT: the board decides about a write, not whoever asks for it.

Further deliberate decisions:

- `FC6` (write single register) on a 32-bit or a 64-bit value is
  **rejected** — a half-written value is worse than a refusal.
- `FC16` first validates the **whole** range and only then writes — a
  half-executed write would leave the equipment in an undefined state.
- Reading a range that lies even partly outside the map returns an
  exception. Zeros would send the integrator looking for the fault at
  their end.
- A broadcast (address 0) on RTU is **executed but not answered** — the
  standard requires it; otherwise two slaves would transmit at once.

### Pitfalls

| Pitfall | Fix |
|:---|:---|
| Master and slave on the same RS485 line | a line has one master — the build **rejects this at your desk** and the editor shows it in red right on the page |
| Wrong word order | `word_order` must match what the SCADA expects — the same trap as on the master side |
| Several SCADA clients at once | the TCP slave serves **one connection**; each further one would cost ~6–8 kB of RAM, which the S3 does not have to spare |
| A client vanishes without closing (power cut, WiFi drop) | nothing to do — an idle connection is dropped after 60 s, so the slot frees itself and the next client gets served |

Diagnostics: the board's status line (the editor's device page, or the
serial command `VUI!` in the terminal) includes
`mbslv=<requests>,<exceptions>`. A growing exception count means the
SCADA is reading outside the map or trying to write to a variable
without permission.

## Typical pitfalls

| Pitfall | Fix |
|:---|:---|
| Nonsensical f32 values | swap `word_order` (big ↔ little) |
| Address off by one | the vendor documentation counts from 1 or uses the 3xxxx notation — in ctrl32 the address is always the 0-based protocol address |
| Device does not answer over RTU | check the baud rate/parity, the A/B wires and the termination |
| TCP target behind NAT or in another segment | the board and the device belong on the same (separate) equipment network |
| No values from a TCP device, or the link stops after a router restart | the device's IP changed — check it with the [device scanner](/docs/deployment/find-devices/) and give the device a DHCP reservation |
| A written value does not stick | the device refused or overrode it, and the cyclic read brought its value back — check the device's own logic or interlock |

### Bringing up an RS485 line

Check in this order:

| # | Check | Symptom when wrong |
|:---:|:---|:---|
| 1 | **A and B swapped** — the commonest fault | silence, not errors |
| 2 | **The unit address** — two slaves with the same unit | they answer together and the master sees noise |
| 3 | **Baud rate, parity, stop bits** — all three, on every device | silence or garbage |
| 4 | **Termination** — 120 ohm at the two ends, nowhere else | works at low baud rates, fails at higher ones |
| 5 | **A login console on the port** (Linux device) | the line is taken — release it in *Prepare a Linux device* |

Wiring and timing are explained on [What Modbus is](/docs/buses/modbus-basics/#wiring-an-rs485-pair).
