# Performance and limits

Every number on this page is **measured**, not estimated, and measured on
the **slowest board we ship** — a classic ESP32 at 240 MHz with Ethernet,
WEBview and a CAN master running alongside. A faster board (S3, P4) has more
headroom, not less.

## Declared limits

The editor refuses a project that exceeds them **at your desk** — not as a
stuttering panel on a machine. They are also the numbers for the datasheet.

| Limit | Value |
|---|---|
| Tags | 512 |
| Alarms | 128 |
| Screens | 32 |
| Widgets per screen | 64 |
| LD/FBD blocks | 512 |
| Compiled program | 32 kB |
| Instance data | 8 kB |
| Trends | 4 |
| WEBview clients | 2 |
| Axes (drives) | 4 |
| PLC tasks | 2 (fast + slow) |

## How many blocks really fit

The program is N AND blocks over 150 tags — every block reads two tags and
writes one, which is the worst realistic ratio:

| Blocks | Average cycle | Of a 10 ms period |
|---|---|---|
| 64 | 110 µs | 1.1 % |
| 100 | 153 µs | 1.5 % |
| 200 | 274 µs | 2.7 % |
| **400** | **515 µs** | **5.2 %** |

400 blocks run on the weakest board we ship with a cycle that is 95 %
idle. The declared limit of 512 is not a performance boundary but a
program-size budget: a simple block costs ~10 B of the compiled
program, so 512 blocks take 16 % of the 32 kB.

In practice the **tag table** (512) runs out sooner than the blocks do.

## A real program, not a synthetic test

| Program | ST lines | Tags | Cycle |
|---|---|---|---|
| half a machine | 100 | 110 | 168 µs |
| **a whole machine** | 190 | 215 | **304 µs** |

"A whole machine" means: 40 analog inputs scaled and alarmed, 30 motors with
interlocks, a 40-step sequence and a positioning ramp. **3 % of a 10 ms
cycle**, zero overruns.

A realistic ST line costs ~1.6 µs, a ladder block ~1.3 µs.

## What the cycle actually spends its time on

The interesting part: **it is not the arithmetic, it is tag access.** A
synthetic loop over local variables runs at 0.145 µs per instruction; the
same code touching tags is several times slower.

That is why the lock in the tag table was removed on 2026-08-16 — every
value is one naturally aligned 32-bit word, so the hardware already
guaranteed what the mutex was being paid for. The result, same packs, same
board:

| | before | after |
|---|---|---|
| 400 blocks | 2 660 µs | **515 µs** |
| a whole machine | 1 319 µs | **304 µs** |
| 10 000 instructions (local variables) | 1 410 µs | 1 420 µs |

The last row is the control sample: code that does not touch tags did not
move by a microsecond. Everything that moved, moved because of tags.

## The degradation rule

When performance runs out, the order is fixed and written into the code
itself:

**logic > communication > graphics**

Under overload, frames are dropped. **The cycle is never extended.** The
display may stutter; machine control may not.

## The diagnostics you can see

The panel measures min/average/max cycle time and an overrun counter and
reports them to the editor. When someone writes heavy logic and the picture
starts to stutter, they will see why — and the reports include what the
monitoring itself costs.

---

The measurements are repeatable and the numbers are not from paper — the
panel reads them itself (min/average/max cycle). The method and the test
projects are available on request.
