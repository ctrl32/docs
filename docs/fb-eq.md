---
image: img/blk-eq-ld.webp
image_alt: "EQ in the editor"
---

# EQ

Q is TRUE when IN1 and IN2 are equal within the tolerance EPS: |IN1 - IN2| <= EPS.

![EQ on a rung](img/blk-eq-ld.webp){: .sb-center}

![EQ on a WEBview screen](img/blk-eq-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM EQ_ST
  eq_q_st := ABS(eq_in1 - eq_in2) <= eq_eps;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN1` | input | REAL | - | The first value. |
| `IN2` | input | REAL | - | The second value. |
| `EPS` | parameter | REAL | 0 | How close counts as equal. |
| `Q` | output | BOOL | - | TRUE when |IN1 - IN2| <= EPS. |

## Description

EQ has a tolerance and the other comparisons do not, for a reason worth
understanding: **two calculated numbers are almost never exactly
equal.**

Ask whether a temperature has reached 50.0 °C with an exact comparison
and you may wait forever - the measurement passes 49.9997 and 50.0001
and never lands on 50.0 exactly.

```
temp     ──IN1─┐
setpoint ──IN2─┤ EQ EPS=0.5 ├── Q ──> at_temperature
```

"Within half a degree" is what you meant anyway.

!!! tip "Leave EPS at 0 only for whole numbers"
    Comparing a step count, a recipe number or a state code with EPS = 0
    is fine - those are exact. For anything measured or calculated, give
    it a tolerance that reflects what the sensor can actually resolve.

An unconnected input is 0. A threshold comparison that drives a physical
output belongs on [HYST](blocks-signal.md), which does not chatter.

---

Every block of the family: [Comparison](blocks-compare.md) · every block: [Function blocks](blocks.md)
