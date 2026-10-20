---
title: Quick start
source: docs/quickstart.md
hero: img/quickstart-sealin.webp
---

# From an installed editor to a program running in the board - in minutes

All you need is the board, a USB cable and a PC. Install one program, open or create a project, flash the runtime once, download, and watch live values in your own rungs.

## Who it is for
- Anyone evaluating ctrl32 for the first time
- Electricians and PLC programmers who want ladder, FBD or ST on an ESP32, STM32 or Linux board
- Builders of their own hardware on a processor module, with or without a display

## What you get
- **One program does everything**: the ST compiler, the pack builder and the flasher are compiled into the editor - no helper process to be missing, moved or a version behind; the pack the editor builds is byte for byte the one the release tools build
- Shipped projects: `tutorials\` (one idea per project) and `examples\` (whole working projects)
- A **New project** wizard: name, location, hardware (board or module) and what the project does - each tick creates the matching part of the project, every part can be added or removed later
- Your own board with a display: reuse a catalog board's display initialisation and touch calibration, pick the display and touch pins from the module's unused pins; `.hdw32` imported boards are offered too
- **Flash runtime** over USB from the editor, read back and verified; a chip that does not match the board is refused, so a wrong COM port cannot be written
- **Runtime updates over the network** on two-slot boards, with automatic rollback
- **Download cannot brick the board**: inactive slot, verification, switch only when everything is right
- **ONLINE**: live values from the board in the ladder rungs, on block pins, in the variable list and in the screen preview

## How it works
1. Run `ctrl32-setup-<version>.exe`.
2. *File -> Open* a shipped project, or *New project* (Welcome tab, toolbar or Ctrl+N) and pick the hardware and what the project does.
3. First time only: *Flash runtime* on the board page - over USB, verified, tens of seconds.
4. Pick the COM port and click *Download to board*: built into a pack, written to the inactive slot, verified, switched, restarted.
5. Switch on ONLINE and watch the program run.

## Pictures
- ![The seal-in example open in the ladder editor](img/quickstart-sealin.webp) - the seal-in tutorial in the ladder editor
- ![The New project wizard with a board picked: the name, where it lands and what the project will do](img/newproj-board.webp) - the New project wizard
- ![The Flash runtime dialog](img/deploy-runtime.webp) - writing the runtime from the editor
- ![The same rungs with the board running: green is current flowing, and every pin carries its live value](img/editor-online.png) - ONLINE: live values in the rungs

## Runs on
- Any catalog board, or a processor module carrying your own hardware
- ESP32 boards with 8 MB or 16 MB of flash (two runtime slots, network update), 4 MB boards (USB road)
- STM32 F7 (network update through the board's QSPI memory; first move via ST-LINK)
- Linux devices (runtime bundle under `%ProgramData%\ctrl32\linux`)

## Facts to keep exact
- Installer: `ctrl32-setup-<version>.exe`; installs `ctrl32_editor.exe` (the editor), `ctrl32.dat` (catalog of boards and chips), `runtimes\` (prebuilt firmware for every supported board), `examples\` (sample projects)
- Starter projects: `tutorials\ladder_sealin.prj32` (seal-in circuit), `tutorials\time_setpoint.prj32` (a TIME setpoint typed on the screen driving a timer's PT), `examples\tm8_6_proofer.prj32` (three-zone proofing cabinet: PT100 probes, SSR heaters, hysteresis, operator interface in WEBview), `examples\tubex_panel.prj32` (Ethernet, a Modbus slave, NeoPixel LEDs)
- The editor starts empty; Name is mandatory and becomes the folder and file name; default location `Documents\ctrl32\projects`, project at `<location>\<name>\<name>.prj32`
- A project cannot be deployed without hardware; the board decides pins, memory and which runtime is flashed; a project may change hardware later
- Wizard roles: visualization on the display, WEBview screens, first program in ladder or ST, CAN master, Modbus RTU or TCP slave, MQTT, net32
- On a module the *Visualization* tick decides the runtime: with a display, or headless with bigger program limits; on a board the type comes from the catalog
- An old runtime refuses a newer pack - the fix is always: flash the runtime
- Network runtime update: needs 8 MB or 16 MB flash (two slots); the board writes the slot it is not running from, checks it is for its own chip and memory, restarts, confirms only once the program loaded and the server is up; otherwise the bootloader rolls back at the next reset; program, retentive values and network settings stay; under a minute
- The first update onto the two-slot table goes over USB
- 4 MB boards keep the USB road (a display runtime is 2.4 MB, two do not fit); device page shows `ota=0`
- STM32 F7: two parts (a small loader that never changes + the runtime); the running one is kept aside, the new one written and verified, put back if it does not confirm; generations counted `g1`, `g2`, ...; one-time move via *Flash runtime* over ST-LINK
- Linux: checks the file is built for its processor, starts it once as a self-check, keeps the previous binary, rolls back on its own; the first update onto a runtime that knows this road (1.00.042) is the bundle's `install.sh`
- Download sequence: build pack -> inactive slot -> board verifies CRC, format and target board -> only then switch the active slot and restart; on error the old pack keeps running; the switch restarts the program (never mid-run)
- No port is preselected; both transfer dialogs ask for it when bytes are about to move
- ONLINE requires the editor and the board to run the same program, otherwise the editor offers to download it

## Call to action
Download the editor and open `tutorials\ladder_sealin.prj32` - then make your own with *New project*.
