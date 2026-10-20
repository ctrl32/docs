# VENT

The bathroom fan: runs with the light after a delay, runs on after it, runs on humidity, or by hand.

## In Structured Text

```iecst
PROGRAM VENT_ST
VAR vent : VENT; END_VAR
  vent(LIGHT := vent_light, HUM := vent_hum, MANUAL := vent_manual, T_DELAY := vent_t_delay, T_RUNON := vent_t_runon, T_MAX := vent_t_max, H_ON := vent_h_on, H_OFF := vent_h_off);
  vent_fan := vent.FAN;
  vent_humid := vent.HUMID;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `LIGHT` | input | BOOL | - | The bathroom light. |
| `HUM` | input | REAL | - | Relative humidity, %. |
| `MANUAL` | input | BOOL | - | An edge toggles the fan by hand. |
| `T_DELAY` | parameter | TIME | T#2m | The light must be on this long first (a short visit runs no fan). |
| `T_RUNON` | parameter | TIME | T#10m | How long the fan runs after the light went off. |
| `T_MAX` | parameter | TIME | T#1h | The longest humidity or manual run. |
| `H_ON` | parameter | REAL | 70.0 | Humidity that starts the fan. |
| `H_OFF` | parameter | REAL | 60.0 | Humidity that ends the demand. |
| `FAN` | output | BOOL | - | The fan. |
| `HUMID` | output | BOOL | - | The humidity demand, for a screen. |

## Description

The humidity demand comes on at `H_ON` and holds until the humidity drops
to `H_OFF`, for at most `T_MAX`. `T_MAX` also ends a manual run somebody
forgot.

It uses 4 of the program's 32 timers and edge detectors.

---

Every block of the family: [Home automation](blocks-home.md) · every block: [Function blocks](blocks.md)
