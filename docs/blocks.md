# Function blocks

A function block is a piece of logic somebody already wrote and tested,
so you do not have to. A timer, a counter, a motor starter with feedback
supervision — you drop it into a rung or a diagram, wire its pins, and it
behaves the same on every board ctrl32 runs on.

ctrl32 ships **53 of them**. This page is what they have in common; the
pages that follow are the reference, grouped the way the Toolbox groups
them.

| Group | Blocks | What they are for |
|:---|:---|:---|
| [Timers](blocks-timers.md) | TON, TOF, TP, BLINK | delays, pulses, flashing |
| [Counters](blocks-counters.md) | CTU, CTD | counting events |
| [Boolean](blocks-boolean.md) | AND, OR, XOR, NOT, R_TRIG, F_TRIG, SR, RS | logic, edges, latches |
| [Maths](blocks-math.md) | ADD, SUB, MUL, DIV, MIN, MAX, ABS, MOVE | arithmetic |
| [Comparison](blocks-compare.md) | GT, GE, LT, LE, EQ, SEL | decisions on numbers |
| [Signal handling](blocks-signal.md) | SCALE, LIMIT, HYST, RAMP, PT1 | turning a raw value into a usable one |
| [Equipment blocks](blocks-equipment.md) | MOTOR, VALVE, PID | starters, valves and a controller, ready made |
| [Motion](blocks-motion.md) | MC_POWER, MC_MOVEVELOCITY, MC_MOVEABS, … | driving an axis |
| [CANopen](blocks-can.md) | CO_CIA402, CO_SDOWRITE, CO_SDOREAD, CO_RAMPTIME | talking to a drive directly |
| [Services](blocks-services.md) | IR_SEND, SMS_SEND, GSM_INFO | infrared, SMS, modem state |

## Anatomy of a block

Every block has three kinds of pin, and the difference matters:

| | What it is | When it is read |
|:---|:---|:---|
| **Inputs** | values that change while it runs — a sensor, another block's output | every cycle |
| **Parameters** | settings that belong to *this* instance — a delay, a limit | every cycle, but you normally set them once |
| **Outputs** | what the block produces | written every cycle |

An input you leave unconnected is **0** (or FALSE). A parameter you leave
alone keeps its default, which is listed with every block.

The practical difference is where you type them: inputs get wired to
tags, parameters are typed into the block's own fields. If a value should
be adjustable from a screen, it belongs on a tag wired to an input — not
in a parameter.

## An instance remembers, a formula does not

`AND` has no memory: the same inputs always give the same output.
A timer does — it has to know how long IN has been held.

Blocks with memory get an **instance**: a name, and a piece of RAM
reserved for it. Two `TON` instances count independently even with the
same PT. That is why blocks with memory ask for a name and blocks
without one do not.

!!! success "The editor knows the RAM cost before you upload"
    Instances are allocated when the project is compiled, not while the
    equipment runs — so the editor can tell you a program does not fit
    *at your desk*, instead of the board finding out on the equipment.

## Times are always milliseconds

Every time parameter in every block is in **milliseconds**, and every
block measures real elapsed time.

This sounds obvious and it is the single most common way home-made
timers go wrong: counting cycles (`if (++n >= 100)`) drifts the moment
the cycle jitters, and it jitters as soon as the network gets busy. A
ctrl32 timer that says 1000 ms waits a second, whatever the cycle is
doing.

The exceptions are marked at the block: PID uses **seconds** for TI and
TD because that is how controllers are tuned everywhere, and the motion
ramps use seconds for the same reason.

## Order of execution

Blocks run in the order they appear in the program, top to bottom. Data
flows between them through tags: block A writes a tag, block B reads it.

That order is yours to get right. A block reading a tag that a *later*
block writes sees the value from the **previous cycle** — one cycle old.
Usually that is harmless; in a fast chain of calculations it is not, and
the fix is to put them in the order the data flows.

!!! tip "Ladder and FBD are the same runtime"
    A rung and a diagram compile to the same blocks and execute the same
    way. Drawing in ladder does not cost anything at runtime, and does
    not limit what you can use — every block below is available as a box
    in a rung with EN/ENO.

## EN and ENO

Any block placed in a ladder rung gets **EN** (enable) and **ENO**:

- the rung conducts → the block executes, ENO carries the rung on
- the rung does not → **the block freezes**: its state is kept and its
  outputs hold their last value

Freezing, not resetting, is deliberate: a timer in a rung that stops
conducting keeps its elapsed time, so a rung that flickers does not
silently restart the measurement. If you want it reset, reset it
explicitly.

## What a block will never do

- **Crash the board.** `DIV` by zero gives 0. An out-of-range index does
  nothing. A block from a newer editor that this firmware does not know
  is skipped with an entry in the diagnostic buffer.
- **Allocate memory while running.** Everything is reserved at compile
  time.
- **Block the cycle.** No block waits for anything; the ones that talk to
  hardware (SMS, SDO, infrared) report progress on their outputs and let
  the cycle carry on.

## Writing your own

The shipped library is not the limit — you can write blocks of your own
in Structured Text and use them exactly like these, no firmware release
involved. See [Structured Text](st-language.md).

The rule of thumb for what stays in C++: hardware access, precise timing
and PID. Everything else is better written in ST, where you can read it,
change it and ship it as data.
