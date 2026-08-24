# Motion blocks

Nine blocks for driving an axis, named after **PLCopen Motion** — the
naming used across the automation world, so `MC_POWER`
and `MC_MOVEABS` mean here what they mean elsewhere.

Every one of them takes an **AXIS** number at the call. Which axis is
never guessed: in Structured Text you write `pwr(AXIS := 0, Enable :=
go);` and the compiler refuses a motion block without it. A guessed axis
is a moving axle.

---

## Turning the axis on

### MC_POWER

| Pin | Type | Meaning |
|:---|:---:|:---:|
| `Enable` | input, bool | axis on/off |
| `Status` | output, bool | axis ready and operational |
| `Error` | output, bool | axis in fault |

Nothing else moves until `Status` is TRUE. On a CANopen drive this runs
the CiA 402 state machine — several steps of controlword and statusword
that the block handles for you.

### MC_RESET

| Pin | Type | Meaning |
|:---|:---:|:---:|
| `Execute` | input, bool | acknowledge the axis fault |
| `Done` | output, bool | the reset completed |
| `Error` | output, bool | the reset failed |

Fault acknowledge, on a rising edge of Execute. If `Error` stays on, the
cause is still present — reset does not clear a fault that is still
happening.

---

## Making it move

### MC_MOVEVELOCITY — constant speed

| Pin | Type | Meaning |
|:---|:---:|:---:|
| `Execute` | input, bool | start on the rising edge |
| `Velocity` | input, number | target speed |
| `Direction` | parameter (0) | 0 = forward, 1 = reverse |
| `InVelocity` | output, bool | target speed reached |
| `Busy` | output, bool | the block is working |

Ramps up to `Velocity` and holds it. This is the block for a conveyor, a
pump, a fan — anything that runs at a speed rather than to a position.

### MC_MOVEABS — go to a position

| Pin | Type | Meaning |
|:---|:---:|:---:|
| `Execute` | input, bool | start on the rising edge |
| `Position` | input, number | where to go |
| `Velocity` | input, number | how fast to travel |
| `Accel`, `Decel` | parameters, **seconds** to reach `Velocity` (100, 100) | ramps |
| `Done` | output, bool | arrived |
| `Busy` | output, bool | on the way |

Absolute: the position is measured from the axis zero, so the axis must
be **homed** first.

### MC_MOVEREL — go a distance

Same pins, but `Distance` instead of `Position`: move this far from
wherever you are now. No homing required, and errors accumulate over
repeated moves — which is fine for indexing and wrong for positioning.

### MC_HOME — reference run

| Pin | Type | Meaning |
|:---|:---:|:---:|
| `Execute` | input, bool | start the homing run |
| `Done` | output, bool | the axis knows where it is |
| `Busy` | output, bool | homing in progress |

Until this has completed, absolute positions mean nothing.

### MC_STOP — controlled stop

| Pin | Type | Meaning |
|:---|:---:|:---:|
| `Execute` | input, bool | stop |
| `Decel` | parameter, **seconds** (5) | deceleration ramp |
| `Done` | output, bool | stopped |
| `Busy` | output, bool | stopping |

A stop along a defined ramp. Not an emergency stop — see below.

---

## Reading the axis

| Block | Inputs | Outputs |
|:---|:---:|:---:|
| **MC_READACTPOS** | Enable | Position, Valid |
| **MC_READACTVEL** | Enable | Velocity, Valid |
| **MC_READSTATUS** | Enable | Running, Error |

`Valid` is the pin that matters. It goes FALSE when the value is stale —
the drive has stopped answering, the bus has dropped — and **acting on a
stale position is a fault that appears once a month and nobody
understands**. Gate anything that uses the position on `Valid`.

---

## A frequency drive is not a servo

The reference target is the **Lenze i550** over CANopen: a frequency
drive with no position loop of its own. The board generates the profile
and sends a speed setpoint every cycle.

That has consequences worth knowing before promising anything:

**Position comes over the bus, and the bus takes time.** Sampling in the
drive, transfer over CAN and the PLC cycle add up to a real 15–30 ms. At
500 mm/s that is 7–15 mm of travel you do not know about yet.

**Which is why the creep phase is mandatory.** The profile ramps down to
a slow approach speed before the target. At 20 mm/s a 20 ms delay is
0.4 mm; at 500 mm/s the same delay is 10 mm. The creep phase is not an
optimisation, it is what makes the accuracy possible.

**Realistic repeatability is ±0.5 to 2 mm**, depending on the mechanics.
It is not a servo and it should not be sold as one.

The delay and repeatability figures are what this class of hardware
gives; commissioning against the reference drive is still running, and
the numbers will be confirmed — or tightened — from those measurements.

!!! danger "Set the drive's own ramps to minimum"
    The most common commissioning problem on this hardware: the drive has
    acceleration ramps configured *and* the program ramps the setpoint.
    The two disagree, and the axis overshoots and oscillates. One place
    owns the profile — the program — so wind the drive's ramps down and
    leave them there.

!!! warning "Watch for stale position data"
    Count the cycles since the last position update and **stop the
    motion** if it exceeds a few. Positioning on a value that stopped
    arriving is the failure that shows up once a month and takes a week
    to find.

---

## Safety

Stopping over CANopen is **not** a safety function. Neither is
`MC_STOP`, and neither is anything in this page.

- Limit switches belong **hard-wired** into the drive or onto inputs —
  software limits are a supplement, not protection.
- The i550 has **STO** terminals; that is what an emergency stop wires
  into.
- Define what happens on loss of the encoder, on a motion timeout, and
  on a deviation between commanded and actual speed. All three occur on
  real projects.

See [Intended use](intended-use.md).

---

## Setting the drive up

The i550 ships with **Lenze's own state machine active**, not CiA 402 —
the full story, and the DIP switches worth writing on the drawing, is
in [CANopen — drives](canopen.md). The startup block switches the mode
over SDO so a project built from the i550 profile never meets it.

See [CANopen blocks](blocks-can.md) for what talks to a drive directly,
and [Buses](buses.md) for the wiring.
