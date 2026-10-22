---
title: "Equipment: MOTOR"
slug: fb-motor
section: "Function blocks"
order: 175
sidebar_position: 175
image: img/blk-motor-ld.webp
image_alt: "MOTOR in the editor"
generator: tools/docs_export.py
---

# MOTOR

Motor starter with feedback supervision: START raises CMD, FB must confirm within T_FB, otherwise a latched FAULT.

![MOTOR on a rung](img/blk-motor-ld.webp){: .sb-center}

![MOTOR on a WEBview screen](img/blk-motor-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM MOTOR_ST
VAR motor : MOTOR; END_VAR
  motor(START := motor_start, STOP := motor_stop, FB := motor_fb,
        ACK := motor_ack, T_FB := motor_t_fb);
  motor_cmd_st := motor.CMD;
  motor_fault_st := motor.FAULT;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `START` | input | BOOL | - | Start command. |
| `STOP` | input | BOOL | - | Stop command - overrides START. |
| `FB` | input | BOOL | - | Feedback: the motor is actually running. |
| `ACK` | input | BOOL | - | Acknowledge a fault (works only at standstill). |
| `T_FB` | parameter | TIME | T#3s | How long the feedback may take. |
| `CMD` | output | BOOL | - | The contactor command. |
| `FAULT` | output | BOOL | - | Latched fault. |

## Errors

| When | What it means |
|:---|:---|
| FAULT | FB did not confirm within T_FB after CMD went on; CMD has dropped. Stays latched until ACK at standstill. |

## Description

What it does, in order:

1. START raises CMD - unless STOP is present, which always wins.
2. From then on, **FB must confirm within T_FB**. If it does not, FAULT
   latches and CMD drops.
3. FAULT stays latched until ACK - and **ACK only works at standstill**,
   so nobody can acknowledge a fault into a running motor.

```
   start_pb ──START─┐
    stop_pb ──STOP──┤            ├── CMD   ──> contactor
aux_contact ──FB────┤ MOTOR      ├── FAULT ──> motor_fault
     ack_pb ──ACK───┘ T_FB=T#3s
```

**Why the feedback matters.** Without it, a blown fuse, a tripped
overload or a contactor that welded open looks exactly like a running
motor: the command is on and the program is content. With it, the
program knows within three seconds that what it asked for did not
happen - instead of carrying on as though it had.

!!! tip "Wire the feedback to the thing you want to be sure of"
    An auxiliary contact on the contactor proves the coil pulled in. A
    current relay proves current is flowing. A speed switch proves the
    shaft is turning. Each one catches more failures than the one before
    it, and costs a little more.

!!! warning "STOP is not an emergency stop"
    STOP is a command in software. Emergency stop is a wired circuit
    that removes power without asking the program. See
    [Intended use](/docs/about/intended-use/).

---

Every block of the family: [Equipment](/docs/blocks/blocks-equipment/) · every block: [Function blocks](/docs/blocks/)
