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

### Turn and shift

Turns the picture by any angle round its middle, scales it and shifts it - the part always lies the same way for the blocks after it.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `angle` | -360 .. 360 | 0 | deg | anticlockwise |
| `scale` | 5 .. 400 | 100 | % | size of the result |
| `dx` | -8192 .. 8192 | 0 | px | shift to the right |
| `dy` | -8192 .. 8192 | 0 | px | shift down |

### Unroll ring

Unrolls a ring or a disc round a centre into a straight strip (left to right round the circle, the centre at the top) - a label round a bottle, the teeth of a gear, a dial.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `cx` | 0 .. 8192 | 320 | px | the centre |
| `cy` | 0 .. 8192 | 240 | px | the centre |
| `radius` | 1 .. 8192 | 200 | px | how far out from the centre is unrolled |

### Halve

Halves the picture once or several times with a proper blur first (an image pyramid) - a cleaner small picture than Resize for finding large things fast.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `levels` | 1 .. 4 | 1 |  | how many times it is halved |

### Lens correction

Takes the barrel or pincushion of a wide lens out of the picture, so straight edges are straight and a Ruler holds across the whole picture. The numbers come from a lens calibration (a chessboard in front of the camera).

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `fx` | 1 .. 100000 | 1000 | px | focal length across |
| `fy` | 1 .. 100000 | 1000 | px | focal length down |
| `cx` | 0 .. 8192 | 640 | px | the optical centre |
| `cy` | 0 .. 8192 | 360 | px | the optical centre |
| `k1` | -5 .. 5 | 0 |  | radial distortion |
| `k2` | -5 .. 5 | 0 |  | radial distortion |
| `p1` | -1 .. 1 | 0 |  | tangential distortion |
| `p2` | -1 .. 1 | 0 |  | tangential distortion |

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

### One channel

Takes one channel of the colour picture as a gray one - the red, the saturation, the lightness ... - the way to make a colour into something Threshold can cut.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `which` | blue / green / red / hue / saturation / value / lightness | value |  | which channel (hue is stretched to 0..255 round the colour wheel) |

### Adaptive threshold

Black and white by a level that follows the picture - each point is compared with its own neighbourhood, so uneven light or a shadow across the part does not matter.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `block` | 3 .. 255 | 11 | px | the neighbourhood (odd) |
| `c` | -50 .. 50 | 2 |  | taken off the neighbourhood's mean before comparing |
| `method` | gaussian / mean | gaussian |  | how the neighbourhood is averaged |
| `invert` | yes / no | no |  | white where it is darker instead |

### White balance

Takes a colour cast out of the picture (the gray-world rule) - a yellowish lamp or a bluish window stops shifting the colours a Colour block reads.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `strength` | 0 .. 100 | 100 | % | how much of the cast is taken out |

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

### Smooth, keep edges

Smooths noise inside areas and leaves the edges sharp (a bilateral filter) - a blur that does not wash the part into the belt.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `diameter` | 1 .. 15 | 7 | px | how far around each point is looked at |
| `colour` | 1 .. 255 | 50 |  | how different a shade may be and still be smoothed together |
| `space` | 1 .. 255 | 50 |  | how far a point still counts |

### Stretch contrast

Stretches the brightness so the darkest part of the picture becomes black and the brightest white - a dull picture becomes a clear one, whatever the light.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `low` | 0 .. 49 | 1 | % | share of the darkest points that count as black |
| `high` | 0 .. 49 | 1 | % | share of the brightest points that count as white |

### Gamma

Brightens or darkens the middle shades without touching black and white (a gamma curve) - 100 leaves the picture as it is, less brightens, more darkens.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `gamma` | 10 .. 500 | 100 | % | 100 = unchanged; 50 = brighter middle; 200 = darker middle |

### Local contrast

Raises the contrast piece by piece (CLAHE), so a dark corner and a bright corner each get their detail back - better than Equalize on uneven light.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `clip` | 0.5 .. 40 | 2 |  | how far the contrast may be pushed (more = stronger |
| `tiles` | 1 .. 32 | 8 |  | the picture is split into this many tiles each way |

### Combine pictures

Puts two pictures of the same size together - added, subtracted, the darker or the lighter of the two, a blend, or the black-and-white ones by AND / OR / XOR.

**In:** `a` (picture), `b` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `mode` | add / subtract / and_ / or_ / xor_ / min / max / blend | add |  | how the two are put together (and_ / or_ / xor_ for black-and-white pictures) |
| `share` | 0 .. 100 | 50 | % | the first picture's share in a blend |

### Mask

Keeps the picture where a black-and-white mask is white and blacks out the rest - a shape found earlier cuts out what a later block may see.

**In:** `src` (picture), `mask` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `invert` | yes / no | no |  | keep where the mask is black instead |

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

### Top-hat

Keeps only the small bright details on a dark or uneven background (a top-hat) - scratches, bright marks, text on a dark plate.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 .. 99 | 9 | px | a detail larger than this is background |
| `shape` | rect / ellipse / cross | rect |  | the shape of the structuring element |

### Black-hat

Keeps only the small dark details on a bright or uneven background (a black-hat) - dust, dark marks, printed text on a bright label.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 .. 99 | 9 | px | a detail larger than this is background |
| `shape` | rect / ellipse / cross | rect |  | the shape of the structuring element |

### Outline

The outline of every shape in a black-and-white picture (the difference of a dilate and an erode) - a thin ring round each object.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 .. 99 | 3 | px | the thickness of the outline |
| `shape` | rect / ellipse / cross | rect |  | the shape of the structuring element |

### Fill holes

Fills every hole inside the white shapes of a black-and-white picture - a ring becomes a disc, a part with a bore counts by its whole outline.

**In:** `src` (picture)  
**Out:** `out` (picture)

### Distance map

Every white point becomes as bright as it is far from the nearest black one - the middle of a thick shape shines, its rim stays dark; a way to find the widest place or to split touching parts.

**In:** `src` (picture)  
**Out:** `out` (picture)

## Edges

### Edges

White on the edges of things, black elsewhere (Canny).

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `low` | 0 .. 1000 | 50 |  | weaker edges continue a strong one above this |
| `high` | 0 .. 1000 | 150 |  | an edge starts above this |

### Gradient

How fast the brightness changes at every point (Sobel) - bright where there is an edge, black where the picture is flat. A softer edge picture than Edges, with the strength kept.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `direction` | both / x / y | both |  | edges across (x) |
| `size` | 1 / 3 / 5 / 7 | 3 |  | the size of the kernel - larger sees softer edges |

### Laplacian

The second change of brightness (Laplacian) - lights up the fine detail and the edges in every direction at once; also what Sharpness measures.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `size` | 1 / 3 / 5 | 3 |  | the size of the kernel |

### Gradient (fine)

Like Gradient, with the Scharr kernel - more exact on the direction of thin edges.

**In:** `src` (picture)  
**Out:** `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `direction` | both / x / y | both |  | edges across (x) |

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

### Filter objects

Keeps only the objects of a list that look right - by area, by how round they are, by how elongated, by how solid (a ring or a C is not solid). The rest are dropped.

**In:** `objects` (list of objects)  
**Out:** `kept` (list of objects), `count` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `area_min` | 0 .. 100000000 | 0 | px² | smallest area kept |
| `area_max` | 0 .. 100000000 | 100000000 | px² | largest area kept |
| `round_min` | 0 .. 100 | 0 | % | least roundness kept (a disc is 100 |
| `round_max` | 0 .. 100 | 100 | % | most roundness kept |
| `aspect_max` | 1 .. 1000 | 1000 |  | longest side over shortest side |
| `solid_min` | 0 .. 100 | 0 | % | least solidity kept (a filled shape is 100 |

### Object shape

Measures the shape of one object of a list - how round, how solid, how elongated, its turned frame and its angle. For checking a part is the right shape, not only there.

**In:** `objects` (list of objects)  
**Out:** `found` (yes/no), `roundness` (number), `solidity` (number), `aspect` (number), `perimeter` (number), `w` (number), `h` (number), `angle` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `index` | 0 .. 999 | 0 |  | which object of the list |

### Nearest object

Which object of a list lies closest to a point - the one under the gripper, the one at the mark.

**In:** `objects` (list of objects)  
**Out:** `found` (yes/no), `index` (number), `x` (number), `y` (number), `dist` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `px` | 0 .. 8192 | 320 | px | the point |
| `py` | 0 .. 8192 | 240 | px | the point |

### Find corners

Finds the strong corners of the picture (Shi-Tomasi) as a list of points - the corners of a plate, the ends of a slot.

**In:** `src` (picture)  
**Out:** `objects` (list of objects), `count` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `max_count` | 1 .. 500 | 50 |  | at most this many corners |
| `quality` | 1 .. 100 | 10 | % | a corner weaker than this share of the strongest is dropped |
| `min_dist` | 1 .. 500 | 10 | px | two corners closer than this are one |

### Fill from point

Starts at a point and takes every neighbouring point of a similar shade - the whole part under the point becomes a white shape, whatever its outline.

**In:** `src` (picture)  
**Out:** `out` (picture), `area` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 320 | px | the starting point |
| `y` | 0 .. 8192 | 240 | px | the starting point |
| `tolerance` | 0 .. 255 | 20 |  | how different a neighbour's shade may be and still belong |

### Find by features

Finds a taught picture even when it is turned or nearer or farther from the camera (ORB feature matching) - a logo, a printed mark, a part at any angle. Teach it by dragging over the part on the block's picture.

**In:** `src` (picture)  
**Out:** `objects` (list of objects), `found` (yes/no), `x` (number), `y` (number), `angle` (number), `scale` (number), `matches` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `pattern` | text | (empty) |  | the taught picture (one of the project's pictures) |
| `min_matches` | 4 .. 500 | 12 |  | at least this many matching features make a find |

### Find markers

Finds ArUco / AprilTag markers - printed squares with a code - and gives each one's number, place and angle. A cheap, exact way to know where a fixture, a tray or a robot is.

**In:** `src` (picture)  
**Out:** `objects` (list of objects), `count` (number), `id` (number), `x` (number), `y` (number), `angle` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `dictionary` | aruco_4x4_50 / aruco_5x5_100 / aruco_6x6_250 / aruco_7x7_50 / apriltag_36h11 | aruco_4x4_50 |  | the family the markers were printed from |

### Find chessboard

Finds the inner corners of a chessboard in the picture - the pattern a lens calibration and a camera-to-table check are done with.

**In:** `src` (picture)  
**Out:** `found` (yes/no), `objects` (list of objects), `count` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `cols` | 2 .. 30 | 9 |  | inner corners across |
| `rows` | 2 .. 30 | 6 |  | inner corners down |

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

### Caliper

Walks along a line and finds every edge on it - the width of a part, the gap between two, the number of pins. Teach the line by dragging it over the picture.

**In:** `src` (picture)  
**Out:** `found` (yes/no), `width` (number), `edges` (number), `first` (number), `last` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x1` | 0 .. 8192 | 100 | px | the line's start |
| `y1` | 0 .. 8192 | 100 | px | the line's start |
| `x2` | 0 .. 8192 | 400 | px | the line's end |
| `y2` | 0 .. 8192 | 100 | px | the line's end |
| `contrast` | 1 .. 255 | 40 |  | the jump in brightness that is an edge |
| `polarity` | any / dark_to_light / light_to_dark | any |  | which edges count |

### Brightness statistics

The mean, the darkest, the brightest and the spread of the brightness in an area - for a check that a lamp works, a surface is even, a print is there.

**In:** `src` (picture)  
**Out:** `mean` (number), `min` (number), `max` (number), `spread` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 0 | px | left edge of the area |
| `y` | 0 .. 8192 | 0 | px | top edge of the area |
| `w` | 1 .. 8192 | 200 | px | width of the area |
| `h` | 1 .. 8192 | 200 | px | height of the area |

### Sharpness

How sharp the picture is in an area (the variance of the Laplacian) - a camera knocked out of focus, a lens fogged up, a print smudged. Yes when it is at least the limit.

**In:** `src` (picture)  
**Out:** `ok` (yes/no), `value` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 0 | px | left edge of the area |
| `y` | 0 .. 8192 | 0 | px | top edge of the area |
| `w` | 1 .. 8192 | 200 | px | width of the area |
| `h` | 1 .. 8192 | 200 | px | height of the area |
| `min` | 0 .. 1000000 | 100 |  | the sharpness that is still fine (read the value on a good picture |

### Histogram

How the shades are spread in an area - the most common shade, the share of dark points and of light ones.

**In:** `src` (picture)  
**Out:** `peak` (number), `dark` (number), `light` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `x` | 0 .. 8192 | 0 | px | left edge of the area |
| `y` | 0 .. 8192 | 0 | px | top edge of the area |
| `w` | 1 .. 8192 | 200 | px | width of the area |
| `h` | 1 .. 8192 | 200 | px | height of the area |
| `dark_below` | 0 .. 255 | 64 |  | a point darker than this is dark |
| `light_above` | 0 .. 255 | 192 |  | a point brighter than this is light |

### Distance

The distance and the direction between two points given as numbers - from two Pick blocks, two markers, a corner and a hole.

**In:** `x1` (number, optional), `y1` (number, optional), `x2` (number, optional), `y2` (number, optional)  
**Out:** `dist` (number), `angle` (number), `dx` (number), `dy` (number)

### Compare with taught

Compares an area with the same area taught on a good part and says how much differs - a missing print, a wrong label, a scratch. Teach by dragging over the area on the block's picture.

**In:** `src` (picture)  
**Out:** `ok` (yes/no), `diff` (number), `out` (picture)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `pattern` | text | (empty) |  | the taught picture of the area (one of the project's pictures) |
| `x` | 0 .. 8192 | 0 | px | left edge of the area |
| `y` | 0 .. 8192 | 0 | px | top edge of the area |
| `w` | 1 .. 8192 | 200 | px | width of the area |
| `h` | 1 .. 8192 | 200 | px | height of the area |
| `level` | 1 .. 255 | 40 |  | a point that differs by more than this counts |
| `max_diff` | 0 .. 100 | 5 | % | the share of differing points that is still fine |

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

### Match shape

Is one of the found objects the taught shape, whatever its size or turn (Hu moments)? Teach by dragging over a good part on the block's picture - its outline is the reference.

**In:** `objects` (list of objects)  
**Out:** `ok` (yes/no), `index` (number), `diff` (number)

| Setting | Range | Default | Unit | Meaning |
|:---|:---:|:---:|:---:|:---|
| `pattern` | text | (empty) |  | the taught picture the outline is taken from (one of the project's pictures) |
| `max_diff` | 0 .. 10 | 0.5 |  | how different the closest object's outline may be (0 = the same shape) |

