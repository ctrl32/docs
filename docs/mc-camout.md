---
image: img/blk-mccamo-ld.webp
image_alt: "MC_CamOut on a rung of a ladder program"
---

# MC_CamOut

Releases the follower from its cam where it stands.

![MC_CamOut on a rung](img/blk-mccamo-ld.webp){: .sb-center}

![MC_CamOut on a WEBview screen](img/blk-mccamo-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_CamOut_ST
VAR mccamo : MC_CamOut; END_VAR
  mccamo(AXIS := 2, Execute := mccamo_execute);
  mccamo_done_st := mccamo.Done;
  mccamo_busy_st := mccamo.Busy;
  mccamo_error_st := mccamo.Error;
  mccamo_errorid_st := mccamo.ErrorID;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|
| yes | - | yes | - |

**Needs:** any drive - a servo, a frequency drive, a stepper chip, the virtual master, the simulation.

A board (ESP32) refuses the block at the build; a project for a Linux device
carries it. The STM32 runtime has no motion library.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | starts the command on the rising edge; the outputs hold while it is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
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
| 2 | the axis is not powered - `MC_Power` first |
| 3 | the axis is in ErrorStop - acknowledge with `MC_Reset` |
| 10 | the block is not on this runtime - a Linux block on a board |
| 15 | the command buffer is full |

## Description

The follower leaves the cam at the velocity it had and keeps it (ContinuousMotion)
until a command takes it - an `MC_Stop` or `MC_Halt` brings it to a stand. The
`MC_CamIn` that held it answers `CommandAborted`.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
