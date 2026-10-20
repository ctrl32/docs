---
title: Why ctrl32 at home
source: docs/home-automation.md
hero: img/home-lights.webp
---

# Give your smart home reflexes that keep working when the hub does not

Home Assistant is an excellent brain; it was never meant to be the reflexes. ctrl32 turns an ESP32 into a small PLC for the decisions that must not stop - the pump, the blind limit, the boiler - and hands the brain everything it needs over MQTT, without a line of YAML.

## Who it is for
- Home Assistant users whose pump, valve, heater or blinds must not depend on a server, a Wi-Fi access point or the internet
- Electricians and makers who already know ladder, function blocks or structured text
- Anyone wiring sensors and I/O around a house who wants fieldbuses on the board
- Builders who want PLC discipline at hobby-hardware cost

## What you get
- **A real cycle**: the logic runs on a fixed period (10 ms is the usual) - reads inputs into a snapshot, decides, writes outputs; it never waits for the network or for an automation to fire
- **A fixed overload rule** written into the runtime: **logic > communication > graphics** - the screen stutters before the control does; the cycle is never stretched
- **A watchdog and a defined safe state** - a controller that hangs quietly is worse than one that restarts loudly
- **Numbers you can check**: on the slowest board shipped, 400 logic blocks cost 515 µs, about 5 % of a 10 ms cycle
- **The wires that reach things**, on the same board: Wi-Fi and Ethernet, RS-485 (Modbus RTU), CAN, I²C / SPI / 1-Wire, a touch display
- **One drawing on the glass and in a browser** (WEBview) - no second design, no cloud in between; a kitchen-wall tablet shows the house without talking to anything outside the flat
- **Home Assistant without a plugin**: turn on MQTT and discovery, and the board appears as a device with its variables as sensors, switches and numbers
- **Ladder, FBD or ST**, compiled in the editor and run as bytecode on the board - not a scripting language that restarts when it throws
- **A house block library**: twenty ready blocks built around the wall button - short click, long press, double click, dimming, blinds with travel times, a staircase timer, a thermostat with hysteresis, sunrise and sunset - written in ST, so you can open, read and copy them
- **Alarms with acknowledgement, a timestamped diagnostic buffer, trends and retentive values** that survive a power cut
- **Analog inputs that read real values** - a 4-20 mA pressure transmitter, a thermistor, a Pt1000 - without computing a single gain
- **net32**, a device network: several boards share variables, each running its own logic
- **stepCAN** for I/O where things are: a modular I/O bus in which a module's address comes from where it is, not from a switch on it

## The two jobs
| The job | Who is good at it |
|:---|:---|
| Dashboards, history, phone, voice, "when I come home" | **Home Assistant** |
| A deterministic loop, interlocks, limits, a safe state | **a controller - ctrl32 on an ESP32** |
| Talking between them | **MQTT**, both ways |

Why it matters: the evening the hub updates, a container restarts or the access point reboots, nothing in the house decides anything for ninety seconds. Usually harmless - except a circulation pump whose stop condition lives in an automation, a valve that closes "when the sensor says so" on a server that is not answering, a heater switched by a scheduler that just lost the clock, a garden pump on a dry well. The fix is not a faster server; it is putting the two or three decisions that must not stop into something that cannot stop.

## The honest integration pattern
- **ctrl32 decides, Home Assistant asks.** Interlocks, limits and timings live in the controller; HA sets setpoints, shows history and runs comfort logic ("nobody home -> lower the target").
- **Two-way, but one owner.** The setpoint belongs to HA, the decision to the controller; neither overwrites the other.
- **The house survives the hub.** HA down for an afternoon: the heating holds the last setpoint, the pump respects its dry-run protection, the blinds stop at the limit.

## stepCAN: I/O without one cable per signal
| | With address switches | With stepCAN |
|:---|:---|:---|
| Adding a module | set the address, avoid clashes | plug it in |
| Replacing a failed one | remember what the old one was set to | plug it in |
| Wrong module in a slot | discovered eventually, by behaviour | the head station sees the mismatch |
| Commissioning | a tool and a list | power up |

The usual alternatives each cost something: a device per point on Wi-Fi (the interlock now depends on the access point), a cable per signal to a central rack (the copper and labour dwarf the electronics), a fieldbus with addressed modules (every module must be told who it is, and a replacement needs somebody to remember the setting).

## Compared
| | Cloud relays and plugs | Per-device firmware configured in files | Everything in the hub's automations | An industrial controller with its vendor's editor | **ctrl32 on an ESP32** |
|:---|:---|:---|:---|:---|:---|
| Where the decision happens | a vendor's server | the device, simple rules | the hub | the controller | **the controller** |
| Works with the internet down | often not | yes | yes, while the hub is up | yes | **yes** |
| Works with the **hub** down | no | partly | **no** | yes | **yes** |
| How you write the logic | a phone app | text files | a visual automation editor | ladder / FBD / ST | **ladder, FBD or ST** |
| Fieldbuses (Modbus, CAN) | rarely | some | via add-ons | yes | **yes, on the board** |
| A local screen | no | no | a tablet on the hub | yes, expensive | **yes, glass and browser** |
| Cost per controlled point | low | very low | low | high | **very low** |
| What you own afterwards | an account | a config file | automations | a project | **a project, and the file format** |

Two honest notes: a per-device firmware with simple rules is excellent for a lamp - if all you need is a lamp, use it. And an industrial controller is the right answer when a certificate is required.

## What it is NOT
- No certification of any kind: not CE marking of a finished product, not a functional-safety rating, not a type approval
- Not a safety function: the thermal cut-out, the RCD, the limit switch and the emergency stop are hard-wired; a controller decides what is comfortable, never what is safe
- Not an insurance-grade installation
- Mains wiring is an electrician's job, in every country that has rules about it
- It is a tool for learning, experimenting and building your own things

## How it works
1. Quick start: install the editor, open a shipped project, look at it.
2. Your first project: a button and a lamp from nothing, with the simulation running at your desk before any hardware exists.
3. Lights from the glass: the wall panel that drives Home Assistant lamps.
4. Put it on a board: a board from zero.

## Pictures
- ![A wall button driving a light and a stairwell timer, drawn as a function block diagram in the editor](img/home-lights.webp) - home blocks in a function block diagram

## Runs on
- ESP32 boards (the slowest shipped: a classic ESP32 at 240 MHz); the editor and runtimes also cover STM32 and Linux - a Raspberry Pi doing the heavy end of a house runs the Linux runtime just the same
- Buses: Wi-Fi, Ethernet, RS-485 / Modbus RTU, CAN, I²C, SPI, 1-Wire, MQTT; stepCAN over CANopen
- Home Assistant over MQTT with discovery; shipped tutorials drive Zigbee lamps through HA

## Facts to keep exact
- Cycle: 10 ms is the usual period
- Benchmark: classic ESP32 at 240 MHz, with Ethernet, a Wi-Fi access point, CAN and a 40-screen visualisation beside it - 400 logic blocks = 515 µs, about 5 % of a 10 ms cycle
- Degradation order: logic > communication > graphics
- What each bus reaches: Wi-Fi/Ethernet - the hub, the broker, a phone browser; RS-485 - energy meters, I/O modules, thermostats, inverters; CAN - batteries, hybrid inverters, chargers and wallboxes; I²C / SPI / 1-Wire - temperature, pressure, light, air quality, expanders; touch display - a wall panel that works with the internet off
- Hardware: a board with two fieldbuses and a screen costs less than a single smart relay from a catalogue
- House block library: twenty blocks, written in ST
- Shipped tutorials: a thermostat fed by Home Assistant, and lights from the glass (switches and dims real Zigbee lamps through HA with the true state reported back)
- stepCAN: one Cat5e cable carries the CAN network past every module, beside it a one-way "you are next" chain; at power-up the head station hands out CANopen node-IDs in strict physical order - 64 modules in under a second; 64 modules per segment, 500 kbit/s, up to 30 m of bus, RJ45 in the CANopen connector standard, DIN-rail backplane or scattered around a building (or both on one segment); CANopen CiA 301, 305 and 401 underneath, I/O arrives as variables in the cycle
- stepCAN today: a published specification and reference design, not a box you can order yet; open documentation covers the physical layer, enumeration, CANopen profile, power distribution, a reference module design, a bill of materials and a verification page saying which questions are settled and which open - https://www.ctrl32.com/docs/stepcan/

## Call to action
Download the editor, open a shipped project, and try lights from the glass - in an afternoon you will know exactly what you are choosing.
