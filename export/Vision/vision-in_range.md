---
title: "Measurements: In range"
slug: vision-in_range
section: "Vision"
order: 282
sidebar_position: 282
image: img/vbc-in_range.webp
image_alt: "The In range block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# In range

**Measurements** · in the trade: *tolerance check, pass/fail* · in a project file: `in_range`

Yes when the number lies between the two limits (both included).

![The In range block on the Vision canvas](img/vbc-in_range.webp){: .sb-center}

![The window of the In range block: its settings on the left, its picture on the right](img/vb-in_range.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Yes when the number lies between `min` and `max`, both included - the tolerance check that turns a measurement into a pass/fail. A brightness between 40 and 80, a count between 12 and 12, a distance between 48.5 and 51.5 mm: the block's *ok* is the result that goes into the PLC program's variable.

The limits may come from variables (the small list beside each setting), so a recipe sets the tolerance per product. The measuring blocks of the v11 table have min/max built in; In range serves everything else.

## Typical uses

- a measurement against its tolerance
- a count against the expected number
- a limit from a recipe

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `v` | number | the number to check |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `ok` | yes/no | min <= v <= max |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `min` | -1000000 .. 1000000 | 0 |  | lowest good value |
| `max` | -1000000 .. 1000000 | 100 |  | highest good value |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## Used in

- The reTerminal with EtherCAT (the code reader) - a shipped example project

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
