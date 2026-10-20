---
title: Drive control, Lenze i550
source: docs/example-i550.md
hero: img/example-i550-0.webp
---

# Drive a Lenze i550 over CANopen without a single line of communication code

A speed dial with START/STOP, a keypad setpoint, live current, torque, DC link and output frequency read from the drive's own objects, a trend and an alarm - on a 2.8" panel and mirrored to a phone.

## Who it is for
- Builders of equipment with frequency drives on CANopen
- Integrators commissioning Lenze i550 drives
- Anyone who wants drive diagnostics on a screen without writing polling code
- Teams that want a phone page for the operator beside the panel

## What you get
- The whole CiA 402 state machine inside one supplied block, `DRIVE_i550`
- The i550 added from the device list: its profile brings the PDO layout along
- The profile switches the drive from Lenze's own state machine to CiA 402 over SDO at startup - the drive reacts from the first command
- Drive diagnostics as plain variables: an object index and a gain, no logic
- A fault lamp and an alarm from one statusword bit (`drive_sw.3`)
- A speed setpoint that survives power cycles (one flag on the variable)
- START/STOP as one toggle button that always names the action it will take
- A WEBview phone page (360×640) served over Ethernet with DHCP + mDNS

## How it works
1. The i550 sits on the CAN bus as node 2 at 500 kbit/s; `axis1` binds it.
2. TPDO1 starts with the statusword and the actual speed (four bytes the state machine reads); everything after them is data for the diagnostics.
3. Four variables read the drive's objects straight from the PDOs (`source: canopen`, an index, a gain), each with a deadband so a standing motor does not repaint the screen.
4. The ladder has three rungs: a 1 Hz BLINK heartbeat, the `DRIVE_i550` composite over `axis1`, and `drive_sw.3` into `fault`.
5. The ramp times live in RAMPCFG, a one-block FBD program: `CO_RAMPTIME` writes `acc` and `dec` to the drive - it has no output pin, so it gets a small FBD program instead of a forced rung.
6. Four screens: Drive, Detail, Trend, Alarms - plus the phone page.

## Pictures
- ![The drive screen, online with a standing drive: the dial, START, the setpoint](img/example-i550-0.webp) - Drive screen from a running bench: dial, START/STOP, setpoint, three lamps (running, fault, heartbeat); shows the persisted 500 rpm
- ![The ladder: three rungs — heartbeat, the DRIVE_i550 composite, the fault bit](img/ladder-i550.webp) - The three-rung ladder program
- ![The detail screen from the live bench: DC link 314 V on a standing drive](img/example-i550-1.webp) - Detail screen, live: motor standing at 0.00 A, 0.0 Hz, DC link 314 V
- ![The alarm table in simulation: the drive fault raised](img/example-i550-3.webp) - Alarm table in simulation: without a drive the statusword reads -1 and the fault raises itself

## Runs on
- Olimex ESP32-EVB with a MOD-LCD2.8RTP, 240×320 portrait
- Lenze i550 on the CAN bus (node 2, 500 kbit/s) - or nothing: the screens run and the fault lamp is lit
- CANopen; WEBview over the EVB's Ethernet jack (deliberately no WiFi: a display and WiFi together is a memory tier the EVB does not carry)

## Facts to keep exact
- Safety: the drive starts ONLY after START is pressed - never as a side effect of downloading. Stopping over CANopen is NOT a safety function; an emergency stop belongs on the i550's STO terminals, hard-wired
- Node 2, 500 kbit/s; node address and bit rate are set by DIP switches on the drive
- The i550 ships with Lenze's own state machine active, not CiA 402; the profile switches the mode over SDO at startup (otherwise correct values in 0x6040 do nothing)
- Diagnostics table: `current` 0x6078 × 0.0016 (A); `torque` 0x6077 × 0.001177 (Nm); `dc_voltage` 0x6079 × 0.001 (V); `frequency` 0x2DDD × 0.1 (Hz)
- The drive publishes per mille of its RATED values: rated current 1.6 A gives 0.0016, rated torque 1.177 Nm gives 0.001177
- 0x2DDD is the actual output frequency; 0x2D87 is the setpoint after the ramp (looks correct until the load slips)
- Fault = CiA 402 statusword bit 3 (`drive_sw.3`)
- `DRIVE_i550` pins: `command` enables, `setpoint` is the speed, `direction` reverses; returns `running` and actual `speed`
- Setpoint keypad clamped to 0-1500 rpm; `persist: true`
- Trend: actual speed over the last 60 s, sampled every 250 ms, recorded in the board
- Alarm: the fault bit with 200 ms delay
- Phone page 360×640: actual-speed number with a bar, setpoint slider, START/STOP, reverse, four diagnostics, trend
- START/STOP button uses `text_on` (green START at rest, lit red STOP while running)
- Try: ramp times from the detail screen (re-ramps on next start, no download); add motor voltage 0x2D89 from TPDO2 with `gain: 0.1`; change the dial's `max` together with input clamp and trend `min`/`max`

## Call to action
Download the ctrl32 editor and open the shipped project `examples\i550_EVB.prj32`.
