---
title: "Power and energy"
slug: peripherals-power
section: "Chips and services"
order: 326
sidebar_position: 326
generator: tools/docs_export.py
---

# Power and energy

Nine power monitors, three energy meters and two battery gauges.

## Measuring what a setup draws

| You need | Reach for |
|:---|:---:|
| DC current and voltage on a rail | `INA219`, `INA226`, `INA236` |
| A battery charger / UPS: supply and battery voltage and current, charge state | `BQ25790` |
| higher precision, wider range | `INA228`, `INA238` |
| three rails at once | `INA3221` |
| current without an external shunt | `INA260` (shunt built in) |
| mains energy, single phase | `ADE7953`, `ATM90E26` |
| mains energy, three phase | `ATM90E32` |
| battery state of charge | `MAX17043`, `LC709203F` |

`INA226` measures current through a shunt and voltage at the same time
and reports power directly. `INA3221` does three channels, which suits a
board watching its own supplies.

## Why measure current in a real setup

Current is the cheapest condition monitoring there is. A motor drawing
more than it did last month has a bearing going; one drawing less has
lost its load — a slipping belt, an empty hopper, a broken coupling.

None of that needs a special sensor. It needs current you can already
measure, a [trend](/docs/operation/), and somebody looking at it
occasionally.

!!! tip "Alarm on the change, not the value"
    An absolute current limit catches a seized motor and nothing else. A
    limit relative to what *this* equipment normally draws — a running
    average over a week — catches the bearing three months before it
    fails.

## The traps

!!! danger "Mains metering means mains voltage"
    `ADE7953` and the `ATM90E` parts connect to live conductors. That is
    an electrician's job, in an enclosure rated for it, with the
    isolation the standards require — not a breakout board on a bench.

!!! warning "Shunt placement decides what you measure"
    A shunt in the wrong leg measures the wrong thing; a shunt after the
    load measures correctly but sits at load potential, which the monitor
    may not tolerate. Follow the reference circuit — this is not the
    place for improvisation.

!!! tip "Battery gauges need to learn"
    A fuel gauge estimates charge from voltage and current, and the
    estimate is poor until it has seen a full charge and discharge.
    Expect the first week to be optimistic.

## The chips

### Power monitoring

| Chip | Bus | What it is |
|:---|:---:|:---|
| `INA219` | I2C | I2C current/voltage/power monitor — channels: 0 = current [A], 1 = bus voltage [V], 2 = power [W]. PeriphRec.config = shunt resistance in tenths of mΩ (0 = 100 mΩ, the common blue module; YAML key shunt_mohm). Address 0x40–0x4F. |
| `INA226` | I2C | I2C current/voltage/power monitor — channels: 0 = current [A], 1 = bus voltage [V], 2 = power [W]. PeriphRec.config = shunt resistance in tenths of mΩ (0 = 100 mΩ, the common blue module; YAML key shunt_mohm). Current is computed from Vshunt/R; fine-tuning via variable gain/offset. |
| `BQ25790` | I2C | I2C buck-boost battery charger with ADC (TI BQ25790 / BQ25792; the UPS of the reTerminal E10-1) — channels: 0 = supply voltage VBUS [V], 1 = battery VBAT [V], 2 = supply current IBUS [A], 3 = battery current IBAT [A] (+ = charging), 4 = charge state (0 off, 1 trickle, 2 pre, 3 fast, 4 taper, 6 top-off, 7 done), 5 = supply present (1/0), 6 = die temperature [°C]. Read-only: the charge limits stay the board's. Address 0x6B. |
| `INA228` | I2C | I2C 20-bit current/voltage/power monitor — channels: 0 = current [A], 1 = bus voltage [V], 2 = power [W]. PeriphRec.config = shunt in tenths of mΩ (0 = 100 mΩ, YAML shunt_mohm). Address 0x40–0x4F. |
| `INA229` | SPI | SPI 20-bit current/voltage/power monitor (the INA228 over SPI) — channels: 0 = current [A], 1 = bus voltage [V], 2 = power [W]. PeriphRec.config = shunt in tenths of mΩ (0 = 100 mΩ, YAML shunt_mohm). addr = CS pin. |
| `INA236` | I2C | I2C current/voltage/power monitor (the INA226 successor) — channels: 0 = current [A], 1 = bus voltage [V], 2 = power [W]. PeriphRec.config = shunt in tenths of mΩ (0 = 100 mΩ, YAML shunt_mohm). Address 0x40–0x4F. |
| `INA238` | I2C | I2C current/voltage/power monitor (85 V bus) — channels: 0 = current [A], 1 = bus voltage [V], 2 = power [W]. PeriphRec.config = shunt in tenths of mΩ (0 = 100 mΩ, YAML shunt_mohm). Address 0x40–0x4F. |
| `INA239` | SPI | SPI current/voltage/power monitor (the INA238 over SPI) — channels: 0 = current [A], 1 = bus voltage [V], 2 = power [W]. PeriphRec.config = shunt in tenths of mΩ (0 = 100 mΩ, YAML shunt_mohm). addr = CS pin. |
| `INA260` | I2C | I2C current/voltage/power monitor with the shunt built in (2 mΩ) — channels: 0 = current [A], 1 = bus voltage [V], 2 = power [W]. No shunt configuration at all. Address 0x40–0x4F. |
| `INA3221` | I2C | I2C 3-channel current/voltage monitor — channels: 0–2 = current 1–3 [A], 3–5 = bus voltage 1–3 [V]. One shunt value for all three channels: PeriphRec.config = tenths of mΩ (0 = 100 mΩ, YAML key shunt_mohm). Address 0x40–0x43. |

### Energy metering

| Chip | Bus | What it is |
|:---|:---:|:---|
| `ADE7953` | I2C | I2C single-phase energy metering AFE — channels: 0 = Vrms, 1 = Irms A, 2 = Irms B, 3 = active power A (signed), 4 = active power B (signed), all RAW 24-bit counts (scaling depends on the divider/shunt/CT — put it into the variable gain); 5 = line frequency [Hz]. Init writes the datasheet unlock (0xAD to 0xFE, 0x0030 to 0x120). Address 0x38. VERIFY ON THE BENCH. |
| `ATM90E26` | SPI | SPI single-phase energy meter — channels: 0 = Urms [V], 1 = Irms [A], 2 = active power (raw complement counts, the unit depends on metering calibration), 3 = line frequency [Hz], 4 = power factor. Probe rewrites SagTh with its power-on default (0x1D64) and reads it back. Metering calibration is left at defaults — calibrate on the bench. addr = CS pin. |
| `ATM90E32` | SPI | SPI three-phase energy meter — channels: 0-2 = Urms A/B/C [V], 3-5 = Irms A/B/C [A], 6 = line frequency [Hz], 7 = total active power (raw complement counts). 16-bit register addresses; probe via CfgRegAccEn 0x55AA + LastSPIData readback. Calibrate on the bench. addr = CS pin. |

### Battery gauges

| Chip | Bus | What it is |
|:---|:---:|:---|
| `LC709203F` | I2C | I2C LiPo fuel gauge (ON Semi) — channels: 0 = cell voltage [V], 1 = state of charge [%]. Fixed address 0x0B; commands carry a CRC-8 PEC. VERIFY ON THE BENCH. |
| `MAX17043` | I2C | I2C LiPo fuel gauge — channels: 0 = cell voltage [V], 1 = state of charge [%]. Fixed address 0x36 (collides with the AS5600 — one bus carries only one of them). |

Every entry above is in the editor: pick the chip, give it
an address or a chip-select pin, and its channels become variables.
See [Adding a peripheral](/docs/buses/adding-peripherals/) for the
click-through.
