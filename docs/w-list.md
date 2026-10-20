# list

**Containers** · in a project file: `type: list`

A scrolling container whose children are its rows.

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `item_height` | integer | - | height of one row |
| `inertia` | yes / no | yes | flick scrolling |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](states-motion.md) - see the [Property reference](widgets.md).

## Description

A scrolling container. The children are the rows, and only the
visible ones are drawn — so a long list costs what fits on the
screen, not what it contains.

`inertia` gives the flick-and-glide behaviour a phone has. Leave it
on for capacitive glass; on resistive touch, which wants a firm
press, it is less natural and turning it off can feel more
controlled.

---

Every widget of the family: [Containers](widgets-containers.md) · every widget: [Property reference](widgets.md)
