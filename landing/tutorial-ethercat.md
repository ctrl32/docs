---
title: EtherCAT drive
source: docs/tutorial-ethercat.md
hero: img/ethercat-device.webp
---

# One cable, a drive at the end, a motor that turns from the screen

Run a CiA 402 drive over EtherCAT from a Linux device: import the vendor's description, let the axis wizard build the rest, and command it with the standard motion blocks.

## Who it is for
- Builders of drive-based equipment moving to EtherCAT
- Integrators using Lenze i550 or other CiA 402 drives
- Teams who want drive values (current, torque, DC link) as variables without hand-written mapping

## What you get
- An EtherCAT master on a spare network port of a Linux device
- Device descriptions (ESI files) in a device library; the Lenze i550 is already there
- *Add from library*: vendor and product code checked, process-data sizes, CiA 402 layout, a signal and variable for every value the device sends
- A PDO mapping tab showing sync managers, assigned PDOs and entries
- Extra objects - current, torque, DC link voltage, output frequency - added by ticking them and pressing Import
- An axis wizard: slave, axis, start-up writes for velocity mode under network control, and the variables, in one step
- The same motion blocks as a CANopen drive: `MC_Power`, `MC_MoveVelocity`
- A log that says in plain words what is wrong when the line does not come up

## How it works
1. Pick the master's port in Online > Prepare a Linux device (on the reTerminal E10-1: `eth1`); cable into the drive's IN socket.
2. Add the vendor's ESI file in Tools > Device library, EtherCAT section.
3. Under Ethernet add EtherCAT; press *Add from library* and pick the device.
4. Open the slave, read the PDO mapping tab, tick the extra values on the Variables tab and press Import.
5. Motion > add axis, bus EtherCAT, device from the library.
6. Set the motor data in the drive itself (keypad or its own tool) before the first start.
7. Deploy, read the log, press START on the screen.

## Pictures
- ![The PDO tab: the sync managers of the drive, the PDOs assigned to the one picked, and the entries that PDO carries](img/ethercat-device.webp) - what the drive sends and what the project added
- ![The tree with the line in place: the master sits under the adapter it owns, eth1, with its slave under it](img/ecat-tree.webp) - the master under its own adapter
- ![The EtherCAT master's page](img/ecat-buspage.webp) - cycle time and slaves in wiring order
- ![The axis wizard: the bus, the device from the library and the axis it will make](img/axis-wizard.webp) - one step to a working axis
- ![The start-up writes of the slave: what the project sets in the drive at every start](img/ecat-sdo-tab.webp) - visible before anything turns

## Runs on
- A Linux device with a spare network port: the reTerminal with its E10-1 expansion (second gigabit port, `eth1`)
- Lenze i550 with an EtherCAT module; any CiA 402 drive works the same way with its own description file

## Facts to keep exact
- Project: `examples\reterminal_ecat_example.prj32` (example page "reTerminal, the drive on EtherCAT")
- The master owns its interface: raw frames, no IP address on it
- Wiring: master into the first device's IN, OUT to the next IN; the last OUT stays empty
- The tree shows one row per adapter under Ethernet once the editor has looked at the device; before that the master sits under Ethernet itself
- The runtime refuses a line where the wrong device (vendor/product code) sits at a position
- A drive always sends status word, actual speed and error code; current, torque, DC link voltage and output frequency are objects the master may add
- Motor data (pole pairs, rated speed, rated current, voltage curve) lives in the drive; factory values end the first start in an over-current trip; a replaced network module carries no motor data
- Healthy log order: interface up, slaves found, mapping written, images mapped, axis bound, cycle running
- Log messages: *no slave answers* (wrong socket or wrong port); *another device at that position* (vendor/product code mismatch, compare on the Device tab); *SDO rejected* (the next line says why); *the bus did not reach OPERATIONAL* (usually the mapping)
- START from the screen has a confirmation
- Bench: a 0.37 kW motor at 300 rpm drawing 0.48 A at 20 Hz, DC link 319 V - all as variables
- Safety: stopping over EtherCAT is not a safety function; the emergency stop belongs on the drive's STO terminals, hard-wired
- Trademark line: EtherCAT® is a registered trademark and patented technology of Beckhoff Automation GmbH, Germany (keep the original notice wording on the web page)

## Call to action
Download the editor and open `examples\reterminal_ecat_example.prj32`.
