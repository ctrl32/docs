---
title: "Comparison: LT"
slug: fb-lt
section: "Function blocks"
order: 166
sidebar_position: 166
image: img/blk-lt-ld.webp
image_alt: "LT in the editor"
generator: tools/docs_export.py
---

# LT

Q is TRUE when IN1 < IN2.

![LT on a rung](img/blk-lt-ld.webp){: .sb-center}

![LT on a WEBview screen](img/blk-lt-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM LT_ST
  lt_q_st := lt_in1 < lt_in2;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN1` | input | REAL | - | The value tested. |
| `IN2` | input | REAL | - | The value it is compared with. |
| `Q` | output | BOOL | - | IN1 < IN2. |

## Description

| Block | Q is TRUE when |
|:---|:---:|
| **GT** | IN1 > IN2 |
| **GE** | IN1 ≥ IN2 |
| **LT** | IN1 < IN2 |
| **LE** | IN1 ≤ IN2 |
| **EQ** | IN1 and IN2 are equal within EPS |

All take two number inputs and give one boolean output. An unconnected
input is 0.

### Comparisons chatter at the threshold

A measurement sitting near the limit - noise, vibration, a sensor's
last digit - crosses back and forth many times a second, and the output
follows: a relay clacks, an alarm floods the log, a WEBview client
drowns in updates. It is not a bug in the block. **The fix is
hysteresis** - [HYST](/docs/blocks/blocks-signal/) - and for anything driving a
physical output it should be your default choice over GT/LT. Use plain
comparisons for decisions inside the logic, where chattering costs
nothing.

!!! tip "Deadband is the other half"
    An analog variable with a deadband stops reporting changes smaller
    than the deadband, which quiets everything reading it. Set it on the
    variable, not in the logic. See [Variables](/docs/editor-overview/variables/).

In a ladder rung the same comparison can be a compare contact, which
conducts while the comparison holds.

---

Every block of the family: [Comparison](/docs/blocks/blocks-compare/) · every block: [Function blocks](/docs/blocks/)
