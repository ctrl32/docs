# CANopen blocks

Four blocks that talk to a CANopen device directly, below the level the
[motion blocks](blocks-motion.md) work at. You need them when the drive
profile does not cover what a particular device wants.

Like the motion blocks, each one is bound to an **axis** at the call:
`sdo(AXIS := 0, …)`.

---

## CO_CIA402 — the drive state equipment

| Pin | Type | Meaning |
|:---|:---:|:---|
| `Enable` | input, bool | run the state equipment |
| `Ready` | output, bool | the drive is in *operation enabled* |
| `Fault` | output, bool | the drive is in fault |

The CiA 402 state equipment on its own. This is what
[MC_POWER](blocks-motion.md#mc_power) uses underneath, exposed for when
you want to build something the MC_ blocks do not cover.

A CiA 402 drive is not controlled by writing a speed. There is a state
equipment, driven through controlword `0x6040` and observed through
statusword `0x6041`, and it must be walked through in order —
*switch on disabled* → *ready to switch on* → *switched on* →
*operation enabled*. `Ready` is TRUE only at the end of that walk.

---

## CO_SDOWRITE — write a parameter

| Pin | Type | Meaning |
|:---|:---:|:---:|
| `IN` | input, number | the value |
| `INDEX`, `SUB` | parameters | which object |
| `VALUE`, `SIZE` | parameters | value and byte width |

**This runs at startup only.** The project compiler turns it into a
startup record; it never executes inside the cycle.

That restriction is the point. An SDO exchange takes milliseconds and
involves waiting for an answer — do it in the cycle and the cycle timing
is gone, non-reproducibly, in a way that shows up as jitter nobody can
explain. Parameterise at startup; use PDOs for anything cyclic.

**What it is for:** the settings a drive needs before it will behave —
switching the i550 into CiA 402 mode, setting a ramp, choosing a
reference source.

---

## CO_SDOREAD — read a parameter

| Pin | Type | Meaning |
|:---|:---:|:---:|
| `INDEX`, `SUB` | parameters | which object |
| `OUT` | output, number | the value read |

Startup only, for the same reason. Use it to read a nameplate value, a
motor rating, a firmware revision — something you want in the program but
that does not change while it runs.

---

## CO_RAMPTIME — ramp times, safely

| Pin | Type | Meaning |
|:---|:---:|:---|
| `ACC` | input, **seconds** | acceleration time, 0 → target rpm |
| `DEC` | input, **seconds** | deceleration time |
| `REF` | input, number | reference speed the times relate to |

Writes the CiA 402 ramp objects `0x6048` and `0x6049` — and it is careful
about when:

- **only when the axis is at standstill**, and
- **only when the values actually changed**.

So the cycle never touches SDO while the equipment is moving. This is the
block that lets ACC and DEC be adjustable from a [WEBview](webview.md)
screen without the adjustment being able to disturb a running axis.

---

## PDO timing belongs to the cycle

Anything cyclic — actual position, actual speed, controlword, setpoint —
travels as **PDO**, and the timing is tied to the cycle:

- **RPDO** received at the start of the cycle, into the process image
- **TPDO** transmitted at the end

Never asynchronously. A PDO arriving at a random moment produces jitter
that cannot be estimated and therefore cannot be compensated, and
non-reproducible faults are the most expensive kind.

For position feedback specifically, set the drive's PDO to
**synchronous** transmission (sent after SYNC). Event-driven transmission
means values at unpredictable times, and the delay compensation the
positioning depends on stops working.

## What the bus can carry

At 500 kbit/s an 8-byte PDO takes about 130 µs. Four drives with two PDOs
each is eight frames, roughly 1 ms — about **10 % of a 10 ms cycle**.

Eight drives is still comfortable. Beyond that, either shorten the cycle
or move to 1 Mbit/s, which costs bus length.

## Heartbeat is not optional

A drive that stops answering must be noticed. Heartbeat monitoring is
mandatory, and the reaction to a drop-out is a **quick stop** — not
carrying on with the last values received.

See [Buses](buses.md) for wiring, node IDs and termination, and
[Motion blocks](blocks-motion.md) for the layer above this one.
