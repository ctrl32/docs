# Download to the board

Downloading is **one button in the editor** (the blue :ti-download: icon, or `F5`).
There is no separate application, you need neither Python nor PlatformIO,
and you do not have to know what happens underneath. This chapter is about
what happens underneath — because during commissioning it comes in useful
exactly once.

## Step by step

**The first time, over USB** — a board fresh from the box, or one that
has never seen this ctrl32 version:

![The toolbar: the port picker and the download button](img/deploy-toolbar.webp){: .sb-center}

1. Connect the board with a USB cable. Windows needs the bridge driver of
   the board's USB chip once; [ESP32](setup-esp32.md) says which.
2. Pick the board's port in the toolbar's **port picker**. It starts
   empty on purpose; nothing is written until you choose one.
3. Open the board tab (click the board in the tree) and press **Flash
   runtime**. The dialog names the runtime it will write and its version,
   which must be of the editor's **line** (the first two numbers of the
   version - see [Versions](#versions-lines-and-builds) below); *Flash
   runtime* writes it, reads it back and verifies it. Tens of seconds.
4. Press :ti-download: in the toolbar, or `F5`. The project builds, goes
   into the inactive slot, is verified, and the board switches to it and
   restarts. Seconds.
5. Press **ONLINE** (the plug icon) and watch the program run.

**Every next time** — step 4 alone. The runtime stays; only the program
changes. A build error stops the download before anything is sent and
opens the output.

**Over the network** — for a board that is installed and reachable over
Ethernet or WiFi:

1. Type the board's address into the port picker — an IP, or the
   `name.local` the project gave it. [Finding your boards](find-devices.md)
   lists what answers on the network.
2. :ti-download: as before. The *Download to device* dialog shows
   *Network* as the target; the same slot-and-verify road, over the
   board's own web server. A Linux device is reached this way only - its
   dialog offers no USB road.
3. A **runtime** can travel the same road on the 8 and 16 MB boards:
   *Flash runtime* with the address in the port picker writes the new
   runtime into the inactive application slot, the board restarts into
   it, confirms it after the program loaded, and rolls back to the old
   runtime by itself if that does not happen. The program, the retentive
   values and the network settings stay.

**What to check afterwards** — the status bar shows the board's name and
version once ONLINE; the panel's own `INFO` line (the serial terminal,
:ti-terminal-2:) carries the runtime version, the pack's CRC and the
state of every bus. A pack the board refused says why in the download
dialog — the table further down lists the messages.

## Two different things: the runtime and the program

| | Runtime | Program (pack) |
|:---|:---|:---:|
| what it is | the board's firmware | your screens, variables and logic |
| when it is written | on a new board or a new ctrl32 version | on every project change |
| how | *Flash runtime* on the board page (over USB) | the :ti-download: button / `F5` |
| takes | tens of seconds | seconds |

**Changing a screen does not mean reflashing the board.** The visualization
is data, not code — the board reads it straight from flash.

!!! note "Network upload and security"
    The network target uses the same web server the browser interface
    runs on — whoever can reach the board over Ethernet or WiFi could
    replace the program. The WEBview settings page has **Allow program
    upload over the network**; switched off, the board never registers
    the upload endpoint and only USB uploads work. The board belongs
    on its own equipment network in every case.

## What happens when you press :ti-download:

1. The editor **builds the project into a binary pack**. If the build fails,
   nothing else happens and a window opens with the whole output.
2. The pack travels to the board — the dialog offers **two targets**:
   the USB cable (serial, 2 kB chunks, each acknowledged), or the
   **network address** of the board (an IP or `name.local`, prefilled
   from the project's mDNS name). Both roads carry the same pack with
   the same guarantees.
3. It is written into the **inactive slot** — the board has two (`visu_a`,
   `visu_b`) and is currently running from one of them.
4. The board **verifies the whole pack**: CRC, format, schema version and
   target board.
5. **Only then** does it switch the active slot and restart.

!!! success "A download cannot brick the board"
    When anything is wrong — a broken cable, a bad pack, the wrong board —
    the switch simply does not happen. The old pack stays in the other slot
    and the board keeps running. That is not luck; it is the point of having
    two slots.

## Pick the port here

The port selector in both transfer dialogs starts **empty** and the action
stays disabled until you choose one. Nothing is preselected on purpose: a
port nobody picked reads as a setting, and the first sign that it was not
would be bytes going to a device that is not there.

## Why the board refuses a pack

| Message | Cause |
|:---|:---|
| `ERR: size/slot` | the pack is larger than the partition (or the slot cannot be opened) |
| `ERR: crc` | the transfer was corrupted — try again, check the cable |
| invalid target | the project is for a **different board** than the one connected |
| old format version | the runtime is older than the pack → **flash the runtime** |

The target-board check is deliberately strict. A pack for a board with a
different display and different pins would load and run — and the equipment
would do something other than what you expect.

## Transport: the cable, or the equipment network

During commissioning the USB cable is the road that always works — and it
is the only road for [online monitoring](online.md), which therefore parks
itself for the duration of a download and reconnects by itself after the
board restarts.

The **network target** carries the same pack with the same slot-and-verify
guarantees, over the board's own web server. Mind the security switch
described above: a board that accepts a program over the network belongs
on its own equipment network, never on one strangers can reach.

!!! warning "Download into a setup that is standing still"
    Writing to flash stalls cache access **for both cores**, so the logic
    does not run while it happens, even at the highest priority. The board
    therefore allows a download only in STOP — the same reason big PLCs
    have a RUN/STOP switch.

## Runtime

The firmware is written from a catalog of prebuilt binaries for the board
(`runtimes/`), **not compiled on your PC**. You need no toolchain installed
and you get exactly the binary we tested.

![The Flash runtime dialog — the runtime's build date, the chip it expects, and the port to write it over](img/deploy-runtime.webp){: .sb-center}

The editor flashes it itself — no esptool, no Python. The flash is **read
back and verified** before the dialog says done, and the chip that answers
on the port is compared with the one the runtime was built for: a wrong
COM port is refused, not written. When the packaged runtime is older than
the editor, the dialog prints its build date in **orange** — flash the
runtime before you chase ghosts.

It runs on its own thread, so the editor keeps drawing meanwhile, and it
does not touch the pack slots — your program stays in the board after a
runtime flash.

## What is downloaded together with the program

The pack contains everything the board needs, in one file:

- the header (magic, schema version, target board, CRC32),
- the tables of strings, variables, alarms and styles,
- assets (fonts, icons, images),
- screens,
- the **compiled program** and the ST source (used to prove identity when
  going online).

The board parses nothing out of it — it maps it from flash and reads it
directly. Loading a screen takes less than a millisecond.

## Versions: lines and builds

A ctrl32 version reads `X.YY.ZZZ`. The first two numbers are the
**line** - the generation of the runtime every board and Linux device
runs; the last three are the **editor build** inside that line. A line
opens with its `.000` release, and that is when the runtimes change: a
board on line `1.01` runs `1.01.000` and keeps it through every editor
release of the line (`1.01.001`, `1.01.002` ...). An editor and a device
work together when their lines are equal - the device's page in the
editor and *Flash runtime* say so in those words, and a device whose line
is older is flashed once, at the next line.

What that means for you: an editor update inside a line changes nothing
on your boards, and the runtime you flash is always the line's - there is
one runtime per line, not one per editor build. A new line is a release
note you can see: its number ends in `.000`.

