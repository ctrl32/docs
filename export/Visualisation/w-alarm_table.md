---
title: "Trends and alarms: alarm_table"
slug: w-alarm_table
section: "Visualisation"
order: 69
sidebar_position: 69
image: img/gallery-alarms.webp
image_alt: "The alarm_table widget on a screen"
generator: tools/docs_export.py
---

# alarm_table

**Trends and alarms** · in a project file: `type: alarm_table`

The list of what is wrong, and what was.

![The alarm_table widget on a screen](img/gallery-alarms.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `filter` | one of `active` / `unacked` / `history` / `all` | - | which alarms to show: active, unacked, history or all |
| `min_priority` | one of `info` / `warning` / `fault` / `critical` | - | the lowest priority shown |
| `rows` | integer | `8` | how many fit |
| `show_time` | yes / no | yes | when it happened |
| `show_ack_button` | yes / no | yes | let the reader acknowledge |
| `sort` | one of `newest_first` / `priority` | `newest_first` | ordering: newest_first or priority |
| `font` | font | - | text size |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

The list of what is wrong, and what was.

**`filter` decides what the table is for**, and it is worth having more
than one:

- **`active`** — what is wrong *now*. The screen somebody looks at when
  something has stopped.
- **`unacked`** — what has not been seen yet, including things that
  have already cleared. This is the one that catches the intermittent
  fault nobody was standing there for.
- **`history`** — what happened, in order. The answer to "it did
  something odd this morning".

**`sort` by priority when the table is short.** With eight rows and a
busy alarm situation, newest-first can push the critical one off the
bottom while a stream of information messages fills the view.

A lamp with `alarm_ref:` reads the same alarm definition as the table
and goes red exactly when the table says so (see
[States and motion](/docs/visualisation/states-motion/)). A value's `warn_above` gives
the soft warning stage, the alarm the hard action stage.

!!! tip "Timestamps are only as good as the clock"
    An alarm history with no time is a list of things that happened in
    an unknown order. Make sure the board's clock is set — from the
    network, from an RTC, or from the browser — **before**
    commissioning, not after. Otherwise the first day's history is
    stamped in 1970.

---

Every widget of the family: [Trends and alarms](/docs/visualisation/widgets-data/) · every widget: [Property reference](/docs/visualisation/widgets/)
