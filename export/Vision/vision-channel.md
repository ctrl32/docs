---
title: "Colour: One channel"
slug: vision-channel
section: "Vision"
order: 232
sidebar_position: 232
image: img/vbc-channel.webp
image_alt: "The One channel block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# One channel

**Colour** · in the trade: *colour plane extraction* · in a project file: `channel`

Takes one channel of the colour picture as a gray one - the red, the saturation, the lightness ... - the way to make a colour into something Threshold can cut.

![The One channel block on the Vision canvas](img/vbc-channel.webp){: .sb-center}

![The window of the One channel block: its settings on the left, its picture on the right](img/vb-channel.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Takes one channel of a colour picture as a gray picture: the red, the green or the blue part, or the hue, the saturation, the value or the lightness of each point. It is how a colour becomes something a [Threshold](/docs/vision/vision-threshold/) can cut - the red channel makes a red print on a white label stand out as dark, the saturation channel makes any coloured mark bright on a gray background, whatever the colour.

Hue is stretched from the colour wheel to 0..255 so that it fits a gray picture; the lightness channel is the plain brightness, the same as [Grayscale](/docs/vision/vision-gray/). Try the channels on the block's picture: the right one shows the thing you want as the clearest contrast.

## Typical uses

- a red print on a white label as dark on light
- any coloured mark as bright on gray (saturation)
- the plane with the best contrast for a threshold

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | a colour picture |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the chosen channel, as a gray picture |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `which` | blue / green / red / hue / saturation / value / lightness | value |  | which channel (hue is stretched to 0..255 round the colour wheel) |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
