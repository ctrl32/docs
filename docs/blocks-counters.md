# Counters

Two blocks: one counts up, one counts down. Both count **edges**, not
states — a signal that stays TRUE counts once, not once per cycle.

---

## CTU — up counter

**A rising edge of CU increments; R resets; Q is TRUE once CV has reached PV.**

| Pin | Type | Meaning |
|---|---|---|
| `CU` | input, bool | count up on the rising edge |
| `R` | input, bool | reset — while TRUE, CV is 0 |
| `PV` | parameter, number (10) | the preset the counter is aiming at |
| `Q` | output, bool | TRUE while CV ≥ PV |
| `CV` | output, number | the count so far |

Reset has priority: while R is TRUE the counter stays at zero and ignores
CU.

**What it is for:** anything you need a quantity of. Parts in a box,
strokes of a press, bottles past a sensor, retries before giving up.

```
part_sensor ──CU─┐
box_changed ──R──┤ CTU PV=24 ├── Q ──> box_full
                 └────────── CV ──> parts_in_box
```

Q comes on at the 24th part and stays on until somebody changes the box.

!!! tip "CV is the number the operator wants to see"
    Bind it to a tag and show it. "24 of 24" tells an operator more than
    a lamp does, and it costs one widget.

---

## CTD — down counter

**A rising edge of CD decrements; LD loads CV = PV; Q is TRUE at zero.**

| Pin | Type | Meaning |
|---|---|---|
| `CD` | input, bool | count down on the rising edge |
| `LD` | input, bool | load — sets CV to PV |
| `PV` | parameter, number (10) | the value LD loads |
| `Q` | output, bool | TRUE while CV ≤ 0 |
| `CV` | output, number | what is left |

A down counter starts life at zero, which means **Q is TRUE before you
load it**. Pulse LD once at startup, or whenever a new batch begins.

**What it is for:** counting down to something. Remaining parts in a
batch, lives left before a fault, doses left in a container.

```
batch_start ──LD─┐
part_done   ──CD─┤ CTD PV=50 ├── Q ──> batch_finished
                 └────────── CV ──> parts_remaining
```

---

## Counting edges, not states

Both blocks look for a **rising edge** — a transition from FALSE to TRUE.
This is what you want almost always: a sensor that stays covered by a
stationary part counts one part, not thousands.

It also means the signal has to **drop** before it can count again. A
sensor that never clears never counts a second time, and that is not the
counter's fault — it is worth checking on the machine when a count seems
stuck.

!!! warning "A bouncing input counts every bounce"
    A mechanical contact can bounce several times in a millisecond, and
    the counter is fast enough to see all of them. Put a short
    [TON](blocks-timers.md#ton-on-delay) in front of a mechanical
    contact, or use the input filtering on the peripheral if it has one.

## Retentive counting

A counter's CV lives in RAM and starts at zero after a power cycle. If a
count has to survive being switched off — parts made this shift, total
operating hours — write CV to a **retentive tag**, and load it back on
startup.

See [Tags](tags.md) for which storage survives what: retentive memory is
limited on purpose, and writing it every cycle wears it out.

## Wider counts

CV is a number, so it counts far past what a 16-bit counter manages. What
it will not do is count forever with single-unit precision — beyond a few
million, the smallest step it can represent grows. For a lifetime part
counter, count *batches* rather than parts, or keep the total in an
integer tag and increment it yourself.
