---
title: "Ladder: LD_RET"
slug: fb-ld_ret
section: "Function blocks"
order: 188
sidebar_position: 188
generator: tools/docs_export.py
---

# LD_RET

Return: while its network conducts, the program ends here for this cycle.

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|

## Description

A ladder element at the end of a network, `-( RET )-`, not a block one
places; it has no pins. The coil's kind list and the menu's **Coil
type** offer `(RET)`, and a lower row of a branch may end in one too.

While the network conducts, the program ends for this cycle - the
networks after it do not run. The whole network is evaluated first:
every coil of it is written.

In test mode a return lights while it fires. See [Ladder](/docs/programming/ladder/).

---

Every block of the family: [Ladder](/docs/programming/ladder/) · every block: [Function blocks](/docs/blocks/)
