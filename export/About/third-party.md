---
title: "Third-party licences"
slug: third-party
section: "About"
order: 347
sidebar_position: 347
generator: tools/docs_export.py
---

# Third-party licences

ctrl32 is built on open-source components. Every one of them is under a
**permissive** licence — the kind that asks for a copyright notice and
nothing else — with two exceptions in the Linux runtime, listed in their
own section below, whose conditions fall on us and not on you.

!!! success "What this means for you"
    Nothing here obliges you to publish your project, your logic or your
    screens. You may sell projects with a ctrl32 board on them, keep your
    know-how to yourself, and you owe no fees to anyone on this page. The
    only obligation is ours: to keep the notices, which is what this page
    does.

## In the board

Everything that runs on the equipment.

| Component | Licence | What it does |
|:---|:---:|:---|
| ESP-IDF | Apache 2.0 | the operating system on ESP32 boards |
| FreeRTOS | MIT | task scheduling — the PLC cycle runs as one of them |
| LovyanGFX | BSD 2-clause | the rasteriser that draws the screens |
| lwIP | BSD 3-clause | the network stack (ethernet, WEBview, Modbus TCP) |
| STM32Cube HAL | BSD 3-clause | the hardware layer on STM32 boards |
| CMSIS | Apache 2.0 | the processor core headers on STM32 boards |
| Espressif hosted-WiFi components | Apache 2.0 | the WiFi of ESP32-P4 boards, which reaches the radio through a companion chip |
| cJSON | MIT | reads the small pieces of JSON the WEBview exchanges |

!!! note "The CANopen master is ours"
    ctrl32 does not use a third-party CANopen stack. The NMT master, SDO
    client, PDO mapping and the CiA 402 drive handling are our own code, so
    there is no licence on this page covering them.

## In the Linux runtime

The Linux runtime carries everything above that applies to a headless
device, and four components of its own.

| Component | Licence | What it does |
|:---|:---:|:---|
| open62541 | MPL 2.0 | the OPC UA server |
| OpenSSL | Apache 2.0 | the certificates of the OPC UA endpoints |
| OpenCV | Apache 2.0 | the camera picture and the image processing - with the libraries it carries (libjpeg-turbo, libpng, zlib, quirc; on 64-bit Arm also KleidiCV), each under its own permissive licence |
| SOEM | GPL 2.0 with the linking exception | the EtherCAT master |

!!! note "The two exceptions, and what they mean for you"
    open62541 is under the Mozilla Public License 2.0 and SOEM under the
    GPL 2.0 with an explicit linking exception. Both allow a proprietary
    program to link them; both ask that the sources of the component itself
    stay public, and they are — we ship them unmodified. Neither reaches
    your project, your logic or your screens, and there is nothing for you
    to publish or to sign. Selling a device as an EtherCAT master also
    requires a master licence from the EtherCAT Technology Group — a
    paperwork step on the vendor's side, not the user's.

EtherCAT® is a registered trademark and patented technology, licensed by Beckhoff Automation GmbH, Germany.

## In the editor

Everything that runs on your PC. None of it reaches the equipment.

| Component | Licence | What it does |
|:---|:---:|:---|
| Dear ImGui | MIT | the editor's user interface |
| SDL2 | zlib | window, input and the canvas the screens are drawn into |
| esp-serial-flasher | Apache 2.0 | writes the runtime to ESP32 boards |
| tree-sitter | MIT | parses Structured Text while you type |
| tree-sitter-iec61131-3-st | MIT | the IEC 61131-3 grammar for the above |
| yaml-cpp | MIT | reads and writes project files |
| stb_truetype | public domain | turns fonts into what the board displays |
| zlib | zlib | compresses the WEBview files |
| TweetNaCl | public domain | verifies licence signatures offline |

## In the browser

The WEBview page is written from scratch — plain TypeScript on a Canvas,
no framework. There is nothing third-party in it at all, which is also why
it stays under 20 kB compressed.

## Fonts

| Font | Licence | Used for |
|:---|:---:|:---|
| Noto Sans | SIL OFL 1.1 | the editor interface and board text |
| DejaVu Sans Mono | permissive (Bitstream Vera / DejaVu) | code and declarations |
| Tabler Icons | MIT | the icon set available to your screens |

All three may be redistributed with a commercial product.

!!! warning "Fonts are worth checking when you add your own"
    Graphics libraries often bundle fonts under mixed licences. ctrl32 ships
    only the three above, deliberately. If you add a font of your own to a
    project, its licence is yours to check — the editor bakes it into the
    pack and it travels to the board with everything else.

## What is deliberately not here

The obvious way to write firmware from a desktop application is to bundle
**esptool**, which is GPL-2.0. Shipping it would place obligations on the
whole product — the very thing this page exists to rule out. ctrl32 uses
Espressif's **esp-serial-flasher** (Apache 2.0) for ESP32 boards and its
own ST-LINK client for STM32 boards, so no GPL component is distributed
with the editor or the runtime.

## Full licence texts

The complete texts are installed with the editor:

```
C:\Program Files\ctrl32\licenses\third-party-licenses.txt
```

One file, every component, each notice reproduced verbatim, with a summary
table at the top saying which licence each part is under and whether it runs
in the board or in the editor. The file is generated from the build, and the
release refuses to produce an installer when any component's text is missing
— a licence file with a gap in it is worse than none, because it looks
complete.

!!! note "This page is not legal advice"
    It describes what ctrl32 contains and under what terms those parts were
    obtained. If your industry or your customer requires a formal licence
    audit, have this reviewed by a lawyer — that is a different document.
