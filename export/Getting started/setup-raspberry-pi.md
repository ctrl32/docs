---
title: "Raspberry Pi"
slug: setup-raspberry-pi
section: "Getting started"
order: 3
sidebar_position: 3
generator: tools/docs_export.py
---

# Raspberry Pi: from a blank card to a running program

This page takes a 64-bit Raspberry Pi - Pi 4, Pi 5, CM4, CM5, Zero 2 W, or
a Seeed reTerminal - from a blank card to the ctrl32 runtime running your
project, watched live from the editor. Everything after writing the card
is done from the editor; no Linux command is typed.

**You need**

- a Windows PC with the ctrl32 editor installed - the Linux runtime comes
  with it,
- the Raspberry Pi on the same network as the PC,
- the **Raspberry Pi Imager** to write the card.

---

## 1. Write the card

Write **Raspberry Pi OS Lite (64-bit)** with the Raspberry Pi Imager.
*Lite* is deliberate: the runtime draws the display itself and needs no
desktop.

In the Imager's settings, before writing:

- a **hostname** you will recognise on the network,
- a **user** and its **password**,
- **SSH enabled**,
- the network (WiFi) if the device is not on a cable.

Boot the device with the card.

---

## 2. Make the project

*New project* (Ctrl+N), a name, and under *Linux* the device: the
**reTerminal**, or **Raspberry Pi** for every other model.

![The New project wizard with the Linux boards in the list](img/lx-wizard.webp){: .sb-center}

Tick what the project does - Visualization for a screen, WEBview for the
browser, and the buses the device will talk on. Every part can be added
later from the project tree.

A Raspberry Pi without a monitor serves WEBview; HMI screens are added
from the tree (right-click *Screens* > *Add screen*) when a monitor is on
the HDMI.

---

## 3. Tell the editor where the device is

**Online > Prepare a Linux device**: the device's address, the user and
the password from step 1, and which device it is.

![The Prepare a Linux device page](img/lx-prepare-open.webp){: .sb-center}

Leave **Do not ask for the password again** ticked: the editor puts its
own key on the device and later visits need the address alone. The
password is used once and never stored.

---

## 4. Look before anything changes

**Look at the device** logs in, reads what the device is and lists what
*Prepare* will do. Looking changes nothing.

![What the device is, and the list of steps Prepare will take](img/lx-prepare-plan.webp){: .sb-center}

---

## 5. The operating system settings

Under the plan, **Operating system of this device** holds what belongs to
the device rather than to the project:

![The Operating system section](img/lx-prepare-sys.webp){: .sb-center}

| Setting | When |
|:---|:---|
| Expansion board | a reTerminal E10-1 or another board on the header - its boot lines are added |
| Free the serial port from the login console | an RS-485 line on the serial port |
| Load the I2C driver at every start | chips over I2C |
| Buses on the header | SPI, I2C, the UART |
| CAN and serial controllers on SPI | a CAN or serial HAT - one row per chip |
| Real-time kernel for EtherCAT | an EtherCAT bus cycle under a millisecond |
| Device name, Network | a fixed address instead of DHCP |

Each ticked line is one step. The device restarts only when a boot
setting changed, and the page says so first.

---

## 6. Prepare it

**Prepare it** copies the runtime over, installs it with its own account,
gives it the device's identity, starts it and waits until it answers.
Each step is reported as it lands. From then on the device starts the
runtime at every boot.

---

## 7. Download the program

Pick the device's address in the toolbar's port picker and press
:ti-download: or `F5`. The runtime loads the project and the screen comes
up.

Every later change is this step alone.

---

## 8. Check it and watch it run

- **ONLINE** (the plug icon) shows the live values in the rungs, the
  variables and the screen preview.
- **WEBview**: `http://<address>:8080` in a browser on the same network.
- **OPC UA**: every variable is served on port 4840 - see [OPC UA](/docs/buses/opcua/).
- The [scanner](/docs/deployment/find-devices/) finds the device from now on.

![The board card of a Linux device](img/lx-board-card.webp){: .sb-center}

---

## Updating the runtime

A new line of the editor (a version ending in `.000`) brings a new runtime.
*Flash runtime* with the device's address sends it over the network:

![Upload runtime: the device, its current version and the one the editor has](img/lx-runtime-dlg.webp){: .sb-center}

The device checks the file is built for its processor, starts it once as a
self-check, keeps the previous runtime and returns to it by itself if the
new one does not reach the program and the server. The program, the
retained values and the settings stay.

---

## The ports the runtime uses

| Port | What lives there |
|:---|:---|
| `8080` | WEBview, the program upload, the scanner |
| `4840` | the OPC UA server |
| `3232` | the editor's online connection |

A firewall between the editor and the device has to pass these three.

---

## Other Linux devices

The **STM32MP157C-DK2** gets its operating system from ST's OpenSTLinux
package and its runtime by hand; the steps are on
[Setting up a Linux device](/docs/hardware/linux-setup/), together with the manual
road for every device and the settings file of the runtime.

---

## Next

- [The Linux runtime](/docs/hardware/linux-runtime/) - what it does and its limits
- [Modbus](/docs/buses/modbus/), [CANopen](/docs/buses/canopen/), [EtherCAT](/docs/buses/ethercat/)
- [Editor](/docs/editor-overview/editor/), [Variables](/docs/editor-overview/variables/)
