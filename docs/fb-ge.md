---
image: img/blk-ge-ld.webp
image_alt: "GE in the editor"
---

# GE

Q is TRUE when IN1 >= IN2.

![GE on a rung](img/blk-ge-ld.webp){: .sb-center}

![GE on a WEBview screen](img/blk-ge-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM GE_ST
  ge_q_st := ge_in1 >= ge_in2;
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
| `Q` | output | BOOL | - | IN1 >= IN2. |

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
hysteresis** - [HYST](blocks-signal.md) - and for anything driving a
physical output it should be your default choice. Use plain comparisons
for decisions inside the logic, where chattering costs nothing.

!!! tip "Deadband is the other half"
    An analog variable with a deadband stops reporting changes smaller
    than the deadband, which quiets everything reading it. Set it on the
    variable, not in the logic. See [Variables](variables.md).

In a ladder rung the same comparison can be a compare contact, which
conducts while the comparison holds.

---

Every block of the family: [Comparison](blocks-compare.md) · every block: [Function blocks](blocks.md)
