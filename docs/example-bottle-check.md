---
image: img/measure-screen.webp
image_alt: "The bottle screen: the camera with the three windows, the level, the cap, the label and the OK lamp"
---

# Bottle check — level, cap, label

The three checks of a filling line on one camera: the **fill level** in
millimetres against a tolerance, the **cap** in place wherever the bottle
stopped, the **label** read and in place — three vision programs, every
answer a variable, and one rung of the PLC program that says OK.

**Project:** `examples\bottle_check.prj32`
**Board:** Seeed reTerminal (CM4), or any 64-bit Linux device with a camera
**Needs:** a USB camera on `/dev/video0` looking at the bottle from the
side — or nothing: the editor runs every program on the drawn bottle it
ships, and the screen's lamps answer on the desk

![The bottle screen](img/measure-screen.webp)

## The three programs

- **level** — a **Ruler** across the bottle's body (320 px = 80 mm) gives
  millimetres per pixel; a **Fill level** block walks its window from the
  shoulder down, finds the surface and answers its height above the
  bottle's bottom in millimetres (70 mm on the drawn bottle), with a
  tolerance of 60 to 80 mm.
- **cap** — a **Fixture** taught on the bottle's top finds the bottle
  wherever it stopped and shifts the picture, so the **Part in place**
  window drawn on the cap stays on the cap: a dark part whose centre must
  sit within 15 px of where it was taught.
- **label** — a **Crop** to the label feeds a **Read code** (the Code 128
  on it), a **Part in place** checks the white label sits where it
  should.

Every program runs twice a second and writes its results into
variables: `level_mm`, `level_ok`, `cap_ok`, `fx_found` and `fx_dx` (the
Fixture's answer), `label_text`, `label_read`, `label_ok`. The PLC
program's one rung ANDs the three `ok` variables into `ok`.

## The screen

The camera's picture with the three windows drawn over it (green: the
level, orange: the cap, blue: the label), the Fill level block's own
picture beside it with the surface it found, and the three results —
the level in millimetres with its lamp, the cap with the Fixture's
"found" and its shift, the label's text — under a large lamp for the
rung.

## Built step by step

[Measuring, step by step: a bottle](tutorial-measuring.md) builds this
project from its first block, with every block window on the way.
