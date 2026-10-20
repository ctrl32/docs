---
image: img/gallery-controls.webp
image_alt: "The slider widget on a screen"
---

# slider

**Controls** · in a project file: `type: slider`

A slider for a value where the approximate setting matters more than the exact number.

![The slider widget on a screen](img/gallery-controls.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | required | what it writes |
| `min` | number | `0.0` | the bottom of the range |
| `max` | number | `100.0` | the top of the range |
| `step` | number | `1.0` | the increment, and with it how many values a drag writes |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](states-motion.md) - see the [Property reference](widgets.md).

## Description

For a value where the *approximate* setting matters and the exact
number does not: brightness, speed, a proportion.

`step` also determines how much traffic the slider makes. A step of
0.1 on a range of 0–100 writes a thousand distinct values as a finger
crosses, and every one of them is a change the board redraws and the
browser hears about.

With a knob, a press on a focused slider enters edit and a turn walks
its range in fifty steps.

!!! warning "A slider is a poor way to type a number"
    On a 4.3" screen with a gloved finger, a slider spanning 0–100
    sets values to about five units. Where the number matters — a
    temperature setpoint, a length — use an `input` and let the person
    type it.

    A good compromise: a slider for coarse setting with the value
    shown beside it, and buttons for ±1 — the `spinbox` is that
    compromise in one widget.

---

Every widget of the family: [Controls](widgets-controls.md) · every widget: [Property reference](widgets.md)
