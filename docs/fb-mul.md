---
image: img/blk-mul-ld.webp
image_alt: "MUL in the editor"
---

# MUL

OUT = IN1 × IN2.

![MUL on a rung](img/blk-mul-ld.webp){: .sb-center}

![MUL on a WEBview screen](img/blk-mul-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MUL_ST
  mul_out_st := mul_in1 * mul_in2;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN1` | input | REAL | - | First factor. |
| `IN2` | input | REAL | - | Second factor. |
| `OUT` | output | REAL | - | The product. |

## Description

An unconnected input is 0 - worth a thought on MUL, because the result
is then 0.

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
consecutive whole numbers stop being distinguishable; and calculated
values are rarely exactly equal - compare them with
[EQ](blocks-compare.md) and a tolerance.

### Order matters

Blocks execute in program order and pass values through variables. A
block reading a variable that a later block writes gets last cycle's
value; write a chain in the order it flows, or use
[Structured Text](st-language.md) for a long calculation.

---

Every block of the family: [Maths](blocks-math.md) · every block: [Function blocks](blocks.md)
