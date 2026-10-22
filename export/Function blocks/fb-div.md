---
title: "Maths: DIV"
slug: fb-div
section: "Function blocks"
order: 159
sidebar_position: 159
image: img/blk-div-ld.webp
image_alt: "DIV in the editor"
generator: tools/docs_export.py
---

# DIV

OUT = IN1 ÷ IN2; division by zero gives 0 and never stops anything.

![DIV on a rung](img/blk-div-ld.webp){: .sb-center}

![DIV on a WEBview screen](img/blk-div-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM DIV_ST
  div_out_st := div_in1 / div_in2;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN1` | input | REAL | - | The dividend. |
| `IN2` | input | REAL | - | The divisor. |
| `OUT` | output | REAL | - | The quotient (0 when IN2 is 0). |

## Description

### Division by zero gives zero

`DIV` with IN2 = 0 produces **0**. It does not fault, does not produce
infinity, and does not stop the equipment. An unconnected IN2 is 0 too.

This is a deliberate choice: a divisor that is briefly zero is perfectly
normal - a flow that has not started, a length not yet measured, a
sensor still warming up. A controller that halted the cycle over it
would be useless.

!!! warning "Zero is a plausible-looking wrong answer"
    The danger is not the crash that does not happen, it is the 0 that
    flows onward and looks like a real measurement. Where the result
    drives something that matters, check the divisor:

    ```
    flow ──IN1─┐
    time ──IN2─┤ DIV ├── OUT ──> rate
    time ──[GT 0]── Q ──> rate_valid
    ```

    and let `rate_valid` gate whatever uses `rate`.

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
[EQ](/docs/blocks/blocks-compare/) and a tolerance.

---

Every block of the family: [Maths](/docs/blocks/blocks-math/) · every block: [Function blocks](/docs/blocks/)
