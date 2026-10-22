---
title: "Maths: ABS"
slug: fb-abs
section: "Function blocks"
order: 162
sidebar_position: 162
image: img/blk-abs-ld.webp
image_alt: "ABS in the editor"
generator: tools/docs_export.py
---

# ABS

OUT = the value of IN without its sign.

![ABS on a rung](img/blk-abs-ld.webp){: .sb-center}

![ABS on a WEBview screen](img/blk-abs-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM ABS_ST
  abs_out_st := ABS(abs_in);
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN` | input | REAL | - | The value. |
| `OUT` | output | REAL | - | |IN|. |

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

Values are floating point: fractions are fine, and past about 16
million consecutive whole numbers stop being distinguishable. Blocks run
in program order and a block reading a variable a later block writes
gets last cycle's value.

---

Every block of the family: [Maths](/docs/blocks/blocks-math/) · every block: [Function blocks](/docs/blocks/)
