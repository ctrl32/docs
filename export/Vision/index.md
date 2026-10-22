---
title: "Vision"
slug: vision
section: "Vision"
order: 211
sidebar_position: 211
image: img/vision-page.webp
image_alt: "The Vision page of the editor with a program of blocks and the Toolbox beside it"
generator: tools/docs_export.py
---

# Vision

**A camera that checks, measures and reads - set up at your desk, without a line of code.** A Linux device with an ordinary USB camera becomes a vision station: is the part there, is it the right colour, where is its edge, how high is the fill, how wide is the part, what does its code say, is a person in the cell. The answers are variables of the PLC program, and the screens, Modbus, OPC UA and MQTT use them like any other.

A vision program is **drawn**: a chain of blocks - the camera, what is done with its picture, what is measured - connected on the Vision page. There are [89 blocks](/docs/vision/vision-blocks/), the toolset of an industrial vision system: regions of interest, filters and thresholds, morphology, blob analysis, pattern and feature matching, markers, calibration, calipers and gauges in millimetres, 1D and 2D codes, laser triangulation, trained neural networks. **Every block has its own window** with its settings and the picture it makes, and every block has [its own page](/docs/vision/vision-blocks/) in this documentation.

What makes it reliable is one rule: the editor runs the program on a test picture with **its own copy of the device's vision engine**. What the windows show at your desk is what the device computes on the line; change a setting and every picture and value follows at once. Online, the same windows show the device's own run.

!!! note "64-bit Linux devices"
    Vision runs on the Linux runtime of a **64-bit** device - the reTerminal, a Raspberry Pi 4 / 5, a CM4 / CM5, a PC-class device - with a camera of the project (see [Cameras](/docs/vision/cameras/)). The STM32MP1 device is too slow for it and has none; the editor offers the Vision node only for a device that can run it, and a project for another board that carries a vision program is refused at build.

## The Vision node

The vision programs have their own node in the tree, **Vision**, right under the device beside **Cameras**. It is there for every 64-bit Linux device.

![The Vision node under a Linux device, with two programs](img/camera-tree.webp){: .sb-center}

| Where | Action | What happens |
|:---|:---|:---|
| the **Vision** node | click | opens the Vision page |
| the **Vision** node | right-click → **Add vision program** | a new program named `vision1`, `vision2` ... with a **Camera** block set to the project's first camera, running every 200 ms; the page opens on it (greyed at 32 programs, the limit) |
| a program under the node | click | opens the page on that program |
| a program under the node | right-click → **Remove vision program** | removes it with its results |

A project holds up to **32** vision programs; a program up to **256** blocks and **128** results.

## The Vision page

![The Vision page: the program's blocks and their connections, the test picture's buttons above, the Toolbox on the right](img/vision-page.webp){: .sb-center}

The page is the program's graph, with as much room as the screen gives. Above it:

| Element | What it does |
|:---|:---|
| the program list | which program the page shows and edits - every program of the device is in it |
| **Settings...** | opens the [program's window](#the-programs-window): its name, when it runs, BUSY and DONE, the results |
| *The program is complete.* / *Not complete: ...* | the device's own check of the program, word for word: a complete program names nothing; an incomplete one says what is missing (an input nothing feeds, a block without a camera) |
| **Take a picture from the device** | fetches one picture of the camera the program's Camera block names, over the network, and makes it the test picture (the device's address comes from the online session or from the network upload settings; greyed without one, or while a picture is on its way) |
| **Open a picture...** | a picture file (jpg, jpeg, png, bmp) as the test picture |
| the picture's size, or *No test picture yet* | what the program runs on at the desk |
| *the whole program: N ms on this PC* | how long the editor's engine took on the test picture - a feel for the cost of the program (the device is slower than a PC: a Raspberry Pi 4 about four times) |
| online: *prog ... runs=... ms=...* | the device's own line about the program - how often it ran, its errors, its time |

### The canvas

Every block is a box: its title and id in the header, the **inputs as dots on the left** with their names, the **outputs as dots on the right** with their names and, once the program has run, their values. A required input nothing feeds is a **red** dot - the program is not complete until it is fed; an optional input nothing feeds is a dim dot and reads 0, FALSE or an empty picture.

| Gesture | What it does |
|:---|:---|
| click a block | selects it (the highlighted border); `Ctrl` + click adds it to the selection or takes it out |
| drag on the empty canvas | a selection rectangle: every block it touches is selected |
| `Ctrl+A` / `Esc` | every block / none |
| drag a block | moves it - a selected block moves the whole selection |
| double-click a block | opens the [block's window](#the-blocks-window) |
| drag from an output dot to an input dot | connects them - a picture into a picture input, a number into a number input, a list of objects into a list input, a text into a text input. A connection of two different types is refused (*These do not fit*), and so is one that would make a loop. Dropping on an input that is already fed replaces its connection |
| click a wire | selects it (drawn thicker, in the selection colour); a click on the empty canvas unselects it |
| right-click a wire | **Remove connection** |
| drag a wire off its input dot | picks the wire up - drop it on another input to move the connection, or let it go anywhere and the connection is gone |
| right-click an input dot | disconnects it |
| right-click a block | the block's menu: **Settings** (the window), **Result ... into** (one entry per number, yes/no or text output - pick the variable it goes into), **Remove block** |
| the Delete key | removes the selected wire; with no wire selected, the selected blocks, their connections and their results |
| `Ctrl+C` / `Ctrl+X` / `Ctrl+V` | copy, cut and paste the selected blocks with their settings; the connections between them come along, the copies get new ids |
| mouse wheel / `Ctrl` + wheel | scrolls / zooms around the mouse; a middle button drag or `Space` + drag moves the view, `Home` = zoom 100 % |
| `F1` | the page of the selected block |

The wires are drawn orthogonally; a wire that runs backwards (an output used by a block drawn to the left of it) is routed under the blocks. The blocks run in the order of their connections, whatever their place on the canvas.

### The Toolbox

While the Vision page is in front, the **Toolbox** panel on the right lists every block in eleven groups - Source, Geometry, Colour, Filters, Shapes, Edges, Finding objects, Logic, Measurements, Ready tools, Learned models - the groups of the [block index](/docs/vision/vision-blocks/). The groups fold and unfold like the ladder's; hold the mouse on a block to read what it does. **A click adds the block** to the program at the right of the canvas, below the lowest block, with the next unused id (`n1`, `n2` ...), and selects it. Connect it, set it, and the test picture runs through it at once.

## The program's window

**Settings...** opens it, in the middle of the screen.

![The program's window: its name, when it runs, BUSY and DONE, the results into variables](img/vision-settings.webp){: .sb-center}

| Field | What it does |
|:---|:---|
| **Name** | the program's name - 1 to 32 letters, digits, `_` or `-`, unique among the device's programs (Enter applies) |
| **Runs** | **on a rising edge** - the program looks once each time a BOOL variable goes from 0 to 1, the PLC way: the program sets *part_in* when the part is in position; or **periodically** - every so many milliseconds, for a check that watches all the time |
| **Trigger (BOOL)** | the variable whose rising edge starts a run (edge mode) |
| **Period [ms]** | the period, 0 to 3 600 000 ms (periodic mode); 200 ms is the default |
| **BUSY (BOOL)** | an optional variable that is on while the program runs |
| **DONE (BOOL)** | an optional variable that comes on when the results are written; BUSY and DONE go off at the next trigger - a rung waits on DONE |
| *The program is complete.* / *Not complete: ...* | the same check as on the page |
| **Results into variables** | one row per result: `block.output → variable`, with an **X** that removes it. Results are added from a block's right-click menu on the canvas (*Result ... into*) |
| **Close** | closes the window |

Results are written only after a run that **succeeded**: a program that could not look - no picture, the camera unplugged - writes nothing and says why on the device's console and in its diagnostic buffer. A single block that cannot run - an input nothing feeds (a *Mask* with no mask picture, a *Difference* with one wire), a picture of the wrong kind - leaves **its own** outputs empty and the blocks fed from it have none either; the blocks that do not depend on it still run, so the rest of the program keeps its pictures on the canvas while you fix it. Its window says the reason in red where the picture would be, and the Toolbox repeats it under the block list. A number or a yes/no result goes into a number or a BOOL variable; a **text** result (what a code says, a model's label) into a **STRING** variable; a picture or a list of objects never goes into a variable - it goes into the next block, or into a [camera element](/docs/vision/cameras/#the-picture-after-the-filters) on a screen.

## The block's window

**Double-click a block** (or its menu → **Settings**) and its window opens in the middle of the screen - the same size and the same shape for every block; opening another block closes it.

![The window of a Presence block: its settings on the left, the outputs under them, the picture with the area framed on the right](img/vision-block.webp){: .sb-center}

**On the left:**

| Element | What it does |
|:---|:---|
| the block's description | what the block does, in a sentence (greyed, at the top) |
| the **settings table** - *name* | every setting of the block, with its unit after it; hold the mouse on the name to read what the setting means |
| the settings table - *value* | the value: a number field (typed, kept inside the setting's range - a value outside it is ignored), a tick for a yes/no, a list for a choice, a text; a hue setting shows a swatch of its colour; a `pattern` setting lists the taught pictures of the project and says *(not taught yet)* before the first teach; a `model` setting lists the ONNX files of the project; the Camera block's `camera` lists the project's cameras |
| the settings table - *variable* | **fixed**, or a **variable** the device reads into the setting **before every run**, kept inside the range: a recipe or the PLC program then changes the check - another product, another area, another limit - without a new vision program. A number or yes/no setting takes a number or BOOL variable, a text setting (the expected text of Read code, the labels of a model) a STRING variable. Not every setting is bindable: a taught picture, a model, a camera and a choice are fixed |
| **Import model...** | a button of the two model blocks: an `.onnx` file (at most 64 MB) becomes a file of the project and the block's `model` names it - the model's own terms are yours to check |
| **Calibrate from this picture** | a button of Lens correction: finds the chessboard in the test picture and fills the lens numbers in |
| **Teach the plane from this picture** | a button of Plane from a board: the chessboard on the working plane becomes the mapping to millimetres |
| **Teach the baseline from this picture** | a button of Laser line profile: the laser line on the empty plane becomes the zero of every height |
| the **code box** | the ST code block shows its code in a box instead of a value field; it compiles when the box loses focus and the line under it says *Compiles.* or names the error |
| **Outputs** | every output of the block with its value from the last run - a number, 1/0 for a yes/no, a text in quotes, the size of a picture, the count of a list; hold the mouse on the name to read what the output means |
| **Close** | closes the window |

**On the right, large: what the block shows** - its picture, or for a measuring block the picture it measured with its area, its line or its ring drawn on it: **green** when the answer is *yes*, **red** when it is *no*; the objects a finder found are framed and numbered; a match carries its score. The line above the picture says where it comes from: *the test picture, on the editor's own copy of the device's engine*, or *online: the device's own run* (the device's picture of this block, fetched twice a second), or *no picture yet* until a test picture is taken or opened.

**Teaching on the picture** - the gestures the picture takes, named under the caption of the window that offers them:

| Gesture | Blocks | What it sets |
|:---|:---|:---|
| **drag a rectangle** | every block with an area - Crop, Presence, Colour check, Edge position, the gauges, the statistics | the area `x`, `y`, `w`, `h` (at least 2 x 2 pixels) |
| **drag over the part** | Find pattern, Find by features, Match shape, Fixture, Compare with taught | the taught picture: the cut-out becomes a picture of the project and the block's `pattern` names it (at least 8 x 8 pixels; Compare with taught takes the area too, Fixture the reference point). Teach on the test picture, not online |
| **drag a line** | Ruler, Caliper | the line `x1`, `y1`, `x2`, `y2` |
| **click four corners** | Straighten | the corners `x1`..`y4` - top-left, top-right, bottom-right, bottom-left; the caption counts the clicks |
| **right-click a point** | Colour check, Colour range | the colour: the hue of that point (a gray or dark point has no colour and is refused) |

The numbers in the table follow every gesture and can still be typed.

## Test pictures and the desk run

The pictures need a **test picture**: **Take a picture from the device** (the camera the program reads, over the network) or **Open a picture...** (a file). The editor then runs the program on it with its own copy of the device's vision engine - every block's window shows its picture and its values, the page shows how long the whole program took. The picture stays with the editor session, not with the project.

Build a check from pictures of real parts: take ten good ones and ten bad ones with **Take a picture from the device**, keep them in a folder, and open them one after the other while setting the limits. A check that passes every good picture and fails every bad one at the desk does the same on the line.

**Online**, the windows show the device's own run instead: its picture of every block, its values, and the program's line on the page (how many runs, errors, milliseconds). Teaching is a desk gesture - teach on a test picture, then download.

**One camera, several programs.** Every program begins with its own Camera block, and any number of them may name the same camera: one program per question - the fill level, the cap, the label - each with its own trigger or period, its own results and its own time on the page. A program that fails does not stop the others, and a slow one (a pattern search, a model) does not hold up a fast one.

## Measuring

Every measuring block answers in pixels, and in millimetres as soon as a **scale** (millimetres per pixel) is wired into its `scale` input:

- the [Ruler](/docs/vision/vision-ruler/) - drag along a known length on its picture and type what it is - gives the scale of a flat plane the camera faces squarely;
- the [Plane from a board](/docs/vision/vision-world/) - one chessboard lying on the working plane, taught with a button - gives a top view of the plane in which one millimetre is a known number of pixels, whatever angle the camera looks from, and its scale with it;
- the [Lens correction](/docs/vision/vision-undistort/) takes the barrel of a wide lens out first, so that the scale holds across the whole picture;
- the [Scale](/docs/vision/vision-scale/) block converts any other number.

Every gauge takes a **tolerance** - `min` and `max`, 0 = no limit - and answers *ok*: a value outside the pair is a failed check, never a fault.

**Millimetres with a Ruler**, the usual order:

1. Connect a [Ruler](/docs/vision/vision-ruler/) to the picture the gauges measure on (the camera's, or a Fixture's `out`).
2. In its window drag along a length you know - the part's body, a mark, a rule laid on the belt - and type its real length in `length`. The block answers `mm_per_px`: a body 320 px wide that is 80 mm reads 0.25.
3. Wire `mm_per_px` into the `scale` input of every gauge. Their `_mm` outputs and their `min` / `max` are now in millimetres; a gauge with nothing on `scale` answers in pixels.

A tolerance is easiest typed from a good part: read the gauge's value on a good test picture, then set `min` and `max` around it. Bound to a variable (the variable column of the block's window), a recipe sets the tolerance per product without a new vision program.

**A level is a jump of brightness.** The [Fill level](/docs/vision/vision-level/) block averages every row across its window and stops at the first jump at least `contrast` big (40 suits most liquids) - drag the window over the straight part of the vessel only, and set `polarity` to the one change the surface makes (*light to dark* for a dark liquid under a light headspace), so that a label's edge further down cannot be taken for the surface. `position` counts from the edge the search starts at, `level` from the opposite edge - the fill height a specification states.

## Coordinates

A part on a belt never lies exactly where it lay when the check was drawn. The [Fixture](/docs/vision/vision-fixture/) block, taught once by a drag over the part, finds the part on every later picture and shifts (and turns) the whole picture back so that the part sits where it was taught - every block after it keeps its areas.

The rules of a fixtured program:

- **Connect the measuring blocks to the Fixture's `out`, not to the camera.** A block fed straight from the camera keeps its window on the camera, and the part walks out of it.
- **Teach the Fixture on something with edges** that is always there and always looks the same - the top of a bottle with its neck and shoulder, a corner of a part. A drag over one flat shade has no detail to find, and the block says the taught picture has no detail.
- **A part that is not found** leaves the picture unshifted and `found` off; the blocks after it still run. Hand `found` to a variable and let the PLC program tell "no part" from "a bad part".
- **A part that may lie turned** needs `max_angle` above 0. Every degree of the search costs time; leave it at 0 when the part never turns.
- **`dx`, `dy` and `angle`** say how far the part had moved and turned - into variables, they show a feeder drifting long before a check fails.

After a Fixture, a [Part in place](/docs/vision/vision-part_ok/) window drawn on a feature (a cap, a seal, a label) judges the feature itself: `found` off = the feature is missing; `found` on with `ok` off = it is there but off its place or the wrong size, and its `dx` / `dy` say which way it slid.

The [Plane from a board](/docs/vision/vision-world/) block fixes the working plane in the same way: after it, a point of the picture is a point of the plane in millimetres.

## Finding objects

Some blocks give a **list of objects** rather than a number - [Find objects](/docs/vision/vision-contours/) (the separate white areas of a black-and-white picture), [Find circles](/docs/vision/vision-circles/), [Find lines](/docs/vision/vision-lines/), [Find corners](/docs/vision/vision-corners/), [Find markers](/docs/vision/vision-aruco/), [Find pattern](/docs/vision/vision-pattern/), [Detect (model)](/docs/vision/vision-dnn_detect/). Every object has its centre, its frame, a radius, an angle and an area, and the list is sorted - the largest first, or left to right, or top to bottom - so *object 0* always means the same one. [Pick object](/docs/vision/vision-pick/) gives one object's numbers, [Check objects](/docs/vision/vision-objcheck/) judges the whole list, [Filter objects](/docs/vision/vision-filter_objects/) keeps the ones that look right, [Crop to object](/docs/vision/vision-crop_object/) looks only where the part really is.

## Reading codes

[Read code](/docs/vision/vision-code/) reads a **QR code**, a **barcode** (every
one-dimensional code: EAN, UPC, Code 128, Code 39, ITF, Codabar, GS1
DataBar), a **DataMatrix**, *pdf417* or *aztec*; *any* reads every kind at
once and its *format* output names the kind it read. One block per kind
is the faster road when the kinds are known.

- **The reading area.** Put a [Crop](/docs/vision/vision-crop/) in front of the
  reader: a code outside the area does not count, and a quarter of the
  picture costs a quarter of the search.
- **The picture the reader gets.** [Gamma](/docs/vision/vision-gamma/),
  [Stretch contrast](/docs/vision/vision-normalize/) and [Sharpen](/docs/vision/vision-sharpen/)
  before the reader help a glossy label under a lamp or a soft picture.
  Bind their settings to variables and put sliders for them on a screen:
  the operator sets them while watching that picture, and the values are
  kept over a restart. Neutral is gamma 100, contrast 0, sharpen 1.
- **Two programs.** A reader takes a few hundred milliseconds. A preview
  of the prepared picture at that pace stutters, so the preview gets its
  own program (every 100 ms) and the readers theirs (every 400-500 ms).
  A screen camera element whose text names a block (`prep.shp`) shows that
  block's picture live.
- **The answers are variables**: found, the text, the kind, the value as
  a number when the code is one. The text of a code lands in a **STRING**
  variable, a kind only a Linux device has. A barcode's value is its
  text: thirteen digits of an EAN-13 do not fit a number exactly.
- **expect** empty reads any code; a text in *expect* makes *match* say
  whether the code carries it - a lot number, a product.
- **Size and light.** A barcode reads when it is about a fifth of the
  picture wide or more. Bring a small label close, keep it flat and out
  of the glare.

![Reading codes: the camera's picture with a QR code and an EAN-13 label, the texts read off it](img/example-reterminal-ecat-codes.webp){: .sb-center}

## A piece of ST

When the blocks do not have the calculation you need, the [ST code](/docs/vision/vision-st/) block takes a few lines of ST - the same language as the PLC program - over its inputs `a`..`d` and `p`, `q`, and writes `y1`..`y4` and `r1`, `r2`. It compiles in the window and runs on the device inside the vision program.

## Learned models

For the things no rule describes - a scratch of any shape, a part that is "wrong" in a hundred ways, mixed products, a person in the cell - [Classify (model)](/docs/vision/vision-dnn_classify/) and [Detect (model)](/docs/vision/vision-dnn_detect/) run a **trained neural network**, an ONNX model imported into the project with the window's **Import model...** button. The model is trained on a PC from pictures you collected, or taken from a model zoo; it is never trained on the device.

**Adding a model:**

1. Add the block, open its window and press **Import model...**: the `.onnx` file (at most 64 MB) becomes a file of the project, carried in the project file like a picture, and `model` names it. The deploy takes it to the device with the program - nothing is downloaded on the device.
2. Describe the model's input from its own documentation: `width` and `height` (416 x 416 for a small YOLOX, 640 x 640 for most YOLO exports), `scale` and `mean` (a model trained on 0..1 wants `scale` 0.003922 = 1/255; a model that wants the raw picture 0..255 wants `scale` 1, `mean` 0), `swap_rb` (on for RGB, off for a model that takes BGR as it comes).
3. For a detector set `layout`: *auto* reads SSD and the YOLO families off the output's shape, a YOLOX export keeps its boxes in grid units and must be named *yolox*.
4. Type `labels` - the class names **in the model's own order**, separated by commas - so that `label` and `only` speak names instead of numbers. `only` keeps one class (`person`, `car`, `bottle`): the count and the best match then speak of that class alone.
5. Open a test picture: the window frames every detection with its score. No frame at all on a picture where something is plainly there usually means the input is described wrongly - try the other `scale` / `swap_rb` before anything else.

**What it costs.** A model is the heaviest block there is. A small detector (YOLOX-Nano, 3.6 MB, the 80 everyday classes of the COCO set) takes about **180 ms per picture** on a reTerminal (a Raspberry Pi CM4) on the whole frame: twice a second is the right pace, and a [Crop](/docs/vision/vision-crop/) in front of the block makes it faster when only part of the view matters. Run a model on a trigger or every half second to a second, never ten times a second.

**Its terms.** A model you download comes with its own terms, and they are part of the decision: some published detection models are offered only under terms that do not allow them inside a closed product. Read them before you build a product on one; a model released under permissive terms (Apache 2.0, MIT), or one you trained yourself, goes in the same way.

## The control comes first

A vision program runs on the device **below the PLC**, on its own thread, away from the core the cycle and the EtherCAT line use. When the device is busy, a picture waits - the cycle never does. A camera that stops giving pictures is a failed run, never a check on an old picture. The device's console and its diagnostic buffer say what a failed run lacked.

## Speed

The page says how long the whole program took on the PC; the online line says what the device takes. Most blocks cost a few milliseconds - a program of a Ruler and a Fill level, or of a Crop, a Read code and a Part in place, runs in about 10 ms on a reTerminal. Three kinds of block cost the rest:

- **searches for a taught picture** - [Fixture](/docs/vision/vision-fixture/), [Find pattern](/docs/vision/vision-pattern/), [Find by features](/docs/vision/vision-features/): a Fixture searching the whole frame of a reTerminal takes about 200 ms, and more with every degree of `max_angle`;
- **[Read code](/docs/vision/vision-code/)**, which searches the whole picture it receives;
- **[learned models](#learned-models)**.

The cure is the same for all three: a [Crop](/docs/vision/vision-crop/) in front of them, to the area where the part (or the code) can be - the smaller the area, the shorter the search (half the area, about half the time). Then match the program's period to what it costs: a program that takes 200 ms cannot run every 100 ms.

## When a reading is wrong

| What you see | What to do |
|:---|:---|
| the page says *Not complete* | it names the block and the input; the input is drawn red on the canvas - connect it |
| a block's window says the taught picture has no detail | the drag covered one flat shade - drag again over the part **with its edges** |
| the device's picture is darker or brighter than the one at the desk | the camera's automatics: fix the exposure, the gain and the white balance on the camera's page ([Exposure and colour](/docs/vision/cameras/#adding-a-camera)) - a check wants the same picture every time. A lamp helps a camera more than any block does |
| a check passes and fails on the same part | the same: fixed exposure first, then limits set from ten good and ten bad pictures (see [Test pictures](#test-pictures-and-the-desk-run)) |
| a window drawn on a feature misses it when the part stops elsewhere | put a [Fixture](#coordinates) in front and connect the block to the Fixture's `out` |
| the Fixture's `found` is off on good parts | lower `min_score` a little, or teach again on a part with more edges; a part that lies turned needs `max_angle` |
| a Fill level reads a label's edge instead of the surface | set `polarity` to the change the surface makes and shrink the window to the vessel's straight part |
| a value in pixels where millimetres were wanted | nothing is wired into the block's `scale` input - see [Measuring](#measuring) |
| a code is not read | the code's smallest element must be at least two pixels wide, better three, and in focus - move the camera closer or change the lens; a Crop to the label helps |
| a model frames nothing | the model's input is described wrongly - `scale`, `mean`, `swap_rb`, `layout` (see [Learned models](#learned-models)) |
| the program is slow, or its online time is longer than its period | see [Speed](#speed) |
| the results never change in the PLC program | a run that failed writes nothing: the online line counts the errors, the device's console and diagnostic buffer say why (no picture, the camera unplugged) |

## Where to go next

- [Vision blocks](/docs/vision/vision-blocks/) - every block, its own page.
- [Cameras](/docs/vision/cameras/) - the camera's page, every field.
