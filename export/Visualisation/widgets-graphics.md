---
title: "Images and icons"
slug: widgets-graphics
section: "Visualisation"
order: 25
sidebar_position: 25
generator: tools/docs_export.py
---

# Images and icons

The widgets that draw pictures: an image, an icon and the ctrl32 mark, a
line, a shape and an animated image.

---

![The graphics family: an image, three tinted icons, corner radii and the font sizes](img/gallery-graphics.webp){: .sb-center}

## The widgets

<!-- w-index: begin -->

| Widget | What it is |
|:---|:---|
| [image](/docs/visualisation/w-image/) | A bitmap from the project's assets, for what only a picture can say. |
| [icon](/docs/visualisation/w-icon/) | A vector glyph, sharp at any size, that can switch glyph and colour with a variable. |
| [logo](/docs/visualisation/w-logo/) | The ctrl32 mark, drawn as vectors in one colour. |
| [camera](/docs/visualisation/w-camera/) | The live picture of one of the project's cameras, or of a vision block - 64-bit Linux devices, and the ESP32-P4 panel for an http:// camera. |
| [anim_image](/docs/visualisation/w-anim_image/) | A picture made of frames, cycling on its own or picked by a variable. |
| [line](/docs/visualisation/w-line/) | A line through points in the widget's own frame - a pipe, an arrow, an outline. |
| [shape](/docs/visualisation/w-shape/) | A rectangle or an ellipse that fills the widget. |

<!-- w-index: end -->

## Colour and tint

`color` on an icon and `tint` on an image both recolour what is drawn.
The practical use is **one asset, several meanings**: the same warning
triangle in amber for a warning and red for a fault, without a second
file.

Combined with [states](/docs/visualisation/widgets/), the colour can follow a variable —
so a single icon covers running, stopped and faulty from one definition.

---

## Turning and circling

![A propeller turning at the fan's speed, a marker riding a circle as the speed climbs](img/wl-rotate.webp){: .sb-center}

Any widget may carry a `rotate:` key; an icon, an image, a shape and a
line are drawn **turned** by it (a text is not — a bitmap face does not
turn). The picture turns clockwise about the centre of its rectangle.
Two forms:

| Form | Keys | Meaning |
|:---|:---|:---|
| an angle from a value | `var`, `min`, `max`, `from`, `to` | the angle runs from `from` to `to` degrees as the variable sweeps `min`..`max` — a damper, a pointer, a compass |
| turning at a speed | `speed`, `gain` — or `rpm` alone | the picture turns at `speed` × `gain` revolutions per minute (a drive's Hz or % become rpm); `rpm` alone is a decoration that always turns |

```yaml
# a damper's blade: 0..100 % = 0..90 degrees
- { type: icon, icon: line, rect: [40, 40, 80, 80], rotate: { var: damper, min: 0, max: 100, from: 0, to: 90 } }
# a propeller at the fan's speed (the variable is in rpm)
- { type: icon, icon: propeller, rect: [70, 50, 100, 100], rotate: { speed: fan_rpm, gain: 1 } }
```

A turning picture may show its corners outside the rectangle — when the
picture fills its rectangle, leave the rectangle about 1.4× the picture.
An ellipse keeps its axes (a circle looks the same from every angle); a
rectangle turns.

**Motion on a circle.** The `move:` key, which walks a widget along a
straight path, also takes a circle: `center`, `radius`, and the angle
from `from_deg` to `to_deg` (0 at twelve o'clock, clockwise) as the
variable sweeps its range. The widget's **centre** rides the arc — the
icons around a dial, a marker on a round gauge:

```yaml
- { type: icon, icon: point, rect: [108, 8, 24, 24],
    move: { var: fan_rpm, min: 0, max: 1200, center: [120, 100], radius: 80, from_deg: -120, to_deg: 120 } }
```

Give the same variable to `rotate:` and the picture turns as it travels.
The browser draws both exactly as the glass does.

!!! warning "A #RRGGBB colour used to come out black"
    If you have an older project where an icon renders in the style
    colour rather than the one you chose, this is why: the web-style
    `"#F5A623"` spelling was not parsed and silently yielded black. Both
    spellings work now. Re-check any colour that never looked right.
