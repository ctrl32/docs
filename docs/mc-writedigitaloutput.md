---
image: img/blk-mcwdo-ld.webp
image_alt: "MC_WriteDigitalOutput on a rung of a ladder program"
---

# MC_WriteDigitalOutput

Sets one bit of the drive's outputs word.

![MC_WriteDigitalOutput on a rung](img/blk-mcwdo-ld.webp){: .sb-center}

![MC_WriteDigitalOutput on a WEBview screen](img/blk-mcwdo-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MC_WriteDigitalOutput_ST
VAR mcwdo : MC_WriteDigitalOutput; END_VAR
  mcwdo(AXIS := 0, Execute := mcwdo_execute,
        Value := mcwdo_value, Output := mcwdo_output,
        OutputNumber := mcwdo_outputnumber,
        ExecutionMode := mcwdo_executionmode);
  mcwdo_done_st := mcwdo.Done;
  mcwdo_busy_st := mcwdo.Busy;
  mcwdo_error_st := mcwdo.Error;
  mcwdo_errorid_st := mcwdo.ErrorID;
END_PROGRAM
```

`AXIS` names the axis at the call - its number on the Motion node, the first axis
is 0; the compiler refuses a motion block without it. The same block sits on a
rung in LD and in a function block diagram with the axis in its properties.

## Where it runs

| Linux runtime | ESP32 boards | EtherCAT | CANopen |
|:---:|:---:|:---:|:---:|
| yes | yes | yes | - |

**Needs:** a drive whose cyclic set carries the outputs word (object 0x60FE); no shipped device description carries it yet, so every drive answers ErrorID 8 until one does.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | bool | - | starts the command on the rising edge; the outputs hold while it is TRUE and fall when it falls (or stay one cycle when it fell before the command ended) |
| `Value` | input | bool | - | the bit to write |
| `Output` | parameter | integer | 0 | 0 = the drive's outputs word (CiA 402 object 0x60FE) |
| `OutputNumber` | parameter | integer | 0 | the bit of the word, 0 to 31 |
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
| 8 | this drive cannot do it |
| 15 | the command buffer is full |
| 17 | a mode this runtime does not do (`mcDelayed`) |

## Description

Writes one bit of the drive's digital outputs word on the rising edge of `Execute`:
`Output` 0 is the word (CiA 402 object 0x60FE), `OutputNumber` the bit (0 to 31),
`Value` what it becomes - a brake, a lamp, a valve on the drive's own terminals.
`ExecutionMode` immediately or queued after the running command.

---

The library's rules - what every block answers, the axis's states, units and
time, the drives - are on [Motion blocks](blocks-motion.md).
