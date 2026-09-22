---
image: img/editor-fbd.png
image_alt: "A function block diagram in the editor"
---

# Tutorial projects

Seventeen small projects, each about **one idea** — and six of them are
the projects the step-by-step pages build. Open one, read it whole
in a minute, and you know the thing it teaches.

When the single ideas are familiar, two **worked projects** put them
together across two real boards:

- [From a blank device to a running one](tutorial-linux-device.md) —
  a Raspberry Pi with nothing but an operating system becomes a
  ctrl32 device, from the editor, without a single Linux command.
- [RS-485, step by step](tutorial-rs485.md) — the wires, the port,
  the master, a device, a variable, and what to check when the pair
  stays silent.
- [OPC UA, step by step](tutorial-opcua.md) — turn the server on,
  read a value, write one back, and choose what the device's
  certificate should be before it leaves the desk.
- [EtherCAT, step by step](tutorial-ethercat.md) — a spare network
  port becomes a line with a drive on it, and the motor turns from
  the screen.
- [A vehicle bus, step by step](tutorial-vehicle.md) — an engine on
  J1939: the parameter groups it broadcasts taken from the library,
  the same control unit asked for its readings and its fault codes,
  and one rung that does the asking when a person presses.
- [Two boards over Modbus](tutorial-modbus-pair.md) — a WiFi slave
  measuring temperatures, an ethernet master displaying and
  commanding them, and the same interlock written in all three
  languages.
- [Hot tank](three-zone-thermostat.md) — the complete system that
  grows out of it: a three-zone heated bath from cosmetics
  production, router-less WiFi, per-zone thermostats, AUTO/MANUAL, a
  code-protected settings page, link protection, an MQTT uplink to a
  SCADA and a full technical manual with measured load figures.
- [Thermostat fed by Home Assistant](tutorial-ha-thermostat.md) — the
  EVB and its glass heat by a Zigbee sensor read through HA, with a
  ladder watchdog deciding how much to trust the network.
- [Lights from the glass](tutorial-ha-lights.md) — the F7 Discovery
  switches and dims real Zigbee lights through HA, with the ACTUAL
  states reported back to the lamps beside the switches.

They are deliberately not impressive. A project that demonstrates six
features at once teaches none of them, because you cannot tell which
part is doing what.

Find them in **ProgramData\ctrl32\tutorials**.

!!! success "They are tested on every build"
    Most of these are also regression fixtures: the build compiles them
    and compares the result, every time. So they cannot quietly rot into
    something that no longer works — if one of them does something the
    documentation does not describe, the project is right.

---

## Ladder

![The seal-in circuit: a start button that latches through the contact it energised](img/quickstart-sealin.webp){: .sb-center}

| Project | Teaches |
|:---|:---|
| **ladder_sealin** | the seal-in circuit — a start button that latches through the contact it energised. The oldest pattern in ladder, and still the one you write most |
| **ladder_sealin_st** | the same circuit written in **ST** — open the two side by side and the language stops being a mystery |
| **ladder_box** | a block **in** a rung with EN/ENO: what happens when the rung stops conducting, and why the answer is "freezes", not "resets" |
| **first_light** | the project of [Your first project](tutorial.md): a button, an off-delay timer, a lamp, a screen |
| **own_block** | a start/stop latch as **your own function block**, used twice — the project of [Your own function block](own-block.md) |
| **bit_lamp** | one **bit** of a word under a coil — a lamp test that writes bit 3 without disturbing the rest of the word |

Start with `ladder_sealin`. If you have written ladder before, it will
look familiar in ten seconds and confirm that nothing here is exotic.

---

## Structured Text

![Structured Text in the editor, with the same variables the rungs use](img/st-editor.webp){: .sb-center}

| Project | Teaches |
|:---|:---|
| **st_pous** | several program units in one project, and how they are ordered |
| **st_ld_mix** | a ladder POU and an ST POU **in the same project** — the two are not alternatives, they are views you can mix per program unit |
| **st_string** | bounded strings in ST: parsing a command, the motif behind reading a barcode scanner |

`st_ld_mix` is the one worth opening if you are deciding which language
to use. The answer is usually "both" — a sequence in ST, the interlocks
in ladder, because that is where each is clearest.

---

## Function block diagram

| Project | Teaches |
|:---|:---|
| **fbd_intro** | a complete tank controller in seven blocks: 4–20 mA scaled to a percentage, hysteresis deciding "full", and a low-level detector delayed so a wave does not trip it |

![The FBD editor with fbd_intro open: SCALE, HYST, NOT, LT and TON wired through named variables](img/editor-fbd.png){: .sb-center}

---

## Drives

| Project | Teaches |
|:---|:---|
| **i550_axis** | a frequency inverter over CAN from the wizard to the first turn of the motor — the project of [A drive over CAN, step by step](tutorial-i550-can.md) |

---

## Home Assistant

| Project | Teaches |
|:---|:---|
| **ha_thermostat_evb** | a wall thermostat whose room temperature arrives from a Zigbee sensor through Home Assistant, with a watchdog that says so when it stops — the project of [A thermostat fed by Home Assistant](tutorial-ha-thermostat.md) |
| **ha_lights_f7** | two lights and a dimmer driven from the glass, where every switch has a lamp beside it showing what the bulb really did — the project of [Lights and a dimmer from the glass](tutorial-ha-lights.md) |

---

## Timing and values

| Project | Teaches |
|:---|:---|
| **timer_et** | the `ET` output of a timer bound to a variable — so a delay can be *shown* filling on a screen instead of leaving somebody waiting at a blank panel |
| **time_setpoint** | a `TIME` variable set from the screen: the operator changes a delay without anybody rebuilding anything |
| **pou_order** | why execution order matters, and what happens when two program units' blocks are interleaved |

`time_setpoint` is the small idea with the largest payoff in practice.
Every delay somebody might want to adjust should be a variable, and it
costs one field.

---

## How to use them

**Read first, run second.** These are short enough to read whole, and
the reading is the point. Open the project, look at the variable list,
look at the program, then press **Simulate** and watch it do what you
just read.

**Then break something.** Change a threshold and see what happens.
Delete a rung. Swap two blocks in `pou_order` and watch the value go one
cycle stale. Nothing here can hurt anything, and the failures teach more
than the successes.

**Then copy the pattern.** A seal-in circuit, a timer with its elapsed
time on a screen, a setpoint the operator can change — those are the
pieces most projects are made of.

---

## Where next

| | |
|:---|:---|
| [Your first project](tutorial.md) | build one from an empty file |
| [Examples](examples.md) | the complete board projects |
| [Function blocks](blocks.md) | everything the library offers |
| [Ladder](ladder.md) · [FBD](fbd-composites.md) · [ST](st-language.md) | the languages themselves |
