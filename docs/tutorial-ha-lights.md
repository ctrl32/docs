# Lights and a dimmer from the glass

Two Zigbee lights switched — and one of them dimmed — from the touch
glass of an STM32F746 Discovery, through Home Assistant. The board
never speaks Zigbee: its switches and its slider are ordinary ctrl32
variables, MQTT discovery turns them into HA entities, and four small
HA automations bind those to the real lights.

| | Value |
|:---|:---|
| Board | STM32F746-DISCO (480×272 touch, ethernet) |
| Light 1 | a dimmable Zigbee bulb — switch + brightness slider |
| Light 2 | a wall relay light — on/off |
| Project file | `ha_lights_f7.prj32` |

The project is installed with the editor in `tutorials\`. The broker
route is the same as every HA connection —
[Home Assistant](home-assistant.md) covers it; the EVB
[thermostat tutorial](tutorial-ha-thermostat.md) is this page's
sibling, with the data flowing the other way.

---

## The design decision worth copying

Every card carries **two truths**: the switch is what you *ask*, the
lamp beside it is what Home Assistant *reports back* from the real
bulb. They are different variables on purpose (`light1_on` vs
`fb1_on`) — a drive gets the same treatment (controlword vs
statusword), and lights deserve no less. Turn the bulb off from a
phone and the lamp on the glass goes dark, while the switch still
shows what was last asked; the "any light on" lamp in the header sums
the ACTUAL states, not the wishes.

---

## What you create, step by step

### 1. Project and board

New project, board `ST 32F746GDISCOVERY`, 480×272. Ethernet with
DHCP runs by itself.

### 2. The variables

| Variable | Type | Who writes it | Why |
|:---|:---|:---|:---|
| `light1_on` | bool | the glass (and HA) | ceiling light command |
| `light1_dim` | f32 %, retentive | the glass (and HA) | brightness 1–100 |
| `light2_on` | bool | the glass (and HA) | wall light command |
| `fb1_on`, `fb2_on` | bool | **Home Assistant** | the REAL states, written back |
| `any_on` | bool | the ladder | header lamp — from the actuals |
| `all_off` | bool | the glass | one button clears both commands |

### 3. MQTT

```yaml
mqtt:
  broker: 192.168.0.53
  username: ctrl32
  password: ctrl32mqtt
  client_id: ctrl32-f7lights
  topic: ctrl32/f7lights
  publish_mode: per_tag
  discovery: true
  interval_ms: 1000
  tags:
    - { name: light1_on,  write: true }
    - { name: light1_dim, write: true }
    - { name: light2_on,  write: true }
    - { name: fb1_on,     write: true }
    - { name: fb2_on,     write: true }
    - any_on
```

The commands carry **write** so HA's automations *and* anybody in the
HA UI can flip them — the glass and the phone stay in step because
they move the same variable. `any_on` is read-only: a binary sensor.

### 4. The ladder

Three rungs:

1. **Heartbeat** — 1 Hz BLINK.
2. **`any_on`** — OR over `fb1_on`, `fb2_on`: the summary lamp counts
   what is actually lit.
3. **All off** — R_TRIG on the button, then a SEL per command writing
   `false`. One press, both commands cleared; the automations do the
   switching-off.

### 5. The screen

One landscape screen, two cards. Each card: a name, a bulb icon, the
**actual-state lamp** (a `state:` colour set — yellow when lit), the
command switch; the ceiling card adds the brightness slider with its
percentage. The footer holds the All-off button. Nothing here is
special — every element is on the [widgets](widgets.md) pages.

### 6. Download

Over the network or USB — F5. Within seconds HA shows
**ctrl32-f7lights** with six entities.

---

## The Home Assistant half

Four automations — two per light, command and feedback. Replace the
`light.…` entity ids with your own.

**Ceiling command** — the switch or the slider changed, so drive the
bulb (brightness comes along on every change):

```yaml
alias: ctrl32 F7 lights - ceiling command
trigger:
  - platform: state
    entity_id: switch.ctrl32_f7lights_light1_on
  - platform: state
    entity_id: number.ctrl32_f7lights_light1_dim
action:
  - choose:
      - conditions:
          - condition: state
            entity_id: switch.ctrl32_f7lights_light1_on
            state: "on"
        sequence:
          - service: light.turn_on
            target:
              entity_id: light.your_dimmable_bulb
            data:
              brightness_pct: >-
                {{ states('number.ctrl32_f7lights_light1_dim') | int }}
    default:
      - service: light.turn_off
        target:
          entity_id: light.your_dimmable_bulb
mode: restart
```

**Ceiling feedback** — whatever the bulb really does lands back on
the glass:

```yaml
alias: ctrl32 F7 lights - ceiling actual state
trigger:
  - platform: state
    entity_id: light.your_dimmable_bulb
action:
  - choose:
      - conditions:
          - condition: state
            entity_id: light.your_dimmable_bulb
            state: "on"
        sequence:
          - service: switch.turn_on
            target:
              entity_id: switch.ctrl32_f7lights_fb1_on
    default:
      - service: switch.turn_off
        target:
          entity_id: switch.ctrl32_f7lights_fb1_on
mode: restart
```

The wall light gets the same pair without the brightness line.

---

## Proving it

- Flip the ceiling switch on the glass: the bulb lights at the
  slider's percentage, the card's lamp follows a beat later — that
  beat is the round trip through the broker and back.
- Drag the slider: the bulb dims live.
- Turn the bulb off **from the phone**: the lamp on the glass goes
  dark, the header lamp with it.
- Press **All off** with both lights on: one press, both really off.

## When it does not work

| Symptom | Look at |
|:---|:---|
| no device in HA | boot log `mqtt:` lines; broker, credentials, discovery on |
| switch flips but the bulb ignores it | the command automation's entity id; try the bulb from HA directly |
| bulb changes, the lamp does not | the feedback automation; the lamp watches `fb1_on`, never the command |
| everything lags seconds | the broker host's load; MQTT itself is milliseconds |
