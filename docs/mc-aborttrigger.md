---
image: img/blk-mcprbx-ld.webp
image_alt: "MC_AbortTrigger on a rung of a ladder program"
---

# MC_AbortTrigger

Disarms a touch probe.

![MC_AbortTrigger on a rung](img/blk-mcprbx-ld.webp){: .sb-center}

![MC_AbortTrigger on a WEBview screen](img/blk-mcprbx-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_AbortTrigger_ST
VAR mcprbx : MC_AbortTrigger; END_VAR
  mcprbx(AXIS := 0, Execute := mcprbx_execute,
         TriggerInput := mcprbx_triggerinput);
  mcprbx_done_st := mcprbx.Done;
  mcprbx_busy_st := mcprbx.Busy;
  mcprbx_error_st := mcprbx.Error;
  mcprbx_errorid_st := mcprbx.ErrorID;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|
| yes | - | yes | - |

**Needs:** the same drive as `MC_TouchProbe`.

A board (ESP32) refuses the block at the build; a project for a Linux device
carries it. The STM32 runtime has no motion library.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | disarms the probe `TriggerInput` names |
| `TriggerInput` | parameter | `MC_TriggerInput` | `mcProbe1Rising` | `mcProbe1Rising` 1, `mcProbe1Falling` 2, `mcProbe2Rising` 3, `mcProbe2Falling` 4 |
| `Done` | output | bool | - | the command reached its goal |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](blocks-motion.md));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |
| 10 | the block is not on this runtime - a Linux block on a board |
| 15 | the command buffer is full |

## Description

Disarms the probe `TriggerInput` names; the `MC_TouchProbe` waiting on it answers
`CommandAborted`. `Done` at once.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
