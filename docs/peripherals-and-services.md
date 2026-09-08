# Chips and services

How the board works with the ADS1115 analog-to-digital converter, with
fitted retentive memory (FRAM/EEPROM), with a real-time clock (RTC) —
and the services that run on the board's own pins: 1-Wire
thermometers, a quadrature encoder, PWM outputs, NeoPixel strips, an
IR remote, a cellular modem and a GPS receiver.
Technical background: `specs/007-peripherals-services/`.

## ADS1115 — analog inputs (project peripheral)

You connect the converter to the I2C header of the board and add it in
the editor as a peripheral (exactly like the TCA9555 expander) — the
procedure is shown in the clip
[Adding peripherals to a board](adding-peripherals.md):

```yaml
peripherals:
  - { type: ADS1115, name: adc1, bus: i2c, addr: 0x48, range: 4.096 }
tags:
  - name: temperature
    datatype: f32
    source: { periph: { chip: adc1, pin: 0 } }   # pin = channel AIN0..3
    gain: 0.0125      # raw value -> physical units
    offset: -40.0
    deadband: 0.5     # mandatory on analog variables — filters noise
    unit: "°C"
```

- The **address** is 0x48–0x4B depending on the chip's ADDR pin;
  **range** is the full-scale range in volts (6.144 / 4.096 / 2.048 /
  1.024 / 0.512 / 0.256, 4.096 without the key). The raw value is
  16-bit signed; with single-ended wiring 0..32767.
- The channels are measured in turn, each one is refreshed within
  4 PLC cycles at the latest (40 ms with a 10 ms cycle).
- A disconnected or unfitted chip: one event in the diagnostics, the
  variables hold their last value, the board keeps running; once it is
  connected the chip comes back to life on its own.

## Retention — values that survive a power-down

Variables in the RVAR (retain) list are stored automatically according to
what the board has fitted — **nothing is configured**:

| The board has | Behaviour |
|:---|:---|
| FRAM | changes are stored within 1 s; no write-count limit |
| EEPROM | changes are stored within 5 minutes at the latest (to preserve chip life — even with a permanently changing value it lasts > 9 years) |
| nothing | internal flash (NVS), stored within 10 s — the original behaviour |

- The image in memory is protected by a checksum in two alternating
  copies — a power failure in the middle of a write can never corrupt
  both; after startup the last complete state applies.
- Changing the list of retain variables (a different project/version)
  means the variables start from their initial values plus an entry in
  the diagnostics. Values are never mixed up between variables: every
  stored value is keyed by the variable's **name and type**, so a new
  project reusing an old name with a different type starts from its
  initial value (with a diagnostics entry) instead of loading foreign
  bits.
- If the board catalog declares memory but the chip does not answer,
  the board reports it and falls back to NVS — retention never stops
  working.
- Capacity: 64 retain variables (NVS: 16).

**For frequently changing values (piece counters updated every cycle)
FRAM is the right choice** — EEPROM only stores them once every
5 minutes.

## Real time (RTC)

A board with a PCF8563 fitted (battery-backed) knows the date and time
even after a power-down. Alarms and diagnostics then carry the real
time.

Setting the time:

- **Service cable**: the serial command `VUT!YYYY-MM-DD hh:mm:ss`,
  typed into any terminal on the board's COM port.
- **NTP**: a board with network access and NTP configured in the
  project sets itself, and keeps itself set.
- **WEBview**: the "Set board time" button in the status bar — it takes
  the time from the phone/PC. The button only appears on boards that
  support setting the time.

States (`VUT!` prints `source=` and `state=`):

- `rtc / ok` — the time runs from the RTC chip and survives a
  power-down
- `sys / none|invalid` — there is no RTC (or its battery is flat):
  the time is valid until power-down, after a restart it begins at
  2000-01-01; a flat battery is reported by the diagnostics

The time is **local** — the board does not deal with time zones or
daylight saving; at the changeover set the time the same way you would
in a real setup.

---

## Services on the board's own pins

Each of these is a device-tree page in the editor: right-click the
board (or the matching bus node) and add it. The configuration travels
in the project — changing pins or bindings never means new firmware.

### 1-Wire (DS18B20 thermometers)

One bus on a free GPIO, up to **8 DS18B20** temperature sensors. Each
sensor is identified by its ROM code, so swapping wiring order changes
nothing. With the board connected, **Scan bus** discovers the fitted
sensors from the panel and binds them to variables (°C) — the cheapest
way to get many temperatures over tens of metres of cable.

### Encoder (quadrature)

An incremental encoder wired straight into the panel — the hardware
PCNT counter on free GPIO pins, so this is the low-latency position
path (no bus delay). A, B and optional Z/index pins, counting mode and
direction invert; counts land in a position variable (and optionally a
velocity variable in counts/s), engineering units come from the
variable's gain/offset.

### PWM outputs

Up to **4 outputs** (the chip's LEDC hardware). The duty comes from
the bound variable in percent 0–100; frequency 100 Hz – 40 kHz per
output. Slow PWM for SSR heaters belongs in ST logic, not here — a
relay cycling in seconds is logic, not a waveform.

### NeoPixel (WS2812)

Up to **4 strips of 16 LEDs**. Every LED binds three variables R, G, B
(0–255) created as one consecutive block — the **Create VARs** button
makes them all at once, and the logic or a screen then paints lights
by writing plain numbers.

### IR remote

A TSOP receiver and an IR LED on free GPIOs. **Learn** captures a
button from any remote (NEC is decoded; anything else is stored as raw
timing) and each learned key pulses its bool variable on receive —
a hand-held remote becomes a set of inputs. The
[IR_SEND block](blocks-services.md) transmits a table entry by index.

### Cellular modem (SMS and mobile data)

SMS alarms and mobile data over an AT modem on the spare UART
(Adrastea-I, EC25, SIM7000G/7080G, SIM800L). RX/TX are the panel's
pins — wire them **crossed** to the module (panel RX to module TX).
The message table holds up to 8 texts; the
[SMS_SEND and GSM_INFO blocks](blocks-services.md) use them from the
logic. The service reports its state in a status variable: 0 = no
modem, 1 = searching network, 2 = ready, 3 = SMS sent. Modem chips and
antenna notes: [Cellular modems](peripherals-connectivity.md).

### GPS receiver

An NMEA receiver on the spare UART writes position, speed and
satellite count into variables once a second, and can also **set the
panel clock** — an installation without any network gets real time.
The modem and the GPS share the one spare UART: a project carries one
or the other, not both.

### Memory (EEPROM/FRAM viewer)

A service page for commissioning: it reads the raw content of the
board's retain memory live from the panel. The retain image occupies
two A/B copies at the start; the rest is free. On a board with no
memory chip the retain data lives in NVS (flash) and there is no raw
chip to browse.
