---
image: img/blk-ftrig-ld.webp
image_alt: "F_TRIG in the editor"
---

# F_TRIG

Detects a falling edge: Q is TRUE for exactly one cycle after CLK drops.

![F_TRIG on a rung](img/blk-ftrig-ld.webp){: .sb-center}

![F_TRIG on a WEBview screen](img/blk-ftrig-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM F_TRIG_ST
VAR ftrig : F_TRIG; END_VAR
  ftrig(CLK := ftrig_clk);
  ftrig_q_st := ftrig.Q;
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
| `Q` | output | BOOL | - | One cycle of TRUE per falling edge. |

## Description

**What it is for:** reacting to something ending. A part leaving a
sensor, a guard being released, a signal that was there and is not.

!!! tip "One cycle is short"
    An edge pulse lives for a single cycle - 10 ms or so. It is meant to
    be *consumed* by the logic in the same cycle: counted, latched, used
    as a trigger. It is not something a person can see, and it is not
    something a slow device will notice. Latch it if it has to last.

In a ladder rung the same thing is the `-[N]-` falling-edge contact.

---

Every block of the family: [Boolean](blocks-boolean.md) · every block: [Function blocks](blocks.md)
