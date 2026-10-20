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
| [TON](fb-ton.md) | Delays switching on: Q goes TRUE once IN has been held continuously for PT. | yes | yes | yes |
| [TOF](fb-tof.md) | Delays switching off: Q follows IN on at once and stays on for another PT after IN drops. | yes | yes | yes |
| [TP](fb-tp.md) | Fires a fixed pulse: a rising edge of IN makes Q TRUE for exactly PT (non-retriggerable). | yes | yes | yes |
| [BLINK](fb-blink.md) | Blinks: while RUN is TRUE, Q alternates T_ON on and T_OFF off. | yes | yes | yes |

<!-- fb-index: end -->

## Choosing between them

| You want | Block |
|:---|:---:|
| ignore a signal until it has held | [TON](fb-ton.md) |
| keep something running after the reason stopped | [TOF](fb-tof.md) |
| a fixed dose, regardless of how long the trigger lasts | [TP](fb-tp.md) |
| something that flashes | [BLINK](fb-blink.md) |

## The trap worth knowing

Never build a timer by counting cycles. `n := n + 1; IF n > 100 THEN`
looks like it waits a second and does — until the WiFi stack gets busy,
the cycle stretches, and your second becomes 1.4. Every block here uses a
monotonic millisecond clock and is immune to that.

The same applies to your own ST blocks: take a timestamp, compare
timestamps.
