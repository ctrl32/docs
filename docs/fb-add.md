---
image: img/blk-add-ld.webp
image_alt: "ADD in the editor"
---

# ADD

OUT = IN1 + IN2 + IN3 + IN4; unconnected inputs are 0.

![ADD on a rung](img/blk-add-ld.webp){: .sb-center}

![ADD on a WEBview screen](img/blk-add-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM ADD_ST
  add_out_st := add_in1 + add_in2 + add_in3 + add_in4;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN1` | input | REAL | - | First addend. |
| `IN2` | input | REAL | - | Second addend. |
| `IN3` | input | REAL | - | Third addend (0 when unconnected). |
| `IN4` | input | REAL | - | Fourth addend (0 when unconnected). |
| `OUT` | output | REAL | - | The sum. |

## Description

**ADD takes up to four inputs**, and unconnected ones are 0. A new ADD
shows two; *Add input* on its right-click menu opens the third and the
fourth, *Remove input* takes the last one away. An input in use is
always shown.

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

Values are floating point, which means:

- **Fractions are fine.** 0.1 °C, 2.5 mm, no scaling tricks needed.
- **Big integers lose precision.** Past about 16 million, consecutive
  whole numbers stop being distinguishable. A part counter that must be
  exact into the millions belongs in an integer variable.
- **Equality is unreliable.** `1.0 - 0.9 - 0.1` is not exactly 0. Never
  test two calculated values with `=`; use [EQ](blocks-compare.md) with
  a tolerance.

### Order matters

Blocks execute in program order and pass values through variables, so a
chain of calculations has to be *written* in the order it flows. A block
reading a variable that a later block writes gets last cycle's value.
For a long calculation [Structured Text](st-language.md) is the better
tool: expressions evaluate in the order you write them, on one line,
with no intermediate variables at all.

---

Every block of the family: [Maths](blocks-math.md) · every block: [Function blocks](blocks.md)
