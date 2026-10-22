---
title: "Home automation: SCHEDULE"
slug: home-schedule
section: "Function blocks"
order: 204
sidebar_position: 204
generator: tools/docs_export.py
---

# SCHEDULE

Two windows a day, a value: VALUE is V_IN inside either window on the listed days and V_OUT outside.

## In Structured Text

```iecst
PROGRAM SCHEDULE_ST
VAR schedule : SCHEDULE; END_VAR
  schedule(ENABLE := schedule_enable, MINUTES := schedule_minutes, WEEKDAY := schedule_weekday, DAYS := schedule_days, FROM1 := schedule_from1, TO1 := schedule_to1, FROM2 := schedule_from2, TO2 := schedule_to2, V_IN := schedule_v_in, V_OUT := schedule_v_out);
  schedule_value := schedule.VALUE;
  schedule_q := schedule.Q;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `ENABLE` | input | BOOL | - | FALSE = Q is off and VALUE is V_OUT. |
| `MINUTES` | input | INT | - | Bind SYS.MINUTE_OF_DAY. |
| `WEEKDAY` | input | INT | - | Bind SYS.WEEKDAY. |
| `DAYS` | input | INT | - | A bit per day, Monday = 1 .. Sunday = 64; 127 every day, 31 Monday to Friday. |
| `FROM1` | parameter | INT | 360 | The first window's first minute (360 = 06:00). |
| `TO1` | parameter | INT | 480 | The minute the first window ends (480 = 08:00). |
| `FROM2` | parameter | INT | 960 | The second window's first minute (960 = 16:00). |
| `TO2` | parameter | INT | 1320 | The minute the second window ends (1320 = 22:00). |
| `V_IN` | parameter | INT | 2 | The value inside - comfort for THERMOSTAT's MODE. |
| `V_OUT` | parameter | INT | 1 | The value outside - eco. |
| `VALUE` | output | INT | - | V_IN inside a window, V_OUT outside. |
| `Q` | output | BOOL | - | TRUE inside a window. |

## Description

The block is two DAYTIME windows over the same days. Wire `VALUE` into
THERMOSTAT's `MODE` and the room heats by the clock (comfort 06:00-08:00
and 16:00-22:00, eco between).

`DAYS` is an input with no default: with 0 no day matches, so give it a
value. A different weekend: a second SCHEDULE with `DAYS` 96 and a SEL
block on `Q`. More windows or other days: another SCHEDULE beside it.

---

Every block of the family: [Home automation](/docs/blocks/blocks-home/) · every block: [Function blocks](/docs/blocks/)
