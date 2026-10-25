---
title: "Filters: Combine pictures"
slug: vision-combine
section: "Vision"
order: 246
sidebar_position: 246
image: img/vbc-combine.webp
image_alt: "The Combine pictures block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Combine pictures

**Filters** · in the trade: *image arithmetic, boolean image operations* · in a project file: `combine`

Puts two pictures of the same size together - added, subtracted, the darker or the lighter of the two, a blend, or the black-and-white ones by AND / OR / XOR.

![The Combine pictures block on the Vision canvas](img/vbc-combine.webp){: .sb-center}

![The window of the Combine pictures block: its settings on the left, its picture on the right](img/vb-combine.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Puts two pictures of the same size together point by point. `add` and `subtract` do what they say; `min` keeps the darker of the two and `max` the lighter; `blend` mixes them with `share` percent of the first; `and_`, `or_` and `xor_` are for black-and-white pictures - white where both are white, where either is, where exactly one is.

AND of two colour ranges finds what is red AND bright; OR of two thresholds finds the parts of two shades at once; a picture AND a mask keeps only what lies inside the mask ([Mask](/docs/vision/vision-mask/) does that in one block, with a colour picture too). The two pictures must have the same size - crop or resize them alike.

## Typical uses

- red AND bright with two colour ranges
- two shades of parts with OR
- a picture blended with a reference for the operator

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `a` | picture | the first picture |
| `b` | picture | the second picture, the same size |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the two put together as `mode` says |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `mode` | add / subtract / and_ / or_ / xor_ / min / max / blend | add |  | how the two are put together (and_ / or_ / xor_ for black-and-white pictures) |
| `share` | 0 .. 100 | 50 | % | the first picture's share in a blend |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
