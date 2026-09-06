# What Modbus is

Modbus is the oldest fieldbus still in daily use — published in 1979
for Modicon PLCs, and alive today for one reason: it is **simple
enough that everything speaks it**. Energy meters, drives, I/O
modules, SCADA packages, one-euro temperature transmitters — if an
industrial device has a communication port at all, Modbus is the
protocol it is most likely to offer.

This page explains the protocol itself: what the registers are, why
the same register has three different numbers in three different
manuals, and where the classic traps come from. How to configure it
in a project is on [Modbus](modbus.md).

---

## One master asks, slaves answer

Modbus is a **request–response** protocol. One side — the **master**
(TCP manuals say *client*) — sends a request: *"device 1, give me 2
registers from address 0."* The addressed **slave** (*server*)
answers with the values, or with an error. That is the whole
protocol. There are no events, no subscriptions, no device discovery:
**a slave never speaks unless asked**, and everything the master
knows, it knows because it keeps asking.

That simplicity carries consequences worth knowing:

| Modbus has no… | So in practice… |
|:---|:---|
| discovery | you must be told the address and the map — nothing announces itself |
| data types on the wire | a register is 16 bits, full stop; what they *mean* comes from the device manual |
| units or names | register 12 is just register 12 — the map in the manual is the contract |
| events | fresh data costs a poll; the master decides the rate |

A device is therefore only usable together with its **register map**
— the table in its manual saying which address holds what. Reading a
Modbus manual *is* the skill; the rest is configuration.

---

## The four tables

A slave exposes up to four separate data tables. Two hold **bits**,
two hold **16-bit registers**; two are read-only, two writable:

| Table | Holds | Access | Classic prefix | Typical content |
|:---|:---|:---|:---:|:---|
| **Coils** | bits | read + write | `0x` | outputs, commands, enable flags |
| **Discrete inputs** | bits | read only | `1x` | input terminals, status bits |
| **Input registers** | 16-bit words | read only | `3x` | measurements |
| **Holding registers** | 16-bit words | read + write | `4x` | setpoints, parameters, and in practice measurements too |

The names are historical — a "coil" was literally a relay coil in
1979. Do not read meaning into them beyond the access rules: many
devices put measurements into *holding* registers simply because one
table is easier to implement than two.

Each table has its own address space starting at **0**. Coil 3 and
holding register 3 are different things in different tables — the
request says which table it wants via the function code.

## Function codes

The request carries a **function code** — table + operation in one
number. The handful you will actually meet:

| FC | Does | On table |
|:---:|:---|:---|
| 1 | read bits | coils |
| 2 | read bits | discrete inputs |
| 3 | read registers | holding |
| 4 | read registers | input |
| 5 | write one bit | coils |
| 6 | write one register | holding |
| 15 | write several bits | coils |
| 16 | write several registers | holding |

When something is wrong, the slave answers with an **exception**
instead of data:

| Exception | Meaning | What it usually tells you |
|:---:|:---|:---|
| 01 | illegal function | the device does not support that FC |
| 02 | illegal data address | you are reading outside its map — check the addressing notation below |
| 03 | illegal data value | write refused: out of range, or the register is read-only |
| 04 | slave device failure | the device took the request and failed internally |

An exception is the *good* failure mode: the device answered and told
you why. **No answer at all** is the wiring/baud-rate/address class
of problem, not the map class.

---

## Why the same register has three numbers

The single largest source of Modbus confusion — and of "address off
by one" bugs — is that three addressing notations coexist, and every
manual picks one without saying so.

**On the wire** the address is a plain number counted **from 0**
within one table. This is the *protocol address* — the only one the
devices themselves ever see.

**In manuals** you will meet two older conventions built on top:

- **1-based counting** — the first register is called "1", so the
  manual's register 1 is protocol address 0, and everything is
  shifted by one.
- **The 5-digit notation** — the table prefix glued onto the 1-based
  number: `40001` means "holding register, the first one" (protocol
  address 0). `30007` is input register, protocol address 6.

The same physical register, spelled every way it can be:

| Protocol address (ctrl32) | 5-digit notation | 1-based manual | IEC address |
|:---:|:---:|:---:|:---:|
| holding 0 | 40001 | register 1 | `%MW0` |
| holding 6 | 40007 | register 7 | `%MW6` |
| input 2 | 30003 | register 3 | — |
| coil 3 | 00004 | coil 4 | `%MX3` |

The **IEC column** is the fourth spelling, from the PLC world:
IEC 61131 addresses like `%MW100` (memory word) or `%MX10` (memory
bit). Some PLC vendors document their Modbus maps in it; it counts
from 0, like the protocol.

!!! note "ctrl32 always uses the protocol address"
    Everywhere in ctrl32 — a variable's `address:`, the slave map,
    the device catalog — the number is the **0-based protocol
    address**. When a manual says `40123`, strip the `4` and subtract
    one: `address: 122`, function code *holding*. The editor's map
    pages print both spellings side by side so the integrator on the
    other end can check against their manual either way:

![The Modbus slave map in the editor: every row shows the protocol address and the manual number — 4x 0-1 (40001), 0x 3 (4)](img/modbus-slave-map.png){: .sb-center}

The symptom of getting this wrong is precise: **everything is off by
exactly one register**, or the device answers exception 02 at the
edge of its map. When a value looks shifted, try the neighbouring
address before suspecting anything else.

---

## Registers are 16 bits — bigger values are a convention

The protocol moves 16-bit words. Everything larger is an agreement
between the two ends, not a feature of Modbus:

- A **32-bit value** (`f32`, `u32`, `i32`) occupies **two
  consecutive registers**, and the protocol does not say which half
  comes first. That is the **word order** — *big* (high word first)
  or *little* — and it genuinely differs from vendor to vendor.
  Getting it wrong produces values that are not shifted but
  **nonsense**: astronomically large, absurdly small, or jumping
  wildly while the true value barely moves. It is the most common
  Modbus fault in the field.
- **Scaling** is a convention too. A register holding `235` may mean
  23.5 °C (×0.1) or 235 V (×1) — the manual's scale factor becomes
  `gain`/`offset` on the variable.
- **Signed vs unsigned** is again the manual's word: the wire cannot
  tell −1 from 65535.

---

## RTU and TCP

The same protocol travels two ways, and a device usually offers one:

| | Modbus RTU | Modbus TCP |
|:---|:---|:---|
| carried by | RS485 twisted pair | Ethernet or WiFi |
| framing | silence gaps + CRC16 | a 6-byte header (MBAP), no CRC — TCP already guarantees integrity |
| device address | **unit ID 1–247**, set on the device | the **IP address**; the unit ID usually ignored (1) |
| topology | one master, up to 32 devices on one cable pair | anything IP reaches; gateways bridge to RTU behind them |
| speed | 9600–115200 baud, timing-sensitive | network speed |

Two details that matter in practice:

- On **RTU**, one line has **one master** — two masters talk over
  each other and nothing works. The unit ID is set on the device
  (DIP switches or a display menu), and every device on the line
  needs a *different* one and the *same* baud rate and parity.
- In the editor, changing a device's unit ID in its window moves the
  device's variables with it; a unit already taken on that line is
  refused.
- On **TCP**, the unit ID still exists in the header. It matters
  behind an **RTU↔TCP gateway**, where it selects which serial
  device behind the gateway you mean — the gateway's IP plus the
  drive's unit ID.

---

## Where next

| | |
|:---|:---|
| [Modbus](modbus.md) | configuring master and slave in a project — variables, the catalog, limits |
| [Two boards over Modbus](tutorial-modbus-pair.md) | a complete worked pair: WiFi slave, ethernet master |
| [Finding your boards](find-devices.md) | the scanner that locates the boards to talk to |
