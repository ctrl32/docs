---
title: "Maths: SUB"
slug: fb-sub
section: "Function blocks"
order: 157
sidebar_position: 157
image: img/blk-sub-ld.webp
image_alt: "SUB in the editor"
generator: tools/docs_export.py
---

# SUB

OUT = IN1 - IN2.

![SUB on a rung](img/blk-sub-ld.webp){: .sb-center}

![SUB on a WEBview screen](img/blk-sub-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM SUB_ST
  sub_out_st := sub_in1 - sub_in2;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN1` | input | REAL | - | The value subtracted from. |
| `IN2` | input | REAL | - | The value subtracted. |
| `OUT` | output | REAL | - | The difference. |

## Description

An unconnected input is 0.

| Block | Inputs | Output | Result |
|:---|:---:|:---:|:---:|
| **ADD** | IN1…IN4 | OUT | IN1 + IN2 + IN3 + IN4 |
| **SUB** | IN1, IN2 | OUT | IN1 − IN2 |
| **MUL** | IN1, IN2 | OUT | IN1 × IN2 |
| **DIV** | IN1, IN2 | OUT | IN1 ÷ IN2 |
| **MIN** | IN1, IN2 | OUT | the smaller of the two |
| **MAX** | IN1, IN2 | OUT | the larger of the two |
| **ABS** | IN | OUT | the value without its sign |

### Numbers on ctrl32

Values are floating point: fractions are fine; past about 16 million,
consecutive whole numbers stop being distinguishable; and `1.0 - 0.9 -
0.1` is not exactly 0, so never test two calculated values with `=` -
use [EQ](/docs/blocks/blocks-compare/) with a tolerance.

### Order matters

Blocks execute in program order and pass values through variables. A
block reading a variable that a later block writes gets last cycle's
value; write a chain in the order it flows, or use
[Structured Text](/docs/programming/st-language/) for a long calculation.

---

Every block of the family: [Maths](/docs/blocks/blocks-math/) · every block: [Function blocks](/docs/blocks/)
