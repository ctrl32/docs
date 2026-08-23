# MQTT telemetry in ctrl32

> **Home Assistant?** There is a page for that: [Home Assistant](home-assistant.md)
> takes you from nothing to working entities. What follows here is the
> mechanics underneath — start with that page unless you want them.
>
> The section on this page: [Home Assistant mode](#home-assistant-mode-one-topic-per-variable)
> — in that mode the board acts as a process data server (an OPC equivalent).

The board can push variable values to an **MQTT broker** — typically into
ThingsBoard or OpenRemote, where the customer builds charts, dashboards
and notifications. The board is a data source (gateway role), not a
historian: it sends the current state, the server keeps the history.

## How to switch it on

1. In the device tree, double-click the **MQTT** node (or right-click →
   *MQTT settings…*).
2. Tick *Publish telemetry to broker* and fill in the broker address
   and credentials.
3. In the variable list, tick the variables that should be sent.
4. *Apply* → *Download to board*. The configuration is part of the pack —
   changing the broker or the variable list **does not require new firmware**.

MQTT settings are part of the **FULL** level (same as CAN and Modbus).

| Field | Meaning |
|:---|:---|
| broker | IP address or hostname (e.g. `192.168.0.10`) |
| port | 1883 (plain MQTT, no encryption) |
| username / token | in ThingsBoard this is the **device access token** |
| password | for a generic broker; ThingsBoard does not need it |
| topic | base topic; default `v1/devices/me/telemetry` |
| interval | how often a message may be sent at most (default 5 s, min 1 s) |
| setTag commands | allows writes from the dashboard (see below) |

## What the board sends

A flat JSON containing **only the values that changed** since the last
message goes out on the base topic:

```json
{"voltage_l1": 231.4, "contactor": true, "pieces": 1250}
```

- If nothing changed, **nothing is sent** — no pointless traffic.
- After connecting (including after an outage) the complete state is
  sent once, so the dashboard has everything.
- Decimal places follow the variable settings; `bool` goes out as
  `true`/`false`.
- The variable deadband filters noise — without it a noisy analog input
  would send messages forever.

## Commands from the dashboard (setTag)

If commands are enabled, the board listens on the ThingsBoard RPC topic
and accepts:

```json
{"method":"setTag","params":{"pieces":0}}
```

A write is a **command, not direct memory access** — the board executes
it only if the variable is among the published ones and has **rw** access.
Otherwise it answers with an error and writes nothing. The reply goes to
the topic `.../rpc/response/<id>`.

> Never use remote commands for safety functions. E-stop, limit
> switches and doors must be hard-wired.

## Security and limits

- **No TLS.** Encryption is not enabled on the ESP32-S3 (it does not
  fit into RAM alongside control and graphics). The broker must live on
  the **separate equipment network**, not on the internet. The board does
  not belong on a public network.
- The token and password are stored in the project pack in plain text.
- Published variable limit: **64**. The editor will not allow more.
- One broker per board.

| Situation | Behaviour |
|:---|:---|
| Broker unreachable at startup | the board runs normally and connects in the background |
| Broker outage | one diagnostic event, repeated reconnection, the complete state is sent once it is back |
| Slow network | telemetry never extends the control cycle (it runs on the other core) |
| Pack without MQTT | the client never starts, no memory overhead |

## ThingsBoard step by step

1. *Devices* → *Add device*, copy the **Access token**.
2. In the editor: broker = the IP of the ThingsBoard server, username =
   the token, leave the topic at its default.
3. After the upload the values appear under *Latest telemetry* of the
   device.
4. A *Switch* or *Knob* widget in the dashboard → RPC method `setTag`,
   parameters `{"tag_name": value}`.

For OpenRemote or any other broker only the topic and the credentials
change — the message format is the same.

## Home Assistant mode (one topic per variable)

The MQTT settings let you switch the publish mode to **one topic per
variable**. The board then behaves as a process data server — the equivalent
of an OPC server:

| What | Topic | Note |
|:---|:---:|:---|
| tag value | `<base>/<tag>` | **retained** — a new client gets the state immediately |
| write to a tag | `<base>/<tag>/set` | only tags with writing enabled |
| availability | `<base>/status` | `online` / `offline` (last will) |

For example, with the base topic `ctrl32/boilerroom` the temperature
goes to `ctrl32/boilerroom/temperature` and the setpoint is changed by
writing to `ctrl32/boilerroom/setpoint/set`.

### Why retained and last will

- **Retained**: after a restart, Home Assistant immediately receives the
  last value of every variable from the broker. Without it the entities would
  stay empty until a value on the equipment happened to change.
- **Last will (LWT)**: when the board drops out (network or power
  failure), the broker itself publishes `offline` and the entities in HA
  grey out. Without it HA would keep showing the last known value as if
  it were current — which is worse than no value at all.

### Enabling writes — per variable

Every published variable has its own **write** checkbox. It can only be
ticked for a variable that is `rw` in the project. Without it the board
**ignores** a write from the broker, even if somebody sends one. So the
project decides what the supervisory system may touch — not the
other way round.

### The fastest route: MQTT Discovery

In one-topic-per-variable mode the **MQTT Discovery** option is enabled. On
connect the board sends the broker a configuration for every entity and
Home Assistant creates them **by itself** — you write no YAML. All you
need is the MQTT integration set up in HA.

The entities are grouped under a single device, so you see the board in
HA as a whole with all its values underneath. The entity type follows
the variable:

| Variable | Entity in HA |
|:---|:---:|
| numeric, read-only | sensor with a unit |
| boolean, read-only | binary sensor |
| numeric, writable | number (`number`) |
| boolean, writable | switch (`switch`) |

The configuration is published as retained, so it survives a restart of
both HA and the broker. After a project change the entities update
themselves.

### Exporting the configuration (when you want YAML)

If you would rather keep the configuration under your own control
(version control, manual edits), turn Discovery off and use the export:

The *Export YAML for Home Assistant* button produces a file with one
entity per variable:

- numeric read-only variable → `sensor` (with a unit)
- boolean read-only variable → `binary_sensor`
- numeric writable variable → `number`
- boolean writable variable → `switch`

Paste the file into `configuration.yaml` (or pull it in with
`!include`) and restart HA. The ranges on `number` are deliberately
wide — narrow them down in HA to suit the equipment.

### Control stays on the board

The logic, the timers and the local buttons keep running **even when
Home Assistant is switched off, the network is dead and the broker is
unreachable**. MQTT is only a window to the outside. Verified by
measurement: with an unreachable broker the cycle runs at 24 µs with
zero overruns. That is why nothing on it stops while HA is
being updated.

The price of MQTT is roughly **12 kB of RAM** — and only when it is
enabled in the project.

### Ghosts after a project change

Retained messages stay on the broker even after a variable is renamed. Clear
the old topic with an empty retained message:

```
mosquitto_pub -h <broker> -t ctrl32/boilerroom/old_tag -r -n
```

## Typical pitfalls

| Pitfall | Fix |
|:---|:---|
| Nothing shows up in the dashboard | check the token (in ThingsBoard it goes into *username*, not the password) and whether the variable is ticked |
| Values arrive rarely | that is by design — only changes are sent; check the variable deadband |
| A command from the dashboard does nothing | the variable must be published **and** have rw access |
| Broker behind NAT or on the internet | not supported without TLS — the broker belongs on the equipment network |
