---
title: "Ready tools: Colour check"
slug: vision-colour
section: "Vision"
order: 297
sidebar_position: 297
image: img/vbc-colour.webp
image_alt: "The Colour check block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Colour check

**Ready tools** · in the trade: *colour verification, HSV hue match* · in a project file: `colour`

Is the area the right colour? Counts the pixels of the area near the taught hue and says yes when enough of them are.

![The Colour check block on the Vision canvas](img/vbc-colour.webp){: .sb-center}

![The window of the Colour check block: its settings on the left, its picture on the right](img/vb-colour.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Is the area the right colour? The block counts the pixels of the area whose hue lies within `tolerance` of the taught `hue` (and that are saturated and bright enough to have a colour at all - `sat_min`, `val_min`) and says *match* when their share reaches `min_share`. The right cap, the right label, the right wire, the right product on the belt.

Drag the area on the block's picture, then **right-click a point of the colour** to teach the hue; the swatch beside the setting shows it. The hue runs round the colour wheel (red 0, yellow 30, green 60, cyan 90, blue 120, magenta 150); a tolerance of 10 separates most colours, 20 is safer under changing light. A [White balance](/docs/vision/vision-balance/) before it keeps a yellow lamp from shifting the hues. The window frames the area green or red.

## Typical uses

- the right cap, label or sleeve on the product
- the right wire or the right component colour
- a colour code on a part or a crate

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | a colour picture |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `match` | yes/no | the share of the area in the taught colour reaches min_share |
| `share` | number | the share of the area in the taught colour, in percent |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 0 | px | left edge of the area |
| `y` | 0 .. 8192 | 0 | px | top edge of the area |
| `w` | 1 .. 8192 | 100 | px | width of the area |
| `h` | 1 .. 8192 | 100 | px | height of the area |
| `hue` | 0 .. 179 | 0 |  | the colour (red 0 |
| `tolerance` | 1 .. 90 | 10 |  | how far from the hue still counts |
| `sat_min` | 0 .. 255 | 60 |  | grays below this saturation never count |
| `val_min` | 0 .. 255 | 40 |  | pixels darker than this never count |
| `min_share` | 0 .. 100 | 50 | % | share of the area that must match |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## On the block's window

- **Drag on the picture** to set the area (`x`, `y`, `w`, `h`). The numbers follow and can still be typed.
- **Right-click a point** of the picture to take its colour: `hue` becomes that point's hue (the median of a 5 x 5 patch). A gray or dark point has no colour and is refused.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
