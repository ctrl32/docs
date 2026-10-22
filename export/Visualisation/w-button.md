---
title: "Controls: button"
slug: w-button
section: "Visualisation"
order: 39
sidebar_position: 39
image: img/gallery-controls.webp
image_alt: "The button widget on a screen"
generator: tools/docs_export.py
---

# button

**Controls** · in a project file: `type: button`

A press that writes a variable - momentary, toggle, set or reset, or a recipe action.

![The button widget on a screen](img/gallery-controls.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `text` | text | - | the label |
| `text_on` | text | `` | the label while the variable is TRUE (text when ON in the inspector) |
| `tag` | variable | required | what it writes |
| `mode` | one of `momentary` / `toggle` / `set` / `reset` / `recipe_load` / `recipe_save` / `recipe_delete` | - | how it writes: momentary, toggle, set, reset, or a recipe action |
| `value` | number | `1.0` | the value written |
| `icon` | image_ref | - | a glyph beside the text |
| `confirm` | yes / no | no | ask before acting |
| `confirm_text` | text | - | what the question says |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A button writes a variable; it binds a BOOL with access `rw`. A
variable the program alone writes cannot be written from a screen.

**The mode is the whole widget:**

- **`momentary`** — TRUE while held, FALSE when released. A jog
  button, a horn, anything that should stop when the finger leaves.
- **`toggle`** — each press flips the value. A light, a mode, an
  enable. Give it a **`text_on`** (*text when ON* in the inspector)
  and the caption follows the state: the button says START while the
  drive is off and STOP while it runs, filled with the style's accent
  colour. One widget, honest both ways.
- **`set`** / **`reset`** — a press writes the value and leaves it.
  Two buttons, one to start and one to stop, is often clearer than
  one that toggles: the person can see which state they are asking
  for.
- **`recipe_load`** / **`recipe_save`** / **`recipe_delete`** — the
  buttons beside a `recipe_table`: they bind to the table of the same
  screen and need no variable. A button with `confirm` asks first; on
  a delete that is the right default. See [Recipes](/docs/operation/recipes/).

With a knob, a press on a focused button acts exactly as a tap would.

**Setpoint buttons through a rising edge.** A `+` button wired through
`R_TRIG` into an addition steps once per press; holding the button
does not run the setpoint away. Interlocks belong in the logic, not on
the screen: a manual command that may act only while automatic mode
is off is gated in the program, so it holds however the value is
written — from the glass, the browser or a bus.

In WEBview a button does not write into a variable directly. It sends
a **command**, and the board decides whether to accept it.

!!! tip "Use confirm on anything that moves"
    `confirm` is not decoration. Capacitive touch near a frequency
    drive can register presses nobody made, and a sleeve can lean on
    the glass. A dialogue on a command that starts something is the
    difference between electrical noise and an axle turning.

    Write `confirm_text` so it says what will happen — "Start
    conveyor?" beats "Are you sure?".

---

Every widget of the family: [Controls](/docs/visualisation/widgets-controls/) · every widget: [Property reference](/docs/visualisation/widgets/)
