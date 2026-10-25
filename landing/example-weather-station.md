---
title: Weather station
source: docs/example-weather-station.md
hero: img/meteo-now.webp
---

# A weather station of two devices - a glass indoors, a sensor outdoors, the forecast from Home Assistant

A 3.95" portrait glass shows the outdoor temperature, humidity and pressure measured by a small ESP32-C3 node outside, the three-day forecast that Home Assistant writes to it over MQTT, a large clock, and the last twelve hours as two trends. The two devices are one net32 system: the sensor publishes, the glass subscribes, and the project opens and deploys them together.

## Who it is for
- Makers and integrators who want a finished weather station for a hallway or a kitchen
- Home Assistant users who want its forecast on a dedicated panel
- Anyone learning how two ctrl32 devices share variables over net32
- Builders of small sensor nodes who need a display for them

## What you get
- **Now:** the clock and the date, today's condition as a large icon, the outdoor temperature, humidity, pressure with its three-hour tendency arrow, and a lamp that says the sensor is alive
- **Forecast:** today, tomorrow and the day after, each with an icon, the high, the low and the rain in mm
- **Clock:** a large clock with the day and the date, and the current weather under it
- **Trend:** the outdoor temperature and the air pressure over the last 12 hours
- Two colour schemes, night and autumn; the choice is kept over a restart
- The sensor node: a BME280 measuring temperature, humidity and pressure, sent over WiFi

## How it works
1. The project is a net32 system of two devices: **station** (node 1, the glass) and **sensor** (node 2, the ESP32-C3 with the BME280).
2. The sensor reads the BME280 on I2C and publishes `out_t`, `out_h` and `out_p` over net32 every two seconds; the station subscribes to the three and shows them. Ten seconds of silence put the sensor lamp out.
3. Home Assistant writes the condition and the three-day forecast into the station's variables over MQTT, one topic per variable (`<topic>/<variable>/set`); the station also publishes its outdoor values for Home Assistant to use.
4. The condition is a number - 1 sunny, 2 clear night, 3 partly cloudy, 4 cloudy, 5 fog, 6 rain, 7 thunderstorm, 8 snow, 9 wind, hail or exceptional, 0 unknown; program `WEATHER` turns each code into the icon to show. Without a forecast the station shows the sun by day and the moon at night.
5. The program keeps a pressure sample every 30 minutes; the difference against three hours ago picks the arrow - rising, falling or steady (1 hPa either way).
6. The clock is set over NTP; the date and the weekday come from the device's own time.

## Pictures
- ![The Now screen on a dark portrait glass: the time and date, a partly cloudy icon, 12.4 °C outside, the sensor lamp green, humidity 68 % and pressure 1016.2 hPa with a steady arrow, and the four tabs at the bottom](img/meteo-now.webp) - Now
- ![The Forecast screen: today partly cloudy 14 and 6 degrees with 10 mm of rain, tomorrow rain 11 and 7 degrees with 80 mm, the day after sunny 15 and 4 degrees](img/meteo-forecast.webp) - Forecast: three days
- ![The Clock screen: a large clock with Sunday and the date, the autumn button, and the current weather with temperature, humidity and pressure](img/meteo-clock.webp) - Clock
- ![The net32 system in the editor: the sensor node 2 and the station node 1 on one line, each with out_t, out_h and out_p](img/meteo-system.webp) - Two devices, one net32 system

## Runs on
- The glass: Makerfabs MaTouch Lite ESP32-S3 3.95" (320×480 portrait)
- The sensor: an ESP32-C3-MINI-1 board with a BME280 at address 0x77 on I2C, SDA 7 / SCL 6
- Both on the same WiFi network; the forecast needs an MQTT broker and Home Assistant

## Facts to keep exact
- Four screens on the station: Now, Forecast, Clock, Trend; tabs along the bottom
- Station = net32 node 1, sensor = net32 node 2, net32 over UDP on WiFi
- The sensor sends every 2 s; a value older than 10 s counts as stale
- Forecast variables per day: code, high, low, rain (fc0 = today, fc1 = tomorrow, fc2 = the day after); the current condition is `w_code`
- MQTT in per-variable mode: Home Assistant writes `<topic>/<variable>/set`; the station publishes out_t, out_h, out_p and the pressure tendency
- Condition codes 0-9 as listed above
- Pressure tendency: a sample every 30 minutes, compared with three hours back; ±1 hPa decides rising or falling
- The trends cover 12 hours with a sample every 30 seconds
- Colour schemes: night and autumn, a toggle on the Clock screen, retained
- The shipped project carries placeholder WiFi; put in your network's name and password, and your broker, before deploying

## Call to action
Download the ctrl32 editor and open the shipped project `examples\meteo_station.prj32`.
