---
title: "Containers: popup"
slug: w-popup
section: "Visualisation"
order: 32
sidebar_position: 32
generator: tools/docs_export.py
---

# popup

**Containers** · in a project file: `type: popup`

A modal window over the screen that keeps touch from what is underneath.

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `radius` | integer | `8` | corner rounding |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A modal window over the screen. While it is visible, **touch does not
reach what is underneath** — which is the whole point: a question that
can be ignored by pressing something else is not a question.

Popups are hidden by default and shown by binding `visible_if` to a
variable the logic sets.

**Use one for:** a confirmation the logic itself raises, a fault that
must be seen before anything else, a value that has to be entered
before a sequence can start.

A popup belongs to a moment — a question, a confirmation — and covers
the screen; a `window` is part of the screen.

!!! warning "A popup that appears while somebody is pressing something"
    If the logic can raise a popup at any moment, it can raise one
    under a finger that is already moving — and the press lands on
    the popup instead of the button. For anything raised
    automatically, make the dismiss button somewhere a finger is
    unlikely to already be.

---

Every widget of the family: [Containers](/docs/visualisation/widgets-containers/) · every widget: [Property reference](/docs/visualisation/widgets/)
