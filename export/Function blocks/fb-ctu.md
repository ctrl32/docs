---
title: "Counters: CTU"
slug: fb-ctu
section: "Function blocks"
order: 146
sidebar_position: 146
image: img/blk-ctu-ld.webp
image_alt: "CTU in the editor"
generator: tools/docs_export.py
---

# CTU

Counts up: a rising edge of CU increments CV, R resets it, Q is TRUE once CV has reached PV.

![CTU on a rung](img/blk-ctu-ld.webp){: .sb-center}

![CTU on a WEBview screen](img/blk-ctu-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM CTU_ST
VAR ctu : CTU; END_VAR
  ctu(CU := ctu_cu, R := ctu_r, PV := ctu_pv);
  ctu_q_st := ctu.Q;
  ctu_cv_st := ctu.CV;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `CU` | input | BOOL | - | Count up on the rising edge. |
| `R` | input | BOOL | - | Reset - while TRUE, CV is 0. |
| `PV` | parameter | INT | 10 | The preset the counter is aiming at. |
| `Q` | output | BOOL | - | TRUE while CV >= PV. |
| `CV` | output | INT | - | The count so far. |

## Description

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
    Bind it to a variable and show it. "24 of 24" tells an operator more
    than a lamp does, and it costs one widget.

### Counting edges, not states

The block looks for a **rising edge** - a transition from FALSE to TRUE.
A signal that stays TRUE counts once, not once per cycle: a sensor that
stays covered by a stationary part counts one part, not thousands. It
also means the signal has to **drop** before it can count again. A
sensor that never clears never counts a second time, and that is not the
counter's fault - it is worth checking on the hardware when a count
seems stuck.

!!! warning "A bouncing input counts every bounce"
    A mechanical contact can bounce several times in a millisecond, and
    the counter is fast enough to see all of them. Put a short TON in
    front of a mechanical contact, or use the input filtering on the
    peripheral if it has one.

### Retentive counting

CV lives in RAM and starts at zero after a power cycle. If a count has
to survive being switched off - parts made this shift, total operating
hours - write CV to a **retentive variable**, and load it back on
startup. See [Variables](/docs/editor-overview/variables/) for which storage survives what:
retentive memory is limited on purpose, and writing it every cycle wears
it out.

### Wider counts

CV counts far past what a 16-bit counter manages. For a lifetime part
counter, count *batches* rather than parts, or keep the total in an
integer variable and increment it yourself.

In a ladder rung CTU can sit in the series itself: the network drives
the count input and Q carries the rung on.

---

Every block of the family: [Counters](/docs/blocks/blocks-counters/) · every block: [Function blocks](/docs/blocks/)
