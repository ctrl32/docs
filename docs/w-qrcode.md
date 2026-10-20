---
image: img/wl-qrcode.webp
image_alt: "The qrcode widget on a screen"
---

# qrcode

**Indicators** · in a project file: `type: qrcode`

A QR code of a text - typically the board's own address.

![The qrcode widget on a screen](img/wl-qrcode.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `text` | text | required | what the code carries |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](states-motion.md) - see the [Property reference](widgets.md).

## Description

A QR code of `text`, as large as the widget allows, drawn in fg on bg
— keep them dark on light, the way every phone camera expects.

The obvious use is the board's own address: a phone pointed at the
panel opens the same screens in its browser. A link to the manual, a
service form or the WiFi login of a guest network are the others.

```yaml
- { type: qrcode, rect: [872, 396, 150, 150], text: "http://192.168.0.172/" }
```

---

Every widget of the family: [Indicators](widgets-indicators.md) · every widget: [Property reference](widgets.md)
