---
title: "Equipment: VALVE"
slug: fb-valve
section: "Function blocks"
order: 176
sidebar_position: 176
image: img/blk-valve-ld.webp
image_alt: "VALVE in the editor"
generator: tools/docs_export.py
---

# VALVE

Valve with end-position check: OPEN opens, CLOSE has priority, FB must arrive within T_FB, otherwise a latched FAULT.

![VALVE on a rung](img/blk-valve-ld.webp){: .sb-center}

![VALVE on a WEBview screen](img/blk-valve-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM VALVE_ST
VAR valve : VALVE; END_VAR
  valve(OPEN := valve_open, CLOSE := valve_close, FB := valve_fb,
        ACK := valve_ack, T_FB := valve_t_fb);
  valve_cmd_st := valve.CMD;
  valve_fault_st := valve.FAULT;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `OPEN` | input | BOOL | - | Open command. |
| `CLOSE` | input | BOOL | - | Close command - has priority. |
| `FB` | input | BOOL | - | End-position feedback. |
| `ACK` | input | BOOL | - | Acknowledge a fault. |
| `T_FB` | parameter | TIME | T#5s | How long the travel may take. |
| `CMD` | output | BOOL | - | The valve output. |
| `FAULT` | output | BOOL | - | Latched fault. |

## Errors

| When | What it means |
|:---|:---|
| FAULT | The valve did not reach its end position within T_FB - jammed, no air, a broken limit switch, or a travel longer than T_FB. Stays latched until ACK. |

## Description

The same shape as MOTOR, with the timing a valve needs: T_FB defaults to
five seconds because a valve has to physically travel, and CLOSE wins
over OPEN because closed is the safer state for most processes.

```
recipe_step ──OPEN──┐
  e_stop_ok ──CLOSE─┤            ├── CMD   ──> valve_solenoid
   limit_sw ──FB────┤ VALVE      ├── FAULT ──> valve_stuck
     ack_pb ──ACK───┘ T_FB=T#5s
```

A latched FAULT here means the valve did not reach its end position in
time - jammed, no air, a broken limit switch, or a travel time that is
simply longer than T_FB on a cold morning. All four are worth knowing
about.

!!! tip "Set T_FB from the real thing, not the catalogue"
    Watch the actual travel time in the [Scope](/docs/operation/scope/), then give it
    generous headroom - perhaps double. A T_FB set too tight produces
    nuisance faults on a cold morning, and nuisance faults teach whoever
    is using it to acknowledge without looking, which is worse than no
    fault at all.

---

Every block of the family: [Equipment](/docs/blocks/blocks-equipment/) · every block: [Function blocks](/docs/blocks/)
