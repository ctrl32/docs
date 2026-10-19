---
image: img/blk-mcvel-ld.webp
image_alt: "MC_MoveVelocity on a rung of a ladder program"
---

# MC_MoveVelocity

Runs at a velocity, for as long as nothing else takes the axis.

![MC_MoveVelocity on a rung](img/blk-mcvel-ld.webp){: .sb-center}

![MC_MoveVelocity on a WEBview screen](img/blk-mcvel-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_MoveVelocity_ST
VAR mcvel : MC_MoveVelocity; END_VAR
  mcvel(AXIS := 0, Execute := mcvel_execute,
        Velocity := mcvel_velocity,
        ContinuousUpdate := mcvel_continuousupdate,
        Acceleration := mcvel_acceleration,
        Deceleration := mcvel_deceleration, Jerk := mcvel_jerk,
        Direction := mcvel_direction,
        BufferMode := mcvel_buffermode);
  mcvel_invelocity_st := mcvel.InVelocity;
  mcvel_busy_st := mcvel.Busy;
  mcvel_active_st := mcvel.Active;
  mcvel_commandaborted_st := mcvel.CommandAborted;
  mcvel_error_st := mcvel.Error;
  mcvel_errorid_st := mcvel.ErrorID;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|
| yes | yes | yes | yes |

**Needs:** any drive - a servo, a frequency drive, a stepper chip, the virtual master, the simulation.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | starts the command on the rising edge; the outputs hold while it is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
| `Velocity` | input | number | - | the speed of the move, in units per the axis's time base - above 0 |
| `ContinuousUpdate` | parameter | bool | FALSE | a changed input is taken at once while `Execute` holds |
| `Acceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Deceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Jerk` | parameter | number | 0 | the jerk limit, in acceleration units per second; 0 = none (a trapezoid) |
| `Direction` | parameter | `MC_Direction` | `mcPositiveDirection` | `mcPositiveDirection` 1, `mcNegativeDirection` 3, `mcCurrentDirection` 4 |
| `BufferMode` | parameter | `MC_BufferMode` | `mcAborting` | what the command does to the one running: `mcAborting` 0 takes the axis at once, `mcBuffered` 1 waits for the running one to finish, `mcBlendingLow` 2, `mcBlendingPrevious` 3, `mcBlendingNext` 4, `mcBlendingHigh` 5 join the two moves at that velocity |
| `InVelocity` | output | bool | - | the commanded velocity is reached (PLCopen judges the set value) |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Active` | output | bool | - | this command moves the axis now (a buffered one waits with `Busy` alone) |
| `CommandAborted` | output | bool | - | another command took the axis, or the axis was stopped |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |

A project written before this library used the name `MC_MOVEVELOCITY` for it; the old name
opens and builds as an alias.

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
| 11 | the drive reports a fault (`MC_ReadAxisError` carries its code) |
| 12 | the target is past a software limit, or a moving axis reached one |
| 13 | the following error passed its limit |
| 15 | the command buffer is full |

## Description

Ramps up to `Velocity` and holds it - a conveyor, a pump, a fan, anything that runs
at a speed rather than to a position. `Busy` and `Active` stay on after `Execute`
falls (the axis keeps turning); `InVelocity` falls with `Execute`. A direction
`MC_Power` did not permit is refused with ErrorID 7.

On a frequency drive the velocity goes to the drive as its setpoint and the drive's
own ramps apply on top of the block's; on a servo and on the simulation the ramp is
the block's alone.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
