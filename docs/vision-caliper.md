<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Caliper

**Measurements** · in the trade: *caliper tool, edge pairs along a scan line* · in a project file: `caliper`

Walks along a line and finds every edge on it - the width of a part, the gap between two, the number of pins, their pitch. Teach the line by dragging it over the picture; wire a scale (mm per pixel) and the width comes in millimetres too.

![The window of the Caliper block: its settings on the left, its picture on the right](img/vb-caliper.webp){: .sb-center}

Walks along a line and finds every edge on it - every place the brightness jumps by at least `contrast` - the way a caliper tool does in a machine vision system. The first and the last edge give the *width* of a part, the number of edges counts pins or teeth, their mean spacing is the *pitch*, and every edge is handed on as an object (*edges_out*) for the geometry blocks. With a scale wired into `scale` the width and the pitch come in millimetres too, and `min`/`max` make *ok* a tolerance check on the width.

The line is dragged on the block's picture; place it across the part where the edges are clean, a little longer than the part on both sides. `polarity` keeps only the dark-to-light or the light-to-dark edges - the two sides of a dark part on a light belt are one of each, so *any* finds both; a printed stripe on the part is left out by choosing the polarity of the part's own edges. Blur or a low contrast setting finds more, noisier edges; a [Gaussian blur](vision-gauss.md) of 3 before the caliper and a contrast of 40 is a good start.

The window draws the line with every edge found on it and the width.

## Typical uses

- the width of a part, the gap between two
- the number of pins, teeth or stripes and their pitch
- the position of an edge for a geometry block

## Inputs

| Input | Type | Meaning |
|:---|:---:|:---|
| `src` | picture | the picture the line lies on |
| `scale` | number (optional) | millimetres per pixel from a Ruler or a Plane block (optional: without it width_mm is in pixels) |

## Outputs

| Output | Type | Meaning |
|:---|:---:|:---|
| `found` | yes/no | at least two edges were found |
| `width` | number | pixels between the first and the last edge |
| `edges` | number | how many edges were found |
| `first` | number | the first edge, pixels from the line's start |
| `last` | number | the last edge, pixels from the line's start |
| `pitch` | number | the mean spacing of the edges, in pixels |
| `edges_out` | list of objects | every edge as an object at its place on the line |
| `width_mm` | number | the width through the scale (px when none) |
| `pitch_mm` | number | the pitch through the scale (px when none) |
| `ok` | yes/no | the width lies between min and max (in the unit the scale gives) |

A number or a yes/no output goes into a variable of the PLC program (right-click the block on the Vision page, *Result ... into*); a text output into a STRING variable; a picture or a list of objects into the next block.

## Settings

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x1` | 0 .. 8192 | 100 | px | the line's start |
| `y1` | 0 .. 8192 | 100 | px | the line's start |
| `x2` | 0 .. 8192 | 400 | px | the line's end |
| `y2` | 0 .. 8192 | 100 | px | the line's end |
| `contrast` | 1 .. 255 | 40 |  | the jump in brightness that is an edge |
| `polarity` | any / dark_to_light / light_to_dark | any |  | which edges count |
| `min` | 0 .. 100000 | 0 |  | the width must be at least this (0 = no limit) - in mm when a scale is wired |
| `max` | 0 .. 100000 | 0 |  | the width must be at most this (0 = no limit) |

Every number and yes/no setting can be read from a **variable** before each run instead of being fixed - pick it in the list beside the setting (the variable column of [the block's window](vision.md#the-blocks-window)). A text setting takes a STRING variable the same way.

## On the block's window

- **Drag along the line** on the picture: `x1`, `y1`, `x2`, `y2` take its ends.

---

Every block: [Vision blocks](vision-blocks.md) · how a program is drawn and what its window shows: [Vision](vision.md) · the cameras: [Cameras](cameras.md)
