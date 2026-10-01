# People counter — a learned model on the reTerminal

The camera looks at a doorway, a hall, a cell. A **Detect (model)**
block runs a small trained network twice a second, keeps the *person*
class and hands three things to variables: how many people are in
view, the score of the best match and whether anybody is there at all.
The screen shows the detector's own picture — every person framed with
its score — and the numbers beside it.

**Project:** `examples\people_counter.prj32`
**Board:** Seeed reTerminal (CM4), or any 64-bit Linux device with a camera
**Needs:** a USB camera on `/dev/video0` — the model travels inside the
project, nothing is downloaded on the device

## What is in it

- **The model is a file of the project.** YOLOX-Nano, a 3.6 MB network
  trained on the 80 everyday classes of the COCO set (person, car,
  bottle, chair, dog ...), imported with the block's *Import model*
  button and carried in the project file like a picture. The block's
  settings say what it expects: an input of 416 × 416, the picture as it
  comes (scale 1, nothing taken off, BGR), the *yolox* layout, and the
  80 labels in the model's order.
- **Only people count.** The block's *only* setting names the one class
  that reaches the count; change it to `car`, `bottle` or `chair` and the
  same project counts those.
- **The detector's picture on the screen.** The camera element names the
  block (`count.det`) instead of the camera, so the glass and the browser
  show what the detector saw, with its frames and scores, not the raw
  picture.
- **Three variables.** `people` (the count), `best` (the score of the best
  match in percent) and `somebody` (a yes/no the PLC program can use —
  a door that waits while somebody is in the cell, a light that stays on
  while the room is in use).

The network is not trained on the device, and it is not ours: it is the
YOLOX-Nano model published by Megvii under the Apache 2.0 licence, which
allows it to ship inside a product. Its licence text is in the editor's
third-party file and travels with the project. A model you train
yourself, or another Apache or MIT model from a model zoo, goes in the
same way — see [Learned models](vision.md#learned-models) for what the
block needs to know about it, and the note there about models whose
licence a product cannot carry.

On a reTerminal the model takes a few hundred milliseconds per picture:
twice a second on the whole frame is the right pace for a doorway, and
a **Crop** in front of the block makes it faster when only one part of
the view matters.
