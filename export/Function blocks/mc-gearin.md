---
title: "Motion, the line shaft: MC_GearIn"
slug: mc-gearin
section: "Function blocks"
order: 123
sidebar_position: 123
image: img/blk-mcgin-ld.webp
image_alt: "MC_GearIn on a rung of a ladder program"
generator: tools/docs_export.py
---

# MC_GearIn

Couples the axis to a master at a ratio - the line shaft.

![MC_GearIn on a rung](img/blk-mcgin-ld.webp){: .sb-center}

![MC_GearIn on a WEBview screen](img/blk-mcgin-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_GearIn_ST
VAR mcgin : MC_GearIn; END_VAR
  mcgin(AXIS := 2, Execute := mcgin_execute,
        Master := mcgin_master,
        ContinuousUpdate := mcgin_continuousupdate,
        RatioNumerator := mcgin_rationumerator,
        RatioDenominator := mcgin_ratiodenominator,
        MasterValueSource := mcgin_mastervaluesource,
        Acceleration := mcgin_acceleration,
        Deceleration := mcgin_deceleration, Jerk := mcgin_jerk,
        BufferMode := mcgin_buffermode, Delay := mcgin_delay);
  mcgin_ingear_st := mcgin.InGear;
  mcgin_busy_st := mcgin.Busy;
  mcgin_active_st := mcgin.Active;
  mcgin_commandaborted_st := mcgin.CommandAborted;
  mcgin_error_st := mcgin.Error;
  mcgin_errorid_st := mcgin.ErrorID;
  mcgin_register_st := mcgin.Register;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | STM32 | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|:---:|
| yes | - | - | yes | - |

**Needs:** a servo in cyclic position mode (csp) on EtherCAT with the distributed clock - a frequency drive answers ErrorID 8.

A board (ESP32) refuses the block at the build; a project for a Linux device
carries it. The STM32 runtime has no motion library.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | starts the command on the rising edge; the outputs hold while it is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
| `Master` | parameter | integer | 0 | the master axis - its number on the Motion node (the first axis is 0) |
| `ContinuousUpdate` | parameter | bool | FALSE | a changed input is taken at once while `Execute` holds |
| `RatioNumerator` | parameter | integer | 1 | the gear ratio - follower turns per `RatioDenominator` master turns; a ratio of 2 : 3 never drifts |
| `RatioDenominator` | parameter | integer | 1 | the gear ratio's denominator |
| `MasterValueSource` | parameter | `MC_Source` | `mcActualValue` | the master position the follower follows: `mcCommandedValue` 0, `mcSetValue` 1, `mcActualValue` 2 - the measured one on a real line |
| `Acceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Deceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Jerk` | parameter | number | 0 | the jerk limit, in acceleration units per second; 0 = none (a trapezoid) |
| `BufferMode` | parameter | `MC_BufferMode` | `mcAborting` | what the command does to the one running: `mcAborting` 0 takes the axis at once, `mcBuffered` 1 waits for the running one to finish, `mcBlendingLow` 2, `mcBlendingPrevious` 3, `mcBlendingNext` 4, `mcBlendingHigh` 5 join the two moves at that velocity |
| `Delay` | parameter | seconds | 0 | the chain delay the follower compensates, in seconds - measured on the line, never guessed |
| `InGear` | output | bool | - | the follower is coupled |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Active` | output | bool | - | this command moves the axis now (a buffered one waits with `Busy` alone) |
| `CommandAborted` | output | bool | - | another command took the axis, or the axis was stopped |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |
| `Register` | output | number | - | the follower's position against the master's through the ratio and the phase, in the follower's units; 0 = in register |

A project written before this library used the name `MC_GEARIN` for it; the old name
opens and builds as an alias.

## Error codes

`ErrorID` is one table for the whole library ([Motion blocks](/docs/blocks/blocks-motion/));
this block answers these of it:

| ErrorID | When |
|:---:|:---|
| 1 | the axis is not bound to a drive |
| 2 | the axis is not powered - `MC_Power` first |
| 3 | the axis is in ErrorStop - acknowledge with `MC_Reset` |
| 4 | the axis is stopping - an `MC_Stop` holds it |
| 5 | the axis is homing - only `MC_Stop` may interrupt it |
| 7 | an input makes no sense (a velocity of 0, a ratio of 0, a bit that does not exist) |
| 8 | this drive cannot do it |
| 9 | the master axis is not there, or is this axis |
| 10 | the block is not on this runtime - a Linux block on a board |
| 11 | the drive reports a fault (`MC_ReadAxisError` carries its code) |
| 12 | the target is past a software limit, or a moving axis reached one |
| 13 | the following error passed its limit |
| 15 | the command buffer is full |

## Description

A line shaft is one axis following another: the plate cylinders of a press follow
the drum, a slitter follows the web, a labeller follows the conveyor. `MC_GearIn`
couples the block's axis to the axis `Master` at the ratio
`RatioNumerator : RatioDenominator` - from the master's **measured** position
(`MasterValueSource` = `mcActualValue`) or its set value, every bus cycle, exactly
(a ratio of 2 : 3 never drifts, however long the line runs), with the master's
velocity through the ratio as the follower's feed-forward. `InGear` once coupled;
the axis is in SynchronizedMotion until `MC_GearOut`.

`Delay` is our extension: the chain delay the follower compensates, in seconds -
the time between the master's position being sampled and the follower's setpoint
being applied. Without it a follower lags the master by velocity × delay, an error
that grows with speed and doubles when the cycle doubles, which is what a press
shows as colours running away during ramps. Measure it, do not guess it: run the
line at a constant speed with `Delay` 0, read `Register`, divide by the speed -
that quotient is the delay. `Delay` is read every cycle, so it can be tuned from a
screen while the line runs; only the block that holds the gear writes it.

`Register` is our other extension: the follower's actual position against the
master's, through the ratio and the phase, in the follower's units - 0 is in
register, and a ramp of the master shows the uncompensated delay as a bump the
size of velocity × delay. `Master` may be a servo axis or a **virtual master** - an
axis with no drive that the program commands, or one that follows a counter
variable (the drum's encoder); the EtherCAT page says how it is made. A changed
ratio while `Execute` holds is applied at standstill.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](/docs/blocks/blocks-motion/).
