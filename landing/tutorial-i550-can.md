---
title: A drive over CAN
source: docs/tutorial-i550-can.md
hero: img/i550-wiring.webp
---

# Run a Lenze i550 over CANopen - from the wiring to the first turn of the motor

Enable, run at a setpoint, stop, reset a fault and read the actual speed from a panel on the CAN bus. The axis wizard creates the device, the process data and the variables in one step; five rungs and a browser screen do the rest.

## Who it is for
- Builders of conveyors, pumps and fans driven by frequency inverters
- Integrators commissioning Lenze i550 drives over CANopen
- PLC programmers who know PLCopen motion blocks and want them on a panel

## What you get
- A step-by-step bench procedure: wiring, DIP switches, project, wizard, program, screen, start
- The **CAN axis wizard**: one *Create* makes the CAN device with its PDO mapping and start-up SDOs, the axis, and nine named variables for the motion blocks
- Synchronous process data: sent after the SYNC the panel produces, so values arrive at a known moment in the cycle
- The i550 network-control start-up writes done for you - without them the drive ignores every controlword
- Five ladder rungs with PLCopen-style blocks: `MC_Power`, `MC_MoveVelocity`, `MC_Stop`, `MC_Reset`, `MC_ReadActualVelocity`
- A browser (WEBview) operator page on a board without a display; on a board with a display the same widgets go on an HMIview screen
- The desk refuses a CAN project with an axis but no PDO mapping - before it reaches the device
- ONLINE: the same rungs live in the editor - contacts, block pins and coils with their values
- Everything the wizard made stays editable; changing the node-ID moves the variables and the axis with it

## How it works
1. Wire the bus: CAN_H, CAN_L and the signal ground, terminated at both ends.
2. Set the drive's DIP bank: node 2, 500 kbit/s, terminator ON - then power-cycle the drive.
3. *New project*: pick the board, tick CAN / CANopen master and First program in LD (WEBview on for a board without a display).
4. Right-click **CANopen Master** -> *Add Axis (drive)*: name `axis1`, node 2, profile Lenze i550, speed - *Create*.
5. Draw five rungs in PLC_PRG, one per motion block, each driven by a wizard variable.
6. Place the buttons, lamps, input and value on the browser screen.
7. Download (F5), open the panel's page, press Enable, set a speed, press Run.

## Pictures
- ![The panel and the drive on one bus](img/i550-wiring.webp) - the panel and the i550 on one CAN bus
- ![The DIP bank set for node 2, 500 kbit/s, terminated](img/i550-dip.webp) - the drive's DIP bank
- ![The wizard with the board picked](img/newproj-board.webp) - the New project wizard
- ![The CAN axis wizard](img/axis-wizard.webp) - the CAN axis wizard
- ![The tree: the CAN device and the axis under CANopen Master](img/i550-tree.webp) - what the wizard created in the tree
- ![The PDO mapping the wizard made](img/i550-pdo.webp) - the PDO mapping
- ![The axis window](img/i550-axis.webp) - the axis window
- ![The five rungs](img/i550-ladder.webp) - the program: five rungs
- ![The browser screen](img/i550-web.webp) - the WEBview operator page

## Runs on
- Drive: **Lenze i550** with its CANopen control unit
- Panel: any board that carries CAN (a catalog board listing `CAN` among its buses, or your own module with a transceiver on the CAN pins); the page uses an **Olimex ESP32-EVB** (CAN transceiver on the board, no display)
- Bus: CANopen

## Facts to keep exact
- Project file `tutorials\i550_axis.prj32`
- Needed: a panel with CAN, the i550 with the CANopen control unit, its motor and mains, a twisted pair, two 120 Ω terminators (the drive has one on its DIP switch), the STO wiring, USB for the first download
- Wiring panel -> drive X216: `CAN_H` -> `CH`, `CAN_L` -> `CL`, `GND` -> `CG` (signal ground always, not optional)
- Terminate both ends: 120 Ω between CAN_H and CAN_L at the panel, the drive's `R` switch ON at the other end; middle drives `R` OFF; shield connected at one end; power the panel from its own supply, not a bench USB port
- STO is wired, not programmed: a stop over CAN is not a safety function and must never be the only one
- DIP bank: `R` = terminator; `64 32 16 8 4 2 1` = node address as the sum of ON switches (node 2: only `2` ON; all seven OFF = address from parameter 0x2301:001); `d c b a` = bit rate, `OFF ON OFF ON` = 500 kbit/s (all four OFF = rate from parameter 0x2301:002; a combination not in the table falls back to 500 kbit/s); switches are read at power-on
- Wizard fields: instance name `axis1`, CAN node `2`, profile `Lenze i550`, what the axis does `speed` (`positioning` adds the blocks and variables for going to a position), CAN device ticked, EDS preselected as the i550 file with the most objects, MC variables ticked, prefix empty for the first axis
- TPDO1 (drive transmits): statusword 0x6041, actual speed 0x6044, then actual current and torque; RPDO1 (drive receives): controlword 0x6040, speed setpoint 0x6042; both synchronous
- SDO parameters: velocity mode, and on the i550 the two entries that hand control to the network
- Axis: rated current and torque left at 0 (read from the drive at start); *Units per revolution* and *Feed constant* matter for positioning
- Nine wizard variables: `enable`, `run`, `stop`, `reset`, `speed`, `ready`, `fault`, `running`, `velocity`; add `stopped` and `cleared` (BOOL, the `Done` outputs of MC_Stop and MC_Reset) yourself
- Block pins: MC_Power `Error` -> `fault`; MC_MoveVelocity `Velocity` <- `speed`, `Direction` default `mcPositiveDirection`; MC_ReadActualVelocity `Velocity` -> `velocity`; MC_Stop = controlled stop along the drive's deceleration ramp; MC_Reset acknowledges a fault
- With one axis the blocks are assigned to it by themselves; with more, the block's sheet asks
- Screen: Enable (toggle), ready led, Run (toggle), running led, Stop (momentary), Reset (momentary), fault led, input `speed` 0 … 1500, value `velocity`
- Troubleshooting: node **OFFLINE** = bus/DIP/rate/terminator/CG/swapped wires/no power cycle; `CAN: NO CYCLE` = axis without a PDO-mapped device; ready but Run does nothing = drive not under network control; oscillation = drive ramps slower than the panel's profile, set the drive's ramps to minimum; Actual 0 = TPDO1 lacks 0x6044; panel restarting every few seconds = CAN transmit into a bus nobody acknowledges

## Call to action
Download the editor and open `tutorials\i550_axis.prj32`.
