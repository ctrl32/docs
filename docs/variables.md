# Variables

**A variable is the only place in the whole system where a value lives.**
A widget holds no value, only a reference to a variable; the logic reads
and writes variables; Modbus, CANopen and the browser all reach the same
ones. That is why the screen, the program and the outside world cannot
drift apart — there is nothing to drift.

The variable table is at the same time the PLC's **process image**.

![The variable list of the thermostat example — types, units, deadbands and access in one declaration block](img/tags-variables.webp){: .sb-center}

---

## VAR and RVAR

Variables live in **lists**, and a project has at least one.

| Object | What it is |
|:---|:---|
| **VAR** | a named list of global variables. A project starts with one called `VAR`; add more from *Add Object* to group things by area — `VAR_Heating`, `VAR_Conveyor`. |
| **RVAR** | the **retain** list — its variables survive a power-down. **At most one per project**, added the same way. |

The grouping in VAR lists is for you, not for the program: a variable in
`VAR_Heating` is reached by name exactly like any other. Split them when
a single list stops being something you can scan.

### Retain is membership, not a checkbox

This is the part worth reading twice. **A variable is retained because
it is in the RVAR list** — not because a flag is set on it somewhere.

That single rule prevents the classic mess: retention declared in two
places that disagree, and nobody able to say which values actually
survive a restart. Open RVAR and you are looking at the complete list of
what the board remembers.

Move a variable in, and it is retained. Move it out, and it is not.

### What belongs in RVAR

Things that must be known after power comes back:

- a piece counter, an hour meter
- a setpoint somebody typed
- which step a sequence had reached
- a latched fault that must not clear itself by a power cycle

**What does not:** measurements, calculated values, anything the program
recomputes on its own within a cycle or two.

!!! danger "Never write retained data on every change"
    Retain storage has a finite number of write cycles. A variable
    that changes every cycle and is stored on every change wears the
    memory out within months.

    RVAR is for what you need to remember, not for the instantaneous
    value of a measurement. If you are unsure whether something belongs
    there, ask what breaks if it comes back as zero — if the answer is
    "nothing", leave it in VAR.

!!! success "FRAM makes this painless"
    On hardware with FRAM, writes take microseconds and the endurance is
    practically unlimited, so the whole timing problem around power loss
    disappears. Where retention matters, it is worth choosing hardware
    that has it.

---

## What every variable has

| Property | What it is for |
|:---|:---|
| **name** | the only thing you refer to it by; in ST it is an identifier |
| **type** | `BOOL`, `I16`, `U16`, `I32`, `U32`, `REAL` (f32), `STRING`, `TIME` |
| **access** | `ro` / `rw` — for the browser and the operator, not for the logic |
| **source** | where the value comes from (below) |
| **gain / offset** | conversion to a physical quantity: `y = x · gain + offset` |
| **unit, decimals** | how it is displayed |
| **deadband** | from what change on it counts as a change |

!!! warning "A name must not be an ST keyword"
    Names like `NOT`, `AND`, `VAR`, `REAL`, `TIME` or `END_IF` become
    something else in the generated program. The editor refuses them at
    build time and says which one.

---

## Bits of a word

Every bit of an integer variable is addressable on its own, everywhere
the variable itself goes:

- **ST**: `IF status.5 THEN`, `mask.0 := ready;`
- **Ladder / FBD**: a contact, a coil or a block's bool pin binds
  variable + bit — the picker offers the bit field
- **Screens**: the switch and led widgets carry `bit:`

The index must fit the declared width: bits 0–15 on a 16-bit variable,
0–31 on a 32-bit one. A wrong index, a `REAL`, a `TIME` or a bool (a bool
*is* a bit) are refused at build time with the variable named. The index
is a constant.

!!! success "A bit write never loses a neighbour"
    Writing `mask.0` from the logic while a browser switch flips `mask.7`
    is safe — bits are written atomically, so neither writer can undo the
    other's work.

---

## Where the value comes from

| Source | Meaning |
|:---|:---|
| **internal** | board memory only |
| **modbus** | from a controller, a drive or a meter — unit, function code, address |
| **canopen** | an object from a node's dictionary (index/subindex), over PDO or SDO |
| **gpio** | a local board input or output, optionally inverted |
| **periph** | a chip pin on a local bus (expander, thermometer, LED) |
| **adc** | the internal ADC1 — calibrated millivolts, × gain + offset |
| **opcua** | a node polled from an OPC UA server — see [The Linux runtime](linux-runtime.md) |
| **s7** | a DB value or flag bit read from an S7 PLC — see [+7 (S7 PLC)](plus7.md) |
| **nvl** | a variable owned by another ctrl32 device — see [net32](net32.md) |

```yaml
- { name: vbat, datatype: f32, unit: mV, decimals: 0, deadband: 5,
    source: { adc: { pin: 34 } } }
```

The variable receives **millivolts** roughly ten times a second; a battery
divider is one `gain` away from volts. Only **ADC1** pins work (classic
ESP32: GPIO 32–39, ESP32-S3: GPIO 1–10) — ADC2 shares silicon with WiFi
and loses, so an ADC2 pin is refused at build time, not discovered on the
bench.

The quickest way to make one is the board card: every free pin has a row
with a name field, and a pin marked *ADC1* offers *analog input* in the
choice beside the name, next to *input* and *output*. Type the name, pick
*analog input*, and the variable exists with the pin already set; the
same choice turns it back into a digital one.

## System variables

Every project has a set of variables the device fills in by itself,
once per cycle, before your logic runs. They live under the reserved
name `SYS.` and are used like any other variable — in a rung, in ST, on
a screen, in an alarm. Right-click a variable list in the tree and pick
*Add system variable* to bring one into the project; in ST you may
simply write it, `x := SYS.UPTIME_S;`, and the build adds it for you.

| name | type | meaning |
|:---|:---|:---|
| `SYS.FIRST_CYCLE` | BOOL | TRUE in the first cycle after start — the place for start-up code |
| `SYS.UPTIME_S` | DINT | seconds since start |
| `SYS.CYCLE_US`, `SYS.CYCLE_MAX_US` | DINT | the last and the worst cycle time |
| `SYS.OVERRUNS` | DINT | cycles that ran past their period |
| `SYS.CYCLE2_US`, `SYS.OVERRUNS2` | DINT | the same for the second task |
| `SYS.CYCLE3_US`, `SYS.OVERRUNS3`, `SYS.CYCLE4_US`, `SYS.OVERRUNS4` | DINT | the same for the third and fourth task |
| `SYS.CAN_OK` | BOOL | the CAN driver runs |
| `SYS.CAN_FAULT` | BOOL | the bus is off, or recovering from bus-off |
| `SYS.CAN_RECOVERIES` | DINT | bus-off recoveries since start |
| `SYS.ETH_OK`, `SYS.WIFI_OK`, `SYS.NET_OK` | BOOL | the interface has an address; NET_OK = either |
| `SYS.MQTT_OK` | BOOL | the MQTT client is connected |
| `SYS.NVL_PEERS`, `SYS.NVL_NODES` | INT | net32 peers alive, and configured |
| `SYS.MB_OK` | BOOL | every polled Modbus device answers |
| `SYS.S7_OK` | BOOL | the +7 connection is up |
| `SYS.RETAIN_BACKEND` | INT | where retentive values go: 0 flash, 1 FRAM, 2 EEPROM |
| `SYS.RETAIN_OK` | BOOL | the last retentive write succeeded |
| `SYS.RETAIN_SAVE` | BOOL | **writable** — set it and the retentive values are written now; the device clears it |
| `SYS.OTA_PENDING` | BOOL | a freshly updated runtime that has not confirmed itself yet |
| `SYS.TIME_VALID` | BOOL | the clock is set — NTP answered or the RTC was read |
| `SYS.HW_ID` | DINT | the board's hardware id |
| `SYS.HOUR`, `SYS.MINUTE` | INT | the wall clock in the project's time zone (*clock: tz*); 0 while `SYS.TIME_VALID` is FALSE |
| `SYS.MINUTE_OF_DAY` | INT | hour x 60 + minute, 0..1439 - the number a schedule compares |
| `SYS.WEEKDAY` | INT | 1 = Monday .. 7 = Sunday |
| `SYS.DAY`, `SYS.MONTH`, `SYS.YEAR`, `SYS.DAY_OF_YEAR` | INT | the date, 1-based |

A fact a device does not have reads FALSE or 0 there; nothing is ever
invented.

### Saving retentive values

Retentive variables are written to the chip on an interval that suits
it — an EEPROM once in five minutes (its cells wear), FRAM every second,
flash every ten seconds. *Project → Retentive save interval* changes it
for a project that needs to. Independent of the interval,
`SYS.RETAIN_SAVE` writes everything **now**: put it on the OK of a keypad
and a value the operator confirmed is on the chip before the hand leaves
the glass, whatever the interval says.

!!! note "EEPROM cells wear"
    An EEPROM cell takes about a million writes. A program that pulses
    `SYS.RETAIN_SAVE` every cycle, or an interval of a few seconds on a
    value that changes all the time, wears it out in months. FRAM does
    not care.

!!! note "Battery duty, not measurement"
    The internal ADC is fine for a battery level, a potentiometer or a
    light sensor. For anything called **measurement**, use an
    ADS1115-class peripheral on the I²C bus — see
    [Adding peripherals](adding-peripherals.md).

!!! danger "Word order for Modbus `REAL`"
    A `REAL` travels over Modbus in two 16-bit registers, and **the word
    order differs from vendor to vendor**. It is the most common source
    of nonsense values. There is a `word_order` switch for it — when
    23.5 °C reads as 3.4·10³⁸, start there.

!!! note "SDO never in the cycle"
    CANopen objects read over **SDO** are slow and do not belong in the
    cycle — they are for parameterisation at startup. What belongs in the
    cycle is **PDO**. See [CANopen](canopen.md).

---

## TIME — a duration the operator can set

Delays belong to the operator, not to a rebuild. That is what a `TIME`
variable is for:

```yaml
- { name: delay, datatype: time, unit: s, decimals: 1, init: 2500 }
```

- **the table always holds milliseconds** — the logic, the buses and
  Modbus see an ordinary integer
- **the board shows it the readable way** — `2s500ms`, `10s`, `1m5s`,
  `1h2m` — and the keypad **edits it in the variable's unit** (`ms`, `s`,
  `min`, `h`): with `unit: s` the operator types `2.5` and 2500 is stored
- **`min`/`max` on the `input` widget are in the same unit**, so the
  operator is bounded by numbers they can see
- **in ST it is a `TIME`**, so `t1(PT := delay)` and
  `delay := T#1s500ms` need no conversion

That is how a "preheat time" reaches an operator's screen: an `input`
bound to a `TIME` variable, and the same variable as the timer's `PT`.

!!! note "Time comparisons are unsigned"
    A `TIME` runs past 2³¹ ms (24.8 days), which is ordinary for
    something never switched off. Comparisons are unsigned, so
    `IF t1.ET > T#500ms` still holds after a month.

---

## Deadband is not cosmetics

An analog input always has noise. Without a deadband the board repaints
the display on every flicker of the last bit, and sends that same flicker
over the WebSocket to every connected browser.

Set it **larger than the noise and smaller than what you care about**:
for a pressure resolved to 0.01 bar, 0.05 bar is sensible.

This one field does more for how a project feels to use than any other.

---

## Why reading a variable is the most expensive thing in the cycle

The variable table is **lock-free**: a value is one naturally aligned
32-bit word and a type never changes after registration, so a reader gets
either the old value or the new one, never half of each. The hardware
guarantees it and no lock is needed.

Before that, every access paid for a lock — about 1.5 µs per take/give
pair, which was 20–100× the memory access it guarded. The control
program went from 1.32 ms to **0.30 ms**. See [Performance and
limits](limits.md).

**The practical consequence: keep intermediate results in POU local
variables, not in global ones.** A global variable is an interface — to
the screen, to Modbus, to monitoring. Not scratch space.

!!! warning "A type wider than 32 bits does not fit"
    `LREAL`, `LINT` and a string stored inside the value are unsupported
    precisely because they would break the lock-free read. Strings are
    indices into a string table.

---

## A snapshot, not an instant

The renderer and online monitoring both read a **snapshot**: every value
in it is fresh in itself, but it is not a consistent instant across all
of them. It never was — a writer updates them one at a time.

For display that is right. When you need two values guaranteed to be from
the same cycle, compute them in the logic and write the result.

---

## Limit

**512 variables** (a Linux device: 5 120; an ESP32 without PSRAM, the
LITE class: 128 — the full table by board type is in
[Performance and limits](limits.md)). In practice this is
the first thing to run out — before blocks, before compilation. The
editor refuses a project over the limit at build time, at your desk.
