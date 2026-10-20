# Setting up a Linux device

[The Linux runtime](linux-runtime.md) says what it can do; this page
is the other half — **how a blank device becomes one**, step by step,
nothing assumed. At the end the device boots straight into your
visualisation, serves its WEBview and OPC UA, and appears in the
editor's [scanner](find-devices.md) like any other board.

!!! tip "The road from the editor"
    [Raspberry Pi](setup-raspberry-pi.md) does the whole thing from
    the editor, with pictures, for a Raspberry Pi or a reTerminal. This
    page is the reference behind it: every device, every setting, and
    the manual road.

Three devices are in the catalogue — the reTerminal, the DK2 and
**any 64-bit Raspberry Pi** — and they differ only in how the
operating system gets onto them. The ctrl32 part — the runtime, the
service, the settings file — is identical on all of them.

!!! note "Where the runtime comes from"
    The Linux runtime **installs with the editor** — there is
    nothing separate to download. After installing the editor, look
    in `%ProgramData%\ctrl32\linux\`:

    - `ctrl32-runtime-reterminal-<version>.tar.gz` — prebuilt for
      the reTerminal (`ctrl32run` + its service file),
    - `ctrl32-runtime-dk2-<version>.tar.gz` — prebuilt for the DK2
      (plus the library set it runs against),
    - `ctrl32-runtime-raspi-<version>.tar.gz` — prebuilt for **any
      64-bit Raspberry Pi** (Pi 4, Pi 5, CM4, CM5, Zero 2 W): the
      runtime, its service file and `ctrl32run.default.example`, the
      settings file with every bus variable explained.

    Everything is version-matched to the editor.
    Everything else on this page is standard, freely available
    software.

---

## Prepare a Linux device (the editor's road)

For a Raspberry Pi or a reTerminal with a fresh **Raspberry Pi OS** on
its card (SSH enabled and a user with a password, both set in the
Raspberry Pi Imager), the editor installs the runtime itself:
*Online* → *Prepare a Linux device*. The page opens as a tab beside the
project's own, so the project stays at hand while a device installs or
restarts, and every line the work prints goes to Messages as well.

![The Prepare a Linux device page before anything has been looked at](img/lx-prepare-open.webp){: .sb-center}

| Field / button | What it does |
|:---|:---|
| **Address**, **User**, **Password** | how the editor logs in; the password is the one set when the card was written |
| **Device** | which device it is (reTerminal or Raspberry Pi) — it sets the identity the runtime gets |
| **Do not ask for the password again** | ticked by default: the editor puts its own key on the device the first time, later visits need the address alone. The password is used once and never stored |
| **Look at the device** | logs in and reads what the device is; **changes nothing**. The page then shows what it found and the plan |
| **Operating system of this device** | the device's own settings, below — each ticked line becomes one step of the plan |
| **Prepare it** | works through the plan and reports each step as it lands |

![The page after a look: what the device is, and the list of steps Prepare will take](img/lx-prepare-plan.webp){: .sb-center}

The plan is the whole of what Prepare does: the runtime copied over and
unpacked, installed with its own account and permissions, given the
device's identity, started by the system at every boot, and waited for
until it answers. A device that already runs ctrl32 is told so; from
there the network road takes over. After Prepare the device needs no
password: programs and runtime updates go over the network.

The runtime update dialog shows the device, the runtime it runs and the
one the editor has:

![Upload runtime: the device, its current version and the one the editor has](img/lx-runtime-dlg.webp){: .sb-center}

The board card in the tree shows what the device told the editor about
itself — its buses, its interfaces, its screen:

![The board card of a Linux device](img/lx-board-card.webp){: .sb-center}

---

## Seeed reTerminal (Raspberry Pi CM4)

### 1. The operating system

Flash **Raspberry Pi OS Lite (64-bit)** with the official Raspberry
Pi Imager. *Lite* is deliberate: the device needs no desktop — the
runtime draws the glass itself, and a desktop would only fight it
for the screen.

In the Imager's settings (the gear, before writing):

- set a **hostname** you will recognise on the network,
- create a **user** (any name; the examples below use `ctrl32`),
- **enable SSH** — the first sessions run over it.

Boot the reTerminal with the freshly written card, find its address
(your router's client list, or `ping <hostname>.local`) and connect:

```
ssh ctrl32@<address>
```

### 2. The display driver

The reTerminal's 5" panel needs Seeed's device-tree overlay. Two
things matter and both have caught people:

- the **kernel headers must match the running kernel** — run
  `sudo apt update && sudo apt full-upgrade`, reboot, and only then
  build the driver, or DKMS builds against the wrong version;
- the Raspberry Pi's own *Touch Display 2* overlay looks like it
  should work on this panel — **it does not**. Use Seeed's.

```
sudo apt install git dkms raspberrypi-kernel-headers
git clone https://github.com/Seeed-Studio/seeed-linux-dtoverlays
cd seeed-linux-dtoverlays
sudo ./scripts/reTerminal.sh
sudo reboot
```

The script installs the panel, touch and sensor modules through DKMS
(they survive later kernel updates) and adds
`dtoverlay=reTerminal,tp_rotate=1` to `/boot/firmware/config.txt`.
After the reboot the glass lights up with the console — the panel is
alive.

### 3. The runtime user's groups

The runtime draws and reads touch as a normal user — no root. That
works through three group memberships:

```
sudo usermod -aG video,render,input ctrl32
```

Log out and back in so they take effect.

### 4. The ctrl32 runtime

Copy `ctrl32-runtime-reterminal-<version>.tar.gz` from
`%ProgramData%\ctrl32\linux\` on the editor PC to the device (`scp`
does it in one line) and unpack it into the user's home (the
examples use `/home/ctrl32/ctrl32/`), then install the service:

```
sudo cp ctrl32run.service /etc/systemd/system/
sudo nano /etc/systemd/system/ctrl32run.service
```

In the unit, set `User=` to your user and the path in `ExecStart=`
to where `ctrl32run` really is. Then write the settings file the
unit reads:

```
sudo nano /etc/default/ctrl32run
```

```
CTRL32_PACK=/home/ctrl32/ctrl32/current.visu
CTRL32_PORT=8080
CTRL32_HWID=0x20000001
```

| Setting | Meaning |
|:---|:---|
| `CTRL32_PACK` | the program file the runtime runs — the editor's upload replaces it atomically |
| `CTRL32_PORT` | the WEBview / upload port; `8080` is the Linux standard the scanner expects |
| `CTRL32_HWID` | the device's identity — `0x20000001` = reTerminal, `0x20000002` = STM32MP157C-DK2, `0x20000003` = any Raspberry Pi. The scanner names the device by it, and an upload for different hardware is refused by name |
| `CTRL32_RS485` | optional: the Modbus RTU line — a USB-RS485 adapter (`/dev/ttyUSB0`, direction handled by the adapter) or the SoC UART of an RS485 HAT (`/dev/ttyAMA0`) |
| `CTRL32_RS485_RTS` | `1` with a HAT on the SoC UART: the kernel drives the direction pin (DE) from RTS. Leave it out for a USB adapter. **More lines**: `CTRL32_RS485=/dev/ttyUSB0,/dev/ttyUSB1,…` names up to four RS485 lines (`CTRL32_RS485_RTS=1,0,…` per line); the project declares the extra lines (right-click *Serial* in the editor → *Add RS485 line*, each with its own baud and parity) and every RTU device and variable says which line it is on — the same unit number may then live on two lines |
| `CTRL32_ECAT` | optional: the network interface your **EtherCAT** slaves hang on — a second NIC or a USB one that the runtime owns alone — **nothing else goes over that link**: the runtime refuses an interface that carries an IP address and says which address it found; remove the address or use a dedicated adapter. The project's EtherCAT page lists the slaves in bus order and their signals; the service unit grants the raw-socket right the master needs |
| `CTRL32_CAN` | optional: the CAN interface for CANopen, raw CAN and net32 over CAN — `can0` of a CAN HAT (MCP2515 / MCP251xFD overlay) or a USB adapter (`gs_usb`, `slcan`). The runtime sets the interface's bitrate from the project and brings it up itself, see below. **More buses**: `CTRL32_CAN=can0,can1` — the project declares its extra buses (right-click the CAN node in the editor → *Add CAN bus*), each with its own bitrate, and every CAN device, axis and variable says which bus it is on; the same node-ID may then live on two buses |

Enable and start:

```
sudo systemctl daemon-reload
sudo systemctl enable --now ctrl32run
```

The device now shows the ctrl32 mark, and without a program it waits
for one. `CTRL32_PACK` may point at a file that does not exist yet —
the first upload from the editor creates it.

#### CAN on a Linux device

The runtime configures the interface itself when it starts: the
**bitrate** the project declares on its CAN node (every bus its own),
bus-off recovery, and the interface up. Nothing is typed on the
device — the service unit carries the right this needs. The log says
which it did:

```
can: can0 up at 500000 bit/s (set by the runtime)
```

A runtime started by hand from a shell has no such right; it then
prints the `ip link` line to run once as root instead. A USB adapter
that sets its own speed (`slcan`) is only brought up.

#### Modbus TCP slave on a Linux device

A Linux device answers as a **Modbus TCP slave** on port 502 (or the
port the project's Modbus slave page sets) — a SCADA, a PLC or another
ctrl32 device reads and writes its variable map over the network, up
to four connections at once. The service unit carries the right the
standard port needs; a runtime started by hand from a shell is told
so and can use a port above 1023 instead.

#### The serial console

On a Raspberry Pi image the device's own UART (`/dev/serial0`)
carries a login console by default. A HAT on that UART then shares
the line with a shell that answers every Modbus frame with a login
prompt — the slave "never answers". The runtime names this when it
opens the port; the editor turns the console off for you (below), or
do it on the device (`raspi-config` → *Interface Options* → *Serial
Port*: login shell **No**, hardware **Yes**) and reboot. A USB-RS485
adapter has no such conflict.

#### The operating system, from the editor

Everything a Linux device needs beyond the project is set from the
editor — *Online* → *Prepare a Linux device*, then **Look at the
device**. Under the device's summary the editor shows what it can set
on the device itself:

- **Expansion board** — a preset for the boards the catalog knows
  (the reTerminal E10-1: its CAN controller, RS-485/RS-232 and second
  network port), which writes the boot lines the board needs and turns
  on what its own chips require (the I2C driver, the serial port). The
  board's RS-485 transceiver is driven the way the board wires it — on
  the E10-1 the direction is a pair of GPIO lines, and picking its
  serial port on the bus page writes that with the port. The
  board's own chips are known to the scanner by name; the ones the
  operating system drives (the E10-1's control expander and its
  charger) are shown as such and never added to a project
- the boot lines the device itself asked for (an expansion controller
  you assigned on the device's bus page)
- **Free the serial port from the login console** — ticked whenever a
  console is found on a UART
- the I2C driver at every start
- the **device name**
- the **network**: an interface, then *leave as it is*, *automatic
  address (DHCP)* or a *fixed address* with prefix, gateway and DNS
- **Buses on the header** - SPI, I2C and the UART as ticks (their pins
  are the processor's: SPI0 on GPIO 7-11, I2C on GPIO 2/3, the UART on
  GPIO 14/15). The ticks start as the device's boot configuration says;
  a tick adds its line, an untick removes it, and the device restarts
- **CAN and serial controllers on SPI** - a list: **+ Add controller**
  takes the next free chip select, and any mix fits - four CAN
  controllers, two CAN and two serial, and so on. Each row picks the chip
  (MCP2515, MCP2517FD/MCP2518FD, SC16IS750 with one serial port or
  SC16IS752 with two), the SPI bus and chip select (SPI0 and SPI1 on a
  Raspberry Pi 3; SPI0, SPI1 and SPI3 to SPI6 on a Pi 4 or a CM4), the
  **chip-select pin** (the bus's own or any GPIO of the header), the
  interrupt pin and the crystal. The editor counts how many more fit on
  this device: a bus whose pins I2C, the UART or another bus already use
  drops out, and a chip select an expansion board holds (the reTerminal
  E10-1's own CAN controller) shows as taken. Two functions on one pin,
  or a chip whose driver the device's kernel lacks, are refused in words
  before anything is written. After the restart every CAN controller is
  a CAN interface (`can0`, `can1`, ...) and every serial controller one or
  two serial ports, ready to pick in the **Buses and chips** tab of the
  device's board page. A device with CAN of its own on the board (the
  STM32MP1) uses that one
- **Real-time kernel for EtherCAT** - one tick, for a bus cycle under a
  millisecond. The editor installs the distribution's real-time kernel
  for the device's processor (and its headers where a display driver has
  to be rebuilt for it), boots it with the last processor core kept for
  the bus, and gives the runtime the setting that pins its bus thread to
  that core. The standard kernel stays on the card and
  `config.txt.bak-prert` beside the boot configuration is the way back.
  A device that already runs it says so in place of the tick; a device
  whose package source offers no real-time kernel, or whose boot
  configuration the editor does not know, is refused in words

The same section is on the **board page** of a Linux device, under what
the scan found: a login for the device and *Look at the device*, then
tick and *Apply*. Prepare is for a device that has nothing yet; the board
page is for the one the project runs on. Prepare itself is a page beside
the project's own, not a window in the way - the project stays at hand
while a device installs or restarts, and every line the work prints goes
to Messages as well.

The editor lists what pressing **Apply** will do, step by step, and
says beforehand when the device will restart (only a boot setting
needs that). Each step is checked on the device after it ran; a step
that did not take is named, and the rest is left alone. Pressing
Apply again on a device that already is as chosen changes nothing —
the editor says so. A setting the device cannot take (a boot
configuration the editor does not know, a network not managed by
NetworkManager, a name that is not a name) is refused in words before
anything is sent.

Changing the address of the port the editor is talking over ends the
session — the editor says so; afterwards the device answers at the
new address, and that is the address to type.

### 5. Check it

- `systemctl status ctrl32run` — *active (running)*; the console
  lives in `journalctl -u ctrl32run`.
- A browser on `http://<address>:8080` answers.
- The editor's scanner (:ti-eyeglass:) shows the device with its
  name and version.

From here on, everything is [the normal flow](linux-runtime.md):
download a program, go online, read it over OPC UA.

---

## Any Raspberry Pi

Every 64-bit Raspberry Pi — Pi 4, Pi 5, CM4 or CM5 on any carrier,
Zero 2 W — runs the same runtime as the reTerminal. In the editor
the device is **Raspberry Pi** (`0x20000003`); a monitor on HDMI
shows the visualisation, a device without one serves WEBview.

1. Write **Raspberry Pi OS Lite (64-bit)** to the card with the
   Raspberry Pi Imager; set the user, enable SSH and the network in
   its settings. Boot, log in.
2. From the PC, copy the bundle over and run its installer — three
   commands in PowerShell (Windows 10/11 ship `scp` and `ssh`; they
   ask for the Pi user's password you set in the Imager):

   ```
   scp "$env:ProgramData\ctrl32\linux\ctrl32-runtime-raspi-<version>.tar.gz" pi@raspberrypi.local:~
   ssh pi@raspberrypi.local "mkdir -p rt && tar xzf ctrl32-runtime-raspi-*.tar.gz -C rt && sudo sh rt/install.sh"
   ```

   `install.sh` creates the `ctrl32` user, installs the runtime and
   the systemd unit, writes `/etc/default/ctrl32run` and starts the
   service; it prints the `/devinfo` address at the end.
3. The bus lines your hardware has go into `/etc/default/ctrl32run`:
   `CTRL32_RS485` for an RS485 adapter or HAT, `CTRL32_CAN` for a
   CAN HAT or USB adapter (the runtime sets its bitrate from the
   project), `CTRL32_ECAT` for a dedicated EtherCAT NIC. No monitor: nothing
   to set, the runtime serves WEBview when no display is connected.
   After an edit: `sudo systemctl restart ctrl32run`.
4. From here on SSH is not needed: the editor's scanner finds the
   device, **Deploy** sends the project over the network, ONLINE
   works — step 5 above.

A CAN HAT needs its device-tree overlay in `/boot/firmware/config.txt`
(the HAT's vendor page says which, e.g.
`dtoverlay=mcp2515-can0,oscillator=16000000,interrupt=25`); a USB CAN
adapter appears as `can0` by itself. Check with `ip link` — the
interface must exist before the runtime can open it.

## ST STM32MP157C-DK2

The DK2 has no card slot workflow of its own — ST's **OpenSTLinux
Starter Package** is written to the SD card through the USB-DFU port
with **STM32CubeProgrammer** (both are downloads from ST; the
Starter Package page documents the boot-switch positions and the
flashing steps).

One trap worth knowing before it costs an evening: CubeProgrammer's
flash layout file (`.tsv`) resolves the image paths **relative to
itself** — keep the `.tsv` next to the image files it names, not in
a subfolder.

After the first boot (console on the ST-LINK's virtual COM port,
115200; or SSH once the device has an address):

1. **Disable the demo desktop** — it owns the glass otherwise:
   `systemctl disable --now weston.service` (the exact unit name can
   differ between OpenSTLinux releases; `systemctl list-units | grep
   -i weston` finds it). With weston gone, the **boot splash**
   (`psplash`) has nothing to quit it and keeps holding the display
   — the shipped service unit kills it before every start
   (`ExecStartPre=-/usr/bin/pkill psplash`); keep that line when you
   adjust paths, or the glass stays on the splash forever.
2. Copy `ctrl32-runtime-dk2-<version>.tar.gz` from
   `%ProgramData%\ctrl32\linux\` on the editor PC and unpack it to
   `/opt/ctrl32/`.
3. Copy the service unit **from the bundle** to
   `/etc/systemd/system/` and write `/etc/default/ctrl32run` with
   `CTRL32_PACK=/opt/ctrl32/current.visu`,
   `CTRL32_HWID=0x20000002` and port `8080`. Unlike on the
   reTerminal, **do not edit the unit's `ExecStart`**: it starts the
   runtime through the loader shipped in the bundle's `libs/` —
   OpenSTLinux's own C library is older than the one the runtime is
   built against, and a plain `ExecStart` fails on exactly that.
4. `systemctl daemon-reload && systemctl enable --now ctrl32run`.

The checks are the same: the service running, the browser on
`:8080`, the device in the scanner.

---

## The ports the runtime uses

| Port | What lives there |
|:---|:---|
| `8080` (HTTP) | WEBview, the program upload, the scanner's identity question |
| `4840` | the [OPC UA server](linux-runtime.md) |
| `3232` | the editor's online wire |

On a plant network with a firewall between the editor and the
device, these three are what has to pass.

---

## Any other Linux device

The prebuilts cover the catalogue devices, and the Raspberry Pi one
runs on every 64-bit Raspberry Pi. For another device - an industrial
PC, a gateway, another module - write to us: the runtime is built for
it and joins the catalogue, like every device here.

---

## Updating

- **The program**: from the editor, over the network — nothing on
  this page is repeated, ever.
- **The runtime**: from the editor, over the network, the same way a
  board's runtime goes since 1.00.042 - *Flash runtime* with the device's
  IP. The device checks the file is built for its processor, starts it
  once as a self-check, keeps the previous binary as `ctrl32run.prev` and
  rolls back on its own if the new runtime never gets as far as the
  program and the server. The program file, the retained values and the
  settings file are not touched. By hand it is still: stop the service,
  replace `ctrl32run`, start the service - the one road onto a runtime
  older than 1.00.042.
- **The kernel** (reTerminal): safe — the display driver is in DKMS
  and rebuilds itself for the new kernel.

> **Raspberry Pi and a monitor.** The `raspberry_pi` board declares its display as *optional*: a fresh project starts with a WEBview screen, and HMI screens are added from the tree (right-click *Screens* → *Add screen*) when a monitor hangs on the HDMI. The runtime draws the glass only when a DRM output is connected; without one it serves WEBview and runs on.
