---
title: "Text and values: label"
slug: w-label
section: "Visualisation"
order: 35
sidebar_position: 35
image: img/gallery-value.webp
image_alt: "The label widget on a screen"
generator: tools/docs_export.py
---

# label

**Text and values** · in a project file: `type: label`

Fixed text: a heading, a unit, a name beside a lamp, an instruction.

![The label widget on a screen](img/gallery-value.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `text` | text | - | what it says |
| `font` | font | - | which face and size |
| `align` | one of `left` / `center` / `right` | `left` | left, center or right within its rectangle |
| `valign` | one of `top` / `center` / `bottom` | `top` | where the line sits in the rectangle's height |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

Fixed text: a heading, a unit, a name beside a lamp, an instruction.
It binds no variable.

**Alignment matters more than it looks.** A column of labels aligned
right against a column of values aligned left reads as a table, and
the eye follows it without effort. The same labels aligned left
produce a ragged gap between name and number that the reader has to
cross every time.

**A label beside a value.** A value always sits in the middle of its
rectangle's height. Give the label next to it `valign: center` and
the same height, and the two lines stand on one baseline.

With a [state](/docs/visualisation/states-motion/) painting `fg`, the label's text
changes colour with a variable. A text is never drawn turned by
`rotate:` — a bitmap face does not turn.

**A test line of your own language.** One label with the accented
letters your language needs, on a screen you keep, proves the font
carries them — at your desk, not in front of a customer. The other
controller's address in a label (`DB120.DBW4`) costs nothing and
doubles the screen as the map between the two sides.

!!! warning "Check your language's accented characters early"
    A font baked without the right character range drops accents
    silently — the text renders, just without the marks, and it is
    the kind of thing nobody notices in the editor and everybody
    notices on the board. Put one label with your worst-case word on
    a test screen and look at it on the glass.

---

Every widget of the family: [Text and values](/docs/visualisation/widgets-text/) · every widget: [Property reference](/docs/visualisation/widgets/)
