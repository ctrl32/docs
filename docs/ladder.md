# Ladder (LD) on ctrl32

The ladder editor draws the logic the way an electrician reads a
schematic: rungs between two power rails, contacts in series and in
parallel, the coil at the right. Underneath there is no separate
"ladder runtime" — every rung compiles into the same function blocks
the FBD editor produces and the panel already executes. Uploading a
ladder program is uploading data, never firmware.

## Elements (v1)

| Symbol | Meaning |
|---|---|
| `-[ ]-` | NO contact — conducts while the tag is TRUE |
| `-[/]-` | NC contact — conducts while the tag is FALSE |
| `-[P]-` / `-[N]-` | rising / falling edge (one cycle) |
| `-( )-` | coil — the rung result lands in the tag |
| `-(S)-` / `-(R)-` | set / reset latch |
| block in the rung | TON, TOF, TP, CTU, CTD — the rung drives IN, Q carries on |

Blocks show their second output at the right stub: a counter its **CV**
(how many it has counted), a timer its **ET** (how long it has been
running). Bind it to a tag, or just read it — during
[online monitoring](online.md) the value comes straight from the machine.

Series contacts AND together; a parallel branch ORs. The classic
start/stop seal-in is exactly:

```
|--[ start ]--+--[/ stop ]-----------------( run )--|
|--[ run   ]--+
```

## Working with rungs

- **+ Rung** adds a rung; **click a contact or the coil** to change
  its tag (with a filter), its kind, insert contacts before/after,
  add a parallel branch, drop a timer/counter into the rung, or move
  the rung up/down. Everything is undoable.
- A `(S)` and `(R)` pair on the same tag becomes ONE flip-flop; the
  pair's order decides the priority (set-first = set wins).
- **Two plain coils on one tag are refused at the desk** — the last
  writer would silently win on the panel. Use a branch or S/R.
- Every contact and coil shows its variable name and, underneath,
  the tag's **description as a `//comment`** (edited right in the
  element popup; the *comments* checkbox hides them when the rungs
  should pack tighter). Descriptions travel with the project.
- In **test mode** the rungs show the live power flow: conducting
  wires and symbols turn green, the coil fills when its tag is TRUE.
  This is the same test PLC the FBD scheme uses. Clicking a contact
  toggles its tag.

## Ladder and FBD

A program belongs to ONE editor. Ladder-owned programs carry the
ladder icon in the tree and open in the LD editor; opening them in
FBD is read-only (the blocks are regenerated from the rungs, edits
there would be lost). An FBD network that fits the ladder subset can
be viewed as rungs; anything richer — analog paths, multiple
consumers of one output, PID — stays in FBD or moves to ST.

## Limits

32 rungs per program, 8 parallel branches per fork, one coil column.
The real ceiling is the shared block budget (64 blocks) — the
Resources panel shows the consumption as you build.
