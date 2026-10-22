---
title: "Controls: calendar"
slug: w-calendar
section: "Visualisation"
order: 52
sidebar_position: 52
image: img/wl-calendar.webp
image_alt: "The calendar widget on a screen"
generator: tools/docs_export.py
---

# calendar

**Controls** · in a project file: `type: calendar`

A month; the variable holds a date as one number YYYYMMDD.

![The calendar widget on a screen](img/wl-calendar.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | required | the date as a number YYYYMMDD (a DINT) |
| `font` | font | - | how the days are drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A month. The variable holds a date written as one number, `20261016`;
its day is drawn in the accent, a tap on another day writes that day,
and the arrows in the header page through the months.

Give it a `DINT` variable. A program reads the date with plain
arithmetic — the year is `day / 10000`, the month `day / 100 MOD 100`
— and a holiday, a service date or the first day of a heating plan is
one comparison away.

With a knob, a press on a focused calendar enters edit and a turn
changes the value.

!!! note "Today's circle"
    The day ringed in the calendar is today's date from the board's
    clock, so a board with network time shows the real day.

---

Every widget of the family: [Controls](/docs/visualisation/widgets-controls/) · every widget: [Property reference](/docs/visualisation/widgets/)
