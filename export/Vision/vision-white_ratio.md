---
title: "Measurements: White share"
slug: vision-white_ratio
section: "Vision"
order: 279
sidebar_position: 279
image: img/vbc-white_ratio.webp
image_alt: "The White share block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# White share

**Measurements** · in the trade: *area fraction, pixel count* · in a project file: `white_ratio`

How much of the picture is white, in percent - use it after a threshold or a colour range.

![The White share block on the Vision canvas](img/vbc-white_ratio.webp){: .sb-center}

![The window of the White share block: its settings on the left, its picture on the right](img/vb-white_ratio.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

How much of the picture is white, in percent - the area fraction after a threshold or a colour range. It turns "how much of the window is red", "how much of the belt is covered", "how large is the stain" into one number, without finding objects. With a [Mask](/docs/vision/vision-mask/) or a [Crop](/docs/vision/vision-crop/) before it the share refers to the part alone.

It wants a black-and-white picture; on a gray one every non-black point counts. An [In range](/docs/vision/vision-in_range/) after it gives the yes/no.

## Typical uses

- how much of the window is the taught colour
- coverage of a surface by glue, paint or print
- how large a stain or a gap is

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | a black-and-white picture |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `value` | number | the share of white, in percent |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

The block has no settings.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
