---
image: img/blk-mcrerr-ld.webp
image_alt: "MC_ReadAxisError on a rung of a ladder program"
---

# MC_ReadAxisError

The drive's own error code.

![MC_ReadAxisError on a rung](img/blk-mcrerr-ld.webp){: .sb-center}

![MC_ReadAxisError on a WEBview screen](img/blk-mcrerr-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_ReadAxisError_ST
VAR mcrerr : MC_ReadAxisError; END_VAR
  mcrerr(AXIS := 0, Enable := mcrerr_enable);
  mcrerr_valid_st := mcrerr.Valid;
  mcrerr_busy_st := mcrerr.Busy;
  mcrerr_error_st := mcrerr.Error;
  mcrerr_errorid_st := mcrerr.ErrorID;
  mcrerr_axiserrorid_st := mcrerr.AxisErrorID;
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
| `AxisErrorID` | output | integer | - | the drive's own error code - the CiA 402 error register, an EtherCAT slave's AL status |

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](blocks-motion.md));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |

## Description

`AxisErrorID` is the code of the drive itself: the CiA 402 error register of a
CANopen drive, the AL status of an EtherCAT slave. `ErrorID` 11 on any block says
"the drive reports a fault" - this block says which one, in the words of the
drive's manual.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
