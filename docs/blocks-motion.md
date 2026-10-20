# Motion blocks

The motion library is **PLCopen Motion Control Part 1**, whole and with
the specification's own names, inputs and outputs: `MC_Power`,
`MC_MoveAbsolute`, `MC_GearIn` mean here exactly what they mean in any
other controller a programmer has met. Every block of Part 1 is in the
Toolbox and in Structured Text; the blocks that need a servo with its own
position loop, tables kept on the device or a probe input are marked
**Linux** below and run on the Linux runtime - a frequency drive over
CANopen on a board gets the rest.

Every block takes an **AXIS** at the call. Which axis is never guessed:
in [Structured Text](st-language.md) you write
`pwr(AXIS := 0, Enable := go);` and the compiler refuses a motion block
without it. A guessed axis is a moving axle.

The names a project used before this library - `MC_POWER`, `MC_MOVEABS`,
`MC_READACTVEL`, `Accel`, `RatioNum`... - stay as **aliases**: an older
project opens and builds; the one value whose meaning moved
(`MC_MOVEVELOCITY`'s `Direction`, a reverse flag before, a direction
number now) is translated when the project opens.

---

## The blocks

Every block has a page of its own: the block on a rung and on a WEBview
screen, its Structured Text, where it runs, its pins, the `ErrorID`s it
answers and what it does. The last two columns say whether a Linux device
and an ESP32 board build it - the STM32 runtime has no motion library.

<!-- mc-index: begin -->

### Turning the axis on

| Block | What it does | Linux | ESP32 |
|:---|:---|:---:|:---:|
| [MC_Power](mc-power.md) | Switches the axis on and off - the CiA 402 state machine, handled for you. | yes | yes |
| [MC_Reset](mc-reset.md) | Acknowledges the axis fault - ErrorStop goes back to Standstill. | yes | yes |
| [MC_ReadStatus](mc-readstatus.md) | Which state the axis is in - exactly one of eight. | yes | yes |
| [MC_ReadAxisError](mc-readaxiserror.md) | The drive's own error code. | yes | yes |

### Making it move

| Block | What it does | Linux | ESP32 |
|:---|:---|:---:|:---:|
| [MC_MoveVelocity](mc-movevelocity.md) | Runs at a velocity, for as long as nothing else takes the axis. | yes | yes |
| [MC_Halt](mc-halt.md) | A controlled stop that does not lock the axis. | yes | yes |
| [MC_Stop](mc-stop.md) | A controlled stop that holds the axis while Execute is TRUE. | yes | yes |
| [MC_MoveAbsolute](mc-moveabsolute.md) | Moves to a position measured from the axis zero. | yes | yes |
| [MC_MoveRelative](mc-moverelative.md) | Moves this far from the position commanded now. | yes | yes |
| [MC_MoveAdditive](mc-moveadditive.md) | Adds a distance to the target of the running move. | yes | yes |
| [MC_Home](mc-home.md) | The reference run - the axis learns its zero. | yes | yes |
| [MC_SetPosition](mc-setposition.md) | Moves the coordinate system, not the axis. | yes | yes |
| [MC_SetOverride](mc-setoverride.md) | The operator's "slower, please" - scales every command. | yes | yes |

### Reading the axis

| Block | What it does | Linux | ESP32 |
|:---|:---|:---:|:---:|
| [MC_ReadActualPosition](mc-readactualposition.md) | The measured position. | yes | yes |
| [MC_ReadActualVelocity](mc-readactualvelocity.md) | The measured velocity. | yes | yes |
| [MC_ReadActualTorque](mc-readactualtorque.md) | The measured torque of a servo. | yes | yes |
| [MC_ReadMotionState](mc-readmotionstate.md) | Is the axis accelerating, decelerating, at constant velocity, which way. | yes | yes |
| [MC_ReadAxisInfo](mc-readaxisinfo.md) | The switches, the drive's readiness, homed or not. | yes | yes |
| [MC_ReadParameter](mc-readparameter.md) | Reads one of the axis's numbers by its Part 1 number. | yes | yes |
| [MC_ReadBoolParameter](mc-readboolparameter.md) | Reads one of the axis's flags by its Part 1 number. | yes | yes |
| [MC_WriteParameter](mc-writeparameter.md) | Writes one of the axis's numbers while the program runs. | yes | yes |
| [MC_WriteBoolParameter](mc-writeboolparameter.md) | Writes one of the axis's flags while the program runs. | yes | yes |

### Continuous and superimposed motion

| Block | What it does | Linux | ESP32 |
|:---|:---|:---:|:---:|
| [MC_MoveContinuousAbsolute](mc-movecontinuousabsolute.md) | Moves to a position and arrives at a velocity instead of standing still. | yes | - |
| [MC_MoveContinuousRelative](mc-movecontinuousrelative.md) | Moves a distance and arrives at a velocity. | yes | - |
| [MC_MoveSuperimposed](mc-movesuperimposed.md) | A move on top of whatever the axis is doing. | yes | - |
| [MC_HaltSuperimposed](mc-haltsuperimposed.md) | Stops the superimposed part of the motion alone. | yes | - |

### Profiles and cams

| Block | What it does | Linux | ESP32 |
|:---|:---|:---:|:---:|
| [MC_PositionProfile](mc-positionprofile.md) | The axis follows a table of time against position. | yes | - |
| [MC_VelocityProfile](mc-velocityprofile.md) | The axis follows a table of time against velocity. | yes | - |
| [MC_AccelerationProfile](mc-accelerationprofile.md) | The axis follows a table of time against acceleration. | yes | - |
| [MC_CamTableSelect](mc-camtableselect.md) | Names the cam table MC_CamIn will ride. | yes | - |
| [MC_CamIn](mc-camin.md) | Couples the axis to a master through a cam table. | yes | - |
| [MC_CamOut](mc-camout.md) | Releases the follower from its cam where it stands. | yes | - |

### The line shaft

| Block | What it does | Linux | ESP32 |
|:---|:---|:---:|:---:|
| [MC_GearIn](mc-gearin.md) | Couples the axis to a master at a ratio - the line shaft. | yes | - |
| [MC_GearOut](mc-gearout.md) | Releases the follower from its gear where it stands. | yes | - |
| [MC_GearInPos](mc-gearinpos.md) | Gears in at a defined relation of the two positions. | yes | - |
| [MC_PhasingAbsolute](mc-phasingabsolute.md) | Shifts a geared follower against its master to a phase. | yes | - |
| [MC_PhasingRelative](mc-phasingrelative.md) | Shifts a geared follower by a further phase. | yes | - |
| [MC_CombineAxes](mc-combineaxes.md) | The follower is the sum or the difference of two masters. | yes | - |

### Torque

| Block | What it does | Linux | ESP32 |
|:---|:---|:---:|:---:|
| [MC_SetTorqueLimit](mc-settorquelimit.md) | Holds the drive's torque limits every bus cycle. | yes | yes |
| [MC_TorqueControl](mc-torquecontrol.md) | Commands the torque itself, with a speed the drive limits itself to. | yes | yes |
| [MC_TorqueFF](mc-torqueff.md) | The acceleration feed-forward of a servo in position mode. | yes | - |

### Probes and digital words

| Block | What it does | Linux | ESP32 |
|:---|:---|:---:|:---:|
| [MC_TouchProbe](mc-touchprobe.md) | Records the axis position at the edge of a probe input. | yes | - |
| [MC_AbortTrigger](mc-aborttrigger.md) | Disarms a touch probe. | yes | - |
| [MC_DigitalCamSwitch](mc-digitalcamswitch.md) | Up to 32 outputs switched by the axis position. | yes | - |
| [MC_ReadDigitalInput](mc-readdigitalinput.md) | One bit of the drive's inputs word. | yes | yes |
| [MC_ReadDigitalOutput](mc-readdigitaloutput.md) | One bit of the drive's outputs word. | yes | yes |
| [MC_WriteDigitalOutput](mc-writedigitaloutput.md) | Sets one bit of the drive's outputs word. | yes | yes |

<!-- mc-index: end -->

---

## What every block answers

Part 1 gives every block the same face, and the runtime keeps to its
timing rules:

| Pin | Meaning |
|:---|:---|
| `Execute` | the command starts on the **rising edge**; the outputs hold while `Execute` is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
| `Enable` | a level: the block works while TRUE and answers `Valid` while its values are good |
| `Done` / `InVelocity` / `InGear` / `InSync` | the command reached its goal |
| `Busy` | the block has taken the command and has not finished with it |
| `Active` | the command is the one moving the axis now (a buffered one waits with `Busy` and no `Active`) |
| `CommandAborted` | another command took the axis, or the axis was stopped |
| `Error`, `ErrorID` | the command failed, and why |

`ErrorID` is one table for the whole library; every block's page lists
the codes it can answer:

| ErrorID | Meaning |
|:---:|:---|
| 1 | the axis is not bound to a drive |
| 2 | the axis is not powered (`MC_Power` first) |
| 3 | the axis is in **ErrorStop** - acknowledge with `MC_Reset` |
| 4 | the axis is stopping (an `MC_Stop` holds it) |
| 5 | the axis is homing |
| 6 | the axis is not homed and the command needs an absolute position |
| 7 | an input is out of range (a negative velocity, a direction that does not exist, a zero ratio) |
| 8 | this drive cannot do it (a position move on a drive with no position feedback, a torque command on a frequency drive) |
| 9 | the master axis is invalid |
| 10 | the block is not on this runtime (a Linux block on a board) |
| 11 | the drive reports a fault |
| 12 | the target is past a software limit |
| 13 | the following error exceeded its limit |
| 14 | the bus to the drive is down |
| 15 | the command buffer is full |
| 16 | the table (cam, profile, cam switches) is missing or wrong |
| 17 | the drive is in the wrong mode for the command |
| 18 | the parameter is read-only |
| 19 | the axis has to stand still for this |
| 20 | the axis is not synchronised |

A command **buffer mode** decides what a new command does to the one
running: `mcAborting` (the default) takes the axis at once, `mcBuffered`
waits for the running one to finish, `mcBlendingLow` / `mcBlendingHigh`
/ `mcBlendingPrevious` / `mcBlendingNext` join the two moves at the
lower, higher, previous or next velocity. The names are constants in
Structured Text (`BufferMode := mcBuffered`).

---

## The axis

An axis is in exactly one state, and `MC_ReadStatus` tells which:

```
Disabled --MC_Power--> Standstill --move--> DiscreteMotion / ContinuousMotion
                           |                        |
                        MC_Home                  MC_Stop
                           |                        |
                        Homing                   Stopping --(Execute falls)--> Standstill
   any state --fault or limit--> ErrorStop --MC_Reset--> Standstill (or Disabled)
   a geared or cammed follower: SynchronizedMotion
```

`MC_Stop` is special: while its `Execute` holds, the axis stays in
**Stopping** and refuses every other motion command (ErrorID 4) - it is
the controlled stop of a sequence, not an emergency stop. `MC_Halt`
stops the same way but lets the next command take the axis at once.

### Units and time

The axis has **units** - revolutions, millimetres, degrees - and
`units_per_rev` says how many make one turn of the motor (1 = the axis
counts revolutions). Positions and distances are in units; velocities in
units per the axis's **time base**, per **minute** by default (a 1 unit =
1 revolution axis speaks rpm, as every older project did), per
**second** (PLCopen's u/s), or **rpm** - revolutions per minute whatever
the position unit, the natural pair for a servo whose positions are its
increments; accelerations and decelerations in that velocity unit **per
second**; jerk per second squared. A block's
`Acceleration` 0 takes the axis's **default ramp**; 0 everywhere means the
built-in 1000 rpm/s on a servo and the drive's own ramp on a frequency
drive.

The axis window's *Limits and defaults* holds the time base, the system
limits (velocity, acceleration, deceleration, jerk - every command is
capped by them), the default ramps, the **modulo** period of a rotary
axis, the **software limits** (a target past them is refused with
ErrorID 12, a moving axis stops at them and goes ErrorStop) and the
**following-error** limit. `MC_ReadParameter` reads them by their Part 1
numbers (1 commanded position, 2 and 3 the software limits, 4 the limits
enabled, 7 the following error, 8 the maximum velocity, 9 the commanded
velocity, 10 the actual velocity, 12 to 17 the acceleration, deceleration
and jerk limits), `MC_WriteParameter` moves the application limits while
the program runs.

### Reading the axis

Every reader takes `Enable` and answers `Valid`, `Busy`, `Error`,
`ErrorID` and its value. **`Valid` is the pin that matters.** It goes
FALSE when the value is stale - the drive has stopped answering, the bus
has dropped - and acting on a stale position is a fault that appears
once a month and nobody understands. Gate anything that uses the
position on `Valid`.

---

## The Motion page

**Linux.** The tables the motion blocks read are made on the **Motion**
page of a Linux device: right-click **Motion** in the device tree (it sits
beside Cameras and Vision) or use the buttons on the page.

![The Motion page with a cam table](img/motion-page.webp)

Three kinds of table live there, each in its own list:

| Kind | What it holds | How a block names it |
|---|---|---|
| **Cam** | master position to slave position, one point per line; **Periodic** makes the cam repeat every master turn | `CamTable 0`, `CamTable 1`, ... in `MC_CamTableSelect` |
| **Profile** | time in seconds to position, velocity or acceleration | `TimePosition 0`, `TimeVelocity 0`, `TimeAcceleration 0` in the profile blocks |
| **Cam switch table** | tracks: an output (1 to 32), the first and the last position it is on, an on lead and an off lag in milliseconds | `Switches 0` in `MC_DigitalCamSwitch` |

A table has a **Name** (one word of up to 31 characters, not taken by
another table of the kind) and the number the blocks use is its place in
its list - the first cam is 0. **Points** are typed one per line, x and y,
with x going up, two to 256 of them; **Apply points** checks and takes
them, and a line the page cannot read is named under the field. The
tracks of a switch table are a table of their own: **Add track**, edit the
cells, **Remove track**.

**Remove table** takes a table out; a block that named it answers
`ErrorID` 16 (the table is missing or wrong) until another table takes its
number. The tables travel in the project and with it to the device; a
device of another kind than Linux refuses them at the build.

---

## The line shaft

**Linux.** Followers geared to a master in position - the cylinders of
a press following its drum - are `MC_GearIn` (a ratio) and
`MC_GearInPos` (a ratio and a defined relation of the two positions),
on servos in cyclic position mode over [EtherCAT](ethercat.md). What
the followers gear to is not the master's setpoint but its **measured
position**: the drum's encoder, or the actual position of a servo
master, usually through a virtual master axis that follows that
counter (see [EtherCAT - a virtual master](ethercat.md#a-virtual-master)).

### Gearing in at a relation

`MC_GearInPos` takes a rational ratio (`RatioNumerator` /
`RatioDenominator`, whole numbers, so a 2 : 3 never drifts) and a
relation: when the master stands at `MasterSyncPosition`, the follower
stands at `SlaveSyncPosition`, in the axes' units. At gear-in the
follower moves the shortest way into the relation at `Velocity`, then
follows the master's position every bus cycle with the velocity
feed-forward.

- While `Execute` holds, a changed `SlaveSyncPosition` is a further,
  smooth move to the new relation - the operator's **register trim**.
- A changed ratio is applied the moment the line stands still.
- `InSync` is in gear and in the relation.
- `Register` is the follower's actual position against the master's
  through the ratio and the phase, in the follower's units; 0 is in
  register, negative is behind.

A ratio coming from a REAL setpoint on a screen is passed as a whole
number (`RatioNumerator := REAL_TO_INT(r_num)`). On a servo whose
`units_per_rev` is its increments (65536) and whose time base is `rpm`,
the phases are plain increments and every velocity is rpm.

The drives' positions are absolute: a ratio and a phase kept in
persisted variables - a [recipe](recipes.md) of speed, ratios and phases
is the natural form - bring the same relation back after a restart,
and the next gear-in finds it without homing and without a movement. A
set loaded at standstill re-gears the line: the ratios take effect and
each follower moves into its phase without a new gear-in.

### The chain delay

A follower made from a measured position lags it: the drive samples,
the bus carries, the runtime computes, the drive applies. The delay is a
property of the chain - the drives' input latch, their velocity filter
and loop, the bus's sampling and applying - not of the speed, and it
shrinks with the bus cycle (roughly 1.2 ms plus 1.7 cycles on the Lenze
i700: about 3 ms at a 1 ms cycle, 1.7 ms at 250 µs). Uncompensated, the
register is the velocity times that delay - about a thousand increments
at 300 rpm on a 1 ms cycle, and it grows with the speed: the error a
press shows as colours running away during ramps. No bus cycle is short
enough to remove it; it is compensated, through the gear blocks'
`Delay` input (seconds), and it is **measured, not estimated**:

1. Set `Delay` to 0, gear in, run the master at a constant speed.
2. Read `Register` in the hold - it is negative, the follower behind.
3. Divide it by the velocity in increments per second (300 rpm = 327 680
   increments per second at 65 536 per revolution): 1 000 increments
   behind at 300 rpm is 3 ms.
4. Enter it. The register in the hold goes to a few increments.

A screen with the register live and at its peak (with a reset for the
peak) and a trend of it makes the measurement a matter of reading two
numbers. The delay moves with the drives' loop settings - the number the
hold implies includes the follower's response - so it is **re-measured
after any loop change**.

### The ramps

With the delay in, what usually remains is a spike at the **start** of
every ramp: the follower's loop taking up the breakaway. It is the same
size whatever the acceleration, so an acceleration feed-forward does
not touch it; the drive's **position controller gain** is the lever (on
the Lenze servo inverters `0x2980`; raising it from the motor's own
figure of 28.4 1/s to 80 1/s took the spike from about 225 increments to
under 20). Higher is not always better - a gain the drive accepts can
still make the follower lag more - so raise it in steps and stop where
the spike stops shrinking. What is left, a few tens of increments that
differ from run to run, is the drives' speed loops, tuned on the real
line with its motors and loads.

`MC_TorqueFF` hands the drive the torque a ramp needs up front, a gain
times the acceleration the setpoint asks for, written as the drive's
torque offset every cycle (0 = off). On a bare motor the inertia torque
is under a per cent even at a hard ramp and no gain moves the register;
on a press the plate cylinder is the inertia. Raise the gain until the
register stops dipping at the start of a ramp, and stop before it
overshoots.

### What to watch

- **The register**, live and at its peak, and its trend - the one number
  the print sees. A peak at the start of a ramp is the loop taking up the
  breakaway (the position controller gain, above).
- **`InSync`** of each follower: off while a follower moves into its
  phase, off when it is out of gear.
- **The device page**: the EtherCAT master up with every slave
  operational, and the bus counters - a working-counter error is a
  slave gone.

---

## A frequency drive is not a servo

The reference target on CANopen is a **frequency drive** with no position
loop of its own: the board generates the profile and sends a speed
setpoint every cycle. That has consequences worth knowing before
promising anything.

**Position comes over the bus, and the bus takes time.** Sampling in the
drive, transfer over CAN and the PLC cycle add up to a real 15 to 30 ms.
At 500 mm/s that is 7 to 15 mm of travel you do not know about yet.

**Which is why the creep phase is mandatory.** `MC_MoveAbsolute` and
`MC_MoveRelative` on such a drive run on the ramp positioning engine: the
profile ramps down to the axis's **creep speed** before the target and
stops inside its **window**. At 20 mm/s a 20 ms delay is 0.4 mm; at
500 mm/s the same delay is 10 mm. The creep phase is not an
optimisation, it is what makes the accuracy possible.

**The position has to come from somewhere.** The axis names it in its
window: a **variable** that carries the drive's own counter over PDO
(*Position feedback* lists the project's integer variables; *Counter
increments per revolution* is that counter's resolution, so the axis
can speak its units while the engine counts increments), or a local
**encoder** on the board. An axis with neither is a velocity axis: a
position move answers Error 8, `MC_MoveVelocity`, `MC_Stop`, `MC_Halt`
and the readers work.

**Realistic repeatability is ±0.5 to 2 mm**, depending on the mechanics.
It is not a servo and it should not be sold as one.

!!! danger "Set the drive's own ramps to minimum where the program positions"
    The most common commissioning problem on this hardware: the drive has
    acceleration ramps configured *and* the program ramps the setpoint.
    The two disagree, and a positioning axis overshoots and oscillates.
    One place owns the profile - the program - so wind the drive's ramps
    down and leave them there. A velocity-only axis may keep the drive's
    ramps: there the program's default ramp is quicker and the drive's
    own decides.

!!! warning "Watch for stale position data"
    The axis's **position watchdog** stops the motion when no fresh
    position arrives within a few cycles. Positioning on a value that
    stopped arriving is the failure that shows up once a month and takes
    a week to find.

---

## Safety

Stopping over CANopen or EtherCAT is **not** a safety function. Neither
is `MC_Stop`, and neither is anything on this page.

- Limit switches belong **hard-wired** into the drive or onto inputs -
  the software limits are a supplement, not protection.
- A drive's **STO** terminals are what an emergency stop wires into.
- Define what happens on loss of the encoder, on a motion timeout, and
  on a deviation between commanded and actual speed. All three occur on
  real projects.

See [Intended use](intended-use.md).

---

## Setting the drive up

The i550 ships with **Lenze's own state machine active**, not CiA 402 -
the full story, and the DIP switches worth writing on the drawing, is in
[CANopen - drives](canopen.md). The startup block switches the mode over
SDO so a project built from the i550 profile never meets it.

The quickest road to a working axis is the **CAN axis wizard**:
right-click *CANopen Master* in the project tree and choose *Add Axis
(drive)*, or press the *CAN wizard...* button in an axis window. The wiring,
the drive's switches and what to check when it does not move are on
[CANopen](canopen.md).

![The CAN axis wizard](img/axis-wizard.webp){: .sb-center}

| Field | What it sets |
|:---|:---|
| **instance name** | the axis's name, one word; the motion blocks name the axis by it |
| **CAN node** | the drive's node-ID - the address on its DIP switches |
| **Profile** | the drive's profile (`Lenze i550`, ...) |
| **what the axis does** | `speed` (a conveyor, a pump, a fan) or `positioning`, which adds the blocks' variables for going to a position |
| **CAN device with the PDOs the runtime needs** | leave it ticked: without that device the cyclic exchange never starts |
| **EDS** | the drive's own file from the device library; the wizard preselects the matching file with the most objects |
| **variables for the MC blocks**, **prefix** | leave it ticked; the prefix stays empty for the first axis |

It makes three things in one step:

- the **CAN device** of that node with the two PDOs the runtime
  exchanges on every SYNC (TPDO1 statusword + speed, RPDO1 controlword +
  setpoint) and the start-up SDO writes (velocity mode; on the i550 the
  network-control pair that switches its own state machine off)
- the **variables the MC blocks bind to**: `enable`, `run`, `stop`,
  `reset`, `speed`, `ready`, `fault`, `running`, `velocity`; an axis
  that positions adds `move`, `home`, `target`, `position`, `done`
- the **axis** itself, opened in its window

The first axis gets single words; a second one gets its name as a
prefix (`feed_speed`), editable in the dialog. A variable that already
exists under that name is kept, never duplicated. Each variable carries
a comment naming the block pin it is for. What the wizard makes is an
ordinary project afterwards - every part can be changed by hand.

In the axis window, leave the **rated current** and **rated torque** at
0: the runtime reads them from the drive at start. *Units per
revolution* and *Feed constant* matter for positioning; a speed axis
runs in the drive's own units.

A speed axis needs five blocks, one per command:

| Block | Pins to bind | What it does |
|:---|:---|:---|
| `MC_Power` | `Enable`, `Status`, `Error` | enables the drive while `Enable` is TRUE; `Status` = the drive reports it is enabled |
| `MC_MoveVelocity` | `Execute`, `Velocity`, `InVelocity`; `Direction` at its default `mcPositiveDirection` | runs at the setpoint; `InVelocity` = the drive reached it |
| `MC_Stop` | `Execute`, `Done` | a controlled stop along the drive's deceleration ramp |
| `MC_Reset` | `Execute`, `Done` | acknowledges a drive fault |
| `MC_ReadActualVelocity` | `Enable`, `Velocity` | the measured speed, every cycle |

Every motion block names its axis. With one axis in the project a block
on a rung or in a diagram is assigned to it by itself; with more, the
block's sheet asks which. The build refuses a CAN project with an axis
and no device carrying a PDO mapping - at the desk, before anything is
deployed.

Ramp times written with `CO_RAMPTIME` (see [CANopen blocks](blocks-can.md))
are variables like any other: changed from a screen, they take effect
the next time the motor starts, with no new download.

See [CANopen blocks](blocks-can.md) for what talks to a drive directly,
[EtherCAT](ethercat.md) for the servos, and [Buses](buses.md) for the
wiring.
