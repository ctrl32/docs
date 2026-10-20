---
image: img/home-lights.webp
image_alt: "PUSHBUTTON in the editor"
---

# PUSHBUTTON

Tells a short click from a long press on one wall contact.

![PUSHBUTTON](img/home-lights.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM PUSHBUTTON_ST
VAR pushbutton : PUSHBUTTON; END_VAR
  pushbutton(IN := pushbutton_in, T_LONG := pushbutton_t_long, T_DOUBLE := pushbutton_t_double);
  pushbutton_short := pushbutton.SHORT;
  pushbutton_long := pushbutton.LONG;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN` | input | BOOL | - | The wall contact, TRUE while pressed. |
| `T_LONG` | parameter | TIME | T#400ms | Held longer than this is a long press. |
| `T_DOUBLE` | parameter | TIME | T#300ms | Two clicks closer than this belong together. |
| `SHORT` | output | BOOL | - | TRUE for ONE cycle after a single short click. |
| `LONG` | output | BOOL | - | TRUE from T_LONG until the finger lifts. |

## Description

`SHORT` waits `T_DOUBLE` after the release before it fires, so a double
click never counts as two shorts. A long press makes no `SHORT` at all.
A double click makes no `SHORT` either - MULTICLICK reports it - so a
light does not flicker on the way to a scene.

The usual pair is PUSHBUTTON's `SHORT` into a TOGGLE (a light switch) or
into a STAIRLIGHT. DIMMER has its own PUSHBUTTON inside and takes the wall
contact straight.

```iecst
PROGRAM LIGHTS
VAR
  b_kitchen : PUSHBUTTON;
  l_kitchen : TOGGLE;
END_VAR
  b_kitchen(IN := btn_kitchen);
  l_kitchen(TRIG := b_kitchen.SHORT, SET := all_on, RESET := all_off);
  light_kitchen := l_kitchen.Q;
END_PROGRAM
```

It uses 3 of the program's 32 timers and edge detectors.

---

Every block of the family: [Home automation](blocks-home.md) · every block: [Function blocks](blocks.md)
