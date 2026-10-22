---
title: "Boolean: RS"
slug: fb-rs
section: "Function blocks"
order: 151
sidebar_position: 151
image: img/blk-rs-ld.webp
image_alt: "RS in the editor"
generator: tools/docs_export.py
---

# RS

Reset-dominant latch: remembers, and if set and reset are both TRUE, reset wins.

![RS on a rung](img/blk-rs-ld.webp){: .sb-center}

![RS on a WEBview screen](img/blk-rs-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM RS_ST
VAR rs : RS; END_VAR
  rs(S := rs_s, R1 := rs_r1);
  rs_q1_st := rs.Q1;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `S` | input | BOOL | - | Set. |
| `R1` | input | BOOL | - | Reset. |
| `Q1` | output | BOOL | - | The remembered state. |

## Description

The only difference between RS and SR is what happens when set and reset
arrive **together** - and that is exactly the case you have to think
about, because sooner or later both arrive at once.

**Choose by asking which one is the safe answer:**

- A fault latch: a new fault arriving while somebody presses acknowledge
  should stay latched → **SR** (set wins).
- A running flag: a stop arriving while start is held should stop it →
  **RS** (reset wins).

!!! danger "A latch is not a safety function"
    Reset priority is not a substitute for a hard-wired stop circuit.
    Emergency stop, guards and light curtains are wired, not programmed -
    see [Intended use](/docs/about/intended-use/).

### Latch or coil?

Ladder has set and reset coils (`-(S)-`, `-(R)-`), which do the same
thing as this block. The difference is where the decision lives:

- **Coils** put set and reset on separate rungs. Easy to read, and the
  priority is decided by which rung comes last.
- **A latch block** puts both on one line with the priority written into
  the block name, where nobody can miss it.

For anything where the both-at-once case matters, the block is the
clearer choice.

---

Every block of the family: [Boolean](/docs/blocks/blocks-boolean/) · every block: [Function blocks](/docs/blocks/)
