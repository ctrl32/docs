---
title: "Controls: roller"
slug: w-roller
section: "Visualisation"
order: 47
sidebar_position: 47
image: img/wl-roller.webp
image_alt: "The roller widget on a screen"
generator: tools/docs_export.py
---

# roller

**Controls** · in a project file: `type: roller`

A drum of options whose middle row is the value.

![The roller widget on a screen](img/wl-roller.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | required | the number of the option in the middle row |
| `options` | text | required | one option per line |
| `rows` | integer | `3` | how many rows are visible (odd, 3 to 9) |
| `font` | font | - | how the text is drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A drum of options; **the middle row is the value**, drawn in the
accent. Drag it up or down, or tap the row above or below the middle,
and the option's number is written into the variable.

A roller suits an ordered choice where the neighbours matter — a fan
stage, a speed, an hour — because the person sees what is one step up
and one step down without opening anything.

With a knob, a press on a focused roller enters edit and a turn moves
by one option.

---

Every widget of the family: [Controls](/docs/visualisation/widgets-controls/) · every widget: [Property reference](/docs/visualisation/widgets/)
