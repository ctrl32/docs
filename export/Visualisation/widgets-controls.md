---
title: "Controls"
slug: widgets-controls
section: "Visualisation"
order: 23
sidebar_position: 23
generator: tools/docs_export.py
---

# Controls

The widgets a person can touch: a button, a switch, a slider, a numeric
input and a navigation button, and beside them a checkbox, a dropdown, a
roller, a spinbox, a button matrix, an arc knob, a calendar and a menu.

![Every control on one screen of a home dashboard](img/wl-controls.webp){: .sb-center}

Everything here writes into a variable. The logic reads that variable and
decides what to do — a button does not start a motor, it sets a bit, and
the program starts the motor. That indirection is what lets the same
screen work on the board and in a browser, and what lets the logic refuse
a command that arrives at the wrong moment.

---

![The controls family: toggle and momentary buttons, a switch, a slider and an input, live in simulation](img/gallery-controls.webp){: .sb-center}

## The widgets

<!-- w-index: begin -->

| Widget | What it is |
|:---|:---|
| [button](/docs/visualisation/w-button/) | A press that writes a variable - momentary, toggle, set or reset, or a recipe action. |
| [switch](/docs/visualisation/w-switch/) | A switch that shows a state and changes it, optionally one bit of an integer. |
| [slider](/docs/visualisation/w-slider/) | A slider for a value where the approximate setting matters more than the exact number. |
| [nav](/docs/visualisation/w-nav/) | A button that moves to another screen and writes no variable. |
| [input](/docs/visualisation/w-input/) | A field that opens the board's own keypad to type a value within limits. |
| [recipe_table](/docs/visualisation/w-recipe_table/) | The slots of one recipe definition, for selecting, saving, loading and deleting sets. |
| [checkbox](/docs/visualisation/w-checkbox/) | A box with a tick and a label that toggles a BOOL or one bit of an integer. |
| [dropdown](/docs/visualisation/w-dropdown/) | The chosen option in a box; a tap opens the list and a pick writes the option's number. |
| [roller](/docs/visualisation/w-roller/) | A drum of options whose middle row is the value. |
| [spinbox](/docs/visualisation/w-spinbox/) | A value between a minus and a plus button, stepping within its range. |
| [button_matrix](/docs/visualisation/w-button_matrix/) | A grid of buttons of which one is selected - a segmented control. |
| [arc](/docs/visualisation/w-arc/) | A round knob: drag along the track to set a value read at a glance. |
| [menu](/docs/visualisation/w-menu/) | Rows of text with icons, each opening a screen or writing a value. |
| [calendar](/docs/visualisation/w-calendar/) | A month; the variable holds a date as one number YYYYMMDD. |
| [wheel](/docs/visualisation/w-wheel/) | A ring of icons with captions - the home screen of a round glass with a knob. |

<!-- w-index: end -->

## The knob

A panel with an encoder around its glass is driven without a finger. The
project names the encoder (one of its `encoders:`) and, when the encoder
has one, its push button — a BOOL variable:

```yaml
encoders:
  - { name: knob, a: 40, b: 41, mode: x4, position_tag: knob_pos }
knob: { encoder: knob, button: knob_btn, steps: 4 }
```

From then on the glass behaves the way an encoder-driven interface is
expected to:

- a **turn moves the focus** between the screen's controls in drawing
  order, wrapping at the end — the focused control wears a ring in its
  accent colour;
- a **press on a button**, a switch, a checkbox or a navigation button
  acts, exactly as a tap would;
- a **press on a value widget** — a slider, an arc, a roller, a spinbox,
  a dropdown, a menu, a tileview, a calendar — enters **edit**: the ring
  becomes solid and a turn changes the value (a slider or an arc walks
  its range in fifty steps, a spinbox by its step, a list by one
  option); a second press leaves edit;
- a **long press** leaves edit, or, with nothing in edit, opens the
  project's first screen — the way home;
- a `wheel` takes the turns itself and a press activates its selected
  item.

A screen with a single control starts with it focused, so a page that is
one arc turns at once. A tap on the glass moves the focus to what it
touched; touch and knob live together. `steps` is the number of encoder
counts per detent (4 = one quadrature cycle), `invert` turns the
direction round.

The browser follows the same rules from the keyboard: the arrow keys
turn, Enter presses, Escape is the long press.

---

## What controls do not do

A control never acts directly on an output. It writes a variable; the
logic decides.

That sounds like an extra step and it is the reason the same screen works
in a browser, the reason a command can be refused while the equipment is in
the wrong state, and the reason you can test every screen in simulation
without anything being wired up at all.
