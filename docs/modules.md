# Hardware catalog

One editor, one project file, one runtime family. Pick a board from the
catalog, or put your own design on a supported module and assign its pins in
the editor. What you draw and program runs the same way on every device
below; what differs is how much of it fits and what the hardware can reach.
Every module runs with a display or headless, and WEBview serves the same
screens to a phone either way.

## What every device brings

- **Programs in ladder, function blocks or structured text** - one runtime,
  the same block library everywhere: timers, counters, edge detection, PID,
  motor and valve control, drive and motion blocks
- **Screens on the glass and in the browser** - WEBview shows the project to a
  phone or a PC straight from the device, nothing to install
- **Modbus RTU and Modbus TCP** as master and as slave, **CANopen** master with
  drives, **MQTT** with the usual brokers and Home Assistant
- **Alarms, trends, recipes and retentive values**, a diagnostic log with
  timestamps, forcing and online monitoring from the editor
- **Updates over the network** - the program on every device; the runtime
  itself on modules with 8 MB of flash or more and on Linux, with an
  automatic roll-back when the new one does not come up
- **Diagnostics you can read** - cycle time, memory, bus and drive health on
  the device page and in the editor

## Three sizes

| | Compact | Standard | Linux |
|:---|:---|:---|:---|
| Hardware | ESP32 without PSRAM | ESP32 with PSRAM, ESP32-S3, ESP32-P4, STM32 | Raspberry Pi, STM32MP1, any Linux computer |
| Variables | 128 | 512 | 5120 |
| Alarms | 32 | 128 | 1280 |
| Program blocks | 128 | 512, 1024 headless | 5120 |
| Drive axes | 1 | 4 | 8 |
| Screens | 32 | 32 | 320 |
| Trend traces | 4 | 4, 8 on ESP32-S3 and ESP32-P4 | 8 |
| Phone viewers at once | 1 with a display, 2 headless | 2 | many |
| Network | Ethernet, WiFi when memory allows | Ethernet and WiFi | Ethernet and WiFi |
| Recipes | 4 definitions, 8 sets each | 8 definitions, 64 sets each | 8 definitions, 64 sets each |
| Secure MQTT (TLS) | - | ESP32-S3, ESP32-P4, STM32 | yes |
| OPC UA, EtherCAT master, several CAN and RS485 lines | - | - | yes |

A Compact device is the cheapest way onto a small piece of equipment or a
gateway; a Standard device is the reference for a panel; the Linux runtime is
free and takes the large plants.

## Chips

| Chip | Speed | Wireless | Ethernet | CAN | Displays | Size |
|:---|:---|:---|:---|:---|:---|:---|
| ESP32 | 2 x 240 MHz | WiFi, Bluetooth | yes | 1 | SPI panels | Compact, Standard with PSRAM |
| ESP32-PICO-V3-02 | 2 x 240 MHz | WiFi, Bluetooth | yes | 1 | headless | Standard |
| ESP32-S3 | 2 x 240 MHz | WiFi, Bluetooth LE | over SPI | 1 | parallel and RGB panels up to 800x480 | Standard, the reference |
| ESP32-P4 | 2 x 400 MHz | with a companion chip | yes | 3 | MIPI DSI and RGB panels | Standard, the fastest |
| STM32F746 | 216 MHz | - | yes | 2 | LTDC panels | Standard |
| STM32MP157 | 2 x 650 MHz | module | yes | 2 | LTDC, DSI | Linux |
| Raspberry Pi CM4, 4, 5 | 4 cores | WiFi, Bluetooth LE | yes | over SPI or USB | HDMI, DSI | Linux |

Coming next: the STM32H7, STM32F4 and STM32G4 families. Single-core chips
are not supported - the logic and the graphics live on separate cores by
design.

## Modules

A module is the chip with its flash and memory as the manufacturer solders it.
Every module below is a target for your own hardware; the boards column lists
the catalog boards built on it.

### ESP32

| Module | Flash | PSRAM | Size | Boards on it | Note |
|:---|:---|:---|:---|:---|:---|
| ESP32-MINI-1-H4 | 4 MB (embedded) | - | Compact |  |  |
| ESP32-MINI-1-N4 | 4 MB (embedded) | - | Compact |  |  |
| ESP32-MINI-1U-H4 | 4 MB (embedded) | - | Compact |  | external antenna |
| ESP32-MINI-1U-N4 | 4 MB (embedded) | - | Compact |  | external antenna |
| ESP32-WROOM-32E-N4 | 4 MB | - | Compact | Adafruit HUZZAH32 Feather, DevKitC WEBview setup, ESP32-DevKitC V4, LaskaKit ESPlan, LilyGO T-CAN485, Olimex ESP32-EVB, Olimex ESP32-GATEWAY, Olimex ESP32-PoE, Olimex ESP32-PoE-ISO, SparkFun Thing Plus ESP32, T-Display setup, TTGO T-Display |  |
| ESP32-WROOM-32E-H4 | 4 MB (quad) | - | Compact |  |  |
| ESP32-WROOM-32E-H8 | 8 MB (quad) | - | Compact |  |  |
| ESP32-WROOM-32E-N16 | 16 MB (quad) | - | Compact |  |  |
| ESP32-WROOM-32E-N16R2 | 16 MB (quad) | 2 MB (quad) | Standard |  |  |
| ESP32-WROOM-32E-N4R2 | 4 MB (quad) | 2 MB (quad) | Standard |  |  |
| ESP32-WROOM-32E-N8 | 8 MB (quad) | - | Compact |  |  |
| ESP32-WROOM-32E-N8R2 | 8 MB (quad) | 2 MB (quad) | Standard |  |  |
| ESP32-WROOM-32UE-H4 | 4 MB (quad) | - | Compact |  | external antenna |
| ESP32-WROOM-32UE-H8 | 8 MB (quad) | - | Compact |  | external antenna |
| ESP32-WROOM-32UE-N16 | 16 MB (quad) | - | Compact |  | external antenna |
| ESP32-WROOM-32UE-N16R2 | 16 MB (quad) | 2 MB (quad) | Standard |  | external antenna |
| ESP32-WROOM-32UE-N4 | 4 MB (quad) | - | Compact |  | external antenna |
| ESP32-WROOM-32UE-N4R2 | 4 MB (quad) | 2 MB (quad) | Standard |  | external antenna |
| ESP32-WROOM-32UE-N8 | 8 MB (quad) | - | Compact |  | external antenna |
| ESP32-WROOM-32UE-N8R2 | 8 MB (quad) | 2 MB (quad) | Standard |  | external antenna |
| ESP32-WROVER-E-N8R8 | 8 MB | 8 MB (quad) | Standard |  |  |
| ESP32-WROVER-E-N16R2 | 16 MB (quad) | 2 MB (quad) | Standard |  |  |
| ESP32-WROVER-E-N16R8 | 16 MB (quad) | 8 MB (quad) | Standard |  |  |
| ESP32-WROVER-E-N4R2 | 4 MB (quad) | 2 MB (quad) | Standard |  |  |
| ESP32-WROVER-E-N4R8 | 4 MB (quad) | 8 MB (quad) | Standard | Olimex ESP32-PoE2 |  |
| ESP32-WROVER-E-N8R2 | 8 MB (quad) | 2 MB (quad) | Standard |  |  |
| ESP32-WROVER-IE-N16R2 | 16 MB (quad) | 2 MB (quad) | Standard |  |  |
| ESP32-WROVER-IE-N16R8 | 16 MB (quad) | 8 MB (quad) | Standard |  |  |
| ESP32-WROVER-IE-N4R2 | 4 MB (quad) | 2 MB (quad) | Standard |  |  |
| ESP32-WROVER-IE-N4R8 | 4 MB (quad) | 8 MB (quad) | Standard |  |  |
| ESP32-WROVER-IE-N8R2 | 8 MB (quad) | 2 MB (quad) | Standard |  |  |
| ESP32-WROVER-IE-N8R8 | 8 MB (quad) | 8 MB (quad) | Standard |  |  |

### ESP32-PICO-V3

| Module | Flash | PSRAM | Size | Boards on it | Note |
|:---|:---|:---|:---|:---|:---|
| ESP32-PICO-MINI-02-N8R2 | 8 MB (embedded) | 2 MB (embedded) | Standard |  |  |
| ESP32-PICO-MINI-02U-N8R2 | 8 MB (embedded) | 2 MB (embedded) | Standard |  |  |
| ESP32-PICO-V3 | 4 MB (embedded) | - | Compact |  |  |
| ESP32-PICO-V3-02 | 8 MB (embedded) | 2 MB (embedded) | Standard | inoCORE32-TM1.0, inoCORE32-TM1.1, inoCORE32-TM8.6 |  |
| ESP32-PICO-V3-ZERO | 4 MB (embedded, quad) | - | Compact |  |  |

### ESP32-S3

| Module | Flash | PSRAM | Size | Boards on it | Note |
|:---|:---|:---|:---|:---|:---|
| ESP32-S3-MINI-1-N8 | 8 MB (quad) | - | Standard |  |  |
| ESP32-S3-MINI-1U-N8 | 8 MB (quad) | - | Standard |  | external antenna |
| ESP32-S3-WROOM-1-N16 | 16 MB (quad) | - | Standard | S3 CAN setup, S3 SSD1963 setup |  |
| ESP32-S3-WROOM-1-N16R16VA | 16 MB (quad) | 16 MB (octal) | Standard |  |  |
| ESP32-S3-WROOM-1-N16R2 | 16 MB (quad) | 2 MB (quad) | - |  | octal PSRAM only |
| ESP32-S3-WROOM-1-N16R8 | 16 MB | 8 MB (octal) | Standard | ESP32-S3-DevKitC-1 (N16R8), inoHMI32, inoHMI43, stepHMI32.4, stepHMI32.5 |  |
| ESP32-S3-WROOM-1-N8 | 8 MB (quad) | - | Standard | S3-DevKitC-1 WEBview setup |  |
| ESP32-S3-WROOM-1-N8R2 | 8 MB (quad) | 2 MB (quad) | - |  | octal PSRAM only |
| ESP32-S3-WROOM-1-N8R8 | 8 MB | 8 MB (octal) | Standard |  |  |
| ESP32-S3-WROOM-1U-N16 | 16 MB (quad) | - | Standard |  | external antenna |
| ESP32-S3-WROOM-1U-N16R16VA | 16 MB (quad) | 16 MB (octal) | Standard |  | external antenna |
| ESP32-S3-WROOM-1U-N16R2 | 16 MB (quad) | 2 MB (quad) | - |  | octal PSRAM only; external antenna |
| ESP32-S3-WROOM-1U-N16R8 | 16 MB (quad) | 8 MB (octal) | Standard |  | external antenna |
| ESP32-S3-WROOM-1U-N8 | 8 MB (quad) | - | Standard |  | external antenna |
| ESP32-S3-WROOM-1U-N8R2 | 8 MB (quad) | 2 MB (quad) | - |  | octal PSRAM only; external antenna |
| ESP32-S3-WROOM-1U-N8R8 | 8 MB (quad) | 8 MB (octal) | Standard |  | external antenna |

### ESP32-P4

| Module | Flash | PSRAM | Size | Boards on it | Note |
|:---|:---|:---|:---|:---|:---|
| ESP32-P4NRW32 | 16 MB | 32 MB (hex) | Standard | ESP32-P4-NANO |  |

## Boards

| Board | Chip | Display | Ethernet | WiFi | CAN | RS485 | Size | Phone viewers |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Adafruit HUZZAH32 Feather | ESP32 | - | - | yes | yes | yes | on request | on request |
| DevKitC WEBview setup | ESP32 | - | - | yes | - | - | Compact | 2 |
| ESP32-DevKitC V4 | ESP32 | - | - | yes | yes | yes | on request | on request |
| ESP32-P4-NANO | ESP32-P4 | 800 x 1280 | yes | yes | - | - | Standard | 2 |
| ESP32-S3-DevKitC-1 (N16R8) | ESP32-S3 | - | - | yes | yes | yes | on request | on request |
| inoCORE32-TM1.0 | ESP32-PICO-V3 | - | yes | yes | yes | yes | Standard | 2 |
| inoCORE32-TM1.1 | ESP32-PICO-V3 | - | yes | yes | yes | yes | Standard | 2 |
| inoCORE32-TM1.3 | ESP32-PICO-V3 | - | - | yes | - | - | on request | on request |
| inoCORE32-TM8.6 | ESP32-PICO-V3 | - | - | yes | yes | yes | Standard | 2 |
| inoHMI32 | ESP32-S3 | 480 x 272 | yes | yes | yes | yes | Standard | 2 |
| inoHMI43 | ESP32-S3 | 480 x 272 | - | yes | yes | yes | Standard | 2 |
| inoHMI53 | ESP32-S3 | 800 x 480 | - | yes | yes | yes | on request | on request |
| LaskaKit ESPlan | ESP32 | - | yes | yes | - | yes | Compact | 2 |
| LilyGO T-CAN485 | ESP32 | - | - | yes | yes | yes | on request | on request |
| Olimex ESP32-EVB | ESP32 | 240 x 320 | yes | yes | yes | - | Compact | 1 |
| Olimex ESP32-GATEWAY | ESP32 | - | yes | yes | - | - | Compact | 2 |
| Olimex ESP32-PoE | ESP32 | - | yes | yes | - | - | Compact | 2 |
| Olimex ESP32-PoE-ISO | ESP32 | - | yes | yes | - | - | Compact | 2 |
| Olimex ESP32-PoE2 | ESP32 | - | yes | yes | - | - | Standard | 2 |
| Raspberry Pi | Linux | 1920 x 1080 | - | module | yes | yes | Linux | many |
| S3 CAN setup | ESP32-S3 | - | - | yes | yes | - | Standard | 2 |
| S3 SSD1963 setup | ESP32-S3 | 480 x 272 | - | yes | - | - | Standard | 1 |
| S3-DevKitC-1 WEBview setup | ESP32-S3 | - | - | yes | - | - | Standard | 2 |
| Seeed reTerminal | Linux | 1280 x 720 | - | module | yes | yes | Linux | many |
| SparkFun Thing Plus ESP32 | ESP32 | - | - | yes | yes | yes | on request | on request |
| ST 32F746GDISCOVERY | STM32F746 | 480 x 272 | yes | - | - | - | Standard | 2 |
| ST STM32MP157C-DK2 | Linux | 480 x 800 | - | module | yes | yes | Linux | many |
| stepHMI32.4 | ESP32-S3 | 480 x 272 | - | yes | yes | yes | Standard | 2 |
| stepHMI32.5 | ESP32-S3 | 480 x 272 | - | yes | yes | yes | Standard | 2 |
| stepHMI32.7 | ESP32-S3 | 800 x 480 | - | yes | yes | yes | on request | on request |
| T-Display setup | ESP32 | 240 x 135 | - | yes | - | - | Compact | 1 |
| TTGO T-Display | ESP32 | 240 x 135 | - | yes | yes | yes | on request | on request |

Your own board: choose the module it carries, assign the pins, and the
editor validates the wiring against the module's rules before anything is
built. A photo and a description make it a catalog entry you can share.
