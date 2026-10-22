---
title: "Vision blocks"
slug: vision-blocks
section: "Vision"
order: 213
sidebar_position: 213
generator: tools/docs_export.py
---

<!-- AUTOMATICALLY GENERATED from schema/visu-vision.yaml (tools/gen_vision.py) -->

# Vision blocks

**89 blocks, every one with its own page, its own window and its own picture.** The toolset of a machine vision system - region of interest, filters, binarisation, morphology, blob analysis, template and feature matching, fiducial markers, calibration, calipers and gauges in millimetres, 1D/2D code reading, laser triangulation, trained neural networks - drawn as a chain of blocks on the [Vision](/docs/vision/) page, no programming. Every block is a row of one table: the same table the editor builds the block's window from and the device runs, so what you set at your desk is what the device computes.

Every page says what the block does and when to use it, lists every input, output and setting with its range and default, and shows the block's window on a test picture. Areas are in pixels of the picture the block receives; a picture goes into a picture input, a number into a number input, a list of objects into a list input.

| Port type | What travels | Where it may go |
|:---|:---|:---|
| picture | a colour, gray or black-and-white picture | a picture input, a camera element on a screen |
| number | a measurement or a count | a number input, a variable |
| yes/no | a check's answer | a yes/no input, a BOOL variable |
| list of objects | found things with their place, size, angle and area | a list input |
| text | what a code says, a model's label | a text input, a STRING variable |

## Source

Where the pictures come from.

| Block | In the trade | What it does |
|:---|:---|:---|
| [Camera](/docs/vision/vision-camera/) | image acquisition | The latest picture of one of the project's cameras. |

## Geometry

Cut, scale, turn and straighten the picture, and lock it to the part or to the working plane - so that every block after it looks at the right place, in millimetres.

| Block | In the trade | What it does |
|:---|:---|:---|
| [Crop](/docs/vision/vision-crop/) | region of interest (ROI) | Keeps one rectangle of the picture - later blocks see only that area. |
| [Resize](/docs/vision/vision-resize/) | resampling, scaling | Scales the picture - a smaller picture is analysed faster. |
| [Rotate](/docs/vision/vision-rotate/) | rotation by right angles | Turns the picture by a quarter, a half or three quarters. |
| [Straighten](/docs/vision/vision-warp/) | perspective correction (homography) | Takes a rectangle seen at an angle - a label, a plate, the belt from a camera on the side - and draws it straight. Teach the four corners by four clicks on the picture (top-left, top-right, bottom-right, bottom-left). |
| [Flip](/docs/vision/vision-flip/) | mirroring | Mirrors the picture. |
| [Turn and shift](/docs/vision/vision-affine/) | affine transform (rotation, scale, translation) | Turns the picture by any angle round its middle, scales it and shifts it - the part always lies the same way for the blocks after it. |
| [Unroll ring](/docs/vision/vision-polar/) | polar unwrap (log-polar transform) | Unrolls a ring or a disc round a centre into a straight strip (left to right round the circle, the centre at the top) - a label round a bottle, the teeth of a gear, a dial. |
| [Halve](/docs/vision/vision-pyramid/) | image pyramid (pyrDown) | Halves the picture once or several times with a proper blur first (an image pyramid) - a cleaner small picture than Resize for finding large things fast. |
| [Lens correction](/docs/vision/vision-undistort/) | intrinsic calibration, lens distortion correction | Takes the barrel or pincushion of a wide lens out of the picture, so straight edges are straight and a Ruler holds across the whole picture. The numbers come from a lens calibration (a chessboard in front of the camera). |
| [Fixture](/docs/vision/vision-fixture/) | fixturing, part location, pattern-based alignment | Finds the part by a taught picture and shifts the whole picture so the part sits where it was when taught - every later block keeps its areas wherever the part lies on the belt. Teach by dragging over the part on the block's picture. |
| [Plane from a board](/docs/vision/vision-world/) | camera-to-world calibration, plane rectification (homography) | A chessboard lying on the working plane, seen once, teaches how the camera sees that plane - the block then straightens every picture to a top view with a known number of pixels per millimetre, so every measurement on it is millimetres. Teach with the button on the block's window. |

## Colour

From a colour picture to the gray picture or the black-and-white one the finders and the gauges work on.

| Block | In the trade | What it does |
|:---|:---|:---|
| [Grayscale](/docs/vision/vision-gray/) | grayscale conversion | Turns a colour picture into shades of gray. |
| [Colour range](/docs/vision/vision-hsv_range/) | HSV colour segmentation, colour thresholding | White where the colour is inside the range, black elsewhere. Hue runs 0..179 around the colour wheel (red at 0, green at 60, blue at 120). |
| [Threshold](/docs/vision/vision-threshold/) | binarisation, fixed threshold | White where the picture is brighter than the level, black elsewhere. |
| [Automatic threshold](/docs/vision/vision-otsu/) | automatic binarisation (Otsu's method) | Finds the level that best splits the picture into two, by itself (Otsu's method). |
| [Invert](/docs/vision/vision-invert/) | image inversion | Black becomes white and white black. |
| [One channel](/docs/vision/vision-channel/) | colour plane extraction | Takes one channel of the colour picture as a gray one - the red, the saturation, the lightness ... - the way to make a colour into something Threshold can cut. |
| [Adaptive threshold](/docs/vision/vision-adaptive/) | adaptive (local) threshold | Black and white by a level that follows the picture - each point is compared with its own neighbourhood, so uneven light or a shadow across the part does not matter. |
| [White balance](/docs/vision/vision-balance/) | white balance (gray-world) | Takes a colour cast out of the picture (the gray-world rule) - a yellowish lamp or a bluish window stops shifting the colours a Colour block reads. |

## Filters

Noise out, contrast in, light evened - the picture made ready for a reliable threshold or reader.

| Block | In the trade | What it does |
|:---|:---|:---|
| [Blur](/docs/vision/vision-blur/) | box filter (mean filter) | Averages each pixel with its neighbours - calms noise. |
| [Gaussian blur](/docs/vision/vision-gauss/) | Gaussian filter | A softer blur that keeps edges better than the plain one. |
| [Median](/docs/vision/vision-median/) | median filter | Removes specks and salt-and-pepper noise, keeps edges sharp. |
| [Equalize light](/docs/vision/vision-equalize/) | histogram equalisation | Spreads the brightness over the whole range - a picture under uneven or weak light gets its contrast back before a threshold. |
| [Sharpen](/docs/vision/vision-sharpen/) | unsharp masking | Makes edges crisper - helps a code reader or an edge finder on a slightly soft picture. |
| [Difference](/docs/vision/vision-absdiff/) | image subtraction, frame differencing | The difference of two pictures, pixel by pixel - a part against the empty belt, this picture against a good one. White where they differ after the threshold. |
| [Motion](/docs/vision/vision-motion/) | motion detection, frame differencing | Where the picture changed since the last run - a mask of what moved and how much of the picture it is. The first run after a start has nothing to compare and answers nothing moved. |
| [Smooth, keep edges](/docs/vision/vision-bilateral/) | bilateral filter (edge-preserving smoothing) | Smooths noise inside areas and leaves the edges sharp (a bilateral filter) - a blur that does not wash the part into the belt. |
| [Stretch contrast](/docs/vision/vision-normalize/) | contrast stretching, intensity normalisation | Stretches the brightness so the darkest part of the picture becomes black and the brightest white - a dull picture becomes a clear one, whatever the light. |
| [Gamma](/docs/vision/vision-gamma/) | gamma correction | Brightens or darkens the middle shades without touching black and white (a gamma curve) - 100 leaves the picture as it is, less brightens, more darkens. |
| [Local contrast](/docs/vision/vision-clahe/) | CLAHE (contrast limited adaptive histogram equalisation) | Raises the contrast piece by piece (CLAHE), so a dark corner and a bright corner each get their detail back - better than Equalize on uneven light. |
| [Combine pictures](/docs/vision/vision-combine/) | image arithmetic, boolean image operations | Puts two pictures of the same size together - added, subtracted, the darker or the lighter of the two, a blend, or the black-and-white ones by AND / OR / XOR. |
| [Mask](/docs/vision/vision-mask/) | masking | Keeps the picture where a black-and-white mask is white and blacks out the rest - a shape found earlier cuts out what a later block may see. |

## Shapes

The shapes of a black-and-white picture cleaned, filled, outlined, separated.

| Block | In the trade | What it does |
|:---|:---|:---|
| [Erode](/docs/vision/vision-erode/) | morphological erosion | Shrinks white areas - removes thin lines and small specks. |
| [Dilate](/docs/vision/vision-dilate/) | morphological dilation | Grows white areas - closes small gaps. |
| [Open](/docs/vision/vision-open/) | morphological opening | Erode, then dilate - removes specks and keeps the size of large areas. |
| [Close](/docs/vision/vision-close/) | morphological closing | Dilate, then erode - fills small holes and keeps the size of large areas. |
| [Top-hat](/docs/vision/vision-tophat/) | top-hat transform (white top-hat) | Keeps only the small bright details on a dark or uneven background (a top-hat) - scratches, bright marks, text on a dark plate. |
| [Black-hat](/docs/vision/vision-blackhat/) | black-hat transform | Keeps only the small dark details on a bright or uneven background (a black-hat) - dust, dark marks, printed text on a bright label. |
| [Outline](/docs/vision/vision-gradient/) | morphological gradient | The outline of every shape in a black-and-white picture (the difference of a dilate and an erode) - a thin ring round each object. |
| [Fill holes](/docs/vision/vision-fill_holes/) | hole filling | Fills every hole inside the white shapes of a black-and-white picture - a ring becomes a disc, a part with a bore counts by its whole outline. |
| [Distance map](/docs/vision/vision-distance/) | distance transform | Every white point becomes as bright as it is far from the nearest black one - the middle of a thick shape shines, its rim stays dark; a way to find the widest place or to split touching parts. |

## Edges

Where the brightness changes: the edge pictures the line and circle finders work on.

| Block | In the trade | What it does |
|:---|:---|:---|
| [Edges](/docs/vision/vision-canny/) | edge detection (Canny) | White on the edges of things, black elsewhere (Canny). |
| [Gradient](/docs/vision/vision-sobel/) | gradient magnitude (Sobel) | How fast the brightness changes at every point (Sobel) - bright where there is an edge, black where the picture is flat. A softer edge picture than Edges, with the strength kept. |
| [Laplacian](/docs/vision/vision-laplacian/) | Laplacian operator | The second change of brightness (Laplacian) - lights up the fine detail and the edges in every direction at once; also what Sharpness measures. |
| [Gradient (fine)](/docs/vision/vision-scharr/) | gradient (Scharr operator) | Like Gradient, with the Scharr kernel - more exact on the direction of thin edges. |

## Finding objects

Things located and listed - blobs, circles, lines, taught patterns, markers - with their place, size and shape.

| Block | In the trade | What it does |
|:---|:---|:---|
| [Find objects](/docs/vision/vision-contours/) | blob analysis, connected components, contour extraction | Finds the separate white areas of a black-and-white picture as a list of objects - each with its centre, frame, angle and area - sorted as chosen. |
| [Find circles](/docs/vision/vision-circles/) | Hough circle transform | Finds round things in the picture - holes, caps, bearings - as a list of objects with their centre and radius. |
| [Find pattern](/docs/vision/vision-pattern/) | template matching (normalised cross-correlation) | Finds where a taught picture - a mark, a logo, a part seen from above - appears, as a list of matches with their score. Teach it by dragging over the part on the block's picture. |
| [Find lines](/docs/vision/vision-lines/) | Hough line transform | Finds straight lines in an edge picture (after Edges or a threshold) - the edge of a sheet, a rule, a seam - as a list of objects; each carries its angle and its length, the longest first. |
| [Check objects](/docs/vision/vision-objcheck/) | count and size verification of blobs | Are all the found objects right? Counts them and says yes when their number and every one's size (area) lie within the limits - parts on a tray, holes in a plate, pills in a blister. |
| [Pick object](/docs/vision/vision-pick/) | blob result extraction | Takes one object of a list - number 0 is the first after sorting - and gives its numbers. |
| [Crop to object](/docs/vision/vision-crop_object/) | dynamic region of interest | Keeps the frame around one found object, with a margin - the next blocks look only where the part really is, wherever it lies. |
| [Filter objects](/docs/vision/vision-filter_objects/) | blob filtering by shape features | Keeps only the objects of a list that look right - by area, by how round they are, by how elongated, by how solid (a ring or a C is not solid). The rest are dropped. |
| [Object shape](/docs/vision/vision-object_shape/) | shape descriptors (blob features) | Measures the shape of one object of a list - how round, how solid, how elongated, its turned frame and its angle. For checking a part is the right shape, not only there. |
| [Nearest object](/docs/vision/vision-nearest/) | nearest blob to a point | Which object of a list lies closest to a point - the one under the gripper, the one at the mark. |
| [Find corners](/docs/vision/vision-corners/) | corner detection (Shi-Tomasi) | Finds the strong corners of the picture (Shi-Tomasi) as a list of points - the corners of a plate, the ends of a slot. |
| [Fill from point](/docs/vision/vision-floodfill/) | region growing (flood fill) | Starts at a point and takes every neighbouring point of a similar shade - the whole part under the point becomes a white shape, whatever its outline. |
| [Find by features](/docs/vision/vision-features/) | feature matching (ORB keypoints) | Finds a taught picture even when it is turned or nearer or farther from the camera (ORB feature matching) - a logo, a printed mark, a part at any angle. Teach it by dragging over the part on the block's picture. |
| [Find markers](/docs/vision/vision-aruco/) | fiducial markers (ArUco, AprilTag) | Finds ArUco / AprilTag markers - printed squares with a code - and gives each one's number, place and angle. A cheap, exact way to know where a fixture, a tray or a robot is. |
| [Find chessboard](/docs/vision/vision-chessboard/) | calibration target detection | Finds the inner corners of a chessboard in the picture - the pattern a lens calibration and a camera-to-table check are done with. |
| [Colour of object](/docs/vision/vision-object_colour/) | blob colour classification | The mean colour of every found object (its hue), and the ones inside a hue range kept - one pass sorts the red, green and blue cubes instead of one Colour range branch per colour. |

## Logic

A calculation of your own, in ST.

| Block | In the trade | What it does |
|:---|:---|:---|
| [ST code](/docs/vision/vision-st/) | scripting inside the vision program (IEC 61131-3 Structured Text) | A few lines of ST - the same language as the PLC program - over the block's inputs a, b, c, d (numbers) and p, q (yes/no); it writes y1..y4 (numbers) and r1, r2 (yes/no). Locals in VAR ... END_VAR, loops and conditions as in a program. |

## Measurements

Numbers with a tolerance: levels, diameters, widths, angles, distances, brightness, sharpness - in pixels, and in millimetres with a scale.

| Block | In the trade | What it does |
|:---|:---|:---|
| [Brightness](/docs/vision/vision-brightness/) | mean intensity | The average brightness of the picture, 0 (black) to 255 (white). |
| [White share](/docs/vision/vision-white_ratio/) | area fraction, pixel count | How much of the picture is white, in percent - use it after a threshold or a colour range. |
| [Count objects](/docs/vision/vision-blobs/) | blob count, connected components | Counts the separate white areas of a black-and-white picture, and reports the largest one. |
| [Scale](/docs/vision/vision-scale/) | pixel-to-unit conversion, calibration factor | Turns a number of pixels into millimetres (or any unit) - value x factor + offset. Connect a Ruler's mm_per_px to `factor_in` and the factor is measured, not typed. |
| [Ruler](/docs/vision/vision-ruler/) | scale calibration, pixel size | A known length in the picture - drag along it and type what it is in millimetres - gives the scale of the picture (mm per pixel) for the Scale block. |
| [In range](/docs/vision/vision-in_range/) | tolerance check, pass/fail | Yes when the number lies between the two limits (both included). |
| [Caliper](/docs/vision/vision-caliper/) | caliper tool, edge pairs along a scan line | Walks along a line and finds every edge on it - the width of a part, the gap between two, the number of pins, their pitch. Teach the line by dragging it over the picture; wire a scale (mm per pixel) and the width comes in millimetres too. |
| [Brightness statistics](/docs/vision/vision-stats/) | intensity statistics | The mean, the darkest, the brightest and the spread of the brightness in an area - for a check that a lamp works, a surface is even, a print is there. |
| [Sharpness](/docs/vision/vision-sharpness/) | focus measure, variance of the Laplacian | How sharp the picture is in an area (the variance of the Laplacian) - a camera knocked out of focus, a lens fogged up, a print smudged. Yes when it is at least the limit. |
| [Histogram](/docs/vision/vision-histogram/) | intensity histogram | How the shades are spread in an area - the most common shade, the share of dark points and of light ones. |
| [Distance](/docs/vision/vision-dist/) | point-to-point distance and direction | The distance and the direction between two points given as numbers - from two Pick blocks, two markers, a corner and a hole. |
| [Compare with taught](/docs/vision/vision-golden/) | golden template comparison, image subtraction | Compares an area with the same area taught on a good part and says how much differs - a missing print, a wrong label, a scratch. Teach by dragging over the area on the block's picture. |
| [Fill level](/docs/vision/vision-level/) | edge-based level detection, fill height gauging | The first change of brightness down (or up) a window, averaged across its width - the level of a liquid in a bottle, of a powder in a jar - as pixels from the window's bottom edge and, with a scale, in millimetres; with a tolerance. |
| [Circle (fit)](/docs/vision/vision-circle_fit/) | circle gauge, least-squares circle fit with outlier rejection | An edge on every ray of a ring, a least squares circle through them without the stray points - the diameter and the centre of a hole, a shaft, a lid, with roundness and a tolerance. |
| [Line (fit)](/docs/vision/vision-line_fit/) | line gauge, robust line fit | An edge on every scan across a window, a robust line through them - the angle of a part's edge, its position, its straightness, with a tolerance on the angle. |
| [Angle](/docs/vision/vision-angle/) | angle gauge | The angle between two directions - two Line (fit) blocks, a Line (fit) and a fixed number - with a tolerance. |
| [Distance of points](/docs/vision/vision-points_dist/) | distance gauge | The distance between two points that other blocks found - a circle's centre, a pattern's position, an edge from Pick object - in pixels and, with a scale, in millimetres; with a tolerance. |
| [Part in place](/docs/vision/vision-part_ok/) | position and size verification, presence of a feature | The largest dark (or light) object in a window, judged by where it sits and how big it is - a cap on a bottle, a seal in its seat, a label on its place. |
| [Laser line profile](/docs/vision/vision-laser_line/) | laser triangulation, 2D profile sensor | A line laser shines a line across the part, the camera sees it from an angle, and the line's bend is the height profile - the height of a step, the depth of a groove, the fill of an opaque jar. Teach the baseline on the empty plane; the height comes in millimetres once mm_per_px is set. |

## Ready tools

Whole checks in one block: presence, colour, an edge, a code, a shape.

| Block | In the trade | What it does |
|:---|:---|:---|
| [Presence](/docs/vision/vision-presence/) | presence/absence check | Is something there? Measures the brightness of an area and says yes when it lies between the two limits. |
| [Colour check](/docs/vision/vision-colour/) | colour verification, HSV hue match | Is the area the right colour? Counts the pixels of the area near the taught hue and says yes when enough of them are. |
| [Edge position](/docs/vision/vision-edge/) | edge position, edge detection along a scan direction | Where is the edge? Walks across an area in one direction and reports the first place the brightness jumps. |
| [Read code](/docs/vision/vision-code/) | 1D/2D code reading, symbology, module size | Reads a QR code, a barcode, a DataMatrix, a PDF417 or an Aztec code and checks it against the expected text. |
| [Match shape](/docs/vision/vision-shape/) | shape matching, Hu moment invariants | Is one of the found objects the taught shape, whatever its size or turn (Hu moments)? Teach by dragging over a good part on the block's picture - its outline is the reference. |

## Learned models

A trained neural network of the project, for what no rule describes.

| Block | In the trade | What it does |
|:---|:---|:---|
| [Classify (model)](/docs/vision/vision-dnn_classify/) | deep learning inference, image classification, ONNX | Runs a trained neural network (an ONNX model imported into the project) on the picture and says which of its classes it sees - a good part or a bad one, which of five products, a full or an empty tray. The labels are the model's classes in its order. |
| [Detect (model)](/docs/vision/vision-dnn_detect/) | deep learning inference, object detection, ONNX | Runs a trained detection network (an ONNX model imported into the project - YOLO, SSD) on the picture and gives every object it finds as a list with its class, score and place. For what a rule cannot describe - mixed parts, a scratch of any shape, a person in the cell. |

