---
title: "Boolean: SR"
slug: fb-sr
section: "Function blocks"
order: 150
sidebar_position: 150
image: img/blk-sr-ld.webp
image_alt: "SR in the editor"
generator: tools/docs_export.py
---

# SR

Set-dominant latch: remembers, and if set and reset are both TRUE, set wins.

![SR on a rung](img/blk-sr-ld.webp){: .sb-center}

![SR on a WEBview screen](img/blk-sr-web.webp){: .sb-center}

## In Structured Text

```iecst
PROGRAM SR_ST
VAR sr : SR; END_VAR
  sr(S1 := sr_s1, R := sr_r);
  sr_q1_st := sr.Q1;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `S1` | input | BOOL | - | Set. |
| `R` | input | BOOL | - | Reset. |
| `Q1` | output | BOOL | - | The remembered state. |

## Description

The only difference between SR and RS is what happens when set and reset
arrive **together** - and that is exactly the case you have to think
about, because sooner or later both arrive at once.

**Choose by asking which one is the safe answer:**

- A fault latch: a new fault arriving while somebody presses acknowledge
  should stay latched → **SR** (set wins).
- A running flag: a stop arriving while start is held should stop it →
  **RS** (reset wins).

```
fault_detected ──S1─┐
operator_ack   ──R──┤ SR ├── Q1 ──> fault_latched
```

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
