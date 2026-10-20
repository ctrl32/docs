---
image: img/home-room.webp
image_alt: "PRESENCE in the editor"
---

# PRESENCE

Somebody is here: holds PRESENT for T_HOLD after the last motion.

![PRESENCE](img/home-room.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM PRESENCE_ST
VAR presence : PRESENCE; END_VAR
  presence(MOTION := presence_motion, ENABLE := presence_enable, T_HOLD := presence_t_hold);
  presence_present := presence.PRESENT;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `MOTION` | input | BOOL | - | The PIR sensor. |
| `ENABLE` | input | BOOL | - | FALSE = the output stays off (a sleeping room at night). |
| `T_HOLD` | parameter | TIME | T#5m | How long after the last motion. |
| `PRESENT` | output | BOOL | - | Somebody is here; drive a light through an AND with TWILIGHT's DARK. |

## Description

Motion stretched into presence, so a light stays while somebody reads.
`ENABLE` gates it - a DAYTIME window, a scene. A PRESENCE block can also
drop a THERMOSTAT's `MODE` to eco while nobody is home.

It uses 1 of the program's 32 timers and edge detectors.

---

Every block of the family: [Home automation](blocks-home.md) · every block: [Function blocks](blocks.md)
