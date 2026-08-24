# Modbus in ctrl32

!!! tip "New to Modbus itself?"
    Registers, function codes, why `40001` and address 0 are the same
    thing — the protocol has its own page:
    [What Modbus is](modbus-basics.md). This page is the
    configuration reference, and a complete two-board worked example
    is [Two boards over Modbus](tutorial-modbus-pair.md).

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
- `f32`/`u32` variables are read from **two** registers. The word order
  differs from vendor to vendor and is the most common source of
  nonsensical values — when importing from the catalog it is set
  correctly for you.
- Scaling: `value = raw × gain + offset`. Analog variables need a
  **deadband** — without one a noisy value repaints the screen for
  nothing.

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
| Variables in total | 512 | product limit |

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

## Catalog of Modbus devices

An "EDS for Modbus": the directory `devices/modbus/*.yaml`, one file =
one device (vendor, model, datasheet, `word_order`) plus a register map
(address, fc, data type, scale, unit, description). The catalog is
curated by inovaea and is signed like all the other catalogs.

**Using it in the editor:** the *Modbus RTU master* or *Modbus TCP
master* page → *Add Modbus device…* → pick from the catalog → tick the
registers → choose the transport (RS485 / TCP + IP) → *Import variables*.
The variables get a prefix derived from the model (`sdm630_voltage`), the
right data type, word order and scaling.

First entries: **Eastron SDM120** (single-phase meter) and **SDM630**
(three-phase meter).

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
**two registers**. The address goes into the pack **explicitly**, so
reordering variables in the editor does not shift the map. The order in the
list can be changed with the arrow — it is part of the configuration,
not cosmetics.

### A write is a command

A variable without `writable` ticked answers a write with **exception
0x02**; it never passes silently. The same rule as with WebSocket and
MQTT: the board decides about a write, not whoever asks for it.

Further deliberate decisions:

- `FC6` (write single register) on a 32-bit value is **rejected** — a
  half-written value is worse than a refusal.
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
