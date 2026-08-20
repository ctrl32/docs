# What's new

Every release replaces the previous one — the editor's update check
offers it automatically, and a project saved in an older version always
opens in a newer one. Versions are dated: `year.month.day.build`.

## 2026.08.20.3

**Everything fits in ladder now.** Function blocks with state — timers,
counters, ramps, filters, hysteresis — sit in a rung as EN boxes with
IEC 61131-3 semantics: the block simply does not execute while the rung
is off, its state freezes and its outputs hold. This is the same EN/ENO
behaviour you know from CoDeSys or an S7.

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

