---
title: "Containers: window"
slug: w-window
section: "Visualisation"
order: 34
sidebar_position: 34
image: img/wl-window.webp
image_alt: "The window widget on a screen"
generator: tools/docs_export.py
---

# window

**Containers** · in a project file: `type: window`

A body with a title bar whose X can close it, part of the screen rather than a moment.

![The window widget on a screen](img/wl-window.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `text` | text | - | the title in the bar |
| `tag` | variable | - | written FALSE by the X |
| `bar_height` | integer | `32` | the height of the title bar |
| `font` | font | - | how the title is drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A body with a title bar in the accent. Its children sit under the
bar, in the window's own frame.

With a variable the bar carries an **X**, and the X writes the
variable false. Give the window `visible_if` with the same variable
and the X closes it; anything that sets the variable true again — a
button, a checkbox, the logic reacting to an event — opens it.

```yaml
- type: window
  rect: [872, 548, 368, 146]
  text: "Window"
  tag: win_open
  visible_if: win_open
  children:
    - { type: label, rect: [12, 48, 340, 22], text: "X closes me" }
```

!!! tip "A window or a popup?"
    A `popup` belongs to a moment — a question, a confirmation — and
    covers the screen. A window is part of the screen: a detail that
    can be put away and brought back, while everything around it
    stays usable.

---

Every widget of the family: [Containers](/docs/visualisation/widgets-containers/) · every widget: [Property reference](/docs/visualisation/widgets/)
