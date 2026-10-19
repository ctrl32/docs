---
image: img/blk-mccsw-ld.webp
image_alt: "MC_DigitalCamSwitch on a rung of a ladder program"
---

# MC_DigitalCamSwitch

Up to 32 outputs switched by the axis position.

![MC_DigitalCamSwitch on a rung](img/blk-mccsw-ld.webp){: .sb-center}

![MC_DigitalCamSwitch on a WEBview screen](img/blk-mccsw-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_DigitalCamSwitch_ST
VAR mccsw : MC_DigitalCamSwitch; END_VAR
  mccsw(AXIS := 0, Enable := mccsw_enable,
        Switches := mccsw_switches,
        EnableMask := mccsw_enablemask,
        ValueSource := mccsw_valuesource);
  mccsw_inoperation_st := mccsw.InOperation;
  mccsw_busy_st := mccsw.Busy;
  mccsw_error_st := mccsw.Error;
  mccsw_errorid_st := mccsw.ErrorID;
  mccsw_outputs_st := mccsw.Outputs;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|
| yes | - | yes | yes |

**Needs:** any axis with a position.

A board (ESP32) refuses the block at the build; a project for a Linux device
carries it. The STM32 runtime has no motion library.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Enable` | input | bool | - | the switches run while TRUE |
| `Switches` | parameter | integer | 0 | the cam switch table - its number among the project's switch tables (the first is 0) |
| `EnableMask` | parameter | integer | -1 | which tracks are armed, a bit per output; -1 = all |
| `ValueSource` | parameter | `MC_Source` | `mcSetValue` | the position the switches follow: `mcCommandedValue` 0, `mcSetValue` 1, `mcActualValue` 2 |
| `InOperation` | output | bool | - | the switches run |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |
| `Outputs` | output | integer | - | the word of outputs - bit n is track n + 1 |

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](blocks-motion.md));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |
| 10 | the block is not on this runtime - a Linux block on a board |
| 16 | the table (cam, profile, cam switches) is missing or wrong |

## Description

Drives up to 32 outputs from the axis position: the `Switches` table of the project
(made on the Motion page) says which output is on between which positions, and
ahead of them by a time - a slow valve fires early by velocity × its on-lead and
closes late by velocity × its off-lag, so it is open when the position needs it.
`EnableMask` says which tracks are armed, `ValueSource` whether the set or the
measured position counts; on a modulo axis the windows wrap with it. `Outputs` is
the word, bit n for track n + 1, to wire to real outputs or to read in the program;
`InOperation` while it runs. A table that is missing or has no track answers
ErrorID 16.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
