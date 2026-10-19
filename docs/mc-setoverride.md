---
image: img/blk-mcovr-ld.webp
image_alt: "MC_SetOverride on a rung of a ladder program"
---

# MC_SetOverride

The operator's "slower, please" - scales every command.

![MC_SetOverride on a rung](img/blk-mcovr-ld.webp){: .sb-center}

![MC_SetOverride on a WEBview screen](img/blk-mcovr-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_SetOverride_ST
VAR mcovr : MC_SetOverride; END_VAR
  mcovr(AXIS := 0, Enable := mcovr_enable,
        VelFactor := mcovr_velfactor,
        AccFactor := mcovr_accfactor,
        JerkFactor := mcovr_jerkfactor);
  mcovr_enabled_st := mcovr.Enabled;
  mcovr_busy_st := mcovr.Busy;
  mcovr_error_st := mcovr.Error;
  mcovr_errorid_st := mcovr.ErrorID;
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
| `Enable` | input | bool | - | the factors apply while TRUE |
| `VelFactor` | parameter | number | 1 | 0 to 1: the factor every running and coming command's velocity is scaled by |
| `AccFactor` | parameter | number | 1 | 0 to 1: the same for the acceleration and the deceleration |
| `JerkFactor` | parameter | number | 1 | 0 to 1: the same for the jerk |
| `Enabled` | output | bool | - | the block holds its setting |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](blocks-motion.md));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |

## Description

While `Enable` holds, every running and every coming command is scaled by the three
factors: a potentiometer or a setpoint screen on `VelFactor` slows the whole
program's motion without touching a command. A factor of 0 stops the axis where its
ramp allows; 1 is the program's own numbers.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
