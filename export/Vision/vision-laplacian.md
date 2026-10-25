---
title: "Edges: Laplacian"
slug: vision-laplacian
section: "Vision"
order: 259
sidebar_position: 259
image: img/vbc-laplacian.webp
image_alt: "The Laplacian block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Laplacian

**Edges** · in the trade: *Laplacian operator* · in a project file: `laplacian`

The second change of brightness (Laplacian) - lights up the fine detail and the edges in every direction at once; also what Sharpness measures.

![The Laplacian block on the Vision canvas](img/vbc-laplacian.webp){: .sb-center}

![The window of the Laplacian block: its settings on the left, its picture on the right](img/vb-laplacian.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Lights up the fine detail and the edges in every direction at once (the second change of brightness). A sharp picture has a strong Laplacian and a blurred one a weak one, which is what [Sharpness](/docs/vision/vision-sharpness/) measures; on its own the block is a fast way to make texture, print and edges stand out against flat areas before a threshold.

A larger `size` responds to wider features. The output is noisy on a noisy picture - a small [Gaussian blur](/docs/vision/vision-gauss/) before it helps.

## Typical uses

- fine detail and print made to stand out
- the basis of the Sharpness measure

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | a gray or colour picture |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the detail and the edges, bright on black |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 / 3 / 5 | 3 |  | the size of the kernel |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
