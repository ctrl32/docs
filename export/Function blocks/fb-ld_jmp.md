---
title: "Ladder: LD_JMP"
slug: fb-ld_jmp
section: "Function blocks"
order: 189
sidebar_position: 189
generator: tools/docs_export.py
---

# LD_JMP

Jump: while its network conducts, the networks between it and network N are skipped this cycle.

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `N` | parameter | REAL | 0 | The target network, 1-based. |

## Description

A ladder element at the end of a network, `-( JMP )-`, not a block one
places; it has no pins of its own beside the target. The coil's kind
list and the menu's **Coil type** offer `(JMP)`, and a lower row of a
branch may end in one too.

- A fresh jump aims at the next network; the sheet's field changes the
  target.
- While the network conducts, the networks between the jump and its
  target are **skipped** this cycle.
- A jump goes **forward** only; two jumps either nest or stay apart.
- The whole network is evaluated before the jump is taken - every coil
  of it is written.
- The header of a network that is a jump's target reads in the full
  colour, so the landing place is visible from anywhere.

A jump backwards, past the end, or across another jump's target is
refused at the desk with the network named. In test mode a jump lights
while it fires. See [Ladder](/docs/programming/ladder/).

---

Every block of the family: [Ladder](/docs/programming/ladder/) · every block: [Function blocks](/docs/blocks/)
