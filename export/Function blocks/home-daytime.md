---
title: "Home automation: DAYTIME"
slug: home-daytime
section: "Function blocks"
order: 201
sidebar_position: 201
image: img/home-room.webp
image_alt: "DAYTIME in the editor"
generator: tools/docs_export.py
---

# DAYTIME

A window in the day: Q while the clock is inside FROM..TO on one of DAYS.

![DAYTIME](img/home-room.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM DAYTIME_ST
VAR daytime : DAYTIME; END_VAR
  daytime(ENABLE := daytime_enable, MINUTES := daytime_minutes, WEEKDAY := daytime_weekday, FROM := daytime_from, TO := daytime_to, DAYS := daytime_days);
  daytime_q := daytime.Q;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `ENABLE` | input | BOOL | - | FALSE = Q stays off. |
| `MINUTES` | input | INT | - | The minute of the day - bind SYS.MINUTE_OF_DAY. |
| `WEEKDAY` | input | INT | - | 1 = Monday .. 7 = Sunday - bind SYS.WEEKDAY. |
| `FROM` | parameter | INT | 390 | The first minute (390 = 06:30). |
| `TO` | parameter | INT | 1320 | The minute the window ends (1320 = 22:00). |
| `DAYS` | parameter | INT | 127 | A bit per day, Monday = 1, Sunday = 64; 127 = every day, 31 = Monday to Friday. |
| `Q` | output | BOOL | - | TRUE inside the window. |

## Description

Times are minutes of the day (06:30 = 390). A window over midnight
(`FROM` 1320, `TO` 390) works as you expect.

The clock is the device's, in the project's time zone (*clock: tz*);
while the device has no valid time (`SYS.TIME_VALID` FALSE) the minute
reads 0 and the weekday 0, so `Q` stays FALSE rather than guessing. See
the system variables in [Variables](/docs/editor-overview/variables/).

A DAYTIME drives a THERMOSTAT's `MODE` (comfort by day, eco at night) or
a PRESENCE's `ENABLE`. Two windows a day with a value: SCHEDULE.

It uses none of the program's 32 timers and edge detectors.

---

Every block of the family: [Home automation](/docs/blocks/blocks-home/) · every block: [Function blocks](/docs/blocks/)
