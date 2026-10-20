# Boolean blocks

Eight blocks that work with TRUE and FALSE: four gates, two edge
detectors and two latches.

In ladder you rarely need the gates — contacts in series *are* an AND and
contacts in parallel *are* an OR. They earn their place in FBD, and in
rungs where the logic reads better as a box than as a knot of contacts.

---

## The gates

| Block | Inputs | Output | Q is TRUE when |
|:---|:---:|:---:|:---|
| [AND](fb-and.md) | IN1, IN2 | Q | both inputs are TRUE |
| [OR](fb-or.md) | IN1, IN2 | Q | at least one input is TRUE |
| [XOR](fb-xor.md) | IN1, IN2 | Q | exactly one input is TRUE |
| [NOT](fb-not.md) | IN | Q | the input is FALSE |

An unconnected input is FALSE — which matters: an unconnected input on an
AND holds the output FALSE forever, and on an OR it changes nothing.

**XOR** is the one people reach for least and then find indispensable: it
is "these two disagree". Two end-position sensors that should never both
be on, a command and a feedback that ought to match, a pair of redundant
switches.

```
sensor_open ──IN1─┐
sensor_shut ──IN2─┤ XOR ├── Q ──> position_implausible
```

---

## The blocks

<!-- fb-index: begin -->

| Block | What it does | Linux | ESP32 | STM32 |
|:---|:---|:---:|:---:|:---:|
| [R_TRIG](fb-r_trig.md) | Detects a rising edge: Q is TRUE for exactly one cycle after CLK rises. | yes | yes | yes |
| [F_TRIG](fb-f_trig.md) | Detects a falling edge: Q is TRUE for exactly one cycle after CLK drops. | yes | yes | yes |
| [SR](fb-sr.md) | Set-dominant latch: remembers, and if set and reset are both TRUE, set wins. | yes | yes | yes |
| [RS](fb-rs.md) | Reset-dominant latch: remembers, and if set and reset are both TRUE, reset wins. | yes | yes | yes |
| [AND](fb-and.md) | Q is TRUE when both inputs are TRUE. | yes | yes | yes |
| [OR](fb-or.md) | Q is TRUE when at least one input is TRUE. | yes | yes | yes |
| [XOR](fb-xor.md) | Q is TRUE when exactly one input is TRUE - the two inputs disagree. | yes | yes | yes |
| [NOT](fb-not.md) | Q is TRUE when the input is FALSE. | yes | yes | yes |

<!-- fb-index: end -->

## Latch or coil?

Ladder has set and reset coils (`-(S)-`, `-(R)-`), which do the same
thing as these blocks. The difference is where the decision lives:

- **Coils** put set and reset on separate rungs. Easy to read, and the
  priority is decided by which rung comes last.
- **A latch block** puts both on one line with the priority written into
  the block name, where nobody can miss it.

For anything where the both-at-once case matters, the block is the
clearer choice.

---

## Bit access

Boolean logic often needs one bit out of a word — a status word from a
drive, a mask from a fieldbus device. You do not need a block for that:
write `status.3` on a pin and it reads bit 3 of the integer variable
`status`. The same spelling works as an output.

Bits are written **atomically**, so the logic writing bit 0 and a screen
writing bit 1 never lose each other's work. See [Variables](variables.md).
