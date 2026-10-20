---
title: Bottle inspection by camera
source: docs/tutorial-measuring.md
hero: img/measure-level.webp
---

# Fill level, cap and label checked on every bottle - with one camera

Build three vision checks for a filling line, measure in millimetres, and turn the answers into variables your PLC program and screen use directly. Every step works on the desk, before any device exists.

## Who it is for
- Builders of filling and packaging lines who need an in-line quality check
- Integrators who want camera inspection and PLC logic in one project
- Engineers who want to try vision on the desk with a drawn test picture before buying hardware

## What you get
- Three vision programs on one camera: `level`, `cap` and `label`, each answer a variable
- Measurements in millimetres: a **Ruler** turns pixels into mm, every measuring block takes it on its *scale* input
- **Fill level** block: finds the liquid surface, answers *position*, *level* and *level_mm*, with a min/max tolerance and an *ok* output
- **Fixture** block: finds the bottle top wherever the bottle stopped and shifts (and, within *max angle*, turns back) the whole picture so later checks hit the same place
- **Part in place** block: finds the cap (or the label) and judges where it sits - *found*, *ok*, and *dx* / *dy* saying which way it slid
- **Read code** block: barcode, QR code or DataMatrix (*any* reads whatever is there)
- One ladder rung `level_ok AND cap_ok AND label_ok` into `ok` - a lamp, a conveyor stop or a reject flap reads it
- A screen that draws the three windows over the camera picture, the Fill level block's own picture and the results with lamps

## How it works
1. Add a camera and a vision program; open a picture of a bottle (or the editor's drawn `bottle.png`).
2. Calibrate the plane with a Ruler: drag across the bottle body (320 px), type 80 mm - the Ruler answers 0.25 mm per px.
3. Fill level: drag its area over the bottle body, set polarity *light to dark* and contrast; set the tolerance and hand *level_mm*, *found* and *ok* to variables in the program's Results.
4. Cap: a Fixture taught on the bottle top, then a Part in place on the Fixture's output, polarity dark, over the cap.
5. Label: a Crop to the label feeding Read code, plus a second Part in place (polarity light) checking the white label's place.
6. One rung combines the three verdicts; the screen shows it, on the desk and on the device.

## Pictures
- ![The level program on the Vision page](img/measure-page.webp) - the `level` program on the Vision page
- ![The Fill level window](img/measure-level.webp) - the Fill level block finding the surface
- ![The Fixture window](img/measure-fixture.webp) - the Fixture taught on the bottle's top
- ![The Part in place window on the cap](img/measure-cap.webp) - Part in place judging the cap
- ![The bottle screen in the editor](img/measure-screen.webp) - the operator screen with the three windows and the lamps

## Runs on
- A 64-bit Linux device with a camera (the reTerminal of the examples)
- Or no device at all: the editor on the desk with the drawn test bottle

## Facts to keep exact
- Test picture `bottle.png`: a bottle 320 px wide on a belt, liquid up to row 400
- Ruler: 320 px = 80 mm, *mm per px* = 0.25
- Fill level walks the area from the top (*direction* top down), averages every row across the area's width, stops at the first brightness jump darker than the one before; *polarity* *light to dark* so a label edge further down is not taken for the surface; *contrast* 40 is right for most liquids
- Drawn bottle measures *level_mm* 70 mm; tolerance *min* 60, *max* 80 lights *ok*
- *min* 75 turns *ok* off for the 70 mm bottle; the screen lamp follows within half a second
- Part in place on the cap: *polarity* dark (a red cap on a light bottle), *threshold* between the two, largest dark blob; *ex* / *ey* = expected centre, *pos tol* = allowed offset; missing cap = *found* dark; askew cap = *found* lit, *ok* dark, *dx* / *dy* say which way
- Part in place for the cap connects to the Fixture's *out*, not to the camera
- Drawn label carries a Code 128, `BTL-0815`; Read code *kind* barcode, or QR / DataMatrix / *any*
- Next steps named on the page: **Plane from a board** (one chessboard teaches a top view in millimetres when the camera looks at an angle); binding a tolerance to a variable (the *@* beside the setting) so a recipe sets it per product
- New project on the reTerminal: tick *Visualization* and *Vision*

## Call to action
Download the editor and open the Bottle check example (or build it from the first block with the drawn test bottle on your desk).
