---
title: Vision inspection
source: docs/tutorial-vision.md
hero: img/vision-page.webp
---

# A camera that tells the PLC: is it there, what does it say, where does it lie

Draw a vision check from blocks - presence, code reading, pattern finding - and hand the results to the PLC program. Nothing is programmed, and the device computes exactly what the editor showed.

## Who it is for
- Builders of conveyor and assembly lines that need part checks
- Integrators who want vision inside the controller instead of a separate system
- Engineers who prefer drawing a check to writing image code

## What you get
- USB cameras added under the device; the live picture on the device's screen and in the browser
- Vision programs drawn as blocks, each block with its own window
- A test picture from the device's camera or from a file - every value on the page is real
- Presence: an area dragged on the picture and two brightness limits, framed green or red
- Read code: QR or barcode, optional expected text; found, match, number, text into a STRING
- Find pattern: teach by dragging over the part; found, x, y, score anywhere in the picture
- An ST code block for calculations the blocks do not have
- Results written into project variables, triggered on a rising edge with a DONE flag
- Online, the block windows show the device's own pictures and values

## How it works
1. Scan the device on its board page; right-click Cameras > Add camera, keep MJPG; draw a camera element on a screen.
2. Right-click Vision > Add vision program; take a test picture from the device or open one from a file.
3. Add Presence from the Toolbox (Ready tools), connect the camera's `out` to `src`, drag the area and set the limits.
4. Add Read code (qr or barcode) and Find pattern (drag to teach).
5. Right-click a block > Result present into a BOOL variable; same for match, x and y.
6. Choose *on a rising edge* with the trigger BOOL and a DONE BOOL; a rung waits on DONE.
7. Deploy - the program runs on the device below the PLC.

## Pictures
- ![The Vision page: when it runs, the test picture, the blocks](img/vision-page.webp) - a vision program drawn as blocks
- ![The Cameras node and the Vision node under the device](img/camera-tree.webp) - cameras and vision programs under the device
- ![The window of the presence block: its area framed green on the part](img/vision-block.webp) - green is yes, red is no
- ![Find pattern taught by a drag: the part framed with its score](img/vision-pattern.webp) - teach by a drag
- ![The ST code block's window: a few lines of ST and their result](img/vision-st.webp) - a calculation the blocks do not have

## Runs on
- A 64-bit Linux device: the reTerminal, a Raspberry Pi 4 / 5
- A USB camera plugged in; without a camera, the editor takes any picture from a file

## Facts to keep exact
- Three questions: is the part there, what does its code say, where exactly does it lie
- MJPG: the camera's own pictures pass through the device untouched
- A camera element's text is the camera's name
- The new vision program opens with its camera block already there
- Presence is in the Toolbox group *Ready tools*; connect camera `out` to block `src`; the page says when the program is complete
- Presence limits: the part, darker than the belt, is present between the two brightness limits; the answer follows a limit change at once
- Read code: *qr* or *barcode*; empty *expect* accepts any code; answers *found*, *match*, *number*, *text* (into a STRING variable)
- Find pattern: the cut-out becomes the taught picture, a picture of the project under Assets; answers *found*, *x*, *y*, *score*; a place must be at least *min score* alike
- ST code block: a few lines of ST over its inputs, compiled the moment you leave the box
- A run that could not look (no picture) writes nothing and says why on the device's console
- Troubleshooting: "Not complete" names the block and pin, an unfed input is drawn red; "taught picture has no detail" - drag over the part with its edges; dark picture - exposure settles over the first frames, Take a picture waits, a lamp helps more than any block; slow on a small device - put a Crop in front of Find pattern and Read code

## Call to action
Download the editor, plug a USB camera into a Raspberry Pi or reTerminal, and draw your first check.
