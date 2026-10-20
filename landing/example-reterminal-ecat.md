---
title: reTerminal on EtherCAT
source: docs/example-reterminal-ecat.md
hero: img/example-reterminal-ecat-0.webp
---

# EtherCAT drives, servos, a line shaft and code reading - on one Linux panel

Move a drive from CANopen to EtherCAT with a few lines, run three servo axes in cyclic position mode on a 1 ms distributed clock, gear them into a line shaft with measured delay compensation, keep printing jobs as recipes, and read QR codes, barcodes and DataMatrix from a camera.

## Who it is for
- Builders of printing presses and other multi-axis lines that need an electronic line shaft
- Integrators putting Lenze i550 and i700 drives on EtherCAT
- Teams moving a drive project from CANopen to EtherCAT
- Lines that must read labels and codes from a camera beside the motion

## What you get
- The same project as the CANopen reTerminal example - screens, RS-485 pair, device page, alarms - with the i550 on EtherCAT instead
- Slaves added from their ESI in the device library: *Add from library* fills identity, image sizes, CiA 402 layout and the error-code signal
- Vendor and product checked per slave: the wrong device at a position is refused instead of receiving a controlword
- Two Lenze i700 servo inverters (a single and a double) in cyclic position mode (csp) on the distributed clock at 1 ms
- A servo screen: three axes side by side with enable, run, setpoint, actual velocity, following error, torque, position, error code, and one trend of the three velocities at 50 ms
- An electronic line shaft (`MC_GearIn`, 1:1) with chain-delay compensation and live register readings with peaks
- A virtual master that follows the drum's measured position
- Printing jobs as a recipe (`job`): speed, ratio and phase per follower, applied through `MC_GearInPos`
- An acceleration feed-forward (`MC_TorqueFF`)
- A Codes screen reading QR, barcode and DataMatrix from the camera, with brightness, contrast and sharpen sliders

## How it works
1. The axis names the EtherCAT backend and the slave position: `backend: cia402_ecat, node: 3` - the i550 is the third slave after the two servos.
2. An `ethercat:` section describes the line: the cycle, each slave (vendor and product), image sizes, the SDO writes that put the drive under network control, and signals - which bytes of a slave's input image land in which variable, with a gain. The device setting `ecat=eth1` names the interface, written from the editor's board window.
3. The i550's `sdo_init` list maps current, torque, DC link and output frequency into its user-configurable process data object at every start, and declares the fixed receive object's assignment too, so a drive power-cycled during configuration is set right at the next start.
4. The `SERVO` program commands three axes with three lines each: `MC_Power`, `MC_MoveVelocity`, `MC_ReadActualVelocity`; the same program gears the double's axes to the single and `CO_RAMPTIME` gives the master its ramp.
5. The motor's catalogue row and its controller loops are start-up writes of each i700 slave, because an i700 keeps nothing at power-off.
6. Two vision programs: `prep` (every 100 ms: camera, Gamma, Stretch contrast, Sharpen bound to the sliders) and `codes` (every 400 ms: the same three blocks plus three Read code blocks: qr, barcode, datamatrix).
7. The program never knows which bus its axis rides: the blocks inside `DRIVE_i550` are the same over CANopen and EtherCAT, and the same blocks command a servo in csp.

## Pictures
- ![The drive screen with the i550 on EtherCAT: the same dial, current, torque, DC link and frequency from the mapped process data](img/example-reterminal-ecat-0.webp) - The i550 on EtherCAT: same screen, values from the mapped process data
- ![The drive screen: the dial, START with its confirmation, the values that travel over the line](img/rt-drive-ecat.webp) - Drive screen with START confirmation
- ![The servo screen: three axes side by side with enable, run, the setpoint, the actual velocity, the following error, the torque and the position, and one trend of the three velocities](img/example-reterminal-ecat-servo.webp) - Servo screen: three axes side by side, one velocity trend
- ![The line-shaft screen: the master's run and ramp, the gear switch, the compensated delay, the two registers live and at their peaks, and their trend](img/example-reterminal-ecat-line.webp) - Line shaft: run and ramp, gear switch, delay, registers live and at peaks
- ![The Codes screen: the camera's picture with a QR code and an EAN-13 label, the QR's text and the barcode's digits read off it, a lamp for each](img/example-reterminal-ecat-codes.webp) - Codes: a QR and an EAN-13 label read from the camera

## Runs on
- Seeed reTerminal (CM4) with the reTerminal E10-1 expansion
- EtherCAT on the E10-1's second network port (`ecat=eth1`): two Lenze i700 servo inverters (single and double) ahead of a Lenze i550 with its EtherCAT module
- The two RS-485 slaves of the RS-485 system on the RS-485 terminal
- A USB camera for the Codes screen
- Without hardware the screens run and the lamps stay dark; without the two i700s the master reports the missing slaves and the i550 alone does not run (remove the two slaves and their axes, or put the same drives on the line)
- Also shipped: `reterminal_ecat_4x.prj32` - the same line with four drives (position on the line = axis number, a screen with a column per drive)

## Facts to keep exact
- Safety: the drive starts ONLY after START is pressed and confirmed; stopping over EtherCAT is NOT a safety function - the emergency stop belongs on the i550's STO terminals, hard-wired
- i550 axis: `backend: cia402_ecat, node: 3`
- i550 TxPDO fixed part: statusword, actual velocity, error code; current, torque, DC link, output frequency mapped into the user-configurable object at every start (assignment cleared first, mapping written, then assignment set to both objects)
- Line: `cycle_us: 1000`, `dc: true`; the i550 does not use the distributed clock and stays synchronous to its process data
- i700 csp images: 17 bytes out (target position, velocity feed-forward, mode), 21 bytes in (actual velocity, actual position); double inverter: `stride_out: 17`, `stride_in: 21`, second axis `sub: 1`; its second axis takes the same objects 0x800 higher
- Three signals per servo axis: error code, actual position, following error
- Axes: `servo1` (single), `servo2a` and `servo2b` (double), virtual master `vm`
- SERVO code (per axis):
  `pw1(AXIS := 1, Enable := s1_en);`
  `mv1(AXIS := 1, Execute := s1_go, Velocity := s1_rpm);`
  `rd1(AXIS := 1, Enable := TRUE);`
  `s1_act := rd1.Velocity;`
- Register in increments; 65536 = one revolution; RESET PEAKS clears the peaks
- Measured chain delay: 2 ms cycle 4.5 ms (300 rpm); 1 ms cycle 3.0 / 3.1 / 3.0 ms (60 / 300 / 600 rpm); 500 µs cycle 2.3 ms; 250 µs cycle 1.7 ms (300 rpm) - roughly 1.2 ms plus 1.7 cycles, independent of speed
- Without compensation: -1058 increments at 300 rpm and -1993 at 600 rpm on 1 ms; 1.4 times as much on 2 ms
- Delay found by one run with compensation off: hold register / velocity in increments per second
- Ramp-start spike ~230 increments, the same at 20, 100, 300 and 600 rpm/s (not acceleration)
- Position controller gain 0x2980 (1 ms, 300 rpm in 3 s): 28.4 1/s → spike -225, ramp ±60, hold +60; 50 1/s → -137, ±100, +85; 80 1/s (the example's setting) → -17, -45..+126, +5..+110; 120 1/s accepted and worse (follower lagged half a millisecond more)
- Ships with 80 1/s and a delay of 2.8 ms; re-measure the delay after any loop change
- Bus stayed clean: no lost frame, no overrun, worst wake-up under 30 µs at 1 ms and 250 µs
- Virtual master table (1:1, 2.8 ms compensated): servo1 directly -100 / -99 inc at 300 rpm, -98 / -138 at 600 rpm, 0 after the stop; virtual master reading its encoder -37 / -65 at 300 rpm, -108 / -123 at 600 rpm, 0 after the stop
- A drum following velocity only ran 4 500 increments off its followers at 300 rpm and drifted with every stop - which is why the drum is measured (encoder on the drive's input B)
- Jobs: recipe `job` - master setpoint, followers' ratios as numerator/denominator, phases in increments of the follower's revolution; `MC_GearInPos`; a phase edited while running is a smooth move; a new ratio is applied when the line stands still; values persisted, positions absolute, nothing has to be homed; Load / Save / Delete on the selected row; two in-relation lamps
- `MC_TorqueFF`: one gain for both followers, 0 = off; stays 0 on the bench (bare motor inertia torque under a per cent even at 25 rev/s²); on a press the plate cylinder is the inertia - raise until the register stops dipping at ramp start, stop before overshoot
- i700s on 230 V single-phase: start-up write `0x2540:1 = 0` (drop it on a 400 V supply); with the 400 V default every enable answers error 0x3220
- Motor: MCS06C60 catalogue row (resistance, inductance, rated speed and frequency, power, voltage, back-EMF constant, inertia, rated current and torque) plus current controller gain scaled to the motor's inductance, speed and position controller gains; the factory set (a motor with four times the inductance) hunted at low speed
- Codes: text appears within half a second; Crop to the middle of the picture (search costs a quarter); right-hand picture is `prep.shp`; sliders neutral at 100, 0, 1; settings bound as `gamma: "@rd_gamma"`; kept over a restart
- Code variables: `qr_found`, `qr_text`, `qr_number`, `bar_found`, `bar_text`, `bar_kind`, `dm_found`, `dm_text`; text lands in a STRING variable (Linux devices only); empty *expect* = any code counts, a text there makes *match* say whether the code carries it
- Barcode kinds: EAN, UPC, Code 128, Code 39, ITF, Codabar, GS1 DataBar; Read code also knows pdf417, aztec and any (the *format* output names what it read)
- An EAN-13 value is read as its thirteen digits, as text
- Note: the original page gives `codes` as every 400 ms in one place and "the program runs every 500 ms" in another - check before publishing
- A barcode reads when it is about a fifth of the picture wide or more; vision runs on its own thread beside the PLC - an unread picture is dropped, never a cycle
- The trademark notice, word for word, on the page: *EtherCAT® is a registered trademark and patented technology, licensed by Beckhoff Automation GmbH, Germany.*

## Call to action
Download the ctrl32 editor and open the shipped project `examples\reterminal_ecat_example.prj32` - and `reterminal_ecat_4x.prj32` for four drives. A step-by-step tutorial, "The line shaft, step by step", walks from the first servo to the jobs.
