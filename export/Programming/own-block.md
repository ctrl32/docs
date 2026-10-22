---
title: "Your own function block"
slug: own-block
section: "Programming"
order: 80
sidebar_position: 80
generator: tools/docs_export.py
---

# Your own function block

A function block is a piece of logic with a name, an **interface** (its
input and output pins) and a body that does the work. Once it exists you
use it like `TON` or `CTU`: drop it on a rung, bind its pins, done. Every
use gets its own state, so ten pumps are ten instances of one block, not
ten copies of three rungs.

This page builds one from nothing, in ladder, and uses it twice. The
finished project is `tutorials\own_block.prj32`. Half an hour; no hardware
needed.

**What we are building:** `STARTSTOP` — a start/stop latch with two
inputs (`Start`, `Stop`) and one output (`Run`). Press Start and Run
comes on; it stays on until Stop. The oldest pattern in control, and the
one every pump, fan and conveyor needs.

---

## 1. Create the block

Right-click **Application** in the project tree and choose *Add POU…*.

![The New POU dialog: a name, the language, the type](img/newpou-dialog.webp){: .sb-center}

| Field | Choose | Why |
|:---|:---|:---|
| **name** | `STARTSTOP` | this becomes the block's name in the block list |
| **language** | `LD` | the body is drawn as rungs; `FBD` and `ST` work the same way |
| **type** | `FB` | a function block — it has an interface and keeps state |

*OK* creates the block and opens its page. A new block starts with two
inputs (`IN1`, `IN2`) and one output (`Q`) so that it can be placed
straight away; the next step renames them.

!!! note "PRG, FB, FC"
    A **PRG** is a program: it runs every cycle on its own. An **FB** is a
    block: it runs only where it is placed, once per instance. **FC** (a
    stateless function) is not available yet — use an FB.

---

## 2. Define the interface

Above the rungs sits the **Variables (interface)** pane. Click its header
to open it.

![The interface pane of STARTSTOP: two inputs, one output, the buttons that add more](img/ownblock-iface.webp){: .sb-center}

The pane is the block's declaration in the PLCopen shape:

| Row | Meaning |
|:---|:---|
| `VAR_INPUT` | an input pin — the block reads it |
| `VAR_OUTPUT` | an output pin — the block writes it |
| `VAR` | the local wires the diagram makes between its own blocks (listed, not edited) |

Rename the three pins by typing into the name fields: `IN1` → `Start`,
`IN2` → `Stop`, `Q` → `Run`. The type is `BOOL` or `REAL` per pin.
*+ input* and *+ output* add pins; the *x* removes one. A block has at
most **4 inputs and 2 outputs** — that is the size of a block on a rung.

Every change of the interface bumps the block's version. Instances already
placed in a program are migrated when the block is next built, so a pin
added later does not wreck a program that uses the old shape.

!!! tip "Name pins for the caller"
    `Start` and `Stop` read well on a rung. `IN1` and `IN2` mean nothing
    to whoever wires the block up in a year.

---

## 3. Draw the body

Inside the block, its pins appear as variables named after it —
`STARTSTOP.Start`, `STARTSTOP.Stop`, `STARTSTOP.Run`. A contact on an input
pin reads it; a coil on the output pin writes it.

Two rungs make the latch:

```
1   |--[ STARTSTOP.Start ]-------------------( S  STARTSTOP.Run )--|
2   |--[ STARTSTOP.Stop  ]-------------------( R  STARTSTOP.Run )--|
```

1. On the first rung place a contact (*-[ ]-*), bind it to `Start`; add a
   coil and set it to **-(S)-** (set), bound to `Run`.
2. *+ Rung*, a contact bound to `Stop`, a coil set to **-(R)-** (reset),
   bound to `Run`.

That is the whole block. A set and a reset coil on one variable compile to
a single `SR` latch — the builder does that, you draw the two rungs.

Everything a rung can carry works inside a block: timers, counters,
comparisons, other blocks. Two things are refused by design, at build
time and with the rung named: a block calling itself, and a nesting deeper
than 8. A flattened block may hold at most 64 elementary blocks.

---

## 4. Use it

Open **PLC_PRG**. Your block is in the list the **FB** button of the rung
toolbar opens, next to the shipped ones, and in the Toolbox's block
groups. Place it on a rung:

![PLC_PRG: STARTSTOP twice, each with its own start, stop and contactor](img/ownblock-use.webp){: .sb-center}

The rung is the block's first input: the contact before the block drives
`Start`. The first output continues the rung into the coil: `Run` writes
`m1_run`. The remaining pins are bound in the block's sheet — double-click
it — or in the **Properties** panel below, which shows the same rows:
`Stop` ← `m1_stop`.

The second rung is the same block again with `m2_start`, `m2_stop`,
`m2_run`. The two instances do not share anything: pump 2 keeps running
when pump 1 is stopped, because every use of a block gets its own copy of
its state.

The six variables (`m1_start`, `m1_stop`, `m1_run`, and the `m2_` three)
are ordinary BOOL variables in **VAR**; the start and stop ones are `rw`
so a screen can press them.

---

## 5. A screen, and a run

A screen with two rows — a label, a *Start* button, a *Stop* button
(both `momentary`), and a lamp on the `_run` variable:

![The screen: two pumps, one block](img/ownblock-screen.webp){: .sb-center}

Press **Simulate**. Start pump 1: its lamp lights and stays. Start
pump 2: two lamps. Stop pump 1: one lamp left. Nothing was written twice,
and the latch lives inside the block.

---

## Changing a block later

- **Adding a pin** — the *+ input* / *+ output* buttons; instances keep
  their existing bindings and show the new pin as unbound (`...`).
- **Removing a pin** — the *x*; a binding to it disappears from every
  instance, so look at the program afterwards.
- **A block from a library** — a supplied one such as `DRIVE_i550` is
  read-only: you can open it and read it, not change it. *Save as own*
  makes an editable copy in the project, under your name.
- **Sharing a block** — a block lives in the project file. A block library
  for many projects is a `.yaml` under `libraries\`, see
  [FBD, composites and drives](/docs/programming/fbd-composites/).

---

## Where to go from here

| You want to | Read |
|:---|:---|
| write the body in text instead of rungs | [Structured Text](/docs/programming/st-language/) — `FUNCTION_BLOCK` with `VAR_INPUT` / `VAR_OUTPUT` |
| draw it as a diagram | [FBD](/docs/programming/fbd-composites/) |
| see what the shipped blocks offer before writing your own | [Function blocks](/docs/blocks/) |
| bind a block to a drive | [Motion](/docs/blocks/blocks-motion/) |
