---
image: img/blk-gt-ld.webp
image_alt: "GT in the editor"
---

# GT

Q is TRUE when IN1 > IN2.

![GT on a rung](img/blk-gt-ld.webp){: .sb-center}

![GT on a WEBview screen](img/blk-gt-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM GT_ST
  gt_q_st := gt_in1 > gt_in2;
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
| `Q` | output | BOOL | - | IN1 > IN2. |

## Description

| Block | Q is TRUE when |
|:---|:---:|
| **GT** | IN1 > IN2 |
| **GE** | IN1 ≥ IN2 |
| **LT** | IN1 < IN2 |
| **LE** | IN1 ≤ IN2 |
| **EQ** | IN1 and IN2 are equal within EPS |

All take two number inputs and give one boolean output. An unconnected
input is 0, so `GT` with only IN1 wired asks "is it positive?".

### Comparisons chatter at the threshold

This is the single most common problem with a comparison on real
hardware, and it is not a bug in the block. A measurement sitting near
the limit - noise, vibration, a sensor's last digit - crosses back and
forth many times a second. The output follows, and downstream something
switches at the same rate. A relay clacks, an alarm floods the log, a
WEBview client drowns in updates.

**The fix is hysteresis:** switch on at one level, off at a lower one.
That is what [HYST](blocks-signal.md) does, and for anything driving a
physical output it should be your default choice over GT/LT. Use plain
comparisons for decisions inside the logic, where chattering costs
nothing.

!!! tip "Deadband is the other half"
    An analog variable with a deadband stops reporting changes smaller
    than the deadband, which quiets everything reading it - screens,
    trends, WEBview. Set it on the variable, not in the logic. See
    [Variables](variables.md).

In a ladder rung the same comparison can be a compare contact
(`-[ > ]-`), which conducts while the comparison holds.

---

Every block of the family: [Comparison](blocks-compare.md) · every block: [Function blocks](blocks.md)
