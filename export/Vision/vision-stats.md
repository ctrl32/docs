---
title: "Measurements: Brightness statistics"
slug: vision-stats
section: "Vision"
order: 284
sidebar_position: 284
image: img/vbc-stats.webp
image_alt: "The Brightness statistics block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Brightness statistics

**Measurements** · in the trade: *intensity statistics* · in a project file: `stats`

The mean, the darkest, the brightest and the spread of the brightness in an area - for a check that a lamp works, a surface is even, a print is there.

![The Brightness statistics block on the Vision canvas](img/vbc-stats.webp){: .sb-center}

![The window of the Brightness statistics block: its settings on the left, its picture on the right](img/vb-stats.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

The mean, the darkest point, the brightest point and the spread (standard deviation) of the brightness in an area. Four numbers that say more than one: a lamp that works gives the expected mean, an even surface a small spread, a print in the area a large one, a glint a high maximum. The area is dragged on the block's picture.

Send the four into variables for a screen or a trend, or follow one with [In range](/docs/vision/vision-in_range/). [Histogram](/docs/vision/vision-histogram/) answers the related question "how are the shades distributed".

## Typical uses

- is the surface even (a small spread)
- is there print or a mark in the area (a large spread)
- a lighting trend on a screen

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture (a colour one is taken by its brightness) |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `mean` | number | the mean brightness of the area, 0..255 |
| `min` | number | the darkest point |
| `max` | number | the brightest point |
| `spread` | number | the standard deviation of the brightness |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 0 | px | left edge of the area |
| `y` | 0 .. 8192 | 0 | px | top edge of the area |
| `w` | 1 .. 8192 | 200 | px | width of the area |
| `h` | 1 .. 8192 | 200 | px | height of the area |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## On the block's window

- **Drag on the picture** to set the area (`x`, `y`, `w`, `h`). The numbers follow and can still be typed.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
