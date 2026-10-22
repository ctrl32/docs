---
title: "Home automation: ASTRO"
slug: home-astro
section: "Function blocks"
order: 203
sidebar_position: 203
generator: tools/docs_export.py
---

# ASTRO

Day and dark by the sun: DAY between sunrise and sunset, DARK outside, each edge shifted by an offset.

## In Structured Text

```iecst
PROGRAM ASTRO_ST
VAR astro : ASTRO; END_VAR
  astro(ENABLE := astro_enable, MINUTES := astro_minutes, DOY := astro_doy, UTC_OFF := astro_utc_off, LAT := astro_lat, LON := astro_lon, OFS_RISE := astro_ofs_rise, OFS_SET := astro_ofs_set);
  astro_day := astro.DAY;
  astro_dark := astro.DARK;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `ENABLE` | input | BOOL | - | FALSE = DAY and DARK stay off. |
| `MINUTES` | input | INT | - | Bind SYS.MINUTE_OF_DAY. |
| `DOY` | input | INT | - | Bind SYS.DAY_OF_YEAR. |
| `UTC_OFF` | input | INT | - | Bind SYS.UTC_OFFSET. |
| `LAT` | parameter | REAL | 48.15 | Latitude of the place, as in SUNTIMES. |
| `LON` | parameter | REAL | 17.11 | Longitude of the place, as in SUNTIMES. |
| `OFS_RISE` | parameter | INT | 0 | Minutes added to the sunrise (-30: the day starts half an hour before). |
| `OFS_SET` | parameter | INT | 0 | Minutes added to the sunset (+20: the garden light waits for real dusk). |
| `DAY` | output | BOOL | - | TRUE between the shifted sunrise and sunset. |
| `DARK` | output | BOOL | - | NOT DAY while enabled - the garden light, the blinds at dusk. |

## Description

ASTRO has a SUNTIMES inside. TWILIGHT measures the light where the sensor
is; ASTRO knows it from the calendar and needs no sensor. Both give a
DARK, use the one you have.

---

Every block of the family: [Home automation](/docs/blocks/blocks-home/) · every block: [Function blocks](/docs/blocks/)
