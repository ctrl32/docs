# ctrl32

ctrl32 is an editor and a family of runtimes for automation on ESP32 and
STM32 boards and on Linux devices. In the editor you draw the screens,
define the variables, write the logic in [ladder](ladder.md),
[FBD](fbd-composites.md) or [Structured Text](st-language.md), and
download the project to the device. The same screens also run in a
browser.

!!! warning "Read before you plan anything with it"
    ctrl32 carries **no certification of any kind** - no CE marking for a
    finished product, no functional-safety rating, no type approval. It
    does not belong in an installation where people's safety, other
    people's property or an insurer's opinion depends on it. See
    [Intended use](intended-use.md).

!!! danger "Never route safety through the device"
    Emergency stop, guards, light curtains and limit switches are
    **hard-wired**, always. Stopping a drive over CANopen or EtherCAT is
    not a safety function - that is what a drive's STO terminals are for.
    ctrl32 is not a real-time system: it holds a 10-20 ms cycle
    dependably, with jitter from the network stack.

![The editor: the canvas draws exactly what the device shows](img/editor-canvas.webp){: .sb-center}

## Start

<div class="grid cards" markdown>

-   **Raspberry Pi**

    ---

    From a blank card to the runtime running your project.

    [Raspberry Pi](setup-raspberry-pi.md)

-   **ESP32**

    ---

    From the box to a running program, over USB and over the network.

    [ESP32](setup-esp32.md)

-   **STM32**

    ---

    The STM32F746G-DISCO through its ST-LINK cable.

    [STM32](setup-stm32.md)

-   **When something does not work**

    ---

    The messages the system prints, and what is behind them.

    [Troubleshooting](troubleshooting.md)

</div>

## What it is made of

| Part | What it does |
|:---|:---|
| **Editor** | the installed desktop application - screens, variables, programs, download, online monitoring |
| **Runtime** | the firmware of an ESP32 or STM32 board: draws [HMIview](hmiview.md) on the display, runs the program, talks Modbus, CAN and the other buses |
| **Linux runtime** | the same engines on a Raspberry Pi or another Linux device, with larger limits and OPC UA - [The Linux runtime](linux-runtime.md) |
| **WEBview** | the same screens in a browser, served by the device - [WEBview](webview.md) |
| **net32** | several ctrl32 devices sharing variables as one system - [net32](net32.md) |

## The screens are data, not code

The editor builds the project into a pack - screens, variables, programs
- and the device reads it straight from flash. Changing a screen is a
download, not a reflash of the device. The device keeps two program slots:
a new pack is verified before it becomes active, and a failed download
leaves the old one running. See [Download to the board](deploy.md).

The editor draws with the same code as the device, so the canvas shows
exactly what the device will show.

## Where things are

| You want to | Go to |
|:---|:---|
| know the editor's windows, menus and keys | [Editor](editor-overview.md) |
| declare variables | [Variables](variables.md) |
| draw screens | [Visualisation](visualisation.md) |
| write the program | [Programming](programming.md) |
| look up a block | [Function blocks](blocks.md) |
| connect a bus or a protocol | [Protocols](buses.md) |
| wire a chip | [Chips and services](peripherals-and-services.md) |
| put it on a device | [Deployment](deployment.md) |
| watch, force, trace it running | [Operation](operation.md) |
| know the limits | [Performance and limits](limits.md) |
