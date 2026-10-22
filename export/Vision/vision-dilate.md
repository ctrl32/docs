---
title: "Shapes: Dilate"
slug: vision-dilate
section: "Vision"
order: 248
sidebar_position: 248
image: img/vbc-dilate.webp
image_alt: "The Dilate block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Dilate

**Shapes** · in the trade: *morphological dilation* · in a project file: `dilate`

Grows white areas - closes small gaps.

![The Dilate block on the Vision canvas](img/vbc-dilate.webp){: .sb-center}

![The window of the Dilate block: its settings on the left, its picture on the right](img/vb-dilate.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Grows every white area of a black-and-white picture by a brush of `size` pixels, `times` over. Small gaps close, a broken outline joins up, a thin line thickens into something [Find lines](/docs/vision/vision-lines/) can hold on to, and two parts that nearly touch become one - which is sometimes what you want (the printed letters of one word as one object) and sometimes not.

Three pixels once is the usual dose. To close gaps without growing the shapes use [Close](/docs/vision/vision-close/).

## Typical uses

- small gaps closed in an outline
- thin lines thickened for Find lines
- the letters of a word joined into one object

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | a black-and-white picture (white shapes on black) |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the picture with the white areas grown |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 .. 51 | 3 | px | size of the brush |
| `times` | 1 .. 20 | 1 |  | how many times |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
