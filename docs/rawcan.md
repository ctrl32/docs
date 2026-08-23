# Raw CAN (without CANopen)

The board can speak two ways on the CAN bus:

| | CANopen | **Raw CAN** |
|:---|:---|:---|
| Devices | frequency drives, I/O modules per CiA 301/402 | batteries and BMS, solar inverters, chargers, wallboxes |
| Configuration | EDS file, node-ID, SDO, PDO mapping | frame ID and byte layout |
| Who uses it | industry | home automation and energy |

Most devices in home automation **do not speak CANopen and never
will** — they send their own frames with a fixed byte layout. That is
why raw CAN is a separate part, not an add-on to CANopen.

Both paths run on **the same bus at the same time**. The board can
control a drive over CANopen and read a battery with raw frames
simultaneously.

## The signal model is DBC

A frame has an ID and up to 8 bytes. A signal inside it is defined by
five things — exactly the ones you find in the vendor's DBC file:

| Field | Meaning |
|:---|:---|
| `start_bit` | 0..63; with `little` it is the LSB of the signal, with `big` its MSB |
| `bits` | width 1..32 |
| `byte_order` | `little` (Intel) or `big` (Motorola) |
| `signed` | two's complement |
| `gain` / `offset` | `tag = raw_value × gain + offset` |

Thanks to that a DBC maps one to one and **DBC import can be added
without changing the pack format**.

## YAML

```yaml
raw_can:
  # BMS -> board
  - id: 0x355
    dir: rx
    dlc: 8
    signals:
      - { tag: bat_voltage, start_bit: 0,  bits: 16, byte_order: little, gain: 0.01 }
      - { tag: bat_current, start_bit: 16, bits: 16, byte_order: little, signed: true, gain: 0.1 }
      - { tag: bat_soc,     start_bit: 32, bits: 8,  byte_order: little }

  # 29-bit frame (chargers using J1939-like schemes)
  - id: 0x18FF50E5
    ext: true
    dir: rx
    dlc: 8
    signals:
      - { tag: cell_temp, start_bit: 7, bits: 16, byte_order: big, signed: true, gain: 0.1, offset: -40.0 }

  # board -> BMS, every 100 ms
  - id: 0x305
    dir: tx
    dlc: 2
    period_ms: 100
    signals:
      - { tag: charge_current, start_bit: 0, bits: 16, byte_order: little }
```

`dir: rx` = the board receives the frame and unpacks it into tags.
`dir: tx` = the board builds the frame from tags and transmits it.
`period_ms: 0` means **transmit on change** — the tag deadband has
already filtered the noise, so only a real change is sent.

In the editor this is the tree → **CAN → Raw CAN**. The same fields,
one table per frame.

## Product limits

| Limit | Value |
|:---|:---:|
| Frames | 32 |
| Signals in total | 128 |

The editor rejects a project over the limit at compile time.

## Pitfalls

| Pitfall | Consequence |
|:---|:---|
| **Swapping `little` and `big`** | the values look "almost right" — the same class of fault as the word order on Modbus `f32`. Verify against a known value (voltage, temperature), not one that happens to be fluctuating. |
| An ID overlapping the CANopen range | the two protocols get in each other's way on one bus. Packbuild **rejects** such a project; the editor shows it in red right on the page. |
| Forgotten `signed` | a negative current reads as 65 A instead of −1 A |
| A truncated frame (shorter `dlc` than the signal needs) | the runtime **skips it** and the tag holds its last value — a truncated frame is common while a device is powering up and must not write nonsense |
| `period_ms` too short | at 500 kbit/s an 8-byte frame takes ~130 µs; 10 frames every 10 ms is ~13 % of the bus. Transmit as often as you need to, not as often as you can. |

## How it works inside

TWAI has **a single receive queue**, so only one reader may drain it.
Therefore:

- when CANopen is running, its `poll()` picks the frames up and passes
  those that do not belong to CANopen on to raw CAN (a hook);
- when CANopen is off, a separate `rawcan_task` runs (core 1, 10 ms)
  and reads the queue itself.

TX frames are assembled **after reception** in the same cycle, so that a
value received in this cycle makes it into the reply.

The period is computed from monotonic milliseconds, never in cycles —
with cycle jitter the timing would drift.

## Diagnostics

The serial command `VUI!` prints `rawcan=<received>,<sent>`. If the
received counter does not grow, the device is silent or the bus rate
does not match; if it grows and the values are nonsense, `byte_order`
or `start_bit` is wrong.
