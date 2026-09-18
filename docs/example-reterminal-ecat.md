# reTerminal — the same, with the drive on EtherCAT

The [reTerminal example](example-reterminal.md) with one change: the
Lenze i550 hangs on the E10-1's second network port as an **EtherCAT
slave** instead of its CAN terminal. The screens, the RS-485 pair, the
device page and the alarms are the same project; the drive's part
shows what moving a drive from one bus to the other costs — a few
lines.

**Project:** `examples\reterminal_ecat_example.prj32`
**Board:** Seeed reTerminal (CM4) with the reTerminal E10-1 expansion
**Needs:** a Lenze i550 with its EtherCAT module on the E10-1's second
network port, and the two slaves of the [RS-485 system](example-rs485.md)
on its RS-485 terminal — or nothing: the screens run, the lamps stay dark

!!! warning "The motor is real"
    The drive starts **only** after START is pressed and confirmed.
    Stopping over EtherCAT is **not** a safety function: the emergency
    stop belongs on the i550's STO terminals, hard-wired.

---

## What changes

![The drive screen with the i550 on EtherCAT: the same dial, current, torque, DC link and frequency from the mapped process data](img/example-reterminal-ecat-0.webp){: .sb-center}

- **The axis** names the EtherCAT backend and the slave's position on
  the bus instead of a CANopen node: `backend: cia402_ecat, node: 1`.
- **The slave comes from its ESI.** The i550's description sits in the
  device library; *Add from library* on the EtherCAT page fills the
  identity, the image sizes, the CiA 402 layout and the error-code
  signal — the section below is what that produces, plus the mapping.
- **An `ethercat:` section** describes the line: the cycle, the slave
  (vendor and product so a wrong device is refused), its image sizes,
  the SDO writes that put the drive under network control, and the
  **signals** — which bytes of the slave's input image land in which
  variable. The statusword and the error code are two such signals.
- **The device's setting** `ecat=eth1` names the interface — written
  from the editor's board window, like the serial port.
- **What the drive sends** is partly fixed — statusword, actual
  velocity, error code — and partly the master's choice: the i550 has a
  user-configurable process data object, and the `sdo_init` list maps
  current, torque, DC link and output frequency into it at every start
  (the assignment cleared first, the mapping written, then the
  assignment set to both objects). Four more signals with a gain, and
  the screen shows the same numbers as the CAN twin.

The `DRIVE_i550` block, the confirmation on START, the setpoint by
keypad or slider, the ramps, the lamps from statusword bits, the trend,
the pair, the device page and the alarms: unchanged.

---

## Worth copying

- **A bus is a section, a drive is an axis.** The program never knows
  which bus its axis rides; `MC_POWER` and `MC_MOVEVELOCITY` inside
  `DRIVE_i550` are the same blocks over CANopen and over EtherCAT.
- **Signals, not code.** A byte range of a slave's image, a variable,
  a gain — that is the whole of reading a drive's or a terminal's data.
- **Vendor and product in the slave.** With them the runtime refuses
  to run the line when the wrong device sits at that position, instead
  of writing a controlword into it.
