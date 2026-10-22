---
title: "Maths: MIN"
slug: fb-min
section: "Function blocks"
order: 160
sidebar_position: 160
image: img/blk-min-ld.webp
image_alt: "MIN in the editor"
generator: tools/docs_export.py
---

# MIN

OUT = the smaller of IN1 and IN2.

![MIN on a rung](img/blk-min-ld.webp){: .sb-center}

![MIN on a WEBview screen](img/blk-min-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MIN_ST
  min_out_st := MIN(min_in1, min_in2);
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN1` | input | REAL | - | First value. |
| `IN2` | input | REAL | - | Second value. |
| `OUT` | output | REAL | - | The smaller of the two. |

## Description

### MIN and MAX as guards

The obvious use is picking the smaller of two measurements. The more
common one is putting a ceiling on a value: MIN with a constant on one
input means the output can never go above that constant, whatever a
screen or a fieldbus writes into the other.

For a floor **and** a ceiling in one block, use
[LIMIT](/docs/blocks/blocks-signal/) instead - that is what it is for.

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

Values are floating point; blocks run in program order and a block
reading a variable a later block writes gets last cycle's value.

---

Every block of the family: [Maths](/docs/blocks/blocks-math/) · every block: [Function blocks](/docs/blocks/)
