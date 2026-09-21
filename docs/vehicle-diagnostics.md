---
image: img/vehicle-diag.webp
image_alt: "The diagnostics page: a control unit with its request and answer identifiers, the fault-code variables and the values read over and over"
---

# Vehicle diagnostics

Some things a control unit never broadcasts. Its fault codes, the
readings behind a warning lamp, the serial number of the part somebody
fitted last winter — those are **answers**, and you only get them by
asking.

That conversation is what a workshop tester has with a vehicle, and
ctrl32 can hold it too: it asks, the unit answers, and what comes back
lands in your variables like any other value.

![The diagnostics page: the control unit, its request and answer identifiers, the fault-code variables and the values read over and over](img/vehicle-diag.webp){: .sb-center}

---

## What it needs

**A Linux device.** The transport under the questions — the part that
cuts a long answer into frames and puts it back together — is built
into the Linux kernel, and that is where this runs. On a panel the
diagnostics blocks report an error instead, which is the honest answer
to "read the faults" on equipment that cannot ask.

**A pair of identifiers.** A tester asks on one and the unit answers on
another: **0x7E0 and 0x7E8** is the usual pair, and a unit's own
document names its own. They must differ, and two units on one bus
cannot ask with the same one.

**A bus of its own.** As with the vehicle network itself, a bus that
carries CANopen cannot carry this — a tester's identifiers sit exactly
where CANopen puts its higher node numbers.

---

## Setting one up

In the devices tree, under a CAN bus, add **Diagnostics** and then a
control unit. Under the unit live the **values** you want read.

![The tree: Diagnostics under the CAN bus, the control unit with its identifier, and the values read out of it](img/vehicle-tree.webp){: .sb-center}

A value is one row:

| Field | What it is |
|:---|:---|
| **identifier** | the number the unit's document gives for that value |
| **byte**, **bytes** | which part of the answer, and how wide (1 to 4 bytes) |
| **signed**, **gain**, **offset** | how to turn it into the number a person reads |
| **Period ms** | how often to ask; 0 = only when a program asks |
| **Variable** | where it lands |

Rows with a period **arrive on their own**. No program is needed for
them: set the period, put the variable on a screen, and the value is
there — the same as a Modbus register or a signal off the vehicle bus.

A project may hold **8 control units** and **64 values** in all.

---

## Fault codes

A fault code is not a number a unit publishes; it is a list you ask for.
When it arrives:

- the **count** and the **first codes** go into the variables named on
  the page, so a screen can show them and an alarm can watch them;
- **every** code also goes into the **diagnostic buffer** with the time
  it was read — that is the record a service engineer reads afterwards,
  the same buffer the rest of the runtime writes to.

---

## What a person starts

Reading the faults and clearing them are not things that should happen
every second — they happen when somebody presses a button. That is what
the three blocks are for:

| Block | What it does |
|:---|:---|
| `UDS_DTC` | read the fault codes |
| `UDS_CLEAR` | clear them |
| `UDS_READ` | ask for one value now, without waiting for its period |

They work like the other service blocks: a rising edge sends the
request, `Done` says it was answered, `Error` says it was refused, went
unanswered, or there are no diagnostics on this device. The pin tables
and the ST examples are on the
[service blocks page](blocks-services.md).

!!! note "One question at a time"
    A control unit answers one question at a time — that is what the
    protocol allows. A block pressed while another question to the same
    unit is still in hand reports `Error`; press again when it is free.

!!! tip "A refusal is an answer"
    A unit may refuse to clear its faults while the engine runs, or
    refuse a value in the session it is in. `Error` then means exactly
    that, and the program should say so rather than retry — the answer
    will not change while the conditions do not.

---

## Session and keep-alive

Most values answer straight away. Some live behind an **extended
session** — the unit has to be asked to open it first, and it closes
again when nobody speaks for a while. Both are fields on the page: the
session to open at start-up, and how often to say "still here" so it
stays open.

Leave both at zero and the unit is asked in its default session, which
is what most readings need.

---

## What this is not

- **It is not a tester.** Coding, programming, adaptations, guided
  functions — the vendor's own tool does those, and should.
- **It is not a server.** Our device asks; it never answers a tester's
  questions about itself.
- **It is not a safety function.** A fault code read a second ago is
  history, not a guarantee.
