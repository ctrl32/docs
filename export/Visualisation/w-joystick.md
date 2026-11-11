---
title: "Controls: joystick"
slug: w-joystick
section: "Visualisation"
order: 54
sidebar_position: 54
image: img/wl-joystick.webp
image_alt: "The joystick widget on a screen"
generator: tools/docs_export.py
---

# joystick

**Controls** · in a project file: `type: joystick`

A two-axis pad that writes two variables while a finger holds it - the robot's teleop pad.

![The joystick widget on a screen](img/wl-joystick.webp){: .sb-center}

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `axes` | list | - |  |
| `knob` | integer | `0` |  |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

A two-axis pad. A finger on it writes **two variables while it is
held** — the **forward** axis (up is positive) and the **turn** axis
(left is positive), each scaled to its *Full deflection* at the pad's
edge — and writes **both zero** the moment it lets go; on the glass and
in the browser alike. With a `geometry_msgs/Twist` published by fields
(`linear.x` from the forward variable, `angular.z` from the turn one)
it is the robot's teleop pad: the robot stops when the finger lifts.

The two axes are the element's rows on the Properties sheet: a variable
and the value at full deflection each. *Knob radius* sizes the knob, 0
= a quarter of the pad. A plain element — it works on every runtime,
not only beside ROS.

---

Every widget of the family: [Controls](/docs/visualisation/widgets-controls/) · every widget: [Property reference](/docs/visualisation/widgets/)
