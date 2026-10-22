---
title: "Motion, turning the axis on: MC_Reset"
slug: mc-reset
section: "Function blocks"
order: 92
sidebar_position: 92
image: img/blk-mcrst-ld.webp
image_alt: "MC_Reset on a rung of a ladder program"
generator: tools/docs_export.py
---

# MC_Reset

Acknowledges the axis fault - ErrorStop goes back to Standstill.

![MC_Reset on a rung](img/blk-mcrst-ld.webp){: .sb-center}

![MC_Reset on a WEBview screen](img/blk-mcrst-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_Reset_ST
VAR mcrst : MC_Reset; END_VAR
  mcrst(AXIS := 0, Execute := mcrst_execute);
  mcrst_done_st := mcrst.Done;
  mcrst_busy_st := mcrst.Busy;
  mcrst_error_st := mcrst.Error;
  mcrst_errorid_st := mcrst.ErrorID;
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
| `Execute` | input | bool | - | acknowledges the axis fault on the rising edge |
| `Done` | output | bool | - | the command reached its goal |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |

A project written before this library used the name `MC_RESET` for it; the old name
opens and builds as an alias.

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](/docs/blocks/blocks-motion/));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |
| 15 | the command buffer is full |

## Description

Fault acknowledge on the rising edge of `Execute`: the axis leaves ErrorStop for
Standstill while it is powered, for Disabled when it is not, and the drive's own
fault is reset with it. If the axis stays in ErrorStop the cause is still present -
a reset does not clear a fault that is still happening. `MC_ReadAxisError` carries
the drive's code.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](/docs/blocks/blocks-motion/).
