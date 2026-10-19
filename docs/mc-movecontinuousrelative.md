---
image: img/blk-mccrel-ld.webp
image_alt: "MC_MoveContinuousRelative on a rung of a ladder program"
---

# MC_MoveContinuousRelative

Moves a distance and arrives at a velocity.

![MC_MoveContinuousRelative on a rung](img/blk-mccrel-ld.webp){: .sb-center}

![MC_MoveContinuousRelative on a WEBview screen](img/blk-mccrel-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_MoveContinuousRelative_ST
VAR mccrel : MC_MoveContinuousRelative; END_VAR
  mccrel(AXIS := 0, Execute := mccrel_execute,
         Distance := mccrel_distance,
         EndVelocity := mccrel_endvelocity,
         Velocity := mccrel_velocity,
         ContinuousUpdate := mccrel_continuousupdate,
         Acceleration := mccrel_acceleration,
         Deceleration := mccrel_deceleration,
         Jerk := mccrel_jerk, BufferMode := mccrel_buffermode);
  mccrel_inendvelocity_st := mccrel.InEndVelocity;
  mccrel_busy_st := mccrel.Busy;
  mccrel_active_st := mccrel.Active;
  mccrel_commandaborted_st := mccrel.CommandAborted;
  mccrel_error_st := mccrel.Error;
  mccrel_errorid_st := mccrel.ErrorID;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|
| yes | - | yes | - |

**Needs:** a servo in cyclic position mode (csp) on EtherCAT with the distributed clock - a frequency drive answers ErrorID 8.

A board (ESP32) refuses the block at the build; a project for a Linux device
carries it. The STM32 runtime has no motion library.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | starts the command on the rising edge; the outputs hold while it is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
| `Distance` | input | number | - | how far from the commanded position, in units |
| `EndVelocity` | input | number | - | the velocity the axis arrives at the target with, in units per the time base |
| `Velocity` | input | number | - | the speed of the move, in units per the axis's time base - above 0 |
| `ContinuousUpdate` | parameter | bool | FALSE | a changed input is taken at once while `Execute` holds |
| `Acceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Deceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Jerk` | parameter | number | 0 | the jerk limit, in acceleration units per second; 0 = none (a trapezoid) |
| `BufferMode` | parameter | `MC_BufferMode` | `mcAborting` | what the command does to the one running: `mcAborting` 0 takes the axis at once, `mcBuffered` 1 waits for the running one to finish, `mcBlendingLow` 2, `mcBlendingPrevious` 3, `mcBlendingNext` 4, `mcBlendingHigh` 5 join the two moves at that velocity |
| `InEndVelocity` | output | bool | - | the target is reached at `EndVelocity` |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Active` | output | bool | - | this command moves the axis now (a buffered one waits with `Busy` alone) |
| `CommandAborted` | output | bool | - | another command took the axis, or the axis was stopped |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](blocks-motion.md));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |
| 2 | the axis is not powered - `MC_Power` first |
| 3 | the axis is in ErrorStop - acknowledge with `MC_Reset` |
| 4 | the axis is stopping - an `MC_Stop` holds it |
| 5 | the axis is homing - only `MC_Stop` may interrupt it |
| 7 | an input makes no sense (a velocity of 0, a ratio of 0, a bit that does not exist) |
| 8 | this drive cannot do it |
| 10 | the block is not on this runtime - a Linux block on a board |
| 11 | the drive reports a fault (`MC_ReadAxisError` carries its code) |
| 12 | the target is past a software limit, or a moving axis reached one |
| 13 | the following error passed its limit |
| 15 | the command buffer is full |

## Description

The same as `MC_MoveContinuousAbsolute` with `Distance` from the commanded position
instead of an absolute `Position`: `InEndVelocity` once the end velocity is reached
at the target, no homing required.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
