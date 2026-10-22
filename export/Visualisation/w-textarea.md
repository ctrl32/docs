---
title: "Text and values: textarea"
slug: w-textarea
section: "Visualisation"
order: 37
sidebar_position: 37
image: img/wl-textarea.webp
image_alt: "The textarea widget on a screen"
generator: tools/docs_export.py
---

# textarea

**Text and values** · in a project file: `type: textarea`

Text over several lines, wrapped at the widget's width.

![The textarea widget on a screen](img/wl-textarea.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `text` | text | - | what it shows |
| `tag` | variable | - | a text (STRING) variable to show instead - a Linux device |
| `editable` | yes / no | no | a tap opens the keyboard |
| `align` | one of `left` / `center` / `right` | `left` | how each line sits |
| `font` | font | - | how the text is drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

Text over several lines, **wrapped at the widget's width** — a word
that does not fit starts the next line, and a new line in the text
starts a new line on the screen. An instruction next to a control, a
note on a service page, a paragraph a `label` would cut off.

On a Linux device it can show a text (`STRING`) variable instead of
its fixed text, and with `editable` a tap opens the keyboard: a note
the shift leaves for the next one, a batch comment, a reason for a
stop.

```yaml
- type: textarea
  rect: [1036, 396, 204, 150]
  text: "Scan the code: the same dashboard opens in the browser."
```

---

Every widget of the family: [Text and values](/docs/visualisation/widgets-text/) · every widget: [Property reference](/docs/visualisation/widgets/)
