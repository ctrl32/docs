---
title: "Boolean: XOR"
slug: fb-xor
section: "Function blocks"
order: 154
sidebar_position: 154
image: img/blk-xor-ld.webp
image_alt: "XOR in the editor"
generator: tools/docs_export.py
---

# XOR

Q is TRUE when exactly one input is TRUE - the two inputs disagree.

![XOR on a rung](img/blk-xor-ld.webp){: .sb-center}

![XOR on a WEBview screen](img/blk-xor-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM XOR_ST
  xor_q_st := xor_in1 XOR xor_in2;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN1` | input | BOOL | - | First input. |
| `IN2` | input | BOOL | - | Second input. |
| `Q` | output | BOOL | - | IN1 XOR IN2. |

## Description

| Block | Inputs | Output | Q is TRUE when |
|:---|:---:|:---:|:---|
| **AND** | IN1, IN2 | Q | both inputs are TRUE |
| **OR** | IN1, IN2 | Q | at least one input is TRUE |
| **XOR** | IN1, IN2 | Q | exactly one input is TRUE |
| **NOT** | IN | Q | the input is FALSE |

**XOR** is the one people reach for least and then find indispensable:
it is "these two disagree". Two end-position sensors that should never
both be on, a command and a feedback that ought to match, a pair of
redundant switches.

```
sensor_open ──IN1─┐
sensor_shut ──IN2─┤ XOR ├── Q ──> position_implausible
```

An unconnected input is FALSE. In ladder the gates earn their place
where the logic reads better as a box than as a knot of contacts; in FBD
they are the natural form.

### Bit access

Write `status.3` on a pin and it reads bit 3 of the integer variable
`status`; the same spelling works as an output. Bits are written
**atomically**. See [Variables](/docs/editor-overview/variables/).

---

Every block of the family: [Boolean](/docs/blocks/blocks-boolean/) · every block: [Function blocks](/docs/blocks/)
