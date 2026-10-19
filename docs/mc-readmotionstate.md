---
image: img/blk-mcrms-ld.webp
image_alt: "MC_ReadMotionState on a rung of a ladder program"
---

# MC_ReadMotionState

Is the axis accelerating, decelerating, at constant velocity, which way.

![MC_ReadMotionState on a rung](img/blk-mcrms-ld.webp){: .sb-center}

![MC_ReadMotionState on a WEBview screen](img/blk-mcrms-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_ReadMotionState_ST
VAR mcrms : MC_ReadMotionState; END_VAR
  mcrms(AXIS := 0, Enable := mcrms_enable,
        Source := mcrms_source);
  mcrms_valid_st := mcrms.Valid;
  mcrms_busy_st := mcrms.Busy;
  mcrms_error_st := mcrms.Error;
  mcrms_errorid_st := mcrms.ErrorID;
  mcrms_constantvelocity_st := mcrms.ConstantVelocity;
  mcrms_accelerating_st := mcrms.Accelerating;
  mcrms_decelerating_st := mcrms.Decelerating;
  mcrms_directionpositive_st := mcrms.DirectionPositive;
  mcrms_directionnegative_st := mcrms.DirectionNegative;
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
| `Enable` | input | bool | - | the block works while TRUE |
| `Source` | parameter | `MC_Source` | `mcSetValue` | the stream the state is judged from: `mcCommandedValue` 0, `mcSetValue` 1, `mcActualValue` 2 |
| `Valid` | output | bool | - | the values are good: the axis is bound and answers |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |
| `ConstantVelocity` | output | bool | - | the velocity is constant |
| `Accelerating` | output | bool | - | the velocity rises |
| `Decelerating` | output | bool | - | the velocity falls |
| `DirectionPositive` | output | bool | - | the axis moves in the positive direction |
| `DirectionNegative` | output | bool | - | the axis moves in the negative direction |

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](blocks-motion.md));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |

## Description

Five flags from the motion: constant velocity, accelerating, decelerating, and the
direction. `Source` picks the stream they are judged from - the set value of the
kernel (`mcSetValue`), or the measured one (`mcActualValue`), where the direction
comes from the measured velocity's sign and the acceleration still from the
kernel, because the acceleration of a measured signal is noise.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
