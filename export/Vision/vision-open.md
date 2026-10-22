---
title: "Shapes: Open"
slug: vision-open
section: "Vision"
order: 249
sidebar_position: 249
image: img/vbc-open.webp
image_alt: "The Open block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Open

**Shapes** · in the trade: *morphological opening* · in a project file: `open`

Erode, then dilate - removes specks and keeps the size of large areas.

![The Open block on the Vision canvas](img/vbc-open.webp){: .sb-center}

![The window of the Open block: its settings on the left, its picture on the right](img/vb-open.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

An erode followed by a dilate with the same brush. Specks, thin lines and bridges thinner than the brush vanish in the erode and do not come back in the dilate, while the large shapes - shrunk and then grown by the same amount - keep their size and place. It is the one-step way to clean the background after a threshold before [Find objects](/docs/vision/vision-contours/) counts what is there.

Choose `size` just above the largest speck you want gone; a brush larger than a detail of the part removes that detail too.

## Typical uses

- the background cleaned before Find objects
- specks removed with the shapes kept their size

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | a black-and-white picture |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the picture without the small specks, the shapes their old size |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 .. 51 | 3 | px | size of the brush |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
