---
title: "Boolean: AND"
slug: fb-and
section: "Function blocks"
order: 152
sidebar_position: 152
image: img/blk-and-ld.webp
image_alt: "AND in the editor"
generator: tools/docs_export.py
---

# AND

Q is TRUE when both inputs are TRUE.

![AND on a rung](img/blk-and-ld.webp){: .sb-center}

![AND on a WEBview screen](img/blk-and-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM AND_ST
  and_q_st := and_in1 AND and_in2;
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
| `Q` | output | BOOL | - | IN1 AND IN2. |

## Description

| Block | Inputs | Output | Q is TRUE when |
|:---|:---:|:---:|:---|
| **AND** | IN1, IN2 | Q | both inputs are TRUE |
| **OR** | IN1, IN2 | Q | at least one input is TRUE |
| **XOR** | IN1, IN2 | Q | exactly one input is TRUE |
| **NOT** | IN | Q | the input is FALSE |

An unconnected input is FALSE - which matters: an unconnected input on
an AND holds the output FALSE forever.

In ladder you rarely need the gates - contacts in series *are* an AND
and contacts in parallel *are* an OR. They earn their place in FBD, and
in rungs where the logic reads better as a box than as a knot of
contacts.

### Bit access

Boolean logic often needs one bit out of a word - a status word from a
drive, a mask from a fieldbus device. You do not need a block for that:
write `status.3` on a pin and it reads bit 3 of the integer variable
`status`. The same spelling works as an output. Bits are written
**atomically**, so the logic writing bit 0 and a screen writing bit 1
never lose each other's work. See [Variables](/docs/editor-overview/variables/).

---

Every block of the family: [Boolean](/docs/blocks/blocks-boolean/) · every block: [Function blocks](/docs/blocks/)
