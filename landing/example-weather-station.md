---
title: Weather station
source: docs/example-weather-station.md
hero: img/meteo-now.webp
---

# A weather station of two devices - a glass indoors, a sensor outdoors, the forecast from the web

A 3.95" portrait glass shows the outdoor temperature, humidity and pressure measured by a small ESP32-C3 node outside, the three-day forecast the station reads from Open-Meteo itself over a secure connection, a large clock, and the last twelve hours as two trends. The two devices are one net32 system: the sensor publishes, the glass subscribes, and the project opens and deploys them together. Without the sensor the glass shows the web's outdoor values; without a network it shows nothing but the clock it last knew.

## Who it is for
- Makers and integrators who want a finished weather station for a hallway or a kitchen
- Anyone who wants a forecast on a panel without a server of their own
- Anyone learning how two ctrl32 devices share variables over net32, and how a device reads a web service over https
- Builders of small sensor nodes who need a display for them

## What you get
- **Now:** the clock and the date, today's condition as a large icon, the outdoor temperature, humidity, pressure with its three-hour tendency arrow, and a lamp that says the sensor is alive
- **Forecast:** today, tomorrow and the day after, each with an icon, the high, the low and the rain in mm
- **Clock:** a large clock with the day and the date, and the current weather under it
- **Trend:** the outdoor temperature and the air pressure over the last 12 hours
- Two colour schemes, night and autumn; the choice is kept over a restart
- The sensor node: a BME280 measuring temperature, humidity and pressure, sent over WiFi
- The outdoor values published over MQTT for a home system that wants them
- A complete, working web source to copy for any other service that answers JSON

## How it works
1. The project is a net32 system of two devices: **station** (node 1, the glass) and **sensor** (node 2, the ESP32-C3 with the BME280).
2. The sensor reads the BME280 on I2C and publishes its three values over net32 every two seconds; the station subscribes to them. Ten seconds of silence put the sensor lamp out, and the program shows the web's outdoor values instead.
3. The station's web source asks Open-Meteo every 30 minutes over `https://` for the current weather and three days of forecast at the station's coordinates; the eighteen fields land in variables, `web_ok` says whether the last read succeeded. The secure read waits for the clock, so the station sets its time over NTP first.
4. Open-Meteo answers with WMO weather codes; program `WEATHER` turns each code into the station's own condition - sunny, clear night, partly cloudy, cloudy, fog, rain, thunderstorm, snow, wind - and the condition into the icon to show.
5. The program keeps a pressure sample every 30 minutes; the difference against three hours ago picks the arrow - rising, falling or steady (1 hPa either way).
6. The clock is set over NTP; the date and the weekday come from the device's own time.

## Setting it up
1. **Open the project.** The tree shows the system's two devices, **station** and **sensor**, each with its own **WiFi** node; the station carries **Clock**, **MQTT** and **Web data** under its WiFi.
2. **WiFi on both devices.** Click the station's **WiFi**: the mode *STA* (the device joins a network), the **Wi-Fi name (SSID)** and the **Wi-Fi password** of your home network - a network that reaches the internet, because the forecast comes from it. The same on the sensor. The shipped project carries placeholders; nothing joins until these are yours. A station whose join fails raises its own access point instead and then shows the clock and zeros: no sensor, no network, no forecast.
3. **The clock.** The station's **Clock** node: **NTP time sync** on, the server `pool.ntp.org`, the timezone Central European with summer time. The forecast is read over a secure connection, and a secure read waits until the time is set - a certificate is valid from a date to a date.
4. **The place.** The **Web data** node opens the page with the source `weather`: its address carries the coordinates as the two numbers after `latitude=` and `longitude=` (the shipped project points at Banská Bystrica, 48.7363 N, 19.1462 E). To move the station, press **Weather (Open-Meteo)...**, type your latitude and longitude (a map shows them; four decimals place the point within about ten metres), keep 3 days and the current weather on, press **Create** - the source is replaced, the eighteen variables and the program stay. Editing the two numbers in the address does the same.
5. **The forecast model** (optional). Open-Meteo returns a model's value at the nearest grid point, not a measurement, and its default picks a model per region. If the station should agree with the forecast you trust on your phone, add that model to the end of the address, `&models=icon_eu` for instance; the Web data help page lists the names. Different models differ by a few degrees in the same hour - that is the forecast, not the station.
6. **MQTT** (optional). The **MQTT** node under the station's WiFi names the broker of a home system that should receive the outdoor values; put in your broker, or remove the node from its context menu when nothing listens. The station runs the same without it.
7. **Deploy both devices** - the system page deploys them together, or each one with F5 while it is selected. The station joins the network, sets its clock and reads the forecast; the first picture is on the glass about ten seconds after the start, and from then on every 30 minutes. A read that fails is retried after 30 seconds, a minute, two minutes, up to the period.
8. **Taking it along.** Away from home, the station reads the forecast through a phone's hotspot: give its WiFi the hotspot's name and password and deploy. The sensor is not on that network, so the sensor lamp stays dark and the glass shows the web's outdoor values.

## The secure connection in detail
- The address: `https://api.open-meteo.com/v1/forecast?latitude=48.7363&longitude=19.1462&current=temperature_2m,relative_humidity_2m,pressure_msl,wind_speed_10m,weather_code,is_day&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum&forecast_days=3&timezone=auto` - the current block and the daily block are what the eighteen fields point into, `timezone=auto` makes "today" the station's day
- The station checks the server's certificate chain against the public roots it carries, the name in the certificate against the host in the address, and the validity dates against its NTP clock; a server that fails any of the three is refused and the status variable `web_ok` goes FALSE
- One secure session per read: opened, the answer taken, closed. The session's buffers live in the board's external memory, so a read costs the glass about three kilobytes of internal memory for a few seconds and nothing between reads
- The answer is a small JSON document; the fields take their numbers straight out of it, and a field the answer lacks keeps the variable's last value and is noted once in the diagnostic buffer
- No key, no account: Open-Meteo's forecast is free for non-commercial use and asks for an attribution on the page that shows it; a commercial installation takes their subscription and carries the key in the same address

## What the station says
- **The glass.** Zeros with the sensor lamp dark and no condition icon mean no sensor and no forecast yet - the station is joining the network or waiting for its clock, or its WiFi settings are not yours. Values with the lamp dark are the web's outdoor values. Values with the lamp lit are the sensor's.
- **The diagnostic buffer** (the editor's Diagnostics page, or the device's console) says each change once: `web weather: ok (18 fields)` after the first good read, `web weather: failed - <reason>` when a read fails - the host the DNS does not know, no secure connection, an HTTP status, not the JSON expected - and `ok` again when it recovers; `STA '<name>' failed -> AP fallback` when the WiFi join failed.
- **The INFO line** of the device carries `wifi=1,<address>` once it is on your network, `web=1/1,<reads>,<failures>` once the forecast is in, `nvl=1/1` once the sensor is heard, `mqtt=1` once the broker took the connection.

## Pictures
- ![The Now screen on a dark portrait glass: the time and date, a partly cloudy icon, 12.4 °C outside, the sensor lamp green, humidity 68 % and pressure 1016.2 hPa with a steady arrow, and the four tabs at the bottom](img/meteo-now.webp) - Now
- ![The Forecast screen: today partly cloudy 14 and 6 degrees with 10 mm of rain, tomorrow rain 11 and 7 degrees with 80 mm, the day after sunny 15 and 4 degrees](img/meteo-forecast.webp) - Forecast: three days
- ![The Clock screen: a large clock with Sunday and the date, the autumn button, and the current weather with temperature, humidity and pressure](img/meteo-clock.webp) - Clock
- ![The net32 system in the editor: the sensor node 2 and the station node 1 on one line, each with out_t, out_h and out_p](img/meteo-system.webp) - Two devices, one net32 system
- ![The Web data page of the station in the editor: the source weather with its Open-Meteo address, the period of 1800 s, the status variable web_ok and the eighteen fields with their variables and paths](img/web-page.webp) - The station's web source in the editor

## Runs on
- The glass: Makerfabs MaTouch Lite ESP32-S3 3.95" (320×480 portrait)
- The sensor: an ESP32-C3-MINI-1 board with a BME280 at address 0x77 on I2C, SDA 7 / SCL 6
- Both on the same WiFi network with internet access for the forecast; an MQTT broker only if a home system should receive the values
- The forecast alone needs only the glass and a WiFi with internet - a phone's hotspot does

## Facts to keep exact
- Four screens on the station: Now, Forecast, Clock, Trend; tabs along the bottom
- Station = net32 node 1, sensor = net32 node 2, net32 over UDP on WiFi
- The sensor sends every 2 s; a value older than 10 s counts as stale and the web's value takes over
- The web source: Open-Meteo over https, every 30 minutes (1800 s), status variable `web_ok`, eighteen fields: the current temperature, humidity, sea-level pressure, wind, weather code and day/night, and per day the code, high, low and precipitation; the coordinates are in the address, the shipped project's are Banská Bystrica 48.7363 / 19.1462
- The secure read needs the clock: NTP on, `pool.ntp.org`, Central European time; the first read follows the time sync, about ten seconds after the start
- A failed read is retried after 30 s, 60 s, 2 min, up to the period; failure and recovery are said once in the diagnostic buffer
- The default forecast model is Open-Meteo's `best_match`; another model is `&models=<name>` at the end of the address
- Condition codes of the station: 1 sunny, 2 clear night, 3 partly cloudy, 4 cloudy, 5 fog, 6 rain, 7 thunderstorm, 8 snow, 9 wind, 0 unknown - mapped from the WMO codes by the program
- Pressure tendency: a sample every 30 minutes, compared with three hours back; ±1 hPa decides rising or falling
- The trends cover 12 hours with a sample every 30 seconds
- Colour schemes: night and autumn, a toggle on the Clock screen, retained
- The shipped project carries placeholder WiFi and broker settings; put in your network's name and password before deploying
- A station whose WiFi join fails raises its own access point and shows zeros: no sensor, no forecast

## Call to action
Download the ctrl32 editor and open the shipped project `examples\meteo_station.prj32`.
