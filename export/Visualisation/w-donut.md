---
title: "Charts: donut"
slug: w-donut
section: "Visualisation"
order: 73
sidebar_position: 73
image: img/wl-donut.webp
image_alt: "The donut widget on a screen"
generator: tools/docs_export.py
---

# donut

**Charts** · in a project file: `type: donut`

A ring - one value filling it, or slices in the ratio of several variables.

![The donut widget on a screen](img/wl-donut.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | - | the value of a single ring |
| `series` | list | - | the slices |
| `min` | number | `0.0` | the bottom of a single ring's range |
| `max` | number | `100.0` | the top of a single ring's range |
| `thickness` | integer | `0` | the ring's width, px; 0 = a quarter of the radius |
| `show_value` | yes / no | yes | the value in the middle |
| `font` | font | - | how the value is drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A ring, in one of two ways:

- **one value** fills the ring from `min` to `max` and stands in its
  middle — a battery's charge, a tank, a share in per cent;
- **slices** with `series`: the ring is cut in the ratio of the
  variables, each in its colour — where the house's power goes, what
  the solar panels feed. The middle then shows their sum.

```yaml
- { type: donut, rect: [20, 410, 170, 170], tag: soc, min: 0, max: 100, thickness: 16 }
- type: donut
  rect: [210, 410, 170, 170]
  thickness: 18
  series:
    - { tag: pv_home, color: "#5BD18B", label: "Home" }
    - { tag: pv_bat, color: "#F15BB5", label: "Battery" }
    - { tag: pv_grid, color: "#FFD166", label: "Grid" }
```

It draws the present only and costs nothing beyond the widget.

---

Every widget of the family: [Charts](/docs/visualisation/widgets-charts/) · every widget: [Property reference](/docs/visualisation/widgets/)
