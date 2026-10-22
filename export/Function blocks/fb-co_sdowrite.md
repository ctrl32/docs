---
title: "CANopen: CO_SDOWRITE"
slug: fb-co_sdowrite
section: "Function blocks"
order: 179
sidebar_position: 179
image: img/blk-sdow-web.webp
image_alt: "CO_SDOWRITE in the editor"
generator: tools/docs_export.py
---

# CO_SDOWRITE

Writes an object of the drive over SDO - at startup only, never in the cycle.

![CO_SDOWRITE on a WEBview screen](img/blk-sdow-web.webp){: .sb-center}

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | - |

**Needs:** a CANopen device on the CAN bus.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN` | input | REAL | - | The value. |
| `INDEX` | parameter | REAL | 0 | Object index. |
| `SUB` | parameter | REAL | 0 | Object subindex. |
| `VALUE` | parameter | REAL | 0 | The value written. |
| `SIZE` | parameter | REAL | 1 | Byte width of the object. |

## Description

Bound to an **axis** at the call: `sdo(AXIS := 0, …)`.

**This runs at startup only.** The project compiler turns it into a
startup record; it never executes inside the cycle.

That restriction is the point. An SDO exchange takes milliseconds and
involves waiting for an answer - do it in the cycle and the cycle timing
is gone, non-reproducibly, in a way that shows up as jitter nobody can
explain. Parameterise at startup; use PDOs for anything cyclic.

**What it is for:** the settings a drive needs before it will behave -
switching the i550 into CiA 402 mode, setting a ramp, choosing a
reference source.

See [Buses](/docs/buses/) for wiring, node IDs and termination.

---

Every block of the family: [CANopen](/docs/blocks/blocks-can/) · every block: [Function blocks](/docs/blocks/)
