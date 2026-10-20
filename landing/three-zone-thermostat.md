---
title: Hot tank, three zones
source: docs/three-zone-thermostat.md
hero: img/thermostat-home.png
---

# A complete three-zone hot tank: touch panel, phone view and SCADA reporting - no router needed

One board at the tank measures three PT100 probes and switches three SSR heaters; a touch panel operates it, a phone mirrors it, and an MQTT uplink reports the whole tank to a SCADA anywhere in the world. Every screen, mode, setting, protection and the measured cost are documented.

## Who it is for
- Builders of heated baths and tanks in cosmetics production (creams, emulsions, oils) and similar process heating
- Integrators who need a field board and an operator panel that keep working without plant infrastructure
- SCADA integrators who want a clean Modbus TCP map and MQTT topics

## What you get
- **The process board owns its outputs**: the panel asks, the zone board decides with its own interlocks, thermostat and link watchdog; if the panel disappears the process side fails to a safe state on its own
- Its own WiFi: the zone board raises an access point, the panel joins it; at the same time the same radio joins the plant WiFi for MQTT (`mode: apsta`) - unplug the plant network and everything keeps running
- Two heartbeats: the panel's Link lamp blinks with the zone board; **three seconds of panel silence drop every heater**, and normal operation resumes by itself
- Five thermostat variables per zone, all offsets from the setpoint - move the setpoint and the whole set of lines moves with it
- AUTO (on/off thermostat across a band, nothing to tune) and MANUAL (command switches visible only in MANUAL, behind the access code)
- Three gates no mode can override: probe interlock, link watchdog, and an alarm engine that only reports
- Four pages - Home, Trend, Alarms, Setup - with a red connection banner; an access code with a five-minute auto-lock
- The full visualization in a phone browser, laid out for a phone, same states and protections
- SCADA over MQTT: twenty variables, published only on change, writes via `/set` honoured only where the project allows
- Measured: the uplink, MQTT and SCADA load cost no overruns - the degradation rule *logic > communication > graphics* measured rather than promised

## How it works
1. Download the zone board first over USB - it carries the AP configuration; the `ctrl32-zones` network goes on the air.
2. Download the panel; it joins the network and the temperatures appear within seconds.
3. With defaults each zone holds 15-25 °C; set the real setpoints on Home, bands and alarm offsets on Settings (behind the code).
4. Prove the protections: pull a probe (its zone drops out, *sensor fault* appears); power the panel off (heaters drop within 3 seconds and return with the panel).
5. Connect a SCADA over MQTT or Modbus TCP using the published topics and register map.

## Pictures
- ![The Home page in AUTO: three zone cards with the large current temperature, the small editable setpoint, the AUTO badge and the output lamp; zone B is heating](img/thermostat-home.png) - Home in AUTO
- ![The Home page in MANUAL: the toggle switches replace the AUTO badges; zone B is commanded on and its output lamp confirms it](img/thermostat-home-manual.png) - Home in MANUAL
- ![The Home page with the link down: the red banner with the yellow exclamation mark, the Link lamp frozen, every output off](img/thermostat-home-linkdown.png) - the link-down banner
- ![The Trend page: one mini chart per zone, each plotting the current temperature and the setpoint over eight hours](img/thermostat-trend.png) - eight-hour trends per zone
- ![The Alarms page: the alarm table with an active high-limit alarm on zone A](img/thermostat-alarms.png) - the alarm table
- ![The access-code page: the code field on the left, the phone connection details on the right](img/thermostat-login.png) - the access-code page with phone connection details
- ![The access-code page after the right code: the Open settings button has appeared](img/thermostat-login-open.png) - the way in after the right code
- ![The Settings page: the five thermostat variables as a grid of three zone columns, and the mode switch below](img/thermostat-settings.png) - the protected Settings grid
- ![The mobile Home page in AUTO: stacked zone cards with the current temperature, the setpoint field, the AUTO badge and the output lamp](img/thermostat-web-home.png) - phone Home in AUTO
- ![The mobile Home page in MANUAL: the command switches replace the AUTO badges; zone B is commanded on](img/thermostat-web-home-manual.png) - phone Home in MANUAL
- ![The mobile Trend page: three stacked charts, one per zone](img/thermostat-web-trend.png) - phone Trend
- ![The mobile Alarms page with an active high-limit alarm on zone A](img/thermostat-web-alarms.png) - phone Alarms
- ![The mobile access-code page: the code field, no way in](img/thermostat-web-login.png) - phone access code, locked
- ![The mobile access-code page after the right code: the Open settings button has appeared](img/thermostat-web-login-open.png) - phone access code, unlocked
- ![The mobile Settings page: the five variables per zone stacked, and the Manual mode switch](img/thermostat-web-settings.png) - phone Settings

## Runs on
- At the tank: **inoCORE32-TM8.6** - ESP32-PICO-V3-02, 2x 240 MHz, 8 MB flash, 2 MB PSRAM, no display (WEBview to a phone), 3x MAX31865 (PT100), 3x SSR 240 V/16 A, WiFi (AP + uplink), CAN, RS485, SPI - `tm8_6_wifi_zones.prj32`
- At the operator: **stepHMI32.4** - ESP32-S3, 2x 240 MHz, 16 MB flash, 8 MB PSRAM, 4,3" 480x272 SSD1963 capacitive touch, WiFi, CAN, RS485 - `stephmi_wifi_panel.prj32`
- Links: Modbus TCP between the boards, MQTT to SCADA, WEBview to phones

## Facts to keep exact
- Projects installed in `examples\wifi_pair`
- The zone board raises AP `ctrl32-zones`; the AP side is always **192.168.4.1** (why the process board hosts); the panel polls ten times a second and writes settings and commands the moment they change
- Zone board `beat` blinks twice a second; panel `panel_beat` retriggers a 3-second watchdog; commands, mode and settings survive the outage
- Thermostat variables (whole degrees) and defaults: Setpoint 20 °C, Band+ 5 (heat OFF at setpoint + Band+), Band− 5 (heat ON at setpoint − Band−), Alarm+ 20, Alarm− 10; with defaults: 40 °C high alarm, 25 °C heat OFF, 20 °C set, 15 °C heat ON, 10 °C low alarm; the alarm lines sit outside the band on purpose
- Fifteen variables (five per zone) on the protected Settings page; the setpoint also editable on Home; all persisted on the zone board
- Probe interlock: a sensor reading below 2 °C (loose or shorted PT100) refuses to heat; the watchdog drops manual commands too; the alarm engine never switches anything
- Pages in fixed order: Home, Trend, Alarms, Setup; banner text *TM8.6 not connected* with a yellow **!**
- Trend: two curves per zone (current + setpoint), 8 hours, one sample per minute (480 samples per curve), in panel RAM (restart starts afresh)
- Alarms: *over alarm limit* (warning, 2 s), *under alarm limit* (warning, 2 s), *sensor fault* (fault, below 2 °C, 3 s), *Display link lost — heating off* (fault, zone board, 1 s), *Link to zones lost — heating is off* (fault, panel, 1 s); limit alarms clear when back inside, sensor fault clears when the probe reads sanely
- Access code fixed in the program, as delivered `1234`; changing it = edit the comparison in the block named `gate` in `stephmi_wifi_panel.prj32` and download; auto-lock after five minutes; a wrong entry does nothing
- Settings ranges: Setpoint 0-90, Band+ / Band− 1-30, Alarm+ / Alarm− 1-40, Manual mode on/off; out-of-range values refused at the keypad (not clamped); persisted immediately, throttled
- Phone: `http://zones.local` (= 192.168.4.1, the zone board - works even with the panel down), `http://farmol.local` (= 192.168.4.2, the panel's full visualization); mDNS names, raw addresses as fallback; all printed on the access-code page; the WiFi password is printed there too; the pair's network does not reach the internet
- Phone page bar: a two-by-two grid; with two editors at once the last write wins and both pages show it within a second
- MQTT: twenty variables under `ctrl32/hottank/`, per-variable topics, at most once a second, only on change; topics `temp_a/b/c`, `sp_a/b/c` (writable), `mode_man`, `cmd_a/b/c` (writable), `heat_a/b/c`, `trip_hi_*`, `trip_lo_*`, `link_ok`, `status` (`online` + a broker-kept last will); writes to `<topic>/set` (e.g. `20` to `ctrl32/hottank/sp_a/set`); the board republishes the accepted value
- The bench measurements used a public broker on purpose; production keeps the broker on its own network (MQTT credentials travel in plain text)
- Measured 10 ms cycle (current / min / max µs, overruns, heap low mark): pair only 93 / 77 / 164, 0, 2 120 kB; + uplink + MQTT quiet 109 / 77 / 449, 0, 2 102 kB; + SCADA 4 writes/s + full echo for 60 s (240 commands, 341 messages) 108 / 77 / 449, 0, 2 102 kB; uplink costs ~16 µs average (0.16 % of the period) and ~18 kB once; panel 38 / 19 / 60 µs throughout
- Power loss: setpoints, bands, alarm offsets and AUTO/MANUAL mode survive; manual commands, panel alarm history and trend history do not; the panel reads first on boot, never pushes
- Modbus TCP map on `192.168.4.1:502`, unit 1, word order big: temp_a/b/c holding 0-1, 2-3, 4-5 (f32, read); sp_a/b/c holding 6/7/8 (40007…), band_hi 9/10/11, band_lo 12/13/14, alarm_hi 15/16/17, alarm_lo 18/19/20 (read/write); coils 0/1/2 cmd (rw), 3/4/5 heat (read), 6 beat (read), 7 panel_beat (rw), 8/9/10 trip_hi, 11/12/13 trip_lo (read), 14 link_ok (read), 15 mode_man (rw, 1 = manual); non-writable writes refused with a Modbus exception

## Call to action
Download the editor and open `tm8_6_wifi_zones.prj32` and `stephmi_wifi_panel.prj32` from `examples\wifi_pair`.
