---
title: "Services: IR_SEND"
slug: fb-ir_send
section: "Function blocks"
order: 182
sidebar_position: 182
image: img/blk-ir-ld.webp
image_alt: "IR_SEND in the editor"
generator: tools/docs_export.py
---

# IR_SEND

Sends an infrared code from the project's IR key table on the rising edge of Execute.

![IR_SEND on a rung](img/blk-ir-ld.webp){: .sb-center}

![IR_SEND on a WEBview screen](img/blk-ir-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM IR_SEND_ST
VAR ir : IR_SEND; END_VAR
  ir(Execute := ir_execute, KEY := 0);
  ir_done_st := ir.Done;
  ir_error_st := ir.Error;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| - | yes | - |

**Needs:** an infrared transmitter on a pin and the project's IR key table.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Execute` | input | BOOL | - | Send on the rising edge. |
| `KEY` | parameter | REAL | 0 | Index into the project's IR key table. |
| `Done` | output | BOOL | - | The code went out (held while Execute holds). |
| `Error` | output | BOOL | - | No transmitter, or KEY out of range. |

## Errors

| When | What it means |
|:---|:---|
| Error | No IR transmitter is configured, or KEY is outside the key table. |

## Description

The codes themselves are not in the logic - they are **learned into the
project** on the peripherals page, where each one gets a number. The
block sends number KEY.

`Done` holds while Execute holds, after a successful transmit.

**What it is for:** driving equipment that has no other interface. Air
conditioning, a projector, a heat pump, a roller door - anything whose
only input is a remote control.

```
temp_too_high ──[R_TRIG]── Execute ──[IR_SEND KEY=2]── Done ──> ac_commanded
```

!!! tip "Infrared is one-way"
    Nothing tells you the air conditioner obeyed. Where it matters,
    measure the result - a temperature that stops rising, a current that
    starts flowing - rather than trusting `Done`, which only means the
    code was transmitted.

The board does the transmitting; the block reports on its outputs and
the cycle carries on - nothing here blocks the cycle. The transmitter is
configured in the project, not in the logic - see
[Peripherals and services](/docs/peripherals-and-services/).

---

Every block of the family: [Services](/docs/blocks/blocks-services/) · every block: [Function blocks](/docs/blocks/)
