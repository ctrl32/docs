---
title: "Containers: panel"
slug: w-panel
section: "Visualisation"
order: 29
sidebar_position: 29
image: img/gallery-cards.webp
image_alt: "The panel widget on a screen"
generator: tools/docs_export.py
---

# panel

**Containers** · in a project file: `type: panel`

A rectangle that groups other widgets, as a unit and as a visual card.

![The panel widget on a screen](img/gallery-cards.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `radius` | integer | `0` | corner rounding |
| `opacity` | integer | `0` | 1 to 99 makes the card translucent, the picture under it shows through; 0 or 100 is the solid card |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A rectangle with children inside it. Children are positioned
**relative to the panel**, so moving the panel moves the group, and a
panel that is hidden hides everything in it.

That last part is the useful bit: one `visible_if` on a panel hides
an entire section of a screen — a manual-control block that only
appears in manual mode, a set of settings that only makes sense for
one recipe.

**Use panels as visual grouping too.** A card around related values,
with a heading label at the top, does more for readability than any
amount of careful spacing.

**Behind glass.** With `opacity` the card is translucent and the
picture under it shows through — an energy flow looks best over a
picture of the house, on a translucent panel.

With a [state](/docs/visualisation/states-motion/) painting `bg`, a panel becomes a
strip that tints with RUN.

!!! tip "Rounded corners have a cost"
    Anti-aliased rounding is computed, not copied. On a screen with a
    few cards it is invisible; on one with thirty small rounded panels
    it is felt. Round the containers, not every element inside them.

---

Every widget of the family: [Containers](/docs/visualisation/widgets-containers/) · every widget: [Property reference](/docs/visualisation/widgets/)
