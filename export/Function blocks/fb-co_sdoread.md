---
title: "CANopen: CO_SDOREAD"
slug: fb-co_sdoread
section: "Function blocks"
order: 180
sidebar_position: 180
image: img/blk-sdor-ld.webp
image_alt: "CO_SDOREAD in the editor"
generator: tools/docs_export.py
---

# CO_SDOREAD

Reads an object of the drive over SDO at startup.

![CO_SDOREAD on a rung](img/blk-sdor-ld.webp){: .sb-center}

![CO_SDOREAD on a WEBview screen](img/blk-sdor-web.webp){: .sb-center}

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | - |

**Needs:** a CANopen device on the CAN bus.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `INDEX` | parameter | REAL | 0 | Object index. |
| `SUB` | parameter | REAL | 0 | Object subindex. |
| `OUT` | output | REAL | - | The value read. |

## Description

Bound to an **axis** at the call: `rd(AXIS := 0, …)`.

Startup only, for the same reason as CO_SDOWRITE: an SDO exchange takes
milliseconds and waits for an answer, and in the cycle it would break
the cycle timing. Use it to read a nameplate value, a motor rating, a
firmware revision - something you want in the program but that does not
change while it runs.

---

Every block of the family: [CANopen](/docs/blocks/blocks-can/) · every block: [Function blocks](/docs/blocks/)
