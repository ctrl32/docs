---
title: "Images and icons: image"
slug: w-image
section: "Visualisation"
order: 61
sidebar_position: 61
image: img/gallery-graphics.webp
image_alt: "The image widget on a screen"
generator: tools/docs_export.py
---

# image

**Images and icons** · in a project file: `type: image`

A bitmap from the project's assets, for what only a picture can say.

![The image widget on a screen](img/gallery-graphics.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `src` | image_ref | required | which picture |
| `tint` | colour | - | recolour it |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A bitmap from the project's assets: a logo, a photograph, a diagram of
the thing being controlled.

**An image is a picture, and pictures are large.** It is baked into
the project file at the size it is shown, so a full-screen photograph
is a serious part of the upload and of the board's flash. Check what
it costs before deciding a screen needs one.

Use images for what only a picture can say — a diagram with the
sensors marked on it, a photograph of the part being handled. For
symbols, an `icon` is smaller, sharper and recolourable.

`tint` recolours the picture — one asset, several meanings. An image
can be turned by `rotate:`. The project's images are also what the
boot splash on the HMIview page shows (see [HMIview](/docs/visualisation/hmiview/)).

!!! tip "A layout diagram beats a paragraph"
    One drawing of the equipment with the lamps placed where the real
    sensors are tells somebody more in a second than a table of names
    does in a minute — especially somebody who has never seen it
    before.

---

Every widget of the family: [Images and icons](/docs/visualisation/widgets-graphics/) · every widget: [Property reference](/docs/visualisation/widgets/)
