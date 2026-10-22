---
title: "Charts"
slug: widgets-charts
section: "Visualisation"
order: 27
sidebar_position: 27
generator: tools/docs_export.py
---

# Charts

Five widgets that turn numbers into a picture: an energy flow, columns, a
ring, a small curve and a cloud of points.

A [trend](/docs/visualisation/w-trend/) answers *what happened over time*. These
answer the questions a dashboard asks: *where is the energy going*, *which
room is warmest*, *how full is the battery*, *does one value follow
another*.

---

![The four charts of a home energy screen: the flow, columns, rings and small curves](img/wl-energy_flow.webp){: .sb-center}

## The widgets

<!-- w-index: begin -->

| Widget | What it is |
|:---|:---|
| [energy_flow](/docs/visualisation/w-energy_flow/) | Circles joined by lines along which dots run in the direction the energy flows. |
| [bar_chart](/docs/visualisation/w-bar_chart/) | Columns - one per variable, or the history of one variable. |
| [donut](/docs/visualisation/w-donut/) | A ring - one value filling it, or slices in the ratio of several variables. |
| [sparkline](/docs/visualisation/w-sparkline/) | A small curve of one variable's recent past, to sit beside the number. |
| [chart_item](/docs/visualisation/w-chart_item/) | One part of a chart - a node, a link, a column, a slice - written by the build. |
| [scatter](/docs/visualisation/w-scatter/) | Points of recent pairs of values, one against the other. |

<!-- w-index: end -->

## What a chart costs

The sparkline, the bar chart's history and the scatter keep their past
in the same recorder as the trends: every variable they draw is one of
the recorded variables a project may have (see [Limits](/docs/operation/limits/)). The
energy flow, the columns of variables and the rings draw the present only
and cost nothing beyond the widget.
