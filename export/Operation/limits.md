---
title: "Performance and limits"
slug: limits
section: "Operation"
order: 339
sidebar_position: 339
generator: tools/docs_export.py
---

# Performance and limits

Every number on this page is **measured**, not estimated, and measured on
the **slowest board we support** — a classic ESP32 at 240 MHz with Ethernet,
WEBview and a CAN master running alongside. A faster board (S3, P4) has more
headroom, not less.

## Declared limits

The editor refuses a project that exceeds them **at your desk** — not as a
stuttering board in a real setup. They are also the numbers for the datasheet.

Every target is one of **three types**: with a display, headless, or
the [Linux runtime](/docs/hardware/linux-runtime/). A board with glass spends its
RAM on rendering; a headless board spends the same RAM on a bigger
program; a Linux device has gigabytes and carries many times
everything. You pick the type by picking the target — nothing to
configure.

| Limit | With display | Headless | Linux |
|:---|:---:|:---:|:---:|
| Variables | 512 | 512 | **20 480** |
| 64-bit variables (LINT, ULINT, LREAL) | 64 | 64 | **2 048** |
| Alarms | 128 | 128 | **4 096** |
| Screens | 32 | 32 (WEBview) | **1 024** |
| Widgets per screen | 64 | 64 | **1 024** |
| Programs | 8 | 8 | **128** |
| LD/FBD blocks | 512 | **1024** | **40 960** |
| Compiled program | 32 kB | **64 kB** | **4 MB** (64 kB per program) |
| Instance data | 8 kB | **24 kB** | **4 MB** (256 kB per program) |
| Function block instances per program | 32 | 32 | **256** |
| Trend curves (per chart) | 4 | 4 | 4 |
| Trend curves (whole project) | 8 (classic ESP32: 4) | 8 (classic ESP32: 4) | **32** |
| WEBview clients (ESP32; STM32F7: 1) | 2 | 2 | **16** |
| Axes (drives) | 4 | 4 | **64** |
| PLC tasks | 4 | 4 | 4 |

**ESP32-P4 boards.** Their 32 MB of PSRAM carry a bigger table: every
ESP32-P4 board, with a display or headless, holds **4 096 variables**,
**512 alarms** and **256 widgets per screen**. Everything else on it is
the number of its type above. The editor knows it from the board you
pick — nothing to configure.

**Vehicle buses.** A project that speaks
[J1939](/docs/buses/vehicle-buses/) — on a truck, a boat or a tractor — holds:

| Limit | How many |
|:---|:---:|
| Networks (one per CAN interface) | 4 |
| Control units on them | 32 |
| Parameter groups | 64 |
| Signals in those groups | 256 |
| A message assembled from many frames | 1785 bytes on a Linux device, 512 on a panel |
| Control units asked over [diagnostics](/docs/buses/vehicle-diagnostics/) | 8 |
| Values read out of them | 64 |

**The LITE class.** An ESP32 without PSRAM (the classic WROOM-32
module and the boards built on it) has 320 kB of internal RAM for
everything, and the tables sized by the variable limit sit all over
the runtime. Such a board carries **128 variables, 32 alarms, 128
blocks and 1 axis** - with those numbers the same board runs the
display, WiFi with its access point, CAN and WEBview together. The
board's catalog card says which class it is, the editor refuses a
bigger project at your desk and the runtime refuses a bigger pack.
The classes and their boards are listed in the
[module catalog](/docs/hardware/modules/).

The Linux numbers are not paper: a generated proof project — 600
variables, 40 screens of ~96 widgets each — runs on the reTerminal
with the logic cycling at 10 ms and every variable served over
[OPC UA](/docs/buses/opcua/).

## How many blocks really fit

The program is N AND blocks over 150 variables — every block reads two variables and
writes one, which is the worst realistic ratio:

| Blocks | Average cycle | Of a 10 ms period |
|:---|:---:|:---:|
| 64 | 110 µs | 1.1 % |
| 100 | 153 µs | 1.5 % |
| 200 | 274 µs | 2.7 % |
| **400** | **515 µs** | **5.2 %** |

400 blocks run on the weakest board we support with a cycle that is 95 %
idle; 600 blocks measure 641 µs on a headless classic board — the
1024-block headless limit extrapolates to ~1.1 ms, 11 % of the cycle. The declared limit of 512 is not a performance boundary but a
program-size budget: a simple block costs ~10 B of the compiled
program, so 512 blocks take 16 % of the 32 kB.

In practice the **variable table** (512) runs out sooner than the blocks do.

## A real program, not a synthetic test

| Program | ST lines | Variables | Cycle |
|:---|:---:|:---:|:---:|
| half an installation | 100 | 110 | 168 µs |
| **a full installation** | 190 | 215 | **304 µs** |

"A full installation" means: 40 analog inputs scaled and alarmed, 30 motors with
interlocks, a 40-step sequence and a positioning ramp. **3 % of a 10 ms
cycle**, zero overruns.

A realistic ST line costs ~1.6 µs, a ladder block ~1.3 µs.

## What the cycle actually spends its time on

The interesting part: **it is not the arithmetic, it is variable access.** A
synthetic loop over local variables runs at 0.145 µs per instruction; the
same code touching variables is several times slower.

That is why the lock in the variable table was removed — every
value is one naturally aligned 32-bit word, so the hardware already
guaranteed what the mutex was being paid for. The result, same packs, same
board:

| | before | after |
|:---|:---:|:---:|
| 400 blocks | 2 660 µs | **515 µs** |
| a full installation | 1 319 µs | **304 µs** |
| 10 000 instructions (local variables) | 1 410 µs | 1 420 µs |

The last row is the control sample: code that does not touch variables did not
move by a microsecond. Everything that moved, moved because of variables.

## Fonts on 4 MB boards

A device with a display embeds ten text sizes. Boards with 4 MB of
flash and a display are the exception: their runtime leaves out the
largest face, 36 px, to keep room for new capabilities. A project on
such a board that uses the 36 px size still works exactly the same: the
editor puts that face inside the project's pack (about 200 kB), and the
device loads it from there. A project that never uses 36 px pays
nothing. On every other board every size is built in.

## The degradation rule

When performance runs out, the order is fixed and written into the code
itself:

**logic > communication > graphics**

Under overload, frames are dropped. **The cycle is never extended.** The
display may stutter; control may not.

## The diagnostics you can see

The board measures min/average/max cycle time and an overrun counter and
reports them to the editor. When someone writes heavy logic and the picture
starts to stutter, they will see why — and the reports include what the
monitoring itself costs.

---

The measurements are repeatable and the numbers are not from paper — the
board reads them itself (min/average/max cycle). The method and the test
projects are available on request.
