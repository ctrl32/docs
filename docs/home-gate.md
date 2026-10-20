# GATE

A garage door or a gate: one impulse key cycles open - stop - close - stop; the photocell reverses a closing gate.

## In Structured Text

```iecst
PROGRAM GATE_ST
VAR gate : GATE; END_VAR
  gate(TRIG := gate_trig, OPEN := gate_open, CLOSE := gate_close, SAFETY := gate_safety, T_RUN := gate_t_run, T_REVERSE := gate_t_reverse, T_AUTO := gate_t_auto);
  gate_m_open := gate.M_OPEN;
  gate_m_close := gate.M_CLOSE;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `TRIG` | input | BOOL | - | The impulse key (the remote, the keypad). |
| `OPEN` | input | BOOL | - | An edge opens; the same direction stops. |
| `CLOSE` | input | BOOL | - | An edge closes; the same direction stops. |
| `SAFETY` | input | BOOL | - | The photocell or the safety edge: a closing gate reverses and stays open while TRUE. |
| `T_RUN` | parameter | TIME | T#20s | The travel time; the motor runs one second longer. |
| `T_REVERSE` | parameter | TIME | T#500ms | The pause before the other direction. |
| `T_AUTO` | parameter | TIME | T#0s | A fully open gate closes by itself after this; 0 = never. |
| `M_OPEN` | output | BOOL | - | The motor relay open. |
| `M_CLOSE` | output | BOOL | - | The motor relay close. |

## Description

A key while the gate runs stops it; the next one runs the other way than
the last run. While `SAFETY` is TRUE no close command is taken and the
automatic close waits.

The two outputs are never TRUE together. The gate drive's own safety
devices stay wired as the manufacturer says - the block is the key logic,
not the protection.

It uses 6 of the program's 32 timers and edge detectors.

---

Every block of the family: [Home automation](blocks-home.md) · every block: [Function blocks](blocks.md)
