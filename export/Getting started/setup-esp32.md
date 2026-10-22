---
title: "ESP32"
slug: setup-esp32
section: "Getting started"
order: 4
sidebar_position: 4
generator: tools/docs_export.py
---

# ESP32: from the box to a running program

This page takes an ESP32 board from the box to a program running on it
and watched live from the editor. The same steps hold for every ESP32
family in the [hardware catalog](/docs/hardware/modules/): ESP32, ESP32-S3, ESP32-P4
and the C3 / C6 nodes.

**You need**

- a Windows PC with the ctrl32 editor installed,
- the board and a **USB data cable** (a charging-only cable powers the
  board and carries no data),
- the driver of the board's USB bridge chip - see step 2.

---

## 1. Install the editor

Run `ctrl32-setup-<version>.exe`. It installs the editor, the board
catalog, the runtime for every supported board and the sample projects.
There is nothing else to install - no toolchain, no Python, no flasher.

---

## 2. Install the USB driver

The board talks to the PC through a USB-serial bridge chip, and Windows
needs that chip's driver before a COM port appears. The board's card in
the editor names the chip:

| Bridge chip | Shows in Device Manager as | Driver |
|:---|:---|:---|
| CP210x | Silicon Labs CP210x | Silicon Labs "CP210x VCP" |
| CH340 | USB-SERIAL CH340 | WCH "CH341SER" |
| CH9102 | USB-Enhanced-SERIAL CH9102 | WCH "CH343SER" |

A board whose USB goes straight into the chip (the native USB of an
ESP32-S3, C3, C6 or P4) appears as a USB serial device without a driver.
The board's card says which of the two a board has.

A PC on the internet usually fetches the driver by itself the first time
the board is plugged in. A notebook without internet needs it downloaded
beforehand.

**No COM port after plugging in** means one of two things: the driver is
missing (Device Manager shows an unknown device), or the cable carries no
data. Swap the cable before you doubt the board.

---

## 3. Make the project

*New project* (Ctrl+N) opens the wizard.

![The New project wizard with a board picked](img/newproj-board.webp){: .sb-center}

1. **Name** - becomes the folder and the file name.
2. **Location** - `Documents\ctrl32\projects` unless you pick another.
3. **Hardware** - the board from the catalog, or the module your own
   hardware carries.
4. **What the project does** - screens on the display, WEBview, the first
   program in ladder or ST, CAN, Modbus, MQTT, net32. Every part can be
   added or removed later from the project tree.

*Create project* writes `<location>\<name>\<name>.prj32` and opens it.

---

## 4. Flash the runtime

The runtime is the board's firmware. It goes on **once**, before the
first program, and again only when the editor brings a new line (a
version ending in `.000`).

1. Connect the board and pick its COM port in the toolbar's **port
   picker**. The picker starts empty on purpose.
2. Click the board in the project tree and press **Flash runtime**.

![The Flash runtime dialog](img/deploy-runtime.webp){: .sb-center}

The editor writes the runtime, reads it back and verifies it. A port
where a different chip answers is refused, not written. It takes about a
minute; the board restarts.

---

## 5. Download the program

Press :ti-download: in the toolbar, or `F5`.

![The toolbar: the port picker and the download button](img/deploy-toolbar.webp){: .sb-center}

The project is built, written into the board's inactive program slot,
verified, and only then made active. A failed download leaves the running
program untouched. A build error stops everything before a byte is sent
and opens the output.

Every later change is this step alone.

---

## 6. Watch it run

Press **ONLINE** (the plug icon beside the port picker). Rungs, block
pins, variables and the screen preview show the live values of the board.

![Rungs with the board running: green is power flowing, every pin carries its live value](img/editor-online.png){: .sb-center}

ONLINE needs the editor and the board to run the same program; if they do
not, the editor offers to download it.

---

## 7. Over the network

A board on Ethernet or WiFi takes every later program over the network:

1. Type the board's IP address, or the `name.local` of the project, into
   the port picker. The [scanner](/docs/deployment/find-devices/) lists what answers.
2. :ti-download: as before.

A board with **8 or 16 MB of flash** takes a new runtime the same way:
*Flash runtime* with the address in the port picker. The board writes it
into its second application slot, restarts into it and returns to the
old runtime by itself if the new one does not come up. Boards with
**4 MB of flash** take the runtime over USB only.

The first runtime update onto a board flashed before network updates
existed goes over USB once.

---

## When something does not work

| What you see | What to do |
|:---|:---|
| no COM port | install the bridge driver; swap the cable for a data cable |
| the board refuses the program, naming two versions | flash the runtime (step 4) |
| invalid target | the project is for another board - pick the right board in the project |
| `ERR: crc` | the transfer was corrupted - check the cable, try again |
| the board does not appear on the network | see [Finding your boards](/docs/deployment/find-devices/) |

---

## Next

- [Editor](/docs/editor-overview/editor/) - the layout and what is where
- [Variables](/docs/editor-overview/variables/)
- [Ladder](/docs/programming/ladder/), [FBD](/docs/programming/fbd-composites/), [Structured Text](/docs/programming/st-language/)
- [Download to the board](/docs/deployment/deploy/) - the slots, the runtime, the messages
- [Performance and limits](/docs/operation/limits/)
