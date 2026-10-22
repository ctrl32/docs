---
title: "Edges: Gradient (fine)"
slug: vision-scharr
section: "Vision"
order: 259
sidebar_position: 259
image: img/vbc-scharr.webp
image_alt: "The Gradient (fine) block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Gradient (fine)

**Edges** · in the trade: *gradient (Scharr operator)* · in a project file: `scharr`

Like Gradient, with the Scharr kernel - more exact on the direction of thin edges.

![The Gradient (fine) block on the Vision canvas](img/vbc-scharr.webp){: .sb-center}

![The window of the Gradient (fine) block: its settings on the left, its picture on the right](img/vb-scharr.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

The same as [Gradient](/docs/vision/vision-sobel/) with the Scharr kernel, which is more exact about the direction of thin edges and responds the same to an edge whatever its angle. Prefer it when the angle of an edge matters - before a [Line (fit)](/docs/vision/vision-line_fit/) on a thin line - and the plain Gradient when it does not.

## Typical uses

- thin edges whose angle matters
- a cleaner edge picture before a Line (fit)

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

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
