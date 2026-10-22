---
title: "Home automation: ENERGY"
slug: home-energy
section: "Function blocks"
order: 209
sidebar_position: 209
generator: tools/docs_export.py
---

# ENERGY

Kilowatt-hours from a power: E counts kWh from a power in kW, once a second; COST is E times PRICE.

## In Structured Text

```iecst
PROGRAM ENERGY_ST
VAR energy : ENERGY; END_VAR
  energy(P := energy_p, RESET := energy_reset, E_IN := energy_e_in, PRICE := energy_price);
  energy_e := energy.E;
  energy_cost := energy.COST;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `P` | input | REAL | - | The power, kW (a meter's reading). |
| `RESET` | input | BOOL | - | An edge starts from 0. |
| `E_IN` | input | REAL | - | The count to continue from - bind the SAME variable as E. |
| `PRICE` | parameter | REAL | 0.25 | The cost of one kWh. |
| `E` | output | REAL | - | The count, kWh. |
| `COST` | output | REAL | - | E times PRICE. |

## Description

The count lives in the variable bound to `E`: bind it to `E_IN` as well
and mark it retained (*Variables → retain*), and the counter survives a
restart. Without the `E_IN` wire the block counts one second at a time
and forgets.

It uses 2 of the program's 32 timers and edge detectors.

---

Every block of the family: [Home automation](/docs/blocks/blocks-home/) · every block: [Function blocks](/docs/blocks/)
