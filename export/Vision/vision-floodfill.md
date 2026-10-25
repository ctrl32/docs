---
title: "Finding objects: Fill from point"
slug: vision-floodfill
section: "Vision"
order: 272
sidebar_position: 272
image: img/vbc-floodfill.webp
image_alt: "The Fill from point block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Fill from point

**Finding objects** · in the trade: *region growing (flood fill)* · in a project file: `floodfill`

Starts at a point and takes every neighbouring point of a similar shade - the whole part under the point becomes a white shape, whatever its outline.

![The Fill from point block on the Vision canvas](img/vbc-floodfill.webp){: .sb-center}

![The window of the Fill from point block: its settings on the left, its picture on the right](img/vb-floodfill.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Starts at one point and takes every neighbouring point of a similar shade, and their neighbours, until the shade changes by more than `tolerance`: the whole part under the point becomes a white shape, whatever its outline, and the rest stays black. It is the way to pick a part by one point - "whatever lies under the gripper", "the surface the mark is on" - without a threshold that would also pick everything else of that shade.

*area* is the size of the filled shape, in pixels. The point is typed and may come from a variable (the place another block found). A lower tolerance stops at fainter changes; a shaded part wants a higher one.

## Typical uses

- the whole part under a point, whatever its outline
- the surface a mark is on, as a mask
- the area of a region picked by one point

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | a gray or colour picture |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | black and white: the filled part white |
| `area` | number | the filled part's area, in pixels |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 320 | px | the starting point |
| `y` | 0 .. 8192 | 240 | px | the starting point |
| `tolerance` | 0 .. 255 | 20 |  | how different a neighbour's shade may be and still belong |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
