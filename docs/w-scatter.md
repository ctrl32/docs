---
image: img/wl-scatter.webp
image_alt: "The scatter widget on a screen"
---

# scatter

**Charts** · in a project file: `type: scatter`

Points of recent pairs of values, one against the other.

![The scatter widget on a screen](img/wl-scatter.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | required | x - along the bottom |
| `series` | list | - | y - one cloud per variable |
| `x_min` | number | `0.0` | the x axis bottom |
| `x_max` | number | `100.0` | the x axis top |
| `min` | number | `0.0` | the y axis bottom |
| `max` | number | `100.0` | the y axis top |
| `sample_ms` | integer | `1000` | one pair every, ms |
| `points` | integer | `60` | how many recent pairs it keeps |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](states-motion.md) - see the [Property reference](widgets.md).

## Description

Points of recent pairs: x is the widget's variable, y each series'
variable, sampled **together** every `sample_ms`. Where a trend shows
two values against time, a scatter shows them against each other — and
a relationship nobody would see in two curves stands out as the shape
of the cloud.

In the picture the house power is drawn against the outdoor
temperature: the colder it is, the more the house takes. A pump's flow
against its speed, a motor's current against its load and a press's
force against its stroke are the same picture.

```yaml
- type: scatter
  rect: [456, 396, 368, 296]
  tag: out_temp
  x_min: -10
  x_max: 30
  min: 0
  max: 10
  sample_ms: 5000
  points: 120
  series:
    - { tag: house_power, color: 0xFD84, label: "House power" }
```

It keeps its past in the same recorder as the trends: every variable
it draws is one of the recorded variables a project may have (see
[Limits](limits.md)).

---

Every widget of the family: [Charts](widgets-charts.md) · every widget: [Property reference](widgets.md)
