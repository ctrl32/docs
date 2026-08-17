# Online monitoring

An editor connected to a running panel shows **live values in the places you
are looking at anyway**: at the contacts in a rung, on block pins, in the
variable list and in the screen preview. It is the same view as test mode,
except the values are not computed by a simulation — they come from the
**machine**.

## Switching it on

Pick the COM port in the toolbar and click the plug icon. The colour is the
state:

| Colour | Meaning |
|---|---|
| **green** | the panel answers and runs the same program |
| **amber** | looking for the port (cable unplugged, panel restarting) |
| **red** | the panel answers but runs a **different program** |

The tooltip over the icon carries three numbers worth a look: what the
monitoring costs the panel (in µs), how old the last reading is, and the
sample counter.

!!! tip "A frozen sample counter is not a broken connection"
    If the panel answers but `seq` does not move, **the PLC cycle has
    stopped**. That is a diagnosis, not a timeout — and it saves an hour of
    looking in the wrong place.

## The same program, or nothing

Values travel from the panel **by index**, not by name. If the editor held a
newer project than the panel, it would show real numbers under the wrong
names — a lie that looks alive, which is worse than an empty field.

So both sides compare two numbers when connecting:

- **the tag table fingerprint** — the names and types of all tags in index
  order,
- **the pack CRC** — the exact identity of the program (a changed rung
  leaves the tags alone but moves the offsets of local variables).

When they do not match, the editor says *"The panel runs a different program
— downloading this one"* and opens the download. Monitoring parks itself
meanwhile (the upload needs the same port) and reconnects after the restart.

You can also read the fingerprint from the command line:

```powershell
visu_editor.exe project.yaml --tag-hash
# TAGHASH 43943135  (215 tags)
```

On site that separates "the panel runs a different program" from "the cable
is bad" without guessing.

## What can be watched

| Kind | Where from | Note |
|---|---|---|
| **tags** | the panel's tag table | always works |
| **wires between blocks** | the VM's instance memory | names come from the compiled program |
| **block members** (`t1.ET`, `c1.CV`) | the VM's instance memory | the same |
| **panel state** | cycle, overruns, heap | including what the monitoring itself costs |

Wires and block members are not tags — since the move to bytecode they are
words of instance memory (which is exactly why the cycle got 5× faster). The
editor learns their names by building the project and comparing the compiled
program **byte for byte** with what is in the pack. When they match, the
offsets are provably the panel's; when they do not, it shows tags only and
says so.

In a rung that means concrete things: for a counter **how much it has
counted** (`CV`), for a timer **how long it has been running** (`ET`, in ms
below a second and in seconds above it), and which `PT` or `PV` the block is
**really** working with — not the one drawn on it. When a parameter is fed
from a tag, that difference is exactly what you are looking for.

## What it costs the cycle

The panel samples only what you are looking at, and only ten times a second
— a faster eye would not read it anyway. Measured on a classic ESP32 (10 ms
cycle, machine program):

| state | logic | whole task body |
|---|---|---|
| nobody watching | 299 µs | 287 µs |
| 8 tags | 299 µs | 288 µs |
| 64 tags (the maximum) | 299 µs | ~289 µs |

One watched value costs **~0.34 µs per sample**, so 64 values ten times a
second is **2.2 µs per cycle** — 0.02 % of a ten-millisecond period. With
nobody online the list is empty and even that is not executed.

## Panel statistics stay live

Cycle time, overruns, heap and the bus states keep updating while you are
online. The monitoring worker owns the serial port, so it asks the panel for
them itself every ~2 s and everything that used to open the port for that —
the status bar, the device page, the CAN and Modbus dots — reads from there.
A reading older than 6 s is not shown at all: a frozen cycle time that keeps
being displayed is worse than an empty field.

## The serial console keeps working

The terminal tab reads **through** the monitoring session: every line the
panel prints that is not a protocol answer lands in a buffer the terminal
drains, and typing works too (the worker does the writing). The diagnostic
pages — CAN dump, modem status, the diagnostic buffer — go the same way, so
they answer while you are online instead of reporting "no reply".

## Writing values (force)

Not yet — fields are read-only while online. A forced value on an output is
exactly what people get hurt by, so it will come as its own feature:
visibly, with a time limit, and never silently.

## Buffer (scope)

A live view ten times a second shows a steady state and **misses short
events** — a pulse one cycle long simply falls between samples. That is
what the scope is for: up to 8 values sampled **every cycle** into a ring
buffer in the panel, with a trigger and the history from before it.

It has its own page: [Scope](scope.md).

!!! success "Recording switched off costs nothing"
    Not "almost nothing" — the cycle performs a single comparison and does
    not enter sampling at all. While recording, 8 values every cycle cost
    ~5 µs, or 0.05 % of the period.
