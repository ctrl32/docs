---
title: "Adding a peripheral"
slug: adding-peripherals
section: "Protocols"
order: 317
sidebar_position: 317
generator: tools/docs_export.py
---

# Adding peripherals to a board

A fifteen-second procedure: open the board, right-click to add a chip to
a bus, and it is in the project. The demonstration runs on the **inoCORE32-TM**
board and adds a TCA9555 expander and an ADS1115 converter to I2C.

![The device catalog: pick the chip, the bus rules decide where it may sit](img/board-catalog.webp){: .sb-center}

What those peripherals do at run time — mapping pins onto variables,
converter ranges — is described in
[Board peripherals and system services](/docs/peripherals-and-services/).

> **Pins are not configured at run time.** A peripheral added in the
> editor is **compile-time** configuration: it goes into the pack and
> the board reads it at startup. The pin assignment never changes while
> running — a deliberate decision that protects you from a badly
> uploaded project switching a pin that has something else on it.
