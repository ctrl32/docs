---
image: img/blk-move-ld.webp
image_alt: "MOVE in the editor"
---

# MOVE

OUT = IN - the IEC assignment as a block.

![MOVE on a rung](img/blk-move-ld.webp){: .sb-center}

![MOVE on a WEBview screen](img/blk-move-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MOVE_ST
  move_out_st := move_in;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN` | input | REAL | - | The source. |
| `OUT` | output | REAL | - | The destination. |

## Description

It looks like it does nothing, and in a diagram it nearly does - its job
is to get a value from one variable into another (a tag-to-tag copy).
Where it earns its keep is **in a ladder rung**, as the plain result
box: while the rung conducts, the value is committed; while it does not,
the destination holds.

```
recipe_ready ──[ MOVE IN=recipe_temp ]── OUT ──> setpoint
```

The setpoint takes the recipe value the moment the recipe is ready, and
keeps it afterwards. That "commit a value when a condition is met" is
one of the most common things a control program does.

---

Every block of the family: [Maths](blocks-math.md) · every block: [Function blocks](blocks.md)
