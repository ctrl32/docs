---
title: Knob panel on the M5Stack Dial
source: docs/example-m5dial-knob.md
hero: img/dial-home.webp
---

# A round knob panel - turn to choose, press to change

The M5Stack Dial is a round 1.28" glass inside a rotary knob. This example makes it a small room controller: a ring of icons as the home screen, a heating setpoint on an arc the knob turns, a light with a switch and a dimmer, and a fan whose propeller spins at the fan's speed. The knob alone runs every screen; the touch glass works too.

## Who it is for
- Builders of room controllers, thermostats and appliance front panels
- Anyone who wants a knob-and-glass interface without writing firmware
- Designers of round displays - wall controllers, ovens, coffee grinders, amplifiers
- Teams who want to try a knob interface on the desk with a simulated room

## What you get
- **Home:** a wheel of four icons - Heating, Light, Fan, Setup; turning the knob moves the selection round the ring, the selected item's name in the centre, a press opens its screen
- **Heating:** an arc from 15 to 28 °C with the setpoint in its centre and the room temperature under it; press to edit, turn to change, press again to finish
- **Light:** an on/off switch and a dimmer slider; the knob walks between them
- **Fan:** a propeller that turns at the fan's speed, a marker that rides a circle as the speed climbs, the speed in rpm and the fan's switch
- **Setup:** the knob's raw counts, for checking the encoder
- A home button on every screen; the round glass is masked round in the editor as on the device

## How it works
1. The project's `knob:` names the encoder and its push button: the encoder moves the focus from widget to widget, a press acts on the focused widget (or starts and ends editing a value), a long press goes home.
2. The home screen is one `wheel` widget: its items are the icons, their names and the screens they open.
3. The arc edits the setpoint while it is being edited; it draws the value in its centre itself.
4. The propeller is an icon with `rotate:` - its turning speed follows the variable `fan_rpm`; the marker is an icon with `move:` on a circle from -120° to +120° as the speed goes from 0 to 1200 rpm.
5. Program `SIM` is the room: the room temperature drifts toward the setpoint, the fan spins up when it is switched on and runs down when it is switched off.

## Pictures
- ![The round home screen: four icons on a ring - a flame, a bulb, a fan and a gear - with the flame selected and the word Heating in the centre](img/dial-home.webp) - Home: the wheel of icons
- ![The Heating screen: an orange arc with its handle, the setpoint 21.0 °C in the centre, the room temperature 20.4 °C under it and a home button](img/dial-heating.webp) - Heating: the knob turns the arc
- ![The Light screen: the word Light, a switch turned on and a dimmer slider in yellow, and a home button](img/dial-light.webp) - Light: switch and dimmer
- ![The Fan screen: a cyan propeller, an orange marker on its circle, 1180 rpm and the fan's switch turned on](img/dial-fan.webp) - Fan: the propeller turns at the fan's speed

## Runs on
- M5Stack Dial (ESP32-S3, round 240×240 glass, rotary encoder with a push button)
- Nothing needed to start: the room is simulated

## Facts to keep exact
- Glass 240×240, round; the encoder on GPIO 40/41, the push button on GPIO 42 (pressed = low); 4 encoder counts per step
- The knob: turn = move the focus or change the edited value, press = act or edit, long press = home
- Widgets used: `wheel` (home), `arc` (heating), `switch` and `slider` (light), icons with `rotate:` and `move:` (fan)
- Setpoint range 15-28 °C, start 21.0 °C; the fan runs up to 1200 rpm
- In WEBview, the browser's arrow keys, Enter and Escape act as the knob
- The encoder's direction and the touch orientation are set on the board (`invert:` on the encoder)

## Call to action
Download the ctrl32 editor and open the shipped project `examples\m5dial_knob.prj32`.
