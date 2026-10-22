---
title: "Maths: MAX"
slug: fb-max
section: "Function blocks"
order: 161
sidebar_position: 161
image: img/blk-max-ld.webp
image_alt: "MAX in the editor"
generator: tools/docs_export.py
---

# MAX

OUT = the larger of IN1 and IN2.

![MAX on a rung](img/blk-max-ld.webp){: .sb-center}

![MAX on a WEBview screen](img/blk-max-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MAX_ST
  max_out_st := MAX(max_in1, max_in2);
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
| `OUT` | output | REAL | - | The larger of the two. |

## Description

### MIN and MAX as guards

The obvious use is picking the larger of two measurements. The more
common one is putting a floor on a value:

```
setpoint ──IN1─┐
      50 ──IN2─┤ MAX ├── OUT ──> setpoint_guarded
```

Now the setpoint can never go below 50, whatever a screen or a fieldbus
writes into it.

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
