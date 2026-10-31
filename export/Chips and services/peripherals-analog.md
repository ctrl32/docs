---
title: "Analog in and out"
slug: peripherals-analog
section: "Chips and services"
order: 328
sidebar_position: 328
generator: tools/docs_export.py
---

# Analog inputs and outputs

Nine ADCs, six DACs and two PWM drivers — the bridge between the digital
variable table and the 4–20 mA, 0–10 V world industrial sensors and actuators
live in.

## Inputs

| You need | Reach for |
|:---|:---:|
| the workhorse: 16-bit, four channels | `ADS1115` |
| the same, faster and coarser | `ADS1015` (12-bit) |
| eight channels | `ADC128S102`, `MCP3008` |
| a single channel, minimal wiring | `MCP3221`, `MCP3421` |
| load cells and strain gauges | `NAU7802` (24-bit, built-in amplifier) |
| a wide input range | `ADS1118` |
| thermocouples, three-wire RTDs, load cells — the analog input card | `ADS1220` (24-bit, a gain to 128, two excitation currents, a temperature sensor) |
| the same with eight inputs, a gain to 256, currents to 1 mA | `ADS122S14` (24-bit, the newer part of the family) |

`ADS1115` is the default for good reasons: 16 bits is enough for almost
anything, four channels covers a small equipment, and its programmable gain
amplifier handles small signals without extra parts.

### Reading 4–20 mA

The industrial standard, and it needs one resistor: current through a
precision resistor becomes a voltage the ADC can read. 4–20 mA through
**165 Ω** gives 0.66–3.3 V, which suits a 3.3 V input.

You do not work the rest out yourself: tell the channel it is a
4-20 mA input, give it the shunt and what the range means, and the
device delivers bar (or whatever your unit is). The same goes for
0-10 V sensors, thermistors and Pt100/Pt1000 —
[Reading real values](/docs/peripherals-and-services/analog-inputs/) is the page.

Why the world uses current rather than voltage is worth knowing. A broken
wire reads **0 mA** — outside the 4–20 range, and therefore *detectably*
wrong. A 0–10 V sensor with a broken wire reads 0 V, which is a perfectly
valid "zero".

!!! tip "Use the dead band below 4 mA"
    Alarm on anything under about 3.5 mA. That is a wire fault, a dead
    sensor or a power failure at the transmitter — and being able to tell
    is what you paid for when you chose 4–20 mA.

## Outputs

DACs — `MCP4725`, `MCP4728`, `DAC7678`, `GP8403` — produce a real
voltage for a drive input, an analog setpoint, a proportional valve.
`GP8403` is worth noting: it outputs **0–10 V directly**, without the
amplifier the others need.

Digital potentiometers — `MCP4461`, `MCP47A1` — replace a trimmer in
somebody else's circuit.

PWM drivers — `PCA9685` (16 channels), `TLC59208F` — produce a switching
signal. With an RC filter it approximates an analog voltage; without one
it drives LEDs, heaters and servos directly.

| You need | Reach for |
|:---|:---:|
| 0–10 V for a drive | `GP8403` |
| a clean low-voltage analog signal | `MCP4725`, `MCP4728` |
| many channels of dimming or heating | `PCA9685` |
| to replace a trimmer | `MCP4461` |

!!! warning "3.3 V is not 10 V"
    Most DACs output at most their supply voltage. A drive expecting
    0–10 V sees a third of the setpoint you think you sent and runs at a
    third of the speed — which looks like a scaling bug in the program,
    and is not. Either use `GP8403`, or add an amplifier.

!!! tip "Scale in the variable, not in the logic"
    Give the variable a scale and a unit and let it convert counts to bar or
    volts. The logic then reads bar, the screen shows bar, and nobody has
    to remember what 24 576 meant. For an input, the shortest road there is
    to say what is wired to it — see
    [Reading real values](/docs/peripherals-and-services/analog-inputs/).

## The chips

### Analog inputs

| Chip | Bus | What it is |
|:---|:---:|:---|
| `ADC128S102` | SPI | SPI 12-bit ADC, 8 single-ended channels (TI) — raw counts per channel; two frames per conversion (address, then data). addr = CS pin. |
| `ADS1015` | I2C | I2C 12-bit ADC, 4 single-ended channels (AIN0–3 = pin 0–3, INPUTS only), address 0x48–0x4B — the faster 12-bit sibling of the ADS1115 (same registers, conversion in 12-bit steps of 16: raw keeps the ADS1115 scale). Optional key range = full scale in volts, stored as PGA code+1 like the ADS1115. |
| `ADS1115` | I2C | I2C 16-bit ADC, 4 single-ended channels (AIN0–3 = pin 0–3, INPUTS only), address 0x48–0x4B. Optional key range = full scale in volts (6.144/4.096/2.048/1.024/0.512/0.256, default 4.096) — stored in PeriphRec.config as PGA code+1 (0 = default). The raw variable value is the i16 conversion register; engineering units come from the variable gain/offset. |
| `ADS1118` | SPI | SPI 16-bit ADC (the ADS1115 over SPI) — 4 single-ended channels, raw conversion counts at ±2.048 V; units via variable gain/offset. addr = CS pin. |
| `ADS1220` | SPI | SPI 24-bit delta-sigma ADC (TI) — 4 inputs as single-ended channels or differential pairs, a PGA 1-128, two matched excitation currents (10-1500 µA) for an RTD, four reference choices (internal 2.048 V, REFP0/REFN0, AIN2/AIN3, AVDD), a temperature sensor for a thermocouple's cold junction, 50/60 Hz rejection. Every field of its four configuration registers is a setting of the channel; the channel's sensor type (thermocouple, RTD by excitation, a bridge, Ni1000) does the arithmetic. addr = CS pin. |
| `ADS122S14` | SPI | SPI 24-bit delta-sigma ADC (TI) — 8 inputs, any two as a pair or one against ground, a PGA 0.5-256, two excitation currents in 1 µA or 10 µA units up to 1 mA on any input, the reference internal (1.25 or 2.5 V), external on AIN4/AIN5 (buffered on request) or the supply, four speed modes with 20/25 SPS 50/60 Hz rejection, global chop, a start delay, burn-out currents of 0.2/1/10 µA, a temperature sensor and the supply and reference monitors. Every field of its configuration registers is a setting of the channel, the same sensor types as the ADS1220. addr = CS pin. |
| `MCP3008` | SPI | SPI 10-bit ADC, 8 single-ended channels — raw counts per channel (units via variable gain/offset). addr = CS pin. |
| `MCP3204` | SPI | SPI 12-bit ADC, 4 single-ended channels — raw counts per channel (units via variable gain/offset). addr = CS pin. |
| `MCP3221` | I2C | I2C 12-bit ADC, 1 channel, no configuration at all — channel 0 = raw counts (units via variable gain/offset). Address 0x48–0x4F (factory-coded). |
| `MCP3421` | I2C | I2C 18-bit delta-sigma ADC, 1 differential channel — channel 0 = raw converter value; engineering units via variable gain/offset. PeriphRec.config: bits 0–2 = PGA code +1 (YAML gain: 1/2/4/8), bits 4–6 = resolution code +1 (YAML bits: 12/14/16/18, default 16 — 15 SPS). Address 0x68–0x6F (factory-coded). |
| `NAU7802` | I2C | I2C 24-bit ADC for strain-gauge bridges (weighing) — channel 0 = raw converter value; kilograms come from variable gain/offset (scale calibration = two known points). PeriphRec.config: bits 0–3 = PGA gain code +1 (default x128, YAML key gain: 1..128), bits 4–7 = rate code +1 (default 10 SPS, YAML key rate: 10/20/40/80/320). The internal 3.0 V LDO powers the bridge (AVDD). |

### Analog outputs

| Chip | Bus | What it is |
|:---|:---:|:---|
| `DAC7678` | I2C | I2C 12-bit DAC, 8 channels (OUTPUTS) — raw = (variable - offset) / gain clamped to 0..4095, written on change per channel. Address 0x48–0x4B. |
| `GP8403` | I2C | I2C 2-channel 0–10 V DAC (DFRobot GP8403) — channels 0/1 are OUTPUTS: raw = (variable - offset) / gain, 12-bit over the range. Optional key range = 5 or 10 (V full scale, default 10) — stored in PeriphRec.config as 1 = 5 V. Address 0x58–0x5F. Verify on the bench — written from the DFRobot library, not a datasheet. |
| `MCP4461` | I2C | I2C quad digital potentiometer — channels 0–3 = volatile wipers, raw 0..256 (OUTPUTS). Address 0x2C–0x2F. |
| `MCP4725` | I2C | I2C 12-bit DAC — channel 0 is an OUTPUT: raw = (variable - offset) / gain, clamped to 0..4095. Variable gain/offset therefore defines the engineering units (e.g. gain 10.0/4095 for a 0–10 V module). Written only on change. |
| `MCP4728` | I2C | I2C 12-bit DAC, 4 channels (OUTPUTS) — raw = (variable - offset) / gain, clamped to 0..4095; all four channels go out in one fast write, only on change. Address 0x60–0x67. |
| `MCP47A1` | I2C | I2C 6-bit DAC, 1 channel (OUTPUT) — raw 0..63; the cheapest analog trim output there is. Fixed address 0x2E. |

### PWM outputs

| Chip | Bus | What it is |
|:---|:---:|:---|
| `PCA9685` | I2C | I2C 16-channel 12-bit PWM — every pin is an OUTPUT, the variable value is duty in % (0–100, like the on-chip PWM service). Optional key freq_hz = PWM frequency 24–1526 Hz (default 200) — stored directly in PeriphRec.config. Address 0x40–0x7F (0x70 is the all-call address — avoid it with other chips). |
| `TLC59208F` | I2C | I2C 8-channel 8-bit LED PWM — every channel is an OUTPUT, the variable value is duty in % (0–100). Address 0x20–0x27 (configurable wider; the check covers the common range). |

Every entry above is in the editor: pick the chip, give it
an address or a chip-select pin, and its channels become variables.
See [Adding a peripheral](/docs/buses/adding-peripherals/) for the
click-through.
