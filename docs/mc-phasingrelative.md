---
image: img/blk-mcphr-ld.webp
image_alt: "MC_PhasingRelative on a rung of a ladder program"
---

# MC_PhasingRelative

Shifts a geared follower by a further phase.

![MC_PhasingRelative on a rung](img/blk-mcphr-ld.webp){: .sb-center}

![MC_PhasingRelative on a WEBview screen](img/blk-mcphr-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_PhasingRelative_ST
VAR mcphr : MC_PhasingRelative; END_VAR
  mcphr(AXIS := 2, Execute := mcphr_execute,
        PhaseShift := mcphr_phaseshift,
        Velocity := mcphr_velocity,
        ContinuousUpdate := mcphr_continuousupdate,
        Acceleration := mcphr_acceleration,
        Deceleration := mcphr_deceleration, Jerk := mcphr_jerk,
        BufferMode := mcphr_buffermode);
  mcphr_done_st := mcphr.Done;
  mcphr_busy_st := mcphr.Busy;
  mcphr_active_st := mcphr.Active;
  mcphr_commandaborted_st := mcphr.CommandAborted;
  mcphr_error_st := mcphr.Error;
  mcphr_errorid_st := mcphr.ErrorID;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | STM32 | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|:---:|
| yes | - | - | yes | - |

**Needs:** a follower in gear (`MC_GearIn` / `MC_GearInPos`) - ErrorID 20 otherwise.

A board (ESP32) refuses the block at the build; a project for a Linux device
carries it. The STM32 runtime has no motion library.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | starts the command on the rising edge; the outputs hold while it is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
| `PhaseShift` | input | number | - | added to the shift the follower has, in the follower's units |
| `Velocity` | input | number | - | the speed the shift is moved at |
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

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](blocks-motion.md));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |
| 2 | the axis is not powered - `MC_Power` first |
| 3 | the axis is in ErrorStop - acknowledge with `MC_Reset` |
| 7 | an input makes no sense (a velocity of 0, a ratio of 0, a bit that does not exist) |
| 10 | the block is not on this runtime - a Linux block on a board |
| 11 | the drive reports a fault (`MC_ReadAxisError` carries its code) |
| 12 | the target is past a software limit, or a moving axis reached one |
| 13 | the following error passed its limit |
| 15 | the command buffer is full |
| 20 | the axis is not synchronised |

## Description

The same as `MC_PhasingAbsolute` with `PhaseShift` added to the shift the follower
has - the operator's "a little more" on a register correction screen.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
