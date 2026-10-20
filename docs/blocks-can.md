# CANopen blocks

Four blocks that talk to a CANopen device directly, below the level the
[motion blocks](blocks-motion.md) work at. You need them when the drive
profile does not cover what a particular device wants.

Like the motion blocks, each one is bound to an **axis** at the call:
`sdo(AXIS := 0, …)`.

---

## The blocks

<!-- fb-index: begin -->

| Block | What it does | Linux | ESP32 | STM32 |
|:---|:---|:---:|:---:|:---:|
| [CO_CIA402](fb-co_cia402.md) | The CiA 402 drive state machine on its own: Enable walks the drive to operation enabled, Ready says it got there. | yes | yes | - |
| [CO_SDOWRITE](fb-co_sdowrite.md) | Writes an object of the drive over SDO - at startup only, never in the cycle. | yes | yes | - |
| [CO_SDOREAD](fb-co_sdoread.md) | Reads an object of the drive over SDO at startup. | yes | yes | - |
| [CO_RAMPTIME](fb-co_ramptime.md) | Sets the drive's acceleration and deceleration times - written only at standstill and only on change. | yes | yes | - |

<!-- fb-index: end -->

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
