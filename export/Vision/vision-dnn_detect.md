---
title: "Learned models: Detect (model)"
slug: vision-dnn_detect
section: "Vision"
order: 303
sidebar_position: 303
image: img/vbc-dnn_detect.webp
image_alt: "The Detect (model) block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Detect (model)

**Learned models** · in the trade: *deep learning inference, object detection, ONNX* · in a project file: `dnn_detect`

Runs a trained detection network (an ONNX model imported into the project - YOLO, SSD) on the picture and gives every object it finds as a list with its class, score and place. For what a rule cannot describe - mixed parts, a scratch of any shape, a person in the cell.

![The Detect (model) block on the Vision canvas](img/vbc-dnn_detect.webp){: .sb-center}

![The window of the Detect (model) block: its settings on the left, its picture on the right](img/vb-dnn_detect.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project and an ONNX model added to the project as an asset.

## Description

Runs a trained detection network - an ONNX model imported into the project - and gives every object it finds as a list with its class, its score and its place: people in a cell, mixed parts on a belt, bottles, boxes, vehicles, whatever the model was trained on. *count*, and the best detection's *class*, *label*, *score*, *x*, *y* are outputs of their own; the list goes on to [Pick object](/docs/vision/vision-pick/), [Nearest object](/docs/vision/vision-nearest/), [Check objects](/docs/vision/vision-objcheck/). `only` keeps one class (`person` for a people counter), `min_score` drops weak detections and `overlap` merges boxes of one object.

The settings describe the model's input like the classifier's; `layout` says how its output is read - *auto* reads it off the output's shape for SSD and the YOLO families, a YOLOX export keeps its boxes in grid units and must be named. The shipped People counter carries YOLOX-Nano - 3.6 MB, 80 everyday classes - with every setting right for it: open it and change `only` to count cars or bottles with the same block. A small detector takes a few hundred milliseconds on a Raspberry Pi 4: run it on a trigger or every second, not ten times a second. The model file carries its own licence.

## Typical uses

- people in a cell or a zone - a count, a presence
- mixed products on one belt, each with its place
- a defect or a foreign object of any shape

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture (resized to the model's input by the block) |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `objects` | list of objects | every detection as an object - its class in the number, its score, its box as the frame |
| `count` | number | how many detections (of the `only` class when set) |
| `found` | yes/no | at least one detection reached min_score |
| `class` | number | the best detection's class number |
| `label` | text | its name from the labels setting |
| `score` | number | the best detection's score, in percent |
| `x` | number | the best detection's centre, pixels from the left |
| `y` | number | the best detection's centre, pixels from the top |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `model` | text | (empty) |  | the model (an .onnx file imported into the project) |
| `labels` | text | (empty) |  | the class names in the model's order, separated by commas (empty = the class number) |
| `width` | 8 .. 2048 | 640 | px | the model's input width |
| `height` | 8 .. 2048 | 640 | px | the model's input height |
| `scale` | 0 .. 1 | 0.003922 |  | the input is multiplied by this (0.003922 = 1/255 for a model trained on 0..1) |
| `mean` | 0 .. 255 | 0 |  | taken off every channel before scaling |
| `swap_rb` | yes / no | yes |  | the model wants RGB (most do) rather than BGR |
| `min_score` | 0 .. 100 | 50 | % | a detection below this is dropped |
| `overlap` | 0 .. 100 | 45 | % | two boxes overlapping more than this are one object |
| `layout` | auto / ssd / yolov5 / yolov8 / yolox | auto |  | the model's output layout (auto reads it off the output's shape; a YOLOX export keeps its boxes in grid units and must be named - the shipped people counter is one) |
| `only` | text | (empty) |  | only detections with this label count (empty = every class) - `person` for a people counter |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## On the block's window

- **Import model...** - a button in the window: an `.onnx` file (at most 64 MB) becomes a file of the project and the setting `model` names it.

## Used in

- People counter - a shipped example project

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
