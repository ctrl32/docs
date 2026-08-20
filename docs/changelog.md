# What's new

Every release replaces the previous one — the editor's update check
offers it automatically, and a project saved in an older version always
opens in a newer one.

Starting with **1.00.001**, versions are plain numbers in the form
`generation.feature.build`: the last field counts builds, the middle
one grows with new capabilities, the first one practically never
moves. Releases before that carried dates (`year.month.day.build`).

## 1.00.010

**Important fix — download your project again.** The editor's
download stamped packs with an outdated format label, and from
1.00.008 on a panel with the new runtime could reject or fault the
program because of it — online monitoring then showed nothing.
Install this build and download the project once (F5); nothing else
is needed. Runtimes flashed from 1.00.008/9 are fine as they are.

## 1.00.009

**A clean start.** A new project begins truly empty — no pre-made
program in the tree; you add LD, FBD or ST yourself. And a program
opened in ladder always has its first rung waiting: the bare arrow,
ready for the first contact.

- The diagnostics page no longer shows memory bars or heap numbers —
  cycle times, overruns and project consumption stay.
- The standing "online — switch to offline" note is gone from the
  editor toolbars; the grayed controls say it.
- Ladder drawing polish: a parallel branch connects to the run wire
  to the pixel (no tick above, no stub poking left of the branch) and
  block frames have sharp, fully joined corners.
- A saved project reloads its internal connection variables exactly
  as it saved them — a reopened ladder program keeps its rung shape
  instead of decomposing into helper-variable rungs.

## 1.00.008

**The blinker counts down for you.** BLINK blocks have a new `REM`
output pin: the time left in the current phase, live on the right
stub in online and simulation — next to the timers' `ET` and the
counters' `CV`, every block with an inner value now shows it. Loading
projects that use `REM` needs the runtime from this release; existing
projects and runtimes keep working unchanged.

- Variable declarations can be edited during a running simulation —
  applying re-binds the program on the fly. (Connected to a real
  panel they stay read-only, as everything does.)
- Ladder breathes less air: tighter comment lane, tighter spacing
  between rungs, and rungs with blocks no longer reserve an empty
  row below them.
- Toolbox tiles of the motion, CAN and communication blocks got
  short marks that fit the tile — no more clipped names.

## 1.00.007

**One program, one owner.** A program edited in ladder is a read-only
view in the block editor (and the other way round after taking it
over with one click) — so an edit in one view can never be silently
overwritten by a save from the other. Previously a comment written in
LD could wipe blocks that had just been drawn in FBD; that cannot
happen any more, and the two views finally stay in step.

- **Comments are shared.** Rung comments and network comments are the
  same text — write it in either editor, switch, and it is there.
- **Arrange respects networks.** With network dividers present the
  Arrange button lays blocks out inside their own network — dataflow
  columns per band, band heights to fit — instead of scattering the
  whole canvas.

## 1.00.006

**Function blocks get a proper interface pane.** Above the canvas of
every LD and FBD tab sits a variables table in the PLCopen shape:
`VAR_INPUT` and `VAR_OUTPUT` rows of a function block (name and type
edited right there, ports added with one button) and a `VAR` section
listing the local connection variables the diagrams create. Building
your own block is now the standard flow: add a POU of the *function
block* kind, define its inputs and outputs in the pane, draw the
inside — in FBD **or in ladder** — and place it as a block in any
program. Interface changes bump the block's version automatically so
existing instances migrate cleanly.

- **Toolbox sorted.** Blocks are grouped the same way everywhere —
  Boolean, Math, Timers, **Counters**, General, **Motion**, **CAN**
  and **GSM/GPS** — in the Toolbox of both editors and in every
  add-block menu. Motion and CAN blocks were missing from the block
  palette entirely; now every group is one click away. Groups start
  collapsed each time the editor opens.
- In FBD the operand names sit **below** the wire line (values stay
  above it) — a connection passing a pin row no longer runs through
  the text.

## 1.00.005

**Comments are written straight on the canvas.** Every ladder rung has
a comment line above it — click it and type, multiple lines welcome;
click away and it stays. Network comments in the block diagram work
the same way. No dialog anywhere.

- A network in the block diagram can be **selected** like a rung in
  ladder — click its empty area and it highlights with the same quiet
  grey background.
- The rung comment no longer touches the blocks below it, and while
  connected a conducting block's frame is drawn as thick as the
  conducting wires — the active path reads at a glance.

## 1.00.004

**A rung does not need a coil.** A ladder rung can now end without an
output coil — the run wire simply ends in a small arrow, the standard
notation. A new rung starts that way: just the arrow, and you build
from there. Blocks placed on a bare rail get a TRUE contact drawn in
front of them, and contacts before a block act as its EN condition —
no helper variable needed. Everything still converts cleanly between
LD and FBD, both directions.

- **Clean networks in FBD.** A connection never crosses a network
  divider any more: across networks the signal travels by its
  variable name, shown at both pins — for a direct block-to-block
  link that name is `instance.PIN`. Generated FBD layouts also got
  proper spacing: band heights follow the tallest block and columns
  leave room for the operand labels.
- Live values in ladder now sit above the pin variables of blocks
  placed inside a rung too — inputs, parameters and the second
  output alike, matching the boxes.
- Thinner connection and block lines in the editors — the drawing is
  lighter; symbols keep their weight, and the live power flow is
  still thick and green.
- Selecting a rung highlights it with a quiet grey background
  instead of a bright frame over the rung comment.

## 1.00.003

**The block diagram mirrors the ladder.** A program edited in LD shows
its FBD view organized in numbered networks — one horizontal band per
rung, in rung order, with the rung comments on the network dividers.
Every ladder save refreshes the layout, so the two views never drift
apart. A diagram with no dividers yet is network 1 and says so.

- Online mode is now read-only without exceptions: the context menus
  and edit popups of both editors stay closed while the connection is
  live. The one thing that still switches online is the LD/FBD/ST view.

## 1.00.002

- Live values in LD and FBD are drawn **above each pin variable** —
  inputs, parameters and outputs alike — where they cannot collide
  with names or connection wires; live rows stretch to make room.
- The view switch (LD ↔ FBD) moved to the front of the toolbar and
  stays available during online monitoring.
- The status bar shows the version number instead of the build date.

## 1.00.001

First numbered release (see the numbering note above).

- Online values placed clear of labels and wires.
- A ladder element cut in one rung pastes into any other rung.

## 2026.08.20.4

- **Online monitoring is read-only.** While the editor is connected to
  a running panel, the program cannot be modified — no adding, moving
  or deleting; edits resume the moment you go offline.
- Right-click **cut / copy / paste** for blocks, contacts and boxes in
  both LD and FBD; **insert rung above / below**; rung comments in LD
  and network dividers with comments in FBD.
- Newly inserted blocks and contacts come with `...` placeholder pins —
  nothing is silently bound to a variable you did not pick.
- The toolbox is split into MATH and BOOLEAN sections.
- Live values are shown directly in the FBD editor during simulation
  and online monitoring.

## 2026.08.20.3

**Everything fits in ladder now.** Function blocks with state — timers,
counters, ramps, filters, hysteresis — sit in a rung as EN boxes with
the standard IEC 61131-3 EN/ENO behaviour: the block simply does not
execute while the rung is off, its state freezes and its outputs hold.

- **LD ↔ FBD switching** — right-click a program in the tree and open
  it in the other editor. Ladder always opens as FBD; FBD opens as
  ladder whenever the network fits rung form, and if it does not, the
  status bar names the exact block that is in the way.
- **Trends with up to 4 curves** in one chart, each with its own color
  — on the panel and in the browser alike.
- **Gauge**: arc thickness is adjustable and the needle can be switched
  off for a clean modern look.
- **Alarm table**: row text size is selectable; the row height and the
  touch target scale with it.
- **Toolbar**: New, Open, Save, Undo in the expected order, icons
  properly centered.
- The Run/Step controls of the block editor appear only while the
  simulation is on — online they had no business being there.
- **CANopen**: the SDO parametrization picker now offers every writable
  object of the device dictionary, not only the non-mappable ones —
  ramp times and friends included.
- The online activity bar in the status line sweeps at the real
  polling rate of the link: one sweep is one read cycle, a stalled
  panel leaves the bar standing full.

## 2026.08.20.2

- The editor build is signed again and the update manifest with it.
- First version of the activity bar and the LD/FBD context-menu switch.

## 2026.08.20.1

- **ESP32-P4 support.** The Waveshare P4-NANO with the 10.1"
  MIPI-DSI touch panel (1280×800) is a supported target with a
  precompiled runtime in the installer: display, touch, Ethernet and
  WiFi work out of the box.
- **Upload over the network.** The panel accepts a visualization pack
  over Ethernet or WiFi (`POST /upload`), with exactly the same
  safety as over USB: the pack lands in the inactive slot, is fully
  validated, and only then does the panel switch — an upload can never
  brick a panel.
- On the P4 the panel serves the WEBview over Ethernet and its own
  WiFi access point at the same time; packs on the P4 may be up to
  4 MB (room for photo-heavy screens), with an 8 MB decoded-image
  cache in PSRAM.

## 2026.08.19

- **Online, offline and simulation are now three separate things.**
  Going online never silently switches the editor into simulation;
  the transport controls show only when the simulation is on.
- **Five sizes of quality text** (13/15/18/20/22/24/28/36 px plus the
  numeric and seven-segment faces), TTF import for custom fonts, and
  full Slovak diacritics everywhere.
- **I2C toolbox**: a bus scanner in the editor, an address dropdown
  fed by the chip catalog, and automatic chip identification where the
  silicon supports it.
- The device Resources page was decluttered; column widths are
  draggable; device renames propagate everywhere.

## 2026.08.18

- S3 panels run their PSRAM at the full 80 MHz — measurably smoother
  screens on photo-heavy projects.
- The editor flashes runtimes itself (no external tooling), and the
  installer ships a precompiled runtime for every supported board —
  the *Upload runtime* button works on a fresh machine with nothing
  else installed.
- Fixes for installed-editor paths (Program Files is read-only) and
  for user profiles with diacritics in the name.

## 2026.08.17

