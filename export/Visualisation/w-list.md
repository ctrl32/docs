---
title: "Containers: list"
slug: w-list
section: "Visualisation"
order: 30
sidebar_position: 30
generator: tools/docs_export.py
---

# list

**Containers** · in a project file: `type: list`

A scrolling container whose children are its rows.

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `item_height` | integer | - | height of one row |
| `inertia` | yes / no | yes | flick scrolling |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A scrolling container. The children are the rows, and only the
visible ones are drawn — so a long list costs what fits on the
screen, not what it contains.

`inertia` gives the flick-and-glide behaviour a phone has. Leave it
on for capacitive glass; on resistive touch, which wants a firm
press, it is less natural and turning it off can feel more
controlled.

---

Every widget of the family: [Containers](/docs/visualisation/widgets-containers/) · every widget: [Property reference](/docs/visualisation/widgets/)
