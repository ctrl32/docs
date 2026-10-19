---
image: img/blk-mcrai-ld.webp
image_alt: "MC_ReadAxisInfo on a rung of a ladder program"
---

# MC_ReadAxisInfo

The switches, the drive's readiness, homed or not.

![MC_ReadAxisInfo on a rung](img/blk-mcrai-ld.webp){: .sb-center}

![MC_ReadAxisInfo on a WEBview screen](img/blk-mcrai-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_ReadAxisInfo_ST
VAR mcrai : MC_ReadAxisInfo; END_VAR
  mcrai(AXIS := 0, Enable := mcrai_enable);
  mcrai_valid_st := mcrai.Valid;
  mcrai_busy_st := mcrai.Busy;
  mcrai_error_st := mcrai.Error;
  mcrai_errorid_st := mcrai.ErrorID;
  mcrai_homeabsswitch_st := mcrai.HomeAbsSwitch;
  mcrai_limitswitchpos_st := mcrai.LimitSwitchPos;
  mcrai_limitswitchneg_st := mcrai.LimitSwitchNeg;
  mcrai_simulation_st := mcrai.Simulation;
  mcrai_communicationready_st := mcrai.CommunicationReady;
  mcrai_readyforpoweron_st := mcrai.ReadyForPowerOn;
  mcrai_poweron_st := mcrai.PowerOn;
  mcrai_ishomed_st := mcrai.IsHomed;
  mcrai_axiswarning_st := mcrai.AxisWarning;
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
| `HomeAbsSwitch` | output | bool | - | the home switch is on |
| `LimitSwitchPos` | output | bool | - | the positive limit switch is on |
| `LimitSwitchNeg` | output | bool | - | the negative limit switch is on |
| `Simulation` | output | bool | - | the axis is simulated - no drive |
| `CommunicationReady` | output | bool | - | the drive answers on the bus |
| `ReadyForPowerOn` | output | bool | - | the drive is ready to be switched on |
| `PowerOn` | output | bool | - | the drive is switched on |
| `IsHomed` | output | bool | - | the axis knows its zero |
| `AxisWarning` | output | bool | - | the drive reports a warning |

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](blocks-motion.md));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |

## Description

Nine facts about the axis: the home and the two limit switches, whether the axis is
simulated, whether the drive answers on the bus, is ready to be switched on and is
switched on, whether the axis is homed, and the drive's warning flag. The switches
come from the drive's inputs word where the cyclic set carries it.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
