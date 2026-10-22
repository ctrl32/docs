---
title: "Motion, profiles and cams: MC_VelocityProfile"
slug: mc-velocityprofile
section: "Function blocks"
order: 118
sidebar_position: 118
image: img/blk-mcvpro-ld.webp
image_alt: "MC_VelocityProfile on a rung of a ladder program"
generator: tools/docs_export.py
---

# MC_VelocityProfile

The axis follows a table of time against velocity.

![MC_VelocityProfile on a rung](img/blk-mcvpro-ld.webp){: .sb-center}

![MC_VelocityProfile on a WEBview screen](img/blk-mcvpro-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_VelocityProfile_ST
VAR mcvpro : MC_VelocityProfile; END_VAR
  mcvpro(AXIS := 0, Execute := mcvpro_execute,
         TimeVelocity := mcvpro_timevelocity,
         ArraySize := mcvpro_arraysize,
         TimeScale := mcvpro_timescale,
         VelocityScale := mcvpro_velocityscale,
         Offset := mcvpro_offset,
         BufferMode := mcvpro_buffermode);
  mcvpro_done_st := mcvpro.Done;
  mcvpro_busy_st := mcvpro.Busy;
  mcvpro_active_st := mcvpro.Active;
  mcvpro_commandaborted_st := mcvpro.CommandAborted;
  mcvpro_error_st := mcvpro.Error;
  mcvpro_errorid_st := mcvpro.ErrorID;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | STM32 | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|:---:|
| yes | - | - | yes | - |

**Needs:** a servo the kernel feeds, or a velocity axis it runs - a drive with its own ramp engine answers ErrorID 8.

A board (ESP32) refuses the block at the build; a project for a Linux device
carries it. The STM32 runtime has no motion library.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | starts the command on the rising edge; the outputs hold while it is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
| `TimeVelocity` | parameter | integer | 0 | the profile table - its number among the project's profiles (the first is 0) |
| `ArraySize` | parameter | integer | 0 | how many points of the table to use; 0 = the whole table |
| `TimeScale` | parameter | number | 1 | the table's time multiplied by this |
| `VelocityScale` | parameter | number | 1 | the table's value multiplied by this |
| `Offset` | parameter | number | 0 | added to the table's value |
| `BufferMode` | parameter | `MC_BufferMode` | `mcAborting` | what the command does to the one running: `mcAborting` 0 takes the axis at once, `mcBuffered` 1 waits for the running one to finish, `mcBlendingLow` 2, `mcBlendingPrevious` 3, `mcBlendingNext` 4, `mcBlendingHigh` 5 join the two moves at that velocity |
| `Done` | output | bool | - | the command reached its goal |
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
| 8 | this drive cannot do it |
| 10 | the block is not on this runtime - a Linux block on a board |
| 11 | the drive reports a fault (`MC_ReadAxisError` carries its code) |
| 12 | the target is past a software limit, or a moving axis reached one |
| 13 | the following error passed its limit |
| 15 | the command buffer is full |
| 16 | the table (cam, profile, cam switches) is missing or wrong |

## Description

The same as `MC_PositionProfile` with the table holding velocities: `TimeVelocity`
names it, `VelocityScale` scales the value. The axis is in ContinuousMotion while
it follows and stays at the last velocity when the table ends.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](/docs/blocks/blocks-motion/).
