---
title: "Forcing values"
slug: force
section: "Operation"
order: 340
sidebar_position: 340
generator: tools/docs_export.py
---

# Forcing values

Everything else in the editor **shows** a setup. This one **changes**
it: a valve opens because somebody typed a number on a laptop. Forcing is
a commissioning aid — for checking wiring, exercising an output before the
sensor exists, or proving an interlock — and it is not a way to run
equipment.

Open it from *Online → Force*.

## What it does

A forced variable is held by the **board**, not by the editor. The value is
written into the variable on both sides of the program: before the logic runs,
so the logic reads it, and after, so an output the logic just wrote is
overridden. That is the standard scan model — anything else would make
forcing an input work and forcing an output quietly not.

The program cannot win against a force. That is the point, and it is why
the rules below matter.

## How long it lasts

| | |
|:---|:---:|
| Released when you release it | yes |
| Released when the editor closes or the cable is pulled | **no** |
| Released by a power cycle | **yes** — the table is RAM |
| Optional timeout | yes, in seconds; `0` means hold until released |

Closing the editor deliberately does **not** release a force: a
technician who forces a valve open, walks around the equipment and comes
back expects to find it open. A power cycle does clear it, because a
board that came back from a power failure still holding somebody's value
would be a trap — and the board has no dedicated lamp to
warn about it.

!!! warning "A forced variable that is retentive keeps its last value"
    Forcing is gone after a restart, but if the variable itself is retentive,
    the **value** it was left at survives — that is the variable's property,
    not the force's. The program owns it again from the first cycle.

## Nothing is silent

- Every set, release and expiry goes into the board's **diagnostic
  buffer**, so its own log carries what was held and for how
  long.
- The editor's **status bar** shows `FORCED n` in a colour that belongs
  to nothing else, on every page, and clicking it opens this window.
- The list in the window is what the **board** reports, never what this
  editor asked for. The two differ the moment a force expires or somebody
  else releases one, and the equipment is the party telling the truth.

## Using it

1. Pick the variable from the list (the filter takes a substring).
2. Set the value. A BOOL gets a checkbox; a number gets a field; a TIME
   variable is forced in milliseconds.
3. Leave the hold at `0` to keep it until you release it, or enter
   seconds for a timeout the board enforces itself.
4. *Force this value*.

Release one with the button next to it, or all of them with *Release
all* — which is never disabled while anything is held.

## Limits and refusals

| | |
|:---|:---:|
| Forced variables at once | 8 |
| Longest timeout | 1 hour |
| Requires | ONLINE, and the same program in editor and board |

Eight is deliberate. Somebody who needs to force nine things at once is
not commissioning any more, they are rewriting the program — and that
belongs in the editor, not in a live equipment.

!!! danger "This is not a safety function"
    Forcing bypasses your program's logic, including its interlocks. It
    does not bypass hard-wired safety — emergency stop, doors and light
    curtains are wired, not programmed — and nothing here changes the
    rule that [safety is never routed through the board](/docs/index/).
