---
title: "Charts: bar_chart"
slug: w-bar_chart
section: "Visualisation"
order: 72
sidebar_position: 72
image: img/wl-bar_chart.webp
image_alt: "The bar_chart widget on a screen"
generator: tools/docs_export.py
---

# bar_chart

**Charts** · in a project file: `type: bar_chart`

Columns - one per variable, or the history of one variable.

![The bar_chart widget on a screen](img/wl-bar_chart.webp){: .sb-center}

![The bar_chart widget on a screen](img/wl-bar_history.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | - | the variable of a history chart |
| `series` | list | - | one column per variable |
| `history` | yes / no | no | columns of the variable's past |
| `sample_ms` | integer | `3600000` | one column of the history, ms |
| `bars` | integer | `24` | how many columns of history |
| `min` | number | `0.0` | the bottom of the scale |
| `max` | number | `100.0` | the top of the scale |
| `show_value` | yes / no | yes | the value over each column |
| `font` | font | - | how values and labels are drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

Columns, in one of two ways:

- **one column per variable** of `series` — the rooms' temperatures,
  the three phases, the consumers of a house — each in its colour with
  its label under it;
- **the history of one variable** with `history: true` — one column
  per `sample_ms`, the last `bars` of them: every hour's energy of the
  day.

```yaml
- type: bar_chart
  rect: [630, 20, 380, 170]
  min: 0
  max: 30
  series:
    - { tag: room1, color: "#FF9F43", label: "Living" }
    - { tag: room2, color: "#4EA8DE", label: "Bedroom" }
- { type: bar_chart, rect: [630, 210, 380, 120], tag: pv, history: true, sample_ms: 3600000, bars: 24, min: 0, max: 8 }
```

The history form keeps its past in the same recorder as the trends:
its variable is one of the recorded variables a project may have (see
[Limits](/docs/operation/limits/)). The columns of variables draw the present only
and cost nothing beyond the widget.

---

Every widget of the family: [Charts](/docs/visualisation/widgets-charts/) · every widget: [Property reference](/docs/visualisation/widgets/)
