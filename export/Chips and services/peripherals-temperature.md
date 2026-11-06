---
title: "Temperature"
slug: peripherals-temperature
section: "Chips and services"
order: 323
sidebar_position: 323
generator: tools/docs_export.py
---

# Temperature

Fourteen ways to measure temperature, and the choice matters more than
the count suggests: a chip that reads to a hundredth of a degree is
useless on a furnace, and a thermocouple converter is pointless in a
fridge.

## Choosing

| You are measuring | Reach for |
|:---|:---|
| room, cabinet, comfort range | an **I2C sensor** — `TMP102`, `LM75B`, `MCP9808` |
| something that must be accurate | `TMP117` (±0.1 °C) or `MCP9808` (±0.25 °C) |
| a furnace, a flue, a mould | a **thermocouple** — `MAX31855`, `MAX31856`, `MCP9600` |
| an industrial process with a PT100 | `MAX31865` |
| something moving, or too hot to touch | `MLX90614` — infrared, non-contact |

**Rule of thumb.** Below about 125 °C, an I2C sensor is cheaper, simpler
and more accurate. Above it, you need a thermocouple or an RTD, and the
extra wiring comes with them.

## The traps

!!! warning "Address collisions"
    `LM75B` and `TMP102` share the 0x48–0x4F range, and so do several
    others. Two chips on one bus at one address means neither works —
    and the symptom is nonsense readings, not silence. The project
    checks this when you build, so you find out at your desk.

!!! warning "Cold-junction compensation is not optional"
    A thermocouple measures a *difference*. The converter has to know
    its own temperature to give you an absolute one, which is why these
    chips report two channels. Put the converter somewhere with a stable
    temperature — not next to the heater it is measuring.

!!! tip "A PT100 wants to know how it is wired"
    `MAX31865` needs telling whether the sensor is 2-, 3- or 4-wire and
    what the reference resistor is. Get it wrong and the reading is
    consistently off — often by a plausible-looking amount, which is the
    kind of error that survives for months.

## The chip's page

The thermocouple and RTD converters have a page of their own (a click
on the chip in the tree): the settings, the words the device writes, a
table of the signals with their variables, and the chip drawn with its
sensor and its bus pins, with the GPIO numbers the project or the board
gives them.

The `MAX31855` comes as seven parts, one per thermocouple type, so the
part is what you pick; the device can correct the chip's straight line
with the standard's table.

![The MAX31855's page: the part, the correction with the standard's table, the three signals, and a type J thermocouple drawn on the chip](img/chip-max31855.webp){: .sb-center}

The `MAX6675` has nothing to set: one frame with the temperature and the
open-thermocouple bit.

![The MAX6675's page: the two signals, and a type K thermocouple drawn on the chip](img/chip-max6675.webp){: .sb-center}

The `MAX31856` has every register on its page: the type, the samples
averaged, the mains filter, the open-circuit test, the cold junction and
its offset, the four fault thresholds, the fault mode and the faults that
drive the FAULT pin, continuous or 1-shot conversions.

![The MAX31856's page: the converter, the fault thresholds and the FAULT pin, the conversions, the words written, and the chip drawn with its thermocouple](img/chip-max31856.webp){: .sb-center}

The `MAX31865` the same for an RTD: the sensor, the reference resistor,
the wires, the mains filter, the fault thresholds in degrees, the fault
detection cycle at start-up, continuous or 1-shot conversions. The
picture follows the wires you chose.

![The MAX31865's page: a three-wire PT100, the fault thresholds, the detection cycle, the words written, and the sensor and reference resistor drawn on the chip](img/chip-max31865.webp){: .sb-center}

## The chips

### Temperature sensors

| Chip | Bus | What it is |
|:---|:---:|:---|
| `LM75B` | I2C | I2C temperature sensor (industry classic) — channel 0 = temperature [°C], 11-bit 0.125 °C resolution, address 0x48–0x4F. Collides with TMP102 addresses — the build watches the bus. |
| `MCP9808` | I2C | I2C precision temperature sensor ±0.25 °C — channel 0 = temperature [°C], 0.0625 °C resolution, address 0x18–0x1F. |
| `MLX90614` | I2C | I2C infrared thermometer (SMBus) — channels: 0 = object temperature [°C] (non-contact), 1 = ambient [°C]. Fixed address 0x5A. Bearings, contacts, moving parts. |
| `STS3X` | I2C | I2C temperature sensor (the SHT3x without the humidity cell) — channel 0 = temperature [°C]. Single shot with CRC. Address 0x4A–0x4B. |
| `STTS22H` | I2C | I2C temperature sensor (ST) — channel 0 = temperature [°C], 0.01 °C resolution, free-running 1 Hz. Address 0x38–0x3F by the ADDR pin. Written from the datasheet. Not yet tested on hardware. |
| `TC74` | I2C | I2C temperature sensor (single byte, 1 °C resolution) — channel 0 = temperature [°C]. Address 0x48–0x4F by suffix. |
| `TMP102` | I2C | I2C temperature sensor — channel 0 = temperature [°C], 12-bit 0.0625 °C resolution, address 0x48–0x4B. |
| `TMP117` | I2C | I2C precision temperature sensor ±0.1 °C — channel 0 = temperature [°C], 7.8125 m°C resolution, address 0x48–0x4B. |

### Thermocouple / RTD

| Chip | Bus | What it is |
|:---|:---:|:---|
| `KMETERISO` | I2C | I2C isolated K-thermocouple module (M5Stack KMeterISO) — channel 0 = temperature [°C]. Fixed address 0x66. Not yet tested on hardware. |
| `MAX31855` | SPI | SPI thermocouple converter (Maxim) — seven parts, one per thermocouple type (`tc_type` K, J, N, S, T, E or R, the suffix of the part number). Channels: 0 = thermocouple [°C] (0.25 °C steps), 1 = cold junction [°C] (0.0625 °C), 2 = fault (0 none, 1 open, 2 shorted to GND, 3 shorted to VCC; a fault keeps the temperature's last value). The chip assumes a straight-line thermocouple; `linearise: true` makes the device correct its reading with the standard's table and the cold junction. addr = CS pin. |
| `MAX31856` | SPI | SPI precision thermocouple converter with linearisation (Maxim) — channels: 0 = thermocouple [°C] (19 bits, 1/128 °C; millivolts in a voltage mode), 1 = cold junction [°C], 2 = the fault status byte (bit 7 cold junction out of range, 6 thermocouple out of range, 5 cold junction high, 4 low, 3 thermocouple high, 2 low, 1 over / under voltage, 0 open). Every register is a setting of the chip: `tc_type` B / E / J / K / N / R / S / T or mv8 / mv32, `average` 1–16, `filter` 50 / 60, `open_detect` off / low / mid / high (the thermocouple's resistance), `cj` (a variable feeding the cold junction when the chip's sensor is off), `cj_offset`, `fault_mode` comparator / interrupt, `cj_high` / `cj_low` / `tc_high` / `tc_low` in degrees, `fault_pin` (the faults that drive the FAULT pin), `mode` auto / one_shot with `period_ms`. addr = CS pin. |
| `MAX31865` | SPI | SPI RTD converter (Maxim) — channels: 0 = temperature [°C] (Callendar-Van Dusen, IEC 751), 1 = the fault status byte (bit 7 over the high threshold, 6 under the low, 5 REFIN- high, 4 REFIN- low, 3 RTDIN- low, 2 over / under voltage), 2 = the sensor's resistance [Ω]. Every register is a setting of the chip: the sensor (`rtd` pt100 / pt1000, an exact `r0`), the reference (`rref` in ohms), the wiring (`wires` 2 / 3 / 4), the filter (`filter` 50 / 60), the fault thresholds in degrees (`fault_high` / `fault_low` — the chip compares every conversion), the fault detection cycle at start-up (`fault_cycle` off / auto / manual with `filter_tc_us`), the conversion mode (`mode` auto / one_shot with `period_ms` — VBIAS off between). A sensor fault = a diag entry, the temperature keeps its last value. addr = CS pin. |
| `MAX6675` | SPI | SPI K-thermocouple converter (Maxim) — channels: 0 = temperature [°C] (0.25 °C steps, 0–1024 °C), 1 = open (1 while the thermocouple is open; the temperature keeps its last value). One frame, nothing to set; T- to GND for the open detection. addr = CS pin. |
| `MCP9600` | I2C | I2C thermocouple converter (K type by default) — channel 0 = hot-junction temperature [°C], 0.0625 °C steps. Address 0x60–0x67. |

Every entry above is in the editor: pick the chip, give it
an address or a chip-select pin, and its channels become variables.
See [Adding a peripheral](/docs/buses/adding-peripherals/) for the
click-through.
