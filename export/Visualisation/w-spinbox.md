---
title: "Controls: spinbox"
slug: w-spinbox
section: "Visualisation"
order: 48
sidebar_position: 48
image: img/wl-spinbox.webp
image_alt: "The spinbox widget on a screen"
generator: tools/docs_export.py
---

# spinbox

**Controls** · in a project file: `type: spinbox`

A value between a minus and a plus button, stepping within its range.

![The spinbox widget on a screen](img/wl-spinbox.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | required | what it writes |
| `min` | number | `0.0` | the bottom of the range |
| `max` | number | `100.0` | the top of the range |
| `step` | number | `1.0` | how far one tap moves the value |
| `font` | font | - | how the value is drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

The value between a minus and a plus button. Each tap moves it by
`step` and never past `min` or `max`; a tap on the number itself
opens the keypad for a value further away.

This is the compromise the `slider` page recommends, in one widget: a
temperature setpoint in steps of 0.5 °C, a count in steps of one —
exact, and without a keypad for the common small change. Where the
exact number matters more than the feel, the spinbox is a better tool
than the `arc`.

```yaml
- { type: spinbox, rect: [640, 130, 184, 50], tag: sp_night, min: 12, max: 24, step: 0.5 }
```

With a knob, a press on a focused spinbox enters edit and a turn moves
the value by its step.

---

Every widget of the family: [Controls](/docs/visualisation/widgets-controls/) · every widget: [Property reference](/docs/visualisation/widgets/)
