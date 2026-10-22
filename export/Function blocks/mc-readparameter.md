---
title: "Motion, reading the axis: MC_ReadParameter"
slug: mc-readparameter
section: "Function blocks"
order: 109
sidebar_position: 109
image: img/blk-mcrpar-ld.webp
image_alt: "MC_ReadParameter on a rung of a ladder program"
generator: tools/docs_export.py
---

# MC_ReadParameter

Reads one of the axis's numbers by its Part 1 number.

![MC_ReadParameter on a rung](img/blk-mcrpar-ld.webp){: .sb-center}

![MC_ReadParameter on a WEBview screen](img/blk-mcrpar-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_ReadParameter_ST
VAR mcrpar : MC_ReadParameter; END_VAR
  mcrpar(AXIS := 0, Enable := mcrpar_enable,
         ParameterNumber := mcrpar_parameternumber);
  mcrpar_valid_st := mcrpar.Valid;
  mcrpar_busy_st := mcrpar.Busy;
  mcrpar_error_st := mcrpar.Error;
  mcrpar_errorid_st := mcrpar.ErrorID;
  mcrpar_value_st := mcrpar.Value;
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
| `ParameterNumber` | parameter | integer | 1 | the Part 1 number: 1 commanded position, 2 and 3 the software limits, 4 and 5 the limits enabled, 6 lag monitoring, 7 the maximum lag, 8 and 9 the velocity limits, 10 actual and 11 commanded velocity, 12 to 17 the acceleration, deceleration and jerk limits; 1000 the chain delay, 1001 the modulo period |
| `Valid` | output | bool | - | the values are good: the axis is bound and answers |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |
| `Value` | output | number | - | the parameter's value |

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](/docs/blocks/blocks-motion/));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |

## Description

`ParameterNumber` picks the value: the commanded position, the software limits, the
following-error limit, the velocity, acceleration, deceleration and jerk limits
(the system ones the axis window sets, the application ones a program may move),
the actual and the commanded velocity; 1000 is the chain delay of a geared
follower, 1001 the modulo period. A number that does not exist answers ErrorID 7.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](/docs/blocks/blocks-motion/).
