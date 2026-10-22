---
title: "Equipment blocks"
slug: blocks-equipment
section: "Function blocks"
order: 89
sidebar_position: 89
generator: tools/docs_export.py
---

# Equipment blocks

Three blocks that anyone controlling equipment ends up needing, and that
ctrl32 ships so you do not have to write them: a motor starter, a valve,
and a PID controller.

They are bigger than the rest of the library because they contain the
parts that are easy to forget — feedback supervision, latched faults, an
acknowledge that only works when it is safe, and an integrator that does
not wind up.

---

## The blocks

<!-- fb-index: begin -->

| Block | What it does | Linux | ESP32 | STM32 |
|:---|:---|:---:|:---:|:---:|
| [MOTOR](/docs/blocks/fb-motor/) | Motor starter with feedback supervision: START raises CMD, FB must confirm within T_FB, otherwise a latched FAULT. | yes | yes | yes |
| [VALVE](/docs/blocks/fb-valve/) | Valve with end-position check: OPEN opens, CLOSE has priority, FB must arrive within T_FB, otherwise a latched FAULT. | yes | yes | yes |
| [PID](/docs/blocks/fb-pid/) | PID controller with anti-windup, bumpless auto/manual transfer and derivative on the measurement. | yes | yes | yes |

<!-- fb-index: end -->
