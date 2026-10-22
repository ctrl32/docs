---
title: "Logic: ST code"
slug: vision-st
section: "Vision"
order: 276
sidebar_position: 276
image: img/vbc-st.webp
image_alt: "The ST code block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# ST code

**Logic** · in the trade: *scripting inside the vision program (IEC 61131-3 Structured Text)* · in a project file: `st`

A few lines of ST - the same language as the PLC program - over the block's inputs a, b, c, d (numbers) and p, q (yes/no); it writes y1..y4 (numbers) and r1, r2 (yes/no). Locals in VAR ... END_VAR, loops and conditions as in a program.

![The ST code block on the Vision canvas](img/vbc-st.webp){: .sb-center}

![The window of the ST code block: its settings on the left, its picture on the right](img/vb-st.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

A few lines of ST - the language of the PLC program - inside the vision program, for the calculation the blocks do not have: a ratio of two measurements, a limit that depends on a recipe value, an average of three distances, a pass/fail that combines four results with a condition. The block's inputs are `a`, `b`, `c`, `d` (numbers) and `p`, `q` (yes/no); it writes `y1`..`y4` (numbers) and `r1`, `r2` (yes/no). An input nothing feeds reads 0 or FALSE.

Locals go in `VAR ... END_VAR` at the start; loops, conditions and the standard functions work as in a program. The code compiles the moment the box loses focus - the window says *Compiles.* or names the line - and runs on the device inside the vision program, on the device's own ST engine, so what the editor shows is what the device computes.

```
VAR ratio : REAL; END_VAR
ratio := a / b;
y1 := ratio * 100.0;
r1 := ratio > 0.95 AND ratio < 1.05 AND p;
```

## Typical uses

- a ratio, a difference or an average of several measurements as one result
- a pass/fail that combines several checks with a condition
- a limit computed from a recipe value or from another measurement

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `a` | number (optional) | a number (0 when nothing feeds it) |
| `b` | number (optional) | a number |
| `c` | number (optional) | a number |
| `d` | number (optional) | a number |
| `p` | yes/no (optional) | a yes/no (FALSE when nothing feeds it) |
| `q` | yes/no (optional) | a yes/no |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `y1` | number | the first number the code wrote |
| `y2` | number | the second number |
| `y3` | number | the third number |
| `y4` | number | the fourth number |
| `r1` | yes/no | the first yes/no the code wrote |
| `r2` | yes/no | the second yes/no |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `src` | text | "y1 := a + b;" |  | the ST statements (a |
| `code` | text | (empty) |  | the compiled code (the editor fills it; never typed) |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## On the block's window

- The window shows the **code box** (up to 8000 characters) instead of a value field for `src`; the code compiles when the box loses focus, and the line under it says *Compiles.* or names the error.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
