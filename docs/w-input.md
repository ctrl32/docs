---
image: img/gallery-controls.webp
image_alt: "The input widget on a screen"
---

# input

**Controls** · in a project file: `type: input`

A field that opens the board's own keypad to type a value within limits.

![The input widget on a screen](img/gallery-controls.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | required | what it writes |
| `keypad` | one of `numeric` / `integer` / `alphanumeric` / `password` | - | which keypad opens: numeric, integer, alphanumeric or password |
| `min` | number | - | the lowest accepted value, in the variable's unit |
| `max` | number | - | the highest accepted value, in the variable's unit |
| `title` | text | - | shown above the keypad |
| `font` | font | - | how the value is drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](states-motion.md) - see the [Property reference](widgets.md).

## Description

Touching it opens a keypad on the board — the board's own, not the
operating system's, because a board has no operating system to ask.
It binds a number or a `TIME` with access `rw`.

**Set `min` and `max`** — in the variable's unit. They are the only
thing standing between a mistyped digit and a setpoint of 9000. The
keypad refuses a value outside the range and says so, which is far
better than accepting it and having the logic clamp it silently.

The browser keypad of WEBview follows the same rules as the one on
the board: it shows and takes the number in the variable's unit — a
`TIME` in seconds when the variable says seconds — and applies the
widget's limits only when the widget has them.

`title` is worth filling in: a keypad with "Target temperature (°C)"
at the top is unambiguous, one with just a number is a guess.

---

Every widget of the family: [Controls](widgets-controls.md) · every widget: [Property reference](widgets.md)
