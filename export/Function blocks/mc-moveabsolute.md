---
title: "Motion, making it move: MC_MoveAbsolute"
slug: mc-moveabsolute
section: "Function blocks"
order: 98
sidebar_position: 98
image: img/blk-mcabs-ld.webp
image_alt: "MC_MoveAbsolute on a rung of a ladder program"
generator: tools/docs_export.py
---

# MC_MoveAbsolute

Moves to a position measured from the axis zero.

![MC_MoveAbsolute on a rung](img/blk-mcabs-ld.webp){: .sb-center}

![MC_MoveAbsolute on a WEBview screen](img/blk-mcabs-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_MoveAbsolute_ST
VAR mcabs : MC_MoveAbsolute; END_VAR
  mcabs(AXIS := 0, Execute := mcabs_execute,
        Position := mcabs_position, Velocity := mcabs_velocity,
        ContinuousUpdate := mcabs_continuousupdate,
        Acceleration := mcabs_acceleration,
        Deceleration := mcabs_deceleration, Jerk := mcabs_jerk,
        Direction := mcabs_direction,
        BufferMode := mcabs_buffermode);
  mcabs_done_st := mcabs.Done;
  mcabs_busy_st := mcabs.Busy;
  mcabs_active_st := mcabs.Active;
  mcabs_commandaborted_st := mcabs.CommandAborted;
  mcabs_error_st := mcabs.Error;
  mcabs_errorid_st := mcabs.ErrorID;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | STM32 | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|:---:|
| yes | yes | - | yes | yes |

**Needs:** a drive with a position: a servo in cyclic position mode, a stepper chip with its own engine, or a frequency drive with a position - its own counter over the bus or an encoder on the board; a plain velocity axis answers ErrorID 8.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | starts the command on the rising edge; the outputs hold while it is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
| `Position` | input | number | - | where to go, in units from the axis zero |
| `Velocity` | input | number | - | the speed of the move, in units per the axis's time base - above 0 |
| `ContinuousUpdate` | parameter | bool | FALSE | a changed input is taken at once while `Execute` holds |
| `Acceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Deceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Jerk` | parameter | number | 0 | the jerk limit, in acceleration units per second; 0 = none (a trapezoid) |
| `Direction` | parameter | `MC_Direction` | `mcShortestWay` | on a modulo axis: `mcPositiveDirection` 1, `mcShortestWay` 2, `mcNegativeDirection` 3, `mcCurrentDirection` 4 |
| `BufferMode` | parameter | `MC_BufferMode` | `mcAborting` | what the command does to the one running: `mcAborting` 0 takes the axis at once, `mcBuffered` 1 waits for the running one to finish, `mcBlendingLow` 2, `mcBlendingPrevious` 3, `mcBlendingNext` 4, `mcBlendingHigh` 5 join the two moves at that velocity |
| `Done` | output | bool | - | the command reached its goal |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Active` | output | bool | - | this command moves the axis now (a buffered one waits with `Busy` alone) |
| `CommandAborted` | output | bool | - | another command took the axis, or the axis was stopped |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |

A project written before this library used the name `MC_MOVEABS` for it; the old name
opens and builds as an alias.

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
| 11 | the drive reports a fault (`MC_ReadAxisError` carries its code) |
| 12 | the target is past a software limit, or a moving axis reached one |
| 13 | the following error passed its limit |
| 15 | the command buffer is full |

## Description

Absolute: `Position` is measured from the axis zero, so the axis has to be
**homed** first (ErrorID 6 otherwise) - unless the drive's position is absolute,
as a servo's is. On a modulo axis `Direction` says which way round.

On a servo in cyclic position mode the kernel generates the profile and feeds the
drive a position every bus cycle. On a frequency drive with a position the move
runs on the ramp positioning engine: the profile ramps down to the axis's creep
speed before the target and stops inside its window - at 20 mm/s a 20 ms bus delay
is 0.4 mm, at 500 mm/s it would be 10 mm, which is why the creep phase is not an
optimisation. A target past an enabled software limit is refused with ErrorID 12
before anything moves.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](/docs/blocks/blocks-motion/).
