---
title: House dashboard
source: docs/example-house-dashboard.md
hero: img/house-home.webp
---

# A house on one 7" panel - heating, energy, lights and doors behind frosted glass

Six dark, translucent screens over photographs of the house they control: the clock and the weather, six heated rooms, the energy flow between the solar panels, the battery, the grid and the car, the lights and the shading, the garage, the front door and the alarm. A simulated house runs behind them, so the dashboard is alive the moment it opens.

## Who it is for
- Integrators who build smart-home panels for family houses and apartments
- Builders of heat-pump, photovoltaic and battery systems who want one wall panel for the whole installation
- Anyone who wants a premium-looking dashboard without drawing a widget by hand
- Teams who want to show a complete home panel on the desk before a house is wired

## What you get
- **Home:** a large clock with the day and a greeting, the outside temperature and humidity, a three-day forecast, the living room's temperature and setpoint, the solar output and the battery, the alarm state, and three scenes (Evening, Away, Night)
- **Weather:** the condition, the temperature and how it feels, humidity, wind, pressure and the chance of rain today, and a four-day forecast with highs, lows and rain
- **Climate:** six rooms, each with its temperature, its setpoint with − and + buttons and a flame lit while it heats; the heat pump's power, flow and return temperatures and COP; the hot-water tank with its level bar
- **Energy:** the energy flow between the solar panels, the grid, the house, the battery and the car; the battery's charge and power; today's power use split into heating, car and house; today's produced, consumed, exported and imported kWh; the solar output over the last 12 hours and how self-sufficient the house is today
- **Lights:** eight lights that switch with a touch, three shading positions on sliders, a dimmer, and All on / All off / Evening mood / Night
- **Access:** the garage door (open, closed or moving) and when it last opened, the front door lock, the alarm with its four zones, and the car charger
- The setpoints are kept over a restart, and the clock sets itself from the internet

## How it works
1. Each screen is one background picture that already carries the frosted cards, the fixed words and the fixed icons; only the live parts - values, state icons, sliders, bars - draw over it.
2. The buttons, switches and the navigation sit under the picture: the picture covers them, a touch still reaches them.
3. Program `SIM` is the house, one step a second: the outdoor temperature follows the day, the solar output follows the sun, the load has its morning and evening peaks, the rooms heat with hysteresis through the heat pump, the battery takes the surplus and covers the deficit, the grid the rest.
4. A state icon is two icons at the same place, each shown with `visible_if` on the state and its opposite - a lit and a dark bulb, an open and a closed lock.
5. The large digits are Noto Sans faces carried in the project, 48 and 76 px.
6. Replace the simulation with the real house: bind the variables to Modbus, MQTT or the panel's own inputs and delete the program `SIM` - the screens stay as they are.

## Pictures
- ![The Home screen over a photograph of a modern house at dusk: the clock, the day and a greeting, the weather card with a three-day forecast, and four cards along the bottom - the living room, the solar output, the alarm and the scenes](img/house-home.webp) - Home
- ![The Weather screen: the current condition and temperature, feels like, humidity, wind, pressure and the rain today, and a four-day forecast with highs, lows and rain](img/house-weather.webp) - Weather
- ![The Climate screen: six room cards with temperature, setpoint and minus and plus buttons, the heat pump with flow, return and COP, and the hot-water tank](img/house-climate.webp) - Climate: six rooms, the heat pump, hot water
- ![The Energy screen: the energy flow between solar, grid, home, battery and car, the battery ring, the power use split, today's kWh bars and the solar output over the last 12 hours](img/house-energy.webp) - Energy
- ![The Lights screen: eight light tiles, some lit, three shading sliders, the living-room dimmer and four scene buttons](img/house-lights.webp) - Lights and shading
- ![The Access screen: the garage door closed, the front door locked, the alarm disarmed with its zones, and the car charger](img/house-access.webp) - Access

## Runs on
- Makerfabs MaTouch ESP32-P4 7" (1024×600)
- Nothing needed to start: the simulated house runs on the panel and in the editor's simulation

## Facts to keep exact
- Six screens: Home, Weather, Climate, Energy, Lights, Access; the navigation bar on the left of every screen
- Six heated rooms: living room, kitchen, bedroom, kids' room, bathroom, office; − and + change the setpoint
- Three scenes on Home: Evening, Away, Night
- Eight lights: facade, garden, path, entrance, living room, kitchen, dining, terrace; three shading sliders: living room, bedroom, office
- Four alarm zones: ground floor, upper floor, garage, garden
- The energy flow shows solar, grid, home, battery and car; the battery shows charging or discharging
- Setpoints are retained variables, kept over a restart
- The clock is set over NTP, Central European time
- The frosted look is baked into the backgrounds: the runtime draws no translucent fill
- The simulation steps once a second

## Call to action
Download the ctrl32 editor and open the shipped project `examples\house_dashboard.prj32`.
