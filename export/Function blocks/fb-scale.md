---
title: "Signal handling: SCALE"
slug: fb-scale
section: "Function blocks"
order: 170
sidebar_position: 170
image: img/blk-scale-ld.webp
image_alt: "SCALE in the editor"
generator: tools/docs_export.py
---

# SCALE

Maps IN linearly from the range IN_MIN..IN_MAX onto OUT_MIN..OUT_MAX.

![SCALE on a rung](img/blk-scale-ld.webp){: .sb-center}

![SCALE on a WEBview screen](img/blk-scale-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM SCALE_ST
  scale_out_st := SCALE(scale_in, scale_in_min, scale_in_max, scale_out_min, scale_out_max);
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN` | input | REAL | - | The raw value. |
| `IN_MIN` | parameter | REAL | 0 | Bottom of the range IN arrives in. |
| `IN_MAX` | parameter | REAL | 100 | Top of the range IN arrives in. |
| `OUT_MIN` | parameter | REAL | 0 | Bottom of the range you want. |
| `OUT_MAX` | parameter | REAL | 100 | Top of the range you want. |
| `OUT` | output | REAL | - | The converted value. |

## Description

**What it is for:** every analog input, ever. A 4–20 mA sensor arriving
as raw counts, a 0–10 V level, a fieldbus word that means something
physical.

```
raw_pressure ──[SCALE 0..4095 → 0..16]── OUT ──> pressure_bar
```

Two things worth knowing:

- **It does not clamp.** IN below IN_MIN gives OUT below OUT_MIN, and
  that is intentional - a reading under range is information, not
  something to hide. Follow it with [LIMIT](/docs/blocks/blocks-signal/) when the
  consumer needs a guaranteed range.
- **Reversing is legal.** Put the larger number in OUT_MIN and the
  smaller in OUT_MAX and the scale inverts, which is how you handle a
  sensor wired backwards without touching the wiring.

!!! tip "Scale once, near the input"
    Convert to engineering units immediately and let the rest of the
    program work in bar, °C and mm. Logic that carries raw counts around
    is logic nobody can read - including you, in a year.

### Putting the signal blocks in order

The usual chain for an analog input, left to right:

```
raw ──[SCALE]── engineering units ──[PT1]── smooth ──[LIMIT]── safe ──> logic
```

Scale first so everything downstream is in real units. Filter second, on
a value you can reason about. Clamp last, closest to whatever must not
receive nonsense. Then take the decision with HYST rather than a bare
comparison, and the whole path from sensor to relay is quiet, readable
and hard to get wrong.

---

Every block of the family: [Signal handling](/docs/blocks/blocks-signal/) · every block: [Function blocks](/docs/blocks/)
