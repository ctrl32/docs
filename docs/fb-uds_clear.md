# UDS_CLEAR

Clears the fault codes of a diagnostic control unit on the rising edge of Execute.

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | - | - |

**Needs:** a diagnostic control unit on the CAN bus (the Diagnostics node).

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | BOOL | - | Clear on the rising edge. |
| `ECU` | parameter | REAL | 0 | Which control unit, as numbered on the Diagnostics node. |
| `Done` | output | BOOL | - | It confirmed; the fault variables went back to zero. |
| `Error` | output | BOOL | - | It refused, said nothing, or there are no diagnostics. |

## Errors

| When | What it means |
|:---|:---|
| Error | The control unit refused (a unit may refuse while the engine runs), did not answer, another question to the same unit is still in hand, or the device runs no diagnostics. |

## Description

`Done` holds while Execute holds after the control unit confirmed - the
fault variables go back to zero with it.

!!! tip "A unit may refuse while the engine runs"
    Clearing faults is often allowed only with the engine stopped.
    `Error` then means exactly that, and the program should say so
    rather than retry - the answer will not change while the conditions
    do not.

!!! note "One question at a time"
    A control unit answers one question at a time. A block pressed while
    another question of the same unit is still in hand reports `Error`;
    press again when it is idle.

Put both `Done` and `Error` on the screen beside the button. A press
that lights neither means the request never got away - a different
fault from a unit that answered "no".

The diagnostics need a **Linux device**; elsewhere every block reports
`Error`. See [Vehicle diagnostics](vehicle-diagnostics.md).

---

Every block of the family: [Vehicle diagnostics](blocks-services.md) · every block: [Function blocks](blocks.md)
