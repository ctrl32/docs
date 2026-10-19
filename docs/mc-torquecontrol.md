---
image: img/blk-mctrq-ld.webp
image_alt: "MC_TorqueControl on a rung of a ladder program"
---

# MC_TorqueControl

Commands the torque itself, with a speed the drive limits itself to.

![MC_TorqueControl on a rung](img/blk-mctrq-ld.webp){: .sb-center}

![MC_TorqueControl on a WEBview screen](img/blk-mctrq-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_TorqueControl_ST
VAR mctrq : MC_TorqueControl; END_VAR
  mctrq(AXIS := 0, Execute := mctrq_execute,
        Torque := mctrq_torque,
        ContinuousUpdate := mctrq_continuousupdate,
        TorqueRamp := mctrq_torqueramp,
        Velocity := mctrq_velocity,
        Acceleration := mctrq_acceleration,
        Deceleration := mctrq_deceleration, Jerk := mctrq_jerk,
        Direction := mctrq_direction,
        BufferMode := mctrq_buffermode);
  mctrq_intorque_st := mctrq.InTorque;
  mctrq_busy_st := mctrq.Busy;
  mctrq_active_st := mctrq.Active;
  mctrq_commandaborted_st := mctrq.CommandAborted;
  mctrq_error_st := mctrq.Error;
  mctrq_errorid_st := mctrq.ErrorID;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|
| yes | yes | yes | - |

**Needs:** a servo declared in cyclic synchronous torque mode (cst) on its slave - a servo in position mode, a frequency drive or the simulation answers ErrorID 8.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | starts the command on the rising edge; the outputs hold while it is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
| `Torque` | input | number | - | the torque to hold, in per cent of the rated torque |
| `ContinuousUpdate` | parameter | bool | FALSE | a changed input is taken at once while `Execute` holds |
| `TorqueRamp` | parameter | number | 0 | the torque ramp, in per cent of the rated torque per second; 0 = at once |
| `Velocity` | parameter | number | 0 | the speed the drive limits itself to while it holds the torque; 0 = the axis's limit |
| `Acceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Deceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Jerk` | parameter | number | 0 | the jerk limit, in acceleration units per second; 0 = none (a trapezoid) |
| `Direction` | parameter | `MC_Direction` | `mcPositiveDirection` | `mcPositiveDirection` 1, `mcNegativeDirection` 3 |
| `BufferMode` | parameter | `MC_BufferMode` | `mcAborting` | what the command does to the one running: `mcAborting` 0 takes the axis at once, `mcBuffered` 1 waits for the running one to finish, `mcBlendingLow` 2, `mcBlendingPrevious` 3, `mcBlendingNext` 4, `mcBlendingHigh` 5 join the two moves at that velocity |
| `InTorque` | output | bool | - | the actual torque is within 5 % of the command |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Active` | output | bool | - | this command moves the axis now (a buffered one waits with `Busy` alone) |
| `CommandAborted` | output | bool | - | another command took the axis, or the axis was stopped |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |

A project written before this library used the name `MC_TORQUECONTROL` for it; the old name
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
| 8 | this drive cannot do it |
| 11 | the drive reports a fault (`MC_ReadAxisError` carries its code) |
| 12 | the target is past a software limit, or a moving axis reached one |
| 13 | the following error passed its limit |
| 15 | the command buffer is full |

## Description

A servo in **cyclic synchronous torque** mode is given `Torque` per cent of its
rated torque while `Execute` holds, ramped at `TorqueRamp`, and the drive limits its
speed to `Velocity` - an unloaded motor in torque control runs away to that limit,
so the limit is not optional. `InTorque` once the actual torque is within 5 % of
the command; the axis is in ContinuousMotion while the torque is held.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
