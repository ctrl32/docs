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
(drive)*, or press the *CAN wizard...* button in an axis window. The whole
road from the wiring to the first turn of the motor, with pictures, is
[A drive over CAN, step by step](tutorial-i550-can.md).

![The CAN axis wizard](img/axis-wizard.webp){: .sb-center}

It takes the axis name, the node-ID and the profile and makes three
things in one step:

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
exists under that name is kept, never duplicated. What the wizard makes
is an ordinary project afterwards - every part can be changed by hand.

See [CANopen blocks](blocks-can.md) for what talks to a drive directly,
[EtherCAT](ethercat.md) for the servos, and [Buses](buses.md) for the
wiring.
