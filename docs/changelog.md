# What's new

Every release replaces the previous one — the editor's update check
offers it automatically, and a project saved in an older version always
opens in a newer one.

Starting with **1.00.001**, versions are plain numbers in the form
`generation.feature.build`: the last field counts builds, the middle
one grows with new capabilities, the first one practically never
moves. Releases before that carried dates (`year.month.day.build`).

## 1.00.040 (2026-09-05)

- **The editor starts empty and New project is a wizard.** One window
  asks for the name, the folder (`Documents\ctrl32\projects` unless you
  browse elsewhere), the board or the processor module, and what the
  project does — visualization, WEBview, ladder or ST, CAN, Modbus,
  MQTT, net32 — and creates the whole project from those ticks. See
  [Quick start](quickstart.md#3-your-own-project).
- **Your own board with a display.** A project on a module declares its
  glass on the board tab: the catalog board with the same display
  controller, the size as mounted, the display and touch pins. The
  editor checks the pins and builds the same display record the catalog
  board gets.
- **A module can run headless.** Every processor module now has two
  runtimes: with a display, or headless with the bigger program limits
  (64 kB program, 24 kB instances, 1024 blocks) for a project that shows
  its screens in WEBview only. The wizard's *Visualization* tick picks
  it; the board tab lets you change it. See
  [Modules](modules.md) and [Performance and limits](limits.md).
- **The LITE class.** A classic module without extra memory carries 128
  variables, 32 alarms, 128 blocks and one axis — with those limits the
  same board runs its display, WiFi with the access point, CAN and
  WEBview together. The catalog says which boards it covers.
- **Ladder blocks.** Every pin of a block is drawn always; a motion block
  carries its axis on the rung (one axis assigns itself, more need the
  choice on the block); a block dropped inside a function block binds to
  the block's own inputs and outputs; blocks without outputs work as
  boxes; a box on an empty rung stays a box.
- **The device reports what it was built for.** The runtime tells the
  editor its variable, alarm and axis capacities, and the editor's
  checks compare them with the catalog.

## 1.00.035

- **net32 — our device network.** ctrl32 devices now work as one
  system — the backbone for home automation. One
  device owns a variable, others subscribe to it by node and name;
  writes travel to the owner as commands. Works over WiFi, ethernet
  and CAN; a silent peer marks its variables stale, drops its health
  flag and never fires queued writes — local logic keeps running.
  The whole story: [net32](net32.md).
- **One project for the whole system.** A single `.prj32` can hold
  every device of an installation: switch devices in the tree, wire
  their shared variables on the net32 canvas by dragging between
  cards — both sides of every subscription are generated for you —
  and **Deploy all** uploads every device over its own connection.
  See [the system project](net32.md#the-system-project).
- **An AI assistant can join your editor session.** Tools → MCP
  server connects an AI assistant (any MCP client) to the project you
  have open: it reads variables, screens and programs, builds, and
  makes edits you can undo with Ctrl+Z — on this computer only, off
  by default, behind a per-session token, with live-board writes
  behind an extra consent switch. See
  [the editor page](editor.md#ai-assistant-connection-mcp-server).
- **4 MB display boards get a slightly larger firmware area.** The
  update itself repartitions the flash — after this runtime update,
  upload the program to the board again (one extra step, one time).

## 1.00.034

- **+7 — the panel talks to an S7 PLC.** A ctrl32 panel can
  replace the operator panel on an existing S7 installation: it reads
  and writes data blocks and flag bits over ethernet, the PLC program
  stays untouched, no GSD files and no TIA project needed. S7-300/400
  work as delivered; an S7-1200/1500 needs PUT/GET enabled and
  non-optimized DBs. Runs on P4, STM32 F7 and Linux devices. The
  whole story: [+7 (S7 PLC)](plus7.md).
- **The device tree shows the +7 link state live** — connected /
  connecting / link down, with request and error counters, on the
  node and on the +7 page.
- **Programs saved by editor 1.00.032 load correctly again.** A
  1.00.033 board could refuse such a program as "corrupted" after a
  runtime update — nothing was corrupted, the reader mis-measured
  the older file's header. Rebuilding the program was never needed;
  updating the runtime to 1.00.034 is the fix.

## 1.00.033

- **A device that answers Modbus TCP now frees a dead connection on
  its own.** A client that vanished without closing (power cut, WiFi
  drop) used to hold the slave's single slot until a restart; an idle
  connection is now dropped after 60 s and the next client gets
  served.
- **Going online no longer asks for a download it does not need.**
  The installed editor compared its own build of the project against
  the panel without the board's facts and kept demanding a new
  program; the comparison now builds with the full board card, and a
  permanent test guards it.
- **Buttons wired through the touch controller's I2C pins work
  again** on boards where the display and the buttons share the bus.
- **The Devices scanner ages its information honestly** — a board's
  address and firmware line fade out when they stop being fresh
  instead of pretending to be live.

## 1.00.032

- **A boot splash.** The panel puts a picture on the glass right
  after power-on — your own image or the ctrl32 mark — and holds it
  until the runtime is up and the configured minimum has passed, so
  the display no longer flickers dark while WiFi or the broker
  connect. Pick the image and the time on the HMIview page
  (0 s turns it off).
- **A button can change its caption when ON.** A latching button
  says START while off and STOP while lit — set *text when ON* in
  the inspector; the ON colour is the style's accent, as before.
- **The gauge's centre number is optional.** On small glass it often
  crowds the dial — one checkbox (*Center number*) hides it, and a
  separate value widget can take its place.
- **Projects are `.prj32` files.** The editor opens and saves the
  package form only, and every example and tutorial ships as one —
  the Welcome page, the Examples menu and the recent list all speak
  it. See [Project format](project-format.md).
- **OPC UA with certificates.** The Linux runtime offers Basic256Sha256
  (and AES) sign-and-encrypt endpoints; the certificate is managed
  from the OPC UA page — self-signed, your own PEM/DER pair, or
  encryption off. A variable can also be kept **off the server**
  with one checkbox. See [The Linux runtime](linux-runtime.md).
- **A USB mouse on a Linux device just works** — plug it in, a cursor
  appears, a click presses like a finger. The on-screen keypad now
  scales with the glass.
- **The Modbus device card creates its variables.** One button makes
  a variable for every register (and keeps them in step with the map
  when it changes); a `+` on a row creates just that one. See
  [Modbus](modbus.md).
- **Limits follow the target everywhere.** A Linux project shows and
  uses the ten-fold numbers in every editor check, not only at build
  time. See [Limits](limits.md).
- Boards that physically carry SPI, I²C or a serial line now say so
  in the catalogue — the device tree offers what the hardware has.

## 1.00.031

!!! warning "Update the boards first"
    The program pack format moved again: **flash the new runtime onto
    a board before sending it a program built by this editor.** The
    board refuses a newer pack loudly and keeps running the old one.

- **One runtime reads another over OPC UA.** A Linux target can name
  an OPC UA server and source variables from its nodes
  (`source: opcua`) — browse the server on the OPC UA page, import,
  and the values are polled in at runtime. See
  [The Linux runtime](linux-runtime.md).
- **The Linux runtime.** ctrl32 now also runs as a Linux program on
  catalogue devices — Seeed reTerminal (5", Raspberry Pi CM4) and
  the ST STM32MP157C-DK2. Same project file, same editor; the device
  boots into the visualisation, takes downloads over the network,
  goes online like any board, and serves **every variable over OPC
  UA**. Limits are roughly **ten times** the microcontroller
  numbers. See [The Linux runtime](linux-runtime.md).
- **MQTT over TLS.** The broker connection can be encrypted on S3,
  P4 and STM32 boards — the editor refuses the combination the
  hardware cannot carry, at your desk. See [MQTT](mqtt.md).
- **Set up WiFi and MQTT on the glass.** Two reserved screens —
  `sys_settings` and `sys_terminal` — let an operator repoint a
  board to a different network or broker, and watch the MQTT
  traffic live, without the editor. See [MQTT](mqtt.md).
- **Bus pins on the board page.** CAN, RS485, I²C and SPI positions
  are assigned on the board page from a list of **allowed pins** —
  pins the chip cannot give you are simply not offered, and boards
  that route a bus themselves show it fixed.
- **The MQTT page.** The whole MQTT configuration sits on its page
  now — no dialog in between.
- **HMIview settings.** Clicking HMIview in the tree opens its
  settings — the resolution (free on targets that scale, fixed
  where the glass decides) and the WEBview canvas size.
- **The scanner sees more.** Linux runtimes appear in the device
  scanner next to the boards; a device reachable over two networks
  shows as one row, not two.

## 1.00.029

!!! warning "Update the boards first"
    This release changes the program pack format: **flash the new
    runtime onto a board before sending it a program built by this
    editor.** The board refuses a newer pack loudly and keeps running
    the old one — nothing breaks, it just tells you to update.

- **Home Assistant.** A board can now publish its variables over MQTT
  and appear in Home Assistant on its own — switches, numbers and
  sensors, discovered automatically, no YAML on the Home Assistant
  side. Two step-by-step tutorials ship with the editor: a thermostat
  that reads its temperature from a Zigbee sensor, and a light panel
  that switches and dims real bulbs. See
  [Home Assistant](home-assistant.md).
- **Buses on the pins you choose.** CAN, RS485, I²C and SPI pins are
  part of the project now — set them in the editor and they travel
  with the program; leave them alone and the board's own defaults
  apply. RS485 works in three wiring shapes: separate DE and RE, the
  two tied together, or an auto-direction converter with just TX/RX.
- **Headless boards take bigger programs.** A board without a display
  spends no memory on drawing, so it holds twice the program: 64 kB of
  compiled logic, 24 kB of block instances, 1024 ladder blocks. The
  editor knows which type it is building for and checks the right
  limits at the desk. See [Limits](limits.md).
- **Analog inputs.** A variable can read the board's own ADC —
  calibrated millivolts, with gain and offset for a battery divider or
  a potentiometer. For real measurement duty an external ADS1115-class
  converter is still the answer, and the editor says so.
- **WEBview is a choice.** A project can mirror the display screens to
  the browser, draw an independent set for it — or switch WEBview off
  entirely and give its memory to the program. The smallest boards
  gain the most: the thermostat tutorial runs on a board where the
  browser server and MQTT would not fit together.
- **A vanished Modbus device no longer freezes the display.** On STM32,
  a slave that stopped answering could hold the screen and the console
  hostage for tens of seconds while the program ran on underneath.
  Communication now waits in its own lane; the glass never rides along.
- **Remembered values check their type.** A retained variable is
  restored only when its stored type matches — a new project reusing a
  name from an old one starts from its own initial value instead of
  inheriting foreign bits, and the diagnostic buffer says when that
  happened.
- WiFi joining is more patient: a board whose access point comes up
  late — a paired board restarting, a router rebooting — retries and
  falls back instead of giving up.

## 1.00.028

- **Find devices.** The :ti-eyeglass: button next to the port picker
  sweeps every COM port and the local network and lists what answered:
  which board, **which program it runs**, its firmware version and its
  address. *Use* on a row points the editor at that board — and opens
  the matching project when it is in your recent list. See
  [Finding your boards](find-devices.md).
- **Boards introduce themselves by program name.** The project's name
  travels with the download, so ten identical boards stop being
  identical — each one says which job it holds, in the scanner and to
  anything else that asks.
- **One version, everywhere.** The editor and every runtime it installs
  now carry the same version number, and the dialogs check it: the
  runtime flasher refuses a stale file, the download dialog says when
  the board should be updated first. "Half of it left old" can no
  longer happen quietly.
- **States and motion now behave on the glass.** A widget driven only
  by a state or a path never redrew on the board's display — the
  marker sat still while the browser moved. Both renderers now agree,
  in both directions: state lamps light in the browser too.
- **Live ladder on STM32.** Online mode on an STM32 board now shows the
  power flow and the values inside a rung — the wires between blocks
  were frozen on this family; they animate exactly as on ESP32 now.
- **A CAN fault no longer restarts the board.** A bus nobody answers —
  a broken transceiver, a shorted pair — used to reboot the whole
  board in a loop. It now recovers on its own and keeps the program
  running; communication is never worth the logic.
- Network program upload is offered only on boards with the memory to
  take it; the smallest ones say so plainly and keep the USB path.

## 1.00.027

- **States and motion on any widget.** A widget can now carry three
  states — true, false and alarm — with a colour for each, driven by a
  variable or by **one bit of an integer**. Four lamps on four bits of a
  status word, no logic between them. And any widget can **travel a
  path** as a value sweeps its range: along a line, or with X and Y
  driven by two values independently. Drawn in the editor, identical on
  the board and in the browser.
- **Vector icons.** Icons are outlines rather than baked bitmaps, so
  they are sharp at any size — a 16-pixel status glyph and a
  screen-filling symbol come from the same entry. A full-screen icon
  used to cost a couple of hundred kilobytes; it now costs tens of
  bytes, and the browser draws them too, which it never could before.
- **Buttons work in online mode.** Pressing a control on the editor's
  canvas while connected now reaches the running board, instead of
  writing into the editor's own copy of the values. Screens switched
  before; everything else looked dead.
- **STM32 boards are written by the editor.** No external tools: the
  editor speaks to the ST-LINK probe directly and writes the board over
  SWD, verifying every byte it wrote before resetting.
- **Colours written as `#RRGGBB` work.** The web spelling everybody
  reaches for used to yield black, silently. Both spellings parse now —
  worth re-checking any colour in an older project that never looked
  right.

## 1.00.026

- **The first STM32 board.** The runtime now runs on STM32F7-class
  hardware (bring-up board: the ST 32F746G-DISCOVERY — 480×272 touch
  glass, ethernet, 8 MB RAM, 16 MB flash). The same project, the same
  pack, the same editor: pick the board and upload. The PLC dispatch
  loop executes from the chip's zero-wait instruction RAM and the
  display is pushed by the 2D DMA engine, so the logic cycle and the
  glass never fight for time.
- **Everything over ethernet.** A network board now serves the full
  WEBview from its own address, accepts program uploads over the wire
  (*Download → Network* in the editor, no cable swap), and — new — the
  editor's **online mode works over ethernet too**: type the board's
  IP where you would pick a COM port and watch live values, the
  console, the scope and forcing exactly as over USB. One protocol,
  two wires.
- **The board knows the time.** With ethernet up it sets its clock
  from the internet automatically (NTP), and the browser can set it
  by hand on a closed network. Alarm and diagnostic timestamps mean
  something now.
- **Retentive values without extra chips.** On the STM32 the variables
  marked *persist* survive restarts and program uploads in the
  processor's own battery-domain memory — no EEPROM wiring, no wear,
  and with a backup battery fitted they survive power loss outright.

## 1.00.023

- **A classic board with a display gets the network.** Boards without
  PSRAM that light a screen used to skip the network stage entirely —
  the memory simply was not there. The firmware stopped paying for a
  demo it never shows, and the freed memory carries an ethernet-only
  WEBview: one viewer, straight from the board. The Olimex EVB wall
  thermostat now serves its Home Assistant banner from the glass.

## 1.00.022

- **Every network board answers Modbus TCP.** Headless runtimes (the
  Olimex PoE family, the generic presets and friends) now run the
  same Modbus TCP slave the display boards always had — a SCADA can
  read and write the variable map on port 502 without a screen attached.
  A pack asking for RTU on a board with no RS485 wired says so on
  the console instead of listening on nothing.
- **The P4 showcase demonstrates bit access live.** A new *Bit
  access* screen (reached from Control): the logic blinks one bit,
  the lamp test drives another, and six switches — on the glass and
  in the browser at once — own the middle of the same word. Proven
  under fire: hundreds of browser toggles against the running logic
  with not one lost write.
- The bench tooling is a single program now; the sample-project
  headers name it instead of retired scripts.

## 1.00.020

- **Bits, everywhere.** Every bit of an integer variable is addressable on
  its own: `IF status.5 THEN` and `mask.0 := ready;` in ST, contacts
  and coils on `variable.bit` in ladder and FBD, the widgets as before —
  one meaning across all of them. The index is checked against the
  variable's width at build time, in the spelling your fingers
  already know.
- **A bit write never loses a neighbour.** Writing one bit from the
  logic while a browser switch flips another and a Modbus master
  rewrites the word is safe — every bit write is atomic. This also
  fixes a real race: a browser switch used to write the whole word
  back from a stale snapshot and could wipe bits the PLC or a Modbus
  master had just changed.
- **Bitwise toolbox.** On integers, `AND`/`OR`/`XOR`/`NOT` are
  bitwise and `SHL`/`SHR` shift — as operators and as functions.
  Building LED masks no longer needs arithmetic gymnastics.
- Program packs are format 48; the board needs this release's
  runtime (the editor tells you, in orange, when it does not have it).

## 1.00.019

- **Every board's firmware is current.** Nine runtimes had lagged
  behind since mid-August (the Olimex PoE family, the generic
  presets, inoCORE32-TM1.0); all nineteen in the catalog are now
  built from the same day's firmware, at the full 240 MHz.
- **The project-vs-board check works in the installed editor.** The
  full validation — display and resolution, buses, pins, peripheral
  limits, pack size against the flash slot — runs inside every build,
  with the same wording everywhere. Until now the installed editor
  silently skipped parts of it that only worked in our development
  tree.
- The documentation gained screenshots of the editor on every major
  page, and its web navigation is grouped into sections.
- Sample projects speak English throughout, including the variable names
  in the seal-in classic.

## 1.00.018

- The bold icon actually reaches the editor now — a stale build cache
  kept the first, timid draft inside the program while the installer
  already wore the new one. If Windows still shows the old icon after
  updating, that is Explorer's icon cache; it refreshes on its own
  (or after a sign-out).

## 1.00.017

- The icon got bold: the dots sit one pixel apart and the "32" fills
  the full width of every size — it now holds its own next to any
  other program's icon.

## 1.00.016

- **ctrl32 has a face.** The dotted "32" in the project's own
  typeface and the brand blue is now the icon of the installer, of
  the editor itself, of its window and taskbar entry and of the Start
  menu shortcuts. Every icon size is drawn dot by dot — the logo
  stays crisp from 16 px up.

## 1.00.015

- **The bare-arc gauge works in the editor too.** A gauge with the
  needle switched off and a custom arc thickness drew correctly on
  the board but grew a needle back in the editor's canvas — the
  editor now carries both properties end to end: drawing, project
  files, download, and the inspector (a Thickness field and a Needle
  switch under the gauge angles).
- **Navigation buttons dropped the arrow.** The chevron took 14 px
  from every nav button's text; the text now gets the whole button —
  on the board, in the browser and in the editor alike.
- **The EVB thermostat example got its dial.** The main screen is the
  familiar thermostat-card look: two nested arcs (room temperature in
  blue, setpoint in orange), whole-degree numbers in the center, a
  +/- setpoint spinner — and the numeric design stays one nav button
  away. The program opens cleanly in the ladder editor, spinner
  included (a rising-edge contact, the ladder-native shape).
- **Every installer now passes the full test gate first.** The engine
  comparison across all example programs, the block and language test
  suites and the editor self-tests run before the installer is built
  — a red test means no installer exists to ship.

## 1.00.014

- **Olimex ESP32-EVB drives a display.** The MOD-LCD2.8RTP module
  (2.8" 320×240 with resistive touch) plugs into the board's UEXT
  connector and the same board id covers both uses: a project with
  HMI screens lights the glass, a project without them keeps the
  board headless with WEBview, exactly as before. Picture and touch
  are verified on real hardware, touch calibration included, and the
  board comes with its own example project sized for the small glass:
  a wall **thermostat** — the board's two relays driven by a ladder
  hysteresis controller with auto/manual, a simulated temperature
  until a sensor is wired, and a portrait web banner prepared for a
  Home Assistant dashboard.
- **One honest limit that comes with it:** this board runs the
  display *or* the WEBview, not both — the classic ESP32 with a
  display project has no memory left for the network stack. The
  board says so plainly at startup and keeps logic, glass and USB
  download running; the headless use keeps its WEBview as always.
  (The groundwork for a display-plus-ethernet mode is in place and
  planned for a future release.)
- The USB download listener now starts earlier and reports loudly if
  it ever cannot start — on a tightly loaded board it could
  previously die silently, leaving no way to download over the
  cable.
- Display boards start a little lighter on internal memory — two
  large fixed buffers moved out of the static segment (no behavior
  change; it is what made the EVB combination fit).

## 1.00.013

- Fixed a red "conflicting ID" warning (and the ambiguous click
  behind it) in the ladder FB menu — the timers and counters appear
  there twice by design, once for the rung and once as a box, and
  the two halves now identify themselves properly.

## 1.00.012

**Download over the network, straight from the editor.** The download
dialog now offers two targets: the USB cable, or the board's network
address (IP or `name.local`, prefilled from the project). The same
pack, the same guarantees — inactive slot, full validation, the old
program stays on any error — just without walking to the equipment.

- **Headless boards accept network uploads too.** Boards without a
  display (inoCORE32-TM1.x and friends) take a pack over Ethernet or
  WiFi the same way the display boards do. Flash the runtime from
  this release once over USB; from then on the network works.
- **And the security switch that belongs with it:** the WEBview
  settings page has *Allow program upload over the network*. Switched
  off, the board never even registers the upload endpoint — for a
  deployed equipment on a shared network. USB always works. The board
  belongs on its own equipment network either way; the browser
  interface rides the same server, so treat network access to the
  board as operator access.
- A landscape project on a portrait glass (the 10.1" board) no longer
  trips the board check — the board rotates, and now the check knows.

## 1.00.011

- Live rows in the block editor got more air — on blocks with two
  outputs the first output's name and the second output's value no
  longer touch, and block parameters line up with their stretched
  rows instead of clustering at the top of the block.

## 1.00.010

**Important fix — download your project again.** The editor's
download stamped packs with an outdated format label, and from
1.00.008 on a board with the new runtime could reject or fault the
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
  board they stay read-only, as everything does.)
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
  a running board, the program cannot be modified — no adding, moving
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
  — on the board and in the browser alike.
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
  board leaves the bar standing full.

## 2026.08.20.2

- The editor build is signed again and the update manifest with it.
- First version of the activity bar and the LD/FBD context-menu switch.

## 2026.08.20.1

- **ESP32-P4 support.** The Waveshare P4-NANO with the 10.1"
  MIPI-DSI touch panel (1280×800) is a supported target with a
  precompiled runtime in the installer: display, touch, Ethernet and
  WiFi work with no setup.
- **Upload over the network.** The board accepts a visualization pack
  over Ethernet or WiFi (`POST /upload`), with exactly the same
  safety as over USB: the pack lands in the inactive slot, is fully
  validated, and only then does the board switch — an upload can never
  brick a board.
- On the P4 the board serves the WEBview over Ethernet and its own
  WiFi access point at the same time; packs on the P4 may be up to
  4 MB (room for photo-heavy screens), with an 8 MB decoded-image
  cache in PSRAM.

## 2026.08.19

- **Online, offline and simulation are now three separate things.**
  Going online never silently switches the editor into simulation;
  the transport controls show only when the simulation is on.
- **Five sizes of quality text** (13/15/18/20/22/24/28/36 px plus the
  numeric and seven-segment faces), TTF import for custom fonts, and
  full Central European diacritics everywhere.
- **I2C toolbox**: a bus scanner in the editor, an address dropdown
  fed by the chip catalog, and automatic chip identification where the
  silicon supports it.
- The device Resources page was decluttered; column widths are
  draggable; device renames propagate everywhere.

## 2026.08.18

- S3 boards run their PSRAM at the full 80 MHz — measurably smoother
  screens on photo-heavy projects.
- The editor flashes runtimes itself (no external tooling), and the
  installer ships a precompiled runtime for every supported board —
  the *Upload runtime* button works on a fresh equipment with nothing
  else installed.
- Fixes for installed-editor paths (Program Files is read-only) and
  for user profiles with diacritics in the name.

## 2026.08.17

