# Home Assistant

A ctrl32 board appears in Home Assistant as a device with all its values
underneath — sensors, switches, numbers — and it does so **by itself**.
No YAML to write, no integration to install beyond MQTT.

This page is the route from nothing to working entities. The mechanics
underneath are on the [MQTT](mqtt.md) page.

---

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
    shared home network. See [Network and security](security.md).

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

An MQTT client such as MQTT Explorer, pointed at the broker, settles most
of these in a minute: you see the topics, the values and the retained
configuration exactly as the board sent them.

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
are plain and documented on the [MQTT](mqtt.md) page.
