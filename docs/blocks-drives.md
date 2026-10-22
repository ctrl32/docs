# Drives

The blocks a program uses to run a frequency drive the device controls over
Modbus. A drive of the project (**Drives** in the tree) becomes such a
drive on its Overview page with **Control from the device**: the editor
makes the drive's Modbus device and its variables, writes the settings that
give the bus the control into the drive's parameter set and adds the
`drives` block library to the project. The block is written in ST, so you
can open it and read how it builds the drive's control word.

The control word and the setpoint are written to the drive on every poll,
and the drive's own fieldbus watchdog stops the drive when the device stops
answering.

A stop over a fieldbus is not a safety function - the drive's safe torque
off (STO) terminals must be wired.

---

## The blocks

<!-- fb-index: begin -->

| Block | What it does | Linux | ESP32 | STM32 |
|:---|:---|:---:|:---:|:---:|
| [DRIVE](drv-drive.md) | Runs one drive the device controls over Modbus: start and stop, the direction, the speed in Hz, fault acknowledgement - and its state, actual speed and current back. | yes | yes | yes |

<!-- fb-index: end -->
