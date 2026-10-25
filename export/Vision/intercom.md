---
title: "Intercom"
slug: intercom
section: "Vision"
order: 213
sidebar_position: 213
generator: tools/docs_export.py
---

# Intercom

A door intercom is a small camera at the door and its live picture on
the wall panel - a bell lamp and a door button beside it. In ctrl32 the
camera is an **ESP32-S3 device** running the ordinary runtime with a
camera section in its project, and the picture is the **camera element**
on an **ESP32-P4 panel** (or a Linux device). Nothing is programmed on
either side; the bell and the door are variables of the system, shared
over net32 like any other.

## The camera device

A board with a camera sensor and PSRAM - the **Seeed XIAO ESP32S3
Sense** is the one in the catalog: an OV2640 on its expansion board, a
microphone, a microSD slot, native USB for the console and the runtime,
eleven free pins on the edge. Pick it as the project's board and add
**Camera** from the device's context menu in the tree. The page:

| Setting | Meaning |
|:---|:---|
| **Resolution** | 320x240, 640x480, 800x600, 1024x768 or 1280x720 |
| **Quality** | the JPEG quality the sensor compresses with, 1 (best) to 63 (smallest) - 12 is a good picture at 25 to 40 kB a frame |
| **Frame rate** | 1 to 25 frames a second - 10 is plenty for a door |
| **Flip**, **Mirror** | the picture turned for a sensor mounted upside down or seen from behind |

The pins come from the catalog board; the page shows them and nothing
has to be wired in the project. The device serves the picture on its own
web server: `http://<name>.local/cam.mjpg` is the stream, `/cam.jpg` the
latest frame - open either in a browser to see the camera before the
panel does.

## The picture on the panel

On the P4 panel's project, add the camera under **Cameras** (the
device's context menu) with the camera device's address as its source:

```
http://door-cam.local/cam.mjpg
```

Then draw a **camera** element on a screen and set its text to the
camera's name. The panel reads the stream, decodes every frame with its
JPEG hardware and scales it into the element with the proportions kept;
the browser of the panel's WEBview shows the same picture. A panel shows
up to two cameras; any network camera with an `http://` MJPEG stream
works the same way. A USB camera and the vision blocks remain the Linux
devices' - see [Cameras](/docs/vision/cameras/).

While the stream is not there (the camera device starting, the network
down) the element shows its border and the camera's name; the panel
tries again after 2 s, 4 s, up to every 30 s, and the diagnostic buffer
says once what stopped it. The INFO line carries
`camv=<live>/<cameras>,<frames>,<failures>`.

## The bell and the door

The camera device has free pins: a bell button on one of them is a
BOOL variable published over net32; the panel subscribes to it, lights a
lamp, opens the Door screen on its edge, and a button on that screen
writes the door variable the device with the relay owns. All of it is
the net32 and screen work described elsewhere; the house dashboard
example carries a Door screen built this way.

## Numbers to plan with

| | |
|:---|:---|
| 640x480 at 10 fps | 3 to 4 Mbit/s on the network |
| 1280x720 | 5 fps at most, a quarter of the panel's screen |
| Streams on one panel | two |
| Viewers of one camera device | two at a time (its own server's limit) |
| Delay door to panel | under a second: a frame's time and the network |

Sound is not part of the picture: the intercom shows and rings, it does
not talk.
