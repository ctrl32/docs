---
image: img/gallery-trend.webp
image_alt: "The trend widget on a screen"
---

# trend

**Trends and alarms** · in a project file: `type: trend`

A chart of how values have behaved, sampled in the board.

![The trend widget on a screen](img/gallery-trend.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `series` | list | - | the traces |
| `timespan_s` | integer | `300` | how much time is shown, seconds |
| `sample_ms` | integer | `1000` | how often a point is taken |
| `autoscale` | yes / no | yes | fit the vertical axis to the data |
| `min` | number | - | fixed axis bottom when autoscale is off |
| `max` | number | - | fixed axis top when autoscale is off |
| `grid` | yes / no | yes | draw gridlines |
| `show_legend` | yes / no | yes | name the traces |
| `scroll_mode` | yes / no | yes | scroll, rather than wrap around |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](states-motion.md) - see the [Property reference](widgets.md).

## Description

A chart of how values have behaved. Up to **four traces**, sampled in
the board — so the history exists whether or not anybody is watching.
Put the current values under the chart, where they can be read
without interpreting the lines.

**`timespan_s` and `sample_ms` together decide what you can see.**
Five minutes at one second per point is 300 points, which is about the
width of a panel screen — sensible. Five minutes at 10 ms per point is
30 000 points squeezed into a few hundred pixels, and everything short
is lost in the squeeze anyway.

**Autoscale is right for watching and wrong for comparing.** With it
on, a flat line fills the chart and looks dramatic; with a fixed
`min`/`max`, flat looks flat and two screens of the same variable can
be compared. Fix the axis for anything somebody will judge by eye.

The traces are its children (see `trace`). The sparkline, the bar
chart's history and the scatter keep their past in the same recorder
as the trends (see [Limits](limits.md)).

!!! tip "For anything short, use the Scope"
    A trend samples periodically. A pulse one cycle long falls between
    two samples by construction — and the fault you are chasing is
    usually exactly that. The [Scope](scope.md) records **every
    cycle** in the board and stops on a trigger. Trend for behaviour
    over minutes, scope for what happened in one.

---

Every widget of the family: [Trends and alarms](widgets-data.md) · every widget: [Property reference](widgets.md)
