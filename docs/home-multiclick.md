# MULTICLICK

Counts the clicks of a burst.

## In Structured Text

```iecst
PROGRAM MULTICLICK_ST
VAR multiclick : MULTICLICK; END_VAR
  multiclick(IN := multiclick_in, T_DOUBLE := multiclick_t_double);
  multiclick_double := multiclick.DOUBLE;
  multiclick_clicks := multiclick.CLICKS;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN` | input | BOOL | - | The wall contact. |
| `T_DOUBLE` | parameter | TIME | T#300ms | The gap that ends a burst. |
| `DOUBLE` | output | BOOL | - | TRUE for one cycle when the burst had exactly two clicks. |
| `CLICKS` | output | INT | - | The count of the burst that just ended, for one cycle; 0 otherwise. |

## Description

A burst ends once `T_DOUBLE` passes after the last release; then
`CLICKS` carries its count (1, 2, 3 ...) for one cycle.

A scene selector counts on `CLICKS`: one click the reading lamp, two the
whole room, three everything off. With SCENE: `CLICKS` into SCENE's `SEL`
and a GT block (`CLICKS > 0`) into its `APPLY`.

It uses 2 of the program's 32 timers and edge detectors.

---

Every block of the family: [Home automation](blocks-home.md) · every block: [Function blocks](blocks.md)
