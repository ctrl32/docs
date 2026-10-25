---
title: "Setup screens and Quick setup"
slug: drives-setup
section: "Drive library"
order: 319
sidebar_position: 319
image: img/drv-motor.webp
image_alt: "The Motor setup screen of a drive"
generator: tools/docs_export.py
---

# Setup screens and Quick setup

Every vendor numbers its parameters differently, but every drive needs
the same few settings: the motor's nameplate, the ramps, where the start
command and the speed come from, what the terminals do. The setup screens
show those settings as **drawn fields, the same for every vendor** - each
field writes the parameter its series assigns to it, so nobody has to
hunt for it in a list of a thousand parameters. The small text under a
field names that parameter.

A field the series does not have is not shown; the values, units and
names in a field are the maker's own, nothing is converted.

## The screens

| Screen | What it holds |
|:---|:---|
| **Motor** | the nameplate (power, voltage, current, frequency, speed, power factor, poles, connection), the control mode, the switching frequency, the boost, the motor identification, the motor's temperature sensor and overload protection |
| **Ramps & limits** | acceleration, deceleration, S-ramp and quick-stop times, minimum and maximum frequency, current and torque limits, the stop mode and the brake chopper |
| **Control** | where the start command and the setpoint come from, reversing, the fixed speeds, the fieldbus address and timeout, the automatic restart |
| **Inputs & outputs** | the function of every digital input, the analog inputs and output, the relays and digital outputs |

![The Motor screen of a Lenze i550](img/drv-motor.webp){: .sb-center}

### The terminals

On **Inputs & outputs** every terminal of the drive is a square
indicator beside its field. While the drive is connected the indicators
show the terminals' states - **green** for TRUE, dark for FALSE, an empty
outline when the drive does not say. Every relay and digital output is a
block of its own, and a block the product does not have is not drawn: a
MICROMASTER 440 shows three relays, a MICROMASTER 420 one.

![Inputs & outputs of a MICROMASTER 440 - six inputs, the analog channels, three relays](img/drv-io.webp){: .sb-center}

## Quick setup

**Quick setup** on the Overview page walks through the essential
settings screen by screen - the motor, the ramps, the control - with
**Next** and **Back**. At the end the settings are in the project and the
wizard offers to write them to the drive at once (**Write to drive**).

![Quick setup, step one: the motor](img/drv-quick.webp){: .sb-center}

A value set on a screen or in the wizard is the same value as on the
Parameters view: it lands in the project's changes and goes to the drive
with **Write to drive**.

---

Back to [Drives](/docs/drives/).
