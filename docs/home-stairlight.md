---
image: img/home-lights.webp
image_alt: "STAIRLIGHT in the editor"
---

# STAIRLIGHT

The staircase light: a pulse lights Q for PT, another pulse restarts the time, WARN blinks before the end.

![STAIRLIGHT](img/home-lights.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM STAIRLIGHT_ST
VAR stairlight : STAIRLIGHT; END_VAR
  stairlight(TRIG := stairlight_trig, OFF := stairlight_off, PERMANENT := stairlight_permanent, PT := stairlight_pt, T_WARN := stairlight_t_warn);
  stairlight_q := stairlight.Q;
  stairlight_warn := stairlight.WARN;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `TRIG` | input | BOOL | - | The button; any edge starts or restarts the time. |
| `OFF` | input | BOOL | - | An edge ends it now. |
| `PERMANENT` | input | BOOL | - | Holds Q while TRUE (cleaning the stairs). |
| `PT` | parameter | TIME | T#3m | How long the light stays. |
| `T_WARN` | parameter | TIME | T#30s | The last part of PT during which WARN blinks. |
| `Q` | output | BOOL | - | The light. |
| `WARN` | output | BOOL | - | Blinks at 1 Hz in the last T_WARN; drive a second lamp, or the same one through an OR. |

## Description

Every further pulse on `TRIG` restarts `PT`, so nobody is left in the dark
without notice: `WARN` blinks in the last `T_WARN`. While `PERMANENT` holds
the light, `WARN` stays off. CENTRAL's `ALL_OFF` goes into `OFF`.

It uses 4 of the program's 32 timers and edge detectors.

---

Every block of the family: [Home automation](blocks-home.md) · every block: [Function blocks](blocks.md)
