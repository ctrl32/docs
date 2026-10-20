---
title: Car cockpit on J1939
source: docs/example-car-cockpit.md
hero: img/cockpit-main.webp
---

# An instrument cluster that reads the vehicle bus - no program needed for a value to arrive

A driver's view on a 7" panel: speed and engine speed gauges, gear, fuel, coolant, battery, odometer, trip, turn signals and twelve warning lamps - with the panel a node on the vehicle's J1939 bus and engine faults spelled out in words.

## Who it is for
- Builders of trucks, buses, agricultural and construction equipment, generator sets and boats
- Integrators who need a cab display on SAE J1939
- Anyone who wants engine fault codes shown in plain words, not just numbers
- Teams who want to demo a cluster on the desk before a vehicle is connected

## What you get
- The cluster: two gauges with coloured scales and redline, tapered needles and large readouts, the gear (N, R or the number), fuel and coolant bars, battery voltage, odometer, trip, clock from the panel's own time, turn signals
- Twelve warning lamps: engine (MIL), stop, warning, oil pressure, battery, coolant, fuel, parking brake, ABS, belt, door, high beam - each lit in its own colour, dim otherwise
- An Engine screen with six round instruments: engine oil, transmission oil and coolant temperatures; oil, fuel delivery and boost pressures - each with green, amber and red bands
- A Communication screen: the node, its three control units with alive lamps, the four DM1 lamps, the first active fault code and a table of every signal with its parameter group
- A Faults screen: the alarm list plus the active DM1 fault code as SPN/FMI numbers, count, and in words
- A Parameters screen: limits the driver sets and the panel keeps over a restart, demo mode, units (mph), and a service counter
- Demo mode: the project opens driving itself through a drive cycle

## How it works
1. Under `j1939:` the panel is a node with an address and a NAME; each control unit lists the groups it sends and each signal names the variable it lands in - the group, start bit, width, gain and offset come from the shipped library.
2. Program `SIM` is the drive cycle: pulls away, shifts up, cruises, brakes and stops, burns fuel, warms the coolant, counts kilometres, blinks the turn signal, and raises a fault now and then.
3. Program `DASH` picks the source (the drive cycle in demo mode, the bus otherwise), computes the lamps against the parameters with hysteresis, watches each controller for silence, spells the fault code out, and runs the service counter.
4. Every alarm is `is_true` on a lamp variable the program sets, so a limit lives in a parameter the driver changes, not in the alarm's definition.
5. The scales, bezels, words and dim icons are one background picture per screen; only the live parts draw over it.
6. DM1 carries the lamps in its first two bytes and the first fault code in the next four; the program joins the SPN and sets one word variable per known code, shown with `visible_if` labels.

## Pictures
- ![The cockpit: the speed and rpm gauges with their scales, the gear in the middle, fuel and coolant bars, the battery, the odometer and the trip, the clock, the turn signals and the row of lamps](img/cockpit-main.webp) - The cluster
- ![The Engine screen: six round instruments with needles — the temperatures of the engine oil, the transmission oil and the coolant, the pressures of the oil, the fuel and the boost](img/cockpit-engine.webp) - Engine: six round instruments
- ![The Communication screen: the J1939 node and its three control units with their lamps, the DM1 lamps, the fault code, and the table of every signal with its group](img/cockpit-bus.webp) - Communication: the node, three control units, DM1, every signal with its group
- ![The Faults screen: the alarm list with an active fault code, the amber lamp and the MIL, and the code spelled out — SPN 110, FMI 0, engine coolant temperature, above normal](img/cockpit-faults.webp) - Faults: SPN 110 / FMI 0 spelled out
- ![The Parameters screen: the speed warning, the redline, the coolant and fuel warnings, the tank, the battery limit and the service interval; demo mode and the units; the service block with the odometer](img/cockpit-settings.webp) - Parameters: limits, demo mode, units, service

## Runs on
- Makerfabs MaTouch ESP32-P4 7" (1024×600)
- SAE J1939 on CAN: a CAN transceiver on the header pins TX 47 / RX 48
- Nothing needed to start: demo mode drives itself; a vehicle on the bus turns demo off and the gauges read the bus

## Facts to keep exact
- J1939 is the bus of trucks, buses, agricultural and construction equipment, generator sets and boats; a passenger car speaks over its diagnostic connector instead - that is vehicle diagnostics, on a Linux device
- Engine speed out of EEC1, coolant out of ET1, fault lamps out of DM1
- Engine screen values come out of ET1, EFL/P1, TRF1 and IC1
- Signal groups in the table: EEC1, EEC2, ET1, EFL/P1, LFE, VEP1, CCVS, AMB, HOURS, VD, DD, ETC1
- Panel node 128 on CAN 0 at 250 kbit/s; engine controller address 0, transmission 3, brakes 11
- A controller is alive while its values keep changing; two seconds of silence turns its lamp red and raises the alarm
- Faults example: SPN 110 = coolant temperature, FMI 0 = "above normal, most severe"
- Demo mode: a fault comes on its own every three minutes; two buttons (Inject a fault / Clear it) raise one now and clear it
- Needle: a `line` widget turned by the value, `rotate:` from -135° at minimum to +135° at maximum; gauge geometry 135° plus 270° of sweep, clockwise
- Lamp from an icon: `state: { var: l_oil, true_color: "#E83A3A", false_color: "#343A46", paint: fg }`
- Custom needle: `needle: false`, `show_value: false`; three `line` widgets of falling width plus a `shape` ellipse hub; the number is a `value` in an 84 px digit face
- A screen holds 64 widgets; a line is three of them (the line and its two points); the six small dials take one segment each
- Service interval is an `input` (keypad); the other parameters are spinboxes (a spinbox step stops at a few hundred)
- Hysteresis in ST: `IF cool > p_cool_lim THEN ... ELSIF cool < p_cool_lim - 4.0 THEN ...`
- Parameters kept over a restart: speed warning, redline, coolant and low-fuel warning, tank, battery limit, service interval; units (mph shown beside the gauge, the gauge keeps km/h); **Service done** is confirmed and starts a new interval
- Try: demo off with nothing on CAN - controller lamps go red after two seconds and the alarm says the bus is silent; on a real engine the gauges follow EEC1 and CCVS, and the DBC import adds groups that do not arrive

## Call to action
Download the ctrl32 editor and open the shipped project `examples\car_cockpit.prj32`.
