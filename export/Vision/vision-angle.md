---
title: "Measurements: Angle"
slug: vision-angle
section: "Vision"
order: 293
sidebar_position: 293
image: img/vbc-angle.webp
image_alt: "The Angle block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Angle

**Measurements** · in the trade: *angle gauge* · in a project file: `angle`

The angle between two directions - two Line (fit) blocks, a Line (fit) and a fixed number - with a tolerance.

![The Angle block on the Vision canvas](img/vbc-angle.webp){: .sb-center}

![The window of the Angle block: its settings on the left, its picture on the right](img/vb-angle.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

The angle between two directions - the angles of two [Line (fit)](/docs/vision/vision-line_fit/) blocks, or one of them and a fixed number - as 0..180 degrees, with `min`/`max` making *ok* a tolerance check. The squareness of two edges, the opening of a flap, the angle of a lever, the alignment of a label against the part's edge.

## Typical uses

- the angle between two edges
- squareness of a cut
- the opening of a flap or a lever

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `a` | number | the first direction, in degrees |
| `b` | number | the second direction, in degrees |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `angle` | number | the angle between them, 0..180 degrees |
| `ok` | yes/no | the angle lies between min and max |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `min` | 0 .. 180 | 0 |  | the angle must be at least this (min = max = 0 means no limit) |
| `max` | 0 .. 180 | 0 |  | the angle must be at most this |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
