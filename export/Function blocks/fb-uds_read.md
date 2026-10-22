---
title: "Vehicle diagnostics: UDS_READ"
slug: fb-uds_read
section: "Function blocks"
order: 187
sidebar_position: 187
generator: tools/docs_export.py
---

# UDS_READ

Asks a diagnostic control unit for one data identifier now, without waiting for its row's period.

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | - | - |

**Needs:** a diagnostic control unit on the CAN bus (the Diagnostics node).

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | BOOL | - | Ask on the rising edge. |
| `ECU` | parameter | REAL | 0 | Which control unit, as numbered on the Diagnostics node. |
| `DID` | parameter | REAL | 0 | Which value, by the number its document gives (the same number the row carries). |
| `Done` | output | BOOL | - | It answered (held while Execute holds). |
| `Error` | output | BOOL | - | It refused, said nothing, or there are no diagnostics. |

## Errors

| When | What it means |
|:---|:---|
| Error | The control unit refused (for example a value outside the session it is in), did not answer, another question to the same unit is still in hand, or the device runs no diagnostics. |

## Description

The answer lands in the variable of the row that carries the same
number, so the screen that shows it needs no second variable - when the
project has such a row. Use this where a value matters at a moment
rather than all the time - a reading taken when the operator presses a
button, not one polled every second for a year. A row with a period of 0
is asked only when a program asks.

!!! note "One question at a time"
    A control unit answers one question at a time. A block pressed while
    another question of the same unit is still in hand reports `Error`;
    press again when it is idle.

!!! tip "A refusal is an answer"
    A unit may refuse a value in the session it is in. `Error` then
    means exactly that, and the program should say so rather than retry
    - the answer will not change while the conditions do not.

The diagnostics need a **Linux device**; elsewhere every block reports
`Error`. See [Vehicle diagnostics](/docs/buses/vehicle-diagnostics/).

---

Every block of the family: [Vehicle diagnostics](/docs/blocks/blocks-services/) · every block: [Function blocks](/docs/blocks/)
