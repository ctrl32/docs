# Download to the board

Downloading is **one button in the editor** (the blue :ti-download: icon, or `F5`).
There is no separate application, you need neither Python nor PlatformIO,
and you do not have to know what happens underneath. This chapter is about
what happens underneath — because during commissioning it comes in useful
exactly once.

## Two different things: the runtime and the program

| | Runtime | Program (pack) |
|:---|:---|:---:|
| what it is | the board's firmware | your screens, tags and logic |
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

![The Flash runtime dialog — the runtime's build date, the chip it expects, and the port to write it over](img/deploy-runtime.webp)

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
- the tables of strings, tags, alarms and styles,
- assets (fonts, icons, images),
- screens,
- the **compiled program** and the ST source (used to prove identity when
  going online).

The board parses nothing out of it — it maps it from flash and reads it
directly. Loading a screen takes less than a millisecond.

## Licence

