---
title: "Filters: Blur"
slug: vision-blur
section: "Vision"
order: 234
sidebar_position: 234
image: img/vbc-blur.webp
image_alt: "The Blur block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Blur

**Filters** · in the trade: *box filter (mean filter)* · in a project file: `blur`

Averages each pixel with its neighbours - calms noise.

![The Blur block on the Vision canvas](img/vbc-blur.webp){: .sb-center}

![The window of the Blur block: its settings on the left, its picture on the right](img/vb-blur.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Averages every pixel with its neighbours in a square of `size` pixels. Noise calms down, fine texture disappears, and a threshold after it gives clean shapes instead of a snowstorm. The price is that edges soften - a code or a caliper measured after a blur loses precision.

Three to five pixels is the usual size for noise; a blur much larger than the detail you want to keep washes it away. [Gaussian blur](/docs/vision/vision-gauss/) does the same with less damage to edges, [Median](/docs/vision/vision-median/) removes specks without softening anything.

## Typical uses

- noise calmed before a threshold
- fine texture removed from a surface

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture to smooth |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the smoothed picture |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 .. 99 | 5 | px | size of the neighbourhood |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
