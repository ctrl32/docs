---
title: Your first project
source: docs/tutorial.md
hero: img/newproj-wizard.webp
---

# From an empty editor to a running project in half an hour

Build a project with three variables, one rung of ladder and a screen, test it in simulation on your PC, and download it to a board only at the very last step.

## Who it is for
- Anyone opening the ctrl32 editor for the first time
- Electricians and automation engineers who think in ladder logic
- Teams who want to test logic and screens before any hardware arrives

## What you get
- A New project wizard: name, location, hardware, theme and what the project does, in one dialog
- Variables in the PLCopen shape (`VAR_GLOBAL ... END_VAR`), with access rights for screens
- A ladder editor with a Toolbox of blocks and a Properties panel for every pin
- A screen canvas that runs the board's own renderer - what you place is what appears on the glass
- Simulation on the PC: the same logic, live screens, no hardware
- A download that cannot brick a board: the old program survives a failed download
- ONLINE monitoring of the real board with live values in the rungs
- WEBview in a browser with nothing drawn for it: with no browser screens defined, the board serves its own

## How it works
1. Press New project, name it `first_light`, pick a board (any board with a display - simulation does not care), keep *Visualization on the display* and *First program in LD*.
2. In VAR declare `button`, `light` and `delay : TIME := T#10s`.
3. In PLC_PRG draw one rung: contact `button`, a TOF block with PT = `delay`, coil `light`.
4. On the HMIview screen add a button, a led, an input and a label, and bind them.
5. Press Simulate: press the button and the lamp stays on for ten seconds after release; type `2` into the delay field and it changes without a rebuild.
6. Connect a board over USB, flash the runtime once, download with F5.
7. Press ONLINE to watch the real board, and open its address in a browser for WEBview.

## Pictures
- ![The New project wizard](img/newproj-wizard.webp) - every ctrl32 project starts here
- ![A board picked: its description and photo](img/newproj-board.webp) - the board card shows what the board carries
- ![The three variables in VAR](img/first-variables.webp) - button, light and delay in the PLCopen shape
- ![The rung, the TOF block selected, its pins in Properties](img/first-ladder.webp) - the whole program is one rung
- ![The block's sheet](img/first-sheet.webp) - the same pin rows, opened right where the block is
- ![The screen: a button, a lamp, the delay](img/first-screen.webp) - the canvas runs the board's own renderer
- ![The toolbar: the port picker and the download button](img/deploy-toolbar.webp) - pick the port, press download
- ![The Flash runtime dialog: the board's precompiled firmware, one button](img/deploy-runtime.webp) - the runtime is flashed once

## Runs on
- Any board in the catalog with a display (simulation needs no hardware at all)
- Connection: USB cable for the first runtime flash and download; network for WEBview and later downloads

## Facts to keep exact
- Finished result: `tutorials\first_light.prj32`; the file lands at `<location>\first_light\first_light.prj32`
- Default location: `Documents\ctrl32\projects`
- New project: Welcome tab button, first toolbar icon, or `Ctrl+N`
- Tree objects under Application: VAR (variables), PLC_PRG (program), HMIview (board screens), WEBview (browser screens); VAR, PLC_PRG and one screen are created with the project
- Variables: `button : BOOL { access := rw }`, `light : BOOL`, `delay : TIME := T#10s { access := rw }`; Apply = `Ctrl+Enter`
- `rw` = a screen may write the variable; `light` is written by the program only
- A TIME holds milliseconds - `T#10s` is 10000; a screen shows `10s`, `2s500ms`, `1m5s`; an input's keypad takes seconds (milliseconds when the unit is `ms`)
- TOF = off-delay timer: Q follows the input at once when it rises and holds for PT after it drops; the rung is IN, the coil is Q; TOF is in the Toolbox group Timers
- Screen: button bound to `button` (text *Push*, mode `momentary`), led to `light`, input to `delay` (min 0.5, max 60), label *Hold to light*; make the button at least 40 px tall
- Simulate is in the Debug menu; ONLINE is the plug icon
- Download: toolbar download icon or `F5`; it goes into the inactive slot, is verified, then activated
- Tip kept from the page: name variables for what they are (`light`), not where they are (`gpio32`)

## Call to action
Download the editor and open `tutorials\first_light.prj32` - or build it yourself in half an hour.
