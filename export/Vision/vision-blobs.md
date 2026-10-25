---
title: "Measurements: Count objects"
slug: vision-blobs
section: "Vision"
order: 280
sidebar_position: 280
image: img/vbc-blobs.webp
image_alt: "The Count objects block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Count objects

**Measurements** · in the trade: *blob count, connected components* · in a project file: `blobs`

Counts the separate white areas of a black-and-white picture, and reports the largest one.

![The Count objects block on the Vision canvas](img/vbc-blobs.webp){: .sb-center}

![The window of the Count objects block: its settings on the left, its picture on the right](img/vb-blobs.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Counts the separate white areas of a black-and-white picture - the blobs - and reports the largest one's centre and area, in one block without a list of objects. For a quick "how many parts are in the window" or "where is the biggest one" it is enough; when the parts themselves are needed, their order and each one's numbers, use [Find objects](/docs/vision/vision-contours/), which hands them on as a list.

`min_area` leaves noise out of the count.

## Typical uses

- how many parts lie in the window
- where the biggest part is
- a quick count before a Check objects

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | a black-and-white picture, the objects white |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `count` | number | how many white areas there are, at least min_area each |
| `x` | number | the largest area's centre, pixels from the left |
| `y` | number | the largest area's centre, pixels from the top |
| `area` | number | the largest area's size, in pixels |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `min_area` | 1 .. 10000000 | 50 | px² | smaller areas are not counted |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
