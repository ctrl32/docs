---
title: "Boolean: OR"
slug: fb-or
section: "Function blocks"
order: 153
sidebar_position: 153
image: img/blk-or-ld.webp
image_alt: "OR in the editor"
generator: tools/docs_export.py
---

# OR

Q is TRUE when at least one input is TRUE.

![OR on a rung](img/blk-or-ld.webp){: .sb-center}

![OR on a WEBview screen](img/blk-or-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM OR_ST
  or_q_st := or_in1 OR or_in2;
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
| `Q` | output | BOOL | - | IN1 OR IN2. |

## Description

| Block | Inputs | Output | Q is TRUE when |
|:---|:---:|:---:|:---|
| **AND** | IN1, IN2 | Q | both inputs are TRUE |
| **OR** | IN1, IN2 | Q | at least one input is TRUE |
| **XOR** | IN1, IN2 | Q | exactly one input is TRUE |
| **NOT** | IN | Q | the input is FALSE |

An unconnected input is FALSE - on an OR it changes nothing.

In ladder you rarely need the gates - contacts in series *are* an AND
and contacts in parallel *are* an OR. They earn their place in FBD, and
in rungs where the logic reads better as a box than as a knot of
contacts.

### Bit access

Write `status.3` on a pin and it reads bit 3 of the integer variable
`status`; the same spelling works as an output. Bits are written
**atomically**, so the logic writing bit 0 and a screen writing bit 1
never lose each other's work. See [Variables](/docs/editor-overview/variables/).

---

Every block of the family: [Boolean](/docs/blocks/blocks-boolean/) · every block: [Function blocks](/docs/blocks/)
