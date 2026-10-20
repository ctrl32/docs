---
title: RS-485 and Modbus RTU
source: docs/tutorial-rs485.md
hero: img/rtu-master-page.webp
---

# Two wires, several devices, a number on the screen

Master Modbus RTU slaves from a Linux device over RS-485: every register becomes a plain variable the program and the screens use, with no code for the bus.

## Who it is for
- Integrators wiring Modbus RTU I/O modules, controllers and sensors
- Projects mixing ctrl32 boards with existing RS-485 devices
- Anyone who has fought a bus that works at 9600 and fails at 115200

## What you get
- A Modbus RTU master added from the tree, devices hanging under it by unit address
- Register maps from the catalogue of Modbus devices, or named yourself
- A variable with a Modbus source carries unit, register, function and type - the program never knows the value came over wires
- 32-bit values (`i32`, `u32`, `TIME`) as two registers in one request, with selectable word order
- Deadband on analog values
- Writable variables written back; the master reads before it writes, so a setpoint kept in the slave is not overwritten at start
- Silent units named on the console and in the diagnostic buffer, with their address
- Spec-correct frame timing: 3.5 characters of silence

## How it works
1. Wire A to A, B to B, a common reference; 120 ohms at the two ends only; one master.
2. In Online > Prepare a Linux device pick the expansion board - the port comes with it and is taken away from the login console.
3. Click the RS485 node, set baud, parity, stop bits and the timeout.
4. Right-click RS485 > add *Modbus RTU master*.
5. Add one device per slave with its unit address; take its registers from the catalogue or define them.
6. Deploy and read the console or the diagnostic buffer.

## Pictures
- ![The Modbus RTU master page: the line it uses and the devices on it](img/rtu-master-page.webp) - the master and its devices
- ![The line's parameters: baud, parity, stop bits, timeout](img/rs485-page.webp) - every device on the pair must agree
- ![A device's register map: what is read, from which address, as what type](img/modbus-registers.webp) - registers become variables

## Runs on
- A Linux device with an RS-485 port: the reTerminal with its E10-1 expansion (port `ttyS0`), or any device with a USB adapter
- Slaves on the bench: an inoCORE32-TM8.6 with three temperature zones and an inoCORE32-TM1.1 panel; any Modbus RTU device works

## Facts to keep exact
- Project: `examples\rs485_system.prj32` (example page "RS-485 system" - one project, three devices, deployed as one)
- Termination: 120 ohms across A and B at the first and last device, nowhere else; termination in the middle is the most common cause of a bus that works at 9600 and fails at 115200
- A ground or shield at one end keeps long cable ends at the same potential
- Modbus RTU has exactly one master
- Two devices on one pair must never share a unit address
- Functions: holding register, input register, coil, discrete input
- A 16-bit value is one register; `i32`, `u32`, `TIME` are two and travel in one request
- Wrong word order gives numbers wildly wrong, not slightly wrong
- Checklist order: A/B swapped (symptom is silence), address, baud/parity/stop bits, termination, login console on the port
- Bench result: the zone temperature the master reads matches the slave's own reading to the digit; a setpoint written from the master's screen lands in the slave and stays; the pair runs in the test wall with every release
- A frame ends after 3.5 characters of silence at the line's baud rate; every ctrl32 device waits that before speaking; keep mixed ctrl32 devices on a current version

## Call to action
Download the editor and open `examples\rs485_system.prj32`.
