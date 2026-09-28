# Vision

A Linux device can **look and decide**: is the part there, is it the
right colour, where is its edge, what does its code say. The answers
are ordinary variables - the PLC program, the screens, Modbus, OPC UA
and MQTT use them like any other.

A vision program is drawn, not written: a chain of blocks - the camera,
what is done with its picture, what is measured - and every block has
its own window with its settings and the picture it makes.

!!! note "Linux devices only"
    Vision runs on the Linux runtime, with a camera of the project (see
    [Cameras](cameras.md)). A project for another board that carries a
    vision program is refused at build.

## Adding a vision program

The vision programs have their own node in the tree, **Vision**, right
under the device beside **Cameras**. Right-click it → **Add vision
program**. A new program starts with its camera block, set to the
project's first camera.

![The Vision node under a Linux device, with two programs](img/camera-tree.webp){: .sb-center}

Click the program to open its page.

![The Vision page: when the program runs, the test picture, the blocks and how they are connected](img/vision-page.webp){: .sb-center}

- **Click a block** in the list on the left to add it.
- **Drag from an output** (the dots on the right of a block) **to an
  input** (the dots on the left) to connect them. A picture goes into a
  picture input, a number into a number input.
- **Right-click an input** to disconnect it. An input nothing feeds is
  drawn red, and the page says what is missing:
  *Not complete: ...*. A complete program says *The program is
  complete.*
- **Drag a block** to move it, **right-click** it to remove it or to
  send one of its results into a variable.

## Every block has its own window

**Double-click a block** to open its window: every setting with its
unit and what it means, the values the block produced, and **what the
block shows** - its picture, or for a measuring block the picture it
measured with its area framed: green when the answer is *yes*, red when
it is *no*. Several windows can be open at once.

![The window of a presence block: its area, its limits, its answer, and the part it found framed in green](img/vision-block.webp){: .sb-center}

**Teach by hand:** a block that looks at an area takes it from a
**drag on its picture**, and a colour check (or a colour range) takes
its colour from a **right click on a point** of the picture - the
label, the cap, the mark it must recognise. The numbers in the window
follow, and can still be typed.

The pictures need a **test picture**: **Take a picture from the device**
(the camera the program reads, over the network), or **Open a
picture...** from a file. The editor then runs the program on it with
its own copy of the device's vision engine - what the windows show is
what the device will compute. Change a setting and the pictures and
values follow at once.

**Online**, the windows show the device's own run instead: its picture
of every block, its values, and how many times the program ran.

Every block and all its settings are listed in
[Vision blocks](vision-blocks.md).

## The ready tools

Four blocks do a whole check on their own:

| Tool | Answers | Typical use |
|:---|:---|:---|
| **Presence** | *present* (yes/no) and the *level* of brightness in an area | is the part in position, is the lens covered |
| **Colour check** | *match* (yes/no) and the *share* of the area in the chosen colour | the right cap, the right label |
| **Edge position** | *found* (yes/no) and the *position* of the first edge in an area, in pixels | where the material ends, a mark on a web |
| **Read code** | *found*, *match* (the expected text) and the code as a *number* when it is one | a QR code or a barcode on the part |

Everything else - cropping, colour ranges, thresholds, filters,
counting objects, turning pixels into millimetres - is there to build
a check of your own.

## Settings from variables

Any number or yes/no setting of a block can come from a **variable**
instead of being fixed: pick the variable in the small list beside the
setting (*fixed* is the other choice). The device reads it **before
every run**, kept inside the setting's range. A recipe or the PLC
program then changes the check - another product, another area,
another limit - without a new vision program.

## Finding objects

Some blocks give a **list of objects** rather than a number: **Find
objects** (the separate white areas of a black-and-white picture) and
**Find circles**. Every object has its centre, its frame, a radius, an
angle and an area, and the list is sorted - the largest first, or left
to right, or top to bottom - so *object 0* always means the same one.

- **Pick object** gives the numbers of one object of the list - its
  position and size go into variables like any result.
- **Crop to object** keeps the frame around one object: the blocks
  after it look only where the part really is, wherever it lies on
  the belt.

The window of a block that finds objects shows each one framed and
numbered on the picture it was found in.

## When it runs

- **On a rising edge** of a BOOL variable - the PLC way: the program
  sets *part_in* when the part is in position, and the vision program
  looks once.
- **Periodically**, every so many milliseconds, for a check that
  watches all the time.

Two optional BOOL variables make a handshake a rung can wait on:
**BUSY** is on while the program runs, **DONE** comes on when its
results are written, and both go off at the next trigger.

## Results into variables

Right-click a block and pick which of its outputs goes into which
variable (a number or a BOOL). The results are written only after a
run that succeeded - a program that could not look (no picture, the
camera unplugged) writes nothing and says why on the device's console
and in its diagnostic buffer.

## The control comes first

A vision program runs on the device **below the PLC**, on its own
thread, away from the core the cycle and the EtherCAT line use. When
the device is busy, a picture waits - the cycle never does. A camera
that stops giving pictures is a failed run, never a check on an old
picture.
