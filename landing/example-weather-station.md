---
title: Weather station
source: docs/example-weather-station.md
hero: img/meteo-now.webp
---

# A weather station of two devices - a glass indoors, a sensor outdoors, the forecast from the web

A 3.95" portrait glass shows the outdoor temperature, humidity and pressure measured by a small ESP32-C3 node outside, the three-day forecast the station reads from Open-Meteo itself, a large clock, and the last twelve hours as two trends. The two devices are one net32 system: the sensor publishes, the glass subscribes, and the project opens and deploys them together. Without the sensor the glass shows the web's outdoor values.

## Who it is for
- Makers and integrators who want a finished weather station for a hallway or a kitchen
- Anyone who wants a forecast on a panel without a server of their own
- Anyone learning how two ctrl32 devices share variables over net32, and how a device reads a web service
- Builders of small sensor nodes who need a display for them

## What you get
- **Now:** the clock and the date, today's condition as a large icon, the outdoor temperature, humidity, pressure with its three-hour tendency arrow, and a lamp that says the sensor is alive
- **Forecast:** today, tomorrow and the day after, each with an icon, the high, the low and the rain in mm
- **Clock:** a large clock with the day and the date, and the current weather under it
- **Trend:** the outdoor temperature and the air pressure over the last 12 hours
- Two colour schemes, night and autumn; the choice is kept over a restart
- The sensor node: a BME280 measuring temperature, humidity and pressure, sent over WiFi
- The outdoor values published over MQTT for a home system that wants them

## How it works
1. The project is a net32 system of two devices: **station** (node 1, the glass) and **sensor** (node 2, the ESP32-C3 with the BME280).
2. The sensor reads the BME280 on I2C and publishes its three values over net32 every two seconds; the station subscribes to them. Ten seconds of silence put the sensor lamp out, and the program shows the web's outdoor values instead.
3. The station's web source asks Open-Meteo every 30 minutes for the current weather and three days of forecast at the station's coordinates; the fields land in variables, `web_ok` says whether the last read succeeded.
4. Open-Meteo answers with WMO weather codes; program `WEATHER` turns each code into the station's own condition - sunny, clear night, partly cloudy, cloudy, fog, rain, thunderstorm, snow, wind - and the condition into the icon to show.
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
- Both on the same WiFi network with internet access for the forecast; an MQTT broker only if a home system should receive the values

## Facts to keep exact
- Four screens on the station: Now, Forecast, Clock, Trend; tabs along the bottom
- Station = net32 node 1, sensor = net32 node 2, net32 over UDP on WiFi
- The sensor sends every 2 s; a value older than 10 s counts as stale and the web's value takes over
- The web source: Open-Meteo, every 30 minutes, the current temperature, humidity, sea-level pressure, wind, weather code and day/night, and per day the code, high, low and precipitation; the coordinates are in the address
- Condition codes of the station: 1 sunny, 2 clear night, 3 partly cloudy, 4 cloudy, 5 fog, 6 rain, 7 thunderstorm, 8 snow, 9 wind, 0 unknown - mapped from the WMO codes by the program
- Pressure tendency: a sample every 30 minutes, compared with three hours back; ±1 hPa decides rising or falling
- The trends cover 12 hours with a sample every 30 seconds
- Colour schemes: night and autumn, a toggle on the Clock screen, retained
- The shipped project carries placeholder WiFi and broker settings; put in your network's name and password before deploying

## Call to action
Download the ctrl32 editor and open the shipped project `examples\meteo_station.prj32`.
