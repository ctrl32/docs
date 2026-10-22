---
title: "Home Assistant"
slug: home-assistant
section: "Protocols"
order: 308
sidebar_position: 308
generator: tools/docs_export.py
---

# Home Assistant

A ctrl32 board appears in Home Assistant as a device with all its values
underneath — sensors, switches, numbers — and it does so **by itself**.
No YAML to write, no integration to install beyond MQTT.

This page is the route from nothing to working entities. The mechanics
underneath are on the [MQTT](/docs/buses/mqtt/) page.

---

![The MQTT page - per-variable topics for Home Assistant](img/mqtt-card.webp){: .sb-center}

## What you need

1. **Home Assistant** with the **MQTT integration** set up.
2. **An MQTT broker** — usually the Mosquitto add-on in HA itself.
3. **A ctrl32 board on the same network**, with ethernet or WiFi.

If you already run anything over MQTT in HA, you have all three.

---

## The route, start to finish

### 1. Give the board a network

In the editor, under the board's network settings: ethernet with DHCP,
or WiFi with the network name and password. The boot log prints the
address it got.

### 2. Point it at the broker

In the project's MQTT settings:

| Field | What to put |
|:---|:---|
| Broker address | the IP of the computer running Mosquitto |
| Port | 1883 |
| User / password | if the broker asks for them |
| Base topic | something that names this board — `ctrl32/boilerroom` |
| Publish mode | **one topic per variable** |
| Discovery | **on** |

The base topic is worth thinking about for ten seconds: it is how you
will recognise this board among others, and changing it later means the
entities in HA are recreated under new names.

*One topic per variable* is one of two publish modes: the other, *one
JSON object*, packs every value into a single message the way
ThingsBoard-style platforms expect. Home Assistant needs the
per-variable mode — discovery and retained values are built on it.

!!! warning "MQTT is not encrypted"
    The connection to the broker, the password included, travels in
    plain text. That is fine on the separate network the board belongs
    on anyway — and worth remembering before putting a board on a
    shared home network. See [Network and security](/docs/about/security/).

### 3. Choose which variables go out

Every variable has a **publish** checkbox, and a separate **write**
checkbox beside it.

Publish what somebody would want to see. Not everything — a hundred
entities in HA is a hundred entities to scroll past, and the internal
working variables of your logic help nobody.

**Write** can only be ticked on a variable that is `rw` in the project,
and it decides what HA is allowed to change. Without it, a write from
the broker is ignored — so the project decides what the outside world
may touch, not the outside world.

### 4. Download and watch it appear

Download the project. On connect, the board tells the broker about every
entity, and HA creates them.

Within seconds you should see a device in HA named after your board, with
the variables underneath it.

---

## What each variable becomes

| The variable is | In Home Assistant |
|:---|:---:|
| numeric, read-only | **sensor**, with its unit |
| boolean, read-only | **binary sensor** |
| numeric, writable | **number** — a box or a slider |
| boolean, writable | **switch** |

Units, decimals and names come from the **variable definition**, so an
entity is labelled the way you labelled it in the project. Fix a unit in
the editor and HA follows on the next download.

---

## When it does not appear

| Symptom | Look at |
|:---|:---|
| nothing at all in HA | is the board connected? The boot log says so, and `<base>/status` should read `online` |
| the device appears but has no entities | Discovery is probably off — turn it on and download again |
| entities are there but greyed out | the board is `offline` — the broker has not heard from it |
| a value never updates | is that variable's **publish** ticked? |
| HA cannot change a value | the **write** checkbox, and the variable must be `rw` |
| `mqtt: skipped (memory tier…)` in the boot log | a classic ESP32 without PSRAM with WEBview on — see *Memory on a classic ESP32* below |
| an automation runs, the board's value never moves | the entity id in the automation, and whether the source entity is `unavailable` |
| a command flips, the real device ignores it | the command automation's target; try the device from HA directly |
| the device changes, the lamp on the glass does not | the feedback automation — the lamp watches the feedback variable, never the command |

An MQTT client such as MQTT Explorer, pointed at the broker, settles most
of these in a minute: you see the topics, the values and the retained
configuration exactly as the board sent them.

---

## Memory on a classic ESP32

A classic ESP32 without PSRAM cannot hold the WEBview server and the
MQTT client in its internal RAM together: the memory tiers skip MQTT
at start-up and the boot log says `mqtt: skipped (memory tier…)`.
When Home Assistant is the remote view anyway, untick **WEBview on**
on the WEBview page and the server's memory pays for the MQTT client.
Boards with PSRAM run both.

---

## Feeding the board from Home Assistant

The board's writable variables are `number` and `switch` entities, so
anything Home Assistant knows — a radio sensor, a light's real state,
the time of day — reaches the board through an ordinary automation
(Settings › Automations, or `automations.yaml`). Copy the exact entity
ids from the board's device in Home Assistant; they are built from
the board's name and the variable's name.

**A value into a number.** Every change of the source, plus a refresh
every few minutes, written into the board — with a guard, because a
battery sensor reports `unavailable` while it sleeps and writing that
into a number fails:

```yaml
alias: <board> - <value> from <source>
trigger:
  - platform: state
    entity_id: sensor.<source>
  - platform: time_pattern
    minutes: "/5"
condition:
  - condition: numeric_state
    entity_id: sensor.<source>
    above: -40          # the range a sane reading lies in
    below: 80
action:
  - service: number.set_value
    target:
      entity_id: number.<board>_<variable>
    data:
      value: "{{ states('sensor.<source>') | float }}"
mode: single
```

**A heartbeat.** One toggle a minute on a `bool` variable with
**write** ticked — the board's watchdog (below) listens for it:

```yaml
alias: <board> - heartbeat
trigger:
  - platform: time_pattern
    minutes: "/1"
action:
  - service: switch.toggle
    target:
      entity_id: switch.<board>_<beat variable>
mode: single
```

**A command and its feedback.** To drive something Home Assistant owns
(a light, a plug) from the glass, use **two variables**: the command
the glass sets, and the feedback Home Assistant writes back from the
real device. Two automations per device — the command one drives it:

```yaml
alias: <board> - <device> command
trigger:
  - platform: state
    entity_id: switch.<board>_<command variable>
action:
  - choose:
      - conditions:
          - condition: state
            entity_id: switch.<board>_<command variable>
            state: "on"
        sequence:
          - service: light.turn_on
            target:
              entity_id: light.<device>
    default:
      - service: light.turn_off
        target:
          entity_id: light.<device>
mode: restart
```

— and the feedback one reports what the device really does:

```yaml
alias: <board> - <device> actual state
trigger:
  - platform: state
    entity_id: light.<device>
action:
  - choose:
      - conditions:
          - condition: state
            entity_id: light.<device>
            state: "on"
        sequence:
          - service: switch.turn_on
            target:
              entity_id: switch.<board>_<feedback variable>
    default:
      - service: switch.turn_off
        target:
          entity_id: switch.<board>_<feedback variable>
mode: restart
```

A dimmer adds a second trigger on its `number` entity and
`brightness_pct: "{{ states('number.<board>_<level variable>') | int }}"`
under `data:` of `light.turn_on`. The glass then shows what was
**asked** (the switch) and what **is** (the lamp beside it); turn the
light off from a phone and the lamp goes dark while the switch still
shows the last request. A summary lamp ("any light on") is built from
the feedback variables, never from the commands.

### What gets the write checkbox

| Variable | write | Why |
|:---|:---:|:---|
| a value Home Assistant feeds in (a reading, a heartbeat, a feedback) | yes | Home Assistant writes it |
| a setpoint or a mode the person may also change from Home Assistant | yes | both sides move the same variable, so they stay in step |
| a physical output (a relay), a verdict the logic computes | no | the outside world watches it, never drives it |

### A watchdog on remote data

A value that arrives over WiFi, a broker and a radio can stop without
a word — it simply stays at its last number. Logic that acts on it
gets a watchdog:

1. an `R_TRIG` and an `F_TRIG` on the heartbeat variable make one
   pulse per edge;
2. the pulse feeds a `TOF` with `PT` of three heartbeats (three
   minutes for a one-minute beat); its `Q` is the verdict "the remote
   data is fresh";
3. the verdict gates only the **automatic** branch of the logic — the
   output goes to its safe state, a banner (`visible_if` on the
   inverted verdict) and an alarm say why, and manual operation from
   the glass keeps working without the network.

Compare a remote reading with a hysteresis comparator (`HYST`), not a
bare comparison — a value that wanders around the setpoint would
chatter an output.

---

## Two things that make it behave properly

**Values are retained.** The broker keeps the last one, so HA gets a
value the moment it subscribes rather than waiting for the board to
publish a change. After an HA restart the dashboard is populated
immediately.

**There is a last will.** If the board drops off — power, network,
anything — the *broker* publishes `offline` on its behalf and the
entities grey out. Without that, HA would keep showing the last known
value as though it were current, which is worse than showing nothing.

Both are on automatically. They are mentioned because they are the
difference between a dashboard you can trust and one you cannot.

---

## If you would rather write the YAML

Turn Discovery off and use **Export YAML for Home Assistant** in the
editor. It produces one entity per published variable, ready to paste
into `configuration.yaml` or pull in with `!include`.

Worth doing when you keep your HA configuration in version control, or
when you want to customise entities beyond what the board knows about —
icons, device classes, areas.

The ranges on `number` entities in the export are deliberately wide;
narrow them in HA to what the program actually accepts.

---

## The board does not depend on Home Assistant

The logic, the timers, the screens and the local buttons keep running
with HA switched off, the network unplugged and the broker gone. MQTT is
a window, never a dependency.

That is worth knowing before building a dashboard: what you are looking
at is a **view of** something that runs on its own, not the thing itself.

!!! warning "Do not build control that needs the broker"
    A switch in HA is convenient. An installation that only starts when
    somebody's home server is up is not. Anything that must work should
    work from the board — HA is how you watch it and how you nudge it,
    not how it runs.

---

## Beyond Home Assistant

The same one-topic-per-variable mode works with anything that speaks MQTT —
Node-RED, ThingsBoard, OpenRemote, Grafana through a bridge, or your own
script. Discovery is a Home Assistant convention; the topics underneath
are plain and documented on the [MQTT](/docs/buses/mqtt/) page.
