---
title: House dashboard
source: docs/example-house-dashboard.md
hero: img/house-home.webp
---

# A house on one 7" panel - heating, energy, lights, doors and the camera at the door behind frosted glass

Seven dark, translucent screens over photographs of the house they control: the clock and the weather, six heated rooms, the energy flow between the solar panels, the battery, the grid and the car, the lights and the shading, the garage, the front door and the alarm - and the door itself: the live picture of a small camera device at the door, its bell and the door strike. A simulated house runs behind the screens, so the dashboard is alive the moment it opens; the door is real, a second device of the same project.

## Who it is for
- Integrators who build smart-home panels for family houses and apartments
- Builders of heat-pump, photovoltaic and battery systems who want one wall panel for the whole installation
- Anyone who wants a door intercom on the wall panel instead of a second system beside it
- Anyone who wants a premium-looking dashboard without drawing a widget by hand
- Teams who want to show a complete home panel on the desk before a house is wired

## What you get
- **Home:** a large clock with the day and a greeting, the outside temperature and humidity, a three-day forecast, the living room's temperature and setpoint, the solar output and the battery, the alarm state, and three scenes (Evening, Away, Night)
- **Weather:** the condition, the temperature and how it feels, humidity, wind, pressure and the chance of rain today, and a four-day forecast with highs, lows and rain - the real weather of your place, read by the panel from the internet every half hour; the simulated weather stands in while the panel is offline
- **Climate:** six rooms, each with its temperature, its setpoint with − and + buttons and a flame lit while it heats; the heat pump's power, flow and return temperatures and COP; the hot-water tank with its level bar
- **Energy:** the energy flow between the solar panels, the grid, the house, the battery and the car; the battery's charge and power; today's power use split into heating, car and house; today's produced, consumed, exported and imported kWh; the solar output over the last 12 hours and how self-sufficient the house is today
- **Lights:** eight lights that switch with a touch, three shading positions on sliders, a dimmer, and All on / All off / Evening mood / Night
- **Access:** the garage door (open, closed or moving) and when it last opened, the front door lock, the alarm with its four zones, and the car charger
- **Door:** the live picture of the camera at the door, the doorbell with the rings today and the time of the last one, the lock state and the strike, an **Open door** button that releases the strike for five seconds, and the lock button; while the bell rings, a bell appears on the Door tab of every screen
- The camera device: a thumb-size board with a camera, a bell button and a relay output, running the ordinary runtime - nothing to program on it
- The setpoints are kept over a restart, and the clock sets itself from the internet

## How it works
1. Each screen is one background picture that already carries the frosted cards, the fixed words and the fixed icons; only the live parts - values, state icons, sliders, bars, the camera - draw over it.
2. The buttons, switches and the navigation sit under the picture: the picture covers them, a touch still reaches them.
3. Program `SIM` is the house, one step a second: the outdoor temperature follows the day, the solar output follows the sun, the load has its morning and evening peaks, the rooms heat with hysteresis through the heat pump, the battery takes the surplus and covers the deficit, the grid the rest.
4. The weather is real: the panel's web source reads the forecast service every 30 minutes - the current weather, how it feels, humidity, wind, pressure and four days of forecast land in variables, and the program shows them while the last read succeeded. Without the internet the program draws a week of weather of its own, so the screens are never empty.
5. A state icon is two icons at the same place, each shown with `visible_if` on the state and its opposite - a lit and a dark bulb, an open and a closed lock, a quiet and a ringing bell.
6. The large digits are Noto Sans faces carried in the project, 48 and 76 px.
7. The project is a net32 system of two devices: **panel** (node 1, the P4 on the wall) and **camera** (node 2, a Seeed XIAO ESP32S3 Sense at the door). The camera device serves its picture as a Motion-JPEG stream on its own web address; the panel reads the stream into the Door screen's camera element and decodes every frame in hardware.
8. The bell button on the camera device is a variable published over net32. The panel subscribes to it: a press counts a ring, records the time, lights the lamp for ten seconds and marks the Door tab on every screen. **Open door** publishes the strike's command for five seconds; the camera device pulses its relay for five seconds at most, whatever the panel says.
9. Replace the simulation with the real house: bind the variables to Modbus, MQTT or the panel's own inputs and delete the program `SIM` - the screens, the weather and the door stay as they are.

## Setting it up
1. **Open the project.** The tree shows the system's two devices, **panel** and **camera**; the panel carries the seven screens, the **Cameras** node and the **Clock**, the camera device its **WiFi** node and its **Camera** node.
2. **The camera device's WiFi.** Click its **WiFi**: the mode *STA*, the **Wi-Fi name (SSID)** and the **Wi-Fi password** of the house network. The shipped project carries placeholders; nothing joins until these are yours. The device announces itself on the network as `door-cam.local`.
3. **The panel.** On Ethernet nothing needs setting - the panel takes its address from the router. The camera's address under **Cameras** is `http://door-cam.local/cam.mjpg`; change it only if you renamed the camera device or gave it a fixed address.
4. **Your place.** The panel's **Web data** node carries the source `weather`: the forecast service's address with the latitude and longitude of the shipped project in it. Put your own coordinates into the address (two numbers, the rest stays) - or open the **Weather** preset, which writes a fresh source for any place. The panel needs the internet for this; everything else runs without it.
5. **The camera device's page.** The **Camera** node shows the sensor's settings - 640×480 at 10 frames a second, quality 12 - and its wiring; the pins come from the board, nothing to assign.
6. **Wiring at the door.** The bell button between pin D0 and GND (the pin's pull-up holds it high, a press pulls it low). The strike's relay module on pin D1: the pin gives a logic level, the module's own driver switches the strike's current.
7. **Deploy both devices** - the system page deploys them together, or each one with F5 while it is selected. The panel shows the picture a few seconds after both are up; the **camera online** lamp on the Door screen says the camera device is heard over net32.
8. **Try it.** Press the bell: the lamp on the Door screen rings for ten seconds, the count grows, the time of the ring is kept, and the Door tab of every other screen shows a bell. Press **Open door**: the strike is released for five seconds on the camera device and the screen says so. About ten seconds after the panel starts, the Weather screen switches from the drawn weather to the real one.

## Pictures
- ![The Home screen over a photograph of a modern house at dusk: the clock, the day and a greeting, the weather card with a three-day forecast, and four cards along the bottom - the living room, the solar output, the alarm and the scenes](img/house-home.webp) - Home
- ![The Weather screen: the current condition and temperature, feels like, humidity, wind, pressure and the rain today, and a four-day forecast with highs, lows and rain](img/house-weather.webp) - Weather
- ![The Climate screen: six room cards with temperature, setpoint and minus and plus buttons, the heat pump with flow, return and COP, and the hot-water tank](img/house-climate.webp) - Climate: six rooms, the heat pump, hot water
- ![The Energy screen: the energy flow between solar, grid, home, battery and car, the battery ring, the power use split, today's kWh bars and the solar output over the last 12 hours](img/house-energy.webp) - Energy
- ![The Lights screen: eight light tiles, some lit, three shading sliders, the living-room dimmer and four scene buttons](img/house-lights.webp) - Lights and shading
- ![The Access screen: the garage door closed, the front door locked, the alarm disarmed with its zones, and the car charger](img/house-access.webp) - Access
- ![The Door screen: the camera element, the doorbell ringing, the front door locked with the strike released, the Open door and Lock buttons, and the camera online with one ring today](img/house-door.webp) - Door: the intercom
- ![The net32 system in the editor: the camera device as node 2 with bell and door_rel, the panel as node 1 with door_rel and bell](img/house-system.webp) - Two devices, one net32 system

## Runs on
- The panel: Makerfabs MaTouch ESP32-P4 7" (1024×600), on Ethernet or WiFi
- The camera device: Seeed XIAO ESP32S3 Sense at the door, on WiFi - the camera on its expansion board, the bell button on D0, the strike's relay on D1
- Nothing needed to start: the simulated house runs on the panel and in the editor's simulation; without the camera device the Door screen shows the camera element empty and the camera lamp dark; without the internet the Weather screen shows the simulation's weather

## Facts to keep exact
- Seven screens: Home, Weather, Climate, Energy, Lights, Access, Door; the navigation bar on the left of every screen
- Six heated rooms: living room, kitchen, bedroom, kids' room, bathroom, office; − and + change the setpoint
- Three scenes on Home: Evening, Away, Night
- Eight lights: facade, garden, path, entrance, living room, kitchen, dining, terrace; three shading sliders: living room, bedroom, office
- Four alarm zones: ground floor, upper floor, garage, garden
- The energy flow shows solar, grid, home, battery and car; the battery shows charging or discharging
- Two devices, one net32 system: panel = node 1, camera = node 2; the camera device publishes `bell`, the panel publishes `door_rel`
- The camera: 640×480 at 10 frames a second, JPEG quality 12; the stream at `http://door-cam.local/cam.mjpg`, the latest frame at `/cam.jpg`
- The bell button on the camera device's D0 (to GND), the strike's relay on its D1; the strike is released for 5 s at most, on both sides
- A ring lights the lamp for 10 s, counts (the count starts over at midnight) and records the time; the Door tab of every screen shows a bell while it rings
- The shipped project carries placeholder WiFi settings on the camera device; the panel needs none on Ethernet
- The weather comes from the panel's web source: the forecast service read every 30 minutes, 23 fields (the current weather and four days), the status variable `web_ok`; the place is the latitude and longitude in the source's address
- The simulation's drawn weather is shown while `web_ok` is false - at the desk always, on the panel until the first read and whenever the internet is gone
- Setpoints are retained variables, kept over a restart
- The clock is set over NTP, Central European time
- The frosted look is baked into the backgrounds: the runtime draws no translucent fill
- The simulation steps once a second; the door is not simulated, the weather only while the web is not read

## Call to action
Download the ctrl32 editor and open the shipped project `examples\house_dashboard.prj32`.
