---
title: "Drive library"
slug: drives
section: "Drive library"
order: 317
sidebar_position: 317
image: img/drv-overview.webp
image_alt: "A drive's Overview page in the editor"
generator: tools/docs_export.py
---

# Drives

A project can hold **frequency drives and servo drives** beside its
screens and its program - or on their own, with no controller at all
(*New project* > **Drives only**). A
drive is a node under **Drives** in the device tree; its page shows every
parameter of the drive, the way its maker groups them, and the project
keeps only what you changed from the factory settings. The editor reads
the drive, compares, writes, stores the settings in the drive and watches
chosen values while it is connected.

![A drive's Overview page](img/drv-overview.webp){: .sb-center}

## The drive library

Every series is one description in the drive library: each parameter with
the maker's own code, name, group, type, unit, range, default and the
names of its values, and its address on every connection the series
speaks.

| Brand | Series | Connection from the PC | Setup screens | Controlled from the device |
|:---|:---|:---:|:---:|:---:|
| Lenze | i550 cabinet | - | yes | - |
| Lenze | 8200 vector, 9300 servo, SMVector | LECOM | - | - |
| Parker | AC10 | - | yes | - |
| Parker | AC15, AC20, AC30 | Modbus TCP | yes | yes |
| KEB | F6 / S6 | Modbus TCP | yes | - |
| Siemens | SINAMICS G120 (CU240B-2 / CU240E-2), G120C | USS | yes | yes |
| Siemens | MICROMASTER 420, 430, 440, SINAMICS G110 | USS | yes | - |
| Siemens | SINAMICS S120 servo, S120 vector | - | yes | - |
| fabrika | F600, F700 | - | yes | - |

A series without a connection from the PC is still complete in the
project: its parameters are set on the page, kept in the project and
written by the device that drives it.

## Adding a drive

Right-click **Drives** in the device tree, **Add drive...**, pick the
brand and the series and give the drive a name. A project may hold as
many drives as it needs; **Remove drive** on the drive's own node takes
it away.

## The drive's page

The list on the left of the page holds its views:

| View | What it shows |
|:---|:---|
| **Overview** | the brand, series and firmware, the connection, the buttons that talk to the drive, the Quick setup, Control from the device and how many parameters are changed |
| **Motor**, **Ramps & limits**, **Control**, **Inputs & outputs** | the [setup screens](/docs/drives/drives-setup/) - the essential settings drawn as fields, whatever the vendor calls them |
| **Parameters** | every parameter in the maker's groups |
| **Monitor** | the values you chose, read over and over while the drive is connected |
| **Trend**, **Diagnostics** | open once the drive is connected |

### Parameters

![Every parameter of a Lenze i550 in its groups](img/drv-params.webp){: .sb-center}

The groups on the left are the maker's; **All parameters** shows the whole
set. Search finds a parameter by its address or its name, **Changed
only** shows what the project changes. A value is edited in its cell - a
parameter with named values offers them in a list, a number is checked
against the parameter's type and range, and a value equal to the default
simply leaves the list of changes. The columns follow the maker: the
object (`0x2917:0`), the code (`P220.00`, `p1120`, `0436`), the Modbus
register where the series has one, the default, the unit, the access.

Right-click a parameter's name and choose **Monitor** to watch it on the
Monitor view.

## Talking to the drive from the PC

Pick the **Connection** and type the drive's **Address**:

| Connection | Address | Example |
|:---|:---|:---|
| Modbus TCP | the drive's IP address, with `:port` and `/unit` when they differ | `192.168.0.50`, `192.168.0.50:502/3` |
| LECOM | the COM port of the PC's RS485 adapter, the baud rate when it differs, the drive's address | `COM5/1`, `COM5@19200/1` |
| USS | the COM port, the baud rate when it differs, the drive's USS address | `COM5/0`, `COM5@38400/1` |

The buttons on the Overview page then:

| Button | What it does |
|:---|:---|
| **Read from drive** | reads every parameter the drive has |
| **Compare** | shows the parameters whose value in the drive differs from the project (Parameters, *Differs from the drive*) |
| **Write to drive** | writes every parameter the project changes |
| **Save in drive** | stores the drive's parameters in its own non-volatile memory, the way the maker does it (a value written over a fieldbus usually lives in RAM until then) |
| **Take into the project** | takes the values just read into the project - a drive set up by hand on site becomes the project's settings |

A job runs in the background, the page says what it is doing and
**Cancel** stops it. A drive that does not answer, a parameter it refuses
or a value out of its range is said in words on the page.

## Control from the device

A drive of a supported series can be **run by the device's program**
over Modbus: start and stop, the speed in Hz, its state back - with one
block, [DRIVE](/docs/blocks/drv-drive/). See [Control from the device](/docs/drives/drives-control/).
