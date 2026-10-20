---
title: Electronic line shaft
source: docs/tutorial-line-shaft.md
hero: img/lineshaft-jobs.webp
---

# An electronic line shaft: cylinders that follow the drum in register

A drum on its own velocity, servo cylinders geared to its measured position at a ratio and a phase, a register number that says how well they hold it, and jobs that carry the numbers - on a Linux device over EtherCAT.

## Who it is for
- Builders of printing presses and other lines with mechanically coupled shafts
- Integrators replacing a mechanical line shaft with servo drives
- Engineers who need measured, repeatable register rather than tuning by feel

## What you get
- Servos laid out from their description in cyclic position mode (csp), byte offsets and units shown
- Double inverters as two axes in one slave (A and B)
- Start-up writes per slave - motor data and loops - so a swapped spare drive gets its set at the next start
- A virtual master that follows the drum's measured position
- `MC_GearInPos`: rational ratio, defined position relation, register trim while running
- A measured chain-delay compensation that takes the register in the hold to a few increments
- Jobs as a recipe: speed, ratio and phase per cylinder; load, save, delete on the device; persisted across restarts, no homing needed
- `MC_TorqueFF` torque feed-forward for the inertia of a press cylinder
- A line screen with live and peak registers and their trend, and sync lamps

## How it works
1. *Add from library* on the EtherCAT line lays the servos out in cyclic position mode.
2. Make three axes: `servo1` on the single, `servo2a`/`servo2b` on the double.
3. `servo1` plays the drum: `MC_Power`, `CO_RAMPTIME`, `MC_MoveVelocity`; add a virtual master that follows its actual position.
4. Gear each follower in with `MC_GearInPos` (ratio, sync positions, velocity).
5. Measure the chain delay: Delay 0, constant speed, read the register, divide by the velocity in increments per second, enter it.
6. Keep jobs as a recipe and load them at standstill to re-gear the line.
7. Set the torque feed-forward gain on the press: raise until the register stops dipping at the start of a ramp, stop before overshoot.

## Pictures
- ![The Jobs screen: the jobs on the device, the job's speed, ratios and phases, and the followers' sync lamps](img/lineshaft-jobs.webp) - jobs on the device
- ![The slave window of a servo in cyclic position mode: the mode, the byte offsets of its words, the increments per revolution and the velocity unit](img/lineshaft-slave.webp) - the servo laid out from its description
- ![The window of the virtual master: no drive, the counter variable it follows and the counts of one revolution](img/lineshaft-vaxis.webp) - the axis everything derives from
- ![The line-shaft screen: the master's run and ramp, the gear switch, the compensated delay, the two registers live and at their peaks, and their trend](img/example-reterminal-ecat-line.webp) - the register is the one number the print sees

## Runs on
- A Linux device with a spare network port as EtherCAT master: the reTerminal with its E10-1 expansion
- Lenze i700 single and i700 double servo inverters in cyclic position mode; any CiA 402 servo with a cyclic position set works with its own description file

## Facts to keep exact
- Project: `examples\reterminal_ecat_example.prj32`
- Words read/written every cycle: target position, actual position, actual velocity, velocity offset, torque offset, torque limits, actual torque; plus increments per revolution and velocity units per rpm from the description
- The torque limits object travels beside the cyclic position PDO pair
- An i700 forgets its motor data and loops at power-off - they are start-up writes on the slave
- What makes a master or follower is the program, not the axis
- Followers gear to the drum's measured position, not its setpoint; the virtual master names the counter variable and counts of one revolution; it can instead run a profile of its own
- `MC_GearInPos` pins: `RatioNumerator`/`RatioDenominator` (whole numbers), `MasterSyncPosition`, `SlaveSyncPosition`, `Velocity`, `Delay` (seconds); outputs `InSync`, `Register` (0 = in register, follower's increments)
- Example ST: `gi2v(AXIS := 2, Execute := line_on AND line_src, Delay := line_tau2 / 1000.0, MasterSyncPosition := 0.0, SlaveSyncPosition := ph2, Master := 4, RatioNumerator := REAL_TO_INT(r2_num), RatioDenominator := REAL_TO_INT(r2_den), Velocity := 18.0);`
- `units_per_rev` 65536, `velocity_per: rpm`; gear-in velocity 18 rpm, shortest way into the relation
- A changed SlaveSyncPosition while Execute holds is a further move (register trim); a changed ratio applies when the line stands still
- Delay: 300 rpm = 327 680 increments per second at 65 536 per revolution; 1 000 increments behind at 300 rpm is 3 ms; not a tuning matter, no bus cycle removes it; re-measure after any loop change
- Recipe named `job`: master setpoint, each follower's ratio numerator/denominator, phase in increments
- Bench jobs: A = 300 rpm, both followers 1:1, phases 0; B = 200 rpm, followers 1:2 and 3:2, phases 20 000 and 40 000; loading B at standstill moved the followers into phase, the next run held 101 and 305 rpm in sync; after a runtime restart the gear-in was in sync at once with no movement
- Drive positions are absolute; nothing has to be homed
- Feed-forward: gain times the setpoint's acceleration, written as torque offset every cycle, one gain for both followers; on a bare motor the inertia torque is under one per cent, so it stays 0 on the bench
- A register peak at the start of a ramp is the drive's loop taking up the breakaway; the drive's position controller gain is the lever
- Device page: `ecat=` with master up and every slave operational; a working-counter error is a slave gone
- Related blocks: `MC_GearIn`, `MC_GearInPos`, `MC_PhasingAbsolute`, the torque blocks
- The trademark notice, word for word, on the page: *EtherCAT® is a registered trademark and patented technology, licensed by Beckhoff Automation GmbH, Germany.*

## Call to action
Download the editor and open `examples\reterminal_ecat_example.prj32`.
