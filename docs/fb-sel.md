---
image: img/blk-sel-ld.webp
image_alt: "SEL in the editor"
---

# SEL

Binary selector: OUT = IN1 when G is TRUE, IN0 when it is FALSE.

![SEL on a rung](img/blk-sel-ld.webp){: .sb-center}

![SEL on a WEBview screen](img/blk-sel-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM SEL_ST
  sel_out_st := SEL(sel_g, sel_in0, sel_in1);
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `G` | input | BOOL | - | Which one to pass. |
| `IN0` | input | REAL | - | Passed when G is FALSE. |
| `IN1` | input | REAL | - | Passed when G is TRUE. |
| `OUT` | output | REAL | - | The chosen value. |

## Description

The IEC binary selector: an if-then-else you can draw.

**What it is for:** two setpoints and a switch between them. Day and
night temperature, fast and slow speed, manual and automatic value.

```
night_mode ──G───┐
  temp_day ──IN0─┤ SEL ├── OUT ──> setpoint
temp_night ──IN1─┘
```

Both inputs are read every cycle whichever one wins, so there is no
"stale" side - swap G and the output follows immediately.

!!! tip "Chaining selectors gives you more than two"
    Feed one SEL's output into the next SEL's IN0 and you get three
    choices, then four. Past about three, the logic is clearer in
    [Structured Text](st-language.md) as a CASE - and considerably
    easier to read a year later.

---

Every block of the family: [Comparison](blocks-compare.md) · every block: [Function blocks](blocks.md)
