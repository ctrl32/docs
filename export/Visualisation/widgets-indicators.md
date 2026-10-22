---
title: "Indicators"
slug: widgets-indicators
section: "Visualisation"
order: 24
sidebar_position: 24
generator: tools/docs_export.py
---

# Indicators

The widgets that show a value without letting anyone change it: a lamp,
a bar and a gauge, and beside them a table, a scale, a spinner and a QR
code.

They are what somebody reads from across the room, so the question with
each is not "does it show the value" but "can it be understood in half a
second, by somebody who is not looking carefully".

---

![The indicators: an LED top right, a bar under the value, a gauge with its needle on the flow](img/gallery-indicators.webp){: .sb-center}

## The widgets

<!-- w-index: begin -->

| Widget | What it is |
|:---|:---|
| [led](/docs/visualisation/w-led/) | A lamp: one variable, two colours, immediately readable. |
| [bar](/docs/visualisation/w-bar/) | A proportion at a glance: where a value sits in its range. |
| [gauge](/docs/visualisation/w-gauge/) | A dial whose needle position is recognised without reading the number. |
| [table](/docs/visualisation/w-table/) | Rows of cells, a row with a variable showing its live value as the last cell. |
| [scale](/docs/visualisation/w-scale/) | A straight scale with numbered ticks and a pointer at the value. |
| [spinner](/docs/visualisation/w-spinner/) | A turning arc that says wait or busy. |
| [qrcode](/docs/visualisation/w-qrcode/) | A QR code of a text - typically the board's own address. |

<!-- w-index: end -->

## Choosing between them

| The question is | Use |
|:---|:---:|
| is it on? | **led** |
| how full, how far, how much of the way | **bar** |
| what is the value, roughly, at a glance | **gauge** |
| what is the value, exactly | a [`value`](/docs/visualisation/widgets-text/) widget |

And the honest answer is often the last one. A number in a large font is
the fastest thing to read on any screen — gauges and bars earn their
place when the *position within a range* matters more than the digits.

---

## What makes indicators expensive

An indicator redraws when its variable changes. An analog variable
without a deadband changes on every flicker of its last digit, so a
gauge bound to one repaints continuously and never sits still.

Set a deadband on the variable, not on the widget. Everything reading it
gets quieter at once — the board, the trend, the browser. See
[Variables](/docs/editor-overview/variables/).
