# Your first project

Half an hour, from an empty project to something running: a variable, a
rung of ladder, a screen, and a download. No hardware needed until the
last step — everything before it runs in simulation on your PC.

If you would rather start by *looking* at something finished, open one of
the [examples](examples.md) instead. This page is for building
one yourself, which teaches more.

**What we are building:** a light that switches on when a button is
pressed and stays on for ten seconds after it is released. Small, but it
has everything — an input, a timer, an output, and a screen to watch it
on.

---

## 1. A new project

*File → New*, then pick your board. If you have none yet, pick anything
with a display — you can change it later, and simulation does not care.

The tree on the left is your project. Everything lives under
**Application**:

| Object | Holds |
|:---|:---|
| **VAR** | your variables |
| **PLC_PRG** | your program |
| **HMIview** | the board's own screens |
| **WEBview** | the browser's screens |

Both `VAR` and `PLC_PRG` are created with the project. You will not need
to add anything.

---

## 2. Three variables

Open **VAR**. Add three:

| Name | Type | Access |
|:---|:---:|:---:|
| `button` | BOOL | rw |
| `light` | BOOL | rw |
| `delay` | TIME | rw |

Give `delay` a unit of `s`, one decimal, and an initial value of
**10000** — the table always holds milliseconds, and the unit is only how
it is shown. The screen will read "10.0 s".

Leave `source` as **internal** for now: these are variables in the
board's memory, which is exactly what you want while learning. Binding
one to a real input is one field, later.

---

## 3. One rung

Open **PLC_PRG**. It starts as a [ladder](ladder.md) program — if it
does not, right click it and choose *Edit as LD*.

Build this rung:

```
button ──[TOF PT=delay]── Q ──> light
```

Concretely:

1. Drop a **contact** on the rung and bind it to `button`.
2. Drop a **TOF** block after it.
3. Set its `PT` parameter to the variable `delay` — a parameter can take
   a variable, which is what makes the time adjustable from a screen.
4. Bind the block's `Q` output to `light`.

That is the whole program. `TOF` is the off-delay timer: `Q` follows the
input immediately when it rises, and holds for `PT` after it drops. See
[Timers](blocks-timers.md).

---

## 4. A screen

Open **HMIview** and add a screen. From the Toolbox, place four things:

| Widget | Bind to | Purpose |
|:---|:---|:---|
| **button** | `button` | mode `momentary` — TRUE while held |
| **led** | `light` | the result |
| **input** | `delay` | so the delay can be changed |
| **label** | — | text: "Hold to light" |

Make the button big — 40 px tall at least. See
[HMIview](hmiview.md) for why.

The canvas is not an approximation: it runs the board's own renderer, so
what you place is what will appear on the glass.

---

## 5. Run it, with no hardware

Press **Simulate**.

The logic starts running on your PC and the screen goes live. Press the
button on the canvas: the lamp lights. Release it: the lamp stays on for
ten seconds, then goes out.

Change the delay in the input field to 2 seconds and try again. Nothing
was rebuilt and nothing was downloaded — the value is a variable, and the
timer reads it every cycle.

**This is the loop worth getting used to.** Most of a project is built
and tested this way, before any hardware is involved at all.

---

## 6. Put it on a board

When you do have hardware:

1. **Connect it** — USB cable, or the network if the board is on one.
2. **Flash the runtime once** — *Flash runtime* on the board page. This
   is the firmware, and it only has to happen the first time or after
   an update.

    ![The Flash runtime dialog: the board's precompiled firmware, one button](img/deploy-runtime.webp){: .sb-center}

See [Download to the board](deploy.md).

---

## 7. Watch it from the outside

With the board running, press **Online**.

Live values appear in the rungs: the contact shows whether the button is
pressed, the timer shows its elapsed time counting. That is the same view
you had in simulation — now reading the real board.

And if the board is on a network, open its address in a browser. The
WEBview is there without you having drawn anything: with no browser
screens defined, it serves the board's own.

---

## What you have learned

Small as it is, that project used the whole shape of the tool:

- **variables are the only place values live** — the screen, the logic
  and the outside world all reach the same ones
- **a parameter can be a variable**, which is how something becomes
  adjustable without a rebuild
- **the canvas is exact**, because it runs the same renderer as the board
- **simulation is not a lesser mode** — it is the same logic, on your PC
- **a download cannot brick a board**, because the old program survives a
  failed one

---

## Where to go from here

| You want to | Read |
|:---|:---|
| know what else is in the block library | [Function blocks](blocks.md) |
| bind a variable to a real input | [Variables](variables.md) |
| talk to a device over Modbus | [Modbus](modbus.md) |
| make the screen usable by somebody else | [HMIview](hmiview.md) |
| see it on a phone | [WEBview](webview.md) |
| find out why something is not behaving | [Online monitoring](online.md) |

Or read one of the [tutorial projects](tutorials.md) — eleven small
ones, each about a single idea — and then an [example
project](examples.md) to see how a complete one is put together.
