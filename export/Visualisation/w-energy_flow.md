---
title: "Charts: energy_flow"
slug: w-energy_flow
section: "Visualisation"
order: 71
sidebar_position: 71
image: img/wl-energy_flow.webp
image_alt: "The energy_flow widget on a screen"
generator: tools/docs_export.py
---

# energy_flow

**Charts** · in a project file: `type: energy_flow`

Circles joined by lines along which dots run in the direction the energy flows.

![The energy_flow widget on a screen](img/wl-energy_flow.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `nodes` | list | - | the circles, at most 8 |
| `links` | list | - | the lines between them, at most 12 |
| `max` | number | `10.0` | the value at which the dots run fastest |
| `font` | font | - | how the values are drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

Circles with an icon, a value and a name, joined by lines along which
dots run **in the direction the energy flows** — solar, grid, battery
and the house in one picture.

Each node shows its own variable. Each link has a variable whose
**sign is the direction** (positive = from `from` to `to`) and whose
size sets the speed; a link at zero stands still and dims. Feeding the
grid and drawing from it is one link and one signed value — the dots
turn round on their own.

| Node key | Meaning |
|:---|:---|
| `name` | what the links call it |
| `x`, `y` | its centre, in the widget's frame |
| `size` | the circle's diameter; 0 = from the widget |
| `icon` | the glyph in the circle |
| `tag` | the value it shows |
| `color` | the circle and its dots |
| `label` | the name under it |

| Link key | Meaning |
|:---|:---|
| `from`, `to` | the two nodes, by name |
| `tag` | the signed flow |
| `color` | the line and its dots |

```yaml
- type: energy_flow
  rect: [20, 20, 580, 360]
  max: 5
  nodes:
    - { name: solar, x: 290, y: 70, size: 90, icon: solar-panel, tag: pv, label: "Solar" }
    - { name: home, x: 510, y: 180, size: 90, icon: home-bolt, tag: load, label: "Home" }
    - { name: grid, x: 70, y: 180, size: 90, icon: plug-connected, tag: grid, label: "Grid" }
  links:
    - { from: solar, to: home, tag: pv_home }
    - { from: grid, to: home, tag: grid }
```

It draws the present only and costs nothing beyond the widget.

!!! tip "Behind glass"
    An energy flow looks best over a picture of the house, on a
    translucent `panel`: set the panel's `opacity` and the photograph
    shows through the card.

---

Every widget of the family: [Charts](/docs/visualisation/widgets-charts/) · every widget: [Property reference](/docs/visualisation/widgets/)
