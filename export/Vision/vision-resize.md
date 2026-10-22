---
title: "Geometry: Resize"
slug: vision-resize
section: "Vision"
order: 216
sidebar_position: 216
image: img/vbc-resize.webp
image_alt: "The Resize block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Resize

**Geometry** · in the trade: *resampling, scaling* · in a project file: `resize`

Scales the picture - a smaller picture is analysed faster.

![The Resize block on the Vision canvas](img/vbc-resize.webp){: .sb-center}

![The window of the Resize block: its settings on the left, its picture on the right](img/vb-resize.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Scales the picture to a share of its size. At 50 % a 1280 x 720 picture becomes 640 x 360 with a quarter of the pixels - the blocks after it run about four times faster. A check that looks for a large thing (is the part there, is the belt empty, which colour) loses nothing at half size; a code reader or a caliper wants the full picture.

Above 100 % the picture is enlarged. That adds no detail - a blurred code stays blurred - but it can help a reader whose smallest bar is under two pixels wide.

The areas of the blocks after a Resize are in pixels of the resized picture.

## Typical uses

- a faster presence or colour check at half size
- a cleaner small picture for a Find pattern
- enlarging a code at the limit of the camera

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture to scale |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the scaled picture |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `scale` | 5 .. 400 | 50 | % | size of the result |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
