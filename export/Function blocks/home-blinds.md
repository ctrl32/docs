---
title: "Home automation: BLINDS"
slug: home-blinds
section: "Function blocks"
order: 196
sidebar_position: 196
image: img/home-blinds.webp
image_alt: "BLINDS in the editor"
generator: tools/docs_export.py
---

# BLINDS

A roller shutter with two keys: UP and DOWN run the motor, the same key stops, the other key reverses, SAFETY drives up and locks.

![BLINDS](img/home-blinds.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM BLINDS_ST
VAR blinds : BLINDS; END_VAR
  blinds(UP := blinds_up, DOWN := blinds_down, STOP := blinds_stop, SAFETY := blinds_safety, T_RUN := blinds_t_run, T_REVERSE := blinds_t_reverse, T_TILT := blinds_t_tilt, T_LONG := blinds_t_long);
  blinds_m_up := blinds.M_UP;
  blinds_m_down := blinds.M_DOWN;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `UP` | input | BOOL | - | The up key (an edge). |
| `DOWN` | input | BOOL | - | The down key (an edge). |
| `STOP` | input | BOOL | - | An edge stops. |
| `SAFETY` | input | BOOL | - | Wind or frost: drives up once and locks both keys while TRUE. |
| `T_RUN` | parameter | TIME | T#25s | The full travel time; the motor runs one second longer so the end switch is reached. |
| `T_REVERSE` | parameter | TIME | T#500ms | The pause between two directions, so the motor never reverses under load. |
| `T_TILT` | parameter | TIME | T#0s | Venetian blinds: the motor time of one tilt step; 0 = a roller shutter. |
| `T_LONG` | parameter | TIME | T#400ms | Venetian blinds: a key held longer than this runs to the end. |
| `M_UP` | output | BOOL | - | The motor relay up. |
| `M_DOWN` | output | BOOL | - | The motor relay down. |

## Description

A key in the direction that already runs stops the motor; the other key
waits `T_REVERSE` with both relays off, then reverses. The two outputs are
never TRUE together. Wire the end switches into the motor as the
manufacturer says - the block only times the run.

With `T_TILT` at zero the block is a **roller shutter**: a click on a key
runs to the end. With `T_TILT` set it is a **venetian blind**: a short
click on a key turns the slats one step (the motor runs `T_TILT`), a key
held past `T_LONG` runs to the end, and a click during a run stops it as
before.

The keys can be wall buttons or a PUSHBUTTON's outputs. TRAVEL beside it
keeps the position.

It uses 8 of the program's 32 timers and edge detectors.

---

Every block of the family: [Home automation](/docs/blocks/blocks-home/) · every block: [Function blocks](/docs/blocks/)
