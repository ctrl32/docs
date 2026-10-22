---
title: "Geometry: Lens correction"
slug: vision-undistort
section: "Vision"
order: 223
sidebar_position: 223
image: img/vbc-undistort.webp
image_alt: "The Lens correction block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Lens correction

**Geometry** · in the trade: *intrinsic calibration, lens distortion correction* · in a project file: `undistort`

Takes the barrel or pincushion of a wide lens out of the picture, so straight edges are straight and a Ruler holds across the whole picture. The numbers come from a lens calibration (a chessboard in front of the camera).

![The Lens correction block on the Vision canvas](img/vbc-undistort.webp){: .sb-center}

![The window of the Lens correction block: its settings on the left, its picture on the right](img/vb-undistort.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Takes the barrel or the pincushion of a wide-angle lens out of the picture, so that a straight edge is straight and a [Ruler](/docs/vision/vision-ruler/) taught in the middle of the picture holds at its corners too. A cheap wide lens bends a straight belt edge by tens of pixels across the picture; a caliper or a line fit measured on it is wrong by that much.

The eight numbers are the lens's calibration. They are not typed: hold a chessboard in front of the camera, take a picture, set how many inner corners the board has and press **Calibrate from this picture** in the block's window - the block finds the corners and fills the numbers in. One picture gives a usable correction; a second and third picture, with the board turned and nearer the corners, give a better one (press the button again on each; the numbers are refined).

The correction belongs to the lens and the resolution: a new camera, a new lens or another picture size wants a new calibration. The numbers are saved with the project.

## Typical uses

- straight belt edges with a wide-angle lens
- a Ruler that holds across the whole picture
- measurements near the corners of the picture

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture straight from the camera |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the picture with the lens distortion taken out, the same size |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `fx` | 1 .. 100000 | 1000 | px | focal length across |
| `fy` | 1 .. 100000 | 1000 | px | focal length down |
| `cx` | 0 .. 8192 | 640 | px | the optical centre |
| `cy` | 0 .. 8192 | 360 | px | the optical centre |
| `k1` | -5 .. 5 | 0 |  | radial distortion |
| `k2` | -5 .. 5 | 0 |  | radial distortion |
| `p1` | -1 .. 1 | 0 |  | tangential distortion |
| `p2` | -1 .. 1 | 0 |  | tangential distortion |
| `board_cols` | 2 .. 30 | 9 |  | inner corners across of the chessboard the calibration is taken from (Calibrate on the block's picture) |
| `board_rows` | 2 .. 30 | 6 |  | inner corners down of that chessboard |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## On the block's window

- **Calibrate from this picture** - a button in the window: with a chessboard of `board_cols` x `board_rows` inner corners in the picture it finds the corners and fills `fx`, `fy`, `cx`, `cy`, `k1` and `k2` in (`p1`, `p2` stay 0). Press it on two or three pictures with the board in different places for a better result.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
