# UDS_DTC

Reads the fault codes out of a diagnostic control unit on the rising edge of Execute.

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | - | - |

**Needs:** a diagnostic control unit on the CAN bus (the Diagnostics node).

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | BOOL | - | Ask on the rising edge. |
| `ECU` | parameter | REAL | 0 | Which control unit, as numbered on the Diagnostics node (0 = the first). |
| `Done` | output | BOOL | - | It answered (held while Execute holds). |
| `Error` | output | BOOL | - | It refused, said nothing, or there are no diagnostics. |

## Errors

| When | What it means |
|:---|:---|
| Error | The control unit refused, did not answer, another question to the same unit is still in hand, or the device runs no diagnostics (they need a Linux device). |

## Description

On a vehicle bus a control unit answers questions: what the fault codes
are, what a measured value is right now. The values a project reads
regularly are set up on the Diagnostics node and arrive on their own -
no program is needed for them. UDS_DTC, UDS_CLEAR and UDS_READ are for
what a **person** sets off: read the faults, clear them, ask once.

The count of faults and the first of their codes land in the variables
the control unit's page names, so a screen shows them like any other
value and an alarm can watch them - the count is one of those variables,
read like any other. Every code also goes into the diagnostic buffer
with its time - that is the record a service engineer reads afterwards.

```iecst
PROGRAM READ_FAULTS
VAR dtc : UDS_DTC; END_VAR
  dtc(Execute := btn_read_faults, ECU := 0);
  faults_read := dtc.Done;
  faults_error := dtc.Error;
END_PROGRAM
```

The units are numbered in the order of the Diagnostics node, from `0` -
the number the tree shows beside each unit.

!!! note "One question at a time"
    A control unit answers one question at a time, which is what the
    protocol allows. A block pressed while another question of the same
    unit is still in hand reports `Error`; the program tries again on
    the next press.

Put both `Done` and `Error` on the screen beside the button. A press
that lights neither means the request never got away - a different
fault from a unit that answered "no".

The diagnostics need a **Linux device**: the transport under the
questions is built into the Linux kernel. On a board whose runtime does
not carry them, every block reports `Error` - the honest answer to "read
the faults" on equipment that cannot ask. See
[Vehicle diagnostics](vehicle-diagnostics.md) for setting up a control
unit.

---

Every block of the family: [Vehicle diagnostics](blocks-services.md) · every block: [Function blocks](blocks.md)
