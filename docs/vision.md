---
image: img/vision-page.webp
image_alt: The Vision page of the editor with a program of blocks and the Toolbox beside it
---

# Vision

**A camera that checks, measures and reads - set up at your desk, without a line of code.** A Linux device with an ordinary USB camera becomes a vision station: is the part there, is it the right colour, where is its edge, how high is the fill, how wide is the part, what does its code say, is a person in the cell. The answers are variables of the PLC program, and the screens, Modbus, OPC UA and MQTT use them like any other.

A vision program is **drawn**: a chain of blocks - the camera, what is done with its picture, what is measured - connected on the Vision page. There are [89 blocks](vision-blocks.md), the toolset of an industrial vision system: regions of interest, filters and thresholds, morphology, blob analysis, pattern and feature matching, markers, calibration, calipers and gauges in millimetres, 1D and 2D codes, laser triangulation, trained neural networks. **Every block has its own window** with its settings and the picture it makes, and every block has [its own page](vision-blocks.md) in this documentation.

What makes it reliable is one rule: the editor runs the program on a test picture with **its own copy of the device's vision engine**. What the windows show at your desk is what the device computes on the line; change a setting and every picture and value follows at once. Online, the same windows show the device's own run.

!!! note "64-bit Linux devices"
    Vision runs on the Linux runtime of a **64-bit** device - the reTerminal, a Raspberry Pi 4 / 5, a CM4 / CM5, a PC-class device - with a camera of the project (see [Cameras](cameras.md)). The STM32MP1 device is too slow for it and has none; the editor offers the Vision node only for a device that can run it, and a project for another board that carries a vision program is refused at build.

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
| click a block | selects it (the highlighted border) |
| drag a block | moves it |
| double-click a block | opens the [block's window](#the-blocks-window) |
| drag from an output dot to an input dot | connects them - a picture into a picture input, a number into a number input, a list of objects into a list input, a text into a text input. A connection of two different types is refused (*These do not fit*), and so is one that would make a loop. Dropping on an input that is already fed replaces its connection |
| right-click an input dot | disconnects it |
| right-click a block | the block's menu: **Settings** (the window), **Result ... into** (one entry per number, yes/no or text output - pick the variable it goes into), **Remove block** |
| the Delete key | removes the selected block, its connections and its results |

The wires are drawn orthogonally; a wire that runs backwards (an output used by a block drawn to the left of it) is routed under the blocks. The blocks run in the order of their connections, whatever their place on the canvas.

### The Toolbox

While the Vision page is in front, the **Toolbox** panel on the right lists every block in eleven groups - Source, Geometry, Colour, Filters, Shapes, Edges, Finding objects, Logic, Measurements, Ready tools, Learned models - the groups of the [block index](vision-blocks.md). The groups fold and unfold like the ladder's; hold the mouse on a block to read what it does. **A click adds the block** to the program at the right of the canvas, below the lowest block, with the next free id (`n1`, `n2` ...), and selects it. Connect it, set it, and the test picture runs through it at once.

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

Results are written only after a run that **succeeded**: a program that could not look - no picture, the camera unplugged - writes nothing and says why on the device's console and in its diagnostic buffer. A number or a yes/no result goes into a number or a BOOL variable; a **text** result (what a code says, a model's label) into a **STRING** variable; a picture or a list of objects never goes into a variable - it goes into the next block, or into a [camera element](cameras.md#the-picture-after-the-filters) on a screen.

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

## Measuring

Every measuring block answers in pixels, and in millimetres as soon as a **scale** (millimetres per pixel) is wired into its `scale` input:

- the [Ruler](vision-ruler.md) - drag along a known length on its picture and type what it is - gives the scale of a flat plane the camera faces squarely;
- the [Plane from a board](vision-world.md) - one chessboard lying on the working plane, taught with a button - gives a top view of the plane in which one millimetre is a known number of pixels, whatever angle the camera looks from, and its scale with it;
- the [Lens correction](vision-undistort.md) takes the barrel of a wide lens out first, so that the scale holds across the whole picture;
- the [Scale](vision-scale.md) block converts any other number.

Every gauge takes a **tolerance** - `min` and `max`, 0 = no limit - and answers *ok*: a value outside the pair is a failed check, never a fault.

## Coordinates

A part on a belt never lies exactly where it lay when the check was drawn. The [Fixture](vision-fixture.md) block, taught once by a drag over the part, finds the part on every later picture and shifts (and turns) the whole picture back so that the part sits where it was taught - every block after it keeps its areas. The [Plane from a board](vision-world.md) block does the same for the working plane: after it, a point of the picture is a point of the plane in millimetres.

## Finding objects

Some blocks give a **list of objects** rather than a number - [Find objects](vision-contours.md) (the separate white areas of a black-and-white picture), [Find circles](vision-circles.md), [Find lines](vision-lines.md), [Find corners](vision-corners.md), [Find markers](vision-aruco.md), [Find pattern](vision-pattern.md), [Detect (model)](vision-dnn_detect.md). Every object has its centre, its frame, a radius, an angle and an area, and the list is sorted - the largest first, or left to right, or top to bottom - so *object 0* always means the same one. [Pick object](vision-pick.md) gives one object's numbers, [Check objects](vision-objcheck.md) judges the whole list, [Filter objects](vision-filter_objects.md) keeps the ones that look right, [Crop to object](vision-crop_object.md) looks only where the part really is.

## A piece of ST

When the blocks do not have the calculation you need, the [ST code](vision-st.md) block takes a few lines of ST - the same language as the PLC program - over its inputs `a`..`d` and `p`, `q`, and writes `y1`..`y4` and `r1`, `r2`. It compiles in the window and runs on the device inside the vision program.

## Learned models

For the things no rule describes - a scratch of any shape, a part that is "wrong" in a hundred ways, mixed products, a person in the cell - [Classify (model)](vision-dnn_classify.md) and [Detect (model)](vision-dnn_detect.md) run a **trained neural network**, an ONNX model imported into the project with the window's **Import model...** button. The model is trained on a PC from pictures you collected, or taken from a model zoo; one ships ready to use in the [People counter](example-people-counter.md) example. The model file carries its own licence - check it before you build a product on a downloaded one.

## The control comes first

A vision program runs on the device **below the PLC**, on its own thread, away from the core the cycle and the EtherCAT line use. When the device is busy, a picture waits - the cycle never does. A camera that stops giving pictures is a failed run, never a check on an old picture. The device's console and its diagnostic buffer say what a failed run lacked.

## Where to go next

- [Vision blocks](vision-blocks.md) - every block, its own page.
- [Cameras](cameras.md) - the camera's page, every field.
- [Vision, step by step](tutorial-vision.md) - the first program: presence and a code.
- [Measuring, step by step: a bottle](tutorial-measuring.md) - a fill level and a cap, in millimetres, with a Fixture.
- [Bottle check](example-bottle-check.md) and [People counter](example-people-counter.md) - two shipped projects.
