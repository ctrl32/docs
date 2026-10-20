---
image: img/gallery-controls.webp
image_alt: "The switch widget on a screen"
---

# switch

**Controls** · in a project file: `type: switch`

A switch that shows a state and changes it, optionally one bit of an integer.

![The switch widget on a screen](img/gallery-controls.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | required | what it writes |
| `label_on` | text | `ON` | text in the on position |
| `label_off` | text | `OFF` | text in the off position |
| `bit` | integer | `-1` | which bit of an integer; -1 = the whole value |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](states-motion.md) - see the [Property reference](widgets.md).

## Description

A switch shows its state *and* changes it, which a button cannot. Use
it where the state matters as much as the act of switching: automatic
/ manual, enabled / disabled, day / night.

**`bit` is worth knowing about.** Point several switches at the same
integer variable with different bit numbers and you get a row of
options in one variable — one word to send over a fieldbus, one value
to store, one thing for the logic to read. Bits are written
atomically, so the switches never overwrite one another; lamps on
other bits of the same word may be driven by the program at the same
time. See [Variables](variables.md).

A switch with `visible_if` on the manual-mode variable exists only in
manual mode, with an AUTO badge standing in its place in automatic —
nobody flips a heater that is not there (see
[States and motion](states-motion.md)). With a state, `paint: accent`
(the default) drives a switch's active colour.

With a knob, a press on a focused switch acts exactly as a tap would.

---

Every widget of the family: [Controls](widgets-controls.md) · every widget: [Property reference](widgets.md)
