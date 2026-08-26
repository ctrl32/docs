# Linux boxes

Some jobs outgrow a microcontroller: hundreds of variables, dozens of
screens, a site that wants OPC UA. For those, the ctrl32 runtime also
runs as a **Linux program** — same project file, same editor, same
logic engines, on a box with gigabytes instead of kilobytes.

Two boxes are in the catalogue today:

| Box | Glass | Runs on |
|:---|:---|:---|
| Seeed reTerminal | 5" 1280 × 720 touch | Raspberry Pi CM4 |
| ST STM32MP157C-DK2 | 4" 480 × 800 touch | STM32MP1 (dual Cortex-A7) |

The runtime draws straight onto the glass — no desktop, no browser in
between. The box boots into your visualisation.

---

## The same project, bigger numbers

A Linux target is picked like any board. What changes is the budget —
the third column of the [limits table](limits.md):

| | ESP32 / STM32 | Linux |
|:---|:---:|:---:|
| Variables | 512 | **5 120** |
| Screens | 32 | **320** |
| Widgets per screen | 64 | **256** |
| Compiled program | 32–64 kB | **320 kB** |
| Instance data | 8–24 kB | **240 kB** |
| LD/FBD blocks | 512–1024 | **5 120** |

And the glass is flexible: a Linux box **scales any authored
resolution** onto its screen, rotation and aspect kept. The same
project can run on the reTerminal's 1280 × 720 and the DK2's 4" glass
without redrawing a single screen.

A **USB mouse** needs no configuration either: plug one in — even
into a running box — and a cursor appears; a click presses exactly
like a finger. Unplug it and the cursor is gone. Touch and mouse
work side by side.

---

## The box's network, from the editor

On the board page, a Linux target's **Box network** section talks to
the *running* box: join a WiFi network, switch the ethernet between
DHCP and a static address. The box applies it through its own
network manager and its answer shows right there — including a
refusal, when the box has no manager to apply with.

---

## Getting a program onto the box

The runtime is installed on the box **once**; after that everything
travels over the network:

1. Open the scanner (:ti-eyeglass:) — the box appears with its name,
   address and the program it runs, like [any other board](find-devices.md).
2. **Use** the row, then download (F5) as usual. The box validates the
   file, swaps it in atomically and restarts into the new
   visualisation — a refused file leaves the old one running, so an
   upload cannot leave the box dark.
3. Go **online** the same way as over a COM port: live values on the
   canvas, the variable table, the [scope](scope.md),
   [forcing](force.md) — the wire is TCP instead of a cable, the
   experience is the same.

---

## OPC UA — every variable, served

A Linux box is also an **OPC UA server**. Every variable of the
running project is a node under `Objects/ctrl32`
(`ns=1;s=<variable name>`), readable by any OPC UA client — SCADA,
historians, test tools.

Writing follows the same rule as everywhere else in ctrl32: a write
from outside is a **command**, and only variables marked `rw` accept
one. Everything else answers "not writable" — the logic owns its
outputs.

## …and read from another server

The box can also be the client. On the **OPC UA page** (in the
device tree under Ethernet) the editor browses any OPC UA server —
another ctrl32 box, a PLC, a SCADA — and imports the picked
variables into VAR. Each one carries its node, and at runtime the
box polls the server into them; the editor never speaks OPC once
the design leaves the desk.

![The OPC UA page: the box's server on top, browse-and-import below](img/opcua-page.webp){: .sb-center}

One server per project, named once. A box that loses the server
keeps running on the last values — logic first, network second.

---

## What a Linux box does not do (yet)

The box speaks over **ethernet**: Modbus TCP (master and slave-side
polling), WEBview, OPC UA, the editor's online wire. CAN, RS485 and
the local buses are not offered on a Linux target — the editor hides
them and the build refuses them, so a project cannot carry
configuration the box would silently ignore. They will arrive with
their drivers.

And the standing rule of the whole product applies unchanged: a
ctrl32 box is [not a safety device](intended-use.md). Emergency
stops stay hard-wired.
