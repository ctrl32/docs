# net32 — sharing variables between devices

**net32** (network variables) connects ctrl32 devices to each other.
One device measures a temperature; another shows it on its screen and
writes the setpoint back. No PLC in the middle, no register maps, no
polling tables — you name the variables and the devices keep them in
step over WiFi, ethernet or CAN.

The design follows one rule: **every shared variable has exactly one
owner.** The owner measures or computes the value; every other device
subscribes to it. Writes go the other way as *commands* to the owner —
the local copy never pretends, it only ever shows the owner's state.

## What it feels like

- On the **owner**, a shared variable is an ordinary local variable
  with a *published* checkbox — publishing changes nothing about how
  the device itself uses it.
- On a **subscriber**, the variable names its source: the owner's
  node number and the variable's name there. It lands in the variable
  table like any Modbus or +7 value and everything downstream
  (screens, logic, alarms, trends, WEBview) treats it normally.
- A setpoint field or a switch bound to a subscribed variable writes
  **to the owner**. The new value appears when the owner confirms it —
  the same honest behaviour WEBview and MQTT writes have always had.

## The link is honest

Networks drop out. net32 is built so a dropout is *visible* and never
*dangerous*:

- Every subscription carries freshness. When the owner falls silent
  past the stale timeout, the last good value stays readable but the
  peer's **health variable** drops to 0 — a `bool` you bind on the
  net32 page and use in logic and on screens (dark lamps, a red
  banner, heaters off).
- Writes toward a silent peer are refused on the spot, never queued —
  a command from ten minutes ago must not fire when the link heals.
- Each device fingerprints its published list. A device hearing a
  layout it does not expect — half the pair updated, half not — marks
  those variables **bad** instead of reading garbage, and says so in
  the diagnostic buffer. Update the second device and everything
  heals by itself.
- Local logic runs on local variables. A device that loses the
  network keeps controlling whatever it owns.

## Transports

| Transport | Where | Notes |
|:---|:---|:---:|
| **UDP** (WiFi / ethernet) | every ctrl32 device | on by default |
| **CAN** | devices with a CAN bus | no network stack needed, coexists with CANopen |

Values travel on change (the variable's deadband applies) plus a
periodic refresh, roughly once a second. On WiFi, where access
points commonly filter multicast, add the peer's address to the
**Peer addresses** list — devices also learn each other's addresses
from what they hear, so one fixed address per pair is enough.

## Setting it up

1. Right-click the **Ethernet** or **WiFi** interface in the device
   tree and pick **Add net32 (network variables)…**
2. Give the device its **node number** (1–254, unique) and a
   **system** number — devices only hear their own system, so two
   installations next to each other stay separate.
3. Tick **published** on the variables this device owns and shares.
5. *Download to board.* net32 is part of the pack — adding a variable
   or a peer never needs new firmware.

Limits: 64 published and 64 subscribed variables per device, 32 peer
addresses. Everything over a limit — and every inconsistency, like
subscribing to a name the remote list does not carry — is refused
when the project builds, with the reason spelled out.

## Good to know

- The remote list you paste is the contract: both sides carry it, and
  the fingerprint computed from it is what protects a half-updated
  pair. When you add a published variable on the owner, update the
  subscriber's remote list too — until then the subscriber shows
  *bad* instead of guessing.
- Shared variables are 32-bit values (bool, integers, real). Strings
  stay local.
- net32 shares variables between **ctrl32 devices**. To talk to a
  foreign PLC use [Modbus](modbus.md) or [+7](plus7.md); to feed a
  SCADA or a home dashboard use MQTT or the OPC UA server.
- Stopping equipment over the network is **not a safety function**.
  E-stop stays hard-wired.
