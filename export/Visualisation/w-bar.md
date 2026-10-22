---
title: "Indicators: bar"
slug: w-bar
section: "Visualisation"
order: 55
sidebar_position: 55
image: img/gallery-indicators.webp
image_alt: "The bar widget on a screen"
generator: tools/docs_export.py
---

# bar

**Indicators** · in a project file: `type: bar`

A proportion at a glance: where a value sits in its range.

![The bar widget on a screen](img/gallery-indicators.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | required | the value |
| `min` | number | `0.0` | the bottom of the range it spans |
| `max` | number | `100.0` | the top of the range it spans |
| `orientation` | one of `vertical` / `horizontal` | - | which way it fills: vertical or horizontal |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A proportion, at a glance. Tank level, load, progress, how far through
a delay.

The strength of a bar is that it shows **where the value sits in its
range** without anybody doing arithmetic. "Forty-two" means nothing on
its own; a bar four-tenths full means something immediately.

**Vertical bars read as level; horizontal ones read as progress.** It
is a small thing and it is worth following, because people bring the
expectation with them.

When the position matters more than the fill, a `scale` is what a bar
is missing.

!!! tip "Set min and max to what matters, not to what is possible"
    A pressure sensor may read 0–16 bar while the interesting range is
    4–6. A bar spanning the full sensor range is a bar that never
    moves. Span the range you care about and let it clip.

---

Every widget of the family: [Indicators](/docs/visualisation/widgets-indicators/) · every widget: [Property reference](/docs/visualisation/widgets/)
