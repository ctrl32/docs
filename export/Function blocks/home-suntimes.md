---
title: "Home automation: SUNTIMES"
slug: home-suntimes
section: "Function blocks"
order: 202
sidebar_position: 202
generator: tools/docs_export.py
---

# SUNTIMES

Today's sunrise and sunset: the minutes of the local day the sun rises and sets at a place.

## In Structured Text

```iecst
PROGRAM SUNTIMES_ST
VAR suntimes : SUNTIMES; END_VAR
  suntimes(DOY := suntimes_doy, UTC_OFF := suntimes_utc_off, LAT := suntimes_lat, LON := suntimes_lon);
  suntimes_sunrise := suntimes.SUNRISE;
  suntimes_sunset := suntimes.SUNSET;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `DOY` | input | INT | - | The day of the year - bind SYS.DAY_OF_YEAR. |
| `UTC_OFF` | input | INT | - | The device's offset to UTC in minutes, summer time included - bind SYS.UTC_OFFSET. |
| `LAT` | parameter | REAL | 48.15 | Latitude, degrees north. |
| `LON` | parameter | REAL | 17.11 | Longitude, degrees east. |
| `SUNRISE` | output | INT | - | The minute of the day, 0..1439. |
| `SUNSET` | output | INT | - | The minute of the day. |

## Description

The defaults are Bratislava. The block computes the standard
approximation, good to a few minutes; a polar night gives 0 and 0, a
midnight sun 0 and 1439. Show the two numbers on a screen or feed them to
a DAYTIME through variables. ASTRO turns them into DAY / DARK.

It is written with the standard functions `SIN`, `COS`, `TAN` and `ACOS`
- open it to see how.

---

Every block of the family: [Home automation](/docs/blocks/blocks-home/) · every block: [Function blocks](/docs/blocks/)
