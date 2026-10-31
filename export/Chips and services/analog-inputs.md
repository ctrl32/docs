---
title: "Reading real values"
slug: analog-inputs
section: "Chips and services"
order: 329
sidebar_position: 329
image: img/analog-current.webp
image_alt: "The sensor sheet of a 4-20 mA channel: the shunt, the range, what it means, and what the variable would hold"
generator: tools/docs_export.py
---

# Analog inputs that read real values

A converter measures **volts**. A pressure transmitter, a level
sensor, a thermistor and a Pt1000 all end up as volts on a pin, and
what those volts MEAN is a property of what is wired there — not of
the converter.

So a channel says what is wired to it, and the device does the
arithmetic. The variable holds **bar**, **percent**, **degrees** —
everywhere it is read: the screen, the browser, the logic, the trend,
OPC UA, Modbus, MQTT.

![The sheet of a 4-20 mA channel: the shunt, the range in milliamps, what it means in bar, and the line that says what a reading would become](img/analog-current.webp){: .sb-center}

---

## What you can pick

| Sensor | What you enter | What the variable holds |
|:---|:---|:---|
| **0-10 V / 0-5 V** through a divider | the divider, and what the range means | your unit |
| **4-20 mA / 0-20 mA** through a shunt | the shunt in ohms, and the range | your unit |
| **NTC thermistor** | the reference resistor and supply, R25 and B | °C |
| **NTC, Steinhart-Hart** | the same, with the three coefficients | °C |
| **Pt100 / Pt1000** | the reference resistor and supply | °C |
| **Ni1000** (DIN 43760) / **Ni1000 TK5000** (Landis+Gyr) | the reference resistor and supply | °C |
| **RTD excited by the converter** (`ADS1220`, `ADS122S14`, `ADS124S08`) — Pt100, Pt1000, Ni1000 in 2, 3 or 4 wires | R at 0 °C, the curve, the wires, the reference resistor | °C |
| **Thermocouple** (`ADS1220`, `ADS122S14`, `ADS124S08`) — K, J, T, E, N, S, R, B | the type, and where the cold junction comes from | °C |
| **Weight** (`ADS1220`, `ADS122S14`, `ADS124S08`) — a strain-gauge bridge: a load cell, a pressure cell | mV/V and the capacity off the cell's label; a tare variable | the capacity's unit |
| **Raw** | gain and offset, as before | whatever you compute |

Every type arrives with the **usual numbers already filled in** — a
165 Ω shunt, a 10 kΩ reference, 3.3 V — and every one of them can be
overwritten, because the next board is not the last one.

---

## Where it is

On the variable's own sheet, under its source. It appears for every
input that measures volts: a converter's channel (ADS1115, ADS1118,
ADS1220) and the board's own ADC alike. Under the numbers the sheet
**draws the wiring** of the type you picked — the converter's pins,
the sensor, the reference resistor, the currents — from the values
you typed, so the picture on the screen is the one to build.

Pick the sensor, check the numbers, and read the last line:

!!! tip "The editor tells you what a reading would be"
    Type a voltage into **If the pin read** and the line beside it
    says what the variable would hold. It is the device's own
    arithmetic answering — the same function the runtime runs — so a
    divider wired upside down shows up at your desk instead of on a
    commissioning day.

![A thermistor channel: the divider it sits in, R25 and B off its datasheet, and 1.65 V reading 25.00 °C](img/analog-ntc.webp){: .sb-center}

---

## The wiring each type expects

**A voltage sensor** goes through a divider, because a 10 V signal
does not belong on a 3.3 V pin. The **divider** number is how many
times bigger the sensor's voltage is than the pin's: a 10 kΩ / 3.3 kΩ
pair is about 4.

**A current loop** goes through a **shunt** — the resistor the loop's
current flows through. 165 Ω turns 4-20 mA into 0.66-3.3 V, which is
inside every converter we ship. The range is in milliamps and what it
means is in your own unit.

**A thermistor or an RTD** is a resistance, so it sits in a divider
with a known **reference resistor** and **supply**. Which half it
sits in is a tick box: *the sensor goes to ground* (the reference
pulls up) or the other way round.

!!! note "Where the numbers come from"
    R25 and B are on the thermistor's datasheet; a Pt100 is 100 Ω at
    zero degrees and a Pt1000 is 1000 Ω. Nothing here has to be
    measured — it is all printed on the part or its box.

---

## Thermocouples, three-wire RTDs and load cells: the ADS1220 family

The `ADS1220` is the converter of the industrial analog input card:
24 bits, a gain up to 128, two matched excitation currents, four
reference choices and its own temperature sensor. The `ADS122S14` is
the newer part of the same family: eight inputs, a gain from 0.5 to
256, currents up to 1 mA on any input, an internal 1.25 or 2.5 V
reference or an external one on AIN4/AIN5, four speed modes, global
chop and three burn-out currents. The `ADS124S08` is the biggest:
twelve inputs and a common one, currents up to 2 mA, two external
reference pairs beside the internal 2.5 V, a sensor bias that holds a
floating thermocouple at mid-supply, and monitors that flag a low
reference or an amplifier at its rail so a broken lead is a refused
reading, never a number. On the channels of any of the three the
same three more types appear:

**An RTD excited by the converter.** No divider: the chip's own
current (10 µA to 1.5 mA) flows through the sensor and through a
**reference resistor**, and the reading is the ratio of the two —
the supply drops out of the arithmetic. Three wires put the second
current through the third wire so the leads cancel; two wires let you
enter the lead resistance; four wires sense straight across the
sensor. The curve is platinum (IEC 60751), nickel (DIN 43760) or the
Landis+Gyr nickel (TK5000, 1500 Ω at 100 °C).

**A thermocouple.** Pick the letter — K, J, T, E, N, S, R or B — and
where the **cold junction** comes from: the converter's own
temperature sensor (the usual choice, when the terminals sit on the
converter's board), a fixed temperature, or another variable (a
sensor at the terminals). The device holds the reference tables of
the standard in both directions; the variable holds the junction's
temperature in °C. A reading beyond the type's table is refused.

**Weight.** A strain-gauge bridge — a load cell, a pressure cell —
excited from the converter's supply and read against it, so the
supply drops out again. Enter the **sensitivity** in mV/V and the
**capacity** off the cell's label; name a BOOL variable as the
**tare** and its rising edge takes the current reading as zero.

!!! tip "Every register of the converter is yours"
    The sheet shows the chip's own settings under the sensor: the
    input pair, the gain, the data rate and mode, the 50/60 Hz
    filter, the reference, the excitation current and where each of
    the two currents goes, the burn-out sources that turn an open
    sensor into a refused reading, the low-side power switch. On the
    `ADS122S14` the block has that chip's fields: the two input pins,
    the speed mode and rate, global chop, the start delay, the
    reference with its buffers, the burn-out current, the current
    unit and the two currents with their pins. On the `ADS124S08`:
    the two input pins (AINCOM among them), the gain with the
    amplifier's bypass, the sinc3 or low-latency filter and the rate,
    global chop and the start delay, the reference pair with its
    buffers, the external reference's volts where the measurement is
    not ratiometric, the reference monitor, the burn-out current, the
    excitation current with its two pins, the sensor bias and the
    pins it reaches, the low-side power switch and the rail monitor.
    Every type fills in its usual values; tick *Set the registers
    myself* to change them, and the sheet says in red what the
    datasheet would refuse (a single-ended input with the amplifier
    in the path, the 50/60 Hz filter above 20 samples a second, the
    burn-out sources in global-chop mode, a gain on a bypassed
    amplifier). The converter's own temperature, supply and reference
    go into variables you name on the chip (`temp`, `supply`,
    `reference`).

Under the settings the sheet **draws the wiring** from the numbers
you typed: the sensor, the divider or shunt, the reference resistor,
the excitation currents and the converter's pins they go to, the
bridge and its excitation, the junction of a thermocouple; on the
right of the converter its bus pins with the GPIO numbers the project
or the board gives them, and on an I2C converter the ADDR pin's tie
for the address and the ALERT/RDY pin's use. Change a number and the
picture follows.

The `ADS1115` and `ADS1015` have a register block of their own under
the sensor: the input (a pin against ground or a pair), the range, the
rate, and the **ALERT/RDY pin** - off, a comparator (asserts above
High, releases below Low), a window (asserts outside Low .. High) or
the conversion-ready output, with its polarity, its latch and the
number of readings beyond a threshold it waits for; Low and High are
volts at the input. A loop that leaves its window raises the pin
without the program's help.

---

## A broken loop is not a low reading

A 4-20 mA sensor that reads 0 mA is not at its zero point: its loop is
broken, or nothing is connected. Left alone, that would arrive as a
large negative pressure and look like real data.

With **a reading outside the range is a fault** ticked — the default
for 4-20 mA — such a reading is refused: the variable keeps the value
it had, and the reason goes into the diagnostic buffer once. The same
happens to a resistance sensor whose input sits at either supply rail,
which is what a cut or shorted wire looks like.

!!! warning "Stale, not wrong"
    A refused reading leaves the last good value in place. That is
    deliberate: on a machine a wrong number is worse than an old one.
    If it matters, watch the value for movement — or put the sensor's
    own fault signal on a second input.

---

## The example

`examples\analog_inputs.prj32` is the whole thing on one screen: a
4-20 mA pressure transmitter, a 0-10 V level sensor, a thermistor in
the tank and a Pt1000 in the flue, on one ADS1115 — and not a single
computed gain anywhere.

![The example's screen: pressure in bar, level in percent, two temperatures in degrees, and a pump that runs while the tank is low and the pressure is sane](img/analog-screen.webp){: .sb-center}

Its logic is three rungs, and they are readable because the values are
real:

- the pressure is sane while it is below its limit **in bar**,
- the tank is low while the level is below the setpoint **in percent**,
- the pump runs while both hold.

Nobody can write "below 3 bar" against a raw converter count.

---

## What to check when a value looks wrong

| What you see | Where to look |
|:---|:---|
| The value is a fixed multiple of what it should be | the divider, or the shunt |
| It moves the right way but the ends are wrong | the range and what it means — they are two pairs, not one |
| A temperature that is wildly off | which half of the divider the sensor is in (the tick box), then the reference resistor |
| A temperature that moves the WRONG way | an NTC falls as it warms; a Pt rises. The type says which |
| The value never moves | the reading may be refused — check the wiring at the pin |
| Everything reads zero | the converter itself: its address, and whether the bus finds it |

---

## What this is not

- **A divider is a divider.** For a three-wire Pt100 and
  tenth-of-a-degree work use an excited channel of the `ADS1220`,
  the `ADS122S14` or the `ADS124S08`, or a MAX31865, which delivers
  degrees by itself.
- **A thermocouple needs one of the `ADS1220` family.** A 16-bit
  converter without a gain stage reads its forty microvolts a degree
  as noise; the type is refused on any other input.
- **Not a filter.** A noisy signal is what the variable's deadband is
  for — and on the `ADS1220` family the 50/60 Hz filter at 20 samples
  a second.
