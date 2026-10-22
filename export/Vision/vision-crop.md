---
title: "Geometry: Crop"
slug: vision-crop
section: "Vision"
order: 215
sidebar_position: 215
image: img/vbc-crop.webp
image_alt: "The Crop block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Crop

**Geometry** · in the trade: *region of interest (ROI)* · in a project file: `crop`

Keeps one rectangle of the picture - later blocks see only that area.

![The Crop block on the Vision canvas](img/vbc-crop.webp){: .sb-center}

![The window of the Crop block: its settings on the left, its picture on the right](img/vb-crop.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Keeps one rectangle of the picture and throws the rest away. Everything after it works on that rectangle alone - the part, the label, the reading window - and a smaller picture is analysed faster: a code reader on a 640 x 360 window takes a quarter of the time it takes on the whole 1280 x 720 picture.

Put a Crop right after the camera when the check concerns one place of the picture. Blocks with an area of their own (Presence, Colour check, the measuring blocks) do not need it; blocks that look at the whole picture they receive (Find objects, Read code, the filters) do.

The rectangle is drawn on the block's picture by a drag; the numbers follow. A rectangle that reaches outside the picture is cut at its edge.

## Typical uses

- the reading window of a code reader
- the part's place for the blocks that look at the whole picture
- a faster program on a smaller picture

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture to cut from |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the rectangle, as a picture of its own (w x h pixels) |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 0 | px | left edge |
| `y` | 0 .. 8192 | 0 | px | top edge |
| `w` | 1 .. 8192 | 320 | px | width |
| `h` | 1 .. 8192 | 240 | px | height |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## On the block's window

- **Drag on the picture** to set the area (`x`, `y`, `w`, `h`). The numbers follow and can still be typed.

## Used in

- Bottle check - a shipped example project
- The reTerminal with EtherCAT (the code reader) - a shipped example project

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
