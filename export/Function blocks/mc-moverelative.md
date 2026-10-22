---
title: "Motion, making it move: MC_MoveRelative"
slug: mc-moverelative
section: "Function blocks"
order: 99
sidebar_position: 99
image: img/blk-mcrel-ld.webp
image_alt: "MC_MoveRelative on a rung of a ladder program"
generator: tools/docs_export.py
---

# MC_MoveRelative

Moves this far from the position commanded now.

![MC_MoveRelative on a rung](img/blk-mcrel-ld.webp){: .sb-center}

![MC_MoveRelative on a WEBview screen](img/blk-mcrel-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_MoveRelative_ST
VAR mcrel : MC_MoveRelative; END_VAR
  mcrel(AXIS := 0, Execute := mcrel_execute,
        Distance := mcrel_distance, Velocity := mcrel_velocity,
        ContinuousUpdate := mcrel_continuousupdate,
        Acceleration := mcrel_acceleration,
        Deceleration := mcrel_deceleration, Jerk := mcrel_jerk,
        BufferMode := mcrel_buffermode);
  mcrel_done_st := mcrel.Done;
  mcrel_busy_st := mcrel.Busy;
  mcrel_active_st := mcrel.Active;
  mcrel_commandaborted_st := mcrel.CommandAborted;
  mcrel_error_st := mcrel.Error;
  mcrel_errorid_st := mcrel.ErrorID;
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
| `Distance` | input | number | - | how far from the commanded position, in units; negative = backwards |
| `Velocity` | input | number | - | the speed of the move, in units per the axis's time base - above 0 |
| `ContinuousUpdate` | parameter | bool | FALSE | a changed input is taken at once while `Execute` holds |
| `Acceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Deceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Jerk` | parameter | number | 0 | the jerk limit, in acceleration units per second; 0 = none (a trapezoid) |
| `BufferMode` | parameter | `MC_BufferMode` | `mcAborting` | what the command does to the one running: `mcAborting` 0 takes the axis at once, `mcBuffered` 1 waits for the running one to finish, `mcBlendingLow` 2, `mcBlendingPrevious` 3, `mcBlendingNext` 4, `mcBlendingHigh` 5 join the two moves at that velocity |
| `Done` | output | bool | - | the command reached its goal |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Active` | output | bool | - | this command moves the axis now (a buffered one waits with `Busy` alone) |
| `CommandAborted` | output | bool | - | another command took the axis, or the axis was stopped |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |

A project written before this library used the name `MC_MOVEREL` for it; the old name
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
| 7 | an input makes no sense (a velocity of 0, a ratio of 0, a bit that does not exist) |
| 8 | this drive cannot do it |
| 11 | the drive reports a fault (`MC_ReadAxisError` carries its code) |
| 12 | the target is past a software limit, or a moving axis reached one |
| 13 | the following error passed its limit |
| 15 | the command buffer is full |

## Description

Same as `MC_MoveAbsolute` with `Distance` instead of `Position`: move this far from
the setpoint the axis is at. No homing required; errors do not accumulate, because
every move starts from the commanded position, not from a measured one. A negative
`Distance` moves backwards.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](/docs/blocks/blocks-motion/).
