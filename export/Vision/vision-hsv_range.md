---
title: "Colour: Colour range"
slug: vision-hsv_range
section: "Vision"
order: 227
sidebar_position: 227
image: img/vbc-hsv_range.webp
image_alt: "The Colour range block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Colour range

**Colour** · in the trade: *HSV colour segmentation, colour thresholding* · in a project file: `hsv_range`

White where the colour is inside the range, black elsewhere. Hue runs 0..179 around the colour wheel (red at 0, green at 60, blue at 120).

![The Colour range block on the Vision canvas](img/vbc-hsv_range.webp){: .sb-center}

![The window of the Colour range block: its settings on the left, its picture on the right](img/vb-hsv_range.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Makes a black-and-white picture that is white wherever the colour lies inside a range and black elsewhere - the quickest way to find a red cap, a green mark or a blue label. The range is given in hue, saturation and value: the hue is the colour itself round the colour wheel (0 red, 30 yellow, 60 green, 90 cyan, 120 blue, 150 magenta, 179 red again), the saturation says how pure it is (0 gray, 255 vivid) and the value how bright (0 black, 255 full).

For red, which sits at both ends of the wheel, set the low hue above the high one (170 to 10): the range then wraps round. Keep the saturation floor above 50 or so, or gray and white parts of the picture - which have every hue - come out white too; keep the value floor above 30 to leave out the shadows.

The colour is picked by a right-click on a point of the block's picture: the hue settles on that point's hue with a tolerance round it. After it put a [White share](/docs/vision/vision-white_ratio/) for "how much of the area has this colour", or [Find objects](/docs/vision/vision-contours/) for "where are the things of this colour".

## Typical uses

- a red cap, a green mark, a blue label as a white shape
- the share of a colour with White share
- the coloured parts for Find objects

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | a colour picture |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | black and white: white where the colour is inside the range |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `h_lo` | 0 .. 179 | 0 |  | lowest hue |
| `h_hi` | 0 .. 179 | 179 |  | highest hue (below the lowest wraps round red) |
| `s_lo` | 0 .. 255 | 60 |  | lowest saturation |
| `s_hi` | 0 .. 255 | 255 |  | highest saturation |
| `v_lo` | 0 .. 255 | 40 |  | lowest brightness |
| `v_hi` | 0 .. 255 | 255 |  | highest brightness |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## On the block's window

- **Right-click a point** of the picture to take its colour: `h_lo` and `h_hi` become that point's hue less and plus 10. A gray or dark point has no colour and is refused.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
