---
title: "Finding objects: Find chessboard"
slug: vision-chessboard
section: "Vision"
order: 274
sidebar_position: 274
image: img/vbc-chessboard.webp
image_alt: "The Find chessboard block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Find chessboard

**Finding objects** · in the trade: *calibration target detection* · in a project file: `chessboard`

Finds the inner corners of a chessboard in the picture - the pattern a lens calibration and a camera-to-table check are done with.

![The Find chessboard block on the Vision canvas](img/vbc-chessboard.webp){: .sb-center}

![The window of the Find chessboard block: its settings on the left, its picture on the right](img/vb-chessboard.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Finds the inner corners of a chessboard in the picture and gives them as a list of points, row by row. A chessboard is the pattern a lens calibration and a camera-to-table check are done with - [Lens correction](/docs/vision/vision-undistort/) and [Plane from a board](/docs/vision/vision-world/) find it themselves with their buttons; this block is for seeing whether the board is found at all (the window draws the corners), for checking that it is still where it was, and for your own measurements between its corners.

`cols` x `rows` are the INNER corners - a board of 10 x 7 squares has 9 x 6. The board must be fully in the picture, flat, and sharp.

## Typical uses

- is the calibration board found before a calibration
- has the camera moved since the plane was taught
- your own measurements between known corners

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | a gray or colour picture with the board |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `found` | yes/no | the whole board with those corners was found |
| `objects` | list of objects | the inner corners, row by row from the top-left one |
| `count` | number | how many corners (cols x rows when found, else 0) |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `cols` | 2 .. 30 | 9 |  | inner corners across |
| `rows` | 2 .. 30 | 6 |  | inner corners down |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
