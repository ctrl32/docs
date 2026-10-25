---
title: "Filters: Median"
slug: vision-median
section: "Vision"
order: 237
sidebar_position: 237
image: img/vbc-median.webp
image_alt: "The Median block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Median

**Filters** · in the trade: *median filter* · in a project file: `median`

Removes specks and salt-and-pepper noise, keeps edges sharp.

![The Median block on the Vision canvas](img/vbc-median.webp){: .sb-center}

![The window of the Median block: its settings on the left, its picture on the right](img/vb-median.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Replaces every pixel by the middle value of its neighbourhood. A lone bright or dark speck - dust, a dead pixel, salt-and-pepper noise - is never the middle value and vanishes, while an edge, where half the neighbourhood is dark and half bright, stays exactly where it was. It is the filter to put before a threshold that produces scattered single pixels.

`size` must be odd; 3 or 5 removes specks, larger sizes start to round off corners.

## Typical uses

- dust and dead pixels removed
- salt-and-pepper noise after a threshold

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture to clean |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the picture with the specks gone |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 .. 99 | 5 | px | size of the neighbourhood (odd) |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
