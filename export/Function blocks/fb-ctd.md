---
title: "Counters: CTD"
slug: fb-ctd
section: "Function blocks"
order: 147
sidebar_position: 147
image: img/blk-ctd-ld.webp
image_alt: "CTD in the editor"
generator: tools/docs_export.py
---

# CTD

Counts down: a rising edge of CD decrements CV, LD loads CV = PV, Q is TRUE at zero.

![CTD on a rung](img/blk-ctd-ld.webp){: .sb-center}

![CTD on a WEBview screen](img/blk-ctd-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM CTD_ST
VAR ctd : CTD; END_VAR
  ctd(CD := ctd_cd, LD := ctd_ld, PV := ctd_pv);
  ctd_q_st := ctd.Q;
  ctd_cv_st := ctd.CV;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `CD` | input | BOOL | - | Count down on the rising edge. |
| `LD` | input | BOOL | - | Load - sets CV to PV. |
| `PV` | parameter | INT | 10 | The value LD loads. |
| `Q` | output | BOOL | - | TRUE while CV <= 0. |
| `CV` | output | INT | - | What is left. |

## Description

A down counter starts life at zero, which means **Q is TRUE before you
load it**. Pulse LD once at startup, or whenever a new batch begins.

**What it is for:** counting down to something. Remaining parts in a
batch, lives left before a fault, doses left in a container.

```
batch_start ──LD─┐
part_done   ──CD─┤ CTD PV=50 ├── Q ──> batch_finished
                 └────────── CV ──> parts_remaining
```

### Counting edges, not states

The block looks for a **rising edge** - a transition from FALSE to TRUE.
A signal that stays TRUE counts once, not once per cycle, and it has to
**drop** before it can count again. A sensor that never clears never
counts a second time - worth checking on the hardware when a count
seems stuck.

!!! warning "A bouncing input counts every bounce"
    A mechanical contact can bounce several times in a millisecond, and
    the counter is fast enough to see all of them. Put a short TON in
    front of a mechanical contact, or use the input filtering on the
    peripheral if it has one.

### Retentive counting

CV lives in RAM and starts at zero after a power cycle. If a count has
to survive being switched off, write CV to a **retentive variable** and
load it back on startup. See [Variables](/docs/editor-overview/variables/) for which storage
survives what: retentive memory is limited on purpose, and writing it
every cycle wears it out.

In a ladder rung CTD can sit in the series itself: the network drives
the count input and Q carries the rung on.

---

Every block of the family: [Counters](/docs/blocks/blocks-counters/) · every block: [Function blocks](/docs/blocks/)
