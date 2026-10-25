---
title: "Ready tools: Read code"
slug: vision-code
section: "Vision"
order: 300
sidebar_position: 300
image: img/vbc-code.webp
image_alt: "The Read code block on the Vision canvas"
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Read code

**Ready tools** · in the trade: *1D/2D code reading, symbology, module size* · in a project file: `code`

Reads a QR code, a barcode, a DataMatrix, a PDF417 or an Aztec code and checks it against the expected text.

![The Read code block on the Vision canvas](img/vbc-code.webp){: .sb-center}

![The window of the Read code block: its settings on the left, its picture on the right](img/vb-code.webp){: .sb-center}

## Where it runs

| Linux runtime, 64-bit | Linux runtime, 32-bit ARM | ESP32 boards | STM32 |
|:---:|:---:|:---:|:---:|
| yes | - | - | - |

**Needs:** a camera of the project (a USB camera or a stream address).

## Description

Reads a code on the part and checks it: a QR code, a one-dimensional barcode (EAN, UPC, Code 128, Code 39, ITF, Codabar, GS1 DataBar), a DataMatrix, a PDF417 or an Aztec code - `kind` picks the symbology, *any* tries every one. *text* is what the code says (into a STRING variable), *number* the same as a number when it is one, *format* which symbology was read, and *match* whether the text equals `expect` - the lot code of the recipe, a STRING variable bound to the setting, so the camera verifies that the right product is on the line.

A code reads when its smallest element - the module - is at least two pixels wide in the picture, better three, and in focus; the reader searches the whole picture it receives, turned or not, so a [Crop](/docs/vision/vision-crop/) to the label's area makes it faster and surer. A [Gamma](/docs/vision/vision-gamma/), a [Stretch contrast](/docs/vision/vision-normalize/) and a [Sharpen](/docs/vision/vision-sharpen/) before it, each bound to a variable the operator turns while watching the preview, rescue a label under poor light - the shipped reTerminal example is built that way. A code too small for the camera is a matter of distance or of the lens, not of settings: at 30 cm an ordinary USB camera resolves a 37 mm EAN, not a 25 mm one.

## Typical uses

- verify the lot or the product code on every pack
- read a serial number into a STRING variable for the traceability record
- a QR code on a pallet or a tray that tells the program what to do

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture with the code |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `found` | yes/no | a code of the chosen kind was read |
| `match` | yes/no | found, and the text equals expect (always true with expect empty) |
| `number` | number | the code's text as a number when it is one, else 0 |
| `text` | text | what the code says (a STRING variable takes it) |
| `format` | text | the symbology that was read - QRCode, EAN13, Code128, DataMatrix ... |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `kind` | qr / barcode / datamatrix / pdf417 / aztec / any | qr |  | what kind of code - barcode is any one-dimensional code (EAN |
| `expect` | text | (empty) |  | the text the code must carry (empty = any code) |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](/docs/vision/#the-blocks-window)). A text setting takes a STRING variable the same way.

## Used in

- Bottle check - a shipped example project
- The reTerminal with EtherCAT (the code reader) - a shipped example project

---

Every block: [Vision blocks](/docs/vision/vision-blocks/) · how a program is drawn and what its window shows: [Vision](/docs/vision/) · the cameras: [Cameras](/docs/vision/cameras/)
