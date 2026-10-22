---
title: "Timers: TP"
slug: fb-tp
section: "Function blocks"
order: 144
sidebar_position: 144
image: img/blk-tp-ld.webp
image_alt: "TP in the editor"
generator: tools/docs_export.py
---

# TP

Fires a fixed pulse: a rising edge of IN makes Q TRUE for exactly PT (non-retriggerable).

![TP on a rung](img/blk-tp-ld.webp){: .sb-center}

![TP on a WEBview screen](img/blk-tp-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM TP_ST
VAR tp : TP; END_VAR
  tp(IN := tp_in, PT := tp_pt);
  tp_q_st := tp.Q;
  tp_et_st := tp.ET;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN` | input | BOOL | - | Trigger, on the rising edge. |
| `PT` | parameter | TIME | T#1s | Pulse length. |
| `Q` | output | BOOL | - | TRUE for PT after the trigger. |
| `ET` | output | TIME | - | Time into the pulse. |

## Description

The pulse is **non-retriggerable**: while it is running, further rising
edges of IN are ignored. It also does not care what IN does afterwards -
once started, the pulse runs its full length even if IN drops
immediately.

**What it is for:** a fixed dose of something. A puff of air, a squirt of
lubricant, a horn before a start, a solenoid that must not be energised
longer than it can take.

```
start_button ──[TP PT=T#500ms]── Q ──> horn
```

Half a second of horn, whether the operator taps the button or leans on
it.

!!! warning "Non-retriggerable matters"
    If you want a pulse that *restarts* on every edge, TP is the wrong
    block - use a rising edge into a TON reset, or hold the trigger in
    an RS latch that the pulse clears.

In a ladder rung TP can sit in the series itself: the network drives
IN and Q carries the rung on.

### Choosing between the timers

| You want | Block |
|:---|:---:|
| ignore a signal until it has held | **TON** |
| keep something running after the reason stopped | **TOF** |
| a fixed dose, regardless of how long the trigger lasts | **TP** |
| something that flashes | **BLINK** |

The time is a duration written the IEC way (`T#500ms`); a bare number
means milliseconds. The block measures real elapsed time, never cycles.

---

Every block of the family: [Timers](/docs/blocks/blocks-timers/) · every block: [Function blocks](/docs/blocks/)
