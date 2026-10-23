---
title: "Online monitoring"
slug: online
section: "Operation"
order: 335
sidebar_position: 335
generator: tools/docs_export.py
---

# Online monitoring

An editor connected to a running board shows **live values in the places you
are looking at anyway**: at the contacts in a rung, on block pins, in the
variable list and in the screen preview. It is the same view as test mode,
except the values are not computed by a simulation — they come from the
**equipment**.

![Online with a Linux runtime over the network - live values, same wire as a COM port](img/online-linux.webp){: .sb-center}

## Switching it on

Pick the COM port in the toolbar and click the :ti-plug: icon. The colour is the
state:

| Colour | Meaning |
|:---|:---|
| **green** | the board answers and runs the same program |
| **amber** | looking for the port (cable unplugged, board restarting) |
| **red** | the board answers but runs a **different program** |

The tooltip over the icon carries three numbers worth a look: what the
monitoring costs the board (in µs), how old the last reading is, and
the sample counter — shown as `seq`, one tick per batch of values the
board sends.

!!! tip "A frozen sample counter is not a broken connection"
    If the board answers but `seq` does not move, **the PLC cycle has
    stopped**. That is a diagnosis, not a timeout — and it saves an hour of
    looking in the wrong place.

## The same program, or nothing

Values travel from the board **by index**, not by name. If the editor held a
newer project than the board, it would show real numbers under the wrong
names — a lie that looks alive, which is worse than an empty field.

So both sides compare two numbers when connecting:

- **the variable table fingerprint** — the names and types of all variables in index
  order,
- **the pack CRC** — the exact identity of the program (a changed rung
  leaves the variables alone but moves the offsets of local variables).

When they do not match, the editor says *"The board runs a different program
— downloading this one"* and opens the download. Monitoring parks itself
meanwhile (the upload needs the same port) and reconnects after the restart.

Two roads from that question, both legitimate:

- **Send your program** — the usual one; the board restarts into it
  and online opens.
- **Look first** — when you want to see what the board is running
  *before* changing anything, use **Download from the panel**
  instead: the editor then holds exactly what the board holds, and
  online works read-only with nothing written to the equipment.

A board that is still **starting up** answers the question a few
seconds late — the editor keeps asking until it does, so a freshly
restarted board comes online by itself. If the question comes back
*again after* an upload the board accepted, believe it: you are
probably holding a different project than the one you sent.

You can also read the fingerprint from the command line:

```powershell
ctrl32_editor.exe project.prj32 --tag-hash
# TAGHASH 43943135  (215 tags)
```

On site that separates "the board runs a different program" from "the cable
is bad" without guessing.

## What can be watched

| Kind | Where from | Note |
|:---|:---|:---|
| **variables** | the board's variable table | always works |
| **wires between blocks** | the VM's instance memory | names come from the compiled program |
| **block members** (`t1.ET`, `c1.CV`) | the VM's instance memory | the same |
| **board state** | cycle, overruns, heap | including what the monitoring itself costs |

Wires and block members are not variables — in the compiled program they are
words of instance memory (which is exactly why the cycle got 5× faster). The
editor learns their names by building the project and comparing the compiled
program **byte for byte** with what is in the pack. When they match, the
offsets are provably the board's; when they do not, it shows variables only and
says so.

In a rung that means concrete things: for a counter **how much it has
counted** (`CV`), for a timer **how long it has been running** (`ET`, as a
duration: `T#850ms`, `T#2s500ms`), for a blinker **how long until it
flips** (`REM`), and which `PT` or `PV` the block is **really** working
with — not the one drawn on it. When a parameter is fed from a variable, that
difference is exactly what you are looking for.

Both graphical editors draw every live value **above its variable** — at
the input and parameter stubs on the left of a block, at the outputs on
the right — so the numbers never sit on the connection lines. Online the
editors are read-only: the one thing that still switches is the LD/FBD
view. Editing resumes the moment you go offline.

## What it costs the cycle

The board samples only what you are looking at, and only ten times a second
— a faster eye would not read it anyway. Measured on a classic ESP32 (10 ms
cycle, control program):

| state | logic | whole task body |
|:---|:---:|:---:|
| nobody watching | 299 µs | 287 µs |
| 8 variables | 299 µs | 288 µs |
| 64 variables (the maximum) | 299 µs | ~289 µs |

One watched value costs **~0.34 µs per sample**, so 64 values ten times a
second is **2.2 µs per cycle** — 0.02 % of a ten-millisecond period. With
nobody online the list is empty and even that is not executed.

## Board statistics stay live

Cycle time, overruns, heap and the bus states keep updating while you are
online. The monitoring worker owns the serial port, so it asks the board for
them itself every ~2 s and everything that used to open the port for that —
the status bar, the device page, the CAN and Modbus dots — reads from there.
A reading older than 6 s is not shown at all: a frozen cycle time that keeps
being displayed is worse than an empty field.

## The serial console keeps working

The terminal tab reads **through** the monitoring session: every line the
board prints that is not a protocol answer lands in a buffer the terminal
drains, and typing works too (the worker does the writing). The diagnostic
pages — CAN dump, modem status, the diagnostic buffer — go the same way, so
they answer while you are online instead of reporting "no reply".

**A Linux device's own shell.** With the device's address typed into the
Terminal's port field instead of a COM port, the tab is the device's shell
over ssh: the editor's key logs in on a device the editor prepared,
otherwise the user name and password fields beside the address take a
login (the password is never stored). What you type goes to the shell,
what it answers comes back into the same window, and the prompt is the
live last line - nothing else has to be opened to work on the device.

**This PC's command prompt.** With `cmd` in the port field, or no port
chosen at all, the tab is the command prompt of this computer: Enter runs
a line, the arrow keys up and down bring earlier lines back, and `Ctrl+C`
(with no text selected) or the **^C** button stops what runs - the same
keys work in a Linux device's shell.

## Writing values (force)

The board can hold a value against the program — for checking wiring or
exercising an output before its sensor exists. It is a commissioning aid
and it has its own page, because it is the one thing here that changes a
equipment rather than showing it: [Forcing values](/docs/operation/force/).

The short version: a force is held by the board until released, closing
the editor does not release it, a power cycle does, and the status bar
says `FORCED n` on every page while anything is held.

## Buffer (scope)

A live view ten times a second shows a steady state and **misses short
events** — a pulse one cycle long simply falls between samples. That is
what the scope is for: up to 8 values sampled **every cycle** into a ring
buffer in the board, with a trigger and the history from before it.

It has its own page: [Scope](/docs/operation/scope/).

!!! success "Recording switched off costs nothing"
    Not "almost nothing" — the cycle performs a single comparison and does
    not enter sampling at all. While recording, 8 values every cycle cost
    ~5 µs, or 0.05 % of the period.
