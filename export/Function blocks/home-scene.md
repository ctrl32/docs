---
title: "Home automation: SCENE"
slug: home-scene
section: "Function blocks"
order: 205
sidebar_position: 205
generator: tools/docs_export.py
---

# SCENE

Two channels, three scenes: an APPLY edge sets A and B to the levels of scene SEL; OFF clears both.

## In Structured Text

```iecst
PROGRAM SCENE_ST
VAR scene : SCENE; END_VAR
  scene(SEL := scene_sel, APPLY := scene_apply, OFF := scene_off, S1_A := scene_s1_a, S1_B := scene_s1_b, S2_A := scene_s2_a, S2_B := scene_s2_b, S3_A := scene_s3_a, S3_B := scene_s3_b);
  scene_a := scene.A;
  scene_b := scene.B;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `SEL` | input | INT | - | The scene, 1..3 (0 = off). |
| `APPLY` | input | BOOL | - | An edge applies the scene SEL. |
| `OFF` | input | BOOL | - | An edge sets both channels to 0. |
| `S1_A` | parameter | REAL | 100.0 | Scene 1, channel A. |
| `S1_B` | parameter | REAL | 100.0 | Scene 1, channel B. |
| `S2_A` | parameter | REAL | 60.0 | Scene 2, channel A. |
| `S2_B` | parameter | REAL | 30.0 | Scene 2, channel B. |
| `S3_A` | parameter | REAL | 20.0 | Scene 3, channel A. |
| `S3_B` | parameter | REAL | 0.0 | Scene 3, channel B. |
| `A` | output | REAL | - | The level of channel A - into a DIMMER's SET. |
| `B` | output | REAL | - | The level of channel B - into a DIMMER's SET. |

## Description

An `APPLY` edge with `SEL` 0 (or any value outside 1..3) sets both
channels to 0, as an `OFF` edge does.

MULTICLICK's `CLICKS` into `SEL` and a GT block (`CLICKS > 0`) into
`APPLY` make one click scene 1, two clicks scene 2, three clicks scene 3
on one wall button. More channels: another SCENE on the same `SEL` and
`APPLY`.

It uses 2 of the program's 32 timers and edge detectors.

---

Every block of the family: [Home automation](/docs/blocks/blocks-home/) · every block: [Function blocks](/docs/blocks/)
