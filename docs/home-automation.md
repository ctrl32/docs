---
image: img/home-lights.webp
image_alt: "A wall button driving a light and a stairwell timer, drawn as a function block diagram in the editor"
---

# Home automation with ctrl32 and the ESP32

**The short version.** A smart home has two jobs, and they are not the
same job. One is the *brain*: dashboards, history, phone, voice,
hundreds of integrations. The other is the *reflexes*: the pump that
must not run dry, the blind that must stop at its limit, the boiler
that must not cycle every forty seconds — the part that has to keep
working when the server reboots, the Wi-Fi drops or the internet is
gone for a day.

Home Assistant is an excellent brain. It was never meant to be the
reflexes. ctrl32 on an ESP32 gives you the reflexes for the price of a
takeaway meal, and hands the brain everything it needs to see, over
MQTT, without a line of YAML.

This page explains why that split is worth making, what it costs, and
where the honest limits are.

---

## 1. The two jobs, and what happens when you merge them

Every smart-home setup eventually meets the same evening: the hub is
updating, a container restarts, the Wi-Fi access point reboots — and
for ninety seconds nothing in the house decides anything. Most of the
time that is harmless. The exceptions are the ones that cost money:

- a circulation pump whose stop condition lives in an automation,
- a valve that closes "when the sensor says so", on a server that is
  not answering,
- a heater that is switched by a scheduler that just lost the clock,
- a garden pump on a dry well.

The fix is not a faster server. It is putting the two or three
decisions that *must not stop* in something that cannot stop — a small
controller that runs one loop, every ten milliseconds, whether or not
anything else in the house is alive.

That is what a PLC is, and it is what ctrl32 makes an ESP32 into.

| The job | Who is good at it |
|:---|:---|
| Dashboards, history, phone, voice, "when I come home" | **Home Assistant** |
| A deterministic loop, interlocks, limits, a safe state | **a controller — ctrl32 on an ESP32** |
| Talking between them | **MQTT**, both ways |

---

## 2. What "it keeps working" actually means here

Not a slogan — three concrete mechanics.

**A real cycle.** The logic runs on a fixed period (10 ms is the
usual), reads its inputs into a snapshot, decides, writes its outputs.
It does not wait for the network, and it does not run "when the
automation fires".

**A rule about what gets dropped.** When a board is overloaded the
order is fixed and written into the runtime: **logic > communication >
graphics**. The screen stutters before the control does. The cycle is
never stretched to draw a prettier picture.

**Numbers you can check.** On the slowest board we ship — a classic
ESP32 at 240 MHz, with ethernet, a Wi-Fi access point, CAN and a
40-screen visualisation running beside it — 400 logic blocks cost
**515 µs**, about **5 %** of a 10 ms cycle. A whole house's worth of
interlocks does not come close to the ceiling. The rest of the
measurements are on the [limits](limits.md) page, with the method.

**And a watchdog and a defined safe state**, because a controller that
hangs quietly is worse than one that restarts loudly.

---

## 3. Why the ESP32 in particular

A house is not short of computing power; it is short of **wires that
reach things**. That is where this chip earns its place:

| On the same board | What it reaches in a house |
|:---|:---|
| **Wi-Fi and ethernet** | the hub, the broker, a browser on a phone |
| **RS-485 (Modbus RTU)** | energy meters, I/O modules, thermostats, inverters |
| **CAN** | batteries, hybrid inverters, chargers and wallboxes |
| **I²C / SPI / 1-Wire** | temperature, pressure, light, air quality, expanders |
| **A touch display** | a panel on the wall that works with the internet off |

Add the price. A board that speaks two fieldbuses and drives a screen
costs less than a single smart relay from a catalogue, and you can put
five of them in a house without thinking about it.

!!! tip "The screen is not the point, but it is a good one"
    The same drawing runs on the panel's glass **and** in a browser
    ([WEBview](webview.md)) with no second design and no cloud in
    between. A tablet on the kitchen wall shows the house without
    talking to anything outside the flat.

---

## 4. Where Home Assistant fits — the honest integration

There is no plugin to install and no YAML to write. Turn on MQTT in
the project, turn on discovery, and the board **appears in Home
Assistant as a device** with its variables underneath as sensors,
switches and numbers. The route, start to finish, is on the
[Home Assistant](home-assistant.md) page.

The pattern that works in practice:

- **ctrl32 decides, Home Assistant asks.** The interlocks, limits and
  timings live in the controller. HA sets setpoints, shows history,
  and runs the comfort logic ("nobody home → lower the target").
- **Two-way, but one owner.** A value has one owner. The setpoint
  belongs to HA, the decision belongs to the controller, and neither
  overwrites the other's.
- **The house survives the hub.** If HA is down for an afternoon, the
  heating still holds the last setpoint, the pump still respects its
  dry-run protection, the blinds still stop at the limit.

Two shipped tutorials do exactly this, end to end:
[a thermostat fed by Home Assistant](tutorial-ha-thermostat.md) and
[lights from the glass](tutorial-ha-lights.md) — a wall panel that
switches and dims real Zigbee lamps through HA, with the true state
reported back to the switch on the screen.

---

## 5. The other half of a house: getting I/O to where things are

A controller on a DIN rail solves nothing by itself. The sensors are
in the boiler room, the buttons are by the doors, the blinds are on
the first floor and the pump is in the garden — and the reason home
automation gets expensive is not the controller, it is **one cable per
signal, all the way back to one box**.

The usual answers each cost something:

- **A device per point on Wi-Fi.** Cheap and quick, and now the
  interlock depends on the access point.
- **A cable per signal to a central rack.** Correct, and priced like
  it: the copper and the labour dwarf the electronics.
- **A fieldbus with addressed modules.** The right shape — one cable
  past every module — with one nuisance that never goes away: each
  module has to be told *who it is*, with DIP switches, a rotary
  encoder or a commissioning tool. Replace a failed module and
  somebody has to remember the setting; fit the right module in the
  wrong slot and nothing tells you.

**[stepCAN](https://www.ctrl32.com/docs/stepcan/) is our answer to
that last nuisance.** It is a modular I/O bus in which a module's
address comes from *where it is*, not from what somebody set on it.
One Cat5e cable carries the CAN network past every module, and
alongside it runs a one-way "you are next" chain. At power-up the head
station walks that chain and hands out CANopen node-IDs **in strict
physical order** — sixty-four modules in under a second.

What that changes in a house:

| | With address switches | With stepCAN |
|:---|:---|:---|
| Adding a module | set the address, avoid clashes | plug it in |
| Replacing a failed one | remember what the old one was set to | plug it in |
| Wrong module in a slot | discovered eventually, by behaviour | the head station sees the mismatch |
| Commissioning | a tool and a list | power up |

The numbers it is designed to: **64 modules per segment**,
**500 kbit/s**, up to **30 m** of bus, RJ45 in the CANopen connector
standard, modules on a DIN-rail backplane or scattered around a
building — or both on one segment.

And because it is **CANopen** underneath (CiA 301, 305 and 401), the
I/O arrives in a ctrl32 project the way CANopen devices already do:
as variables, in the cycle, with the manager the runtime already
carries.

!!! note "Where stepCAN is today"
    stepCAN is a **published specification and reference design**, not
    a box you can order yet. The documentation is open — the physical
    layer, the enumeration, the CANopen profile, the power
    distribution, a reference module design and a bill of materials —
    including a verification page that says plainly which questions
    are settled and which are still open. Read it before you build
    against it: [the stepCAN documentation](https://www.ctrl32.com/docs/stepcan/).

---

## 6. How it compares with the usual ways

Named products change every year; the *categories* do not. Here is
what each one is actually good at.

|:---|:---|:---|:---|:---|:---|
| Where the decision happens | a vendor's server | the device, simple rules | the hub | the controller | **the controller** |
| Works with the internet down | often not | yes | yes, while the hub is up | yes | **yes** |
| Works with the **hub** down | no | partly | **no** | yes | **yes** |
| How you write the logic | a phone app | text files | a visual automation editor | ladder / FBD / ST | **ladder, FBD or ST** |
| Fieldbuses (Modbus, CAN) | rarely | some | via add-ons | yes | **yes, on the board** |
| A local screen | no | no | a tablet on the hub | yes, expensive | **yes, glass and browser** |
| Cost per controlled point | low | very low | low | high | **very low** |
| What you own afterwards | an account | a config file | automations | a project | **a project, and the file format** |

Two honest notes on that table. A per-device firmware with simple
rules is *excellent* for a lamp — if all you need is a lamp, use it.
And an industrial controller is the right answer when a certificate is
required; see the limits below.

What ctrl32 adds is the middle ground that has been missing: **PLC
discipline at hobby prices, with the fieldbuses already on the board**.

---

## 7. What you actually build with it

- **Ladder, function blocks or structured text** — the three
  languages an electrician already knows, compiled in the editor and
  run as bytecode on the board. Not a scripting language that
  restarts when it throws.
- **A block library for houses**: twenty ready blocks built around
  the wall button — short click, long press, double click, dimming,
  blinds with their travel times, a staircase timer, a thermostat
  with hysteresis, sunrise and sunset. They are written in ST, so you
  can open one, read it, and copy it into a block of your own. See
  [Home automation blocks](blocks-home.md).
- **Screens** that work offline, on the panel and in a browser.
- **Alarms with acknowledgement**, a **diagnostic buffer** with
  timestamps, **trends**, and **retentive values** that survive a
  power cut.
- **Analog inputs that read real values** — a 4-20 mA pressure
  transmitter, a thermistor, a Pt1000 — without you computing a
  single gain ([Reading real values](analog-inputs.md)).
- **A device network** (net32) when one board is not enough: several
  boards share variables, each running its own logic.

---

## 8. What it is NOT — read this before you plan anything

This is the part a marketing page usually leaves out, so it is in the
middle of this one.

- **No certification of any kind.** Not CE marking of a finished
  product, not a functional-safety rating, not a type approval.
- **Not a safety function.** Anything that protects a person or the
  building is hard-wired: the thermal cut-out, the RCD, the limit
  switch, the emergency stop. A controller decides what is
  comfortable, never what is safe.
- **Not an insurance-grade installation.** If your insurer would want
  to know what switched the boiler, this is not the thing to hide in
  the wall.
- **Mains wiring is an electrician's job**, in every country that has
  rules about it.

It is a tool for learning, experimenting and building your own
things — and it is honest about that everywhere in this
documentation, including [Intended use](intended-use.md).

---

- **The hardware** is whatever an ESP32 board with the buses you need
  costs — usually less than one smart relay.

---

## 10. How to find out in an afternoon

1. [Quick start](quickstart.md) — install, open a shipped project,
   look at it.
2. [Your first project](tutorial.md) — a button and a lamp, from
   nothing, with the simulation running at your desk before any
   hardware exists.
3. [Lights from the glass](tutorial-ha-lights.md) — the wall panel
   that drives Home Assistant lamps.
4. Put it on a board: [a board from zero](first-run.md).

If after those four you still think the hub should keep the
interlocks, you will at least know exactly what you are choosing — and
that is the point of this page.
