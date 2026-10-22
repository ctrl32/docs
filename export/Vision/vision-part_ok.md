---
title: "Measurements: Part in place"
slug: vision-part_ok
section: "Vision"
order: 294
sidebar_position: 294
image: img/vbc-part_ok.webp
image_alt: "The Part in place block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Part in place

**Measurements** · in the trade: *position and size verification, presence of a feature* · in a project file: `part_ok`

The largest dark (or light) object in a window, judged by where it sits and how big it is - a cap on a bottle, a seal in its seat, a label on its place.

![The Part in place block on the Vision canvas](img/vbc-part_ok.webp){: .sb-center}

![The window of the Part in place block: its settings on the left, its picture on the right](img/vb-part_ok.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Is the part where it belongs, and is it the right size? The block takes the largest dark (or light - `polarity`) blob in a window, judged against `threshold`, and compares its centre with where it should be (`ex`, `ey`, within `pos_tol` pixels) and its frame with the size it should have (`ew` x `eh`, within `size_tol` percent). A cap on a bottle, a seal in its seat, a label on its place, a lid on a box, a component in its footprint - one block, one *ok*.

The window is dragged on the block's picture round the place the part belongs. Leave `ex`/`ey` at 0 for "the window's centre" and `ew`/`eh` at 0 for "any size"; read the measured *cw*, *ch* on a good part and type them when the size matters. `min_area` leaves noise out, `max_area` leaves the background out when the threshold catches it. *dx*, *dy* say how far off the part sits - a trend of them shows a feeder drifting.

## Typical uses

- a cap on a bottle, a lid on a box, a seal in its seat
- a label or a print at its place
- a component in its footprint

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture with the window |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `found` | yes/no | a blob of at least min_area was found in the window |
| `cx` | number | the part's centre, pixels from the left |
| `cy` | number | the part's centre, pixels from the top |
| `cw` | number | the width of the part's frame |
| `ch` | number | the height of the part's frame |
| `dx` | number | how far the centre sits right of where it should be |
| `dy` | number | how far below |
| `ok` | yes/no | found, within pos_tol of its place, and within size_tol of its size |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 0 | px | left edge of the window |
| `y` | 0 .. 8192 | 0 | px | top edge of the window |
| `w` | 1 .. 8192 | 200 | px | width |
| `h` | 1 .. 8192 | 200 | px | height |
| `polarity` | dark / light | dark |  | the part is darker or lighter than the threshold |
| `threshold` | 0 .. 255 | 127 |  | the brightness that separates the part from its background |
| `min_area` | 0 .. 100000000 | 50 | px | a smaller blob is noise |
| `max_area` | 0 .. 100000000 | 0 | px | a bigger blob is not the part (0 = no limit) |
| `ex` | 0 .. 8192 | 0 | px | where the part's centre should be (0 with ey = the window's centre) |
| `ey` | 0 .. 8192 | 0 | px | where the part's centre should be |
| `pos_tol` | 0 .. 8192 | 20 | px | how far off the centre may sit |
| `ew` | 0 .. 8192 | 0 | px | the width the part should have (0 = any) |
| `eh` | 0 .. 8192 | 0 | px | the height the part should have (0 = any) |
| `size_tol` | 0 .. 100 | 20 | % | how much the size may differ |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## On the block's window

- **Drag on the picture** to set the area (`x`, `y`, `w`, `h`). The numbers follow and can still be typed.

## Used in

- Bottle check - a shipped example project

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
