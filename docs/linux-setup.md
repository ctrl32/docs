# Setting up a Linux device

[The Linux runtime](linux-runtime.md) says what it can do; this page
is the other half — **how a blank device becomes one**, step by step,
nothing assumed. At the end the device boots straight into your
visualisation, serves its WEBview and OPC UA, and appears in the
editor's [scanner](find-devices.md) like any other board.

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
      settings file with every bus variable explained,
    - `ctrl32-runtime-src-<version>.tar.gz` — the **source
      archive**: any Linux device with a C++ toolchain builds its
      own runtime from it (see the end of this page).

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
| `CTRL32_ECAT` | optional: the network interface your **EtherCAT** slaves hang on — a second NIC or a USB one that the runtime owns alone (no IP address on it). The project's EtherCAT page lists the slaves in bus order and their signals; the service unit grants the raw-socket right the master needs |
| `CTRL32_CAN` | optional: the CAN interface for CANopen, raw CAN and net32 over CAN — `can0` of a CAN HAT (MCP2515 / MCP251xFD overlay) or a USB adapter (`gs_usb`, `slcan`). The bitrate is set on the interface in the service unit, see below. **More buses**: `CTRL32_CAN=can0,can1` — the project declares its extra buses (right-click the CAN node in the editor → *Add CAN bus*) and every CAN device, axis and variable says which bus it is on; the same node-ID may then live on two buses |

Enable and start:

```
sudo systemctl daemon-reload
sudo systemctl enable --now ctrl32run
```

The device now shows the ctrl32 mark, and without a program it waits
for one. `CTRL32_PACK` may point at a file that does not exist yet —
the first upload from the editor creates it.

#### CAN on a Linux device

The runtime uses the interface as the operating system configured
it; the **bitrate** is set in the service unit, where the line is
already prepared (remove the `#`, match the project's bitrate):

```
ExecStartPre=+/sbin/ip link set can0 up type can bitrate 500000 restart-ms 100
```

`restart-ms` lets the kernel recover from a bus-off. If the interface
is down when the runtime starts, its log prints exactly this line
with the project's bitrate filled in.

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
2. Unpack `ctrl32-runtime-raspi-<version>.tar.gz` from
   `%ProgramData%\ctrl32\linux\` into `/home/<user>/ctrl32/`.
3. Copy `ctrl32run.service` to `/etc/systemd/system/` and set
   `User=` and the `ExecStart=` path as on the reTerminal; copy
   `ctrl32run.default.example` to `/etc/default/ctrl32run` and edit
   it — `CTRL32_HWID=0x20000003`, and the bus lines your hardware
   has: `CTRL32_RS485` for an RS485 adapter or HAT, `CTRL32_CAN` for
   a CAN HAT or USB adapter (its bitrate line in the unit). No
   monitor: `CTRL32_HEADLESS=1`.
4. `sudo systemctl daemon-reload && sudo systemctl enable --now ctrl32run`
   — then step 5 above.

A CAN HAT needs its device-tree overlay in `/boot/firmware/config.txt`
(the HAT's vendor page says which, e.g.
`dtoverlay=mcp2515-can0,oscillator=16000000,interrupt=25`); a USB CAN
adapter appears as `can0` by itself. Check with `ip link` — the
interface must exist before the runtime can open it.

## ST STM32MP157C-DK2

The DK2 has no card slot workflow of its own — ST's **OpenSTLinux
Starter Package** is written to the SD card through the USB-DFU port
with **STM32CubeProgrammer** (both are free downloads from ST; the
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

## Any other Linux device: building from source

The two prebuilts cover the catalogue devices. For anything else —
another Pi, an industrial PC, a gateway — the **source archive**
builds the same runtime natively on the device itself, which also
means it links against the device's own system libraries and no
compatibility questions arise:

```
tar xzf ctrl32-runtime-src-<version>.tar.gz
sudo apt install build-essential cmake ninja-build libdrm-dev libssl-dev
cmake -G Ninja -B build runtime-linux
ninja -C build ctrl32run
```

(The first `cmake` downloads the OPC UA library, so the device needs
network access once.) The result is `build/ctrl32run`; from there the
service installation is exactly step 4 above. A device without a
display runs the same runtime headless — WEBview, OPC UA and the
editor connection all work the same.

---

## Updating

- **The program**: from the editor, over the network — nothing on
  this page is repeated, ever.
- **The runtime**: stop the service, replace `ctrl32run`, start the
  service. The program file and the retained values live next to it
  and survive the swap.
- **The kernel** (reTerminal): safe — the display driver is in DKMS
  and rebuilds itself for the new kernel.
