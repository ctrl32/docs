---
title: "Geometry: Rotate"
slug: vision-rotate
section: "Vision"
order: 217
sidebar_position: 217
image: img/vbc-rotate.webp
image_alt: "The Rotate block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Rotate

**Geometry** · in the trade: *rotation by right angles* · in a project file: `rotate`

Turns the picture by a quarter, a half or three quarters.

![The Rotate block on the Vision canvas](img/vbc-rotate.webp){: .sb-center}

![The window of the Rotate block: its settings on the left, its picture on the right](img/vb-rotate.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Turns the picture by a quarter, a half or three quarters, clockwise. A camera mounted on its side or upside down gives a picture that reads the right way up after this block, so that the areas drawn later make sense on the screen and in the window.

For any other angle use [Turn and shift](/docs/vision/vision-affine/); for a mirror image use [Flip](/docs/vision/vision-flip/). Turning by quarters costs nothing and loses no pixel.

## Typical uses

- a camera mounted on its side
- a camera mounted upside down
- a picture read the way the operator stands

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture to turn |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the turned picture (a quarter turn swaps width and height) |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `angle` | 90 / 180 / 270 | 90 |  | clockwise |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
