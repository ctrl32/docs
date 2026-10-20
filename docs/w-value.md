---
image: img/gallery-value.webp
image_alt: "The value widget on a screen"
---

# value

**Text and values** · in a project file: `type: value`

A live number, with the decimals and the unit of its variable.

![The value widget on a screen](img/gallery-value.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | required | what it shows |
| `font` | font | - | which face and size |
| `show_unit` | yes / no | yes | append the variable's unit |
| `warn_above` | number | - | draw differently above this |
| `warn_color` | colour | - | the colour to use then |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](states-motion.md) - see the [Property reference](widgets.md).

## Description

A number, live. It can show any variable. The decimals and the unit
come from the **variable**, not from the widget — set them once in
the variable table and every screen showing it agrees. A variable
with two decimals and unit `bar` shows `4.25 bar` on the board, in
the browser and in a trend legend. If a value shows too many digits,
fix the variable. `show_unit` exists for the case where the unit is
already in a label beside it and repeating it would be noise.

A value always sits in the middle of its rectangle's height; a label
beside it with `valign: center` and the same height stands on the
same baseline.

**`warn_above` is the cheapest alarm on any screen.** A temperature
that turns amber past 80 needs no alarm definition, no acknowledgement
and no extra widget — and it is read from across the room by somebody
who is not looking for it.

Use it for the soft limit, and a real alarm (see the `alarm_table`)
for the hard one. Together they give a warning stage and an action
stage.

A number without a deadband on its variable repaints on every flicker
of the last digit; set the deadband on the variable (see
[Variables](variables.md)).

!!! tip "Make the important number bigger than feels sensible"
    A screen with one number in a large font and everything else small
    is readable from a distance and instantly tells the reader what
    this screen is *about*. Five numbers of the same size is a screen
    with no subject.

---

Every widget of the family: [Text and values](widgets-text.md) · every widget: [Property reference](widgets.md)
