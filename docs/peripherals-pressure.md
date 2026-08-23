# Pressure and position

Ten pressure sensors and six position sensors.

## Pressure

Two different jobs share the word.

**Barometric** — `BMP280`, `BMP581`, `MS5611`, `LPS22`, `MPL3115A2` —
measures air pressure: weather, altitude, or the drop across a filter.
Fine enough to see a few metres of altitude change.

**Process** — `HONEYWELLABP`, `HONEYWELLABP2`, `XGZP68XX`, `SDP3X` —
measures a fluid or a gas in a pipe or a duct, in the units a machine
cares about. `SDP3X` measures *differential* pressure, which is what a
filter monitor or an air-flow measurement actually needs.

| You are measuring | Reach for |
|---|---|
| weather, altitude | `BMP280`, `MS5611`, `MPL3115A2` |
| pressure and humidity together | `MS8607` |
| a pipe or a tank | `HONEYWELLABP`, `XGZP68XX` |
| the difference across a filter | `SDP3X` |
| hydraulics at industrial pressures | a 4–20 mA transmitter into an [analog input](peripherals-analog.md) |

!!! tip "Altitude from pressure needs a reference"
    Absolute pressure changes with the weather by more than it changes
    over several floors of a building. Altitude without a reference
    pressure drifts by tens of metres between a sunny day and a storm.

## Position

**Magnetic angle** — `AS5600` — reads the angle of a magnet on a shaft.
No contact, no wear, full-turn resolution. A good answer for a rotating
axis that does not need to count revolutions.

**Compass** — `HMC5883L`, `QMC5883L` — measures the earth's field, and
therefore heading. On a machine, more often used to detect a large steel
object moving nearby.

**Inertial** — `MPU6050`, `BMI160`, `LSM6DS` — accelerometer and
gyroscope together: tilt, and vibration.

!!! tip "Vibration is easier than orientation"
    Getting a stable angle out of an inertial sensor needs filtering and
    care. Noticing that vibration has doubled since last month needs
    almost none — and on a machine, that is usually the question worth
    asking. A bearing announces itself weeks before it fails.

!!! warning "A magnetic angle sensor cares where the magnet is"
    `AS5600` wants the magnet centred over the chip, at the distance the
    datasheet gives, with no steel nearby. A millimetre of offset becomes
    degrees of error — and the error varies through the turn, which makes
    it look like the mechanics are at fault.

    A compass in a steel enclosure measures the enclosure.

## The chips

### Pressure sensors

| Chip | Bus | What it is |
|---|---|---|
| `BMP085` | I2C | I2C barometer (BMP085/BMP180, integer datasheet compensation) — channels: 0 = pressure [hPa], 1 = temperature [°C]. Fixed address 0x77. |
| `BMP581` | I2C | I2C pressure + temperature sensor (Bosch, direct-reading — no compensation math) — channels: 0 = pressure [hPa], 1 = temperature [°C]. Address 0x46–0x47. VERIFY ON THE BENCH. |
| `HONEYWELLABP` | I2C | I2C board-mount pressure sensor (Honeywell ABP series) — channels: 0 = raw bridge counts (10–90 % of 2^14; the range is ordering-specific, engineering units via tag gain/offset), 1 = temperature [°C] (11-bit). The address is ordering-specific too — the check accepts 0x08–0x78. |
| `HONEYWELLABP2` | I2C | I2C micropressure sensor (Honeywell ABP2/MPR series) — channels: 0 = raw 24-bit counts (units via tag gain/offset), 1 = temperature [°C]. Command-triggered conversion; the address is ordering-specific — the check accepts 0x08–0x78. |
| `LPS22` | I2C | I2C pressure + temperature sensor (ST LPS22HB/HH) — channels: 0 = pressure [hPa], 1 = temperature [°C]. 1 Hz continuous. Address 0x5C–0x5D. |
| `MPL3115A2` | I2C | I2C barometer/altimeter (NXP) — channels: 0 = pressure [hPa], 1 = temperature [°C]. Barometer mode, OSR 128. Fixed address 0x60. |
| `MS5611` | I2C | I2C barometer (PROM coefficients + first-order datasheet compensation) — channels: 0 = pressure [hPa], 1 = temperature [°C]. Address 0x76–0x77. |
| `MS8607` | I2C | I2C PHT combo, the pressure/temperature die (MS5637-class compensation) — channels: 0 = pressure [hPa], 1 = temperature [°C]. The humidity die is a separate HTU21D at 0x40 — add it as its own peripheral. Fixed address 0x76. |
| `SDP3X` | I2C | I2C differential pressure sensor (Sensirion SDP3x) — channels: 0 = differential pressure [Pa] (the chip reports its own scale factor), 1 = temperature [°C]. Continuous measurement with averaging; address 0x21–0x23. Filter and duct monitoring. |
| `XGZP68XX` | I2C | I2C pressure sensor (CFSensor XGZP68xx modules) — channels: 0 = raw 24-bit counts (the K factor of the ordering goes into tag gain), 1 = temperature [°C]. Fixed address 0x6D. VERIFY ON THE BENCH. |

### Position sensors

| Chip | Bus | What it is |
|---|---|---|
| `AS5600` | I2C | I2C magnetic angle sensor (12-bit) — channels: 0 = raw angle counts 0–4095 (degrees via tag gain 360/4096), 1 = magnet detected (1/0). Fixed address 0x36 — a poor man's absolute encoder for slow axes and dampers. |
| `BMI160` | I2C | I2C accelerometer + gyroscope (Bosch) — channels: 0–2 = acceleration X/Y/Z [g], 3–5 = angular rate X/Y/Z [°/s], 6 = die temperature [°C]. Ranges ±2 g / ±2000 °/s. Address 0x68–0x69. |
| `HMC5883L` | I2C | I2C magnetometer (Honeywell classic) — channels: 0–2 = field X/Y/Z [gauss]. Fixed address 0x1E; continuous mode, ±1.3 G range. |
| `LSM6DS` | I2C | I2C accelerometer + gyroscope (ST LSM6DS3/DSO family) — channels: 0–2 = acceleration X/Y/Z [g], 3–5 = angular rate X/Y/Z [°/s], 6 = die temperature [°C]. Ranges ±2 g / ±250 °/s. Address 0x6A–0x6B. |
| `MPU6050` | I2C | I2C accelerometer + gyroscope — channels: 0–2 = acceleration X/Y/Z [g], 3–5 = angular rate X/Y/Z [°/s], 6 = die temperature [°C]. Ranges ±2 g / ±250 °/s. Address 0x68–0x69. Vibration and tilt monitoring. |
| `QMC5883L` | I2C | I2C magnetometer (the HMC5883L clone) — channels: 0–2 = field X/Y/Z [gauss]. Fixed address 0x0D; continuous mode, ±8 G range. |

Every entry above is in the editor: pick the chip, give it
an address or a chip-select pin, and its channels become tags.
See [Adding a peripheral](adding-peripherals.md) for the
click-through.
