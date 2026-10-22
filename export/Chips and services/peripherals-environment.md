---
title: "Environment"
slug: peripherals-environment
section: "Chips and services"
order: 319
sidebar_position: 319
generator: tools/docs_export.py
---

# Environment

Temperature, humidity and pressure — the sensors that tell you what the
air in a room, a cabinet or a greenhouse is doing.

Most measure several things at once, which is usually what you want:
humidity without temperature is nearly meaningless, and both together
cost less than apart.

## Choosing

| You need | Reach for |
|:---|:---:|
| temperature and humidity, indoors | `SHT31`, `SHT40`, `SHTC3`, `AHT20`, `HDC1080` |
| temperature, humidity **and** pressure | `BME280` — the classic three-in-one |
| the same plus air quality | `BME680` |
| the cheapest usable option | `DHT12`, `AM2320` |
| an industrial humidity probe | `HYT271` |
| air flow | `FS3000` |
| ionising radiation | `GDK101` |

`BME280` is on more boards than anything else here, and deservedly:
three measurements, one small part, an address that rarely collides.
Start there unless something says otherwise.

## The traps

!!! warning "Self-heating"
    A sensor next to a warm component reads the component, not the room.
    Humidity suffers worse than temperature: two degrees of self-heating
    throws relative humidity out by several percent.

    Keep it away from regulators, displays and anything that dissipates
    power — ideally on a little tongue of board with slots cut around it.

!!! warning "Condensation lies"
    A sensor that has been below the dew point reads high for a long time
    afterwards, sometimes permanently if the cell has been contaminated.
    Where condensation is likely, choose a sensor with a protective
    membrane and expect to replace it.

!!! tip "A pressure sensor needs to breathe"
    A sealed enclosure with a pressure sensor inside measures the
    enclosure, not the weather. Give it a vent, and put a filter in the
    vent.

## The chips

### Environmental sensors

| Chip | Bus | What it is |
|:---|:---:|:---|
| `AHT20` | I2C | I2C temperature + humidity sensor (Aosong) — channels: 0 = temperature [°C], 1 = humidity [%RH]. Fixed address 0x38; 80 ms conversion, CRC checked. |
| `AM2320` | I2C | I2C temperature + humidity sensor (Aosong, the wired DHT successor) — channels: 0 = temperature [°C], 1 = humidity [%RH]. Fixed address 0x5C; wake + read command, CRC16 checked; the first transaction after sleep is a wake-up NAK by design. |
| `BME280` | I2C | I2C environmental sensor — channels: 0 = temperature [°C], 1 = humidity [%RH], 2 = pressure [hPa]. Bosch datasheet compensation (calibration constants are read from the chip at startup). Normal mode, one sample every 250 ms. |
| `BME680` | I2C | I2C environmental sensor — channels: 0 = temperature [°C], 1 = humidity [%RH], 2 = pressure [hPa], 3 = gas resistance [Ω] (heater 300 °C / 100 ms, forced mode, 1 s poll). Datasheet float compensation. The gas channel is a RELATIVE air-quality signal that needs minutes after power-up — not a calibrated ppm. Address 0x76–0x77. |
| `BMP280` | I2C | I2C pressure + temperature sensor (BME280 without humidity) — channels: 0 = temperature [°C], 1 = pressure [hPa]. Bosch datasheet compensation, calibration read from the chip at startup. |
| `BMP388` | I2C | I2C barometer (also the BMP390 — chip id 0x50/0x60) — channels: 0 = pressure [hPa], 1 = temperature [°C]. Datasheet float compensation from the NVM coefficients. Address 0x76–0x77. |
| `DHT12` | I2C | I2C temperature + humidity sensor (the wired DHT11 heir) — channels: 0 = temperature [°C], 1 = humidity [%RH]. Fixed address 0x5C; 5-byte register read with a sum checksum. |
| `ENS210` | I2C | I2C temperature + humidity sensor (ScioSense) — channels: 0 = temperature [°C], 1 = humidity [%RH]. Continuous run, valid bits checked. Fixed address 0x43. |
| `FS3000` | I2C | I2C air velocity sensor — channel 0 = raw 12-bit counts (the m/s curve is nonlinear and ordering-specific; approximate via variable gain/offset). Fixed address 0x28. VERIFY ON THE BENCH. |
| `GDK101` | I2C | I2C gamma radiation sensor — channel 0 = dose rate [µSv/h] (10-minute average). Address 0x18–0x1B. VERIFY ON THE BENCH. |
| `HDC1080` | I2C | I2C temperature + humidity sensor (TI) — channels: 0 = temperature [°C], 1 = humidity [%RH]. Fixed address 0x40; both values in one sequential acquisition. |
| `HDC2010` | I2C | I2C temperature + humidity sensor (TI) — channels: 0 = temperature [°C], 1 = humidity [%RH]. Triggered measurement, little-endian data. Address 0x40–0x41. |
| `HTU21D` | I2C | I2C temperature + humidity sensor (also Si7021/SHT21 compatible) — channels: 0 = temperature [°C], 1 = humidity [%RH]. Fixed address 0x40; no-hold measurements alternate T/RH. |
| `HTU31D` | I2C | I2C temperature + humidity sensor (TE) — channels: 0 = temperature [°C], 1 = humidity [%RH]. Conversion command + 6-byte CRC frame. Address 0x40–0x41. |
| `HYT271` | I2C | I2C temperature + humidity sensor (B+B/IST industrial) — channels: 0 = temperature [°C], 1 = humidity [%RH]. Fixed address 0x28; measurement request + 4-byte data fetch. |
| `SHT31` | I2C | I2C temperature + humidity sensor (Sensirion) — channels: 0 = temperature [°C], 1 = humidity [%RH]. Single-shot high repeatability, CRC checked; a new measurement every cycle pass (~15 ms conversion). |
| `SHT40` | I2C | I2C temperature + humidity sensor (Sensirion, 4th gen) — channels: 0 = temperature [°C], 1 = humidity [%RH]. High precision command, CRC checked. |
| `SHTC3` | I2C | I2C temperature + humidity sensor (Sensirion SHTC3) — channels: 0 = temperature [°C], 1 = humidity [%RH]. Fixed address 0x70; wakeup + normal-mode measurement, CRC checked. |

### Water quality

| Chip | Bus | What it is |
|:---|:---:|:---|
| `EZO` | I2C | Atlas Scientific EZO probe circuit (pH/EC/DO/ORP/RTD...) — channel 0 = the probe value as the circuit reports it. ASCII R command with a ~900 ms conversion; one value a second. The I2C address is set per probe (default 0x61–0x67 by type). |

Every entry above is in the editor: pick the chip, give it
an address or a chip-select pin, and its channels become variables.
See [Adding a peripheral](/docs/buses/adding-peripherals/) for the
click-through.
