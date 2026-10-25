---
title: "Filters: Gaussian blur"
slug: vision-gauss
section: "Vision"
order: 236
sidebar_position: 236
image: img/vbc-gauss.webp
image_alt: "The Gaussian blur block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Gaussian blur

**Filters** · in the trade: *Gaussian filter* · in a project file: `gauss`

A softer blur that keeps edges better than the plain one.

![The Gaussian blur block on the Vision canvas](img/vbc-gauss.webp){: .sb-center}

![The window of the Gaussian blur block: its settings on the left, its picture on the right](img/vb-gauss.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

A blur in which the near neighbours count more than the far ones (a Gaussian bell). It calms noise like the plain [Blur](/docs/vision/vision-blur/) but keeps edges in place better, which is why the edge finders are usually fed by it. `size` is the width of the bell in pixels and must be odd; 3 or 5 for camera noise, more for a texture that should disappear.

## Typical uses

- the standard smoothing before an edge detector
- camera noise removed with the edges kept in place

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
| `size` | 1 .. 99 | 5 | px | size of the neighbourhood (odd) |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
