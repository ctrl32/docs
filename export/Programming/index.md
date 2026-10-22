---
title: "Programming"
slug: programming
section: "Programming"
order: 77
sidebar_position: 77
generator: tools/docs_export.py
---

# Programming

The logic is written in the languages a PLC programmer already knows.
Ladder and FBD are two views of the same program — switch between them
any time — and everything compiles into one bytecode that the board
executes. The device never parses text: uploading a program is uploading
data, never firmware.

- [Ladder (LD)](/docs/programming/ladder/) — rungs, contacts, coils and blocks with
  EN/ENO, the way an electrician reads them
- [Function block diagram (FBD)](/docs/programming/fbd-composites/) — the same logic as
  networks of blocks, plus composite blocks you build yourself
- [Structured Text (ST)](/docs/programming/st-language/) — the textual language
  underneath, with the full block library callable from it

Whichever you draw in, the work is done by **function blocks** — 53 of
them, from a timer to a PID controller to a positioning axis. They are
documented group by group:

| | |
|:---|:---|
| [Function blocks](/docs/blocks/) | what they have in common: pins, instances, execution order, EN/ENO |
| [Timers](/docs/blocks/blocks-timers/) · [Counters](/docs/blocks/blocks-counters/) | delays, pulses, blinking, counting |
| [Boolean](/docs/blocks/blocks-boolean/) · [Maths](/docs/blocks/blocks-math/) · [Comparison](/docs/blocks/blocks-compare/) | logic, edges, latches, arithmetic, decisions |
| [Signal handling](/docs/blocks/blocks-signal/) | scaling, clamping, hysteresis, ramps, filtering |
| [Equipment blocks](/docs/blocks/blocks-equipment/) | MOTOR, VALVE and PID — with the parts people forget |
| [Motion](/docs/blocks/blocks-motion/) · [CANopen](/docs/blocks/blocks-can/) | driving an axis, and talking to a drive directly |
| [Services](/docs/blocks/blocks-services/) | infrared, SMS, modem state |

![A ladder program in the editor - the thermostat example](img/ladder-thermostat.webp){: .sb-center}

