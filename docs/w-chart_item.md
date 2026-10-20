# chart_item

**Charts** · in a project file: `type: chart_item`

One part of a chart - a node, a link, a column, a slice - written by the build.

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | - |  |
| `color` | colour | - |  |
| `label` | text | - |  |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](states-motion.md) - see the [Property reference](widgets.md).

## Description

One part of a chart (a node, a link, a column, a slice) — written by
the build from the chart's own lists (`nodes`, `links`, `series`),
never by hand. To change one, edit the list of the chart it belongs
to.

---

Every widget of the family: [Charts](widgets-charts.md) · every widget: [Property reference](widgets.md)
