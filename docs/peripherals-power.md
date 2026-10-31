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
| mains energy, single phase, every register yours | `ATM90E26` |
| mains energy, single phase | `ADE7953` |
| a power converter with its own pulse output, every register yours | `CS5460A` |
| mains energy, three phase, every register yours | `ATM90E32` |
| battery state of charge | `MAX17043`, `MAX17044`, `LC709203F` |

`INA226` measures current through a shunt and voltage at the same time
and reports power directly. `INA3221` does three channels, which suits a
board watching its own supplies.

`ATM90E26` is a meter, not a sampler: it meters only once its two
register blocks have been written behind the chip's start commands,
and the device does that at every start-up with the words of your
project (or the chip's own power-on words when you have set nothing).
On the chip's page you type the hardware - the meter constant in
pulses per kWh, the reference voltage and basic current, the shunt or
current transformer of the L line, the transformer of the N line, the
voltage divider, the gains - the metering mode (the line, the
high-pass filters, what the CF1 / CF2 pulse pins count, the ZX pin,
the anti-tamper threshold), the startup and no-load thresholds, the
voltage sag with its pins, and the calibration from the bench (the
gain and angle errors of the two lines, the voltage and current
readings at the reference); every register's word is derived from
those numbers by the chip maker's own formulas and shown under the
fields, and the wiring picture draws the sensors on the chip's pins.
Its sixteen channels give the L line's voltage, current, active,
reactive and apparent power, power factor and phase angle, the line
frequency, the N line's current, powers and power factor, and the four
energies - forward and reverse, active and reactive - which accumulate
in their variables: make the variable retentive and the total survives
a restart.

`ATM90E32` is its three-phase brother and gets the same treatment: the
meter constant, the grid, the current sensor (a transformer or a Rogowski
coil), the wiring (four or three wires), what the CF2 pin counts, how
the totals are summed and which phases count, the PGA gain of every
channel, the startup thresholds in watts, the monitors - voltage sag,
phase loss, over-voltage, over-current, the frequency window, the
neutral current - with their periods, the three ZX pins, the interrupt
sources of IRQ0 and IRQ1, and the calibration per phase from the bench.
The device writes the configuration behind the chip's access gate at
every start-up and enables metering; the chip then guards its own
configuration with a CRC and raises WarnOut if it drifts. Thirty
channels: every phase's voltage, current, active and reactive power,
power factor and angle, the totals, the frequency, the calculated
neutral current, the chip's temperature and the five energies that
accumulate in their variables.

`CS5460A` is the Cirrus single-phase power converter: two 24-bit
channels for the voltage through a divider and the current through a
shunt or a transformer, the rms voltage and current, the mean active
power of a computation cycle, the apparent power and the power factor,
and the real energy that accumulates in its variable; the EOUT / EDIR
pulse output runs at the rate you set. On its page you type the
sensors (the device derives the full scales of the line from them),
the clock and its divider, the filters, the phase compensation in
degrees at your line frequency, the samples of a cycle, the pulse rate
and format, the INT pin and its events, and the words the chip's own
calibration commands produced on the bench - the gains, the offsets,
the time base. The device writes every register at start-up and starts
continuous computation cycles.

## Why measure current in a real setup

Current is the cheapest condition monitoring there is. A motor drawing
more than it did last month has a bearing going; one drawing less has
lost its load — a slipping belt, an empty hopper, a broken coupling.

None of that needs a special sensor. It needs current you can already
measure, a [trend](operation.md), and somebody looking at it
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
| `ATM90E26` | SPI | SPI single-phase energy meter (Atmel / Microchip) — the L line's voltage, current, active / reactive / apparent power, power factor and phase angle, the line frequency, the N line's current, powers and power factor, and the four energies (forward / reverse, active / reactive) in kWh / kvarh that accumulate in their variables (a retentive variable keeps the total). Every register is a setting of the chip: the meter constant, the reference voltage and basic current, the shunt or CT of the L line and the CT of the N line, the voltage divider, the gains, the metering mode, the startup and no-load thresholds, the voltage sag, and the bench's calibration errors - the device writes them behind the chip's start commands at start-up. addr = CS pin. |
| `ATM90E32` | SPI | SPI three-phase energy meter (Atmel / Microchip) — the three phases' voltage, current, active and reactive power, power factor and phase angle, the totals of active, reactive and apparent power and power factor, the line frequency, the calculated neutral current, the chip's temperature, and the five energies (forward / reverse active, forward / reverse reactive, apparent) in kWh / kvarh / kVAh that accumulate in their variables (a retentive variable keeps the total). Every configuration register is a setting of the chip: the meter constant, the grid, the PGA gains, the metering method, the startup thresholds in watts, the sag / phase-loss / over-voltage / over-current / frequency monitors, the ZX pins, the interrupt sources and the bench's calibration per phase - the device writes them behind the chip's access gate at start-up. addr = CS pin. |
| `CS5460A` | SPI | SPI single-phase power / energy converter (Cirrus Logic) - two 24-bit channels for the line's voltage (a divider) and current (a shunt or a CT, the PGA x10 or x50), the rms voltage and current, the mean active power of a computation cycle, the apparent power and power factor, and the real energy in kWh that accumulates in its variable (a retentive variable keeps the total); the EOUT / EDIR pulse output at the project's rate. Every register is a setting of the chip: the sensors, the clock and its divider, the filters, the phase compensation, the cycle count, the pulse rate and format, the interrupt, the chip's own calibration words. addr = CS pin. |

### Battery gauges

| Chip | Bus | What it is |
|:---|:---:|:---|
| `LC709203F` | I2C | I2C LiPo fuel gauge (ON Semi) — channels: 0 = cell voltage [V], 1 = state of charge [%]. Fixed address 0x0B; commands carry a CRC-8 PEC. VERIFY ON THE BENCH. |
| `MAX17043` | I2C | I2C single-cell Li+ fuel gauge (Maxim) — channels: 0 = cell voltage [V] (1.25 mV a count, 0–5 V), 1 = state of charge [%], 2 = alert (1 while the charge fell below the threshold). Every register is a setting of the chip: `rcomp` (the compensation byte of CONFIG, 97h at power-up), `alert` (the threshold 1–32 %; the ALRT pin goes low under it), `quick_start` (the gauge restarts its first guess at start-up), `sleep` (a BOOL variable whose 1 halts the gauge). Fixed address 0x36 (collides with the AS5600 — one bus carries only one of them). |
| `MAX17044` | I2C | I2C two-cell (2S) Li+ fuel gauge (Maxim, the MAX17043's sibling) — channels: 0 = pack voltage [V] (2.5 mV a count, 0–10 V), 1 = state of charge [%], 2 = alert. The same settings as the MAX17043. Fixed address 0x36. |

Every entry above is in the editor: pick the chip, give it
an address or a chip-select pin, and its channels become variables.
See [Adding a peripheral](adding-peripherals.md) for the
click-through.
