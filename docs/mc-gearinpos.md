---
image: img/blk-mcgip-ld.webp
image_alt: "MC_GearInPos on a rung of a ladder program"
---

# MC_GearInPos

Gears in at a defined relation of the two positions.

![MC_GearInPos on a rung](img/blk-mcgip-ld.webp){: .sb-center}

![MC_GearInPos on a WEBview screen](img/blk-mcgip-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_GearInPos_ST
VAR mcgip : MC_GearInPos; END_VAR
  mcgip(AXIS := 2, Execute := mcgip_execute,
        MasterSyncPosition := mcgip_mastersyncposition,
        SlaveSyncPosition := mcgip_slavesyncposition,
        Velocity := mcgip_velocity, Master := mcgip_master,
        RatioNumerator := mcgip_rationumerator,
        RatioDenominator := mcgip_ratiodenominator,
        MasterValueSource := mcgip_mastervaluesource,
        SyncMode := mcgip_syncmode,
        MasterStartDistance := mcgip_masterstartdistance,
        Acceleration := mcgip_acceleration,
        Deceleration := mcgip_deceleration, Jerk := mcgip_jerk,
        BufferMode := mcgip_buffermode, Delay := mcgip_delay);
  mcgip_startsync_st := mcgip.StartSync;
  mcgip_insync_st := mcgip.InSync;
  mcgip_busy_st := mcgip.Busy;
  mcgip_active_st := mcgip.Active;
  mcgip_commandaborted_st := mcgip.CommandAborted;
  mcgip_error_st := mcgip.Error;
  mcgip_errorid_st := mcgip.ErrorID;
  mcgip_register_st := mcgip.Register;
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
| `MasterSyncPosition` | input | number | - | the master position of the relation, in units |
| `SlaveSyncPosition` | input | number | - | the follower position that belongs to `MasterSyncPosition`, in units |
| `Velocity` | input | number | - | the speed the follower moves into the relation with, in units per the time base |
| `Master` | parameter | integer | 0 | the master axis - its number on the Motion node (the first axis is 0) |
| `RatioNumerator` | parameter | integer | 1 | the gear ratio - follower turns per `RatioDenominator` master turns; a ratio of 2 : 3 never drifts |
| `RatioDenominator` | parameter | integer | 1 | the gear ratio's denominator |
| `MasterValueSource` | parameter | `MC_Source` | `mcActualValue` | the master position the follower follows: `mcCommandedValue` 0, `mcSetValue` 1, `mcActualValue` 2 - the measured one on a real line |
| `SyncMode` | parameter | `MC_SyncMode` | `mcShortest` | `mcShortest` 0, `mcCatchUp` 1, `mcSlowDown` 2 - how the follower reaches the relation |
| `MasterStartDistance` | parameter | number | 0 | the master's travel over which the follower moves into the relation, in units |
| `Acceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Deceleration` | parameter | number | 0 | the ramp, in velocity units per second; 0 = the axis's default |
| `Jerk` | parameter | number | 0 | the jerk limit, in acceleration units per second; 0 = none (a trapezoid) |
| `BufferMode` | parameter | `MC_BufferMode` | `mcAborting` | what the command does to the one running: `mcAborting` 0 takes the axis at once, `mcBuffered` 1 waits for the running one to finish, `mcBlendingLow` 2, `mcBlendingPrevious` 3, `mcBlendingNext` 4, `mcBlendingHigh` 5 join the two moves at that velocity |
| `Delay` | parameter | seconds | 0 | the chain delay the follower compensates, in seconds - measured on the line, never guessed |
| `StartSync` | output | bool | - | the follower is moving into the relation |
| `InSync` | output | bool | - | the follower rides the relation (the table) |
| `Busy` | output | bool | - | the command is taken and not finished |
| `Active` | output | bool | - | this command moves the axis now (a buffered one waits with `Busy` alone) |
| `CommandAborted` | output | bool | - | another command took the axis, or the axis was stopped |
| `Error` | output | bool | - | the command failed |
| `ErrorID` | output | integer | - | why it failed - the table below |
| `Register` | output | number | - | the follower's position against the master's through the ratio and the phase, in the follower's units; 0 = in register |

A project written before this library used the name `MC_GEARINPOS` for it; the old name
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
| 7 | an input makes no sense (a velocity of 0, a ratio of 0, a bit that does not exist) |
| 8 | this drive cannot do it |
| 9 | the master axis is not there, or is this axis |
| 10 | the block is not on this runtime - a Linux block on a board |
| 11 | the drive reports a fault (`MC_ReadAxisError` carries its code) |
| 12 | the target is past a software limit, or a moving axis reached one |
| 13 | the following error passed its limit |
| 15 | the command buffer is full |

## Description

Gears in **at a defined relation of the two positions**: when the master stands at
`MasterSyncPosition` the follower stands at `SlaveSyncPosition`, the relation
repeating every `RatioDenominator` master revolutions. At gear-in the follower
moves into that relation at `Velocity` - at once (`SyncMode` `mcCatchUp`), or over
`MasterStartDistance` of the master's travel before the sync position; `StartSync`
while it does, `InSync` once it is in gear and in the relation.

While `Execute` holds, a changed `SlaveSyncPosition` is a further move - the
operator's register trim, or the phase a job carries - and a changed ratio is
applied at standstill. So a job's phases are plain numbers a recipe keeps: the same
relation comes back after a job change and after a restart, without a mark and
without a homing run, because the drives' positions are absolute. `Delay` and
`Register` are the same extensions as on `MC_GearIn`.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
