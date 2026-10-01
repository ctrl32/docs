<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Unroll ring

**Geometry** · in the trade: *polar unwrap (log-polar transform)* · in a project file: `polar`

Unrolls a ring or a disc round a centre into a straight strip (left to right round the circle, the centre at the top) - a label round a bottle, the teeth of a gear, a dial.

![The window of the Unroll ring block: its settings on the left, its picture on the right](img/vb-polar.webp){: .sb-center}

Unrolls a ring or a disc round a centre into a straight strip: the circle becomes the strip's width (left to right, once round), the radius becomes its height (the centre at the top, the outer edge at the bottom). A label wrapped round a bottle, the teeth of a gear, the marks of a dial, the print round the rim of a cap become a straight line of things that [Caliper](vision-caliper.md), [Read code](vision-code.md) and [Find objects](vision-contours.md) handle as on a flat part.

Type the centre (the part's axis - read it off the block's picture, which draws the centre and the radius) and the radius to the outer edge of what should be unrolled. When the part does not always stop at the same place, let a [Fixture](vision-fixture.md) before it put the part where it was taught.

## Typical uses

- a label wrapped round a bottle
- the teeth of a gear counted with a Caliper
- the print round the rim of a cap

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture with the ring or disc |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `out` | picture | the strip: the circle along its width, the radius down its height |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `cx` | 0 .. 8192 | 320 | px | the centre |
| `cy` | 0 .. 8192 | 240 | px | the centre |
| `radius` | 1 .. 8192 | 200 | px | how far out from the centre is unrolled |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](vision.md#the-blocks-window)). A text setting takes a STRING variable the same way.

---

Every block: [Vision blocks](vision-blocks.md) · how a program is drawn and what its window shows: [Vision](vision.md) · the cameras: [Cameras](cameras.md)
