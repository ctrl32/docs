---
title: "Timers"
slug: blocks-timers
section: "Function blocks"
order: 83
sidebar_position: 83
generator: tools/docs_export.py
---

# Timers

Four blocks: a delay on, a delay off, a fixed pulse, and a blinker.
Between them they cover almost everything a setup needs from time.

All of them measure **real milliseconds**, not cycles, and all of them
report progress on a second output so you can show it on a screen.

---

## The blocks

<!-- fb-index: begin -->

| Block | What it does | Linux | ESP32 | STM32 |
|:---|:---|:---:|:---:|:---:|
| [TON](/docs/blocks/fb-ton/) | Delays switching on: Q goes TRUE once IN has been held continuously for PT. | yes | yes | yes |
| [TOF](/docs/blocks/fb-tof/) | Delays switching off: Q follows IN on at once and stays on for another PT after IN drops. | yes | yes | yes |
| [TP](/docs/blocks/fb-tp/) | Fires a fixed pulse: a rising edge of IN makes Q TRUE for exactly PT (non-retriggerable). | yes | yes | yes |
| [BLINK](/docs/blocks/fb-blink/) | Blinks: while RUN is TRUE, Q alternates T_ON on and T_OFF off. | yes | yes | yes |

<!-- fb-index: end -->

## Choosing between them

| You want | Block |
|:---|:---:|
| ignore a signal until it has held | [TON](/docs/blocks/fb-ton/) |
| keep something running after the reason stopped | [TOF](/docs/blocks/fb-tof/) |
| a fixed dose, regardless of how long the trigger lasts | [TP](/docs/blocks/fb-tp/) |
| something that flashes | [BLINK](/docs/blocks/fb-blink/) |

## The trap worth knowing

Never build a timer by counting cycles. `n := n + 1; IF n > 100 THEN`
looks like it waits a second and does — until the WiFi stack gets busy,
the cycle stretches, and your second becomes 1.4. Every block here uses a
monotonic millisecond clock and is immune to that.

The same applies to your own ST blocks: take a timestamp, compare
timestamps.
