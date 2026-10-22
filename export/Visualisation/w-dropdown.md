---
title: "Controls: dropdown"
slug: w-dropdown
section: "Visualisation"
order: 46
sidebar_position: 46
image: img/wl-dropdown.webp
image_alt: "The dropdown widget on a screen"
generator: tools/docs_export.py
---

# dropdown

**Controls** · in a project file: `type: dropdown`

The chosen option in a box; a tap opens the list and a pick writes the option's number.

![The dropdown widget on a screen](img/wl-dropdown.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | required | the number of the chosen option |
| `options` | text | required | one option per line |
| `font` | font | - | how the text is drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

The chosen option in a box with an arrow. A tap opens the list **over
the screen** — on the board and in the browser alike — and a pick
writes the option's **number** into the variable: 0 for the first
line, 1 for the second. The logic works with the number; the person
reads the words.

Use it where there are more choices than room: a scene, a recipe
group, a language. With two to four options always worth seeing, a
`button_matrix` shows them all at once. The two write the same kind of
value, so both can sit on one variable and choosing in one moves the
other.

```yaml
- type: dropdown
  rect: [40, 236, 368, 44]
  tag: scene
  options: [Day, Evening, Night, Away]
```

With a knob, a press on a focused dropdown enters edit and a turn
moves by one option.

---

Every widget of the family: [Controls](/docs/visualisation/widgets-controls/) · every widget: [Property reference](/docs/visualisation/widgets/)
