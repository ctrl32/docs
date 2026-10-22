---
title: "Finding objects: Pick object"
slug: vision-pick
section: "Vision"
order: 265
sidebar_position: 265
image: img/vbc-pick.webp
image_alt: "The Pick object block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Pick object

**Finding objects** · in the trade: *blob result extraction* · in a project file: `pick`

Takes one object of a list - number 0 is the first after sorting - and gives its numbers.

![The Pick object block on the Vision canvas](img/vbc-pick.webp){: .sb-center}

![The window of the Pick object block: its settings on the left, its picture on the right](img/vb-pick.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Takes one object out of a list and gives its numbers: the centre, the frame, the radius, the angle, the area, and the score when the list came from a finder that scores. `index` says which one - 0 is the first after the list's sorting, so a list sorted left to right makes "the leftmost part" index 0 whatever its size.

Its outputs are the usual way an object's numbers reach a variable, a [Distance of points](/docs/vision/vision-points_dist/), a [Scale](/docs/vision/vision-scale/) or an [In range](/docs/vision/vision-in_range/). *found* is off when the list is shorter than the index, and the numbers are then 0.

## Typical uses

- one object's numbers into variables
- the leftmost part's centre for a Distance of points
- the largest part's size for a limit

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `objects` | list of objects | the list to pick from |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `found` | yes/no | the list has an object at that index |
| `x` | number | the object's centre, pixels from the left |
| `y` | number | the object's centre, pixels from the top |
| `w` | number | the width of the object's frame |
| `h` | number | the height of the object's frame |
| `r` | number | the object's radius (a circle, a marker) or half its larger side |
| `angle` | number | the object's angle, in degrees |
| `area` | number | the object's area, in pixels |
| `score` | number | the finder's score for the object, in percent (0 for a finder that does not score) |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `index` | 0 .. 10000 | 0 |  | which object (0 = the first) |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
