---
title: Lights from the glass
source: docs/tutorial-ha-lights.md
hero: img/ha-lights-glass.webp
---

# Switch and dim real Zigbee lights from a touch panel on the wall

The board never speaks Zigbee: its switches and its slider are ordinary variables, MQTT discovery turns them into Home Assistant entities, and four small automations bind them to the real lights - with the true state reported back to the glass.

## Who it is for
- Home Assistant users who want a wall panel that works locally
- Makers with Zigbee bulbs or relay lights who want a touch screen to drive them
- Anyone who wants commands and real feedback kept honestly apart

## What you get
- A touch screen with two light cards: a dimmable ceiling bulb (switch + brightness slider) and a wall relay light (on/off), plus one **All off** button
- The design worth copying: **two truths per card** - the switch is what you *ask*, the lamp beside it is what Home Assistant *reports back* from the real bulb (`light1_on` vs `fb1_on`)
- The "any light on" lamp in the header sums the ACTUAL states, not the wishes
- MQTT discovery: the board appears in Home Assistant as a device with six entities
- The glass and the phone stay in step because they move the same variable
- Three ladder rungs and four ready Home Assistant automations (command and feedback per light)
- A retentive brightness value

## How it works
1. New project on the ST 32F746GDISCOVERY, 480x272; Ethernet with DHCP runs by itself.
2. Create the command, feedback and summary variables.
3. Turn on MQTT with discovery; mark commands and feedbacks writable, the summary read-only.
4. Draw three rungs: heartbeat, the summary lamp from the feedbacks, the all-off edge.
5. Draw one landscape screen with two cards and the All-off footer; download (F5) over the network or USB.
6. Add the command and feedback automations in Home Assistant and flip the switch: the bulb lights, the lamp follows a beat later.

## Pictures
- ![The glass: two lights with their feedback lamps, a brightness slider and one button that turns everything off](img/ha-lights-glass.webp) - the light panel on the glass
- ![The three rungs: the heartbeat, the summary lamp built from the feedback rather than the commands, and the all-off edge](img/ha-lights-ladder.webp) - the three ladder rungs

## Runs on
- STM32F746-DISCO (480x272 touch, Ethernet)
- MQTT broker and Home Assistant
- A dimmable Zigbee bulb (light 1) and a wall relay light (light 2)

## Facts to keep exact
- Project file `ha_lights_f7.prj32`, installed in `tutorials\`
- Variables: `light1_on` (bool, ceiling command), `light1_dim` (f32 %, retentive, brightness 1-100), `light2_on` (bool, wall command), `fb1_on`, `fb2_on` (bool, the REAL states written back by HA), `any_on` (bool, header lamp from the actuals, ladder), `all_off` (bool, the glass button)
- MQTT: client id `ctrl32-f7lights`, topic `ctrl32/f7lights`, `publish_mode: per_tag`, discovery on, `interval_ms: 1000`; writable: `light1_on`, `light1_dim`, `light2_on`, `fb1_on`, `fb2_on`; `any_on` read-only (a binary sensor)
- Ladder: 1 Hz BLINK; `any_on` = OR over `fb1_on`, `fb2_on`; All off = R_TRIG on the button, then a SEL per command writing `false` - the automations do the switching-off
- Each card: name, bulb icon, actual-state lamp (a `state:` colour set - yellow when lit), command switch; the ceiling card adds the slider with its percentage
- Four HA automations: ceiling command (on switch or slider change: `light.turn_on` with `brightness_pct` from the slider, else `light.turn_off`, mode restart), ceiling feedback (bulb state into `switch.ctrl32_f7lights_fb1_on`); the wall light gets the same pair without brightness
- The lamp watches `fb1_on`, never the command; the delay before the lamp follows is the round trip through the broker; MQTT itself is milliseconds
- The same command/feedback split is what a drive gets (controlword vs statusword)

## Call to action
Download the editor and open `tutorials\ha_lights_f7.prj32`.
