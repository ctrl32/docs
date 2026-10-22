---
title: "The node (ESP32-C3 / C6)"
slug: node
section: "Hardware"
order: 8
sidebar_position: 8
image: img/node-reflexes.webp
image_alt: "The reflex table of a node in the editor: an input, a condition, an output and an action per row"
generator: tools/docs_export.py
---

# The node (ESP32-C3 / C6)

A **node** is the smallest ctrl32 device: an ESP32-C3 or ESP32-C6 module
that carries inputs and outputs and **no program of its own**. The logic
lives in the main device — a panel, a headless board or a Linux device —
and the node is its remote I/O: it reads its inputs, publishes them over
the network, and takes the main device's commands for its outputs.

What makes it more than a dumb I/O module is the **reflex table**: a
short list of "this input switches that output" rules the node keeps
running by itself. The house keeps its light switches when the main
device reboots or the network is gone.

A node is a full ctrl32 device in the editor: the same project file,
the same variables, the same pin pickers, the same deploy. It runs no
program and draws no glass; everything else it does the way every other
board does it.

---

## Which modules

Every ESP32-C3 and ESP32-C6 module of the
[hardware catalog](/docs/hardware/modules/) runs the node image — the MINI and WROOM
families in all their memory variants. The node image is one build per
chip and flash size; a module of the same size runs the same image.

The C6 is the richer chip: Wi-Fi 6 and the radio a future Thread network
will want; both carry one CAN controller, as every ESP32 does. The C3 is the cheaper one for a box
with a handful of switches.

---

## A node project

Pick a C3 or C6 module in the New project wizard. The wizard says what a
node is and offers no program language and no visualization — the node
has no display — only the WEBview page.

The tree of a node project is the tree of every ESP device, with one
difference under **Application**: instead of programs and tasks there is
one row, **Reflexes**.

![The tree and the reflex table of a node](img/node-reflexes.webp){: .sb-center}

---

## Inputs and outputs

A node's inputs and outputs are **variables on pins**, made the way they
are on every board: a digital input or output on a free pin, an analog
input with a [sensor type](/docs/peripherals-and-services/analog-inputs/) on an ADC pin, a 1-Wire
thermometer, a PWM or NeoPixel output, a chip on the I2C bus.

What the node adds is the **Node** section of a variable's Properties:

- an **input** has a debounce time and may be inverted — a contact that
  bounces for a few milliseconds reaches the network once, settled;
- an **output** says what it does **without the main device**: hold the
  last value, go off, go on, or take a value (a PWM duty, a setpoint).

![The Node section of an output variable](img/node-properties.webp){: .sb-center}

The moment the main device goes silent for longer than the **main
device timeout** (the Application page, 5 s by default), every output
goes to that state once, and the reflexes marked "only without the main
device" start acting. When the main device speaks again, it owns the
outputs again.

Any traffic of the main device counts - a net32 frame, a Modbus request
(a read as much as a write), an MQTT command, a frame from the head of
a stepCAN rack. Set the timeout longer than the main device's polling
period: a Modbus master that reads the node every 5 seconds against a
timeout of 3 seconds makes the node see its main device come and go at
every poll, and the safe state and the "only without the main device"
rows run in between.

---

## The reflex table

One row of the table is one rule: **an input, a condition, an output,
an action**, and whether the rule acts only without the main device or
always.

| Column | Choices |
|:---|:---|
| Condition | high, low, rising edge, falling edge, above a threshold, below a threshold — the thresholds with a hysteresis band, so a noisy reading never chatters |
| Action | follow (the output copies the condition), toggle (flips on each edge), set, reset, pulse (on for a time), delay on, delay off |
| Time | the pulse length or the delay, in milliseconds |
| Acts | only without the main device — the default; with it present the main device owns the outputs — or always |

Up to 16 rows. Some rows a house wants:

- **A staircase light.** Input: the push-button, rising edge. Output:
  the lamp, toggle, always. The button works with or without the main
  device; the main device still sees the lamp's state and can switch it
  from a screen.
- **A frost guard.** Input: the room temperature, below 3 with a band of
  1. Output: the heater, follow, only without the main device. While the
  main device runs its own heating logic the row sleeps; when it is
  gone the node keeps the pipes from freezing.
- **A door bell.** Input: the bell button, rising edge. Output: the
  chime relay, pulse, 500 ms, always.

A row the node cannot run is refused where you make it: a follow on an
edge, a pulse without a time, an output that is not a switch the node
drives.

---

## Over what

A node speaks whichever of these the project turns on — several at once
are fine:

| Transport | What it carries |
|:---|:---|
| [net32](/docs/buses/net32/) over Wi-Fi | the node's variables to the main device and its commands back — the usual road |
| net32 over CAN | the same on a CAN wire, where the house is cabled |
| [MQTT](/docs/buses/home-assistant/) | every variable a topic, commands in — a sensor or relay box for a home server, with or without a main device |
| Modbus TCP and RTU ([buses](/docs/buses/)) | the node as a Modbus slave (its variables as registers) and as a master reading an energy meter or a sensor on its RS485 line |

And the **WEBview page**: a node serves one small page to one browser at
a time — its variables, its switches. Big dashboards belong on the main
device.

---

## The stepCAN module

A node can be a module of a **stepCAN rack**: the I/O modules that chain
on one cable, take their address from their position and need no
configuration to be swapped. Tick **stepCAN module** on the Application
page of a node on the stepCAN module board; the node's inputs and
outputs become the module's channels, the rack's head drives them, and
the chain and the terminator are the board's business. The stepCAN
specification itself is published on [its own pages](https://www.ctrl32.com/docs/stepcan/).

How a rack works:

| | |
|:---|:---|
| Cable | one Cat5e cable carries the CAN bus past every module, and beside it a one-way "you are next" chain |
| Connector | RJ45, pinned to the CANopen connector standard |
| Addressing | at power-up the head station walks the chain and hands out CANopen node-IDs in strict physical order — no switches, no commissioning tool |
| Size | up to 64 modules per segment, enumerated in under a second |
| Bus | 500 kbit/s, up to 30 m |
| Mounting | modules on a DIN-rail backplane, scattered around a building, or both on one segment |
| Profile | CANopen (CiA 301, 305 and 401): the I/O reaches a project as CANopen variables, in the cycle |

A module is added or replaced by plugging it in; the address comes from
the position. A wrong module in a slot is seen by the head station as a
mismatch.

---

## Sleeping on batteries

A node that lives on a battery sleeps between its reports. **Sleep
period** on the Application page says how long: 0 means never (a node
on a supply), otherwise 10 to 1020 seconds. The node wakes on the
timer and on any of its own digital inputs changing, debounces the
inputs, publishes its variables, hears what the main device has for
it, runs its reflexes, and sleeps again. Its outputs keep their levels
through the sleep.

The main device knows. A command sent to a sleeping node - a switch
pressed on a screen - is kept and delivered in the node's next window;
a node is reported absent only when two of its periods pass in
silence, not before. At a five-minute period a node reports a year on
two AA cells; a node that wakes every ten seconds spends most of its
charge on the radio.

A stepCAN module never sleeps - the rack powers it and expects its
heartbeat - and the field is greyed out on one.

A sleeping node is reachable only in its window, so a new project or a
runtime over Wi-Fi reaches it the way a command does - at its next
wake; the first load over USB happens before the node ever sleeps.

---

## Loading and updating

The first time, the node is loaded over USB — the chip's own USB port,
no adapter needed. After that the project and the runtime both travel
over Wi-Fi, the way they do to every board that has two runtime slots:
a failed transfer leaves the old one running.

---

## Limits and honesty

| | Node |
|:---|:---:|
| Variables | 128 |
| Alarms | 32 |
| Reflexes | 16 |
| Browser viewers at once | 1 |
| Programs | none — the main device runs the logic |

A node is not a safety device. Emergency stops, door guards and anything
that must act when software fails are wired, never routed through a
node — the [intended use](/docs/about/intended-use/) page says it for every
ctrl32 device.
