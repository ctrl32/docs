---
title: "Measurements: Circle (fit)"
slug: vision-circle_fit
section: "Vision"
order: 290
sidebar_position: 290
image: img/vbc-circle_fit.webp
image_alt: "The Circle (fit) block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Circle (fit)

**Measurements** · in the trade: *circle gauge, least-squares circle fit with outlier rejection* · in a project file: `circle_fit`

An edge on every ray of a ring, a least squares circle through them without the stray points - the diameter and the centre of a hole, a shaft, a lid, with roundness and a tolerance.

![The Circle (fit) block on the Vision canvas](img/vbc-circle_fit.webp){: .sb-center}

![The window of the Circle (fit) block: its settings on the left, its picture on the right](img/vb-circle_fit.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Measures ONE circle precisely: on every one of `rays` rays from the centre `cx`, `cy` between `r_min` and `r_max` the block looks for the edge, then fits a least-squares circle through the edge points with the stray ones rejected - a diameter and a centre to a fraction of a pixel, and *roundness* as how far the worst kept point lies off the circle. The diameter of a hole, a shaft, a lid, a bottle mouth; with a scale wired in, *diameter_mm*, and `min`/`max` make *ok* a tolerance check.

Set the ring (the centre roughly, the two radii well inside and outside the expected edge) by the numbers, or let a [Find circles](/docs/vision/vision-circles/) find the rough place first and feed its centre through variables. `direction` says whether the first edge from the outside counts (a part on its background) or from the inside (a hole); `polarity` which kind of edge. More rays give a steadier result and cost time in proportion; 36 is a good start, 90 for a precise diameter. *points* says how many rays contributed - a low number against the rays means the edge is weak or the ring is off.

## Typical uses

- the diameter of a hole, a shaft, a cap, a bottle mouth
- the centre of a round part for a positioning
- roundness as a quality figure

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture with the circle |
| `scale` | number (optional) | millimetres per pixel from a Ruler or a Plane block (optional) |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `found` | yes/no | enough edge points for a circle |
| `x` | number | the fitted centre, pixels from the left |
| `y` | number | the fitted centre, pixels from the top |
| `diameter` | number | the fitted diameter, in pixels |
| `diameter_mm` | number | the diameter through the scale (px when none) |
| `roundness` | number | how far the worst kept edge point lies off the circle, in pixels (0 = a perfect circle) |
| `points` | number | how many edge points the fit kept |
| `ok` | yes/no | the diameter lies between min and max |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `cx` | 0 .. 8192 | 320 | px | the ring's centre - roughly where the circle is |
| `cy` | 0 .. 8192 | 240 | px | the ring's centre |
| `r_min` | 1 .. 8192 | 40 | px | the ring's inner radius |
| `r_max` | 2 .. 8192 | 120 | px | the ring's outer radius |
| `rays` | 3 .. 360 | 36 |  | how many rays look for the edge |
| `direction` | out_in / in_out | out_in |  | the first edge from the outside (a part on a background) or from the inside (a hole) |
| `contrast` | 1 .. 255 | 40 |  | the jump in brightness that is the edge |
| `polarity` | any / dark_to_light / light_to_dark | any |  | which edges count |
| `min` | 0 .. 100000 | 0 |  | the diameter must be at least this (0 = no limit) - mm with a scale |
| `max` | 0 .. 100000 | 0 |  | the diameter must be at most this (0 = no limit) |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
