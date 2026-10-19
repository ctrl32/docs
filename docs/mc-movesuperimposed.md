---
image: img/blk-mcsup-ld.webp
image_alt: "MC_MoveSuperimposed on a rung of a ladder program"
---

# MC_MoveSuperimposed

A move on top of whatever the axis is doing.

![MC_MoveSuperimposed on a rung](img/blk-mcsup-ld.webp){: .sb-center}

![MC_MoveSuperimposed on a WEBview screen](img/blk-mcsup-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_MoveSuperimposed_ST
VAR mcsup : MC_MoveSuperimposed; END_VAR
  mcsup(AXIS := 0, Execute := mcsup_execute,
        Distance := mcsup_distance,
        VelocityDiff := mcsup_velocitydiff,
        ContinuousUpdate := mcsup_continuousupdate,
        Acceleration := mcsup_acceleration,
        Deceleration := mcsup_deceleration, Jerk := mcsup_jerk);
  mcsup_done_st := mcsup.Done;
  mcsup_busy_st := mcsup.Busy;
  mcsup_active_st := mcsup.Active;
  mcsup_commandaborted_st := mcsup.CommandAborted;
  mcsup_error_st := mcsup.Error;
  mcsup_errorid_st := mcsup.ErrorID;
  mcsup_covereddistance_st := mcsup.CoveredDistance;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|
| yes | - | yes | - |

**Needs:** a servo the kernel feeds (cyclic position mode) - a drive with its own ramp engine answers ErrorID 8.

A board (ESP32) refuses the block at the build; a project for a Linux device
carries it. The STM32 runtime has no motion library.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | starts the command on the rising edge; the outputs hold while it is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
| `Distance` | input | number | - | added on top of the running command, in units |
| `VelocityDiff` | input | number | - | the velocity added on top of the running command's, in units per the time base |
| `ContinuousUpdate` | parameter | bool | FALSE | a changed input is taken at once while `Execute` holds |
| `Acceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Deceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Jerk` | parameter | number | 0 | the jerk limit, in acceleration units per second; 0 = none (a trapezoid) |
| `Done` | output | bool | - | the command reached its goal |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Active` | output | bool | - | this command moves the axis now (a buffered one waits with `Busy` alone) |
| `CommandAborted` | output | bool | - | another command took the axis, or the axis was stopped |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |
| `CoveredDistance` | output | number | - | how much of `Distance` was added so far, in units |

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

Rides **on top** of the running command: `Distance` at `VelocityDiff` more than the
running command's velocity, with its own ramps - a register correction while the web
runs, a trim while a conveyor keeps going. `CoveredDistance` reports what was added
so far; a second superimposed move takes over the first (`CommandAborted` on the
first). `MC_HaltSuperimposed` stops the superimposed part alone.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
