# A board from zero

The gap between "the board arrived" and "my first screen is on it"
is three steps — put the runtime on it once, download the program,
done — but the first of them meets drivers, cables and one strict
rule. This page walks each board family through it. Nothing here is
repeated in daily work: a board set up once takes every later
program [over the network or the cable](deploy.md) without ceremony.

**The one strict rule first**: the runtime goes on **before** the
program, and both come from the same editor install —
[one version for everything](deploy.md). A board with an older
runtime refuses a newer program *by design*, and the message names
both versions. When anything refuses anything, flash the runtime
first and try again.

---

## ESP32 boards

What you need: the board, a **USB data cable** and the right bridge
driver. That last one is the classic field trap, so it goes first.

### The USB bridge driver

The board talks to the PC through a USB-serial bridge chip, and
Windows needs that chip's driver before any COM port appears. The
board's card in the editor (*Supported hardware*) names the chip;
the three common ones:

| Bridge chip | Shows in Device Manager as | Driver |
|:---|:---|:---|
| CP210x | Silicon Labs CP210x | Silicon Labs "CP210x VCP" |
| CH340 | USB-SERIAL CH340 | WCH "CH341SER" |
| CH9102 | USB-Enhanced-SERIAL CH9102 | WCH "CH343SER" |

A PC with internet usually fetches the driver itself the first time
the board is plugged in. A notebook in a production hall usually
**has no internet** — download the driver at the desk and carry it.
No COM port after plugging in means one of exactly two things: the
driver is missing (Device Manager shows an unknown device), or the
cable is a charging cable — power flows, data does not. Swap the
cable before doubting the board.

### Runtime, then program

1. Connect the board, **Select COM** in the toolbar — the fresh COM
   port is in the list.
2. Open the board's card and press **Flash runtime** — the dialog
   shows the runtime's build and the chip it expects, and refuses a
   port where a different chip answers. About a minute; the board
   restarts.
3. Download the program (:ti-download: / `F5`) over the same port.

From then on the board is a citizen: the [scanner](find-devices.md)
finds it, the WEBview serves, [online](online.md) works.

---

## STM32 boards (F746-DISCO class)

Simpler than the ESP32, because the programmer is **on the board**:
the DISCO's ST-LINK connector is power, programmer and serial
console in one USB cable.

- **Driver**: Windows Update installs the ST-LINK driver on first
  contact. Offline, install ST's *ST-LINK USB driver* package
  (a free download from st.com) beforehand.
- **Flash runtime** writes the firmware through the ST-LINK — no
  boot buttons, no jumpers.
- **The program** travels over the ST-LINK's virtual COM port — the
  same cable, picked with Select COM like any serial board.

The F7 keeps two program slots and validates before switching, the
same as every other board: a failed download leaves the running
program untouched.

---

## The Linux runtime

A Linux device is an operating-system install, not a firmware flash,
so it has [its own page](linux-setup.md): the card image, the display
driver, the service, the settings file — from blank card to the
scanner finding the device. What the runtime then does — screens,
OPC UA, going online — is on [The Linux runtime](linux-runtime.md).

---

## When the board does not appear

The checklist lives in
[Finding your boards](find-devices.md) — the short version:
wrong subnet, a runtime old enough to predate the scanner, a missing
USB driver, or a charging-only cable.
