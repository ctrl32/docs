# Maths blocks

Arithmetic, and the assignment block. Nothing surprising here — the
value is in knowing what happens at the edges.

---

## The arithmetic

| Block | Inputs | Output | Result |
|---|---|---|---|
| **ADD** | IN1…IN4 | OUT | IN1 + IN2 + IN3 + IN4 |
| **SUB** | IN1, IN2 | OUT | IN1 − IN2 |
| **MUL** | IN1, IN2 | OUT | IN1 × IN2 |
| **DIV** | IN1, IN2 | OUT | IN1 ÷ IN2 |
| **MIN** | IN1, IN2 | OUT | the smaller of the two |
| **MAX** | IN1, IN2 | OUT | the larger of the two |
| **ABS** | IN | OUT | the value without its sign |

**ADD takes four inputs**, and unconnected ones are 0 — so it doubles as
a two- or three-input adder without any special handling.

**Every other input is 0 when unconnected too**, and that is worth a
thought on MUL (result 0) and DIV (see below).

---

## Division by zero gives zero

`DIV` with IN2 = 0 produces **0**. It does not fault, does not produce
infinity, and does not stop the machine.

This is a deliberate choice: a divisor that is briefly zero is normal on a
real machine — a flow that has not started, a length not yet measured, a
sensor still warming up. A controller that halts the cycle over it would
be useless.

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

## MIN and MAX as guards

The obvious use is picking the larger of two measurements. The more
common one is putting a floor or a ceiling on a value:

```
setpoint ──IN1─┐
      50 ──IN2─┤ MAX ├── OUT ──> setpoint_guarded
```

Now the setpoint can never go below 50, whatever a screen or a fieldbus
writes into it.

For a floor **and** a ceiling in one block, use
[LIMIT](blocks-signal.md#limit-clamp) instead — that is what it is for.

---

## MOVE — assignment

**OUT = IN.** The IEC assignment, as a block.

| Pin | Type | Meaning |
|---|---|---|
| `IN` | input, number | the source |
| `OUT` | output, number | the destination |

It looks like it does nothing, and in a diagram it nearly does — its job
is to get a value from one tag into another. Where it earns its keep is
**in a ladder rung**, as the plain result box: while the rung conducts,
the value is committed; while it does not, the destination holds.

```
recipe_ready ──[ MOVE IN=recipe_temp ]── OUT ──> setpoint
```

The setpoint takes the recipe value the moment the recipe is ready, and
keeps it afterwards. That "commit a value when a condition is met" is
one of the most common things a machine program does.

---

## Numbers on ctrl32

Values are floating point, which means:

- **Fractions are fine.** 0.1 °C, 2.5 mm, no scaling tricks needed.
- **Big integers lose precision.** Past about 16 million, consecutive
  whole numbers stop being distinguishable. A part counter that must be
  exact into the millions belongs in an integer tag.
- **Equality is unreliable.** `1.0 - 0.9 - 0.1` is not exactly 0. Never
  test two calculated values with `=`; use
  [EQ with a tolerance](blocks-compare.md#eq-equal-within-a-tolerance),
  which exists for exactly this reason.

## Order matters

Blocks execute in program order and pass values through tags, so a chain
of calculations has to be *written* in the order it flows. A block
reading a tag that a later block writes gets last cycle's value.

For a long calculation this is where [Structured Text](st-language.md)
becomes the better tool: expressions evaluate in the order you write
them, on one line, with no intermediate tags at all.
