# I/O expanders and drivers

Thirteen expanders, three capacitive touch controllers, two stepper
drivers and a fan controller.

## Why an expander

An ESP32 driving a 16-bit display bus has very few pins left. An expander
turns two I2C wires into sixteen digital pins, and a second expander at
another address turns them into thirty-two.

| | |
|:---|:---:|
| the standard 16-bit expanders | `TCA9555`, `PCF8575`, `MCP23017` |
| 8-bit, cheaper | `PCF8574`, `PCF8574A`, `PCA9554`, `MCP23008` |
| SPI instead of I2C | `MCP23S17`, `MCP23S08` |
| just four pins | `PCA9536` |
| shift registers — cheapest per pin | `SN74HC595` (out), `SN74HC165` (in) |
| a modern part with per-pin drive control | `PI4IOE5V6408` |

!!! warning "An expander pin is not a relay output"
    These pins source a few milliamps — enough for an LED or an
    optocoupler input, nothing more. A relay, a solenoid or a contactor
    needs a driver stage between the expander and the load.

!!! tip "Interrupt pins save polling"
    Most expanders pull an interrupt line when an input changes. Wire it,
    and the board reads the expander when something happened rather than
    constantly — which matters when the same bus also carries sensors.

## Capacitive touch controllers

`CAP1188`, `MPR121`, `TTP229` — these are **touch buttons**, not touch
screens. They sense a finger near a copper pad behind a board, so you can
build a keypad with no moving parts and no holes in the enclosure. `MPR121`
gives twelve channels, `CAP1188` eight, `TTP229` sixteen.

Ideal where the front has to be sealed and wipeable. Poor where operators
wear thick gloves.

!!! note "A board's own touch screen is not here"
    The glass on an HMI panel comes with its controller, and the board
    catalogue already knows which one is fitted. See
    [HMIview](hmiview.md) for what that means for your screens.

## Stepper drivers

`POWERSTEP01` and `TMC5160` drive stepper motors — and they are more than
a power stage. Both take a target position and generate the motion
profile themselves, which is why the [motion blocks](blocks-motion.md)
can command an axis on them the same way they command a drive over
CANopen.

`TMC5160` is the quiet one: its stealth modes make a stepper nearly
silent, which matters in a room with people in it.

## Fan control

`EMC2101` controls a fan and reads its tacho back.

!!! tip "Reading the tacho is worth the wire"
    A stopped fan looks exactly like a running one until something
    overheats. A tacho turns "the fan should be on" into "the fan is
    turning" — the difference between a warning and a repair bill.

## The chips

### I/O expanders

| Chip | Bus | What it is |
|:---|:---:|:---|
| `MCP23008` | I2C | I2C expander 8 DIO — the 8-bit brother of the MCP23017, address 0x20–0x27. Inputs get the internal pull-up; the latch is written before the direction switches. |
| `MCP23017` | I2C | I2C expander 8+8 DIO — 16 pins, address 0x20–0x27. Inputs get the internal 100 k pull-up (GPPU); outputs write the latch before the direction switches. |
| `MCP23S08` | SPI | SPI expander 8 DIO (the MCP23008 over SPI, hardware address pins grounded). Inputs get the pull-up; latch before direction. addr = CS pin. |
| `MCP23S17` | SPI | SPI expander 8+8 DIO (the MCP23017 over SPI, hardware address pins grounded). Inputs get the pull-up; latch before direction. addr = CS pin. |
| `PCA9536` | I2C | I2C expander, 4 DIO pins, fixed address 0x41 — the small brother of the TCA9555 for a few signals (register layout is the single-byte variant of the same family). |
| `PCA9554` | I2C | I2C expander 8 DIO (PCA9554/TCA9534 register family) — address 0x20–0x27, the A variant 0x38–0x3F (the checked range covers both). |
| `PCF8574` | I2C | I2C expander, 8 quasi-bidirectional pins, address 0x20–0x27 (the PCF8574A variant uses 0x38–0x3F and will be a separate type). No config registers: an input pin keeps latch 1 (weak pull-up), writing 0 is a hard low — common relay boards are therefore active-low (invert). |
| `PCF8574A` | I2C | I2C expander, 8 quasi-bidirectional pins — the A variant of the PCF8574 differs ONLY in the address range 0x38–0x3F (both fit on one bus, 16 addresses total). |
| `PCF8575` | I2C | I2C expander, 16 quasi-bidirectional pins, address 0x20–0x27. Like the PCF8574 but 16-bit: an input pin keeps latch 1 (weak pull-up), writing 0 is a hard low — relay boards are typically active-low (invert). |
| `PI4IOE5V6408` | I2C | I2C expander 8 DIO (Diodes Inc) — inputs get the pull-up, the latch is written before the direction switches. Address 0x43–0x44. VERIFY ON THE BENCH. |
| `SN74HC165` | SPI | SPI shift register, 8 INPUTS — the input mirror of the 74HC595. Wire CS to /PL (the parallel load fires when CS asserts). addr = CS pin. |
| `SN74HC595` | SPI | SPI shift register, 8 OUTPUTS — the cheap relay-board driver. Wire CS to RCLK (the latch fires when CS deasserts). One 8-bit register per chip; daisy chains are a future type. addr = CS pin. |
| `TCA9555` | I2C | I2C expander 8+8 DIO — 16 pins, address 0x20–0x27. |

### Touch controllers

| Chip | Bus | What it is |
|:---|:---:|:---|
| `CAP1188` | I2C | I2C capacitive touch controller — 8 touch pads as INPUTS (bool variables). Address 0x28–0x2D. Touch buttons behind the front glass; the interrupt latch is cleared by the driver. |
| `MPR121` | I2C | I2C capacitive touch controller — 12 pads as INPUTS (bool variables), default thresholds 12/6. Address 0x5A–0x5D. VERIFY ON THE BENCH. |
| `TTP229` | I2C | I2C capacitive keypad (TTP229-BSF) — 16 keys as INPUTS (bool variables). Fixed address 0x57. VERIFY ON THE BENCH (the 16-key I2C mode needs the TP2 strap). |

### Motor drivers

| Chip | Bus | What it is |
|:---|:---:|:---|
| `POWERSTEP01` | SPI | SPI stepper system-in-package (ramps, current, position). Used as a motion AXIS backend (AxisRec backend 1), not as a pin chip. |
| `TMC5160` | SPI | SPI stepper motion controller + driver (Trinamic): internal ramp generator, stallGuard, 256-µstep. Used as a motion AXIS backend (AxisRec backend 2), not as a pin chip; the same driver runs the TMC5130 (IOIN version tells them apart). Motor current defaults are conservative — tune GLOBALSCALER/ IRUN on the bench (sense-resistor dependent). |

### Fan controllers

| Chip | Bus | What it is |
|:---|:---:|:---|
| `EMC2101` | I2C | I2C fan controller — channels: 0 = PWM duty OUTPUT (variable 0–100 %), 1 = fan RPM input, 2 = external diode temperature [°C], 3 = internal temperature [°C]. Fixed address 0x4C. Enclosure cooling with real feedback. VERIFY ON THE BENCH. |

Every entry above is in the editor: pick the chip, give it
an address or a chip-select pin, and its channels become variables.
See [Adding a peripheral](adding-peripherals.md) for the
click-through.
