---
title: "Counters"
slug: blocks-counters
section: "Function blocks"
order: 84
sidebar_position: 84
generator: tools/docs_export.py
---

# Counters

Two blocks: one counts up, one counts down. Both count **edges**, not
states — a signal that stays TRUE counts once, not once per cycle.

---

## The blocks

<!-- fb-index: begin -->

| Block | What it does | Linux | ESP32 | STM32 |
|:---|:---|:---:|:---:|:---:|
| [CTU](/docs/blocks/fb-ctu/) | Counts up: a rising edge of CU increments CV, R resets it, Q is TRUE once CV has reached PV. | yes | yes | yes |
| [CTD](/docs/blocks/fb-ctd/) | Counts down: a rising edge of CD decrements CV, LD loads CV = PV, Q is TRUE at zero. | yes | yes | yes |

<!-- fb-index: end -->

## Counting edges, not states

Both blocks look for a **rising edge** — a transition from FALSE to TRUE.
This is what you want almost always: a sensor that stays covered by a
stationary part counts one part, not thousands.

It also means the signal has to **drop** before it can count again. A
sensor that never clears never counts a second time, and that is not the
counter's fault — it is worth checking on the hardware when a count seems
stuck.

!!! warning "A bouncing input counts every bounce"
    A mechanical contact can bounce several times in a millisecond, and
    the counter is fast enough to see all of them. Put a short
    [TON](/docs/blocks/fb-ton/) in front of a mechanical
    contact, or use the input filtering on the peripheral if it has one.

## Retentive counting

A counter's CV lives in RAM and starts at zero after a power cycle. If a
count has to survive being switched off — parts made this shift, total
operating hours — write CV to a **retentive variable**, and load it back on
startup.

See [Variables](/docs/editor-overview/variables/) for which storage survives what: retentive memory is
limited on purpose, and writing it every cycle wears it out.

## Wider counts

CV is a number, so it counts far past what a 16-bit counter manages. What
it will not do is count forever with single-unit precision — beyond a few
million, the smallest step it can represent grows. For a lifetime part
counter, count *batches* rather than parts, or keep the total in an
integer variable and increment it yourself.
