# ctrl32

**HMI and PLC for small machines on a single ESP32 panel.** You draw the
screens, define the tags, write the logic in ladder, in a function block
diagram or in ST — and download it to the panel. The same visualization also
runs in a browser.

A complete engineering tool with a live browser visualization, on
hardware that costs an order of magnitude less than the established
PLC systems.

## What it is made of

| Part | What it does |
|---|---|
| **Panel (firmware)** | runs on the ESP32, draws the visualization on a touch display, reads Modbus, executes the logic |
| **ctrl32 Editor** | an installed desktop application — you draw screens, define tags, write the program and download it to the panel |
| **WEBview** | the same visualization in a browser, served straight from the panel |

## The core principle: the visualization is DATA, not code

Screens are **not compiled into the firmware**. The editor packs them into a
binary pack and the panel reads it directly from flash. Changing a screen
therefore means uploading a file, **not reflashing the panel** — and when
something goes wrong, the old pack stays in the other slot and the panel
keeps running.

## What the panel really handles

The numbers are measured on the slowest board we ship (a classic ESP32 at
240 MHz), with Ethernet and the CAN bus running alongside:

| | |
|---|---|
| 400 ladder blocks | **0.52 ms** out of a 10 ms cycle (5 %) |
| a whole machine program (190 ST lines, 215 tags) | **0.30 ms** (3 %) |
| 10 000 ST instructions | 1.42 ms (14 %) |

And 400 blocks still leave the cycle 95 % idle. Details and method in
[Performance and limits](limits.md).

## What it is NOT

!!! danger "Safety is not handled through the panel"
    The device is **not intended for safety functions**. Emergency stop,
    doors and light curtains must be **hard-wired** — never routed through
    the panel's logic. Stopping a drive over CANopen is not a safety
    function; that is what the drive's STO terminals are for.

Nor is it a real-time system. It holds a 10–20 ms cycle reliably, but jitter
from the network stack exists and we never promise it away.

## Where to start

<div class="grid cards" markdown>

-   **First time in your hands**

    ---

    From installation to your first program in the panel, in minutes.

    [Quick start](quickstart.md)

-   **How you work in it**

    ---

    Editor layout, project tree, screens, tags, POUs.

    [Editor](editor.md)

-   **When the machine behaves differently than you expect**

    ---

    Live values right in the ladder rungs, straight from the running machine.

    [Online monitoring](online.md)

-   **When something does not work**

    ---

    The actual messages the system prints, and what is behind them.

    [Troubleshooting](troubleshooting.md)

</div>
