# Supported hardware

The catalogue in the editor holds **95 entries**. You never have to know
that number: you pick your board from a list, and everything that follows
— pin assignments, which buses exist, how much memory there is, what the
runtime is flashed with — comes from that choice.

---

## The three kinds of entry

| Kind | How many | What it is |
|---|---|---|
| **Modules** | 66 | a bare ESP32 module: you design the board around it |
| **Development boards** | 13 | a ready board with connectors, for prototyping and small installations |
| **Panels** | 11 | a finished device with a display, ready to mount in a door |
| **Presets** | 5 | a development board plus a known-good configuration, to start from |

A **preset** is worth explaining: it is not different hardware, it is the
same board with the peripherals already filled in. `S3 SSD1963 setup` is
an S3 DevKit with the display wired the way the driver expects. Start
from one when you are learning, then change what you need.

---

## Which processor

| Processor | Entries | Where it fits |
|---|---|---|
| **ESP32** | 45 | the workhorse: two cores, ethernet MAC, CAN, plenty of I/O |
| **ESP32-S3** | 33 | more RAM and a faster bus — the reference platform for panels with a display |
| **ESP32-PICO-V3** | 8 | the same ESP32 in a much smaller package |
| **ESP32-P4** | 1 | the fastest, with a native display interface (MIPI DSI) |
| **STM32F7** | 1 | the first of the STM32 family — see below |

**The ESP32-S3 is the reference platform.** Everything ctrl32 does must
work on it; when something does not fit, the design changes rather than
the platform. If you are choosing and have no other constraint, choose an
S3.

The **classic ESP32** has one thing the S3 does not: an **ethernet MAC**.
For a panel that must sit on a wired network without an extra chip, this
is the reason to pick it.

!!! tip "Memory suffixes are worth reading"
    `N16R8` means 16 MB flash and 8 MB PSRAM; `N4` means 4 MB flash and
    no PSRAM. More flash means room for screens and fonts; PSRAM means
    room for trends, alarm history and images. The editor tells you when
    a project outgrows the board you picked — at your desk, not on the
    machine.

---

## STM32 is coming, F7 first

The runtime is not tied to Espressif. The first STM32 target — the
**STM32F746 Discovery** — runs the same VM, the same tags, the same
Modbus and CANopen, the same rasteriser and the same pack format.

What that means for you: a project is not locked to a chip family. The
screens, the logic and the tags are data, and the same data runs on the
silicon that suits the installation.

More of the family follows. Nothing below 64 kB of RAM will be
supported — under that, the runtime has nowhere to live.

---

## Boards with a display

**29 of the entries have a screen.** The rest are headless: they run
logic, talk to fieldbuses and serve the WEBview to a phone or a laptop,
without a display of their own.

Headless is a perfectly good way to build a machine. A panel in the door
costs money and a hole in the enclosure; a WEBview on the operator's
phone costs neither. Many installations want both, and the same project
serves both without being written twice.

---

## The finished panels

These are complete devices — enclosure, display, touch, terminals:

| Family | Sizes |
|---|---|
| **inoCORE32** | compact controllers, with and without a display |
| **inoHMI32 / 43 / 53** | panels around 3.2", 4.3" and 5" |
| **stepHMI32** | panels in several sizes, 480×272 class |
| **Waveshare P4-NANO** | 10.1" on the ESP32-P4 |

---

## Every board has an identity

The practical consequence: a pack built for one board is **refused** by
another. Upload the wrong file to the wrong panel and it tells you so
instead of running something that was never meant for it.

---

## Choosing, briefly

| You need | Look at |
|---|---|
| a display in the door | a **panel** — the size decides the rest |
| wired ethernet, no display | a classic **ESP32** development board with a LAN port |
| your own board around a module | a **module** — the pinout is yours to design |
| to try ctrl32 out this afternoon | a **preset** — DevKit plus a working configuration |
| the most headroom | **ESP32-S3** with 16 MB flash and PSRAM |

Then check [Performance and limits](limits.md) for what fits, and
[Peripherals and services](peripherals-and-services.md) for what you can
attach.
