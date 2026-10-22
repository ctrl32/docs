---
title: "Images and icons: anim_image"
slug: w-anim_image
section: "Visualisation"
order: 65
sidebar_position: 65
image: img/wl-anim_image.webp
image_alt: "The anim_image widget on a screen"
generator: tools/docs_export.py
---

# anim_image

**Images and icons** · in a project file: `type: anim_image`

A picture made of frames, cycling on its own or picked by a variable.

![The anim_image widget on a screen](img/wl-anim_image.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | - | picks the frame by its value |
| `frames` | list | - | the pictures, in order |
| `period_ms` | integer | `500` | how long each frame shows, ms |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A picture made of frames — images of the project. It works two ways:

- **without a variable** it shows the frames one after another, each
  for `period_ms` — a turning fan, a blinking warning;
- **with a variable** the value picks the frame (0 = the first): a
  motor drawn stopped, running or faulted, one picture per state.

In the picture the frames are two drawings of the same fan turned by
45°, with no variable — so it turns. To turn it only while a drive
runs, give it `visible_if` with the drive's *running* variable and lay
a still image of the fan under it.

```yaml
- { type: anim_image, rect: [1090, 210, 96, 96], frames: [fan0, fan1], period_ms: 250 }
```

---

Every widget of the family: [Images and icons](/docs/visualisation/widgets-graphics/) · every widget: [Property reference](/docs/visualisation/widgets/)
