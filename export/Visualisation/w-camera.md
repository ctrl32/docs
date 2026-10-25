---
title: "Images and icons: camera"
slug: w-camera
section: "Visualisation"
order: 64
sidebar_position: 64
image: img/camera-screen.webp
image_alt: "The camera widget on a screen"
generator: tools/docs_export.py
---

# camera

**Images and icons** · in a project file: `type: camera`

The live picture of one of the project's cameras, or of a vision block - 64-bit Linux devices, and the ESP32-P4 panel for an http:// camera.

![The camera widget on a screen](img/camera-screen.webp){: .sb-center}

**Needs:** a camera of the project, on the 64-bit Linux runtime.

## Properties

The widget has no property of its own beyond the ones every widget has.

- `text`: the camera's name, or program.block for a vision block's picture

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

The **camera** element is in the Toolbox. Draw it on a screen and set
its text to the camera's name; the picture fills the element with its
proportions kept. In the editor the element shows the camera's name,
on the device it shows the camera. Nothing is programmed: plug a USB
camera into the device, add it to the project (the **Cameras** node
under the device, see [Cameras](/docs/vision/cameras/)), drop the element on a
screen.

On an **ESP32-P4 panel** the element shows an IP camera - an
`http://` MJPEG stream, a network camera or an ESP32-S3 camera device
(see [Intercom](/docs/vision/intercom/)): the panel's JPEG hardware decodes the
stream, up to two on a panel. A USB camera and the vision blocks stay
with the Linux devices.

The same screen in the **browser** shows the same picture, about ten
times a second — the WEBview draws the screens of the device's glass,
the camera included.

**The picture after the filters.** The same element can show what a
**vision block** makes instead of a camera: write the block as
`program.block` in its text (the program's name, a dot, the block's id
— `codes.shp`), and the element shows that block's picture, live, on
the glass and in the browser. Put it beside the camera and the
operator sees the raw picture and the one the readers get side by side
while turning the settings — a filter that is too strong shows itself
at once. Naming a detector block (a learned model) shows its picture
with every object framed and its score — what the model saw, not the
raw camera. See [Vision](/docs/vision/).

!!! note "64-bit Linux devices only"
    Cameras belong to the Linux runtime on a **64-bit** device — the
    reTerminal, a Raspberry Pi 4 / 5, a CM4 / CM5, a PC-class device.
    The STM32MP1 device is too slow for vision and its runtime has
    none. The Toolbox offers the camera element only when the
    project's target is such a device, and a project for another board
    that carries one is refused at build. A camera that is removed
    while a screen element names it is reported at build.

The camera runs **below the PLC**: its pictures are taken on their own
threads, off the core the cycle uses; when the device is busy a
picture is dropped — the cycle never waits for a camera.

---

Every widget of the family: [Images and icons](/docs/visualisation/widgets-graphics/) · every widget: [Property reference](/docs/visualisation/widgets/)
