# Scope

[Online monitoring](online.md) samples ten times a second. That is right
for a human reading a value and useless for anything short: a pulse one
cycle long falls between two samples by construction, and the fault you
are chasing is usually exactly that.

The scope is the answer. The **board** records up to 8 values **every
cycle** into a ring buffer and stops on a trigger; the editor arms it and
draws what came back.

Open it from *Online → Scope*.

## What it records

| | |
|:---|:---|
| Signals | 8 |
| Samples | 256 rows — 2.56 s at a 10 ms cycle |
| Sampling | every cycle, in the board, never on the PC |
| Cost while recording | **6 µs per cycle** measured on a classic ESP32 at 240 MHz — 0.06 % of a 10 ms period |
| Cost while disarmed | one comparison — the sampler is not entered at all |

The buffer is fixed at 8 × 256 on purpose. A buffer whose size depends on
the project is a buffer whose cost nobody can predict, and this one has to
be free when it is off.

## Using it

1. **Pick the signals.** The list offers variables and, when the editor and the
   board run the same program, the wires between blocks and block members
   (`t1.ET`, `c1.CV`) as well. Up to eight; the counter above the list
   says how many are left.
2. **Set the trigger.**

    | Mode | Fires when |
|:---|:---|
    | now | immediately — fill the buffer once and stop |
    | rising edge | the source crosses the level upwards |
    | falling edge | … downwards |
    | level | the source is at or above the level |

    A BOOL source needs no level and is not asked for one.

3. **Choose how much history to keep.** The *pre* slider says how much of
   the ring is kept from **before** the trigger. This is the point of the
   whole feature: what happened in the 300 ms before the fault is the part
   nobody can arm for by hand.

    The number is exact and it is a promise: with 25 % of a 256-row ring
    the trigger row is row 64, with 64 rows of history behind it — not 63,
    and never zero because the event happened early. The board holds the
    trigger off until that history exists.
4. **Arm.** The board records; the editor shows *waiting for the trigger*,
   then *recording after it*, then *complete* — at which point the rows
   are pulled automatically and drawn.

The signal list, the trigger and the pre-trigger setting are **remembered
between sessions**. They are stored by name, so they are re-resolved
against whatever program is loaded now; a signal that no longer exists is
dropped and the page says so. They live in the editor's preferences, not
in the project — which signals you happen to be looking at is not a
property of the equipment.

!!! tip "A fault that happens once an hour"
    Tick **repeat** and the scope arms itself again after every capture.
    The re-arm waits until the rows have been read, so a capture is never
    overwritten before it has been seen. The counter under the checkbox
    says how many captures this session has produced.

    The board also keeps its recording across an editor restart or a
    pulled cable: on reconnecting, the editor asks whether one is
    running and picks it up instead of showing "off" over a live trace.

## Reading the picture

- **One lane per signal**, stacked like a logic analyser. Eight curves on
  one axis is a picture nobody can read.
- **Time is measured from the trigger.** Zero is where it fired,
  everything to the left of it is the history you asked to keep.
- The milliseconds come from the **board's own cycle period**, not from a
  number typed here — a trace labelled with the wrong period is a
  measurement that lies quietly.
- A BOOL is drawn as a square wave with a filled body. A number gets its
  own auto-scaled lane, with the range printed under its name; a fixed
  scale would hide exactly the small movement you opened the scope for.
- **Move the mouse over the plot** and every lane prints its value at that
  instant, next to its name. The tooltip adds the row and the time
  relative to the trigger.
- **Wheel zooms, drag pans.**

### Measuring between two points

Hovering reads one instant; the question an electrician actually asks is
*how long from this edge to that one*.

- **Left click** plants cursor **A**, **right click** plants **B**. No
  modifier keys — a person holding a probe in the other hand has one hand
  for the mouse.
- The span between them is shaded, and the corner reads
  `A -120 ms   B +80 ms   d 200 ms (5.00 Hz)`. The frequency is the same
  measurement asked the other way round, which is what you want when the
  two cursors sit on consecutive pulses.
- While A is planted, the hover tooltip also gives the time from A and,
  for numbers, the **difference in value** — a ramp's slope without doing
  arithmetic on paper.
- *Clear A/B* removes them; a new capture clears them by itself, because
  a cursor belongs to the recording it was placed in.

## Getting it out

*Export CSV* writes one row per sample: the time in milliseconds first
(**relative to the trigger**, exactly as the picture reads), then one
column per signal, and a `T` in the last column on the trigger row. That is the file you send a customer, or open in a spreadsheet next
to a measurement from something else.

## When it will not arm

| The page says | What it means |
|:---|:---|
| *not online — the scope records IN the board* | there is no connection; this is not a PC-side recorder |
| *the board runs a different program* | the same rule as everywhere: values travel by index, and under a different program they would be values under the wrong names |

If a recording comes back empty, the trigger never fired — check the
source and the level, or use *now* to see what the signals are doing at
all.

!!! note "An edge means a transition"
    Arming a **rising edge** on a signal that is *already* above the level
    does not fire immediately: the trace waits for the signal to go below
    and come back. Otherwise every arming would trigger on its own first
    sample and hand back a recording with no history — which is what it
    used to do before this was measured on a bench.
