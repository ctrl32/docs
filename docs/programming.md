# Programming

The logic is written in the languages a PLC programmer already knows.
Ladder and FBD are two views of the same program — switch between them
any time — and everything compiles into one bytecode that the panel
executes. The device never parses text: uploading a program is uploading
data, never firmware.

- [Ladder (LD)](ladder.md) — rungs, contacts, coils and blocks with
  EN/ENO, the way an electrician reads them
- [Function block diagram (FBD)](fbd-composites.md) — the same logic as
  networks of blocks, plus composite blocks you build yourself
- [Structured Text (ST)](st-language.md) — the textual language
  underneath, with the full block library callable from it

Whichever you draw in, the work is done by **function blocks** — 53 of
them, from a timer to a PID controller to a positioning axis. They are
documented group by group:

| | |
|---|---|
| [Function blocks](blocks.md) | what they have in common: pins, instances, execution order, EN/ENO |
| [Timers](blocks-timers.md) · [Counters](blocks-counters.md) | delays, pulses, blinking, counting |
| [Boolean](blocks-boolean.md) · [Maths](blocks-math.md) · [Comparison](blocks-compare.md) | logic, edges, latches, arithmetic, decisions |
| [Signal handling](blocks-signal.md) | scaling, clamping, hysteresis, ramps, filtering |
| [Machine blocks](blocks-machine.md) | MOTOR, VALVE and PID — with the parts people forget |
| [Motion](blocks-motion.md) · [CANopen](blocks-can.md) | driving an axis, and talking to a drive directly |
| [Services](blocks-services.md) | infrared, SMS, modem state |
