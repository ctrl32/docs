---
title: "Control from the device"
slug: drives-control
section: "Drive library"
order: 321
sidebar_position: 321
image: img/drv-block.webp
image_alt: "The DRIVE block bound to a drive"
generator: tools/docs_export.py
---

# Control from the device

A drive of the project can be **run by the device's program** over
Modbus: start and stop, the direction, the speed in Hz and fault
acknowledgement - and its state, actual speed, current and fault code
back. One block does it for every supported drive:
[DRIVE](/docs/blocks/drv-drive/).

| Drive | Bus |
|:---|:---:|
| Siemens SINAMICS G120 (CU240B-2 / CU240E-2), G120C | Modbus RTU over RS485 |
| Parker AC15, AC20, AC30 | Modbus TCP |

The page of any other drive says that the device cannot control its
series yet.

## Step by step

1. **Open the drive** under *Drives* in the device tree. In
   **Control from the device** on its Overview page pick the **RS485
   line** (or type the drive's **IP address**) and its **Modbus
   address**, then press **Control from the device**.

    The editor makes, in one step:

    - the drive's Modbus device on that line or address;
    - six variables named after the drive - `<name>_cw` (control word),
      `<name>_sp` (setpoint), `<name>_sw` (status word), `<name>_act`
      (actual speed), `<name>_cur` (current), `<name>_flt` (fault code);
    - in the drive's parameter set, the settings that give the bus the
      control: on a SINAMICS the Modbus protocol (`p2030 = 2`), the
      monitoring time (`p2040`), the address (`p2021`) and the baud rate
      of the line (`p2020`); on a Parker one Modbus TCP connection and a
      one-second comms timeout;
    - the `drives` block library in the project.

2. **Place a DRIVE block** in a program and pick the drive in the
   block's properties (**Drive**). The block's word pins are bound to the
   drive's variables, its parameters - the shape of the control word and
   the scales - are set from the drive's description and the motor's
   nameplate.

    ![A DRIVE block bound to a drive](img/drv-block.webp){: .sb-center}

3. **Write the drive's parameters** into the drive once (**Write to
   drive** on its page, then **Save in drive**), so it takes its control
   from the bus.

4. **Download the project** to the device. `Enable`, `Reverse`, `Speed`
   and `Reset` are now the program's.

## The watchdog

The control word and the setpoint are written to the drive on **every
poll**, not only when they change, and the drive's own fieldbus watchdog
is set to about one second. When the device stops answering - a power
cut, a broken cable - the drive stops by itself.

This needs a runtime of line 1.07 or newer on the device.

## Safety

A stop over a fieldbus is **not a safety function**. The drive's safe
torque off (STO) terminals must be wired, and an emergency stop acts on
them, never through the program.

---

Back to [Drives](/docs/drives/).
