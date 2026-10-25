---
title: "Measurements: Compare with taught"
slug: vision-golden
section: "Vision"
order: 289
sidebar_position: 289
image: img/vbc-golden.webp
image_alt: "The Compare with taught block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Compare with taught

**Measurements** · in the trade: *golden template comparison, image subtraction* · in a project file: `golden`

Compares an area with the same area taught on a good part and says how much differs - a missing print, a wrong label, a scratch. Teach by dragging over the area on the block's picture.

![The Compare with taught block on the Vision canvas](img/vbc-golden.webp){: .sb-center}

![The window of the Compare with taught block: its settings on the left, its picture on the right](img/vb-golden.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Compares an area with the same area taught on a good part - the golden template - and says how much differs: a missing print, a wrong label, a scratch, a bent pin, a lead that is not there. The taught picture is subtracted from the current area point by point; a point that differs by more than `level` counts, and *diff* is the share of such points in percent. *ok* is on while the share stays under `max_diff`; the picture output shows the differences in white, so the window and a screen show WHERE the part differs.

Teach by dragging over the area on the block's picture: the drag sets the area and stores its picture as the template. The part must lie exactly as taught - a [Fixture](/docs/vision/vision-fixture/) before it takes care of that - and the light must be steady, or the whole area "differs"; a [Stretch contrast](/docs/vision/vision-normalize/) before both the teach and the check makes it forgiving of a lamp that dims. Start with `level` 40 and `max_diff` 5 %, then read *diff* on good and on bad parts and set the limit between.

## Typical uses

- a missing or wrong print, a missing component
- a scratch or a dent on a known surface
- anything that must look exactly like the good part

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture the area is compared on |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `ok` | yes/no | the differing share is at most max_diff |
| `diff` | number | the share of points that differ, in percent of the area |
| `out` | picture | black and white: white where the area differs from the template |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `pattern` | text | (empty) |  | the taught picture of the area (one of the project's pictures) |
| `x` | 0 .. 8192 | 0 | px | left edge of the area |
| `y` | 0 .. 8192 | 0 | px | top edge of the area |
| `w` | 1 .. 8192 | 200 | px | width of the area |
| `h` | 1 .. 8192 | 200 | px | height of the area |
| `level` | 1 .. 255 | 40 |  | a point that differs by more than this counts |
| `max_diff` | 0 .. 100 | 5 | % | the share of differing points that is still fine |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## On the block's window

- **Drag over the area** on the picture: the drag sets the area (`x`, `y`, `w`, `h`) and stores its picture as the template the setting `pattern` names.
- **Drag on the picture** to set the area (`x`, `y`, `w`, `h`). The numbers follow and can still be typed.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
