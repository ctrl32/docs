---
title: "Home automation: DIMMER"
slug: home-dimmer
section: "Function blocks"
order: 194
sidebar_position: 194
generator: tools/docs_export.py
---

# DIMMER

One button dims: a short click switches between off and the remembered level, a long press ramps.

## In Structured Text

```iecst
PROGRAM DIMMER_ST
VAR dimmer : DIMMER; END_VAR
  dimmer(BTN := dimmer_btn, ON := dimmer_on, OFF := dimmer_off, SET := dimmer_set, MIN := dimmer_min, MAX := dimmer_max, T_RAMP := dimmer_t_ramp);
  dimmer_level := dimmer.LEVEL;
  dimmer_q := dimmer.Q;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `BTN` | input | BOOL | - | The wall contact, straight in (the block has its own PUSHBUTTON). |
| `ON` | input | BOOL | - | An edge switches on to the remembered level. |
| `OFF` | input | BOOL | - | An edge switches off. |
| `SET` | input | REAL | - | Applies a level when it changes (a scene, a slider). |
| `MIN` | parameter | REAL | 10.0 | The lowest level a long press ramps to. |
| `MAX` | parameter | REAL | 100.0 | The highest level. |
| `T_RAMP` | parameter | TIME | T#4s | The time from 0 to 100 %. |
| `LEVEL` | output | REAL | - | 0..100 %, ramping. |
| `Q` | output | BOOL | - | TRUE while LEVEL is above zero. |

## Description

The first long press ramps **up**, the next one **down** (a long press
from below `MIN` always ramps up); the level where the finger lifted is
remembered and a short click comes back to it. `LEVEL` moves at 100 % per
`T_RAMP`, so a 0-10 V output or a PWM lamp fades instead of jumping.

`ON` / `OFF` take CENTRAL's `ALL_ON` / `ALL_OFF`; `SET` takes a SCENE's
`A` or `B`, or a slider. A `LEVEL` for a lamp goes to a PWM output of the
board (the `pwm_out` peripheral takes it directly).

It uses 6 of the program's 32 timers and edge detectors (its PUSHBUTTON
included).

---

Every block of the family: [Home automation](/docs/blocks/blocks-home/) · every block: [Function blocks](/docs/blocks/)
