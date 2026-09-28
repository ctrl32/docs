<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Vision blocks

Every block a vision program is drawn from, with its settings. The same list is the block palette of the editor's Vision page, and a block's settings window shows exactly these settings. How a program is put together: [Vision](vision.md).

Areas are in pixels of the picture the block receives. A picture goes into a picture input, a number into a number input.

## Source

### Camera

The latest picture of one of the project's cameras.

**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `camera` | text | (empty) |  | the camera's name in the project |

## Geometry

### Crop

Keeps one rectangle of the picture - later blocks see only that area.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 0 | px | left edge |
| `y` | 0 .. 8192 | 0 | px | top edge |
| `w` | 1 .. 8192 | 320 | px | width |
| `h` | 1 .. 8192 | 240 | px | height |

### Resize

Scales the picture - a smaller picture is analysed faster.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `scale` | 5 .. 400 | 50 | % | size of the result |

### Rotate

Turns the picture by a quarter, a half or three quarters.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `angle` | 90 / 180 / 270 | 90 |  | clockwise |

### Flip

Mirrors the picture.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `axis` | horizontal / vertical / both | horizontal |  | which way |

## Colour

### Grayscale

Turns a colour picture into shades of gray.

**In:** `src` (picture)  
**Out:** `out` (picture)

### Colour range

White where the colour is inside the range, black elsewhere. Hue runs 0..179 around the colour wheel (red at 0, green at 60, blue at 120).

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `h_lo` | 0 .. 179 | 0 |  | lowest hue |
| `h_hi` | 0 .. 179 | 179 |  | highest hue (below the lowest wraps round red) |
| `s_lo` | 0 .. 255 | 60 |  | lowest saturation |
| `s_hi` | 0 .. 255 | 255 |  | highest saturation |
| `v_lo` | 0 .. 255 | 40 |  | lowest brightness |
| `v_hi` | 0 .. 255 | 255 |  | highest brightness |

### Threshold

White where the picture is brighter than the level, black elsewhere.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `level` | 0 .. 255 | 128 |  | brightness that splits black from white |
| `invert` | yes / no | no |  | white where it is darker instead |

### Automatic threshold

Finds the level that best splits the picture into two, by itself (Otsu's method).

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `invert` | yes / no | no |  | white where it is darker instead |

### Invert

Black becomes white and white black.

**In:** `src` (picture)  
**Out:** `out` (picture)

## Filters

### Blur

Averages each pixel with its neighbours - calms noise.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 .. 99 | 5 | px | size of the neighbourhood |

### Gaussian blur

A softer blur that keeps edges better than the plain one.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 .. 99 | 5 | px | size of the neighbourhood (odd) |

### Median

Removes specks and salt-and-pepper noise, keeps edges sharp.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 .. 99 | 5 | px | size of the neighbourhood (odd) |

## Shapes

### Erode

Shrinks white areas - removes thin lines and small specks.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 .. 51 | 3 | px | size of the brush |
| `times` | 1 .. 20 | 1 |  | how many times |

### Dilate

Grows white areas - closes small gaps.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 .. 51 | 3 | px | size of the brush |
| `times` | 1 .. 20 | 1 |  | how many times |

### Open

Erode, then dilate - removes specks and keeps the size of large areas.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 .. 51 | 3 | px | size of the brush |

### Close

Dilate, then erode - fills small holes and keeps the size of large areas.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 .. 51 | 3 | px | size of the brush |

## Edges

### Edges

White on the edges of things, black elsewhere (Canny).

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `low` | 0 .. 1000 | 50 |  | weaker edges continue a strong one above this |
| `high` | 0 .. 1000 | 150 |  | an edge starts above this |

## Finding objects

### Find objects

Finds the separate white areas of a black-and-white picture as a list of objects - each with its centre, frame, angle and area - sorted as chosen.

**In:** `src` (picture)  
**Out:** `objects` (list of objects), `count` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `min_area` | 1 .. 10000000 | 50 | px² | smaller areas are not objects |
| `max_area` | 1 .. 100000000 | 100000000 | px² | larger areas are not objects |
| `sort` | largest / left_to_right / top_to_bottom | largest |  | which object is number 0 |

### Find circles

Finds round things in the picture - holes, caps, bearings - as a list of objects with their centre and radius.

**In:** `src` (picture)  
**Out:** `objects` (list of objects), `count` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `min_r` | 1 .. 4096 | 10 | px | smallest radius |
| `max_r` | 1 .. 4096 | 200 | px | largest radius |
| `min_dist` | 1 .. 4096 | 20 | px | two centres closer than this are one circle |
| `edge` | 1 .. 1000 | 300 |  | the contrast of the circle's edge |
| `roundness` | 1 .. 100 | 80 | % | how perfect a circle must be (lower finds more |
| `sort` | largest / left_to_right / top_to_bottom | largest |  | which circle is number 0 |

### Pick object

Takes one object of a list - number 0 is the first after sorting - and gives its numbers.

**In:** `objects` (list of objects)  
**Out:** `found` (yes/no), `x` (number), `y` (number), `w` (number), `h` (number), `r` (number), `angle` (number), `area` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `index` | 0 .. 10000 | 0 |  | which object (0 = the first) |

### Crop to object

Keeps the frame around one found object, with a margin - the next blocks look only where the part really is, wherever it lies.

**In:** `src` (picture), `objects` (list of objects)  
**Out:** `out` (picture), `found` (yes/no)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `index` | 0 .. 10000 | 0 |  | which object (0 = the first) |
| `margin` | 0 .. 4096 | 10 | px | added around the object's frame |

## Measurements

### Brightness

The average brightness of the picture, 0 (black) to 255 (white).

**In:** `src` (picture)  
**Out:** `value` (number)

### White share

How much of the picture is white, in percent - use it after a threshold or a colour range.

**In:** `src` (picture)  
**Out:** `value` (number)

### Count objects

Counts the separate white areas of a black-and-white picture, and reports the largest one.

**In:** `src` (picture)  
**Out:** `count` (number), `x` (number), `y` (number), `area` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `min_area` | 1 .. 10000000 | 50 | px² | smaller areas are not counted |

### Scale

Turns a number of pixels into millimetres (or any unit) - value x factor + offset.

**In:** `v` (number)  
**Out:** `value` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `factor` | -1000000 .. 1000000 | 1 |  | units per pixel |
| `offset` | -1000000 .. 1000000 | 0 |  | added after the factor |

### In range

Yes when the number lies between the two limits (both included).

**In:** `v` (number)  
**Out:** `ok` (yes/no)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `min` | -1000000 .. 1000000 | 0 |  | lowest good value |
| `max` | -1000000 .. 1000000 | 100 |  | highest good value |

## Ready tools

### Presence

Is something there? Measures the brightness of an area and says yes when it lies between the two limits.

**In:** `src` (picture)  
**Out:** `present` (yes/no), `level` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 0 | px | left edge of the area |
| `y` | 0 .. 8192 | 0 | px | top edge of the area |
| `w` | 1 .. 8192 | 100 | px | width of the area |
| `h` | 1 .. 8192 | 100 | px | height of the area |
| `min` | 0 .. 255 | 0 |  | darkest brightness that means "present" |
| `max` | 0 .. 255 | 100 |  | brightest brightness that means "present" |

### Colour check

Is the area the right colour? Counts the pixels of the area near the taught hue and says yes when enough of them are.

**In:** `src` (picture)  
**Out:** `match` (yes/no), `share` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 0 | px | left edge of the area |
| `y` | 0 .. 8192 | 0 | px | top edge of the area |
| `w` | 1 .. 8192 | 100 | px | width of the area |
| `h` | 1 .. 8192 | 100 | px | height of the area |
| `hue` | 0 .. 179 | 0 |  | the colour (red 0 |
| `tolerance` | 1 .. 90 | 10 |  | how far from the hue still counts |
| `sat_min` | 0 .. 255 | 60 |  | grays below this saturation never count |
| `val_min` | 0 .. 255 | 40 |  | pixels darker than this never count |
| `min_share` | 0 .. 100 | 50 | % | share of the area that must match |

### Edge position

Where is the edge? Walks across an area in one direction and reports the first place the brightness jumps.

**In:** `src` (picture)  
**Out:** `found` (yes/no), `position` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 0 | px | left edge of the area |
| `y` | 0 .. 8192 | 0 | px | top edge of the area |
| `w` | 1 .. 8192 | 200 | px | width of the area |
| `h` | 1 .. 8192 | 20 | px | height of the area |
| `direction` | left_to_right / right_to_left / top_to_bottom / bottom_to_top | left_to_right |  | which way to walk |
| `contrast` | 1 .. 255 | 40 |  | the jump in brightness that is an edge |

### Read code

Reads a QR code or a barcode and checks it against the expected text.

**In:** `src` (picture)  
**Out:** `found` (yes/no), `match` (yes/no), `number` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `kind` | qr / barcode | qr |  | what kind of code |
| `expect` | text | (empty) |  | the text the code must carry (empty = any code) |

