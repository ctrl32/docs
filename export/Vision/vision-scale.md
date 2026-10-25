---
title: "Measurements: Scale"
slug: vision-scale
section: "Vision"
order: 281
sidebar_position: 281
image: img/vbc-scale.webp
image_alt: "The Scale block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Scale

**Measurements** · in the trade: *pixel-to-unit conversion, calibration factor* · in a project file: `scale`

Turns a number of pixels into millimetres (or any unit) - value x factor + offset. Connect a Ruler's mm_per_px to `factor_in` and the factor is measured, not typed.

![The Scale block on the Vision canvas](img/vbc-scale.webp){: .sb-center}

![The window of the Scale block: its settings on the left, its picture on the right](img/vb-scale.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Turns a number of pixels into millimetres - or inches, degrees of a dial, any unit: the result is `v` x `factor` + `offset`. Wire a [Ruler](/docs/vision/vision-ruler/)'s *mm_per_px* or a [Plane from a board](/docs/vision/vision-world/)'s *mm_per_px* into `factor_in` and the factor is measured rather than typed; the typed `factor` is used when nothing feeds that input.

Every measuring block of the v11 table ([Fill level](/docs/vision/vision-level/), [Caliper](/docs/vision/vision-caliper/), [Circle (fit)](/docs/vision/vision-circle_fit/) ...) takes a scale input of its own and answers in millimetres directly; the Scale block is for the older measurements and for any number of your own.

## Typical uses

- a width measured in pixels shown in millimetres
- the position of an edge as a distance from the belt's edge
- any linear conversion of a measured number

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `v` | number | the number to convert, usually pixels |
| `factor_in` | number (optional) | the factor from a Ruler or a Plane block (used instead of the typed factor when fed) |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `value` | number | v x factor + offset |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `factor` | -1000000 .. 1000000 | 1 |  | units per pixel |
| `offset` | -1000000 .. 1000000 | 0 |  | added after the factor |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
