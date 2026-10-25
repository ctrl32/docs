---
title: "Ready tools: Edge position"
slug: vision-edge
section: "Vision"
order: 299
sidebar_position: 299
image: img/vbc-edge.webp
image_alt: "The Edge position block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Edge position

**Ready tools** · in the trade: *edge position, edge detection along a scan direction* · in a project file: `edge`

Where is the edge? Walks across an area in one direction and reports the first place the brightness jumps.

![The Edge position block on the Vision canvas](img/vbc-edge.webp){: .sb-center}

![The window of the Edge position block: its settings on the left, its picture on the right](img/vb-edge.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Where is the edge? The block walks across an area in `direction` and reports the first place the brightness jumps by at least `contrast` - *position* is in pixels from the area's starting side. Where the material ends, where a web's edge runs, where a stack's top is, where a mark sits: one number, with *found* off when no jump reaches the contrast.

Drag the area on the block's picture across the edge, narrow in the other direction so that only the edge of interest is inside. A [Scale](/docs/vision/vision-scale/) after it turns the position into millimetres; a [Caliper](/docs/vision/vision-caliper/) finds ALL the edges along a line with their pitch, [Line (fit)](/docs/vision/vision-line_fit/) measures an edge's angle.

## Typical uses

- the edge of a web or a sheet for a guiding control
- the top of a stack
- the position of a mark or a cut

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture (a colour one is taken by its brightness) |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `found` | yes/no | an edge with at least the contrast was found |
| `position` | number | the first edge, pixels from the area's starting side |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 0 | px | left edge of the area |
| `y` | 0 .. 8192 | 0 | px | top edge of the area |
| `w` | 1 .. 8192 | 200 | px | width of the area |
| `h` | 1 .. 8192 | 20 | px | height of the area |
| `direction` | left_to_right / right_to_left / top_to_bottom / bottom_to_top | left_to_right |  | which way to walk |
| `contrast` | 1 .. 255 | 40 |  | the jump in brightness that is an edge |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## On the block's window

- **Drag on the picture** to set the area (`x`, `y`, `w`, `h`). The numbers follow and can still be typed.

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
