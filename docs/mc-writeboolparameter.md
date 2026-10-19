---
image: img/blk-mcwbpar-ld.webp
image_alt: "MC_WriteBoolParameter on a rung of a ladder program"
---

# MC_WriteBoolParameter

Writes one of the axis's flags while the program runs.

![MC_WriteBoolParameter on a rung](img/blk-mcwbpar-ld.webp){: .sb-center}

![MC_WriteBoolParameter on a WEBview screen](img/blk-mcwbpar-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_WriteBoolParameter_ST
VAR mcwbpar : MC_WriteBoolParameter; END_VAR
  mcwbpar(AXIS := 0, Execute := mcwbpar_execute,
          Value := mcwbpar_value,
          ParameterNumber := mcwbpar_parameternumber,
          ExecutionMode := mcwbpar_executionmode);
  mcwbpar_done_st := mcwbpar.Done;
  mcwbpar_busy_st := mcwbpar.Busy;
  mcwbpar_error_st := mcwbpar.Error;
  mcwbpar_errorid_st := mcwbpar.ErrorID;
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
| `Execute` | input | bool | - | starts the command on the rising edge; the outputs hold while it is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
| `Value` | input | bool | - | the value to write, TRUE / FALSE |
| `ParameterNumber` | parameter | integer | 4 | the Part 1 number: 1 commanded position, 2 and 3 the software limits, 4 and 5 the limits enabled, 6 lag monitoring, 7 the maximum lag, 8 and 9 the velocity limits, 10 actual and 11 commanded velocity, 12 to 17 the acceleration, deceleration and jerk limits; 1000 the chain delay, 1001 the modulo period |
| `ExecutionMode` | parameter | `MC_ExecutionMode` | `mcImmediately` | `mcImmediately` 0 or `mcQueued` 1 (after the running command); `mcDelayed` 2 is refused with ErrorID 17 |
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
| 7 | an input makes no sense (a velocity of 0, a ratio of 0, a bit that does not exist) |
| 15 | the command buffer is full |
| 17 | a mode this runtime does not do (`mcDelayed`) |
| 18 | the parameter is read-only |

## Description

The same road as `MC_WriteParameter` for the flags: the limits enabled (4, 5), the
lag monitoring (6). Read-only numbers answer ErrorID 18.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
