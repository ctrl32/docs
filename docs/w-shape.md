---
image: img/wl-shape.webp
image_alt: "The shape widget on a screen"
---

# shape

**Images and icons** · in a project file: `type: shape`

A rectangle or an ellipse that fills the widget.

![The shape widget on a screen](img/wl-shape.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `shape` | one of `rect` / `ellipse` | `rect` | what it draws: rect or ellipse |
| `fill` | yes / no | yes | fill it with bg |
| `border_width` | integer | `1` | the outline, in fg, px |
| `radius` | integer | `0` | rounded corners of a rectangle, px |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](states-motion.md) - see the [Property reference](widgets.md).

## Description

A rectangle or an ellipse that fills the widget. A tank, a frame round
a group, a lamp drawn the size of the real one, a ring.

Shapes with [states](states-motion.md) are cheap animation: a shape
that changes colour with a variable is a running motor on a mimic
diagram without a single picture in the project.

A shape can be turned by `rotate:`: a rectangle turns, an ellipse
keeps its axes.

---

Every widget of the family: [Images and icons](widgets-graphics.md) · every widget: [Property reference](widgets.md)
