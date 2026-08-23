# Timers

Four blocks: a delay on, a delay off, a fixed pulse, and a blinker.
Between them they cover almost everything a machine needs from time.

All of them measure **real milliseconds**, not cycles, and all of them
report progress on a second output so you can show it on a screen.

---

## TON — on-delay

**Q switches on once IN has been held continuously for PT ms.**

| Pin | Type | Meaning |
|---|---|---|
| `IN` | input, bool | the condition being timed |
| `PT` | parameter, ms (1000) | how long it must hold |
| `Q` | output, bool | TRUE once IN has held for PT |
| `ET` | output, number | elapsed time so far, ms |

The word that does the work is **continuously**. Any drop of IN, however
brief, puts ET back to zero and the wait starts again.

**What it is for:** ignoring things that are not real yet. A door switch
that rattles, a pressure that dips for an instant, an operator leaning on
a button. TON is how you say "only if it is still true half a second
later".

```
door_open ──[TON PT=2000]── Q ──> alarm_door
```

The alarm fires when the door has been open two seconds, not when
somebody walks through.

!!! tip "ET is worth showing"
    Bind `ET` to a tag and put a bar on the screen. An operator waiting
    for a delay with no feedback assumes the machine is broken; the same
    operator watching a bar fill waits patiently.

---

## TOF — off-delay

**Q stays on for another PT ms after IN drops.**

| Pin | Type | Meaning |
|---|---|---|
| `IN` | input, bool | the condition |
| `PT` | parameter, ms (1000) | how long Q holds after IN drops |
| `Q` | output, bool | TRUE while IN is TRUE, and PT ms longer |
| `ET` | output, number | how long since IN dropped, ms |

Q switches on **immediately** with IN. Only the switching off is delayed.

**What it is for:** run-on. A fan that keeps going after the heater stops.
A lamp that stays lit a moment after the last motion. A conveyor that
finishes carrying what is already on it.

```
heater_on ──[TOF PT=30000]── Q ──> fan
```

The fan runs while the heater does, and half a minute after it — no extra
logic, no timer you have to reset.

---

## TP — pulse

**A rising edge of IN fires Q for exactly PT ms.**

| Pin | Type | Meaning |
|---|---|---|
| `IN` | input, bool | trigger (rising edge) |
| `PT` | parameter, ms (1000) | pulse length |
| `Q` | output, bool | TRUE for PT ms after the trigger |
| `ET` | output, number | time into the pulse, ms |

The pulse is **non-retriggerable**: while it is running, further rising
edges of IN are ignored. It also does not care what IN does afterwards —
once started, the pulse runs its full length even if IN drops
immediately.

**What it is for:** a fixed dose of something. A puff of air, a squirt of
lubricant, a horn before a start, a solenoid that must not be energised
longer than it can take.

```
start_button ──[TP PT=500]── Q ──> horn
```

Half a second of horn, whether the operator taps the button or leans on
it.

!!! warning "Non-retriggerable matters"
    If you want a pulse that *restarts* on every edge, TP is the wrong
    block — use a rising edge into a TON reset, or hold the trigger in
    an RS latch that the pulse clears.

---

## BLINK — blinker

**While RUN is TRUE, Q alternates T_ON ms on and T_OFF ms off.**

| Pin | Type | Meaning |
|---|---|---|
| `RUN` | input, bool | while TRUE, the block blinks |
| `T_ON` | parameter, ms (500) | how long Q stays on |
| `T_OFF` | parameter, ms (500) | how long Q stays off |
| `Q` | output, bool | the blinking signal |
| `REM` | output, number | time left in the current phase, ms |

The two times are separate, which is more useful than it first looks: a
short on-time in a long off-time reads as a discreet heartbeat, the
reverse reads as an urgent alarm, and equal times read as a plain flash.

**What it is for:** telling a person something without words. A flashing
lamp for an unacknowledged alarm, a slow pulse to show the program is
alive, a fast one for "do not touch, it is about to move".

```
fault_unacked ──[BLINK T_ON=200 T_OFF=200]── Q ──> beacon
running       ──[BLINK T_ON=100 T_OFF=1900]── Q ──> heartbeat_led
```

!!! tip "A heartbeat is the cheapest diagnostic you will ever build"
    One BLINK on a spare output, and anyone standing at the machine can
    see whether the program is running — before opening a laptop.

`REM` counts *down* through the current phase. It is there when you need
to synchronise something with the blink rather than just watch it.

---

## Choosing between them

| You want | Block |
|---|---|
| ignore a signal until it has held | **TON** |
| keep something running after the reason stopped | **TOF** |
| a fixed dose, regardless of how long the trigger lasts | **TP** |
| something that flashes | **BLINK** |

## The trap worth knowing

Never build a timer by counting cycles. `n := n + 1; IF n > 100 THEN`
looks like it waits a second and does — until the WiFi stack gets busy,
the cycle stretches, and your second becomes 1.4. Every block here uses a
monotonic millisecond clock and is immune to that.

The same applies to your own ST blocks: take a timestamp, compare
timestamps.
