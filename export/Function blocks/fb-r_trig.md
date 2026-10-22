---
title: "Boolean: R_TRIG"
slug: fb-r_trig
section: "Function blocks"
order: 148
sidebar_position: 148
image: img/blk-rtrig-ld.webp
image_alt: "R_TRIG in the editor"
generator: tools/docs_export.py
---

# R_TRIG

Detects a rising edge: Q is TRUE for exactly one cycle after CLK rises.

![R_TRIG on a rung](img/blk-rtrig-ld.webp){: .sb-center}

![R_TRIG on a WEBview screen](img/blk-rtrig-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM R_TRIG_ST
VAR rtrig : R_TRIG; END_VAR
  rtrig(CLK := rtrig_clk);
  rtrig_q_st := rtrig.Q;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `CLK` | input | BOOL | - | The signal being watched. |
| `Q` | output | BOOL | - | One cycle of TRUE per rising edge. |

## Description

**What it is for:** turning "it is on" into "it just turned on". A button
held down should start one thing, not restart it a hundred times a
second.

```
start_button ──[R_TRIG]── Q ──> begin_cycle
```

!!! tip "One cycle is short"
    An edge pulse lives for a single cycle - 10 ms or so. It is meant to
    be *consumed* by the logic in the same cycle: counted, latched, used
    as a trigger. It is not something a person can see, and it is not
    something a slow device will notice. Latch it if it has to last.

In a ladder rung the same thing is the `-[P]-` rising-edge contact.

---

Every block of the family: [Boolean](/docs/blocks/blocks-boolean/) · every block: [Function blocks](/docs/blocks/)
