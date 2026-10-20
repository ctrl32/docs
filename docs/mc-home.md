---
image: img/blk-mchome-ld.webp
image_alt: "MC_Home on a rung of a ladder program"
---

# MC_Home

The reference run - the axis learns its zero.

![MC_Home on a rung](img/blk-mchome-ld.webp){: .sb-center}

![MC_Home on a WEBview screen](img/blk-mchome-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_Home_ST
VAR mchome : MC_Home; END_VAR
  mchome(AXIS := 0, Execute := mchome_execute,
         Position := mchome_position,
         BufferMode := mchome_buffermode);
  mchome_done_st := mchome.Done;
  mchome_busy_st := mchome.Busy;
  mchome_active_st := mchome.Active;
  mchome_commandaborted_st := mchome.CommandAborted;
  mchome_error_st := mchome.Error;
  mchome_errorid_st := mchome.ErrorID;
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
| `Execute` | input | bool | - | starts the reference run on the rising edge |
| `Position` | input | number | - | the position the reference point gets, in units |
| `BufferMode` | parameter | `MC_BufferMode` | `mcAborting` | what the command does to the one running: `mcAborting` 0 takes the axis at once, `mcBuffered` 1 waits for the running one to finish, `mcBlendingLow` 2, `mcBlendingPrevious` 3, `mcBlendingNext` 4, `mcBlendingHigh` 5 join the two moves at that velocity |
| `Done` | output | bool | - | the command reached its goal |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Active` | output | bool | - | this command moves the axis now (a buffered one waits with `Busy` alone) |
| `CommandAborted` | output | bool | - | another command took the axis, or the axis was stopped |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |

A project written before this library used the name `MC_HOME` for it; the old name
opens and builds as an alias.

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](blocks-motion.md));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |
| 2 | the axis is not powered - `MC_Power` first |
| 3 | the axis is in ErrorStop - acknowledge with `MC_Reset` |
| 4 | the axis is stopping - an `MC_Stop` holds it |
| 5 | the axis is homing - only `MC_Stop` may interrupt it |
| 15 | the command buffer is full |
| 19 | the axis has to stand still for this |

## Description

Until this has completed, absolute positions mean nothing. On a frequency drive
with a position the run approaches the home switch at the axis's homing speed and,
where a local encoder gives a Z pulse, creeps to it; without one the switch edge
itself is the zero. A stepper chip runs its own homing. A servo with absolute
feedback is homed where it stands: the position it stands on IS `Position` from
now. The axis has to stand still (ErrorID 19) and only `MC_Stop` may interrupt a
homing run.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
