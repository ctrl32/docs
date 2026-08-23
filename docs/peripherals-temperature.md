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

## The chips

### Temperature sensors

| Chip | Bus | What it is |
|:---|:---:|:---|
| `LM75B` | I2C | I2C temperature sensor (industry classic) — channel 0 = temperature [°C], 11-bit 0.125 °C resolution, address 0x48–0x4F. Collides with TMP102 addresses — packbuild watches the bus. |
| `MCP9808` | I2C | I2C precision temperature sensor ±0.25 °C — channel 0 = temperature [°C], 0.0625 °C resolution, address 0x18–0x1F. |
| `MLX90614` | I2C | I2C infrared thermometer (SMBus) — channels: 0 = object temperature [°C] (non-contact), 1 = ambient [°C]. Fixed address 0x5A. Bearings, contacts, moving parts. |
| `STS3X` | I2C | I2C temperature sensor (the SHT3x without the humidity cell) — channel 0 = temperature [°C]. Single shot with CRC. Address 0x4A–0x4B. |
| `STTS22H` | I2C | I2C temperature sensor (ST) — channel 0 = temperature [°C], 0.01 °C resolution, free-running 1 Hz. Address 0x38–0x3F by the ADDR pin. VERIFY ON THE BENCH (control register written from the datasheet, not tried on silicon). |
| `TC74` | I2C | I2C temperature sensor (single byte, 1 °C resolution) — channel 0 = temperature [°C]. Address 0x48–0x4F by suffix. |
| `TMP102` | I2C | I2C temperature sensor — channel 0 = temperature [°C], 12-bit 0.0625 °C resolution, address 0x48–0x4B. |
| `TMP117` | I2C | I2C precision temperature sensor ±0.1 °C — channel 0 = temperature [°C], 7.8125 m°C resolution, address 0x48–0x4B. |

### Thermocouple / RTD

| Chip | Bus | What it is |
|:---|:---:|:---|
| `KMETERISO` | I2C | I2C isolated K-thermocouple module (M5Stack KMeterISO) — channel 0 = temperature [°C]. Fixed address 0x66. VERIFY ON THE BENCH. |
| `MAX31855` | SPI | SPI K-thermocouple converter — channels: 0 = thermocouple [°C] (0.25 °C steps), 1 = cold junction [°C]. Fault bits (open/short) drop the sample and log a diag entry. addr = CS pin. |
| `MAX31856` | SPI | SPI precision thermocouple converter (K type configured) — channels: 0 = thermocouple [°C] (19-bit, 0.0078 °C), 1 = cold junction [°C]. Fault register checked. addr = CS pin. |
| `MAX31865` | SPI | SPI RTD converter (PT100/PT1000) — °C straight into the tag. addr = CS pin. PeriphRec.config: bit0 = 3-wire, bit2 = 60 Hz filter (default 50 Hz), bit3 = PT1000, bits 4+ = Rref in tens of ohms (0 = 430 Ω for PT100 / 4300 Ω for PT1000 — common boards). Calibration via tag gain/offset; sensor fault = diag entry and the tag keeps its last value. |
| `MAX6675` | SPI | SPI K-thermocouple converter — channel 0 = temperature [°C], 0.25 °C steps, open-thermocouple detection. addr = CS pin. |
| `MCP9600` | I2C | I2C thermocouple converter (K type by default) — channel 0 = hot-junction temperature [°C], 0.0625 °C steps. Address 0x60–0x67. |

Every entry above is in the editor: pick the chip, give it
an address or a chip-select pin, and its channels become tags.
See [Adding a peripheral](adding-peripherals.md) for the
click-through.
