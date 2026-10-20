---
image: img/wl-rich_text.webp
image_alt: "The rich_text widget on a screen"
---

# rich_text

**Text and values** · in a project file: `type: rich_text`

One paragraph of spans, each with its own colour and font, mixing words with live values.

![The rich_text widget on a screen](img/wl-rich_text.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `spans` | list | - | the pieces of the paragraph: text, tag, color, font |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](states-motion.md) - see the [Property reference](widgets.md).

## Description

One paragraph made of **spans**, each with its own colour and font —
a word in red, a value in a large face — flowing on and wrapping at
the widget's width. A span with a variable shows its live value with
the unit.

| Span key | Meaning |
|:---|:---|
| `text` | the span's words |
| `tag` | a variable whose value follows the words |
| `color` | its colour |
| `font` | its font |

The spans join exactly as written: put the space between two spans
where you want one. A value in the large numeric face carries its
unit in the medium face beside it, the way the `value` widget sets
it.

```yaml
- type: rich_text
  rect: [872, 566, 368, 124]
  spans:
    - { text: "Zone A is ", color: 0xF7BF, font: 1 }
    - { text: "", tag: temp_a, color: 0xFD84, font: 2 }
    - { text: " and the house takes ", color: 0x8CB5, font: 1 }
    - { text: "", tag: house_power, color: 0x055E, font: 2 }
```

---

Every widget of the family: [Text and values](widgets-text.md) · every widget: [Property reference](widgets.md)
