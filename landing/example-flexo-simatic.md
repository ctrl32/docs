---
title: Flexo press SIMATIC panel
source: docs/example-flexo-simatic.md
hero: img/flexo-overview.webp
---

# The operator panel of an eight-colour flexo press - two data blocks in the SIMATIC, nothing else

A 7" panel that reads the PLC's status block and writes setpoints and commands over +7, with the real press drawn as a live mimic and the web moving on it while the line runs.

## Who it is for
- Builders and retrofitters of flexographic printing presses
- Plants with a SIMATIC S7-1200 or S7-1500 that need a modern operator panel
- Integrators who want an HMI without a tag mapping layer between panel and PLC
- Anyone who wants to show a press running on a desk, in demo mode

## What you get
- A light industrial look: navy header, pages on a left rail with the press's own pictograms, white cards, teal for running, blue for a setting, red for a fault, the eight print sections in their inks
- Press page: the vector drawing of the real press - unwind, central impression drum with eight print sections (form + anilox), bridge dryer, tower with two rewinds - and the web in magenta moving while the line runs
- START (confirmed), STOP, JOG (held), RESET, a line-shaft switch, the press state and the web state
- Sections page: eight print sections with sync and fault lamps, form speed and an enable switch each; aniloxes with their lamps; jog of one picked section
- Register page: longitudinal register error of every section in millimetres, correction of the selected section, auto register
- Heating page: eight drying chambers, two bridge dryer zones, two setpoints, heating switch
- Jobs page: jobs kept on the panel as recipes, Load / Save / Delete
- Diagnostics page: alarm list, PLC link status, the two data blocks, demo switch, two-minute trend of line speed and unwind tension
- Demo mode: the project opens running the press on the panel

## How it works
1. The pages bind the PLC's variables directly, with no copy in between: a value on a card is `DB100.DBD0`, a switch writes a bit of `DB101.DBW38`.
2. In demo mode the program `SIM` writes the read variables itself, so the same pages show the press on the panel.
3. A `led` or a `switch` with `bit: 3` reads or writes one bit of an integer variable - sixteen sync lamps, sixteen fault lamps and eight enable switches on three words.
4. The moving web is an `anim_image` with two frames (the web at two phases of its dashes); `tag: web_ph` picks the frame and `DASH` swaps it every quarter of a second while the line runs.
5. The selected section: a `button_matrix` writes 0 to 7 into `unit_sel`; the PLC (or the demo) hands back that section's correction and takes what is typed; the same selection picks the section a jog turns.
6. `DASH` derives the lamps (`l_webbreak`, `l_drv_flt`, `l_plc_lost`, ...) and every alarm is `is_true` on one; the PLC-silent alarm is quiet in demo mode on purpose.
7. The mimic is the vector drawing of the real press, rendered by the generator into two frames with the web layers over it; lamps, temperatures and tensions are live widgets placed by the drawing's own coordinates.

## Pictures
- ![The overview: the unwind, the central impression drum with the eight print sections around it, the bridge dryer and the two rewinds in the tower, the web in magenta over all of it; beside it START, STOP, JOG and RESET, the state and the web; under it the line speed, the three web tensions and the job](img/flexo-overview.webp) - Press overview with the moving web
- ![The Sections page: the eight print sections with their ink, a sync and a fault lamp, the form's speed and an enable switch each; the aniloxes with their lamps; the jog of one picked section](img/flexo-sections.webp) - Sections F1-F8 and aniloxes A1-A8
- ![The Register page: the longitudinal register error of every section in millimetres with a bar, and the correction of the selected section with its error now and the auto register switch](img/flexo-register.webp) - Register errors and correction
- ![The Heating page: the eight drying chambers between the colours with their temperatures and bars, the two zones of the bridge dryer, the two setpoints and the heating switch](img/flexo-heating.webp) - Heating: chambers and bridge dryer
- ![The Jobs page: the jobs kept on the panel as recipes with Load, Save and Delete, and the job's settings - line speed, the tensions, the dryers, the ramp, the repeat length, the job length](img/flexo-jobs.webp) - Jobs as recipes
- ![The Diagnostics page: the alarm list, the PLC link with its address, rack and slot and whether it answers, the two data blocks the panel uses, demo mode, and a two-minute trend of speed and tension](img/flexo-diag.webp) - Diagnostics: alarms, PLC link, trend

## Runs on
- Makerfabs MaTouch ESP32-P4 7" (1024×600)
- SIMATIC S7-1200 or S7-1500 at 192.168.0.55 with the two data blocks and PUT/GET switched on, over +7 (ethernet)
- Nothing needed to start: demo mode runs the press on the panel

## Facts to keep exact
- Eight-colour central-impression flexographic press; sections F1-F8, aniloxes A1-A8
- PLC address 192.168.0.55; PUT/GET switched on; two data blocks
- DB100 (read every 100 ms): `DBD0` line speed, `DBD4` drum speed, `DBD8` `DBD12` `DBD16` tensions A B C, `DBD20` `DBD24` `DBD28` metres on rolls A B C, `DBD32` `DBD36` bridge dryer's two zones, `DBD40` metres of the job, `DBD44` waste (both DINT), `DBX48.0`-`48.3` running / ramping / fault / web break, `DBW50` sync word (bits 0-7 forms F1-F8, 8-15 aniloxes A1-A8), `DBW52` fault word (same bits), `DBD56`-`DBD84` speed of the eight forms, `DBD88`-`DBD116` eight chamber temperatures, `DBD120`-`DBD148` eight register errors
- DB101 (written as the operator types): `DBD0` line speed, `DBD4` `DBD8` `DBD12` tensions A B C, `DBD16` bridge dryer, `DBD20` chambers, `DBD24` ramp, `DBD28` repeat length, `DBD32` job length (DINT), `DBX36.0`-`36.7` start / stop / jog / reset / line shaft on / heating on / auto register / section jog, `DBW38` sections enabled (a bit each), `DBW40` sections in impression, `DBW42` selected section 0-7, `DBD44` its correction
- The +7 client reads up to 64 variables of a PLC; this project uses 63 - which is why lamps are bits of words and the register is corrected for one selected section at a time
- Press states: stopped, ramping, running, jog, fault, web break; web: register within tolerance / out of tolerance
- Live on the mimic: a sync lamp per section, two dryer zone temperatures, tension and metres on the roll at unwind A and rewinds B and C
- Overview numbers: line speed in metres per minute with setpoint and drum turns, three tensions as numbers and bars, job: metres printed of job length, waste, repeat, ramp
- Register bar from minus one to plus one millimetre; correction stepped in hundredths of a millimetre; "all eight within half a millimetre" indicator; a typed correction is added to the auto register (the camera)
- Section jog: with the line standing, the picked form and its anilox turn at jog speed (washing or a plate change)
- Heating demo: chambers warm while heating is on and the line runs, cool when it stands
- Job recipe fields: line speed, three tensions, bridge dryer, chambers, ramp, repeat length, job length; Load writes into the fields and into the PLC (the fields are the PLC's own variables); Delete asks first
- Alarms: web break, drive fault, PLC silent, tension off setpoint, register out of tolerance, dryer cold, roll nearly empty, job done
- Diagnostics PLC link: address, rack, slot, period, answering or not; trend two minutes of line speed and unwind tension
- Generator: `tools/gen_flexo.py`; pictograms from the same set as the drawing
- Try: START with the line shaft on (speed ramps over the ramp time, web moves, sections in impression turn, lamps go green, metres count); switch a section off (form stops, its and its anilox's lamps grey); pick section 3 and hold JOG; after six minutes of running the web breaks in the demo (press stops, one drive shows a fault, RESET clears it); type a register correction; switch auto register off and watch errors drift; save, change, load a job; put a SIMATIC at 192.168.0.55 and switch demo off

## Call to action
Download the ctrl32 editor and open the shipped project `examples\flexo_simatic.prj32`.
