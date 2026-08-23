# Board peripherals and system services

How the board works with the ADS1115 analog-to-digital converter, with
fitted retentive memory (FRAM/EEPROM) and with a real-time clock (RTC).
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
    deadband: 0.5     # mandatory on analog tags — filters noise
    unit: "°C"
```

- The **address** is 0x48–0x4B depending on the chip's ADDR pin;
  **range** is the full-scale range in volts (6.144 / 4.096 / 2.048 /
  1.024 / 0.512 / 0.256, 4.096 without the key). The raw value is
  16-bit signed; with single-ended wiring 0..32767.
- The channels are measured in turn, each one is refreshed within
  4 PLC cycles at the latest (40 ms with a 10 ms cycle).
- A disconnected or unfitted chip: one event in the diagnostics, the
  tags hold their last value, the board keeps running; once it is
  connected the chip comes back to life on its own.

## Retention — values that survive a power-down

Tags in the RVAR (retain) list are stored automatically according to
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
  the diagnostics. Values are never mixed up between variables.
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

- **Service cable**: the serial command `VUT!2026-08-09 14:32:05`,
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
in a real setup with a Simatic.
