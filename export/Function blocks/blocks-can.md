---
title: "CANopen blocks"
slug: blocks-can
section: "Function blocks"
order: 138
sidebar_position: 138
generator: tools/docs_export.py
---

# CANopen blocks

Four blocks that talk to a CANopen device directly, below the level the
[motion blocks](/docs/blocks/blocks-motion/) work at. You need them when the drive
profile does not cover what a particular device wants.

Like the motion blocks, each one is bound to an **axis** at the call:
`sdo(AXIS := 0, …)`.

---

## The blocks

<!-- fb-index: begin -->

| Block | What it does | Linux | ESP32 | STM32 |
|:---|:---|:---:|:---:|:---:|
| [CO_CIA402](/docs/blocks/fb-co_cia402/) | The CiA 402 drive state machine on its own: Enable walks the drive to operation enabled, Ready says it got there. | yes | yes | - |
| [CO_SDOWRITE](/docs/blocks/fb-co_sdowrite/) | Writes an object of the drive over SDO - at startup only, never in the cycle. | yes | yes | - |
| [CO_SDOREAD](/docs/blocks/fb-co_sdoread/) | Reads an object of the drive over SDO at startup. | yes | yes | - |
| [CO_RAMPTIME](/docs/blocks/fb-co_ramptime/) | Sets the drive's acceleration and deceleration times - written only at standstill and only on change. | yes | yes | - |

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

See [Buses](/docs/buses/) for wiring, node IDs and termination, and
[Motion blocks](/docs/blocks/blocks-motion/) for the layer above this one.
