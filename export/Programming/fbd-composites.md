---
title: "Function block diagram (FBD)"
slug: fbd-composites
section: "Programming"
order: 79
sidebar_position: 79
generator: tools/docs_export.py
---

# FBD: composite blocks, axes and drive control

Equipment control in ctrl32 is assembled from blocks in an FBD diagram —
the logic is **data in the pack**, not code in the firmware. Besides the
fixed block library (TON, PID, … — see `widgets.md`) there are:

![An i550 drive in FBD: the DRIVE_i550 block and its ramps, bound to axis 1](img/fbd-i550.webp){: .sb-center}

## Networks — the rungs of FBD

An FBD program is a stack of **networks**, numbered from the top, exactly
as a ladder program is a stack of rungs. A network is a strip: its number
and a comment lane at the top, its blocks inside, its height whatever its
blocks need. There is no free canvas — every block belongs to a network,
and the strips pack top-down with nothing between them.

- **+ Network** in the rung toolbar adds an empty network at the end and
  selects it; a click on a strip's empty space selects it (grey, like a
  selected rung). New blocks — from the Toolbox or *+ block* — land in
  the **selected** network.
- Drag a block into another strip and it belongs there; the strips
  repack on the drop.
- Right-click the number lane: *Insert network above / below*, *Move
  network up / down* (the execution order follows the picture), *Delete
  network* — with its blocks. `Delete` on a selected empty strip does the
  same.
- Click the comment lane and write; the comment sits on a grey plate in
  black, like a rung comment.
- A wire never crosses a strip; across networks the variable's **name**
  carries the signal, drawn at both ends.

![Two networks: the tank logic in the first, the pump interlock in the second](img/fbd-networks.webp){: .sb-center}

## The canvas

The FBD page and the [Vision](/docs/vision/) page draw on the same canvas
and answer the same gestures.

| Gesture | What it does |
|:---|:---|
| click a block | selects it; `Ctrl` + click adds it to the selection or takes it out |
| drag on the empty canvas | a selection rectangle: every block it touches is selected (`Ctrl` keeps the ones selected before) |
| `Ctrl+A` / `Esc` | every block of the program / none |
| drag a selected block | moves the whole selection; the drop keeps every block clear of the others |
| drag from an output to an input | draws a wire |
| click a wire | selects it; `Delete` or its right-click menu **Remove connection** removes it, and the input goes back to `...` |
| drag a wire off its input | picks the wire up: drop it on another input to move it, let it go anywhere and it is gone |
| click an input or an output | its binding: a variable, a constant, one bit of an integer |
| `Delete` | the selected wire, else the selected blocks, else the selected empty network |
| `Ctrl+C` / `Ctrl+X` / `Ctrl+V` | copy, cut and paste the selection - the wires between the copied blocks are drawn again between the copies, a wire from outside stays a binding of the same variable, the copies land beside the originals and are selected |
| mouse wheel | scrolls; `Shift` + wheel scrolls sideways |
| `Ctrl` + wheel | zooms around the mouse, from 40 % to 250 % |
| middle button drag, or `Space` + drag | moves the view |
| `Home` | zoom 100 %, the top left corner |
| `F1` | the page of the selected block |

## Composite block (an FB built from blocks)

A composite is a POU with an **interface** (input/output ports) and its
own internal network — drawn in FBD **or in ladder**, whichever reads
better. In a diagram it is used like an ordinary block; **a
double-click opens it** and shows how it is put together. At compile
time it is flattened into primitives — the board executes a flat list,
with no recursion and no extra interpreter.

- Creating one: right-click on *Application* → **Add POU…**, type **FB**,
  language LD, FBD or ST — the whole procedure, with pictures, is
  [Your own function block](/docs/programming/own-block/).
  Above the canvas sits the **variables pane** in the PLCopen shape:
  `VAR_INPUT` and `VAR_OUTPUT` rows are the block's ports (name and
  BOOL/REAL type edited right in the table, ports added with one
  button; max 4 inputs, 2 outputs), and the `VAR` section lists the
  local connection variables the diagram creates. Changing the
  interface bumps the block version, so existing instances migrate
  cleanly.
- In the ladder view the ports behave as ordinary variables — a
  contact on an input port, the coil on an output port.
- Supplied blocks (for example `DRIVE_i550` from `libraries/`) are
  **read-only** — you can look inside, but not change it. **Save as
  own** creates an editable copy in the project.
- In YAML: the `composites:` section; inside the body `$PORT` marks an
  interface port and `~wire` an internal wire (every use of a composite
  gets its own wires — instances do not share state).
- Limits: nesting depth 8, recursion forbidden, at most 64 blocks AFTER
  flattening — all of it enforced by the compiler, not the board.

## Axis (AXIS) and drives

An **axis** is a drive controlled by motion blocks. It is added by
right-clicking its bus node in the device tree (CANopen master →
CiA402, SPI → POWERSTEP01 or TMC5160 — the node decides the backend)
and carries the backend and its parameters:

| Backend | Bus | Status |
|:---|:---:|:---|
| CiA402 (Lenze i550) | CANopen | tested on the bench |
| POWERSTEP01 | SPI | interface ready, driver ships with the hardware |
| TMC5160 / TMC5130 | SPI | driver written from the datasheet, mock-tested — verify on the bench |

Blocks bound to an axis (they have an axis selector in the top bar of
the diagram):

- `MC_Power` — switch the axis on (Status = axis in operation)
- `MC_MoveVelocity` — velocity; it also accepts a change of the
  setpoint while running
- `MC_Stop` — controlled stop along the decel ramp
- `MC_Reset`, `MC_ReadActualVelocity`, `MC_ReadStatus`
- positioning `MC_MoveAbsolute/MOVEREL/HOME/READACTPOS` (for the SPI
  stepper backends POWERSTEP01 / TMC5160)
- `CO_CIA402` — the core of the state machine (a building block for
  composites)
- `CO_SDOWRITE` — writes a parameter **at startup** (it is translated
  into commissioning; an SDO is never executed inside the cycle)
- `CO_RAMPTIME` — ACC/DEC ramp times in seconds for the commanded
  speed; they are written to the drive only while the axis is stopped

## The supplied DRIVE_i550 block

```
              ┌────────────────┐
  command ────┤ Enable Running ├──── running
  setpoint ───┤ Speed  ActualS.├──── speed
  direction ──┤ Reverse        │
              └───────┬────────┘
                      axis1 (CANopen node …)
```

Inside: `MC_Power` + `MC_MoveVelocity` + `MC_ReadActualVelocity`. STOP = dropping
Enable → the drive coasts down along its own decel ramp and disables
itself. Read the diagnostics (current, torque, DC link, frequency …)
with **CANopen data variables** and `gain` scaling (for example ‰ → A); no
blocks are needed for that.

Verified i550 objects: the actual output frequency is **0x2DDD**
(0.1 Hz); 0x2D87 is the ramped setpoint (at standstill it holds the
setpoint).

## Safety

The motor only starts **from a deliberate operator command** (a button
on the display / in WEBview). Stopping over CANopen is **not** a safety
function — the drive's STO terminals and the limit switches must be
hard-wired.
