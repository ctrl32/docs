---
title: "Network and security"
slug: security
section: "About"
order: 344
sidebar_position: 344
generator: tools/docs_export.py
---

# Network and security

The short version: **a board belongs on its own network, behind
something.** It has no TLS, no login, and it is not built to survive
being reachable from the internet.

This page collects what is true about that, in one place, so nobody has
to assemble it from five others.

---

## What protection exists

| | |
|:---|:---|
| **WiFi** | WPA2 password, if it joins a network or makes its own access point |
| **Network upload** | can be switched off per project |
| **Writes from a browser** | are commands the board may refuse, not direct writes into memory |
| **Packs** | are checksummed and refused if they do not match the board |

## What does not

| | |
|:---|:---|
| **TLS / HTTPS** | none. Traffic is plain HTTP and plain WebSocket. |
| **A login** | none. Whoever reaches the board can see its screens. |
| **Access control on variables** | none per user — the project decides what is writable, not who is asking. |
| **Modbus authentication** | none. Modbus has no such concept, on any device. |

None of that is an oversight. TLS on an ESP32-S3 with a couple of viewers
eats the RAM its own work needs, and a certificate on a device
nobody maintains expires and turns into a warning screen everybody learns
to click past. Rather than pretend, ctrl32 says plainly what it is: a
device for a network you control.

---

## Where a board belongs

**On its own segment.** A separate VLAN, a separate switch, or at the
very least not the same network as the office printers. Everything the
board talks to — I/O modules, drives, meters — belongs there with it.

**Behind a firewall from everything else.** The board should be reachable
from the projects and people that need it, and from nothing else.

**Never port-forwarded.** If somebody needs to see it from outside, the
answer is a **VPN into the network**, not a hole in the router pointed at
the board. A VPN is one thing to maintain and it protects everything
behind it; a port forward is a permanent invitation.

!!! danger "This is not a device to put on the internet"
    No TLS, no login, and firmware that is built for reliability on a
    quiet network rather than for hostility on an open one. A board with
    a public address is a board somebody else can drive.

---

## Its own access point

A board with WiFi can make its own network instead of joining one. That
is often the most secure option available, and the most convenient:

- nothing else is on it
- it reaches as far as the radio does and no further
- there is no infrastructure to configure, argue about or wait for

**Set a password on it.** An open access point is a network anybody in
the car park can join. The project carries the AP credentials, so this is
one field, once.

---

## Turning off what you do not need

**Network upload** can be disabled per project (`network: { upload:
false }`, or the checkbox in the WEBview settings). With it off, new
screens and logic can only arrive over the cable.

Worth doing for anything left running unattended: it removes the one
network path that can change what the board does, while leaving the
WEBview working for people who need to look at it.

---

## What a browser can do

A WEBview viewer can see every screen in the project and write whatever
those screens allow. There is no per-user permission model.

**So put nothing on a WEBview screen that you would not hand to anybody
on that network.** If a setpoint should only be changed by one person,
the network is what protects it, not the screen.

The writes themselves are **commands** — the board decides whether to
accept one, so the logic can refuse a change while the equipment is in the
wrong state. That is a safeguard against mistakes and timing, not against
somebody who should not be there.

---

## Fieldbuses

**Modbus has no security at all**, by design and on every device that
speaks it. Anybody on the wire can read and write anything the slave
exposes. Modbus TCP puts that on a network, which is why the network
matters more than the protocol.

**CANopen** likewise: a device on the bus is trusted because it is on the
bus.

The mitigation for both is physical and topological — who can reach the
wire, and what else is on it.

---

## Keeping the board current

Firmware updates arrive as a runtime you flash from the editor, and packs
as an upload. Neither happens by itself: nothing on the board calls out,
downloads anything, or changes without somebody deciding.

That means no surprise updates — and it means keeping track yourself of
what is running where.

---

## A checklist worth keeping

- [ ] The board is on a segment with only what it needs to talk to
- [ ] No port forwarding, no public address
- [ ] Remote access, where needed, is a VPN
- [ ] WiFi — its own or joined — has a password
- [ ] Network upload is off where nobody should be changing it
- [ ] Nothing on a WEBview screen you would not hand to that network
- [ ] Safety functions are hard-wired and independent of all of this

The last one is not a network matter and it is the one that counts. See
[Intended use](/docs/about/intended-use/).
