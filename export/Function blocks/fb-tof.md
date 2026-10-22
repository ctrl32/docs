---
title: "Timers: TOF"
slug: fb-tof
section: "Function blocks"
order: 143
sidebar_position: 143
image: img/blk-tof-ld.webp
image_alt: "TOF in the editor"
generator: tools/docs_export.py
---

# TOF

Delays switching off: Q follows IN on at once and stays on for another PT after IN drops.

![TOF on a rung](img/blk-tof-ld.webp){: .sb-center}

![TOF on a WEBview screen](img/blk-tof-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM TOF_ST
VAR tof : TOF; END_VAR
  tof(IN := tof_in, PT := tof_pt);
  tof_q_st := tof.Q;
  tof_et_st := tof.ET;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `IN` | input | BOOL | - | The condition. |
| `PT` | parameter | TIME | T#1s | How long Q holds after IN drops. |
| `Q` | output | BOOL | - | TRUE while IN is TRUE, and PT longer. |
| `ET` | output | TIME | - | How long since IN dropped. |

## Description

Q switches on **immediately** with IN. Only the switching off is delayed.

**What it is for:** run-on. A fan that keeps going after the heater stops.
A lamp that stays lit a moment after the last motion. A conveyor that
finishes carrying what is already on it.

```
heater_on ──[TOF PT=T#30s]── Q ──> fan
```

The fan runs while the heater does, and half a minute after it - no extra
logic, no timer you have to reset.

In a ladder rung TOF can sit in the series itself: the network drives
IN and Q carries the rung on. As a box with EN/ENO, a rung that stops
conducting keeps the block's state and its outputs hold their last value.

### Choosing between the timers

| You want | Block |
|:---|:---:|
| ignore a signal until it has held | **TON** |
| keep something running after the reason stopped | **TOF** |
| a fixed dose, regardless of how long the trigger lasts | **TP** |
| something that flashes | **BLINK** |

### Real time, not cycles

The time is a duration written the IEC way (`T#500ms`, `T#1s500ms`,
`T#2m`); a bare number typed into the field means milliseconds. The
block measures real elapsed time on a monotonic millisecond clock, so a
stretched cycle does not stretch the delay. Never build a timer by
counting cycles.

---

Every block of the family: [Timers](/docs/blocks/blocks-timers/) · every block: [Function blocks](/docs/blocks/)
