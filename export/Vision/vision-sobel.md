---
title: "Edges: Gradient"
slug: vision-sobel
section: "Vision"
order: 257
sidebar_position: 257
image: img/vbc-sobel.webp
image_alt: "The Gradient block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Gradient

**Edges** · in the trade: *gradient magnitude (Sobel)* · in a project file: `sobel`

How fast the brightness changes at every point (Sobel) - bright where there is an edge, black where the picture is flat. A softer edge picture than Edges, with the strength kept.

![The Gradient block on the Vision canvas](img/vbc-sobel.webp){: .sb-center}

![The window of the Gradient block: its settings on the left, its picture on the right](img/vb-sobel.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Shows how fast the brightness changes at every point (the Sobel gradient): bright where there is an edge, black where the picture is flat, and the stronger the edge the brighter. Unlike [Edges](/docs/vision/vision-canny/) it does not decide what is an edge and what is not - it hands the strength on, so a threshold of your own can decide, or a [Caliper](/docs/vision/vision-caliper/) can find the strongest change along its line.

`direction` keeps only the changes across the picture (x - vertical edges), down it (y - horizontal edges) or both. A larger `size` sees softer, wider edges and ignores fine texture.

## Typical uses

- edge strength handed on for your own threshold
- vertical or horizontal edges only

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | a gray or colour picture |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the edge strength at every point, as a gray picture |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `direction` | both / x / y | both |  | edges across (x) |
| `size` | 1 / 3 / 5 / 7 | 3 |  | the size of the kernel - larger sees softer edges |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
