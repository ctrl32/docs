---
title: Prepare a Linux device
source: docs/tutorial-linux-device.md
hero: img/lx-prepare-plan.webp
---

# A blank Raspberry Pi becomes a running HMI and controller - without one Linux command

Give the editor an address, a user name and a password; it installs the runtime, sets up the operating system and leaves a device that boots into your visualisation, serves it to a browser and answers OPC UA.

## Who it is for
- Integrators who want a Raspberry Pi or reTerminal as a controller and panel
- Engineers who do not want to administer Linux by hand
- Projects that need CAN, RS-485, I2C or a real-time EtherCAT kernel on a Pi

## What you get
- Everything done from the editor - Online > Prepare a Linux device
- A look before any change: the editor reads the device and lists the plan step by step
- One-time password: the editor puts its own key on the device; the password is never stored
- Operating-system settings from ticks: expansion boards, serial console, I2C driver, header buses, CAN and serial controllers on SPI, real-time kernel, device name and fixed network address
- The runtime installed with its own account, started by the system at every boot
- Updates of project and runtime over the network afterwards
- WEBview at `http://<address>:8080`, OPC UA on port 4840, found by the editor's device scanner

## How it works
1. Write a fresh Raspberry Pi OS card with SSH enabled and a user (the Raspberry Pi Imager asks for both).
2. In the editor: New project, pick the reTerminal or Raspberry Pi under *Linux*, tick what the project does.
3. Online > Prepare a Linux device: type address, user name, password, and which device it is.
4. Press *Look at the device* - nothing changes; the editor shows what it found and the plan.
5. Tick the operating-system settings the device needs.
6. Press *Prepare it*; the editor reports each step as it lands.
7. Build and deploy like any board; the screen comes up, and later runtime updates travel the same network road.

## Pictures
- ![Prepare a Linux device: what the device is, and the plan before anything changes](img/lx-prepare-plan.webp) - the whole plan, shown before anything is changed
- ![The New project wizard with the Linux boards in the list](img/lx-wizard.webp) - pick the device under Linux
- ![The Prepare a Linux device page before anything has been looked at](img/lx-prepare-open.webp) - address, user and password, once
- ![The Operating system section: the serial console, the buses on the header, three controllers on SPI, the real-time kernel, the device name](img/lx-prepare-sys.webp) - device settings as ticks
- ![Upload runtime: the device, its current version and the one the editor has](img/lx-runtime-dlg.webp) - the runtime updates over the network
- ![The board card of a Linux device](img/lx-board-card.webp) - what the device reported about itself

## Runs on
- 64-bit Raspberry Pi: Pi 4, Pi 5, CM4, CM5, Zero 2 W
- Seeed reTerminal (with the E10-1 expansion: CAN interface, RS-485 port, second gigabit port)
- Raspberry Pi OS, on the same network as the PC

## Facts to keep exact
- Time: half an hour; not a single Linux command typed
- The runtime comes with the editor; nothing else to download
- *Do not ask for the password again* (ticked by default): the password is used once and never stored
- *Look at the device* changes nothing
- Plan steps: runtime copied, unpacked, installed with its own account and permissions, given the device's identity, started, waited for until it answers
- A device that already runs ctrl32 is told so and the network road takes over
- The Operating system page is a tab beside the project; every line the work prints goes to Messages as well
- The serial-port option takes the port away from the login console: a login shell on the serial port of a fresh Raspberry Pi OS would fight the RS-485 line
- Real-time kernel for EtherCAT: one tick for a bus cycle under a millisecond - the distribution's real-time kernel, a core kept for the bus, the runtime pinned to it
- CAN and serial controllers on SPI: each row a chip, its SPI bus and chip select, chip-select pin, interrupt pin and crystal; the editor counts how many more fit
- The device restarts only when a boot setting changed, and the window says so beforehand
- WEBview: `http://<address>:8080`; OPC UA: port 4840

## Call to action
Download the editor, write a Raspberry Pi OS card, and let the editor prepare the device.
