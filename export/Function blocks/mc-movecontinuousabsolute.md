---
title: "Motion, continuous and superimposed motion: MC_MoveContinuousAbsolute"
slug: mc-movecontinuousabsolute
section: "Function blocks"
order: 113
sidebar_position: 113
image: img/blk-mccabs-ld.webp
image_alt: "MC_MoveContinuousAbsolute on a rung of a ladder program"
generator: tools/docs_export.py
---

# MC_MoveContinuousAbsolute

Moves to a position and arrives at a velocity instead of standing still.

![MC_MoveContinuousAbsolute on a rung](img/blk-mccabs-ld.webp){: .sb-center}

![MC_MoveContinuousAbsolute on a WEBview screen](img/blk-mccabs-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_MoveContinuousAbsolute_ST
VAR mccabs : MC_MoveContinuousAbsolute; END_VAR
  mccabs(AXIS := 0, Execute := mccabs_execute,
         Position := mccabs_position,
         EndVelocity := mccabs_endvelocity,
         Velocity := mccabs_velocity,
         ContinuousUpdate := mccabs_continuousupdate,
         Acceleration := mccabs_acceleration,
         Deceleration := mccabs_deceleration,
         Jerk := mccabs_jerk, Direction := mccabs_direction,
         BufferMode := mccabs_buffermode);
  mccabs_inendvelocity_st := mccabs.InEndVelocity;
  mccabs_busy_st := mccabs.Busy;
  mccabs_active_st := mccabs.Active;
  mccabs_commandaborted_st := mccabs.CommandAborted;
  mccabs_error_st := mccabs.Error;
  mccabs_errorid_st := mccabs.ErrorID;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | STM32 | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|:---:|
| yes | - | - | yes | - |

**Needs:** a servo in cyclic position mode (csp) on EtherCAT with the distributed clock - a frequency drive answers ErrorID 8.

A board (ESP32) refuses the block at the build; a project for a Linux device
carries it. The STM32 runtime has no motion library.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | starts the command on the rising edge; the outputs hold while it is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
| `Position` | input | number | - | where to go, in units from the axis zero |
| `EndVelocity` | input | number | - | the velocity the axis arrives at the target with, in units per the time base |
| `Velocity` | input | number | - | the speed of the move, in units per the axis's time base - above 0 |
| `ContinuousUpdate` | parameter | bool | FALSE | a changed input is taken at once while `Execute` holds |
| `Acceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Deceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Jerk` | parameter | number | 0 | the jerk limit, in acceleration units per second; 0 = none (a trapezoid) |
| `Direction` | parameter | `MC_Direction` | `mcShortestWay` | on a modulo axis: `mcPositiveDirection` 1, `mcShortestWay` 2, `mcNegativeDirection` 3, `mcCurrentDirection` 4 |
| `BufferMode` | parameter | `MC_BufferMode` | `mcAborting` | what the command does to the one running: `mcAborting` 0 takes the axis at once, `mcBuffered` 1 waits for the running one to finish, `mcBlendingLow` 2, `mcBlendingPrevious` 3, `mcBlendingNext` 4, `mcBlendingHigh` 5 join the two moves at that velocity |
| `InEndVelocity` | output | bool | - | the target is reached at `EndVelocity` |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Active` | output | bool | - | this command moves the axis now (a buffered one waits with `Busy` alone) |
| `CommandAborted` | output | bool | - | another command took the axis, or the axis was stopped |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](/docs/blocks/blocks-motion/));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |
| 2 | the axis is not powered - `MC_Power` first |
| 3 | the axis is in ErrorStop - acknowledge with `MC_Reset` |
| 4 | the axis is stopping - an `MC_Stop` holds it |
| 5 | the axis is homing - only `MC_Stop` may interrupt it |
| 6 | the axis is not homed and the command needs an absolute position |
| 7 | an input makes no sense (a velocity of 0, a ratio of 0, a bit that does not exist) |
| 8 | this drive cannot do it |
| 10 | the block is not on this runtime - a Linux block on a board |
| 11 | the drive reports a fault (`MC_ReadAxisError` carries its code) |
| 12 | the target is past a software limit, or a moving axis reached one |
| 13 | the following error passed its limit |
| 15 | the command buffer is full |

## Description

Travels to `Position` and **arrives at `EndVelocity`** - the entry of a conveyor
section at line speed, a web brought up to the next unit's speed by the time it
reaches it. `InEndVelocity` once the end velocity is reached at the target; the
axis stays in ContinuousMotion at that velocity until something else takes it. The
profile is the kernel's, so the axis needs a servo it feeds positions to.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](/docs/blocks/blocks-motion/).
