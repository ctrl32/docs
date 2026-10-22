---
title: "Colour: Grayscale"
slug: vision-gray
section: "Vision"
order: 226
sidebar_position: 226
image: img/vbc-gray.webp
image_alt: "The Grayscale block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Grayscale

**Colour** · in the trade: *grayscale conversion* · in a project file: `gray`

Turns a colour picture into shades of gray.

![The Grayscale block on the Vision canvas](img/vbc-gray.webp){: .sb-center}

![The window of the Grayscale block: its settings on the left, its picture on the right](img/vb-gray.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Turns a colour picture into shades of gray. Most measuring and finding blocks work on brightness alone and do this themselves when they get a colour picture; put a Grayscale in front of them when several blocks share the gray picture (it is computed once) or when the gray picture itself should be shown on a screen.

To keep ONE colour's information rather than the brightness of all three, use [One channel](/docs/vision/vision-channel/).

## Typical uses

- one gray picture shared by several blocks
- a gray preview on a screen

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | a colour picture |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the same picture in shades of gray |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

The block has no settings.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
