---
title: "Indicators: spinner"
slug: w-spinner
section: "Visualisation"
order: 59
sidebar_position: 59
image: img/wl-spinner.webp
image_alt: "The spinner widget on a screen"
generator: tools/docs_export.py
---

# spinner

**Indicators** · in a project file: `type: spinner`

A turning arc that says wait or busy.

![The spinner widget on a screen](img/wl-spinner.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | - | turns only while it is true |
| `period_ms` | integer | `1000` | one turn, ms |
| `thickness` | integer | `0` | the arc's width; 0 = from the size |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A turning arc that says *wait* or *busy*. With a variable it turns
only while the variable is true and shows just its track otherwise — a
homing run, a recipe being written, a drive ramping up. Without a
variable it always turns.

---

Every widget of the family: [Indicators](/docs/visualisation/widgets-indicators/) · every widget: [Property reference](/docs/visualisation/widgets/)
