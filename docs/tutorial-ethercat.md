---
image: img/ethercat-device.webp
image_alt: "The PDO tab of an EtherCAT drive: its own data and what was added to it"
---

# EtherCAT, step by step

One cable through every device, a drive at the end of it, and a motor
that turns from a button on the screen. This page goes from an empty
network port to a running axis, one step at a time.

[EtherCAT](ethercat.md) is the reference; this is the walk.

**What is used here**

- A Linux device with a **spare network port** — the reTerminal with
  its E10-1 expansion has a second gigabit port, which is exactly what
  this needs.
- A Lenze i550 with an EtherCAT module. Any CiA 402 drive works the
  same way; its own description file is what differs.
- The project is `examples\reterminal_ecat_example.prj32`.

---

## 1. Give the master a port of its own

An EtherCAT master owns its interface: it sends raw frames on it and
no IP address lives there. Pick the port in *Tools › Prepare a Linux
device* (or in *Buses of this device*) — on the reTerminal E10-1 that
is `eth1`, the port the expansion adds.

Plug the cable into the drive's **IN** socket. A line runs from the
master into the first device's IN, out of its OUT and into the next
one's IN; the last device's OUT stays empty.

---

## 2. Put the device's description in the library

Every vendor ships an **ESI file** for its device — an XML description
of what the device is and what it can do. Take it from the vendor's
site or from the disc that came with the drive, and add it in
*Tools › Device library*, the EtherCAT section. The Lenze i550 is in
the library already.

---

## 3. Add the line and the slave

In the tree, under **Ethernet**, add **EtherCAT**. The page that opens
is the master's: the cycle time, and the slaves in the order they are
wired.

![The tree with the line in place: the EtherCAT master, the slave under it and the variables it brought with it](img/ecat-tree.webp){: .sb-center}

![The EtherCAT master's page](img/ecat-buspage.webp){: .sb-center}

Press **Add from library** and pick the device. Everything the project
needs about it comes from its description:

- vendor and product code, so the runtime refuses to run a line where
  the wrong device sits at that position,
- the sizes of its process data,
- the CiA 402 layout when it is a drive,
- a signal, with a variable, for every value the device sends by
  itself.

---

## 4. Look inside the device

Double-click the slave. The window has the same tabs a CAN device has,
and the one to read first is **PDO mapping**: what the device sends by
itself, and what this project added behind it.

![The PDO tab of the drive: its own data, and what was added](img/ethercat-device.webp){: .sb-center}

A drive always sends its status word, its actual speed and its error
code. The current, the torque, the DC link voltage and the output
frequency are objects the master may **add** — and on the
**Variables** tab you tick exactly those, press *Import*, and the
editor writes the mapping, the start-up writes, the signals and the
variables for you.

---

## 5. Make it an axis

A CiA 402 drive is an axis, and the motion blocks command it exactly
as they command a CANopen drive. Use the axis wizard: in the tree,
*Motion › add axis*, choose **EtherCAT** as the bus and the device
from the library. One step makes the slave, the axis on its position,
the start-up writes that put the drive in velocity mode under network
control, and the variables the blocks bind to.

![The axis wizard: the bus, the device from the library and the axis it will make](img/axis-wizard.webp){: .sb-center}

From there the program is ordinary: `MC_POWER` to enable,
`MC_MOVEVELOCITY` for a speed, the status word's bits for the lamps.

---

## 6. The motor data, which is not in the project

A drive holds the motor's data itself — pole pairs, rated speed,
rated current, the voltage curve. A drive that has never met the motor
runs the factory values, and the first start ends in an over-current
trip.

This catches people out when a drive's **network module is replaced**,
because the parameter set lives in the module: the drive looks
identical and knows nothing about the motor. Set the motor data in the
drive, by its keypad or its own tool, before the first start.

The writes the project makes at every start are its own tab, so what
the drive is told is visible before anything turns.

![The start-up writes of the slave: what the project sets in the drive at every start](img/ecat-sdo-tab.webp){: .sb-center}

---

## 7. Bring it up

Deploy, and read the device's log. A healthy line says, in order: the
interface is up, the slaves found and what they are, the mapping
written, the images mapped, the axis bound, the cycle running.

**What the lines mean when it does not work**

- *no slave answers* — the cable is in the wrong socket, or the port
  named in the settings is not the one the cable is in.
- *another device at that position* — the vendor or product code does
  not match the project's. Compare them on the Device tab.
- *SDO rejected* — the device refused a start-up write and the line
  that follows says why, in its own words.
- *the bus did not reach OPERATIONAL* — usually the mapping: a device
  that receives one it cannot do says so and sends zeros.

---

## 8. Turn the motor

START from the screen, with its confirmation. Watch the speed rise on
its ramp and the current with it; the error code stays at zero.

On our own bench that is a 0.37 kW motor at 300 rpm drawing 0.48 A at
20 Hz, with the DC link at 319 V — every one of those numbers coming
over the line as a variable, none of them written by hand.

!!! warning "The motor is real"
    Stopping over EtherCAT is **not** a safety function. The emergency
    stop belongs on the drive's STO terminals, hard-wired.

---

## Where to go next

- [EtherCAT](ethercat.md) — the reference: the device window tab by
  tab, what a master may add, and what the line does not do.
- [reTerminal, the drive on EtherCAT](example-reterminal-ecat.md) —
  the project this page walks.
- [Motion blocks](blocks-motion.md) — what commands an axis.
