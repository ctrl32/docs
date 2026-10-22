---
title: "Drives: DRIVE"
slug: drv-drive
section: "Function blocks"
order: 210
sidebar_position: 210
generator: tools/docs_export.py
---

# DRIVE

Runs one drive the device controls over Modbus: start and stop, the direction, the speed in Hz, fault acknowledgement - and its state, actual speed and current back.

## In Structured Text

```iecst
PROGRAM DRIVE_ST
VAR drive : DRIVE; END_VAR
  drive(Enable := drive_enable, Reverse := drive_reverse, Speed := drive_speed, Reset := drive_reset, StatusWord := drive_statusword, ActualRaw := drive_actualraw, CurrentRaw := drive_currentraw, Profile := drive_profile, SpeedScale := drive_speedscale, ActualScale := drive_actualscale, CurrentScale := drive_currentscale);
  drive_controlword := drive.ControlWord;
  drive_setpointraw := drive.SetpointRaw;
  drive_ready := drive.Ready;
  drive_running := drive.Running;
  drive_fault := drive.Fault;
  drive_actualspeed := drive.ActualSpeed;
  drive_current := drive.Current;
END_PROGRAM
```

## Where it runs

| Linux runtime | ESP32 boards | STM32 |
|:---:|:---:|:---:|
| yes | yes | yes |

**Needs:** a drive of the project controlled from the device (Modbus RTU or Modbus TCP), runtime line 1.07 or newer.

## Pins

| Pin | Kind | Type | Default | Meaning |
|:---|:---:|:---:|:---:|:---|
| `Enable` | input | BOOL | - | TRUE runs the drive; FALSE stops it along the drive's own ramp. |
| `Reverse` | input | BOOL | - | TRUE turns the motor the other way. |
| `Speed` | input | REAL | - | The speed setpoint in Hz (the motor's frequency). |
| `Reset` | input | BOOL | - | TRUE acknowledges a fault of the drive; hold it for a moment, then release it. |
| `StatusWord` | input | DINT | - | The drive's status word, as read (the drive's `_sw` variable). |
| `ActualRaw` | input | REAL | - | The drive's actual speed as the drive reports it (the `_act` variable). |
| `CurrentRaw` | input | REAL | - | The motor current as the drive reports it (the `_cur` variable). |
| `Profile` | parameter | DINT | 1 | How the drive's control word is built - set by the editor from the drive's description: 1 the PROFIdrive control word, 2 a control word with the comms bits, 3 CiA 402. |
| `SpeedScale` | parameter | REAL | 1.0 | The drive's setpoint units per Hz - set by the editor from the drive's parameters (its reference speed and the motor's nameplate). |
| `ActualScale` | parameter | REAL | 1.0 | Hz per unit of the drive's actual speed - set by the editor. |
| `CurrentScale` | parameter | REAL | 1.0 | A per unit of the drive's current - set by the editor. |
| `ControlWord` | output | DINT | - | The control word for the drive (the `_cw` variable). |
| `SetpointRaw` | output | REAL | - | The speed setpoint in the drive's own units (the `_sp` variable). |
| `Ready` | output | BOOL | - | TRUE while the drive is ready to run. |
| `Running` | output | BOOL | - | TRUE while the drive runs (its operation is enabled). |
| `Fault` | output | BOOL | - | TRUE while the drive reports a fault; its code is in the drive's `_flt` variable. |
| `ActualSpeed` | output | REAL | - | The actual speed in Hz. |
| `Current` | output | REAL | - | The motor current in A. |

## Description

**Using it.** Open the drive in the tree, set **Control from the device**
(the RS485 line or the drive's IP address, and its Modbus address), then
place a DRIVE block in a program and pick the drive in the block's
properties (**Drive**). The block's word pins are bound to the drive's
variables and its parameters are set from the drive's description; only
Enable, Reverse, Speed and Reset are yours. Write the drive's parameters
into the drive once (**Write to drive** on its page) so it takes its
control from the bus.

**The watchdog.** The control word and the setpoint are written to the
drive on every poll, not only when they change, and the drive's own
fieldbus watchdog is set to about one second. When the device stops
answering - a power cut, a broken cable - the drive stops by itself.

**Starting.** The block walks the drive's state machine: it asks for the
ready state first and enables the drive when it reports ready, so
Enable can simply stay TRUE. After a fault, Enable alone does not
restart the drive - acknowledge with Reset.

**Which drives.** Siemens SINAMICS G120 (CU240B-2 / CU240E-2) and G120C
on Modbus RTU over RS485, Parker AC15, AC20 and AC30 on Modbus TCP. The
page of any other drive says that the device cannot control its series
yet.

| Drive | Bus | Control word | Speed setpoint |
|:---|:---:|:---:|:---:|
| Siemens SINAMICS G120, G120C | Modbus RTU | 047E stop, 047F run, 04FE acknowledge | 4000 hex = the reference speed p2000 |
| Parker AC15, AC20 | Modbus TCP | CC77 stop, CC7F run, CCF0 acknowledge | % of MAX SPEED (0457) |
| Parker AC30 | Modbus TCP | CC77 stop, CC7F run, CCF0 acknowledge | % of 100% Speed in RPM (0464) |

**Safety.** A stop over a fieldbus is not a safety function. The drive's
safe torque off (STO) terminals must be wired.

---

Every block of the family: [Drives](/docs/blocks/blocks-drives/) · every block: [Function blocks](/docs/blocks/)
