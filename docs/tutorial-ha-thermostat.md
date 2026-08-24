# A thermostat fed by Home Assistant

A wall thermostat on the Olimex ESP32-EVB with its 2.8" glass — with
one twist: the room temperature does not come from a wire, it comes
from **Home Assistant**, read off a Zigbee sensor somewhere in the
house. The board's own relay switches the heating; two small HA
automations feed it the temperature and a heartbeat; a ladder
watchdog decides how much to trust them.

| | Value |
|:---|:---|
| Board | Olimex ESP32-EVB + MOD-LCD2.8RTP (240×320, portrait) |
| Heating | the board's relay 1 (REL1) |
| Temperature | a Zigbee sensor, through Home Assistant and MQTT |
| Project file | `ha_thermostat_evb.yaml` |

The project is installed with the editor in `tutorials\` — open it
while reading. The general route of connecting a board to HA (broker,
discovery, what a variable becomes) is on
[Home Assistant](home-assistant.md); this page builds a complete
working system on top of it.

---

## The design decision worth copying

The temperature arrives over WiFi, ethernet, a broker and a radio —
any link in that chain can die silently. So the board never trusts it
blindly: **remote data gets a watchdog**. Home Assistant toggles a
`ha_beat` variable once a minute; the ladder counts the silence, and
three minutes without a beat means the heating goes OFF, a banner
appears on the glass and an alarm lands in the table. Manual mode
keeps working without HA on purpose — the person standing at the
equipment outranks the network.

The same shape protects drive positioning against stale encoder data
— it is a doctrine, not a trick for this page.

---

## What you create, step by step

### 1. Project and board

New project, board `Olimex ESP32-EVB`, resolution 240×320 portrait.
Ethernet needs no configuration — the board's catalog starts the
LAN8710 with DHCP by itself.

### 2. WEBview off — deliberately

```yaml
webview:
  enabled: false
```

### 3. The variables

| Variable | Type | Who writes it | Why |
|:---|:---|:---|:---|
| `ha_temp` | f32 °C | **Home Assistant** | the Zigbee reading |
| `ha_beat` | bool | **Home Assistant** | the heartbeat, toggled every minute |
| `ha_ok` | bool | the ladder | the watchdog verdict |
| `temp_sp` | f32 °C, retentive | the glass (and HA) | setpoint, survives power loss |
| `auto_mode` | bool, retentive | the glass (and HA) | Auto / Manual |
| `rel1` | bool, GPIO 32 | the ladder | the real heating relay |
| `rel1_cmd` | bool | the glass | manual heat request |

### 4. MQTT

Broker = the machine running Mosquitto (the HA add-on), one topic per
variable, discovery on:

```yaml
mqtt:
  broker: 192.168.0.53
  username: ctrl32
  password: ctrl32mqtt
  client_id: ctrl32-evbtherm
  topic: ctrl32/evbtherm
  publish_mode: per_tag
  discovery: true
  interval_ms: 2000
  tags:
    - { name: ha_temp,   write: true }
    - { name: ha_beat,   write: true }
    - { name: temp_sp,   write: true }
    - { name: auto_mode, write: true }
    - rel1
    - ha_ok
```

**write** is the permission: only these four may be changed from the
broker side. `rel1` and `ha_ok` are read-only sensors in HA — the
outside world watches the relay, it never drives it.

### 5. The ladder

Five things, one rung each (open the project to see them drawn):

1. **Heartbeat** — a 1 Hz BLINK for the lamp in the corner.
2. **The watchdog** — R_TRIG + F_TRIG on `ha_beat` make one pulse per
   edge; the pulse feeds a TOF with PT = 180 000 ms. Its Q is
   `ha_ok`: any beat restarts the three minutes.
3. **Hysteresis comparator** — HYST on `ha_temp` around `temp_sp`
   (0.5 °C band). A bare comparison would chatter the relay.
4. **The relay rung** — `(auto AND cold AND ha_ok) OR (manual AND
   command)` into the `rel1` coil. Note where `ha_ok` sits: it gates
   only the automatic branch.
5. **The setpoint spinner** — R_TRIG per button press, SEL chain,
   LIMIT 15–30 °C clamped last.

### 6. The screens

Three portrait screens: the dial (two nested arcs — blue room
temperature, orange setpoint), Manual, and a two-curve Trend
(`ha_temp` + `temp_sp`). The watchdog banner is one label with
`visible_if: n_haok` — drawn only while HA is silent, exactly like
the [states and motion](states-motion.md) page describes.

### 7. Download

F5 over USB. The boot log prints the MQTT connection, and within
seconds Home Assistant shows a new device **ctrl32-evbtherm** with
six entities.

---

## The Home Assistant half

Two automations — create them in HA (Settings → Automations, or paste
into `automations.yaml`). First the temperature: every change of the
Zigbee sensor (and every 5 minutes as a refresh) is written into the
board's `ha_temp` number entity:

```yaml
alias: ctrl32 EVB thermostat - temperature from Zigbee
trigger:
  - platform: state
    entity_id: sensor.tuya_teplota      # your sensor's entity id
  - platform: time_pattern
    minutes: "/5"
condition:
  - condition: numeric_state
    entity_id: sensor.tuya_teplota
    above: -40
    below: 80
action:
  - service: number.set_value
    target:
      entity_id: number.ctrl32_evbtherm_ha_temp
    data:
      value: "{{ states('sensor.tuya_teplota') | float }}"
mode: single
```

The condition matters: a battery Zigbee sensor reports `unavailable`
while it sleeps, and writing that into a number would fail — the
guard lets only a sane reading through.

Then the heartbeat — the whole automation is one toggle:

```yaml
alias: ctrl32 EVB thermostat - heartbeat
trigger:
  - platform: time_pattern
    minutes: "/1"
action:
  - service: switch.toggle
    target:
      entity_id: switch.ctrl32_evbtherm_ha_beat
mode: single
```

---

## Proving it

- Watch the dial follow the sensor; hold the sensor in your hand and
  the number climbs.
- **Kill the beat** (disable the heartbeat automation): after three
  minutes the banner appears, the alarm fires, the relay drops —
  and Manual still heats.
- Change the setpoint **from HA** (the `temp_sp` number): the dial's
  orange arc moves on the glass. The setpoint is retentive — pull
  the plug, it comes back.

## When it does not work

| Symptom | Look at |
|:---|:---|
| no device in HA | the boot log's `mqtt:` lines — broker address, credentials; discovery must be **on** |
| entities exist, temperature never moves | the automation's sensor entity id, and whether the sensor is `unavailable` |
| heating never starts in Auto | `ha_ok` — no heartbeat automation, or HA down; the banner says so |
