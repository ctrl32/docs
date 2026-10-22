---
title: "Motion, profiles and cams: MC_CamTableSelect"
slug: mc-camtableselect
section: "Function blocks"
order: 120
sidebar_position: 120
image: img/blk-mccts-ld.webp
image_alt: "MC_CamTableSelect on a rung of a ladder program"
generator: tools/docs_export.py
---

# MC_CamTableSelect

Names the cam table MC_CamIn will ride.

![MC_CamTableSelect on a rung](img/blk-mccts-ld.webp){: .sb-center}

![MC_CamTableSelect on a WEBview screen](img/blk-mccts-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_CamTableSelect_ST
VAR mccts : MC_CamTableSelect; END_VAR
  mccts(AXIS := 0, Execute := mccts_execute,
        Master := mccts_master, CamTable := mccts_camtable,
        Periodic := mccts_periodic,
        MasterAbsolute := mccts_masterabsolute,
        SlaveAbsolute := mccts_slaveabsolute);
  mccts_done_st := mccts.Done;
  mccts_busy_st := mccts.Busy;
  mccts_error_st := mccts.Error;
  mccts_errorid_st := mccts.ErrorID;
  mccts_camtableid_st := mccts.CamTableID;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | STM32 | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|:---:|
| yes | - | - | yes | yes |

**Needs:** any drive - a servo, a frequency drive, a stepper chip, the virtual master, the simulation.

A board (ESP32) refuses the block at the build; a project for a Linux device
carries it. The STM32 runtime has no motion library.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | starts the command on the rising edge; the outputs hold while it is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
| `Master` | parameter | integer | 0 | the master axis - its number on the Motion node (the first axis is 0) |
| `CamTable` | parameter | integer | 0 | the cam table - its number among the project's cam tables (the first is 0) |
| `Periodic` | parameter | bool | TRUE | the cam repeats every master period |
| `MasterAbsolute` | parameter | bool | TRUE | the table's master column is absolute (FALSE = relative to the master's position at gear-in) |
| `SlaveAbsolute` | parameter | bool | TRUE | the table's slave column is absolute |
| `Done` | output | bool | - | the command reached its goal |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |
| `CamTableID` | output | integer | - | the id `MC_CamIn` takes |

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](/docs/blocks/blocks-motion/));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |
| 10 | the block is not on this runtime - a Linux block on a board |
| 16 | the table (cam, profile, cam switches) is missing or wrong |

## Description

Picks a **cam** - a table of master position against follower position made on
the Motion page - by its number (`CamTable`), says whether it repeats every master
period (`Periodic`) and whether its two columns are absolute, and answers
`CamTableID` on `Done`; `MC_CamIn` takes that id. A table that is missing or has
fewer than two points answers ErrorID 16.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](/docs/blocks/blocks-motion/).
