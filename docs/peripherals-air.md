# Air quality

Fourteen sensors for CO₂, volatile compounds, particulates and gases.

These are the least straightforward parts in the catalogue, and it is
worth knowing why before choosing: most of them do not measure what their
label suggests. They measure something correlated with it, and the
correlation is only as good as the calibration behind it.

## Real CO₂ or estimated CO₂

**True NDIR sensors** — `SCD30`, `SCD41` — measure carbon dioxide
optically. They are bigger, slower and dearer, and their number means
what it says.

**eCO₂ sensors** — `CCS811`, `ENS160`, `SGP30`, `IAQCORE` — measure
volatile compounds and *estimate* CO₂ from them. Breathe on one and it
rises; open a tin of solvent nearby and it rises just as much. For "is
this room stuffy" that is fine. For ventilation that must hold CO₂ below
a limit, it is not.

If somebody is going to read the number as parts per million of CO₂, pay
for NDIR.

## Choosing

| You need | Reach for |
|---|---|
| CO₂ you can defend | `SCD41`, `SCD30` |
| a cheap "the air is stale" signal | `ENS160`, `SGP4X`, `CCS811` |
| particulates (PM2.5, PM10) | `PMSA003I`, `SPS30`, `SEN5X`, `HM3301` |
| formaldehyde | `SFA30` |
| ozone | `SEN0321` |
| a general air-quality index | `ENS160`, `SGP4X` |

`SEN5X` is worth singling out: particulates, VOC, temperature and
humidity in one module, which saves both board space and the
cross-compensation work below.

## The traps

!!! warning "They need burning in, then re-baselining"
    Most gas sensors read badly for the first hours or days of their
    life. Several also expect to see clean air regularly so they can
    re-baseline — a sensor that never sees fresh air drifts.

    Put the sensor where fresh air reaches it sometimes, and do not trust
    the first day's readings.

!!! warning "Temperature and humidity change the answer"
    Every gas sensor is sensitive to both. Modules with their own
    temperature and humidity cell compensate themselves; the ones without
    need you to feed them values, or they drift with the weather.

!!! danger "None of these are safety instruments"
    A sensor saying the air is breathable is not a gas detector and must
    never be used as one. Life-safety detection uses certified
    instruments with their own alarms, tested to a standard — not a
    breakout board on an I2C bus.

## The chips

### Air quality

| Chip | Bus | What it is |
|---|---|---|
| `AGS10` | I2C | I2C TVOC sensor (ASAIR) — channel 0 = TVOC [ppb]. The chip refreshes every ~1.5 s and the driver polls every 2 s; CRC checked. Fixed address 0x1A. VERIFY ON THE BENCH. |
| `CCS811` | I2C | I2C air quality sensor — channels: 0 = eCO2 [ppm], 1 = TVOC [ppb]; drive mode 1 s. Needs ~20 min burn-in after power-up before the values mean anything. Address 0x5A–0x5B. |
| `ENS160` | I2C | I2C air quality sensor (ScioSense) — channels: 0 = eCO2 [ppm], 1 = TVOC [ppb], 2 = AQI index 1–5. Standard operating mode; the first minutes after power-up are warm-up. Address 0x52–0x53. |
| `HM3301` | I2C | I2C particulate matter sensor (Seeed/Tomoto) — channels: 0 = PM1.0, 1 = PM2.5, 2 = PM10 [µg/m³] (atmospheric). 29-byte frame with a sum checksum. Fixed address 0x40. |
| `IAQCORE` | I2C | I2C VOC sensor (ams iAQ-core) — channels: 0 = eCO2 [ppm], 1 = TVOC [ppb]. Plain 9-byte read; samples with a non-zero status (warm-up, drift) are dropped. Fixed address 0x5A. |
| `PMSA003I` | I2C | I2C particulate matter sensor (Plantower) — channels: 0 = PM1.0, 1 = PM2.5, 2 = PM10 [µg/m³] (atmospheric values). Fixed address 0x12; 32-byte frame with checksum. |
| `SCD30` | I2C | I2C CO2 sensor (Sensirion NDIR, the SCD41 predecessor) — channels: 0 = CO2 [ppm], 1 = temperature [°C], 2 = humidity [%RH]. Fixed address 0x61; continuous measurement every 2 s, float values, CRC checked. |
| `SCD41` | I2C | I2C CO2 sensor (Sensirion NDIR) — channels: 0 = CO2 [ppm], 1 = temperature [°C], 2 = humidity [%RH]. Fixed address 0x62; periodic measurement, a fresh value every ~5 s, CRC checked. |
| `SEN0321` | I2C | I2C ozone sensor (DFRobot Gravity) — channel 0 = O3 [ppb], automatic mode, 1 s poll. Register map from the vendor wiki. Address 0x70–0x73 (DIP switches). VERIFY ON THE BENCH. |
| `SEN5X` | I2C | I2C environmental node (Sensirion SEN54/55) — channels: 0–3 = PM1.0/2.5/4.0/10 [µg/m³], 4 = humidity [%RH], 5 = temperature [°C], 6 = VOC index, 7 = NOx index (SEN55; 0 elsewhere). Fixed address 0x69. |
| `SFA30` | I2C | I2C formaldehyde sensor (Sensirion) — channels: 0 = HCHO [ppb], 1 = humidity [%RH], 2 = temperature [°C]. Continuous measurement, CRC checked. Fixed address 0x5D. |
| `SGP30` | I2C | I2C VOC air quality sensor — channels: 0 = eCO2 [ppm], 1 = TVOC [ppb]. Fixed address 0x58; 1 Hz measurement, CRC checked. The first ~15 s after power-up report the fixed 400/0 warm-up values; baseline persistence is not stored. |
| `SGP4X` | I2C | I2C VOC sensor (SGP40/41) — channel 0 = RAW resistance counts (the Sensirion VOC-index algorithm is not in the firmware; trends via tag gain/offset). Fixed address 0x59. |
| `SPS30` | I2C | I2C particulate matter sensor (Sensirion) — channels: 0 = PM1.0, 1 = PM2.5, 2 = PM4.0, 3 = PM10 [µg/m³]. Fixed address 0x69; integer output format, CRC checked. VERIFY ON THE BENCH. |

Every entry above is in the editor: pick the chip, give it
an address or a chip-select pin, and its channels become tags.
See [Adding a peripheral](adding-peripherals.md) for the
click-through.
