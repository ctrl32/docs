---
title: "Trends and alarms: trace"
slug: w-trace
section: "Visualisation"
order: 70
sidebar_position: 70
image: img/gallery-trend.webp
image_alt: "The trace widget on a screen"
generator: tools/docs_export.py
---

# trace

**Trends and alarms** · in a project file: `type: trace`

One line in a trend, following one variable.

![The trace widget on a screen](img/gallery-trend.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | required | what this line follows |
| `color` | colour | - | how it is drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

One line in a trend. Traces are children of the trend widget — you do
not place them on the screen yourself.

**Give traces colours that survive being printed and photographed.**
Somebody will screenshot the board and send it to you, and two similar
blues become one blue in the process.

---

Every widget of the family: [Trends and alarms](/docs/visualisation/widgets-data/) · every widget: [Property reference](/docs/visualisation/widgets/)
