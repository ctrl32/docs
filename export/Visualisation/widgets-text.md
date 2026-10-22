---
title: "Text and values"
slug: widgets-text
section: "Visualisation"
order: 22
sidebar_position: 22
generator: tools/docs_export.py
---

# Text and values

Four widgets: one draws fixed text, one a number that changes, one a
paragraph that wraps and one a sentence of mixed colours and live values.

Between them they carry most of what a screen actually says, and the
number widget is the fastest thing on any screen to read — worth
remembering before reaching for a gauge.

---

![Labels above, the value widget with unit and decimals below](img/gallery-value.webp){: .sb-center}

## The widgets

<!-- w-index: begin -->

| Widget | What it is |
|:---|:---|
| [label](/docs/visualisation/w-label/) | Fixed text: a heading, a unit, a name beside a lamp, an instruction. |
| [value](/docs/visualisation/w-value/) | A live number, with the decimals and the unit of its variable. |
| [textarea](/docs/visualisation/w-textarea/) | Text over several lines, wrapped at the widget's width. |
| [rich_text](/docs/visualisation/w-rich_text/) | One paragraph of spans, each with its own colour and font, mixing words with live values. |

<!-- w-index: end -->

## Where the decimals come from

Both widgets draw what the variable says. A variable with two decimals
and unit `bar` shows `4.25 bar` on the board, in the browser and in a
trend legend — no per-widget formatting, no disagreement between two
screens showing the same thing.

The corollary: if a value shows too many digits, fix the **variable**.
`show_unit` exists for the case where the unit is already in a label
beside it and repeating it would be noise.

---

## Deadband, again

A number without a deadband on its variable repaints on every flicker of
the last digit — and a value that will not sit still is harder to read
than one that updates twice a second.

Deadband is a property of the variable, so setting it quiets the screen,
the browser and the trend at once. See [Variables](/docs/editor-overview/variables/).
