# Quick start

The goal of this chapter: **from an installed editor to a program running in
the panel.** It takes a few minutes and needs nothing but the panel, a USB
cable and a PC.

## 1. Installation

Run the installer `ctrl32-setup-<version>.exe`. It installs:

| File | What it is for |
|---|---|
| `visu_editor.exe` | the editor itself |
| `visu_stc.exe` | the ST compiler — the editor calls it on every build |
| `packbuild\` | the pack builder (it carries the schema and the board catalog) |
| `ctrl32.dat` | the catalog of boards and chips |
| `examples\` | sample projects to open |

!!! note "Why three programs and not one"
    The compiler and the pack builder are the same tools we use in
    development — so the pack the editor builds for you is **byte for byte**
    the one the command line builds. The format has a single author and no
    way to drift.

    The three belong together: each carries the schema version it was built
    for, and the editor refuses a pack builder that does not match rather
    than quietly building the wrong thing.

## 2. Open a sample project

*File → Open* and pick something from `examples\`. Good places to start:

- `ladder_sealin.yaml` — the classic seal-in circuit with a TON, a counter
  and a latch; the rungs come with the comments under the variables,
- `tubex_panel.yaml` — a real panel with Ethernet, a Modbus slave and
  NeoPixel LEDs,
- `machine_blocks.yaml` — motors, valves, PID and hysteresis,
- `time_setpoint.yaml` — a TIME setpoint the operator types on the screen,
  driving a timer's PT.

## 3. Pick the board

Click the board node in the project tree. The board decides the pins, the
memory and which runtime is flashed into it — a project cannot be deployed
without one.

## 4. Flash the runtime (the first time)

If the panel is new or carries old firmware, the board page has *Flash
runtime*. It is written over USB (esptool) and takes tens of seconds.

!!! warning "An old runtime means the program will not load"
    The pack format evolves. If the runtime is older than the pack, the panel
    refuses it and the editor shows an error. The fix is always the same:
    **flash the runtime**.

## 5. Download the program

Pick the COM port in the toolbar and click the blue ⭳ icon (*Download to
panel*). The editor builds the project and uploads it. What happens
underneath:

1. the project is built into a binary pack,
2. the pack goes into the **inactive slot** in the panel,
3. the panel verifies the CRC, the format and the target board,
4. **only then** does it switch the active slot and restart.

That is why downloading cannot brick the panel: when anything is wrong, the
old pack stays and keeps running.

!!! note "No port is preselected"
    The port selector starts empty, and both transfer dialogs ask for it at
    the moment bytes are about to move. A port nobody chose reads as
    "configured", and the first sign that it was not would be a download
    going nowhere.

## 6. Watch what the machine is doing

Next to the port there is a plug icon — *ONLINE*. Switched on, the editor
shows **live values straight from the panel**: in the ladder rungs, on block
pins, in the tag list and in the screen preview.

There is one condition: **the editor and the panel must run the same
program**. If they do not, the editor says so and offers to download it —
more in [Online monitoring](online.md).

## What next

- [Editor](editor.md) — how it is laid out and what is where
- [Tags](tags.md) — variables, types, deadband and where values come from
- [Ladder](ladder.md) — drawing rungs
- [Download to the panel](deploy.md) — dual slot, runtime, what is verified when
