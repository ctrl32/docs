---
title: "Charts: chart_item"
slug: w-chart_item
section: "Visualisation"
order: 75
sidebar_position: 75
generator: tools/docs_export.py
---

# chart_item

**Charts** · in a project file: `type: chart_item`

One part of a chart - a node, a link, a column, a slice - written by the build.

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | - |  |
| `color` | colour | - |  |
| `label` | text | - |  |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

One part of a chart (a node, a link, a column, a slice) — written by
the build from the chart's own lists (`nodes`, `links`, `series`),
never by hand. To change one, edit the list of the chart it belongs
to.

---

Every widget of the family: [Charts](/docs/visualisation/widgets-charts/) · every widget: [Property reference](/docs/visualisation/widgets/)
