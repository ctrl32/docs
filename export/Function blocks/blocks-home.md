---
title: "Home automation"
slug: blocks-home
section: "Function blocks"
order: 140
sidebar_position: 140
generator: tools/docs_export.py
---

# Home automation

Twenty blocks for a house: the wall button and what it drives, the clock
and the sun. They live
in the `home` block library that ships with the editor, and the Toolbox
lists them under **Home** the moment a project uses the library (*File →
Libraries*, or `libraries: [ libraries/home.yaml ]` in the project file).
Every one of them is written in ST, the way you write your own blocks,
so you can open it, read it and copy it into a block of your own.

The idea behind the family is the **wall button**: one push-button on
the wall does everything a room needs. A short click switches a light,
a long press dims it, a double click sets a scene. The blocks below
understand that button and speak to lights, blinds and heating.

All times are `TIME` parameters (`T#400ms`, `T#3m`) and all of them
measure real milliseconds, never cycles. The defaults are the values a
house wants; the examples on this page use short ones so the pictures
and the tests fit in seconds.

![The lights of the shipped example: a PUSHBUTTON drives a TOGGLE, another one a STAIRLIGHT](img/home-lights.webp){: .sb-center}

---

## The blocks

<!-- fb-index: begin -->

| Block | What it does | Linux | ESP32 | STM32 |
|:---|:---|:---:|:---:|:---:|
| [PUSHBUTTON](/docs/blocks/home-pushbutton/) | Tells a short click from a long press on one wall contact. | yes | yes | yes |
| [MULTICLICK](/docs/blocks/home-multiclick/) | Counts the clicks of a burst. | yes | yes | yes |
| [TOGGLE](/docs/blocks/home-toggle/) | The light switch: every rising edge of TRIG flips Q; SET and RESET are the central commands. | yes | yes | yes |
| [STAIRLIGHT](/docs/blocks/home-stairlight/) | The staircase light: a pulse lights Q for PT, another pulse restarts the time, WARN blinks before the end. | yes | yes | yes |
| [DIMMER](/docs/blocks/home-dimmer/) | One button dims: a short click switches between off and the remembered level, a long press ramps. | yes | yes | yes |
| [PWM](/docs/blocks/home-pwm/) | A level into a slow square wave: Q is TRUE for IN percent of every PERIOD. | yes | yes | yes |
| [BLINDS](/docs/blocks/home-blinds/) | A roller shutter with two keys: UP and DOWN run the motor, the same key stops, the other key reverses, SAFETY drives up and locks. | yes | yes | yes |
| [TRAVEL](/docs/blocks/home-travel/) | Where the blind is: integrates the motor time into a position, 0 = up, 100 = down. | yes | yes | yes |
| [PRESENCE](/docs/blocks/home-presence/) | Somebody is here: holds PRESENT for T_HOLD after the last motion. | yes | yes | yes |
| [TWILIGHT](/docs/blocks/home-twilight/) | It is dark: DARK switches with hysteresis around THRESHOLD, filtered by T_FILTER so a cloud does not switch the garden. | yes | yes | yes |
| [THERMOSTAT](/docs/blocks/home-thermostat/) | A room: two-point heating with three setpoints, a boost and a window pause. | yes | yes | yes |
| [DAYTIME](/docs/blocks/home-daytime/) | A window in the day: Q while the clock is inside FROM..TO on one of DAYS. | yes | yes | yes |
| [SUNTIMES](/docs/blocks/home-suntimes/) | Today's sunrise and sunset: the minutes of the local day the sun rises and sets at a place. | yes | yes | yes |
| [ASTRO](/docs/blocks/home-astro/) | Day and dark by the sun: DAY between sunrise and sunset, DARK outside, each edge shifted by an offset. | yes | yes | yes |
| [SCHEDULE](/docs/blocks/home-schedule/) | Two windows a day, a value: VALUE is V_IN inside either window on the listed days and V_OUT outside. | yes | yes | yes |
| [SCENE](/docs/blocks/home-scene/) | Two channels, three scenes: an APPLY edge sets A and B to the levels of scene SEL; OFF clears both. | yes | yes | yes |
| [GATE](/docs/blocks/home-gate/) | A garage door or a gate: one impulse key cycles open - stop - close - stop; the photocell reverses a closing gate. | yes | yes | yes |
| [VENT](/docs/blocks/home-vent/) | The bathroom fan: runs with the light after a delay, runs on after it, runs on humidity, or by hand. | yes | yes | yes |
| [CENTRAL](/docs/blocks/home-central/) | Everything on, everything off, leaving: ON and OFF edges make a pulse; LEAVE makes the off pulse T_LEAVE later. | yes | yes | yes |
| [ENERGY](/docs/blocks/home-energy/) | Kilowatt-hours from a power: E counts kWh from a power in kW, once a second; COST is E times PRICE. | yes | yes | yes |

<!-- fb-index: end -->

## Standard functions in your own blocks

The blocks above are ST you can read. SUNTIMES uses the standard
functions `SIN`, `COS`, `TAN` and `ACOS`; `SQRT`, `ASIN`, `ATAN`,
`EXP`, `LN`, `LOG` and `EXPT(base, exponent)` are there as well, all on
REAL. See [Structured Text](/docs/programming/st-language/).

---

## How many fit in one program

The timers and edge detectors inside these blocks are the runtime's own
(TON, TOF, R_TRIG ...), and a program holds **32** of them. PUSHBUTTON
uses 3, TOGGLE 3, STAIRLIGHT 4, DIMMER 6, BLINDS 5, MULTICLICK 2,
TWILIGHT 2, THERMOSTAT 2, PWM, TRAVEL and PRESENCE 1 each, DAYTIME
none. A house with many rooms is several programs — one per floor or
one per function (lights, blinds, heating), which is also how you want
to read it. The editor refuses a program that grows past the limit
and says so at the block.

## The example and the tests

`examples/home_blocks.prj32` is a small house on one screen: a kitchen
light with a wall button, a staircase light, a dimmed lamp, one blind
and a room with heating. Open it, start the simulation and press the
buttons on the screen.

Every block is held by a simulation test that presses the buttons in
milliseconds and expects the outputs — the same tests run before every
release, so a block's behaviour is a promise, not a description.
