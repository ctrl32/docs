# Maths blocks

Arithmetic, and the assignment block. Nothing surprising here — the
value is in knowing what happens at the edges.

---

## The arithmetic

| Block | Inputs | Output | Result |
|:---|:---:|:---:|:---:|
| [ADD](fb-add.md) | IN1…IN4 | OUT | IN1 + IN2 + IN3 + IN4 |
| [SUB](fb-sub.md) | IN1, IN2 | OUT | IN1 − IN2 |
| [MUL](fb-mul.md) | IN1, IN2 | OUT | IN1 × IN2 |
| [DIV](fb-div.md) | IN1, IN2 | OUT | IN1 ÷ IN2 |
| [MIN](fb-min.md) | IN1, IN2 | OUT | the smaller of the two |
| [MAX](fb-max.md) | IN1, IN2 | OUT | the larger of the two |
| [ABS](fb-abs.md) | IN | OUT | the value without its sign |

**ADD takes up to four inputs**, and unconnected ones are 0. A new ADD
shows two; *Add input* on its right-click menu opens the third and the
fourth, *Remove input* takes the last one away. An input in use is
always shown.

**Every other input is 0 when unconnected too**, and that is worth a
thought on MUL (result 0) and DIV (see below).

---

## Division by zero gives zero

`DIV` with IN2 = 0 produces **0**. It does not fault, does not produce
infinity, and does not stop the equipment.

This is a deliberate choice: a divisor that is briefly zero is perfectly
normal — a flow that has not started, a length not yet measured, a sensor
still warming up. A controller that halted the cycle over it would be
useless.

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

---

## The blocks

<!-- fb-index: begin -->

| Block | What it does | Linux | ESP32 | STM32 |
|:---|:---|:---:|:---:|:---:|
| [ADD](fb-add.md) | OUT = IN1 + IN2 + IN3 + IN4; unconnected inputs are 0. | yes | yes | yes |
| [SUB](fb-sub.md) | OUT = IN1 - IN2. | yes | yes | yes |
| [MUL](fb-mul.md) | OUT = IN1 × IN2. | yes | yes | yes |
| [DIV](fb-div.md) | OUT = IN1 ÷ IN2; division by zero gives 0 and never stops anything. | yes | yes | yes |
| [MIN](fb-min.md) | OUT = the smaller of IN1 and IN2. | yes | yes | yes |
| [MAX](fb-max.md) | OUT = the larger of IN1 and IN2. | yes | yes | yes |
| [ABS](fb-abs.md) | OUT = the value of IN without its sign. | yes | yes | yes |
| [MOVE](fb-move.md) | OUT = IN - the IEC assignment as a block. | yes | yes | yes |

<!-- fb-index: end -->

## Numbers on ctrl32

Values are floating point, which means:

- **Fractions are fine.** 0.1 °C, 2.5 mm, no scaling tricks needed.
- **Big integers lose precision.** Past about 16 million, consecutive
  whole numbers stop being distinguishable. A part counter that must be
  exact into the millions belongs in an integer variable.
- **Equality is unreliable.** `1.0 - 0.9 - 0.1` is not exactly 0. Never
  test two calculated values with `=`; use
  [EQ with a tolerance](fb-eq.md),
  which exists for exactly this reason.

## Order matters

Blocks execute in program order and pass values through variables, so a chain
of calculations has to be *written* in the order it flows. A block
reading a variable that a later block writes gets last cycle's value.

For a long calculation this is where [Structured Text](st-language.md)
becomes the better tool: expressions evaluate in the order you write
them, on one line, with no intermediate variables at all.
