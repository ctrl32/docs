---
title: "Controls: button_matrix"
slug: w-button_matrix
section: "Visualisation"
order: 49
sidebar_position: 49
image: img/wl-button_matrix.webp
image_alt: "The button_matrix widget on a screen"
generator: tools/docs_export.py
---

# button_matrix

**Controls** · in a project file: `type: button_matrix`

A grid of buttons of which one is selected - a segmented control.

![The button_matrix widget on a screen](img/wl-button_matrix.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | required | the number of the selected button |
| `buttons` | text | required | one caption per button |
| `columns` | integer | `0` | buttons in a row; 0 = all in one row |
| `font` | font | - | how the captions are drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A grid of buttons of which **one is selected** — a segmented control:
Auto / Manual / Off, Day / Evening / Night / Away. A tap writes the
button's number into the variable and the selected one is drawn in
the accent.

It and the `dropdown` write the same kind of value, so both can sit on
one variable: the picture's screen has a dropdown and a matrix on the
same scene, and choosing in one moves the other.

```yaml
- type: button_matrix
  rect: [40, 396, 368, 100]
  tag: scene
  buttons: [Day, Evening, Night, Away]
  columns: 2
```

---

Every widget of the family: [Controls](/docs/visualisation/widgets-controls/) · every widget: [Property reference](/docs/visualisation/widgets/)
