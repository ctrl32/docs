# Tags

**A tag is a variable.** It is also the only place in the whole system where
a value lives — a widget holds no value, only a tag index. That is why the
screen, the logic, WEBview and Modbus all see the same number, with no way
to drift apart.

The tag table is at the same time the PLC's **process image** (the
equivalent of I/Q/M on an S7).

## Creating a tag

In the project tree: *Application → Tags*. Every tag has:

| Property | What it is for |
|---|---|
| **name** | the only thing you refer to it by; in ST it is an identifier |
| **type** | `BOOL`, `I16`, `U16`, `I32`, `U32`, `REAL` (f32), `STRING`, `TIME` |
| **access** | `ro` (read only) / `rw` — for WEBview and the operator, not for the logic |
| **source** | where the value comes from (below) |
| **gain / offset** | conversion to a physical quantity: `y = x · gain + offset` |
| **unit, decimals** | how it is displayed |
| **deadband** | from what change on it counts as a change |

!!! warning "A tag name must not be an ST keyword"
    Names like `NOT`, `AND`, `VAR`, `REAL`, `TIME` or `END_IF` become
    something else in the generated program. The editor refuses them at
    build time and names the tag.

## Where the value comes from

| Source | Meaning |
|---|---|
| **internal** | panel memory only; with `persist` it survives a restart |
| **modbus** | from a PLC, a drive or a meter — unit, function code, address |
| **canopen** | an object from a node's dictionary (index/subindex), over PDO or SDO |
| **gpio** | a local panel input/output, optionally inverted |
| **periph** | a chip pin on a local bus (expander, thermometer, LED) |

!!! danger "Word order for Modbus `f32`"
    A `REAL` travels over Modbus in two 16-bit registers, and **the word
    order differs from vendor to vendor**. It is the most common source of
    nonsense values. There is a `word_order` switch for it; when 23.5 °C
    reads as 3.4·10³⁸, start here.

!!! note "SDO never in the cycle"
    CANopen objects read over **SDO** are slow and do not belong in the
    cycle — they are for parameterization at startup or an operator's
    action. What belongs in the cycle is **PDO**.

## TIME — a time the operator sets

A machine's delays belong to the **operator**, not to a rebuild. That is
what a `TIME` tag is for:

```yaml
- { name: delay, datatype: time, unit: s, decimals: 1, init: 2500 }
```

- **the table always holds milliseconds** — the logic, the buses and Modbus
  see an ordinary integer,
- **the panel shows and edits it in the tag's unit** (`ms`, `s`, `min`,
  `h`). With `unit: s` the widget reads "2.5 s", the operator types `2.5` on
  the keypad and 2500 is stored,
- **`min`/`max` on the `input` widget are in the same unit**, so the
  operator is bounded by the numbers they can see,
- **in ST it is a `TIME`**, so `t1(PT := delay)` and `delay := T#1s500ms`
  need no conversion at all.

This is exactly how you put a "preheat time" on the operator's screen: an
`input` bound to a `TIME` tag, and the same tag as the timer's `PT`.

!!! note "Time comparisons are unsigned"
    A `TIME` runs past 2³¹ ms (24.8 days), which is ordinary on a machine
    that is never switched off. Comparisons are therefore unsigned, and
    `IF t1.ET > T#500ms` still holds after a month of running.

## Deadband is not cosmetics

An analog input always has noise. Without a deadband the panel repaints the
display on every flicker of the last bit, and sends that same flicker over
the WebSocket to every connected browser.

Set the deadband **larger than the noise and smaller than what you care
about**: for a pressure sampled at 0.01 bar resolution, 0.05 bar is
sensible.

## Retention (persist)

An `internal` tag with `persist` survives a power-down. One hard rule
applies:

!!! danger "Do not write retentive data on every change"
    Flash and EEPROM both have a finite number of writes. A tag that changes
    every cycle and is written on every change destroys the memory within
    months. Retentive is for what you need to remember across a power-down —
    a piece counter, a temperature setpoint, the current step — not for the
    instantaneous value of a measurement.

## Why reading a tag is the most expensive thing in the cycle

Since 2026-08-16 the tag table is **lock-free**: a value is one naturally
aligned 32-bit word and a tag's type never changes after registration, so a
reader always gets either the old value or the new one — never half of each.
The hardware guarantees it and no mutex is needed.

Before that, every access paid for a lock (~1.5 µs per take/give pair),
which was 20–100× the memory access it guarded. The machine program went
from 1.32 ms to **0.30 ms**. Details in
[Performance and limits](limits.md).

The practical consequence for you: **keep intermediate results in POU local
variables, not in tags.** A tag is an interface — to the screen, to Modbus,
to monitoring. Not scratch space.

!!! warning "A type wider than 32 bits does not fit the table"
    `LREAL`, `LINT` and a string stored inside the value are unsupported
    precisely because they would break the lock-free read. Strings are
    indices into the string table.

## A snapshot, not an instant

The renderer and online monitoring both read a **snapshot**: every tag in it
is fresh in itself, but it is not a consistent instant across all tags. It
never was — a writer updates them tag by tag. For display that is right;
when you need two values guaranteed to be from the same cycle, compute them
in the logic and write the result.

## Limit

**512 tags.** In practice this is the first thing to run out — before
blocks, before bytecode. The editor refuses a project over the limit at
build time.
