---
title: "Cameras"
slug: cameras
section: "Vision"
order: 212
sidebar_position: 212
generator: tools/docs_export.py
---

# Cameras

A Linux device can show a **live camera picture** on its own screen
(HMIview) and in the browser (WEBview). Plug a USB camera into the
device, add it to the project, drop a **camera** element on a screen -
that is all. Nothing is programmed.

!!! note "64-bit Linux devices only"
    Cameras belong to the Linux runtime on a processor that is up to
    them: a **64-bit** device - the reTerminal, a Raspberry Pi 4 / 5, a
    CM4 / CM5, a PC-class device. The STM32MP1 device (a pair of 32-bit
    cores) is too slow for vision and its runtime has none. The Toolbox
    offers the camera element only when the project's target is such a
    device, and a project for another board that carries one is refused
    at build.

## Which cameras

Any **USB video class** camera - the ordinary USB camera that needs no
driver on a PC works on the device too. A camera that delivers
**MJPG** (almost every one does) is the best choice: the device passes
the camera's own pictures through without decoding them, so a camera
costs the device almost nothing.

A project carries up to **four** cameras.

**IP cameras** work too: type the address of the camera's MJPEG stream
(`http://192.168.1.50/stream.mjpg` - most network cameras offer one) in
the camera's page. The device reads the stream itself; the stream
decides the picture size and the rate. Only plain `http://` - the
device does not do TLS.

## Adding a camera

The camera is a device of the Linux target, and it has its own node in
the tree: **Cameras**, right under the device.

![The Cameras node under a Linux device, with one camera](img/camera-tree.webp){: .sb-center}

1. **Scan the device** on its board page - the scan lists the cameras plugged into it, by name.
2. Right-click **Cameras** → **Add camera** and pick one of them (one entry per camera the scan found; without a scan, the first camera `/dev/video0`). The new camera is named `cam1`, `cam2` ..., at 1280x720, 15 pictures a second, MJPG, and its page opens. A project holds up to four cameras; the entries grey out at the fourth.
3. Click the camera to open its page; right-click it → **Remove camera** removes it (a screen element or a vision block that named it says so at build).

![The camera's page: name, camera, resolution, frames per second, stream](img/camera-page.webp){: .sb-center}

| Field | What it does |
|:---|:---|
| the camera list | which of the project's cameras the page shows and edits |
| **Name** | how the screens and the vision programs name the camera - 1 to 32 characters, no space (Enter applies) |
| **Camera** | which camera of the device: the ones a scan of the device reported, by name, then `/dev/video0` .. `/dev/video3` |
| **IP camera** | the address of a network camera's stream instead of a USB camera - `http://...` for an MJPEG stream, `rtsp://user:password@...` for H.264 / H.265; it replaces the device and sets the stream to MJPG (Enter applies, or leaving the field) |
| **Resolution** | the picture size, from the list the common cameras offer (640x480, 1280x720, 1600x1200, 1920x1080, 2560x1440) |
| **width x height** | any other size, 160..4096 by 120..4096 - a UVC camera answers with the nearest mode it has |
| **Frames per second** | how many pictures a second the camera delivers, 1..60 |
| **Stream** | **MJPG** (recommended - the device passes the camera's own JPEG through untouched, the lightest load) or **YUYV**, for a camera that has no MJPG |

Every field of the page is the same width, so the labels read in one column.

**An RTSP camera.** Most network cameras stream H.264 over RTSP
(`rtsp://user:password@192.168.1.50/stream1` - the path is the
camera's, see its manual). Type the address as the device; the stream
decides the size and the rate. The device decodes it with the FFmpeg
libraries of its operating system, which are not installed with the
runtime - run `sudo apt install ffmpeg` on the device once. Without
them the camera says so on the device's console and every other camera
of the project runs on. An MJPEG stream over http needs nothing.

**Exposure and colour** - the section under the stream, for a USB camera (an IP camera brings its own):

| Control | What it does |
|:---|:---|
| **Fixed exposure** | ticked: the exposure is typed (1..100000 in the camera's units - 100 µs steps on most USB cameras; 150 to start) and the camera's automatic exposure is off; unticked: the camera decides |
| **Fixed gain** | ticked: the gain is typed (0..255); unticked: the camera decides |
| **Fixed white balance** | ticked: the colour temperature is typed (1000..20000 K, 4600 to start); unticked: the camera decides |

A check wants the same picture every time, and a camera's automatics give a different one each run - a part that was *present* at one exposure is gone at the next. Fix the three for a check; leave them off for a live picture that only people look at. The device sets the camera when it opens it and says on its console what the camera took; a USB camera keeps a setting until it is unplugged, so the device puts the camera back on its automatics when a project asks for them - a check project that ran before does not leave its exposure behind.

**Take a picture** fetches one picture from the device and shows it on
the page - the quickest check that the camera is plugged in, pointed
the right way and in focus. It needs the device's address: go online,
or enter the address for the network upload.

A camera's first pictures after it opens come before its automatic
exposure has settled - they are too bright or too dark. **Take a
picture** (here and on the Vision page) waits until the brightness
stops moving before it keeps one, so the picture is the one the camera
gives in steady running. When pictures still differ from run to run,
fix the exposure, the gain and the white balance above; when they are
all dark, light the scene - a lamp helps a camera more than any
setting.

## The camera on a screen

The **camera** element is in the Toolbox. Draw it on a screen and set
its text to the camera's name; the picture fills the element with its
proportions kept. In the editor the element shows the camera's name,
on the device it shows the camera.

![A camera element on a screen in the editor](img/camera-screen.webp){: .sb-center}

The same screen in the **browser** shows the same picture, about ten
times a second - the WEBview draws the screens of the device's glass,
the camera included.

The device also serves the camera to anything else on the network:

| Address | What it answers |
|:---|:---|
| `http://<device>:8080/cam/0.jpg` | the latest picture of the project's first camera |
| `http://<device>:8080/cam/0.mjpg` | the live stream (MJPEG), at most two viewers per camera |

The number is the camera's position in the project: 0 is the first.

### The picture after the filters

The same element can show what a **vision block** makes instead of a
camera: write the block as `program.block` in its text (the program's
name, a dot, the block's id — `codes.shp`), and the element shows that
block's picture, live, on the glass and in the browser. Put it beside
the camera and the operator sees the raw picture and the one the
readers get side by side while turning the settings — a filter that
is too strong shows itself at once. Naming a detector block (a
learned model) shows its picture with every object framed and its
score - what the model saw, not the raw camera.

## The control comes first

The camera runs **below the PLC**: its pictures are taken on their own
threads, off the core the cycle and the EtherCAT line use. When the
device is busy, a picture is dropped - the cycle never waits for a
camera.

## Looking and deciding

A camera can also **check**: is the part there, is it the right colour,
where is its edge, what does its code say - the answers become
variables. See [Vision](/docs/vision/).

One camera serves everything at once: the camera elements of the
screens, the browser, the addresses above and every vision program
that names it - several programs on one camera, each with its own
trigger or period, is the usual way to ask it several questions.

## What comes next

Stereo cameras and the Raspberry Pi camera port.
