---
title: "Images and icons: line"
slug: w-line
section: "Visualisation"
order: 66
sidebar_position: 66
image: img/wl-line.webp
image_alt: "The line widget on a screen"
generator: tools/docs_export.py
---

# line

**Images and icons** · in a project file: `type: line`

A line through points in the widget's own frame - a pipe, an arrow, an outline.

![The line widget on a screen](img/wl-line.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `points` | list | - | the corners, x, y pairs in the widget's own frame |
| `width` | integer | `2` | how thick it is, px |
| `closed` | yes / no | no | join the last point to the first |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A line through its points in the fg colour, smoothed at the edges. A
pipe on a process picture, an arrow, a fixed profile drawn behind a
live value, a triangle — `closed` turns the line into an outline.

The points are relative to the widget's rectangle, so moving the
widget moves the drawing with it. A line can be turned by `rotate:`.

```yaml
- type: line
  rect: [40, 400, 368, 130]
  points: [[0, 110], [90, 50], [180, 80], [270, 20], [368, 60]]
  width: 3
```

---

Every widget of the family: [Images and icons](/docs/visualisation/widgets-graphics/) · every widget: [Property reference](/docs/visualisation/widgets/)
