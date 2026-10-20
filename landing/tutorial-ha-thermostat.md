---
title: Home Assistant thermostat
source: docs/tutorial-ha-thermostat.md
hero: img/ha-therm-glass.webp
---

# A wall thermostat that uses Home Assistant's sensors - and never trusts them blindly

The room temperature comes from a Zigbee sensor through Home Assistant and MQTT; the board's own relay switches the heating, and a ladder watchdog decides how much to trust the network.

## Who it is for
- Home Assistant users who want heating control that keeps its own reflexes
- Makers with a Zigbee temperature sensor and an ESP32 board with a relay
- Anyone who needs to feed remote data into a controller safely

## What you get
- A complete working thermostat on a 2.8" touch glass, three portrait screens: the dial, Manual, and a two-curve Trend
- MQTT with discovery: the board appears in Home Assistant as a device with six entities - no YAML on the board side
- The design worth copying: **remote data gets a watchdog** - Home Assistant toggles a heartbeat once a minute; three minutes of silence switch the heating OFF, show a banner on the glass and raise an alarm
- Manual mode keeps working without Home Assistant on purpose - the person standing at the equipment outranks the network
- Write permission per variable: only four values may be changed from the broker; the relay and the watchdog verdict are read-only sensors in HA
- A retentive setpoint and Auto/Manual mode that survive power loss
- Hysteresis control (0.5 °C band) so the relay never chatters
- Two ready Home Assistant automations: temperature from Zigbee, and the heartbeat

## How it works
1. New project on the Olimex ESP32-EVB, 240x320 portrait; Ethernet starts with DHCP by itself.
2. Untick WEBview - on this board without PSRAM its memory goes to the MQTT client; the remote view **is** Home Assistant.
3. Create the variables and turn on MQTT with discovery, marking the four writable ones.
4. Draw five ladder rungs: heartbeat lamp, the watchdog, the hysteresis comparator, the relay rung, the setpoint spinner.
5. Draw the three screens and download over USB (F5); Home Assistant shows the new device within seconds.
6. Add the two Home Assistant automations and prove it: kill the heartbeat and watch the heating drop after three minutes while Manual still heats.

## Pictures
- ![The dial: the room temperature that came over MQTT, the setpoint, and the green lamp that says Home Assistant is still talking](img/ha-therm-glass.webp) - the thermostat dial on the glass
- ![Manual control: the heat runs from the glass while Auto is off, and needs nothing from the network](img/ha-therm-manual.webp) - manual control without the network
- ![The MQTT page: broker, mode and the variable list](img/mqtt-card.webp) - the MQTT page in the editor

## Runs on
- Olimex ESP32-EVB + MOD-LCD2.8RTP (240x320, portrait), heating on the board's relay 1 (REL1)
- Ethernet (LAN8710, DHCP), MQTT broker (Mosquitto, the HA add-on)
- Home Assistant with a Zigbee temperature sensor

## Facts to keep exact
- Project file `ha_thermostat_evb.prj32`, installed in `tutorials\`
- WEBview off (`webview: enabled: false`): the board has no PSRAM, the HTTP/WS server and the MQTT client do not fit its internal RAM together; with WEBview on, the boot log says `mqtt: skipped (memory tier…)`
- Variables: `ha_temp` (f32 °C, written by HA), `ha_beat` (bool, HA heartbeat toggled every minute), `ha_ok` (bool, watchdog verdict), `temp_sp` (f32 °C, retentive), `auto_mode` (bool, retentive), `rel1` (bool, GPIO 32, the real relay), `rel1_cmd` (bool, manual heat request)
- MQTT: client id `ctrl32-evbtherm`, topic `ctrl32/evbtherm`, `publish_mode: per_tag`, discovery on, `interval_ms: 2000`; writable: `ha_temp`, `ha_beat`, `temp_sp`, `auto_mode`; read-only: `rel1`, `ha_ok`
- Ladder: 1 Hz BLINK heartbeat; watchdog = R_TRIG + F_TRIG on `ha_beat` feeding a TOF with PT = 180 000 ms (its Q is `ha_ok`); HYST on `ha_temp` around `temp_sp` with a 0.5 °C band; relay rung `(auto AND cold AND ha_ok) OR (manual AND command)` into `rel1` - `ha_ok` gates only the automatic branch; setpoint spinner = R_TRIG per press, SEL chain, LIMIT 15-30 °C clamped last
- Watchdog banner: one label with `visible_if: n_haok`
- Dial: two nested arcs - blue room temperature, orange setpoint
- HA automation 1: on every sensor change and every 5 minutes, write the sensor to `number.ctrl32_evbtherm_ha_temp`, guarded by a numeric condition above -40 and below 80 (a sleeping battery sensor reports `unavailable`)
- HA automation 2: every minute toggle `switch.ctrl32_evbtherm_ha_beat`
- The same watchdog shape protects drive positioning against stale encoder data - a doctrine, not a trick

## Call to action
Download the editor and open `tutorials\ha_thermostat_evb.prj32`.
