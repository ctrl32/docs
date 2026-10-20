# nav

**Controls** · in a project file: `type: nav`

A button that moves to another screen and writes no variable.

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `text` | text | - | the label |
| `target` | text | required | which screen to show |
| `icon` | image_ref | - | a glyph beside the text |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](states-motion.md) - see the [Property reference](widgets.md).

## Description

Moves between screens. That is all it does — it writes no variable
and the logic never sees it. A project has up to 32 screens (the
Linux runtime carries more, see [HMIview](hmiview.md)); one is shown
at a time and the operator moves between them with `nav` widgets.

With a knob, a press on a focused nav button acts exactly as a tap
would.

!!! tip "Keep navigation in the same place on every screen"
    A row of nav buttons along the bottom, identical everywhere, means
    somebody can move around without reading. Navigation that jumps
    around by screen makes people hunt, and hunting is what they do
    least well when something has gone wrong.

---

Every widget of the family: [Controls](widgets-controls.md) · every widget: [Property reference](widgets.md)
