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

### Straighten

Takes a rectangle seen at an angle - a label, a plate, the belt from a camera on the side - and draws it straight. Teach the four corners by four clicks on the picture (top-left, top-right, bottom-right, bottom-left).

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x1` | 0 .. 8192 | 100 | px | top-left corner |
| `y1` | 0 .. 8192 | 100 | px | top-left corner |
| `x2` | 0 .. 8192 | 500 | px | top-right corner |
| `y2` | 0 .. 8192 | 100 | px | top-right corner |
| `x3` | 0 .. 8192 | 500 | px | bottom-right corner |
| `y3` | 0 .. 8192 | 400 | px | bottom-right corner |
| `x4` | 0 .. 8192 | 100 | px | bottom-left corner |
| `y4` | 0 .. 8192 | 400 | px | bottom-left corner |
| `out_w` | 8 .. 4096 | 400 | px | width of the straightened picture |
| `out_h` | 8 .. 4096 | 300 | px | height of the straightened picture |

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

### Equalize light

Spreads the brightness over the whole range - a picture under uneven or weak light gets its contrast back before a threshold.

**In:** `src` (picture)  
**Out:** `out` (picture)

### Sharpen

Makes edges crisper - helps a code reader or an edge finder on a slightly soft picture.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `amount` | 1 .. 300 | 100 | % | how much |

### Difference

The difference of two pictures, pixel by pixel - a part against the empty belt, this picture against a good one. White where they differ after the threshold.

**In:** `a` (picture), `b` (picture)  
**Out:** `out` (picture), `share` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `level` | 1 .. 255 | 30 |  | a difference above this counts |

### Motion

Where the picture changed since the last run - a mask of what moved and how much of the picture it is. The first run after a start has nothing to compare and answers nothing moved.

**In:** `src` (picture)  
**Out:** `out` (picture), `share` (number), `moved` (yes/no)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `level` | 1 .. 255 | 25 |  | a change above this counts |
| `min_share` | 0 .. 100 | 1 | % | this much of the picture must change to say moved |

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

### Find pattern

Finds where a taught picture - a mark, a logo, a part seen from above - appears, as a list of matches with their score. Teach it by dragging over the part on the block's picture.

**In:** `src` (picture)  
**Out:** `objects` (list of objects), `found` (yes/no), `x` (number), `y` (number), `score` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `pattern` | text | (empty) |  | the taught picture (a picture asset of the project) |
| `min_score` | 1 .. 100 | 80 | % | how alike a place must be to count as a match |
| `max_count` | 1 .. 50 | 1 |  | at most this many matches |

### Find lines

Finds straight lines in an edge picture (after Edges or a threshold) - the edge of a sheet, a rule, a seam - as a list of objects; each carries its angle and its length, the longest first.

**In:** `src` (picture)  
**Out:** `objects` (list of objects), `count` (number), `angle` (number), `length` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `min_len` | 1 .. 8192 | 50 | px | shorter lines are not counted |
| `max_gap` | 0 .. 500 | 10 | px | a break shorter than this is still one line |
| `votes` | 1 .. 1000 | 50 |  | how many edge points a line needs |

### Check objects

Are all the found objects right? Counts them and says yes when their number and every one's size (area) lie within the limits - parts on a tray, holes in a plate, pills in a blister.

**In:** `objects` (list of objects)  
**Out:** `ok` (yes/no), `count` (number), `bad` (number), `min_area` (number), `max_area` (number), `mean_area` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `count_min` | 0 .. 100000 | 1 |  | at least this many objects |
| `count_max` | 0 .. 100000 | 100000 |  | at most this many objects |
| `area_min` | 0 .. 100000000 | 0 | px² | an object smaller than this is bad |
| `area_max` | 0 .. 100000000 | 100000000 | px² | an object larger than this is bad |

### Pick object

Takes one object of a list - number 0 is the first after sorting - and gives its numbers.

**In:** `objects` (list of objects)  
**Out:** `found` (yes/no), `x` (number), `y` (number), `w` (number), `h` (number), `r` (number), `angle` (number), `area` (number), `score` (number)

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

## Logic

### ST code

A few lines of ST - the same language as the PLC program - over the block's inputs a, b, c, d (numbers) and p, q (yes/no); it writes y1..y4 (numbers) and r1, r2 (yes/no). Locals in VAR ... END_VAR, loops and conditions as in a program.

**In:** `a` (number, optional), `b` (number, optional), `c` (number, optional), `d` (number, optional), `p` (yes/no, optional), `q` (yes/no, optional)  
**Out:** `y1` (number), `y2` (number), `y3` (number), `y4` (number), `r1` (yes/no), `r2` (yes/no)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `src` | text | "y1 := a + b;" |  | the ST statements (a |
| `code` | text | (empty) |  | the compiled code (the editor fills it; never typed) |

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

Turns a number of pixels into millimetres (or any unit) - value x factor + offset. Connect a Ruler's mm_per_px to `factor_in` and the factor is measured, not typed.

**In:** `v` (number), `factor_in` (number, optional)  
**Out:** `value` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `factor` | -1000000 .. 1000000 | 1 |  | units per pixel |
| `offset` | -1000000 .. 1000000 | 0 |  | added after the factor |

### Ruler

A known length in the picture - drag along it and type what it is in millimetres - gives the scale of the picture (mm per pixel) for the Scale block.

**In:** `src` (picture)  
**Out:** `mm_per_px` (number), `px` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x1` | 0 .. 8192 | 100 | px | one end of the known length |
| `y1` | 0 .. 8192 | 100 | px | one end of the known length |
| `x2` | 0 .. 8192 | 300 | px | the other end |
| `y2` | 0 .. 8192 | 100 | px | the other end |
| `length` | 0.001 .. 100000 | 100 | mm | what the length really is |

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
**Out:** `found` (yes/no), `match` (yes/no), `number` (number), `text` (text)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `kind` | qr / barcode | qr |  | what kind of code |
| `expect` | text | (empty) |  | the text the code must carry (empty = any code) |

