---
title: "Finding objects: Find by features"
slug: vision-features
section: "Vision"
order: 273
sidebar_position: 273
image: img/vbc-features.webp
image_alt: "The Find by features block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Find by features

**Finding objects** · in the trade: *feature matching (ORB keypoints)* · in a project file: `features`

Finds a taught picture even when it is turned or nearer or farther from the camera (ORB feature matching) - a logo, a printed mark, a part at any angle. Teach it by dragging over the part on the block's picture.

![The Find by features block on the Vision canvas](img/vbc-features.webp){: .sb-center}

![The window of the Find by features block: its settings on the left, its picture on the right](img/vb-features.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Finds a taught picture even when it is turned, nearer or farther from the camera, or partly covered (ORB feature matching): a logo, a printed mark, a part lying at any angle. The block picks distinctive points on the taught picture and on the current one, matches them, and from the matches works out where the taught thing is, how it is turned and how large it looks. [Find pattern](/docs/vision/vision-pattern/), which needs the same size and turn, is faster and more exact when the part always lies the same way; this block is for the part that does not.

Teach it by **dragging over the part on the block's picture**. The taught picture needs texture - print, edges, a logo; a plain surface has no features to match. `min_matches` says how many matching points make a find: raise it when the block finds the part where it is not. *scale* is in percent of the taught size, *angle* in degrees anticlockwise.

## Typical uses

- a logo or a printed mark at any angle
- a part nearer or farther from the camera
- a partly covered part located

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture to search |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `objects` | list of objects | the find as one object (its frame, angle and the match count as score) |
| `found` | yes/no | at least min_matches features matched |
| `x` | number | the found part's centre, pixels from the left |
| `y` | number | the found part's centre, pixels from the top |
| `angle` | number | how far the part is turned against the taught picture, in degrees |
| `scale` | number | how large the part looks against the taught picture, in percent |
| `matches` | number | how many features matched |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `pattern` | text | (empty) |  | the taught picture (one of the project's pictures) |
| `min_matches` | 4 .. 500 | 12 |  | at least this many matching features make a find |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## On the block's window

- **Drag over the part** on the picture: the cut-out becomes a picture of the project (an asset) and the setting `pattern` names it. Drag at least 8 x 8 pixels; teach on the test picture, not online.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
