---
image: img/blk-pt1-ld.webp
image_alt: "PT1 in the editor"
---

# PT1

First-order filter: OUT approaches IN with the time constant T.

![PT1 on a rung](img/blk-pt1-ld.webp){: .sb-center}

![PT1 on a WEBview screen](img/blk-pt1-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM PT1_ST
VAR pt1 : PT1; END_VAR
  pt1(IN := pt1_in, T := pt1_t);
  pt1_out_st := pt1.OUT;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN` | input | REAL | - | The noisy value. |
| `T` | parameter | TIME | T#1s | Time constant. |
| `OUT` | output | REAL | - | The smoothed value. |

## Description

After T the output has covered about 63 % of a step; after about 3×T it
has effectively arrived. Bigger T means smoother and slower.

**What it is for:** a measurement that jumps around more than the thing
it measures. A flow meter, a load cell on a vibrating frame, a
temperature sensor picking up electrical noise.

```
raw_weight ──[PT1 T=T#500ms]── OUT ──> weight
```

!!! warning "A filter buys smoothness with delay"
    A filtered value is always behind reality, by roughly T. Filter a
    measurement that feeds a fast control loop and you have made the
    loop slower and less stable - filter as little as you can get away
    with, and never more than the loop's own response time.

    For a value that is only *displayed*, a filter costs almost nothing
    and makes a screen far more pleasant to read.

### Putting the signal blocks in order

```
raw ──[SCALE]── engineering units ──[PT1]── smooth ──[LIMIT]── safe ──> logic
```

Scale first so everything downstream is in real units. Filter second, on
a value you can reason about. Clamp last.

---

Every block of the family: [Signal handling](blocks-signal.md) · every block: [Function blocks](blocks.md)
