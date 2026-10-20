---
title: People counter with a model
source: docs/example-people-counter.md
hero: (none - the original page has no picture)
---

# Count people in a doorway, a hall or a cell - with a trained model on the panel

A camera, a small trained network running twice a second, and three variables your PLC program can use: how many people are in view, the best match's score, and whether anybody is there at all.

## Who it is for
- Cells and rooms where a door or a light should depend on whether somebody is inside
- Integrators adding object detection to a control project without a separate vision system
- Anyone who wants to count people, cars, bottles or chairs from a camera

## What you get
- A **Detect (model)** block running a trained network twice a second
- The model is a file of the project: imported with the block's *Import model* button and carried in the project file like a picture - nothing is downloaded on the device
- Only the chosen class counts: the *only* setting names it - `person` here; change it to `car`, `bottle` or `chair` and the same project counts those
- The detector's own picture on the glass and in the browser: every person framed with its score
- Three variables: `people` (the count), `best` (the best match's score in percent), `somebody` (yes/no for the PLC program)
- Your own trained model, or another Apache or MIT model from a model zoo, goes in the same way

## How it works
1. A USB camera on `/dev/video0` looks at the scene.
2. The Detect (model) block runs YOLOX-Nano twice a second and keeps the *person* class.
3. The block's settings say what the model expects: a 416 × 416 input, the picture as it comes (scale 1, nothing taken off, BGR), the *yolox* layout, and the 80 labels in the model's order.
4. The camera element names the block (`count.det`) instead of the camera, so the screen shows what the detector saw.
5. The results land in variables the PLC program uses - a door that waits while somebody is in the cell, a light that stays on while the room is in use.

## Pictures
- (the original page uses no pictures)

## Runs on
- Seeed reTerminal (CM4), or any 64-bit Linux device with a camera
- A USB camera on `/dev/video0`
- Glass and browser (WEBview)

## Facts to keep exact
- Model: YOLOX-Nano, 3.6 MB, trained on the 80 everyday classes of the COCO set (person, car, bottle, chair, dog ...)
- The model is published by Megvii under Apache 2.0, which allows it to ship inside a product; its notice text is in the editor's third-party file and travels with the project. The model is not trained on the device and is not ours
- Input 416 × 416; scale 1, nothing taken off (no mean), BGR; layout *yolox*; 80 labels in the model's order
- Runs twice a second on the whole frame
- On a reTerminal about 180 milliseconds per picture; a **Crop** in front of the block makes it faster when only part of the view matters
- Camera element source: `count.det`
- Variables: `people`, `best` (percent), `somebody`
- Note for the owner: the original points to a "Learned models" section of the vision documentation for what the block needs to know about a model, and a caution about models a product cannot carry

## Call to action
Download the ctrl32 editor and open the shipped project `examples\people_counter.prj32`.
