---
image: img/vehicle-tree.webp
image_alt: "The devices tree of a vehicle project: under the CAN bus sits J1939 with our node, the engine ECU and its parameter groups"
---

# Vehicle buses (J1939)

A vehicle bus is CAN with a different set of manners. Nothing is
addressed to anybody in particular: every control unit broadcasts what
it measures, over and over, and whoever needs a value simply listens.
The identifier of a frame is not a register number — it carries the
**parameter group** the data belongs to and the **address of the unit
that sent it**.

That layer is **J1939**, and three worlds speak it:

| World | What it is called | What changes |
|:---|:---|:---|
| Trucks, buses, off-road equipment | **J1939** | nothing — this is the base |
| Boats | **NMEA 2000 compatible** | its own transport for long messages, its own parameter groups |
| Tractors and implements | **ISOBUS** | industry group 2 in the name, the implement's own parameter groups |

ctrl32 speaks all three, because underneath they are one layer. In the
devices tree the network's icon follows the **industry group** of the
panel's NAME: an engine for a vehicle, a tractor for ISOBUS (group 2), a
ship for a boat (group 4, marine) - set the group on the network's page
and the icon follows.

![The devices tree: under the CAN bus, J1939 with our node, the engine ECU with its parameter groups, and the diagnostics beside it](img/vehicle-tree.webp){: .sb-center}

---

## The wire and the bit rate

A vehicle bus is ordinary CAN: two wires, terminated at both ends,
every node at the same bit rate. **250 kbit/s** is the J1939 rate on
trucks, boats and agricultural equipment; **500 kbit/s** appears on
newer designs. There is no negotiation — at the wrong rate nothing
arrives at all.

On a Linux device the interface and its rate are set under *Online ›
Prepare a Linux device* (the device's buses); the project's CAN node
names the interface it uses, and the runtime brings it up itself.

## Adding the network

In the devices tree, right-click the **CAN** bus and choose **Add
J1939**. The network appears with a sensible address for our node, and
the tree takes this shape:

| Node | What it is |
|:---|:---|
| **J1939** | the network on this bus |
| **Our node** | the panel itself: its address and its NAME |
| **a control unit (SA n)** | a unit we listen to, at its source address |
| **PGN n** | one parameter group that unit broadcasts |
| **Diagnostics** | the same units, asked instead of overheard — see [Vehicle diagnostics](vehicle-diagnostics.md) |

---

## The panel is a node, not a listener

A device on a vehicle bus has a **NAME** — sixty-four bits that say what
it is: the function it performs, the industry it belongs to, the
manufacturer, a serial number. On power-up it asks for an **address**
and defends it: if another unit wants the same one, the **lower NAME
keeps it** and the loser either moves to an unused address or goes quiet.

ctrl32 does the whole of that by itself. You choose the address it
should ask for and the fields of its NAME; it claims, defends, and (when
you allow it) moves out of the way.

![The J1939 page: the address our node asks for, the NAME behind it, and the engine ECU with its parameter groups](img/vehicle-j1939.webp){: .sb-center}

!!! note "Why the address matters"
    On a vehicle bus the address is how other units know who sent a
    value — and who a request is for. 128 to 247 is the range for
    equipment like ours; 254 and 255 are not addresses at all and
    cannot be asked for.

**The fields on Our node's page:**

| Field | What it decides |
|:---|:---|
| **Address** | the address the panel asks for (128 to 247 for equipment like ours) |
| **May take another address** | leave it ticked: when a unit with a lower NAME wants the same number, the panel moves to an unused one instead of going quiet |
| **Function** | what the device is, from the standard's list — 25 is a display |
| **Industry group** | 1 on-highway, 2 agriculture (this is what makes a device ISOBUS), 4 marine |

The line under the fields shows the NAME as the bus compares it. The
industry group and the function are part of the NAME, so they also
decide who wins an address contest. A node that claims an address is
a participant on the bus, not an observer — on a vehicle that is not
yours, agree its address with whoever owns the other units.

**One bus carries one higher layer.** J1939 and CANopen may not share a
pair of wires: the identifier ranges do not collide but the load and the
bit rates do, and nobody wants to find that out on a vehicle. A Linux
device has four CAN interfaces, so the drive and the vehicle can each
have their own.

---

## Parameter groups, and where they come from

A **parameter group** (PGN) is a numbered message — "electronic engine
controller 1", "engine temperature", "wheel-based speed and distance" —
with its signals at fixed bit positions inside it. You never have to
invent one: pick it from the library the editor ships.

![The parameter group window: the shipped library on the left, the picked group with its signals, their bit positions and scaling on the right](img/vehicle-library.webp){: .sb-center}

The library carries the common groups of all three worlds — the engine,
the fuel, the vehicle speed, the fault-code message, the boats' engine
and tank and navigation groups, the tractor's hitches, power take-offs
and valves. Ticking a group makes **one variable per ticked signal**,
already scaled, in a single step you can undo.

On a control unit, **Add parameter group from the library…** opens the
window; untick the signals you do not need. Two groups as they come
out of the library:

| Group | Number | Signal | Scaling |
|:---|:---|:---|:---|
| **EEC1** (electronic engine controller 1) | 61444 | engine speed | 0.125 rpm per bit |
| | | driver's demand torque | 1 % per bit, offset −125 |
| **ET1** (engine temperature 1) | 65262 | coolant temperature | 1 °C per bit, offset −40 |

Nobody types a start bit or an offset. The common set of the library
includes EEC1, EEC2, ET1, EFL/P1 (fuel and oil pressures), LFE (fuel
rate), VEP1 (battery), CCVS (vehicle speed, brake switches), AMB
(ambient), IC1 (boost, intake), HOURS, LFC (fuel used), VD (distance),
EBC1 (brakes), ETC1 (transmission speeds and gear), TRF1 (transmission
oil), DD (fuel level) and DM1 (the fault lamps); the boats' and the
tractors' groups sit in their own lists.

The variables land in the project with their units and their scaling,
ready for a screen, a trend or an alarm. The library holds the
published definitions; **the unit's own document is the authority** —
a vendor may send a group at another rate, leave a signal at "not
available" for ever, or use a proprietary group instead.

Where the library does not reach, the vendor's own **DBC file** does:
the button one row down reads it and offers its messages in the same
window. The proprietary groups (61184, and 65280 upward) are exactly
where that happens.

!!! tip "Two kinds of group number"
    Some groups are addressed to one unit and some are broadcast to
    everybody — the number itself decides which, and the editor says so
    beside it. A broadcast group cannot be sent to a single unit; give
    it the address 255 and it goes to all.

---

## Long messages

Eight bytes is one frame. A parameter group longer than that travels in
pieces and is put back together — announced to everybody, or negotiated
with one unit that acknowledges each block. Either way ctrl32 delivers
the message **whole or not at all**: a missing piece never reaches your
variables as half a value.

On the boats the same job is done by a different transport, **Fast
Packet**, and nothing in a frame says which of the two a message uses —
only its number does. The library knows; a group you type in by hand has
a tick box that says it.

| | J1939 transport | Fast Packet |
|:---|:---|:---|
| Used by | trucks, tractors | boats |
| Length | up to 1785 bytes | 9 to 223 bytes |
| Announced | yes | no |
| Acknowledged | when sent to one unit | never |

!!! note "How long a message a panel can hold"
    A Linux device takes the full 1785 bytes. A panel keeps 512, which
    is more than every group in the library needs.

---

## Boats

**NMEA 2000 compatible** means exactly what it says: the same parameter
group numbers, the same transport, the same units — engine speed and
hours, fuel and water tanks, battery, heading, rudder, depth, speed
through water, position, course and speed over ground, wind,
temperature, humidity, pressure. What it does not mean is a
certification: that is a paid conformance process with the association
that owns the name, and we do not claim it.

---

## Tractors and implements

**ISOBUS** is J1939 with the agricultural half on top: the same
addresses, the same claim, and the industry group in the NAME set to
agriculture, which is how a tractor tells an implement from a gearbox.
The groups are the ones an implement works with — wheel-based and
ground-based speed and distance, the front and rear hitch, both power
take-offs, the lighting, the auxiliary valves.

!!! warning "What ISOBUS does not include here"
    The **Virtual Terminal** — the implement uploading its own screens
    to the tractor's terminal and running them there — is not part of
    this. It is a second visualisation system inside ours, and a farmer
    who hears "ISOBUS" usually means that terminal. Our screens are our
    own: the panel shows them, and the tractor's terminal shows its own.

---

## The fault lamps and the active fault code (DM1)

**DM1** (65226) is the group in which a unit broadcasts its active
faults, about once a second. Its first two bytes are the four lamps;
each lamp is a two-bit signal (0 off, 1 on, 3 not available):

| Signal | Start bit | Bits |
|:---|:---|:---|
| Protect lamp | 0 | 2 |
| Amber warning lamp | 2 | 2 |
| Red stop lamp | 4 | 2 |
| Malfunction indicator lamp | 6 | 2 |

The library carries the lamps. The **first fault code** follows in the
next four bytes and is added as plain signals of the same group:

| Signal | Start bit | Bits |
|:---|:---|:---|
| SPN, low byte | 16 | 8 |
| SPN, middle byte | 24 | 8 |
| FMI | 32 | 5 |
| SPN, high bits | 37 | 3 |
| Occurrence count | 40 | 7 |

The program joins the three parts: `spn := lo + mid * 256 + hi *
65536`. The SPN says **what** is wrong (110 is the coolant
temperature), the FMI **how** (0 is "above normal, most severe"). With
more than one fault active, DM1 grows past one frame and travels as a
long message; it still arrives whole, and the codes after the first
repeat in fours and are read by a program.

To show a code in words, set one boolean per code you know in the
program and put a label per word on the screen with `visible_if`.

## Telling a silent unit from a quiet one

A unit that stops sending leaves its variables at their last value —
the value does not drop to zero. To know a unit is alive, watch a
value it always changes (engine speed while the engine runs) with a
timer in the program: restart it on every change, and two seconds of
silence turns a lamp and an alarm on.

## When nothing arrives

| What you see | What it usually is |
|:---|:---|
| Nothing at all, on any group | the bit rate, a missing terminator, or the interface is not up |
| Nothing from one unit | that unit's address is not the one in the project (`SA`) |
| A value that never changes | the group arrives but the signal's bits are wrong — check start bit and width against the vendor's sheet |
| Numbers that look scaled wrong | gain and offset, in the units the sheet uses |
| The node never takes an address | another unit holds it with a lower NAME — tick *May take another address* |
| The CAN bus also carries a drive | one bus, one higher layer: move one of them to another interface |

---

## Where it runs

| Device | Vehicle buses |
|:---|:---|
| Linux devices | yes, on any of the four CAN interfaces |
| Boards with CAN | yes, on the one bus they have |
| Boards without a CAN transceiver | no bus to speak on |

What a project may hold: **4 networks** (one per CAN interface),
**32 control units**, **64 parameter groups** and **256 signals**. The
editor refuses more at your desk rather than on the vehicle.

---

## Asking a unit a question

Listening is one half. The other — asking a control unit for its fault
codes or for a value it does not broadcast — is
[vehicle diagnostics](vehicle-diagnostics.md), a separate part with its
own page.

!!! note "A vehicle bus is not a car's diagnostic port"
    J1939 is the bus of trucks, buses, agricultural and construction
    equipment, generator sets and boats. A passenger car speaks over
    its diagnostic connector, and that conversation is
    [vehicle diagnostics](vehicle-diagnostics.md), on a Linux device.

!!! warning "Safety"
    A vehicle bus is not a safety function. Nothing on it replaces a
    hard-wired stop, and reading a value does not make it true a second
    later. Treat what arrives as information for the operator and for
    your logic, not as protection.
