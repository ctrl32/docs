# Signal handling

Five blocks that stand between a raw value and a usable one: scaling,
clamping, switching cleanly, limiting how fast something changes, and
smoothing noise.

These are the blocks that turn "the sensor says 6234" into something a
equipment can act on.

---

## The blocks

<!-- fb-index: begin -->

| Block | What it does | Linux | ESP32 | STM32 |
|:---|:---|:---:|:---:|:---:|
| [SCALE](fb-scale.md) | Maps IN linearly from the range IN_MIN..IN_MAX onto OUT_MIN..OUT_MAX. | yes | yes | yes |
| [LIMIT](fb-limit.md) | Clamps IN into the range MN..MX. | yes | yes | yes |
| [HYST](fb-hyst.md) | Comparator with hysteresis: Q switches on at IN >= ON, and off again only at IN <= OFF. | yes | yes | yes |
| [RAMP](fb-ramp.md) | Rate limiter: OUT follows IN, but changes at most RATE units per second. | yes | yes | yes |
| [PT1](fb-pt1.md) | First-order filter: OUT approaches IN with the time constant T. | yes | yes | yes |

<!-- fb-index: end -->

## Putting them in order

The usual chain for an analog input, left to right:

```
raw ──[SCALE]── engineering units ──[PT1]── smooth ──[LIMIT]── safe ──> logic
```

Scale first so everything downstream is in real units. Filter second, on
a value you can reason about. Clamp last, closest to whatever must not
receive nonsense.

Then take the decision with [HYST](fb-hyst.md)
rather than a bare comparison, and the whole path from sensor to relay is
quiet, readable and hard to get wrong.
