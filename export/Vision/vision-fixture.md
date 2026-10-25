---
title: "Geometry: Fixture"
slug: vision-fixture
section: "Vision"
order: 225
sidebar_position: 225
image: img/vbc-fixture.webp
image_alt: "The Fixture block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Fixture

**Geometry** · in the trade: *fixturing, part location, pattern-based alignment* · in a project file: `fixture`

Finds the part by a taught picture and shifts the whole picture so the part sits where it was when taught - every later block keeps its areas wherever the part lies on the belt. Teach by dragging over the part on the block's picture.

![The Fixture block on the Vision canvas](img/vbc-fixture.webp){: .sb-center}

![The window of the Fixture block: its settings on the left, its picture on the right](img/vb-fixture.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Makes every later block independent of where the part lies. Taught once by a drag over the part on the block's picture, the block remembers the part's picture and where it was. On every later picture it looks for the part again, measures how far it moved (and, with `max_angle` above 0, how far it turned) and shifts the whole picture back so that the part sits exactly where it was when taught. A window drawn on the cap finds the cap wherever the bottle stopped; a caliper drawn across the part measures the part, not the belt beside it.

`min_score` says how alike the part must look to count as found; a part the block does not find leaves the picture as it is and answers *found* off - the blocks after it still run, so a program can tell "no part" from "a bad part". `max_angle` lets the part lie turned: the block tries the taught picture at every `angle_step` from -max_angle to +max_angle and keeps the best, which costs time in proportion - leave it at 0 when the part never turns.

The window shows the picture after the shift with the taught part framed and the score; *dx*, *dy* and *angle* say what was undone.

## Typical uses

- a bottle that stops anywhere on the belt
- a part placed by hand on a tray
- every measuring window locked to the part, not to the camera

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture in which the part lies anywhere |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the picture shifted (and turned) back so that the part sits where it was taught; unchanged when not found |
| `found` | yes/no | the part was found with at least min_score |
| `dx` | number | how far the part had moved to the right, in pixels (undone in the output) |
| `dy` | number | how far the part had moved down, in pixels |
| `angle` | number | how far the part had turned, in degrees (0 when max_angle is 0) |
| `score` | number | how alike the part looked, in percent |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `pattern` | text | (empty) |  | the taught picture of the part (a picture asset of the project) |
| `min_score` | 1 .. 100 | 70 | % | how alike the part must look to count as found |
| `ref_x` | 0 .. 8192 | 0 | px | where the taught picture's centre was at the teach (set by the teach) |
| `ref_y` | 0 .. 8192 | 0 | px | where the taught picture's centre was at the teach (set by the teach) |
| `max_angle` | 0 .. 45 | 0 | deg | how far the part may lie turned (0 = it never turns - one match |
| `angle_step` | 0.1 .. 10 | 1 | deg | the step of the turn search - a finer step costs time |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## On the block's window

- **Drag over the part** on the picture: the cut-out becomes a picture of the project and the setting `pattern` names it; `ref_x` and `ref_y` take the centre of the drag, which is where the part is put back on every later picture.

## Used in

- Bottle check - a shipped example project

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
