---
title: Thermostat on Olimex ESP32-EVB
source: docs/example-thermostat.md
hero: img/example-evb-0.png
---

# A complete wall thermostat, running the moment you download it

Ladder logic with hysteresis, an operator screen, a manual mode, a trend, alarms and a phone page - one small project on an Olimex ESP32-EVB that clicks its heating relay around the setpoint with nothing wired up.

## Who it is for
- Anyone starting a first project - this is the shape most first projects turn out to be
- Integrators who want a ready template for a simple on/off control loop
- Commissioning engineers who value a manual screen beside the automatic one
- Anyone evaluating ctrl32 on an ESP32 board without hardware on the bench

## What you get
- A wall thermostat on a 2.8" portrait screen driving the two relays the board has
- A simulated measurement that sweeps the range, so the relay audibly clicks around the setpoint on a bench
- A Home screen: a gauge for the measurement, setpoint buttons, and a switch for automatic mode
- A Manual screen with every actuator on its own - for commissioning and fault finding
- A Trend with two traces recorded in the board, so the history exists whether or not anybody is watching
- A States and motion screen: lamps from a variable, a panel whose background is the state, a marker travelling a scale
- Alarms that appear in the alarm table by themselves
- A WEBview page designed for a phone, not a copy of the board's screen

## How it works
1. A heartbeat: one BLINK on a spare output, so anybody at the board can see the program is running without a laptop.
2. A simulated temperature: SEL, RAMP and PT1 produce something that behaves like a real measurement.
3. The thermostat itself: one HYST comparator - two parameters, the entire control loop.
4. The relay: automatic AND cold, OR manual AND commanded. The interlock is in the logic, not in the screen, so it holds however the value is written.
5. The setpoint buttons: a rising edge into an addition, so holding a button does not run the setpoint away.

## Pictures
- ![The thermostat screen: a gauge, the setpoint, and the buttons](img/example-evb-0.png) - Home: the measurement, the setpoint, automatic on/off
- ![Manual control: both relays, individually](img/example-evb-2.png) - Manual: every actuator on its own
- ![The trend screen, moments after starting: the chart still filling, the two values below it](img/example-evb-3.png) - Trend: two traces recorded in the board, current values under the chart
- ![The states screen: lamps from a variable, a panel background, a marker on a scale](img/example-evb-5.png) - States and motion: two lamps on one variable (one from a named colour set, one with its own colours), a state background, a moving marker
- ![The ladder editor: five rungs of the thermostat, blocks in the rungs](img/editor-ladder.png) - The five-rung ladder program in the editor

## Runs on
- Olimex ESP32-EVB with a MOD-LCD2.8RTP display, 240×320 portrait
- Needs nothing wired up - it runs in simulation as it is
- WEBview page for a phone

## Facts to keep exact
- Screen: 2.8", 240×320, portrait (MOD-LCD2.8RTP)
- Two relays on the board; no temperature sensor on the board - the measurement is simulated
- Five rungs: BLINK heartbeat; SEL + RAMP + PT1 simulated temperature; HYST thermostat; relay logic (auto AND cold, OR manual AND commanded); rising edge into an addition for the setpoint buttons
- Manual heating acts only while automatic mode is OFF (interlock in the logic)
- Trend: two traces, recorded in the board
- Phone page content: a big number, the state, and the two controls that matter
- Try-it ideas: change ON/OFF on the HYST block (relay rhythm in the trend); change T on PT1 (bigger = smoother and later); add a second, lower-limit alarm
- Selling lines from the page: a manual screen "costs an afternoon, saves a day the first time something misbehaves"; a heartbeat is "one block"

## Call to action
Download the ctrl32 editor and open the shipped project `examples\olimex_evb_example.prj32`.
