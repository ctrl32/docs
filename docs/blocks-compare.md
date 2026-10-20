# Comparison blocks

Five comparisons and a selector. These are how a number becomes a
decision.

---

## The comparisons

| Block | Q is TRUE when |
|:---|:---:|
| [GT](fb-gt.md) | IN1 > IN2 |
| [GE](fb-ge.md) | IN1 ≥ IN2 |
| [LT](fb-lt.md) | IN1 < IN2 |
| [LE](fb-le.md) | IN1 ≤ IN2 |
| [EQ](fb-eq.md) | IN1 and IN2 are equal within EPS |

All take two number inputs and give one boolean output. An unconnected
input is 0, so `GT` with only IN1 wired asks "is it positive?".

---

## The blocks

<!-- fb-index: begin -->

| Block | What it does | Linux | ESP32 | STM32 |
|:---|:---|:---:|:---:|:---:|
| [GT](fb-gt.md) | Q is TRUE when IN1 > IN2. | yes | yes | yes |
| [GE](fb-ge.md) | Q is TRUE when IN1 >= IN2. | yes | yes | yes |
| [LT](fb-lt.md) | Q is TRUE when IN1 < IN2. | yes | yes | yes |
| [LE](fb-le.md) | Q is TRUE when IN1 <= IN2. | yes | yes | yes |
| [EQ](fb-eq.md) | Q is TRUE when IN1 and IN2 are equal within the tolerance EPS: |IN1 - IN2| <= EPS. | yes | yes | yes |
| [SEL](fb-sel.md) | Binary selector: OUT = IN1 when G is TRUE, IN0 when it is FALSE. | yes | yes | yes |

<!-- fb-index: end -->

## Comparisons chatter at the threshold

This is the single most common problem with a comparison on real
hardware, and it is not a bug in the block.

A measurement sitting near the limit — noise, vibration, a sensor's last
digit — crosses back and forth many times a second. The output follows,
and downstream something switches at the same rate. A relay clacks, an
alarm floods the log, a WEBview client drowns in updates.

**The fix is hysteresis:** switch on at one level, off at a lower one.
That is what [HYST](fb-hyst.md)
does, and for anything driving a physical output it should be your
default choice over GT/LT.

Use plain comparisons for decisions inside the logic, where chattering
costs nothing.

!!! tip "Deadband is the other half"
    An analog variable with a deadband stops reporting changes smaller than
    the deadband, which quiets everything reading it — screens, trends,
    WEBview. Set it on the variable, not in the logic. See [Variables](variables.md).

---
