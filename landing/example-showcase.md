---
title: Showcase on STM32F746
source: docs/example-showcase.md
hero: img/example-f7-main.webp
---

# One project, any silicon - and a SIMATIC on the same cable

The same runtime, languages, widgets and editor on an STM32F7 Discovery with a 4.3" touch screen and ethernet - reading a SIMATIC S7-1200 live on two of its five screens.

## Who it is for
- Teams who need their HMI projects independent of one chip family
- Integrators adding an operator screen to an existing SIMATIC S7-1200
- Anyone displaying fieldbus status words on a panel
- Projects in languages with accented characters

## What you get
- A project that is not tied to a chip family: a different board underneath, nothing in the project has to know
- A font carrying accented characters, sharp vector icons, a set clock
- Atomic bit access: three independent writers in one 16-bit word, none undoing another
- Four lamps on four bits of one variable - no logic between them
- A SIMATIC data block read every 200 ms, one value written back as a command
- A link lamp beside the PLC's clock bit - the shortest proof the PLC is in RUN and the link is alive
- The panel's own value and the controller's value on one trend, with the alarm list under it
- Online view of the program over the network: the editor takes an IP address wherever it takes a COM port
- The same screens in a phone browser at `http://<board>/`

## How it works
1. Main: a value in a large font with a bar under it, vector icons and switches bound to variables.
2. Info: a line of accented text as a font test, a counter, and a switch writing one bit of a word the logic is hammering at the same time.
3. States: four lamps on four bits of one 16-bit variable - two bits driven by the program at different rhythms, one by the switch on Info, one by the switch beside them.
4. PLC: a data block of the SIMATIC with the controller's own addresses printed beside the values; `DB120.DBW4` is typed here and written to the PLC.
5. Trend: the board's simulated temperature and the REAL the SIMATIC holds on one trend widget, with the project's alarms below.
6. Online: green is current flowing, every pin carries its live value - over ethernet.

## Pictures
- ![The main screen: temperature, switches, icons and the brand mark](img/example-f7-main.webp) - Main: one big number, a bar, icons and switches
- ![The info screen: a line of accented text, a counter, the brand mark and a bit switch](img/example-f7-info.webp) - Info: the accented-text font test and bit access
- ![The states screen: four lamps on four bits of one word](img/example-f7-states.webp) - States: four lamps, four bits, one variable, no code
- ![The PLC screen: a data block read live, one value written back, the controller's clock bit as the link lamp](img/example-f7-plc.webp) - PLC: the SIMATIC data block with its addresses, link lamp and clock-bit lamp
- ![The trend screen: the panel's own value and the controller's on one chart, with the alarm list below](img/example-f7-trend.webp) - Trend: panel value and PLC value together, alarms below
- ![The same rungs with live values from a running board: green power flow, 233 cycles counted](img/editor-online.png) - Online over the network: simulated temperature 30.7, filter output 36.8, counter 233

## Runs on
- ST 32F746G-DISCOVERY, 4.3" landscape, 480×272, ethernet, capacitive touch
- SIMATIC S7-1200 on the same ethernet with PUT/GET allowed (two of the five screens); without one the screens still run and the link lamp stays dark
- WEBview in a phone browser

## Facts to keep exact
- Five screens: Main, Info, States, PLC, Trend; three need nothing wired up
- Board resolution 480×272 landscape, 4.3"
- Font test line: *Príliš žltučký kôň úpel ďábelské ódy*
- States: four lamps on four bits of one 16-bit variable; three independent writers into one word
- PLC data block read every 200 ms; `DB120.DBW4` written; a write is a command, not a force - the PLC owns the value again on its next scan
- Link lamp + `%M0.5` (a bit of the controller's clock byte)
- Address in the label example: `DB120.DBD0`
- Online shot values: simulated temperature 30.7, filter output 36.8, counter 233
- Stopping the PLC: link lamp goes out, alarm arrives after three seconds, the panel's counter keeps running
- Try: flip bit 1 on Info (lamp follows); flip bit 3 (number under the lamps changes by 8); change the sweep of `sim_temp` (high alarm fires and clears)
- An alarm shown twice: as a lamp coloured by the alarm system and in an alarm table - one definition

## Call to action
Download the ctrl32 editor and open the shipped project `examples\f746_disco_example.prj32`.
