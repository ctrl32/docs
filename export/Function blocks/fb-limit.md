---
title: "Signal handling: LIMIT"
slug: fb-limit
section: "Function blocks"
order: 171
sidebar_position: 171
image: img/blk-limit-ld.webp
image_alt: "LIMIT in the editor"
generator: tools/docs_export.py
---

# LIMIT

Clamps IN into the range MN..MX.

![LIMIT on a rung](img/blk-limit-ld.webp){: .sb-center}

![LIMIT on a WEBview screen](img/blk-limit-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM LIMIT_ST
  limit_out_st := LIMIT(limit_mn, limit_in, limit_mx);
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN` | input | REAL | - | The value. |
| `MN` | parameter | REAL | 0 | Lowest allowed value. |
| `MX` | parameter | REAL | 100 | Highest allowed value. |
| `OUT` | output | REAL | - | IN, clamped. |

## Description

**What it is for:** making sure a value that came from somewhere you do
not control - a screen, a recipe, a fieldbus master - cannot ask for
something impossible.

```
setpoint_from_hmi ──[LIMIT MN=20 MX=80]── OUT ──> setpoint
```

!!! warning "Clamping hides the fact that it clamped"
    A setpoint pinned at 80 looks exactly like a setpoint of 80. If it
    matters that somebody asked for more, compare the input with the
    output and flag it - one [EQ](/docs/blocks/blocks-compare/) and you have an
    "out of range" indication instead of a silent surprise.

For a floor alone or a ceiling alone, [MAX or MIN](/docs/blocks/blocks-math/) with
a constant does the same job.

### Putting the signal blocks in order

```
raw ──[SCALE]── engineering units ──[PT1]── smooth ──[LIMIT]── safe ──> logic
```

Scale first so everything downstream is in real units. Filter second, on
a value you can reason about. Clamp last, closest to whatever must not
receive nonsense.

---

Every block of the family: [Signal handling](/docs/blocks/blocks-signal/) · every block: [Function blocks](/docs/blocks/)
