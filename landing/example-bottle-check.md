---
title: Bottle check, level cap label
source: docs/example-bottle-check.md
hero: img/example-bottle-check-glass.webp
---

# Three checks of a filling line on one camera - and one rung that says OK

Fill level in millimetres against a tolerance, the cap in place wherever the bottle stopped, the label read and in place: three vision programs, every answer a variable, one PLC rung.

## Who it is for
- Filling and packaging lines that need level, cap and label inspection
- Integrators who want vision results directly in the PLC program
- Teams who want to build and test an inspection at the desk before a camera is mounted

## What you get
- Fill level measured in millimetres, with a tolerance of 60 to 80 mm
- The cap checked in place wherever the bottle stopped - a Fixture finds the bottle and shifts the picture
- The label's Code 128 read and the label's position checked
- Every result a variable: `level_mm`, `level_ok`, `cap_ok`, `fx_found`, `fx_dx`, `label_text`, `label_read`, `label_ok`
- One PLC rung ANDs the three `ok` variables into `ok`, which lights a large lamp
- The editor runs every program on the drawn bottle it ships, so the lamps answer on the desk without a camera

## How it works
1. **level** - a **Ruler** across the bottle's body (320 px = 80 mm) gives millimetres per pixel; a **Fill level** block walks its window from the shoulder down, finds the surface and answers its height above the bottle's bottom.
2. **cap** - a **Fixture** taught on the bottle's top finds the bottle wherever it stopped and shifts the picture, so the **Part in place** window drawn on the cap stays on the cap: a dark part whose centre must sit within 15 px of where it was taught.
3. **label** - a **Crop** to the label feeds a **Read code** (Code 128); a **Part in place** checks the white label sits where it should.
4. Every program runs twice a second and writes its results into variables; the PLC rung combines them.
5. The screen: the camera picture with the three windows drawn over it (green: level, orange: cap, blue: label), the Fill level block's own picture with the surface it found, the three results, and a large lamp for the rung.

## Pictures
- ![The bottle screen on the device](img/example-bottle-check-glass.webp) - The screen as the device draws it: level 70.0 mm in tolerance, Fixture found the top, cap in place, label `BTL-0815`, OK lamp lit

## Runs on
- Seeed reTerminal (CM4), or any 64-bit Linux device with a camera
- A USB camera on `/dev/video0` looking at the bottle from the side - or nothing: the editor runs the programs on the drawn bottle

## Facts to keep exact
- Ruler: 320 px = 80 mm
- Level on the drawn bottle: 70 mm (70.0 mm on the screen); tolerance 60 to 80 mm
- Cap: centre within 15 px of where it was taught
- Label code: Code 128, reads `BTL-0815` on the drawn bottle
- Program times on a reTerminal: 9, 193 and 10 milliseconds; the Fixture's search is the one that costs, and a Crop in front of it would halve it
- Each program runs twice a second
- Window colours: green = level, orange = cap, blue = label
- Variables: `level_mm`, `level_ok`, `cap_ok`, `fx_found`, `fx_dx`, `label_text`, `label_read`, `label_ok`, rung output `ok`
- A step-by-step tutorial ("Measuring, step by step: a bottle") builds this project from its first block

## Call to action
Download the ctrl32 editor and open the shipped project `examples\bottle_check.prj32`.
