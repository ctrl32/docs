# Light, distance and motion

Twelve light sensors, a distance sensor and a magnetic field sensor.

## Light

Three quite different things share the name:

**Ambient light** — `BH1750`, `TSL2591`, `VEML7700`, `OPT3001`,
`MAX44009` — gives you lux, how bright it is where the sensor sits. Use
it to dim a display, switch lighting, or notice that an enclosure is
open.

**Colour** — `TCS34725`, `APDS9960` — separates light into channels. Use
it to tell one coloured part from another, or to check that a label is
the right shade. `APDS9960` also detects a hand waved in front of it,
which makes a touch-free control for somebody wearing gloves.

**Ultraviolet** — `LTR390` — measures what you cannot see: sunlight
exposure, or whether a UV lamp is actually lit.

### Choosing an ambient light sensor

| | |
|:---|:---:|
| the standard choice | `BH1750` — cheap, simple, well behaved |
| very wide range (dark room to full sun) | `TSL2591`, `VEML7700` |
| accuracy matched to the human eye | `OPT3001` |
| very low power | `MAX44009` |

!!! tip "Lux covers an enormous range"
    Moonlight is about 0.1 lux, an office 500, direct sun 100 000. A
    sensor with a narrow range saturates outdoors and reads zero in a dim
    room. If it might see both, pick one with the range for it rather
    than scaling afterwards.

## Distance

`TOF10120` measures time of flight — it sends an infrared pulse and times
the echo. Good from a few centimetres to about a metre.

!!! warning "It measures the first thing it sees"
    A shiny surface at an angle reflects the pulse away and reads as
    "far". Dust on the window reads as "very close". Both fail in the
    direction that looks plausible, which is why a distance reading
    driving anything important wants a sanity check around it.

## Magnetic field

`MLX90393` measures a magnetic field in three axes. On a setup that
usually means proximity without contact — a magnet on a moving part, and
a sensor that never wears out because nothing touches it.

For a shaft *angle*, see the magnetic angle sensors under
[Position](peripherals-pressure.md).

## The chips

### Light sensors

| Chip | Bus | What it is |
|:---|:---:|:---|
| `APDS9306` | I2C | I2C ambient light sensor — channel 0 = RAW 18-bit ALS counts at gain 3 / 100 ms; scale to lux with the tag gain (the counts-per-lux responsivity is variant-dependent — VERIFY ON THE BENCH). Address 0x52. |
| `APDS9960` | I2C | I2C light + proximity sensor — channels: 0 = clear-channel ALS counts (raw), 1 = proximity counts 0–255. The gesture engine is not used. Address 0x39. |
| `BH1750` | I2C | I2C ambient light sensor — channel 0 = illuminance [lx]. Valid addresses are ONLY 0x23 (ADDR to GND) and 0x5C (ADDR to VCC) — the checked range is wider, in-between addresses do not exist. Continuous high-resolution mode (1 lx, 120 ms). |
| `LTR303` | I2C | I2C ambient light sensor (LTR-303/LTR-329; also the ALS half of the LTR-553) — channel 0 = illuminance [lx] (Lite-On appendix ratio formula, gain x1 / 100 ms). Address 0x29. |
| `LTR390` | I2C | I2C UV sensor — channel 0 = UV index (18-bit, gain x18 typical sensitivity). Fixed address 0x53. VERIFY ON THE BENCH. |
| `LTR501` | I2C | I2C light + proximity sensor — channels: 0 = illuminance [lx] (Lite-On appendix ratio formula at gain x1), 1 = proximity counts (11-bit). Address 0x23. VERIFY ON THE BENCH. |
| `MAX44009` | I2C | I2C ambient light sensor with a 22-bit dynamic range — channel 0 = illuminance [lx] (exponent + mantissa format). Address 0x4A–0x4B. |
| `OPT3001` | I2C | I2C ambient light sensor — channel 0 = illuminance [lx], continuous 800 ms conversions. Address 0x44–0x47. |
| `TCS34725` | I2C | I2C color sensor — channels: 0 = clear, 1 = red, 2 = green, 3 = blue (raw counts, ~101 ms integration). Fixed address 0x29. |
| `TSL2561` | I2C | I2C ambient light sensor, two diodes — channel 0 = illuminance [lx] (datasheet piecewise formula, T package). Valid addresses are ONLY 0x29 / 0x39 / 0x49 (ADDR pin low / float / high) — the checked range is wider. |
| `TSL2591` | I2C | I2C ambient light sensor (high dynamic range) — channel 0 = illuminance [lx] (approximate datasheet formula, medium gain 100 ms). Fixed address 0x29. VERIFY ON THE BENCH. |
| `VEML7700` | I2C | I2C ambient light sensor — channel 0 = illuminance [lx] (gain x1, 100 ms integration). Fixed address 0x10. |

### Distance sensors

| Chip | Bus | What it is |
|:---|:---:|:---|
| `TOF10120` | I2C | I2C laser distance sensor — channel 0 = distance [mm] (filtered register). Fixed address 0x52. VERIFY ON THE BENCH. |

### IMU / motion

| Chip | Bus | What it is |
|:---|:---:|:---|
| `MLX90393` | I2C | I2C 3-axis magnetometer — channels: 0-2 = field X/Y/Z [µT] (POR gain: 0.150 µT/LSB xy, 0.242 z), 3 = die temperature [°C]. Command protocol — SM and RM split across cycles. Address 0x0C–0x0F. VERIFY ON THE BENCH. |

Every entry above is in the editor: pick the chip, give it
an address or a chip-select pin, and its channels become tags.
See [Adding a peripheral](adding-peripherals.md) for the
click-through.
