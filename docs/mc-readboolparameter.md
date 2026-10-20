---
image: img/blk-mcrbpar-ld.webp
image_alt: "MC_ReadBoolParameter on a rung of a ladder program"
---

# MC_ReadBoolParameter

Reads one of the axis's flags by its Part 1 number.

![MC_ReadBoolParameter on a rung](img/blk-mcrbpar-ld.webp){: .sb-center}

![MC_ReadBoolParameter on a WEBview screen](img/blk-mcrbpar-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_ReadBoolParameter_ST
VAR mcrbpar : MC_ReadBoolParameter; END_VAR
  mcrbpar(AXIS := 0, Enable := mcrbpar_enable,
          ParameterNumber := mcrbpar_parameternumber);
  mcrbpar_valid_st := mcrbpar.Valid;
  mcrbpar_busy_st := mcrbpar.Busy;
  mcrbpar_error_st := mcrbpar.Error;
  mcrbpar_errorid_st := mcrbpar.ErrorID;
  mcrbpar_value_st := mcrbpar.Value;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | STM32 | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|:---:|
| yes | yes | - | yes | yes |

**Needs:** any drive - a servo, a frequency drive, a stepper chip, the virtual master, the simulation.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Enable` | input | bool | - | the block works while TRUE |
| `ParameterNumber` | parameter | integer | 4 | the Part 1 number: 1 commanded position, 2 and 3 the software limits, 4 and 5 the limits enabled, 6 lag monitoring, 7 the maximum lag, 8 and 9 the velocity limits, 10 actual and 11 commanded velocity, 12 to 17 the acceleration, deceleration and jerk limits; 1000 the chain delay, 1001 the modulo period |
| `Valid` | output | bool | - | the values are good: the axis is bound and answers |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |
| `Value` | output | bool | - | the parameter's value, as TRUE / FALSE |

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](blocks-motion.md));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |

## Description

The same table as `MC_ReadParameter`, read as TRUE / FALSE - the limits enabled (4,
5), the lag monitoring (6). A number that does not exist answers ErrorID 7.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
