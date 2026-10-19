---
image: img/blk-mcadd-ld.webp
image_alt: "MC_MoveAdditive on a rung of a ladder program"
---

# MC_MoveAdditive

Adds a distance to the target of the running move.

![MC_MoveAdditive on a rung](img/blk-mcadd-ld.webp){: .sb-center}

![MC_MoveAdditive on a WEBview screen](img/blk-mcadd-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_MoveAdditive_ST
VAR mcadd : MC_MoveAdditive; END_VAR
  mcadd(AXIS := 0, Execute := mcadd_execute,
        Distance := mcadd_distance, Velocity := mcadd_velocity,
        ContinuousUpdate := mcadd_continuousupdate,
        Acceleration := mcadd_acceleration,
        Deceleration := mcadd_deceleration, Jerk := mcadd_jerk,
        BufferMode := mcadd_buffermode);
  mcadd_done_st := mcadd.Done;
  mcadd_busy_st := mcadd.Busy;
  mcadd_active_st := mcadd.Active;
  mcadd_commandaborted_st := mcadd.CommandAborted;
  mcadd_error_st := mcadd.Error;
  mcadd_errorid_st := mcadd.ErrorID;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|
| yes | yes | yes | yes |

**Needs:** a drive with a position: a servo in cyclic position mode, a stepper chip with its own engine, or a frequency drive with a position - its own counter over the bus or an encoder on the board; a plain velocity axis answers ErrorID 8.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | starts the command on the rising edge; the outputs hold while it is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
| `Distance` | input | number | - | added to the target of the running move, in units |
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
| 11 | the drive reports a fault (`MC_ReadAxisError` carries its code) |
| 12 | the target is past a software limit, or a moving axis reached one |
| 13 | the following error passed its limit |
| 15 | the command buffer is full |

## Description

`Distance` is added to the **target of the running move**: a stack of additive moves
ends where their sum says, whatever the axis was doing when each arrived. With no
move running it behaves as `MC_MoveRelative`.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
