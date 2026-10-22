---
title: "STM32"
slug: setup-stm32
section: "Getting started"
order: 5
sidebar_position: 5
generator: tools/docs_export.py
---

# STM32: from the box to a running program

This page takes an STM32 board of the catalog - the STM32F746G-DISCO -
from the box to a program running on it and watched live from the
editor. The board's ST-LINK connector is power, programmer and serial
console in one USB cable; there are no boot buttons and no jumpers.

**You need**

- a Windows PC with the ctrl32 editor installed,
- the board and a USB cable into its **ST-LINK** connector,
- for the network road, an Ethernet cable.

---

## 1. Install the editor

Run `ctrl32-setup-<version>.exe`. It installs the editor, the board
catalog, the runtime for every supported board and the sample projects.
There is nothing else to install.

---

## 2. The ST-LINK driver

Windows Update installs the ST-LINK driver the first time the board is
plugged in. A PC without internet needs ST's *ST-LINK USB driver* package
installed beforehand. The board then shows a virtual COM port.

---

## 3. Make the project

*New project* (Ctrl+N), a name, and **STM32F746G-DISCO** as the hardware.

![The New project wizard with a board picked](img/newproj-board.webp){: .sb-center}

Tick what the project does - screens, WEBview, the first program in
ladder or ST, Modbus, MQTT. Every part can be added or removed later from
the project tree. *Create project* writes and opens it.

---

## 4. Flash the runtime

1. Connect the ST-LINK cable and pick the board's COM port in the
   toolbar's **port picker**.
2. Click the board in the project tree and press **Flash runtime**.

![The Flash runtime dialog](img/deploy-runtime.webp){: .sb-center}

The runtime is written through the ST-LINK in two parts: a small loader
that never changes and the runtime itself. The editor verifies both. The
board restarts.

The runtime goes on once, and again only when the editor brings a new
line (a version ending in `.000`).

---

## 5. Download the program

Press :ti-download: in the toolbar, or `F5`. The program travels over the
ST-LINK's virtual COM port - the same cable.

![The toolbar: the port picker and the download button](img/deploy-toolbar.webp){: .sb-center}

The board keeps two program slots: the new program is written into the
inactive one, verified, and only then made active. A failed download
leaves the running program untouched.

---

## 6. Watch it run

Press **ONLINE** (the plug icon beside the port picker). Rungs, block
pins, variables and the screen preview show the live values of the board.

![Rungs with the board running: green is power flowing, every pin carries its live value](img/editor-online.png){: .sb-center}

---

## 7. Over the network

With the board on Ethernet, type its IP address into the port picker:

- **the program**: :ti-download: as before;
- **the runtime**: *Flash runtime* with the address. The board keeps the
  running runtime aside, writes and verifies the new one, and puts the old
  one back by itself if the new one does not come up. The board page counts
  the runtime generations (`g1`, `g2`, ...).

The program and the retentive values stay where they are through a
runtime update.

---

## What the STM32 runtime does not carry

Recipes are not on the STM32 runtime; the editor refuses a project that
uses them for this board. The STM32 runtime drives no axes, so a motion
block there answers ErrorID 1. The other limits are on
[Performance and limits](/docs/operation/limits/).

---

## When something does not work

| What you see | What to do |
|:---|:---|
| no COM port | install the ST-LINK driver; use the ST-LINK connector, not the board's other USB port |
| the board refuses the program, naming two versions | flash the runtime (step 4) |
| invalid target | the project is for another board |
| the board does not appear on the network | see [Finding your boards](/docs/deployment/find-devices/) |

---

## Next

- [Editor](/docs/editor-overview/editor/) - the layout and what is where
- [Variables](/docs/editor-overview/variables/)
- [Ladder](/docs/programming/ladder/), [FBD](/docs/programming/fbd-composites/), [Structured Text](/docs/programming/st-language/)
- [Download to the board](/docs/deployment/deploy/)
