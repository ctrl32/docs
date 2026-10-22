---
title: "Services"
slug: blocks-services
section: "Function blocks"
order: 139
sidebar_position: 139
generator: tools/docs_export.py
---

# Service blocks

Blocks that let the program reach a service the board provides:
infrared, SMS, the modem's own state, and the diagnostics of a vehicle
control unit.

They share a shape. The board does the slow work — a modem takes seconds
to send an SMS — while the block reports progress on its outputs and the
cycle carries on. Nothing here ever blocks the equipment.

---

## The blocks

<!-- fb-index: begin -->

| Block | What it does | Linux | ESP32 | STM32 |
|:---|:---|:---:|:---:|:---:|
| [IR_SEND](/docs/blocks/fb-ir_send/) | Sends an infrared code from the project's IR key table on the rising edge of Execute. | - | yes | - |
| [SMS_SEND](/docs/blocks/fb-sms_send/) | Sends an SMS from the project's message table on the rising edge of Execute. | - | yes | - |
| [GSM_INFO](/docs/blocks/fb-gsm_info/) | Reports the modem's state to the logic: registered on the network, and the signal strength. | - | yes | - |
| [UDS_DTC](/docs/blocks/fb-uds_dtc/) | Reads the fault codes out of a diagnostic control unit on the rising edge of Execute. | yes | - | - |
| [UDS_CLEAR](/docs/blocks/fb-uds_clear/) | Clears the fault codes of a diagnostic control unit on the rising edge of Execute. | yes | - | - |
| [UDS_READ](/docs/blocks/fb-uds_read/) | Asks a diagnostic control unit for one data identifier now, without waiting for its row's period. | yes | - | - |

<!-- fb-index: end -->

## Diagnostics: asking a control unit

On a vehicle bus a control unit answers questions: what the fault codes
are, what a measured value is right now. The values a project reads
regularly are set up on the Diagnostics node and arrive on their own —
no program is needed for them. These three blocks are for what a
**person** sets off: read the faults, clear them, ask once.

They run on the Linux runtime, which carries the diagnostic transport; on
any other device every block reports `Error`. Each block has its own
page in the list above.

---

## Configuring the services

None of these blocks configure anything. The IR transmitter, the modem,
the message texts and the phone numbers are all set up in the project,
on the peripherals and modem pages — see [Peripherals and
services](/docs/peripherals-and-services/).

That separation is deliberate: a phone number changes when somebody
changes job, and that should be an edit in a form, not a change to the
equipment's logic.
