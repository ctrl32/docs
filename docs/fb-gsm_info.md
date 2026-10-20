---
image: img/blk-gsm-ld.webp
image_alt: "GSM_INFO in the editor"
---

# GSM_INFO

Reports the modem's state to the logic: registered on the network, and the signal strength.

![GSM_INFO on a rung](img/blk-gsm-ld.webp){: .sb-center}

![GSM_INFO on a WEBview screen](img/blk-gsm-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM GSM_INFO_ST
VAR gsm : GSM_INFO; END_VAR
  gsm(Enable := gsm_enable);
  gsm_ready_st := gsm.Ready;
  gsm_signal_st := gsm.Signal;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| - | yes | - |

**Needs:** a cellular modem.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Enable` | input | BOOL | - | Read the modem state. |
| `Ready` | output | BOOL | - | Registered on the network - SMS is possible. |
| `Signal` | output | REAL | - | Last signal reading, 0–31. |

## Errors

| When | What it means |
|:---|:---|
| Ready = FALSE | The modem is not registered on the network (or no modem is configured) - an SMS cannot go out now. |
| Signal = 0 | No signal, or not measured yet. |

## Description

The logic-facing view of the modem. `Ready` is the pin to gate SMS
sending on: attempting to send while the modem is not registered wastes
a trigger.

`Signal` is the raw +CSQ reading, refreshed about every 30 seconds:

| Value | Meaning |
|:---|:---:|
| 0 | no signal - **or not measured yet** |
| 1–9 | marginal, expect failures |
| 10–14 | usable |
| 15–31 | good |

Without a configured modem, both outputs stay 0.

```
Enable ──[GSM_INFO]── Ready ──┐
fault_latched ─────────────────┤ AND ├── Execute ──[SMS_SEND]
```

!!! tip "Show the signal on a screen during installation"
    The person mounting the board can then find a spot where the antenna
    works, instead of discovering the problem months later when the
    first real alarm fails to arrive.

!!! note "There is also a status variable"
    A modem status variable carries the same information to *screens*.
    This block is the version for *logic* - interlocks and retry gating.
    Use whichever fits where you are working.

---

Every block of the family: [Services](blocks-services.md) · every block: [Function blocks](blocks.md)
