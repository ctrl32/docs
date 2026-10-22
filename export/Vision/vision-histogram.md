---
title: "Measurements: Histogram"
slug: vision-histogram
section: "Vision"
order: 286
sidebar_position: 286
image: img/vbc-histogram.webp
image_alt: "The Histogram block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Histogram

**Measurements** · in the trade: *intensity histogram* · in a project file: `histogram`

How the shades are spread in an area - the most common shade, the share of dark points and of light ones.

![The Histogram block on the Vision canvas](img/vbc-histogram.webp){: .sb-center}

![The window of the Histogram block: its settings on the left, its picture on the right](img/vb-histogram.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

How the shades are distributed in an area: the most common shade (*peak*), the share of points darker than `dark_below` and the share brighter than `light_above`, in percent. It tells whether a surface is mostly light with a dark mark on it, whether the background is where it should be, whether a threshold still has a clean valley to cut at - and it does so without finding any object.

The area is dragged on the block's picture. The two shares, with an [In range](/docs/vision/vision-in_range/) after them, make a check of "enough dark print on the label" or "no dark stain on the surface".

## Typical uses

- is there enough print on the label
- a dark stain on a light surface
- has the background shade drifted

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture (a colour one is taken by its brightness) |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `peak` | number | the most common shade in the area, 0..255 |
| `dark` | number | the share of points darker than dark_below, in percent |
| `light` | number | the share of points brighter than light_above, in percent |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 0 | px | left edge of the area |
| `y` | 0 .. 8192 | 0 | px | top edge of the area |
| `w` | 1 .. 8192 | 200 | px | width of the area |
| `h` | 1 .. 8192 | 200 | px | height of the area |
| `dark_below` | 0 .. 255 | 64 |  | a point darker than this is dark |
| `light_above` | 0 .. 255 | 192 |  | a point brighter than this is light |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## On the block's window

- **Drag on the picture** to set the area (`x`, `y`, `w`, `h`). The numbers follow and can still be typed.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
