---
title: "Home automation: PWM"
slug: home-pwm
section: "Function blocks"
order: 195
sidebar_position: 195
generator: tools/docs_export.py
---

# PWM

A level into a slow square wave: Q is TRUE for IN percent of every PERIOD.

## In Structured Text

```iecst
PROGRAM PWM_ST
VAR pwm : PWM; END_VAR
  pwm(IN := pwm_in, PERIOD := pwm_period);
  pwm_q := pwm.Q;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN` | input | REAL | - | The level, 0..100 %. |
| `PERIOD` | parameter | TIME | T#10s | The period. |
| `Q` | output | BOOL | - | The relay or the solid-state relay. |

## Description

For a floor-heating valve or a heater relay a period of seconds to
minutes is right. For a lamp use a PWM output of the board instead: the
`pwm_out` peripheral takes the DIMMER's `LEVEL` directly.

It uses 1 of the program's 32 timers and edge detectors.

---

Every block of the family: [Home automation](/docs/blocks/blocks-home/) · every block: [Function blocks](/docs/blocks/)
