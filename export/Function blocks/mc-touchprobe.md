---
title: "Motion, probes and digital words: MC_TouchProbe"
slug: mc-touchprobe
section: "Function blocks"
order: 132
sidebar_position: 132
image: img/blk-mcprb-ld.webp
image_alt: "MC_TouchProbe on a rung of a ladder program"
generator: tools/docs_export.py
---

# MC_TouchProbe

Records the axis position at the edge of a probe input.

![MC_TouchProbe on a rung](img/blk-mcprb-ld.webp){: .sb-center}

![MC_TouchProbe on a WEBview screen](img/blk-mcprb-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_TouchProbe_ST
VAR mcprb : MC_TouchProbe; END_VAR
  mcprb(AXIS := 0, Execute := mcprb_execute,
        FirstPosition := mcprb_firstposition,
        LastPosition := mcprb_lastposition,
        TriggerInput := mcprb_triggerinput,
        WindowOnly := mcprb_windowonly);
  mcprb_done_st := mcprb.Done;
  mcprb_busy_st := mcprb.Busy;
  mcprb_error_st := mcprb.Error;
  mcprb_errorid_st := mcprb.ErrorID;
  mcprb_recordedposition_st := mcprb.RecordedPosition;
  mcprb_commandaborted_st := mcprb.CommandAborted;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | STM32 | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|:---:|
| yes | - | - | yes | - |

**Needs:** a servo whose cyclic set carries the touch-probe words (objects 0x60B8 to 0x60BD); no shipped device description carries them yet, so every drive answers ErrorID 8 until one does.

A board (ESP32) refuses the block at the build; a project for a Linux device
carries it. The STM32 runtime has no motion library.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | arms the probe on the rising edge |
| `FirstPosition` | input | number | - | the start of the window, in units |
| `LastPosition` | input | number | - | the end of the window, in units |
| `TriggerInput` | parameter | `MC_TriggerInput` | `mcProbe1Rising` | `mcProbe1Rising` 1, `mcProbe1Falling` 2, `mcProbe2Rising` 3, `mcProbe2Falling` 4 |
| `WindowOnly` | parameter | bool | FALSE | TRUE = only an edge between `FirstPosition` and `LastPosition` counts; the probe is re-armed otherwise |
| `Done` | output | bool | - | the command reached its goal |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |
| `RecordedPosition` | output | number | - | the axis position at the edge, in units |
| `CommandAborted` | output | bool | - | another command took the axis, or the axis was stopped |

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](/docs/blocks/blocks-motion/));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |
| 8 | this drive cannot do it |
| 10 | the block is not on this runtime - a Linux block on a board |
| 15 | the command buffer is full |

## Description

Arms the drive's touch probe on the rising edge of `Execute` - `TriggerInput` names
probe 1 or 2 and the rising or the falling edge - and answers `RecordedPosition`
(the axis's units) with `Done` when the edge came; with `WindowOnly` only an edge
between `FirstPosition` and `LastPosition` counts and the probe is re-armed
otherwise. `MC_AbortTrigger` disarms it (`CommandAborted`).

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](/docs/blocks/blocks-motion/).
