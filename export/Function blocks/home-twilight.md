---
title: "Home automation: TWILIGHT"
slug: home-twilight
section: "Function blocks"
order: 199
sidebar_position: 199
image: img/home-room.webp
image_alt: "TWILIGHT in the editor"
generator: tools/docs_export.py
---

# TWILIGHT

It is dark: DARK switches with hysteresis around THRESHOLD, filtered by T_FILTER so a cloud does not switch the garden.

![TWILIGHT](img/home-room.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM TWILIGHT_ST
VAR twilight : TWILIGHT; END_VAR
  twilight(LUX := twilight_lux, THRESHOLD := twilight_threshold, HYST := twilight_hyst, T_FILTER := twilight_t_filter);
  twilight_dark := twilight.DARK;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `LUX` | input | REAL | - | The light sensor. |
| `THRESHOLD` | parameter | REAL | 20.0 | The level. |
| `HYST` | parameter | REAL | 5.0 | Half the band: dark below THRESHOLD - HYST, light above THRESHOLD + HYST. |
| `T_FILTER` | parameter | TIME | T#30s | The value must stay on one side this long. |
| `DARK` | output | BOOL | - | TRUE while it is dark. |

## Description

`DARK` comes on once `LUX` has been under `THRESHOLD - HYST` for
`T_FILTER`, and goes off once it has been over `THRESHOLD + HYST` for
`T_FILTER`.

TWILIGHT measures the light where the sensor is; ASTRO knows it from the
calendar and needs no sensor. Both give a DARK, use the one you have. A
light on presence is PRESENCE's `PRESENT` AND TWILIGHT's `DARK`.

It uses 2 of the program's 32 timers and edge detectors.

---

Every block of the family: [Home automation](/docs/blocks/blocks-home/) · every block: [Function blocks](/docs/blocks/)
