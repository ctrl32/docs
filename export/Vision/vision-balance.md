---
title: "Colour: White balance"
slug: vision-balance
section: "Vision"
order: 233
sidebar_position: 233
image: img/vbc-balance.webp
image_alt: "The White balance block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# White balance

**Colour** · in the trade: *white balance (gray-world)* · in a project file: `balance`

Takes a colour cast out of the picture (the gray-world rule) - a yellowish lamp or a bluish window stops shifting the colours a Colour block reads.

![The White balance block on the Vision canvas](img/vbc-balance.webp){: .sb-center}

![The window of the White balance block: its settings on the left, its picture on the right](img/vb-balance.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Takes a colour cast out of the picture. A yellowish lamp, a bluish window, a camera whose automatic white balance settled on the wrong thing - all of them shift every colour, and a [Colour check](/docs/vision/vision-colour/) taught in the morning fails under the evening light. The block assumes the picture is gray on average (the gray-world rule) and scales the three channels until it is; `strength` says how much of the correction is applied.

Use it when the light changes and the colours matter. A picture that really is mostly one colour (a whole red part filling the picture) fools the rule - crop to a window that shows the background too, or fix the camera's white balance on its page instead.

## Typical uses

- a Colour check that holds under a yellow lamp
- a camera whose automatic white balance drifts

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | a colour picture with a cast |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the picture with the cast taken out |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `strength` | 0 .. 100 | 100 | % | how much of the cast is taken out |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
