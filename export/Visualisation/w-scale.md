---
title: "Indicators: scale"
slug: w-scale
section: "Visualisation"
order: 58
sidebar_position: 58
image: img/wl-scale.webp
image_alt: "The scale widget on a screen"
generator: tools/docs_export.py
---

# scale

**Indicators** · in a project file: `type: scale`

A straight scale with numbered ticks and a pointer at the value.

![The scale widget on a screen](img/wl-scale.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | - | where the pointer sits |
| `min` | number | `0.0` | the bottom of the range |
| `max` | number | `100.0` | the top of the range |
| `major` | integer | `5` | numbered ticks |
| `minor` | integer | `4` | ticks between two numbered ones |
| `orientation` | one of `horizontal` / `vertical` | `horizontal` | how it lies: horizontal or vertical |
| `font` | font | - | how the numbers are drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A straight scale with numbered and small ticks. With a variable a
pointer in the accent shows where the value sits on it.

A scale is what a `bar` is missing when the position matters more than
the fill: a pressure against its working range, a level against its
marks. Laid upright beside a tank picture, it reads like the sight
glass on the real one.

---

Every widget of the family: [Indicators](/docs/visualisation/widgets-indicators/) · every widget: [Property reference](/docs/visualisation/widgets/)
