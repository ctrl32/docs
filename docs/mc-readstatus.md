---
image: img/blk-mcstat-ld.webp
image_alt: "MC_ReadStatus on a rung of a ladder program"
---

# MC_ReadStatus

Which state the axis is in - exactly one of eight.

![MC_ReadStatus on a rung](img/blk-mcstat-ld.webp){: .sb-center}

![MC_ReadStatus on a WEBview screen](img/blk-mcstat-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_ReadStatus_ST
VAR mcstat : MC_ReadStatus; END_VAR
  mcstat(AXIS := 0, Enable := mcstat_enable);
  mcstat_valid_st := mcstat.Valid;
  mcstat_busy_st := mcstat.Busy;
  mcstat_error_st := mcstat.Error;
  mcstat_errorid_st := mcstat.ErrorID;
  mcstat_errorstop_st := mcstat.ErrorStop;
  mcstat_disabled_st := mcstat.Disabled;
  mcstat_stopping_st := mcstat.Stopping;
  mcstat_homing_st := mcstat.Homing;
  mcstat_standstill_st := mcstat.Standstill;
  mcstat_discretemotion_st := mcstat.DiscreteMotion;
  mcstat_continuousmotion_st := mcstat.ContinuousMotion;
  mcstat_synchronizedmotion_st := mcstat.SynchronizedMotion;
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
| `Valid` | output | bool | - | the values are good: the axis is bound and answers |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |
| `ErrorStop` | output | bool | - | the axis's state is ErrorStop |
| `Disabled` | output | bool | - | the axis's state is Disabled |
| `Stopping` | output | bool | - | the axis's state is Stopping |
| `Homing` | output | bool | - | the axis's state is Homing |
| `Standstill` | output | bool | - | the axis's state is Standstill |
| `DiscreteMotion` | output | bool | - | the axis's state is DiscreteMotion |
| `ContinuousMotion` | output | bool | - | the axis's state is ContinuousMotion |
| `SynchronizedMotion` | output | bool | - | the axis's state is SynchronizedMotion |

A project written before this library used the name `MC_READSTATUS` for it; the old name
opens and builds as an alias.

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](blocks-motion.md));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |

## Description

An axis is in exactly one state of Part 1's state machine, and this block says
which: Disabled, Standstill, Homing, DiscreteMotion, ContinuousMotion,
SynchronizedMotion, Stopping or ErrorStop. The state is what every motion command
is admitted against - a move in ErrorStop is refused with ErrorID 3, in Stopping
with 4 - so a sequence that reads it knows what the next command will do.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
