# Editor

ctrl32 Editor is an **installed application**, not a web page. The reason is
simple: it draws exactly the pixels you will see on the board — the same
renderer as in the firmware is built into it, fonts, roundings and colours
included. What you see is what gets downloaded.

![A thermostat screen on the canvas, the widget toolbox on the right](img/editor-canvas.webp){: .sb-center}

## Layout

| Part | Where | What is in it |
|:---|:---:|:---|
| **Menu** | top | File, Edit, View, Project, Build, Online, Debug, Tools, Window, Help |
| **Toolbar** | under the menu | new, save, undo/redo, TEST, ONLINE, download |
| **Project tree** | left | the board and everything running on it |
| **Documents** | centre | every tree node has a **page**, opened as a tab |
| **Toolbox** | right | what the visible editor takes: widgets for a screen, blocks for LD/FBD — grouped as Boolean, Math, Timers, Counters, General, Motion, CAN and GSM/GPS (groups start collapsed) |
| **Status bar** | bottom | the result of the last build, the connection state |

The **bug icon at the top right** opens mail to `bugs@ctrl32.com` —
reporting a fault should be one click from wherever you hit it.

![The screen above, its ladder below — one project, two views of the same variables](img/editor-layout.webp){: .sb-center}

## The tree follows the hardware, not the protocols

```
project
  board
    Application          programs, variables, visualizations, axes
    CAN                  the bus itself: bitrate, termination
      Raw CAN            frame-to-variable mapping
      CANopen master     + devices
    RS485                the line: baud, parity, stop bits
      Modbus RTU master  + devices
      Modbus RTU slave   the board as a slave
    Ethernet             DHCP/static IP, mDNS
      Modbus TCP         master and slave
      MQTT               telemetry / Home Assistant
    I2C, SPI             local buses and chips
    Settings
```

One wire can carry several protocols, and the same protocol can run on two
wires (Modbus on RS485 **and** on Ethernet). Sorting by protocol could not
express that; this way matches the hardware.

In a **net32 system project** one more level sits above the board: the
system, with one row per device. A click switches the whole editor to
that device; clicking the system name opens the net32 canvas where the
devices' shared variables are wired together. See
[the system project](net32.md#the-system-project).

!!! note "Settings live on pages, not in the right-click menu"
    A context menu holds **actions** — add, delete, rename. Never settings.
    The bus speed is on the bus page, where a person looks for it. A popup
    is only for **picking from a catalog** (boards, devices, dictionary
    objects).

Nodes for features that are not finished yet are in the tree as well — their
page says so. A customer has to see what the board can have, not guess it.

## Tasks — which programs run

Under *Application* the tree has a *Tasks* node. Each task is a cycle
with its period and priority — *FAST (10 ms, priority 1)* is the main
one and every new project starts with its first program in it. Under a
task you see the programs it calls, in the order they run.

A project holds up to four tasks. The priority follows the period: the
task with the shortest period is priority 1 and runs first when several
are due — the same rule the device schedules them by. *FAST* owns the
inputs and outputs; the other tasks run logic only, each at its own
period.

A program runs only when a task calls it or another program calls it.
A program that nothing calls stays in the project, is drawn grey in the
tree and does not run; hover it and the tree says so. Right-click a task
to change its period, rename it, add a program to it or remove it;
right-click a program under a task to move it up or down in the run
order or to take it out. The program's own menu offers the same choice
under *Task*, including *(none)*.

**Calling a program from a program.** Write its name as a statement in
ST — `STATS();` — or drop the program from the insert menu as a box in
FBD. The called program runs at that point of the caller's cycle, on its
own variables, and what it wrote the caller reads right after the call.
A called program needs no task; the tree shows it in normal colour and
says it is called. A program cannot be called and run by a task at the
same time (it would run twice), calls never form a loop, and they nest
at most eight deep — the build says so.

A project saved before this version keeps working exactly as it did:
every program that had no task written in the file belongs to *FAST*,
and the programs keep the order they ran in.

## Toolbar

| Icon | What it does |
|:---|:---|
| :ti-file-plus: | new project — the wizard: name, folder, board or module, what the project does (the editor starts empty until one is created or opened) |
| :ti-folder-open: | open project |
| :ti-device-floppy: | save project |
| :ti-arrow-back-up: :ti-arrow-forward-up: | undo / redo (both unlimited; the count is in the Edit menu) |
| :ti-terminal-2: | the board's serial terminal |
| :ti-wave-square: | the scope (trace) |
| :ti-eyeglass: | [find devices](find-devices.md) |
| *port picker* | which COM port or address the editor talks to |
| :ti-plug: | **ONLINE** — connect to a real board (:ti-plug-connected: while connected) |
| :ti-download: | **download to the board** (F5) — the only coloured icon in the bar |

While a simulation runs (*Online → Simulation*), a transport joins
the bar: :ti-player-stop: stop, :ti-player-pause: pause,
:ti-player-track-next: one PLC cycle. The complete reference of
menus, keys and mouse gestures is
[Controls and shortcuts](editor-controls.md).

There is deliberately only one blue icon. Downloading into a setup is an
action that must not be confused with any other; everything else is a flat
icon like in any ordinary application.

## TEST — simulation without a board

*Online → Simulation* switches the editor into running: the PLC cycle runs on the PC,
screens react, blocks compute, variables change. It can be paused and stepped
cycle by cycle (*Debug → Step*).

What runs is **the same compiled program and the same block library** as in the
board — the VM is compiled for the PC as well. So logic can be debugged at
your desk and reach the equipment finished.

The difference from [online monitoring](online.md): TEST computes the
values, ONLINE **reads them from the equipment**.

## Build (F7) and download (F5)

**F7** only builds the project and reports the result. **F5** builds and
downloads it.

When a build fails, a window opens with the **whole** output — the text can
be selected and copied with a button, and the same text is in
`build\last_build_error.txt`. A truncated line in the status bar was never
enough for anyone to help you with.

## Language

*View → Language*. The editor speaks English, Slovak, Spanish and
Turkish; more languages are being translated. The first start picks the
language your Windows runs in, when the editor has it, and the choice is
remembered between runs. The documentation is English.

The translations were made by the authors with machine help and
checked where a native speaker was at hand — a wrong word in your
language is worth a message, it gets fixed in the next release.

## AI assistant connection (MCP server)

An AI assistant on your computer — any client that speaks MCP, the
Model Context Protocol — can join your **running editor session**: it sees the
project you have open, runs the build, reads the connected board, and
can make edits that appear live in the editor, each one undoable with
Ctrl+Z. It starts from *Tools → MCP server*, it is off by default,
and it never leaves this computer.

## Licence

- **Linux-only projects are free outright** — saving, download and
  online included,
- what is paid is **ESP32 and STM32** work leaving the editor: saving
  such a project, and talking to such a board — download and online
  alike.

## Updates

*Help -> Check for updates* reads a small signed notice from our web and
tells you whether a newer version exists; with *Check on start* ticked
the editor does this quietly every time it starts. Without internet
nothing happens and nothing is shown.

When a newer version exists, *Help -> New version* opens the update
dialog:

![The update dialog](img/editor-update.webp)

- **Download and verify** fetches the installer into your temporary
  folder and judges it twice before anything else happens: its
  fingerprint must equal the one in the signed notice, and the file
  must carry our publisher signature. A file that fails either test is
  deleted and the dialog says so.
- **Install** starts the verified installer and closes the editor; the
  installer then replaces the program the usual way. The button stays
  off while the open project has unsaved changes - save first, nothing
  is closed under you.
- **Open the download page** takes you to the web instead, the manual
  road.

The editor never updates itself on its own: every step above is your
click. And because a device carries the same version number as the
editor that programmed it, update the runtime of your devices after the
editor (*Upload runtime*) - the editor refuses to work with a runtime of
a different number.
