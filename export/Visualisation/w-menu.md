---
title: "Controls: menu"
slug: w-menu
section: "Visualisation"
order: 51
sidebar_position: 51
image: img/wl-menu.webp
image_alt: "The menu widget on a screen"
generator: tools/docs_export.py
---

# menu

**Controls** · in a project file: `type: menu`

Rows of text with icons, each opening a screen or writing a value.

![The menu widget on a screen](img/wl-menu.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | - | written by the rows that carry a value |
| `items` | list | - | the rows: text, icon, target, value |
| `row_height` | integer | `40` | the height of one row |
| `font` | font | - | how the text is drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

Rows of text, each with an optional icon and an arrow. A row is one of
two things:

- a row with a **`target`** opens that screen — a list of places, the
  way a phone's settings page is a list;
- a row with a **`value`** writes it into the menu's variable and is
  drawn selected while the variable holds it — a list of modes.

| Row key | Meaning |
|:---|:---|
| `text` | what the row says |
| `icon` | a glyph at its left |
| `target` | the screen it opens |
| `value` | the number it writes |

```yaml
- type: menu
  rect: [40, 512, 368, 180]
  row_height: 45
  items:
    - { text: "Climate", icon: flame, target: climate }
    - { text: "Energy", icon: bolt, target: energy }
    - { text: "Home", icon: home, target: home }
```

With a knob, a press on a focused menu enters edit and a turn moves by
one row.

---

Every widget of the family: [Controls](/docs/visualisation/widgets-controls/) · every widget: [Property reference](/docs/visualisation/widgets/)
