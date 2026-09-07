# Motion blocks

Nine blocks for driving an axis, named after **PLCopen Motion** — the
naming used across the automation world, so `MC_POWER`
and `MC_MOVEABS` mean here what they mean elsewhere.

Every one of them takes an **AXIS** number at the call. Which axis is
never guessed: in [Structured Text](st-language.md) you write
`pwr(AXIS := 0, Enable :=
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

<!-- blk:MC_POWER -->
**MC_POWER**

![MC_POWER on a rung](img/blk-mcpow-ld.webp)

![MC_POWER in structured text](img/blk-mcpow-st.webp)

![MC_POWER on the WEBview screen](img/blk-mcpow-web.webp)

<!-- /blk -->

<!-- blk:MC_RESET -->
**MC_RESET**

![MC_RESET on a rung](img/blk-mcrst-ld.webp)

![MC_RESET in structured text](img/blk-mcrst-st.webp)

![MC_RESET on the WEBview screen](img/blk-mcrst-web.webp)

<!-- /blk -->

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

<!-- blk:MC_MOVEVELOCITY -->
**MC_MOVEVELOCITY**

![MC_MOVEVELOCITY on a rung](img/blk-mcvel-ld.webp)

![MC_MOVEVELOCITY in structured text](img/blk-mcvel-st.webp)

![MC_MOVEVELOCITY on the WEBview screen](img/blk-mcvel-web.webp)

<!-- /blk -->

<!-- blk:MC_STOP -->
**MC_STOP**

![MC_STOP on a rung](img/blk-mcstop-ld.webp)

![MC_STOP in structured text](img/blk-mcstop-st.webp)

![MC_STOP on the WEBview screen](img/blk-mcstop-web.webp)

<!-- /blk -->

<!-- blk:MC_MOVEABS -->
**MC_MOVEABS**

![MC_MOVEABS on a rung](img/blk-mcabs-ld.webp)

![MC_MOVEABS in structured text](img/blk-mcabs-st.webp)

![MC_MOVEABS on the WEBview screen](img/blk-mcabs-web.webp)

<!-- /blk -->

<!-- blk:MC_MOVEREL -->
**MC_MOVEREL**

![MC_MOVEREL on a rung](img/blk-mcrel-ld.webp)

![MC_MOVEREL in structured text](img/blk-mcrel-st.webp)

![MC_MOVEREL on the WEBview screen](img/blk-mcrel-web.webp)

<!-- /blk -->

<!-- blk:MC_HOME -->
**MC_HOME**

![MC_HOME on a rung](img/blk-mchome-ld.webp)

![MC_HOME in structured text](img/blk-mchome-st.webp)

![MC_HOME on the WEBview screen](img/blk-mchome-web.webp)

<!-- /blk -->

A stop along a defined ramp. Not an emergency stop — see below.

---

## Reading the axis

| Block | Inputs | Outputs |
|:---|:---:|:---:|
| **MC_READACTPOS** | Enable | Position, Valid |
| **MC_READACTVEL** | Enable | Velocity, Valid |
| **MC_READSTATUS** | Enable | Running, Error |

<!-- blk:MC_READACTPOS -->
**MC_READACTPOS**

![MC_READACTPOS on a rung](img/blk-mcrpos-ld.webp)

![MC_READACTPOS in structured text](img/blk-mcrpos-st.webp)

![MC_READACTPOS on the WEBview screen](img/blk-mcrpos-web.webp)

<!-- /blk -->

<!-- blk:MC_READACTVEL -->
**MC_READACTVEL**

![MC_READACTVEL on a rung](img/blk-mcrvel-ld.webp)

![MC_READACTVEL in structured text](img/blk-mcrvel-st.webp)

![MC_READACTVEL on the WEBview screen](img/blk-mcrvel-web.webp)

<!-- /blk -->

<!-- blk:MC_READSTATUS -->
**MC_READSTATUS**

![MC_READSTATUS on a rung](img/blk-mcstat-ld.webp)

![MC_READSTATUS in structured text](img/blk-mcstat-st.webp)

![MC_READSTATUS on the WEBview screen](img/blk-mcstat-web.webp)

<!-- /blk -->

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

The quickest road to a working axis is the **CAN axis wizard**: right-click
*CANopen Master* in the project tree and choose *Add Axis (drive)*, or
press the *CAN wizard...* button in an axis window. The whole road from the
wiring to the first turn of the motor, with pictures, is
[A drive over CAN, step by step](tutorial-i550-can.md).

![The CAN axis wizard](img/axis-wizard.webp){: .sb-center}

It It takes the axis name, the node-ID and the profile and
makes three things in one step:

- the **CAN device** of that node with the two PDOs the runtime
  exchanges on every SYNC (TPDO1 statusword + speed, RPDO1 controlword +
  setpoint) and the start-up SDO writes (velocity mode; on the i550 the
  network-control pair that switches its own state machine off)
- the **variables the MC blocks bind to**: `enable`, `run`, `stop`,
  `reset`, `speed`, `ready`, `fault`, `running`, `velocity`; an axis
  that positions adds `move`, `home`, `target`, `position`, `done`
- the **axis** itself, opened in its window

The first axis gets single words; a second one gets its name as a
prefix (`feed_speed`), editable in the dialog. A variable that already
exists under that name is kept, never duplicated. What the wizard makes
is an ordinary project afterwards - every part can be changed by hand.

See [CANopen blocks](blocks-can.md) for what talks to a drive directly,
and [Buses](buses.md) for the wiring.
