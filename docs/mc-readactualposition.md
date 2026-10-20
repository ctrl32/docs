---
image: img/blk-mcrpos-ld.webp
image_alt: "MC_ReadActualPosition on a rung of a ladder program"
---

# MC_ReadActualPosition

The measured position.

![MC_ReadActualPosition on a rung](img/blk-mcrpos-ld.webp){: .sb-center}

![MC_ReadActualPosition on a WEBview screen](img/blk-mcrpos-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_ReadActualPosition_ST
VAR mcrpos : MC_ReadActualPosition; END_VAR
  mcrpos(AXIS := 0, Enable := mcrpos_enable);
  mcrpos_valid_st := mcrpos.Valid;
  mcrpos_busy_st := mcrpos.Busy;
  mcrpos_error_st := mcrpos.Error;
  mcrpos_errorid_st := mcrpos.ErrorID;
  mcrpos_position_st := mcrpos.Position;
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
| `Valid` | output | bool | - | the values are good: the axis is bound and answers |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |
| `Position` | output | number | - | the measured position, in units from the zero |

A project written before this library used the name `MC_READACTPOS` for it; the old name
opens and builds as an alias.

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](blocks-motion.md));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |

## Description

`Position` is the drive's measured position, in units from the zero. **`Valid` is
the pin that matters**: it goes FALSE when the value is stale - the drive has
stopped answering, the bus has dropped (ErrorID 14) - and acting on a stale position
is a fault that appears once a month and nobody understands. Gate anything that
uses the position on `Valid`.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
