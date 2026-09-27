---
image: img/example-reterminal-ecat-0.webp
image_alt: "The same reTerminal project with the drive on EtherCAT"
---

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
on its RS-485 terminal — or nothing: the screens run, the lamps stay dark.
The line in the file also carries **two Lenze i700 servo inverters** ahead
of the i550 (a single and a double); without them the master reports
the missing slaves and the i550 alone does not run - remove the two
slaves and their axes, or put the same drives on the line

!!! warning "The motor is real"
    The drive starts **only** after START is pressed and confirmed.
    Stopping over EtherCAT is **not** a safety function: the emergency
    stop belongs on the i550's STO terminals, hard-wired.

---

## What changes

![The drive screen with the i550 on EtherCAT: the same dial, current, torque, DC link and frequency from the mapped process data](img/example-reterminal-ecat-0.webp){: .sb-center}

![The drive screen: the dial, START with its confirmation, the values that travel over the line](img/rt-drive-ecat.webp){: .sb-center}

- **The axis** names the EtherCAT backend and the slave's position on
  the bus instead of a CANopen node: `backend: cia402_ecat, node: 3` -
  the i550 is the third slave, after the two servos.
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
  assignment set to both objects). The list declares the assignment of
  the fixed receive object as well — a drive that lost either one, say
  switched off and on while the master was configuring it, is set right
  at the next start instead of refusing every output image. Four more
  signals with a gain, and the screen shows the same numbers as the CAN
  twin.

The `DRIVE_i550` block, the confirmation on START, the setpoint by
keypad or slider, the ramps, the lamps from statusword bits, the trend,
the pair, the device page and the alarms: unchanged.

---

## The servos

The two i700s are servo inverters and run **cyclic position mode**
(csp): the device computes the position setpoint every cycle and the
drive follows it, so the line runs on the **distributed clock** at
1 ms (`cycle_us: 1000`, `dc: true`); the i550 has no use for the clock
and stays synchronous to its process data, which the console says at
start.

Each servo slave is what *Add from library* produces for an i700: the
mode `csp`, only the csp pair of process data objects assigned (the
start-up writes declare it), and the offsets of the 32-bit words - the
target position, the velocity feed-forward and the mode in the 17 bytes
the drive takes, the actual velocity and the actual position in the 21
it sends. The double inverter carries **two axes in one slave**: its
record says where axis B's words begin (`stride_out: 17`,
`stride_in: 21`) and the axis on it says `sub: 1`. Three signals per
axis read the error code, the actual position and the following error
into variables.

![The servo screen: three axes side by side with enable, run, the setpoint, the actual velocity, the following error, the torque and the position, and one trend of the three velocities](img/example-reterminal-ecat-servo.webp){: .sb-center}

The **servo screen** (the *Servos* door on the drive screen; the web
page has the same) puts the three axes side by side: enable and run
with a confirmation, the setpoint by keypad or slider, the actual
velocity with a bar, the following error, the torque and the position
straight from the drive's words, the error code - and one trend of the
three actual velocities at 50 ms. A well-tuned axis draws a flat line;
one whose loop hunts draws a band, which is what the screen is for: the
drive's loops are tuned against it (the current, speed and position
controller settings are start-up writes of the slave, so a setting
found on the bench is written at every start).

Three axes - `servo1` on the single, `servo2a` and `servo2b` on the
double - are commanded by the `SERVO` program, three lines per axis:

```
pw1(AXIS := 1, Enable := s1_en);
mv1(AXIS := 1, Execute := s1_go, Velocity := s1_rpm);
rd1(AXIS := 1, Enable := TRUE);
s1_act := rd1.Velocity;
```

`MC_POWER` enables the drive, `MC_MOVEVELOCITY` sets the velocity - the
device ramps it and integrates it into the setpoint the drive follows -
and `MC_READACTVEL` reads the actual velocity back. The variables
`s1_en`, `s1_go` and `s1_rpm` are what the servo screen's buttons and
slider write; the program is there to be copied.

---

## The line shaft

![The line-shaft screen: the master's run and ramp, the gear switch, the compensated delay, the two registers live and at their peaks, and their trend](img/example-reterminal-ecat-line.webp){: .sb-center}

The same program gears the double's two axes to the single with
`MC_GEARIN` - ratio 1:1, the master's measured position every bus
cycle - and reads each follower's **register** (its actual position
against the master's, in increments; 65536 = one revolution) into a
variable, with a peak the RESET PEAKS button clears. `CO_RAMPTIME`
gives the master its ramp, so a run is a real profile: ramp up, hold,
ramp down. The *Line shaft* screen (the door on the servo screen) has
the master's run and ramp, the gear switch, the delay the followers
compensate, the two registers live and at their peaks, and a trend of
both.

What the bench measured with it, the master ramping to 300 rpm in 3 s,
the followers at 1:1:

| bus cycle | register in the hold, delay 0 | the delay that implies | register in the hold, delay set | peak during the ramp, delay 0 → set |
|---|---|---|---|---|
| 2 ms | −1479 inc | 4.5 ms | −6 inc | −1483 → −225 |
| 1 ms | −1058 inc | 3.2 ms | +8 inc | −1068 → −237 |
| 500 µs | −653 inc | 2.0 ms | −3 inc | −656 → −244 |
| 250 µs | −568 inc | 1.7 ms | −8 inc | −573 → −234 |

Without the compensation the register is the master's velocity times a
delay that grows with the cycle - 2 ms is 1.4 times 1 ms - which is the
error a press shows as colours running away during ramps. With the
delay set to the number the hold implies, the register in the hold is
within ten increments at every cycle time, and what remains during a
ramp is the followers' own loop under acceleration, the same ~230
increments whatever the cycle. The delay is found the way the table
shows: one run with the compensation off, the hold's register divided
by the velocity in increments per second.
The motors are real. The bench feeds the i700s single-phase from 230 V,
so their start-up writes set the rated mains voltage to 230 V
(`0x2540:1 = 0`; on a 400 V supply drop the line): with the 400 V
default the DC link of such a supply sits between the drive's
undervoltage error and its reset threshold, and every enable answers
the error 0x3220 while everything else looks healthy. The start-up
writes also carry the **motor**: the MCS06C60's catalogue row in the
drive's units (resistance, inductance, rated speed and frequency, power,
voltage, the back-EMF constant, the inertia, rated current and torque)
and the loops for it - the current controller's gain scaled to the
motor's inductance, the speed and position controller gains - because
an i700 keeps nothing at power-off. On the factory set (another motor
with four times the inductance) the axes turned but hunted at low speed;
with their own row every axis holds its setpoint within a few tens of
increments. The double inverter's second axis takes the same objects
0x800 higher. Another motor: its catalogue row in place of these lines.

---

## Worth copying

- **A bus is a section, a drive is an axis.** The program never knows
  which bus its axis rides; `MC_POWER` and `MC_MOVEVELOCITY` inside
  `DRIVE_i550` are the same blocks over CANopen and over EtherCAT - and
  the same blocks command a servo in csp.
- **Signals, not code.** A byte range of a slave's image, a variable,
  a gain — that is the whole of reading a drive's or a terminal's data.
- **Vendor and product in the slave.** With them the runtime refuses
  to run the line when the wrong device sits at that position, instead
  of writing a controlword into it.

How a line is put together, device by device:
[EtherCAT](ethercat.md).

---

## The same board, four buses

The reTerminal carries this project on all four, and the pages differ
only in how it talks to the machine:

- [the drive on CANopen](example-reterminal.md),
- [the drive on EtherCAT](example-reterminal-ecat.md),
- the same line with four drives: `reterminal_ecat_4x.prj32` in the
  examples (position on the line = axis number, a screen with a column
  per drive),
- [two slaves on an RS-485 pair](example-rs485.md),
- [a SIMATIC over ethernet](example-reterminal-s7.md).

---

*EtherCAT® is a registered trademark and patented technology, licensed by Beckhoff Automation GmbH, Germany.*
