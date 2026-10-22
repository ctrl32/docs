---
title: "Filters: Motion"
slug: vision-motion
section: "Vision"
order: 240
sidebar_position: 240
image: img/vbc-motion.webp
image_alt: "The Motion block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Motion

**Filters** · in the trade: *motion detection, frame differencing* · in a project file: `motion`

Where the picture changed since the last run - a mask of what moved and how much of the picture it is. The first run after a start has nothing to compare and answers nothing moved.

![The Motion block on the Vision canvas](img/vbc-motion.webp){: .sb-center}

![The window of the Motion block: its settings on the left, its picture on the right](img/vb-motion.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Compares the picture with the one the block saw at its last run and marks what changed. The output is a mask of the moving things (white where the picture changed by more than `level`), *share* says how much of the picture moved and *moved* comes on when that share reaches `min_share`. A belt that should be running, a door that should stay closed, a hand in the cell, a part that has not stopped yet - all of them are motion.

The first run after a start has nothing to compare with and answers nothing moved. The block compares with its OWN last picture, so a program that runs every 100 ms sees what moved in the last 100 ms; a program that runs on a trigger sees what moved since the last trigger. A camera on automatic exposure makes the whole picture "move" when the light changes - fix the exposure on the camera's page.

## Typical uses

- a belt that should be running (or not)
- a hand or a person in the cell
- a part that has not come to rest yet

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the current picture |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | black and white: white where the picture changed since the last run |
| `share` | number | the share of the picture that changed, in percent |
| `moved` | yes/no | the changed share reached min_share |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `level` | 1 .. 255 | 25 |  | a change above this counts |
| `min_share` | 0 .. 100 | 1 | % | this much of the picture must change to say moved |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
