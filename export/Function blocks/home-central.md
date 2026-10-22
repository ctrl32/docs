---
title: "Home automation: CENTRAL"
slug: home-central
section: "Function blocks"
order: 208
sidebar_position: 208
generator: tools/docs_export.py
---

# CENTRAL

Everything on, everything off, leaving: ON and OFF edges make a pulse; LEAVE makes the off pulse T_LEAVE later.

## In Structured Text

```iecst
PROGRAM CENTRAL_ST
VAR central : CENTRAL; END_VAR
  central(ON := central_on, OFF := central_off, LEAVE := central_leave, CANCEL := central_cancel, T_LEAVE := central_t_leave, T_PULSE := central_t_pulse);
  central_all_on := central.ALL_ON;
  central_all_off := central.ALL_OFF;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `ON` | input | BOOL | - | An edge: ALL_ON pulses (and a pending LEAVE is forgotten). |
| `OFF` | input | BOOL | - | An edge: ALL_OFF pulses now. |
| `LEAVE` | input | BOOL | - | An edge: ALL_OFF pulses after T_LEAVE - time to reach the door. |
| `CANCEL` | input | BOOL | - | An edge forgets a pending LEAVE. |
| `T_LEAVE` | parameter | TIME | T#30s | The time between LEAVE and the ALL_OFF pulse. |
| `T_PULSE` | parameter | TIME | T#200ms | The pulse length. |
| `ALL_ON` | output | BOOL | - | Into TOGGLE's SET and DIMMER's ON. |
| `ALL_OFF` | output | BOOL | - | Into TOGGLE's RESET, STAIRLIGHT's OFF and DIMMER's OFF. |

## Description

One CENTRAL drives the whole house: its `ALL_ON` goes to every TOGGLE's
`SET` and every DIMMER's `ON`, its `ALL_OFF` to every TOGGLE's `RESET`,
STAIRLIGHT's `OFF` and DIMMER's `OFF`.

It uses 7 of the program's 32 timers and edge detectors.

---

Every block of the family: [Home automation](/docs/blocks/blocks-home/) · every block: [Function blocks](/docs/blocks/)
