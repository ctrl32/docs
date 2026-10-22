---
title: "CANopen"
slug: canopen
section: "Protocols"
order: 309
sidebar_position: 309
generator: tools/docs_export.py
---

# CANopen

A drive on a CAN bus is not a device you poll — it is a device
with a state machine, a scheduled exchange of process data, and a
heartbeat that tells you the moment it stops listening.

ctrl32 is the **manager**: NMT master, SDO client, SYNC producer and
heartbeat monitor. The devices on the bus are its nodes.

![The system canvas: the CAN bus hangs off the drive's card, the i550 node on it — click a node and its variables with their object addresses list below](img/canopen-canvas.webp){: .sb-center}

---

## Why not just use Modbus

Both can talk to a drive, and the difference is not speed.

**Modbus** is request and answer. You ask for a register, you wait, you
get it. A drive that has stopped answering looks the same as a slow one
until a timeout expires, and the timing of the exchange has nothing to do
with the timing of your control loop.

**CANopen** is scheduled. Process data (**PDO**) arrives at the start of
your cycle and leaves at the end, so what the logic reads is what was
true this cycle, every cycle. A device that goes quiet is noticed by
**heartbeat** within a defined time, and the reaction is yours to
program.

For an axis that must move accurately, that difference is the whole
game. For a temperature you read once a second, Modbus is simpler and
just as good.

---

## PDO and SDO — the two conversations

![The i550 node's page: TPDO and RPDO slots with their mappings and sync types, the SDO startup parameters one tab over](img/canopen-node.webp){: .sb-center}

**PDO — process data.** Small, fast, cyclic. The controlword, the
setpoint, the actual position, the status. No addressing overhead, no
acknowledgement: a frame goes out and whoever cares receives it.

**SDO — service data.** A request and a confirmed answer, used to read
and write the device's parameters by index and sub-index. It is how you
configure a device — and it takes milliseconds.

!!! danger "Never do SDO inside the cycle"
    An SDO exchange waits for an answer from another device. Waiting
    inside the cycle destroys its timing, non-reproducibly, and shows up
    later as jitter nobody can explain.

    ctrl32 enforces this: `CO_SDOWRITE` and `CO_SDOREAD` are compiled
    into **startup records** and never execute in the cycle. Parameterise
    at startup, use PDOs for everything that repeats.

---

## The tie to the cycle

```
SYNC  →  RPDO in  →  logic  →  TPDO out  →  wait for the period
```

Receive at the start, transmit at the end, always in that order. The
logic works on a snapshot, exactly as it does with local I/O.

**For position feedback, set the drive's PDO to synchronous
transmission** — sent in response to SYNC rather than whenever the drive
feels like it. Event-driven transmission means values arriving at
unpredictable moments, and a delay you cannot measure is a delay you
cannot compensate. Everything positioning does rests on that number
being knowable.

---

## What the bus can carry

At 500 kbit/s an 8-byte PDO takes about **130 µs**.

| Setup | Bus time | Share of a 10 ms cycle |
|:---|:---:|:---:|
| 4 drives, 2 PDOs each | ~1 ms | 10 % |
| 8 drives, 2 PDOs each | ~2 ms | 20 % |

Eight drives is comfortable. Beyond that, shorten the cycle or move to
1 Mbit/s — which costs bus length, because CAN trades speed against
distance.

---

## Heartbeat is not optional

Every node reports periodically that it is alive. The manager watches,
and a node that misses its window is **failed**, not merely late.

**The reaction belongs in your program, and it should be a quick stop.**
Carrying on with the last values received is how a setup keeps moving
after the thing controlling it has gone — and it is the failure mode that
looks fine right up until it does not.

---

## EDS import

A CANopen device comes with an **EDS file** (Electronic Data Sheet,
CiA 306) — the manufacturer's description of every object it exposes,
with indices, sub-indices, types and names.

ctrl32 reads it. *Tools → Device library* installs an EDS into the
project's device repository; from there you pick objects and the editor
**generates the variables**, correctly typed and correctly addressed.
*Add CAN device* shows the repository with the card of each file —
click a device and its parameters are read out on the spot: objects,
how many are writable, the PDO channels, the first free node-ID.
The PDO mapping page lists the whole object dictionary of the device's EDS
when you add an entry (the *mappable only* filter is a checkbox); the
transmission type is chosen per PDO.

Changing the node-ID later, in the device's window, moves the device's
variables and the axis on it to the new node with it.

![Add CAN device: the file's parameters on the card](img/canopen-add.webp){: .sb-center}

That is the difference between an afternoon with a manual and five
minutes with a file. Object `0x6041` sub `0` becomes a variable called
what the manufacturer called it, with the right size and the right sign.

**The parser is deliberately tolerant.** Vendor EDS files are creative:
unknown sections and keys are skipped rather than refused, because a file
that will not load is worth nothing and a file with two odd lines is
worth almost everything. A genuinely unreadable file fails and changes
nothing.

!!! note "EDS is read only in the editor"
    The board never sees an EDS. The pack carries the resulting
    variables, already resolved — so nothing is parsed on the equipment and
    nothing depends on a file being present.

---

## Drives: the trap that costs a day

The reference target is the **Lenze i550**, and it ships with **Lenze's
own state machine active**, not CiA 402.

Write a correct controlword into a drive in that state and nothing
happens. No error, no complaint — the drive simply does not react, and
the search for the bug goes into your own code, where it is not.

The startup block switches the mode over SDO, so a project built from the
i550 profile never meets this. If you are talking to one by hand, it is
the first thing to check.

Node ID, baud rate and termination are DIP switches on the drive itself —
worth writing on the drawing, because nothing in software can tell you
they are wrong.

---

## Wiring a drive (Lenze i550)

![The panel and the drive on one bus](img/i550-wiring.webp){: .sb-center}

| Panel | Drive (X216) | Note |
|:---|:---|:---|
| `CAN_H` | `CH` | one wire of the twisted pair |
| `CAN_L` | `CL` | the other wire |
| `GND` | `CG` | the signal ground — **always**, it is not optional |

- **Terminate both ends.** A 120 Ω resistor between `CAN_H` and `CAN_L`
  at the panel, and the drive's `R` switch ON at the other end. A bus
  without terminators works on the bench and fails in the cabinet.
- **Shield** the pair in a cabinet with drives; connect the shield at one
  end.
- **More drives** are daisy-chained from strip to strip. Only the last
  one keeps `R` ON; the ones in the middle have it OFF.
- **Power the panel from its own supply**, not a bench USB port — a USB
  port does not carry a radio burst and a bus at once, and the resets
  look like a bus problem.

## The drive's switches (Lenze i550)

The i550 reads its node address, its bit rate and its terminator from a
DIP bank on the control unit.

![The DIP bank set for node 2, 500 kbit/s, terminated](img/i550-dip.webp){: .sb-center}

- **`R`** — the terminator. ON at the last drive on the bus, OFF on
  every drive in the middle.

- **`64 32 16 8 4 2 1`** — the node address is the sum of the switches
  that are ON. For node 2, only `2` is ON. With all seven OFF the drive
  takes the address from its parameter 0x2301:001 instead.
- **`d c b a`** — the bit rate, by the table in the picture. `OFF ON OFF
  ON` is 500 kbit/s. All four OFF takes the rate from parameter
  0x2301:002; a combination not in the table falls back to 500 kbit/s.

The switches are read **at power-on**. Set them, then switch the drive
off and on again — a change while it runs does nothing until the next
start.

## The process data of a drive axis (Lenze i550)

The CAN axis wizard's device carries the two PDOs the runtime exchanges
on every SYNC, both with **synchronous** transmission:

| PDO | Direction | Starts with | Used by |
|:---|:---|:---|:---|
| **TPDO1** | drive → panel | the statusword `0x6041` and the actual speed `0x6044` (the first four bytes) | the motion blocks read these two; whatever follows in the PDO is ordinary data |
| **RPDO1** | panel → drive | the controlword `0x6040` and the speed setpoint `0x6042` | the motion blocks write these two |

Its *SDO parameters* hold the start-up writes: velocity mode, and on
the i550 the two network-control entries that switch its own state
machine off. Without them the drive ignores every controlword.

## Reading the drive's own values

Any object a drive publishes in a PDO becomes a variable with
`source: canopen`, its index and a gain - no program involved. The
values worth having from a frequency drive:

| Object | Value | Gain on the i550 |
|:---|:---|:---|
| `0x6078` | motor current | rated current / 1000 (1.6 A rated → 0.0016, in A) |
| `0x6077` | torque | rated torque / 1000 (1.177 Nm rated → 0.001177, in Nm) |
| `0x6079` | DC link voltage | 0.001 (in V) |
| `0x2DDD` | actual output frequency | 0.1 (in Hz) |
| `0x2D89` | motor voltage | 0.1 (in V) |

- Current and torque arrive in **per mille of the drive's rated
  values**, so their gains come from the nameplate.
- **`0x2DDD` is the actual output frequency.** The neighbouring
  `0x2D87` is the setpoint *after the ramp*: it looks alive and correct
  right up until the load slips.
- Give each a **deadband**, so a standing motor does not repaint the
  screen with noise.

The statusword is a variable too, and its bits read straight into a
rung: bit 3 (`sw.3`) is the CiA 402 **fault** bit. With the drive absent
or the bus down the statusword reads **−1** - every bit set, the fault
bit included - so a fault lamp and an alarm on that bit light by
themselves when the drive is unplugged. Give such an alarm a short
delay (200 ms) so a bus hiccup does not raise it.

## When the drive does not move

| You see | The cause, in the order to check |
|:---|:---|
| *ready* never lights, the panel's `INFO` says the node is **OFFLINE** | the bus: the DIP address or the bit rate does not match the project, a terminator is missing, `CG` is not connected, `CH`/`CL` swapped, the switches were changed without a power cycle |
| the console says **`CAN: NO CYCLE`** | the project has an axis but no device with a PDO mapping — the cyclic exchange never starts. The CAN axis wizard's device provides it; a device built by hand needs TPDO1 and RPDO1 mapped |
| *ready* lights, **Run** does nothing, no fault | the drive is not under network control. On the i550 that is the start-up SDO the wizard writes (the network-control entries under *SDO parameters*); a drive commissioned by hand may have them reset |
| the motor starts and **oscillates** or overshoots | the drive's own ramps are slower than the profile the panel sends. Set the drive's acceleration and deceleration ramps to their minimum; the panel makes the profile |
| the *fault* lamp is on | read the fault on the drive's display, remove its cause, reset. A fault that comes back at once is in the drive's parameters or the wiring, not in the project |
| the actual speed stays at 0 while the motor turns | TPDO1 does not carry 0x6044 — check the mapping |
| the whole panel restarts every few seconds | a CAN transmit into a bus nobody acknowledges: a drive that is off, a transceiver that is missing, a shorted pair |

---

## Safety

**Stopping over CANopen is not a safety function.** Neither is a
quick-stop command, nor anything else on this page. What is — STO
terminals, hard-wired limit switches, and the reactions worth defining
— is in [Motion blocks — safety](/docs/blocks/blocks-motion/) and
[Intended use](/docs/about/intended-use/).

---

## Where to go next

- [EtherCAT](/docs/buses/ethercat/) — the other bus a drive can sit on, and
  what changes when it does.

| | |
|:---|:---|
| [CANopen blocks](/docs/blocks/blocks-can/) | `CO_CIA402`, `CO_SDOWRITE`, `CO_SDOREAD`, `CO_RAMPTIME` |
| [Motion blocks](/docs/blocks/blocks-motion/) | the PLCopen layer above them |
| [Raw CAN](/docs/buses/rawcan/) | a device with its own frame format, no CANopen involved |
| [Buses](/docs/buses/) | wiring, termination, and choosing between buses |
