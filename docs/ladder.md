# Ladder (LD) on ctrl32

The ladder editor draws the logic the way an electrician reads a
schematic: rungs between two power rails, contacts in series and in
parallel, the coil at the right. Underneath there is no separate
"ladder runtime" — every rung compiles into the same function blocks
the FBD editor produces and the panel already executes. Uploading a
ladder program is uploading data, never firmware.

## Elements

| Symbol | Meaning |
|---|---|
| `-[ ]-` | NO contact — conducts while the tag is TRUE |
| `-[/]-` | NC contact — conducts while the tag is FALSE |
| `-[P]-` / `-[N]-` | rising / falling edge (one cycle) |
| `-( )-` | coil — the rung result lands in the tag |
| `-(S)-` / `-(R)-` | set / reset latch |
| block in the rung | TON, TOF, TP, CTU, CTD — the rung drives IN, Q carries on |
| **box on the rung** | **any block from the library** with EN/ENO: while the rung conducts it executes, while it does not its state freezes and the outputs hold |

**Everything fits in ladder.** Timers, counters, ramps, filters,
comparators with hysteresis, PID, motor and valve blocks — every block
sits in a rung as a box with the standard EN/ENO behaviour. The Toolbox
offers them in the same groups as the block editor: Boolean, Math,
Timers, Counters, General, Motion, CAN, GSM/GPS.

Blocks show their inner value at the right stub: a counter its **CV**,
a timer its **ET** (elapsed), a blinker its **REM** (time left in the
current phase). Bind it to a tag, or just read it — in simulation and
during [online monitoring](online.md) every stub variable carries its
live value on the line above it.

Series contacts AND together; a parallel branch ORs. The classic
start/stop seal-in is exactly:

```
|--[ start ]--+--[/ stop ]-----------------( run )--|
|--[ run   ]--+
```

## A rung does not need a coil

A new rung starts as a **bare arrow** — no wire across, no coil. Build
it from either end:

- add contacts and finish with a coil — the classic rung;
- or put **blocks on the rail**: a box on a rung with no coil executes
  every cycle (a drawn `TRUE` contact in front of it says so), and the
  run wire simply ends in an arrow. Contacts placed before the boxes
  become their EN condition — no helper variable needed.

## Working with rungs

- **+ Rung** adds a rung; **click a contact, box or the coil** to
  change its tag (with a filter), its kind, insert contacts
  before/after, add a parallel branch or another box. Right-click
  offers cut/copy/paste for elements, boxes and whole rungs, and
  insert rung above/below. Everything is undoable.
- **The comment line above every rung is written directly on the
  canvas** — click it and type, multiple lines welcome, click away to
  keep it. The same text is the network comment in the block-diagram
  view.
- Selecting a rung highlights it with a quiet grey background; the
  palette then targets that rung.
- A `(S)` and `(R)` pair on the same tag becomes ONE flip-flop; the
  pair's order decides the priority (set-first = set wins).
- **Two plain coils on one tag are refused at the desk** — the last
  writer would silently win on the panel. Use a branch or S/R.
- Every contact and coil shows its variable name and, underneath,
  the tag's **description as a `//comment`** (edited right in the
  element popup; the *comments* checkbox hides them when the rungs
  should pack tighter). Descriptions travel with the project.
- In **test mode** the rungs show the live power flow: conducting
  wires, symbols and block frames turn green — the frame as thick as
  the wires, so the active path reads at a glance. Clicking a contact
  toggles its tag (simulation only; connected to a panel everything
  is read-only).

## Ladder and FBD — one owner, two views

A program belongs to ONE editor at a time. A ladder-owned program
opens in the block editor as a read-only view — its networks mirror
the rungs one to one, comments included — and a single button takes
the ownership over when you want to continue in FBD. The way back is
the same button on the other side. Nothing edited in one view can be
silently overwritten by the other.

A function block created from a POU can be drawn in ladder too: its
input and output ports behave as ordinary variables — contacts on the
inputs, the coil on an output (see
[composite blocks](fbd-composites.md)).

## Limits

32 rungs per program, 8 parallel branches per fork, one coil column.
The block budget is shared with the whole program — 512 blocks per
project (see [limits](limits.md)); the Resources panel shows the
consumption as you build.
