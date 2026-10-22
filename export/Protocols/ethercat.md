---
title: "EtherCAT"
slug: ethercat
section: "Protocols"
order: 310
sidebar_position: 310
generator: tools/docs_export.py
---

# EtherCAT

An EtherCAT line is one loop of cable through every device and back.
There is no polling and no addressing in the usual sense: a single
frame travels the loop, each device reads its own bytes out of it and
writes its own bytes into it as the frame passes. That is why a
hundred terminals cost the same cycle as three.

ctrl32 is the **master** of that line, on a Linux device with a
network port to spare. The devices on it are its slaves, in the order
they are wired.

---

## What it costs you to set up

Nothing that a CANopen drive does not also cost, and one thing less:
there are no node-IDs to set with DIP switches. A slave is identified
by **where it sits** on the cable, and by what it says it is — its
vendor and product code. The runtime refuses to run the line when the
device at a position is not the one the project expects, which is the
protection you would otherwise get from a careful label.

---

## The port and the cable

The master **owns its network interface**: it sends raw frames on it,
and no IP address lives there. Pick the port in *Online › Prepare a
Linux device* or in *Buses of this device*; it is stored in the
device's settings as `ecat=<interface>` (for instance `ecat=eth1`, the
second port of a reTerminal E10-1).

The line runs from the master into the first device's **IN** socket,
out of its **OUT** and into the next device's IN; the last device's OUT
stays empty. A cable in an OUT socket where an IN belongs is the
commonest reason for a line on which no slave answers.

---

## The device comes from its description

Every vendor ships an **ESI file** — an XML description of the device:
its identity, the sizes of its process data, what travels in it and
what can be written. It plays exactly the part an EDS file plays for
CANopen.

![The EtherCAT master's page: the cycle and the slaves in bus order](img/ecat-buspage.webp){: .sb-center}

Put the file in the device library (*Tools › Device library*, the
EtherCAT section) and the EtherCAT page's **Add from library** turns a
picked device into a slave: identity, image sizes, the CiA 402 layout
when it is a drive, and one signal with its variable for every value
the device sends by default. The Lenze i550, i700, i750 and i950 ship
in the library (the i950 in two firmware generations; pick the one on the
name plate - a drive answers the scan with its own code and revision).

---

## The device's window

![The tree of a Linux device: the network adapters under Ethernet, and the EtherCAT master under the one it owns](img/ecat-tree.webp){: .sb-center}

The line is added in the tree under **Ethernet** (*EtherCAT*), and its
page is the master's: the cycle and the slaves in the order they are
wired. A Linux device usually has two network ports, so *Ethernet*
shows one row per adapter and the master hangs under the one it owns -
the port with no address. The adapters appear once the editor has
looked at the device; until then the master sits under *Ethernet*
itself.

Double-click a slave and it opens with the same tabs a CAN device has:

![The Device tab: identity, the process image and the CiA 402 offsets](img/ecat-device-tab.webp){: .sb-center}

- **Device** — who it is: vendor, product, the revision of the
  description it came from, the sizes of its process image, and for a
  drive the four byte offsets of the CiA 402 words.
- **Variables** — the device's own objects. Tick what it should send or
  take and *Import* writes the rest.
- **PDO mapping** — what really travels, in the shape every EtherCAT
  tool uses: the slave's **sync managers** (SM2 carries the outputs,
  SM3 the inputs), the **PDOs assigned** to the one picked, and the
  **entries** of the PDO picked among those, each with its offset and
  its name. The device's own mapping is the vendor's and is shown as
  it is; the configurable PDO is the one this project fills.
- **SDO parameters** — what is written into the device every time the
  line starts.
- **I/O mapping** — which byte of the image feeds which variable, with
  its gain and offset.
- **Log** — the device's own messages, read from the panel.

![The PDO tab in the shape every EtherCAT tool uses: the sync managers, what is assigned to the picked one, and what that PDO carries](img/ethercat-device.webp){: .sb-center}

---

## Process data and what a master may add

A slave's process data is partly fixed by its vendor and partly the
master's choice. A drive, for instance, always sends its status word,
its actual speed and its error code; its current, torque, DC link
voltage and output frequency are objects the master may **add** to the
data it sends.

![The Variables tab: the device's own objects, ticked](img/ecat-vars-tab.webp){: .sb-center}

That is what **Map from the device** does. Tick the values in the
device's own dictionary and the editor writes the whole plan: the
mapping, the assignment in the order the standard wants, the signals
that read those bytes, the variables they need and the new image size.
Map again and the plan is replaced, not appended to.

![The start-up writes the editor composed: the assignment cleared, the mapping written, both objects assigned](img/ecat-sdo-tab.webp){: .sb-center}

Doing it by hand means composing 32-bit mapping words out of an index,
a sub-index and a bit width, and writing them in an order the device
accepts. A drive that receives them in the wrong order answers with a
mapping error and sends zeros — and looks, from the outside, exactly
like a broken device.

The order a device accepts is the CoE one: the assignment object
(`0x1C13` for what the device sends, `0x1C12` for what it takes) set to
count 0 first, then the mapping object (sub 0 = 0, the entries, sub 0 =
the count), and only then the assignment with its objects. Write a
mapping entry in the notation the dictionary uses - hex, `0x60780010`
for index 0x6078, sub 0, 16 bits; a word converted to decimal by hand is
easily one digit off, and a drive takes the mapping and refuses the
assignment with nothing saying why.

**Declare both assignments among the start-up writes**, the receive
side as well as the send side, even where the device's default would
do. A drive switched off and on while the master was configuring it can
come back with an empty assignment; with both declared it is set right
at the next start instead of refusing every output image (the bus then
never reaches OPERATIONAL and the device reports an invalid output
configuration).

---

## Which byte is which variable

![The I/O mapping tab: every byte of the image, its variable, its gain](img/ecat-iomap-tab.webp){: .sb-center}

The signals of a slave are plain variables with a byte offset, a width
and a gain. A screen reads them, a program computes with them, and
nothing in between needs code.

---

## A drive on the line

A CiA 402 drive is an **axis**, and the motion blocks command it the
same way whether it sits on CANopen or on EtherCAT — `MC_Power`,
`MC_MoveVelocity` and the rest do not know the difference. The axis
wizard makes the whole thing in one step: the slave from its
description, the axis on its position, the start-up writes that put
the drive in velocity mode under network control, and the variables
the blocks bind to. It is in the tree under *Motion › add axis*, with
**EtherCAT** chosen as the bus and the device picked from the library.
An axis on EtherCAT names its slave by the slave's **position on the
line** (1 = the first device after the master), where a CANopen axis
names a node-ID.

What a drive needs beyond that is its **motor data**. A frequency
inverter keeps them itself - pole pairs, rated speed, rated current,
the voltage curve - and a drive that has never met its motor runs the
factory values: the first start ends in an over-current trip. Set them
in the drive, by its keypad or its maker's tool, before the first
start. This catches people out when a drive's **network module is
replaced**: on drives of the i550 kind the parameter set lives in the
module, so the drive looks identical and knows nothing about the motor.

A servo inverter such as the i700 or the
i750 keeps nothing at power-off and expects its controller to write
them at every start - so the motor's catalogue row (resistance,
inductance, rated speed, frequency, power, voltage, the back-EMF
constant, the inertia, rated current and torque) and the loops computed
for it are **start-up writes of the slave**. A drive run on the factory
motor data turns, but its current loop is tuned for another winding:
the bench's i700s hunted at low speed on the factory set of a motor with
four times the inductance, and were steady to a few increments once
their own row was written. A servo that hunts is judged from the
innermost loop out: the current controller's gain scales with the
motor's inductance (the reset time, L/R, stays), and no speed- or
position-loop setting cures a current loop tuned for another winding.
On a double inverter the second axis takes the same objects **0x800
higher**. For another motor, its catalogue row replaces these writes.

**The rated mains voltage is a start-up write too.** The Lenze servo
inverters default to a 400 V supply (`0x2540:1 = 1`) and forget the
setting at power-off. Fed single-phase from 230 V, the DC link (about
315 V) then sits above the undervoltage error threshold and below the
reset threshold: the drive reaches OPERATIONAL, reads healthy, `0x2540:8`
("DC link voltage critical") is 1, and every enable answers the error
**0x3220** (DC-link undervoltage). Write `0x2540:1 = 0` (230 V) at every
start on such a supply; on a 400 V supply leave it out. A drive that will
not enable is read at `0x2540` and `0x6079` (the DC link) before its
motor is blamed.

**Tune against a trend.** A screen with the actual velocities of the
axes on one trend at a short sample time (50 ms) shows what the loops
do: a well-tuned axis draws a flat line, one whose loop hunts draws a
band. The current, speed and position controller settings are start-up
writes of the slave, so a setting found on the bench is written at
every start.

### The drive's settings from its maker's tool

A servo inverter of the i700 and i750 kind keeps no settings of its own:
its motor data, its control loops, its limits live in the controller,
which writes them into the drive at every start. On your line that
controller is this device, so the settings belong in the project. Set the
drive up once with the maker's tool (motor identification, autotuning,
the oscilloscope — through the device's gateway, see below), save the
drive's parameter file (a GDC file), and press **Import parameters
(GDC)...** on the slave's *Start-up writes* tab. Every setting that
differs from the drive's default becomes a start-up write — scaled and
sized by the device's description — and the identity, the process-data
mappings and the drive's own bookkeeping are left alone, those are the
device's business. The status line says what came of the file: how many
settings will be written, how many sat at their default, how many are
read-only or texts.

From then on a drive swapped for a spare comes up with the same settings
at the next start, with nothing to do on the drive; import the file again
after a change in the maker's tool. A file of another kind of drive is
refused, and a drive the library has no description for cannot be
imported, because the values could not be sized.

### A servo in cyclic position mode

A servo inverter - the Lenze i700, i750 and i950 are the ones in the
library - is driven differently from a frequency inverter: it runs
**csp**, cyclic synchronous position. The device owns the profile. Every
cycle it ramps the velocity the program asked for, integrates it into a
32-bit position setpoint and sends it with the velocity as feed-forward;
the drive's own position loop follows and reports its actual position
and velocity back. The program does not see the difference: the same
`MC_Power` and `MC_MoveVelocity` command a servo and a frequency
inverter, and `CO_RAMPTIME` sets the ramp the setpoint follows.

*Add from library* recognises a servo by its description and lays it
out: the csp pair of process data objects travels, and beside it the
**torque limits** object when the device has one (`MC_SetTorqueLimit`
holds the limits on the drive through it; while no block does, the
device writes the limits the drive had at its configuration every
cycle - an object a drive takes from the image every cycle can never be
left at zero, that is a motor that cannot move). A touch probe the
vendor also assigns stays off. The assignment is declared among the
start-up writes, and the slave's window shows the mode *cyclic position
(csp)* with the byte offsets of the 32-bit words - the target position,
the actual position, the actual velocity, the velocity offset, the
torque offset (the acceleration feed-forward `MC_TorqueFF` writes),
the torque limits, the actual torque, and the mode inside the receive
object, which such a drive wants every cycle. A servo can be declared
in **cyclic torque** mode (cst) instead: its setpoint is then the target
torque `MC_TorqueControl` commands and the window names the speed
limits the drive holds it under - the cst pair of objects replaces the
csp pair (the i700 excludes the one when the other is assigned). Two numbers describe the
drive's units: the increments of one motor revolution (65536 on these
drives) and the velocity units per rpm (Lenze counts 2^31-1 for
480 000 rpm; the description's dictionary carries the figure, and a
drive without a dictionary takes the vendor's known unit). The axis's
own window then says what the program speaks: `units_per_rev` (65536 =
the positions ARE the increments) and the time base of velocities -
`rpm` on such a servo, so the phases are increments and every speed on a
screen is rpm (see [Motion blocks](/docs/blocks/blocks-motion/)). A **double
inverter** carries two axes in one slave: the window names where axis
B's words begin, and an axis on it picks *A* or *B*. On the i700 double
an axis takes 17 bytes and sends 21 (the target position, the velocity
feed-forward and the mode in; the actual velocity and the actual
position among what comes back), so axis B's words start 17 bytes into
the output image and 21 into the input image.

### A virtual master

A line shaft needs a master, and the master need not be a drive. *Add
virtual master axis* on the EtherCAT node makes an axis with nothing
behind it: the program powers it and commands it like any axis
(`MC_Power`, `MC_MoveVelocity`, `CO_RAMPTIME`, `MC_MoveAbsolute`), the device
runs its profile every bus cycle, and every follower geared to it with
`MC_GearIn` sees the commanded position of the same cycle - the line's
one clock. A drum that only takes a speed follows its velocity
(`MC_ReadActualVelocity`); a drum that must be in register is geared to it in
position like the plates. The axis's window has one more choice: a
**source** variable - a 32-bit integer counter, such as the drum's
encoder on the drive's input B mapped as a process-data signal - and
the virtual master is then the measured drum, with the counter's
increments per revolution named beside it; the followers compensate
the chain delay as they do behind a servo master. Following the measured
drum adds nothing to the register - the counter is the same word a
direct master reads - and the followers stay locked to it through every
stop; a drum that follows a velocity only drifts against its followers
with every stop (thousands of increments at a few hundred rpm), which is
why a drum that has to stay in register is measured. A Linux device only:
the EtherCAT master steps it.

A servo in csp needs the **distributed clock** (below): its position
loop expects the setpoint at a fixed phase of its own cycle. While the
axis is off, faulted or the slave is away, the setpoint follows the
actual position, so enabling never jumps and a drive that comes back
starts from where it stands.

---

## Bringing the line up

Deploy, and read the device's log. A healthy line says, in order: the
interface is up, the slaves found and what they are, the mapping
written, the images mapped, the axis bound, the cycle running. The
device page's EtherCAT state (`ecat=`) then shows the master up and
every slave operational.

| The log says | What it means |
|:---|:---|
| *no slave answers* | the cable is in the wrong socket (OUT where IN belongs), or the port named in the device's settings is not the one the cable is in |
| *another device at that position* | the vendor or product code of the device at that position does not match the project's; compare them on the Device tab |
| *SDO rejected* | the device refused a start-up write; the line that follows gives its reason in the device's own words |
| *the bus did not reach OPERATIONAL* | usually the mapping or the assignment: a device that receives one it cannot do says so and sends zeros (see *Process data* above) |

A slave that drops out shows as a working-counter error in the bus
counters of the device page.

---

## Safety

Stopping over EtherCAT is **not** a safety function. The emergency
stop belongs on the drive's STO terminals, hard-wired, exactly as with
any other bus.

---

## What the line does not do

- **One line per device.** The master runs on one network interface;
  a second line would need a second port and is not supported.
- **One clock per line.** The distributed clock phase-locks the cycle
  to the first slave that carries one; a slave without a clock, or one
  that refuses the sync type, stays synchronous to its process data
  and the console says so.
- **Linux only.** The boards run CANopen; EtherCAT wants an interface
  that belongs to the master alone.

---

## Where to go next

- [CANopen](/docs/buses/canopen/) — the same drive on the other bus.
- [Motion blocks](/docs/blocks/blocks-motion/) — what commands an axis.


## Distributed clock and fast cycles

The line's cycle is the master's setting: *Cycle ms* on the EtherCAT
page, or *Cycle µs* when a servo wants less than a millisecond (the µs
field wins when it is set). Two things decide how fast a line can really
run:

- **The distributed clock.** With *Distributed clock* ticked, every device
  that has a clock gets SYNC0 at the cycle and the master locks its own
  cycle to the line's reference clock, so a servo sees its setpoints at
  the same instant every cycle. A device without a clock (the i550, for
  one) keeps running SM-synchronous on the same line - it does not sync,
  it does not stop the others. The device page shows `dc` in the EtherCAT
  state when the clock is running.
- **The device below the runtime.** A cycle under a millisecond needs a
  network port wired straight to the processor (not a USB adapter), a
  real-time kernel and a core kept free for the bus. On a Raspberry Pi
  the editor does this for you: the *Real-time kernel for EtherCAT* tick
  in the device's *Operating system* section
  ([Setting up a Linux device](/docs/hardware/linux-setup/#the-operating-system-from-the-editor))
  installs the `-rt` kernel image the distribution ships, extends the
  kernel line with `isolcpus`, `nohz_full`, `rcu_nocbs` and `irqaffinity`
  so that the last core is the bus's alone, and gives the runtime the
  drop-in that pins its cycle thread to that core; the interrupt mover
  installed with the runtime brings the port's interrupts along once the
  link is up. Measured with an i550 on the reTerminal's own port: 250 µs and
  200 µs run without a lost frame and the worst wake-up lateness stays
  under 15 µs; over a USB adapter the same line carries 1 ms and loses
  frames at 250 µs. The EtherCAT state on the device page carries the
  worst wake-up lateness of the last minute in microseconds - keep it
  under a quarter of the cycle, or the drives will report
  synchronisation errors. Its two counters (lost frames, overruns) start
  once every device on the line is operational, so a start-up never
  reads as a fault.

The examples run the i550 at 4 ms without the clock; a servo line is
set up the same way with the two fields above.

## The vendor's tool reaches a drive through the device

A servo inverter is commissioned with its maker's tool (motor
identification, the control loops, an oscilloscope), and many of them
have no service port: the tool reaches the drive by IP over **EoE**,
Ethernet over EtherCAT, with the EtherCAT master as the gateway. A Linux
device is that gateway. Give a slave an *EoE address* in its window (an
IPv4 address on a subnet of its own, say `192.168.100.11`) and, on the
EtherCAT page, the *EoE gateway* - this device's address on that subnet
(empty = the `.1`). The runtime then raises an interface `ecat0` with the
gateway address, hands every drive its address at start-up, and carries
the frames between the PC and the drives in the cycle's spare time - the
line's own frames come first, an engineering session costs it nothing it
can measure.

Two things on the network side, once per device: IP forwarding on the
Linux device (`net.ipv4.ip_forward = 1` in a file under
`/etc/sysctl.d/`), and a route on the engineering PC to the drives'
subnet through the device (on Windows, as administrator:
`route add 192.168.100.0 mask 255.255.255.0 <the device's LAN address>`).
The tool then adds each drive by its EoE address, and the drives answer
a `ping` the same way. The address is the engineering window only; the
parameters a line runs on come from the project at every start.

---

*EtherCAT® is a registered trademark and patented technology, licensed by Beckhoff Automation GmbH, Germany.*
