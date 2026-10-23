---
title: "Cellular modems"
slug: peripherals-connectivity
section: "Chips and services"
order: 330
sidebar_position: 330
generator: tools/docs_export.py
---

# Cellular modems

Six modems that give a board its own connection to the world — no site
network, no IT department, no cable.

This is how a setup in a field, a pump station or somebody else's
building sends an alarm at three in the morning.

## Choosing

| You need | Reach for |
|:---|:---:|
| SMS only, cheapest, 2G | `SIM800L` |
| SMS and data, 2G, with GPS | `SIM808` |
| LTE-M / NB-IoT — the modern low-power networks | `SIM7080G`, `ADRASTEA` |
| LTE-M / NB-IoT **and** GPS | `SIM7000G` |
| full LTE where bandwidth matters | `EC25` |

**Check what your country still runs.** 2G is switched off in a growing
number of places, and a `SIM800L` on a dead network is a dead board.
LTE-M and NB-IoT are the replacements built for this kind of device —
low power, good building penetration, small data.

## What a modem gives the program

Three blocks — see [Service blocks](/docs/blocks/blocks-services/):

- **`SMS_SEND`** sends a message from the project's table
- **`GSM_INFO`** reports whether the modem is registered and how strong
  the signal is
- the modules with GPS also feed position and time into variables

Message texts and phone numbers live in the **project**, not the logic —
so changing a number when somebody changes job is an edit and an upload,
not a program change.

## The traps

!!! warning "A modem needs current the moment it transmits"
    Transmission bursts pull far more than the average — hundreds of
    milliamps, briefly. A supply sized for the average browns out on the
    first burst, and the symptom is a board that resets when it tries to
    send. Size the supply for the peak and put a capacitor next to the
    modem.

!!! warning "Signal strength is measured where the antenna is"
    Not where the phone in your pocket has bars. An enclosure is a
    Faraday cage; an antenna inside a steel cabinet may see nothing at
    all. Show `GSM_INFO`'s signal on a screen during installation so the
    person mounting the board can find a spot that works — instead of
    discovering the problem months later when the first real alarm fails
    to arrive.

!!! tip "Rate-limit what you send"
    A fault that chatters can send hundreds of messages and a bill to
    match. One fault, one message: a delay in front of the trigger and a
    latch behind it.

!!! danger "SMS is a notification, never a control path"
    Messages get delayed, dropped and duplicated by networks you do not
    control. Nothing on the equipment may depend on one arriving.

## The chips

### Connectivity

| Chip | Bus | What it is |
|:---|:---:|:---|
| `ADRASTEA` | serial | Würth Adrastea-I cellular module (Sony ALT1250): LTE-M + NB-IoT + GNSS in one module, 3.0–3.6 V, AT over UART. Used by the gsm: service (SMS alarms), not a pin chip; its GNSS replaces a separate gps: receiver. PPP data dials but the module FW 06.006 wedges its IPCP on a standard ConfRej — until a module FW fixes it, gsm data: needs an EC25/SIM7xxx instead. European supply chain and operator certificates — the product-line pick. |
| `EC25` | serial | Quectel EC25 cellular module: LTE Cat 4 with 2G/3G fallback, GNSS variants, AT over UART. Used by the gsm: service, not a pin chip. Higher data rates and legacy fallback where LTE-M coverage is thin. |
| `SIM7000G` | serial | SIMCom SIM7000G cellular module: LTE-M + NB-IoT + 2G fallback + GNSS, AT over UART. Used by the gsm: service, not a pin chip. The budget alternative to the Adrastea-I. |
| `SIM7080G` | serial | SIMCom SIM7080G cellular module: LTE-M + NB-IoT + GNSS (no 2G), AT over UART. Used by the gsm: service, not a pin chip. |
| `SIM800L` | serial | SIMCom SIM800L cellular module: 2G GSM/GPRS only, AT over UART. Used by the gsm: service, not a pin chip. CAUTION: 2 A supply bursts and the EU 2G phase-out — prototype use, not for the product. |
| `SIM808` | serial | SIMCom SIM808 cellular module: 2G GSM/GPRS + GNSS in one module (AT+CGNSPWR/CGNSINF — the SIM7000 dialect), AT over UART, separate GPS antenna connector. Used by the gsm: service, not a pin chip. Same 2 A supply bursts and 2G phase-out caution as the SIM800L. |

Every entry above is in the editor: pick the chip, give it
an address or a chip-select pin, and its channels become variables.
See [Adding a peripheral](/docs/buses/adding-peripherals/) for the
click-through.
