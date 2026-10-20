---
title: reTerminal as SIMATIC panel
source: docs/example-reterminal-s7.md
hero: img/rt-s7.webp
---

# Turn a reTerminal into the operator panel of your SIMATIC - no mapping table

The PLC is a SIMATIC S7-1200 on the same ethernet, the reTerminal reads a data block live, writes one value back and watches the PLC's own clock bit to know the controller is alive.

## Who it is for
- Plants with an S7-1200 or S7-1500 that need an operator panel
- Integrators who do not want to keep a tag list in step on two sides
- Service engineers who want to see at a glance which side stopped

## What you get
- A data block read live: a REAL, a DINT, a second REAL and two bits out of `DB120`, each with the PLC's address printed beside it
- One value written back: `DB120.DBW4`, an INT the operator types
- The markers: a REAL at `%MD10` and `%M0.5`, a bit of the controller's clock byte, as a blinking alive lamp
- The panel's own life counter beside the PLC's values - when the counter moves and the PLC values freeze, the fault is on the network
- No mapping table: a variable names the area, the block and the offset - that is the whole configuration
- An alarm when the PLC stops

## How it works
1. No fieldbus at all: the reTerminal and the S7 share the ethernet.
2. Each variable names the PLC area, block and offset; the screen reads them directly.
3. A write is a command, not a force: the PLC owns the value again on its next scan.
4. The link lamp and the clock-bit lamp together prove the PLC is in RUN and the link is alive.

## Pictures
- ![The PLC screen with the controller answering: the data block read live with its own addresses beside the values, the INT written back, the marker word and both lamps lit](img/rt-s7.webp) - The PLC screen with the controller answering

## Runs on
- Seeed reTerminal (CM4)
- SIMATIC S7-1200 or S7-1500 reachable on the network, with PUT/GET allowed in its protection settings
- Without a PLC the screens run and the link lamp stays dark

## Facts to keep exact
- Data block `DB120`: a REAL, a DINT, a second REAL, two bits; label example `DB120.DBD0`
- Written value: `DB120.DBW4` (INT)
- Markers: REAL at `%MD10`; `%M0.5` = a bit of the controller's clock byte
- PUT/GET must be allowed in the PLC; an S7-1200 refuses the connection until it is, and the refusal looks like a network fault - check it first
- Stopping the PLC: link lamp goes out, alarm arrives after three seconds, the panel's counter keeps running
- Try: type a value into `DB120.DBW4` and watch it in the PLC's monitoring table; add a variable of your own (area, block, offset)
- The same reTerminal project family runs on four buses: CANopen, EtherCAT, an RS-485 pair, a SIMATIC over ethernet

## Call to action
Download the ctrl32 editor and open the shipped project `examples\reterminal_s7_example.prj32`.
