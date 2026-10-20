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
| [button](w-button.md) | A press that writes a variable - momentary, toggle, set or reset, or a recipe action. |
| [switch](w-switch.md) | A switch that shows a state and changes it, optionally one bit of an integer. |
| [slider](w-slider.md) | A slider for a value where the approximate setting matters more than the exact number. |
| [nav](w-nav.md) | A button that moves to another screen and writes no variable. |
| [input](w-input.md) | A field that opens the board's own keypad to type a value within limits. |
| [recipe_table](w-recipe_table.md) | The slots of one recipe definition, for selecting, saving, loading and deleting sets. |
| [checkbox](w-checkbox.md) | A box with a tick and a label that toggles a BOOL or one bit of an integer. |
| [dropdown](w-dropdown.md) | The chosen option in a box; a tap opens the list and a pick writes the option's number. |
| [roller](w-roller.md) | A drum of options whose middle row is the value. |
| [spinbox](w-spinbox.md) | A value between a minus and a plus button, stepping within its range. |
| [button_matrix](w-button_matrix.md) | A grid of buttons of which one is selected - a segmented control. |
| [arc](w-arc.md) | A round knob: drag along the track to set a value read at a glance. |
| [menu](w-menu.md) | Rows of text with icons, each opening a screen or writing a value. |
| [calendar](w-calendar.md) | A month; the variable holds a date as one number YYYYMMDD. |
| [wheel](w-wheel.md) | A ring of icons with captions - the home screen of a round glass with a knob. |

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
