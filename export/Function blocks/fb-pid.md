---
title: "Equipment: PID"
slug: fb-pid
section: "Function blocks"
order: 177
sidebar_position: 177
image: img/blk-pid-ld.webp
image_alt: "PID in the editor"
generator: tools/docs_export.py
---

# PID

PID controller with anti-windup, bumpless auto/manual transfer and derivative on the measurement.

![PID on a rung](img/blk-pid-ld.webp){: .sb-center}

![PID on a WEBview screen](img/blk-pid-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM PID_ST
VAR pid : PID; END_VAR
  pid(SP := pid_sp, PV := pid_pv, MAN := pid_man,
      AUTO := pid_auto, KP := pid_kp, TI := pid_ti, TD := pid_td,
      OUT_MIN := pid_out_min, OUT_MAX := pid_out_max);
  pid_out_st := pid.OUT;
  pid_lim_st := pid.LIM;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `SP` | input | REAL | - | Setpoint. |
| `PV` | input | REAL | - | Process value (the measurement). |
| `MAN` | input | REAL | - | Manual output value, used while AUTO is FALSE. |
| `AUTO` | input | BOOL | - | TRUE = automatic, FALSE = manual. |
| `KP` | parameter | REAL | 1 | Proportional gain. |
| `TI` | parameter | seconds | 60 | Integral time, in seconds - 0 disables the I term. |
| `TD` | parameter | seconds | 0 | Derivative time, in seconds - 0 disables the D term. |
| `OUT_MIN` | parameter | REAL | 0 | Lowest output. |
| `OUT_MAX` | parameter | REAL | 100 | Highest output. |
| `OUT` | output | REAL | - | The control output. |
| `LIM` | output | BOOL | - | TRUE while the output is saturated at OUT_MIN or OUT_MAX. |

## Errors

| When | What it means |
|:---|:---|
| LIM | The output is pinned at OUT_MIN or OUT_MAX; the integrator has stopped accumulating (anti-windup). |

## Description

OUT = KP·e + I + D, held within OUT_MIN..OUT_MAX.

Note the units: **TI and TD are in seconds**, not milliseconds. The
other time settings of the library are durations in ms; controllers are
tuned in seconds everywhere in the world, and matching that convention
prevents more mistakes than consistency would.

### The three things that make it usable

**Anti-windup.** When the output is pinned at its limit, the integrator
stops accumulating - it never runs beyond the limits. Without this, a
controller that spends ten minutes asking for more than the equipment
can deliver builds up an enormous integral, and then overshoots wildly
when the process finally responds. `LIM` tells you it is happening.

**Bumpless transfer.** In manual (`AUTO` = FALSE), OUT follows MAN *and
the integrator tracks it*. Switch back to automatic and the output stays
where it was, then moves from there. No jump, no bang.

**Derivative on the measurement, not the error.** A setpoint step would
otherwise produce an enormous derivative kick. This one takes D from PV,
with a TD/8 filter on it, so changing the setpoint moves the output
smoothly.

### Tuning, briefly

1. Start with **TI = 0, TD = 0** - proportional only. Raise KP until the
   process responds briskly and just begins to oscillate, then halve it.
2. Bring in **TI**: start around the process's response time in seconds
   and reduce it until the remaining offset disappears without the loop
   getting sloppy.
3. **Leave TD at 0** unless you have a slow process with real transport
   delay. Derivative amplifies noise, and on most projects it costs more
   than it gives.

!!! tip "Watch it, do not guess"
    Put SP, PV and OUT on one [trend](/docs/operation/) and change one
    parameter at a time. Ten minutes of watching beats an afternoon of
    theory, and the trend is the record of what you did.

!!! warning "Filter the measurement before the controller, gently"
    Noise on PV becomes noise on OUT, and with derivative it becomes a
    lot of noise. A small [PT1](/docs/blocks/blocks-signal/) helps - but every
    millisecond of filtering is a millisecond of delay in the loop, so
    use as little as works.

---

Every block of the family: [Equipment](/docs/blocks/blocks-equipment/) · every block: [Function blocks](/docs/blocks/)
