---
title: "Motion, probes and digital words: MC_ReadDigitalOutput"
slug: mc-readdigitaloutput
section: "Function blocks"
order: 136
sidebar_position: 136
image: img/blk-mcrdo-ld.webp
image_alt: "MC_ReadDigitalOutput on a rung of a ladder program"
generator: tools/docs_export.py
---

# MC_ReadDigitalOutput

One bit of the drive's outputs word.

![MC_ReadDigitalOutput on a rung](img/blk-mcrdo-ld.webp){: .sb-center}

![MC_ReadDigitalOutput on a WEBview screen](img/blk-mcrdo-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_ReadDigitalOutput_ST
VAR mcrdo : MC_ReadDigitalOutput; END_VAR
  mcrdo(AXIS := 0, Enable := mcrdo_enable,
        Output := mcrdo_output,
        OutputNumber := mcrdo_outputnumber);
  mcrdo_valid_st := mcrdo.Valid;
  mcrdo_busy_st := mcrdo.Busy;
  mcrdo_error_st := mcrdo.Error;
  mcrdo_errorid_st := mcrdo.ErrorID;
  mcrdo_value_st := mcrdo.Value;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | STM32 | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|:---:|
| yes | yes | - | yes | - |

**Needs:** a drive whose cyclic set carries the outputs word (object 0x60FE); no shipped device description carries it yet, so every drive answers ErrorID 8 until one does.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Enable` | input | bool | - | the block works while TRUE |
| `Output` | parameter | integer | 0 | 0 = the drive's outputs word (CiA 402 object 0x60FE) |
| `OutputNumber` | parameter | integer | 0 | the bit of the word, 0 to 31 |
| `Valid` | output | bool | - | the values are good: the axis is bound and answers |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |
| `Value` | output | bool | - | the bit |

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](/docs/blocks/blocks-motion/));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |
| 7 | an input makes no sense (a velocity of 0, a ratio of 0, a bit that does not exist) |
| 8 | this drive cannot do it |

## Description

Reads back one bit of the drive's digital outputs word: `Output` 0 is the word
(CiA 402 object 0x60FE), `OutputNumber` the bit. `Valid` while the image carries
the word.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](/docs/blocks/blocks-motion/).
