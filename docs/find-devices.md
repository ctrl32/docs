# Finding your boards

Ten identical boards on a bench are identical right up until the wrong
one gets a program. The scanner exists so that never has to be a guess:
it finds every board it can reach and says **where it is, what it is,
and what it runs**.

Open it with the :ti-eyeglass: button next to the port picker, or
*Online → Find devices…*. Every open starts a **fresh sweep** — a
board unplugged since the last look is not still sitting in the list.

![The scanner over a full bench: five boards on COM ports and four answering from the network, each with its program name and version](img/find-devices-scan.png)

That is a real bench mid-scan: nine rows from seven boards — the
networked ones answer twice, once per way of reaching them. Every
question the dialog exists to answer is on it somewhere: *which
port is the Discovery board?* (COM10), *which of the identical
inoCORE boards runs the Modbus slave?* (the **Program** column),
*which boards still run last week's firmware?* (the orange
versions), *what address did the WiFi board get?* (192.168.0.233).

---

## What a sweep does

Two searches run together:

- **Every COM port** is asked politely — the probe opens the port
  without touching the reset lines, so nothing restarts, not even a
  board that is busy doing real work.
- **The local network** is swept for boards answering on it — ethernet
  and WiFi alike.

Anything that answers becomes a row:

| Column | Meaning |
|:---|:---|
| Port / address | where the board was found — `COM7`, or an IP |
| Board | which hardware it is, resolved from the catalogue |
| Program | the **name of the project** it is running |
| ver | the firmware version on the board |
| IP | the board's own address, when it has one |

The board column comes from the board itself: every runtime reports a
hardware identity, and the editor's catalogue turns it into a name. A
row saying *older firmware* is a board whose runtime predates the
identity report — flash the runtime and it will introduce itself
properly.

---

## The program name

The name in the *Program* column is the **project name** — the `name:`
in the project file, downloaded with the project. Name projects after
what they do (`packing_line_3`, not `test2`) and the scanner becomes an
inventory: ten identical boards, each saying which job it holds.

A board with an older runtime, or no project yet, shows no name.

---

## The version column

Green means the board's firmware matches the editor. Orange means the
board is **older than the editor** — it runs fine, but before the next
download it should get the matching runtime (*Flash runtime* on the
board page). The editor and the runtimes install together and carry
the same version on purpose, so *matching* is one number, not a
compatibility table.

---

## Use

*Use* on a row points the editor at that board — the port picker takes
the row's port or address, and the dialog closes. When the board's
program name matches one of your recent projects, that project opens
too: *Use* means "work with this board", and the editor sets up
everything that follows from it.

The button only appears where it works: a serial row always, a network
row only for boards whose firmware takes editor connections over the
network. A row without *Use* is still information — the board is
there, it answers, and its WEBview is a browser away.
