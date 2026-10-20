---
image: img/wl-tileview.webp
image_alt: "The tileview widget on a screen"
---

# tileview

**Containers** · in a project file: `type: tileview`

Pages switched by a swipe to the left or right, with a dot for each page.

![The tileview widget on a screen](img/wl-tileview.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | - | the number of the page shown |
| `active` | integer | `0` | the page shown first, without a variable |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](states-motion.md) - see the [Property reference](widgets.md).

## Description

Pages — its children — switched by a **swipe** to the left or right,
with a dot for each page underneath. On a phone this is the most
natural way through a handful of similar pages: one zone per page,
one pump per page.

With a variable, the variable **is** the page number: a swipe writes
it, and the logic or another widget can turn the page — a fault on
pump 3 can bring pump 3's page forward on its own.

Every child is one page, laid out in the tileview's own frame. Make
each page a `panel` and put the page's widgets inside it:

```yaml
- type: tileview
  rect: [872, 396, 368, 140]
  tag: page
  children:
    - type: panel
      rect: [0, 0, 368, 140]
      children:
        - { type: value, rect: [16, 50, 300, 60], tag: temp_a }
    - type: panel
      rect: [0, 0, 368, 140]
      children:
        - { type: value, rect: [16, 50, 300, 60], tag: temp_b }
```

With a knob, a press on a tileview enters edit and a turn changes the
page.

---

Every widget of the family: [Containers](widgets-containers.md) · every widget: [Property reference](widgets.md)
