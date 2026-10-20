---
title: Vehicle bus J1939
source: docs/tutorial-vehicle.md
hero: img/veh-screen.webp
---

# Listen to the engine, ask it for its faults

Put an engine's J1939 broadcasts on a screen and read its fault codes with a button - parameter groups from a library, scaling already done, diagnostics in one block.

## Who it is for
- Builders of displays for trucks, agricultural and marine equipment
- Service teams who need fault codes recorded with a timestamp
- Integrators adding a panel to an existing vehicle network

## What you get
- J1939 added to a CAN bus with one right-click; our node with a sensible address
- A NAME editor (function, industry group) and address claiming with *May take another address*
- A library of parameter groups with bit positions and scaling - nobody types an offset
- DBC import for vendor-specific groups
- Each ticked signal becomes a variable with unit and scaling, ready for a screen, trend or alarm
- A listen-only mode that puts not one bit on the wire
- Diagnostics: tester identifier pair, session, keep-alive, periodic value rows that arrive without a program
- `UDS_DTC` block reading fault codes on a button; every code goes into the diagnostic buffer with its time

## How it works
1. Set the CAN interface and bit rate in Online > Prepare a Linux device; on a foreign vehicle start in listen-only.
2. Right-click the CAN bus > Add J1939.
3. On Our node set the address and the NAME.
4. On the control unit press *Add parameter group from the library...* and pick EEC1 and ET1.
5. Deploy and check the values move.
6. Right-click CAN > Add diagnostics; set the identifier pair, session and value rows.
7. One rung: the `read_faults` button into `UDS_DTC`, with `Done` and `Error` lamps on the screen.

## Pictures
- ![The finished screen: what the engine broadcasts, what it answers when asked, and the button that reads the faults](img/veh-screen.webp) - both halves on one screen
- ![The tree: under the CAN bus, J1939 with our node and the engine, and the diagnostics beside them](img/veh-tree.webp) - the shape you work in
- ![The J1939 page: the address our node asks for, the NAME behind it, and the engine's parameter groups](img/veh-network.webp) - who the panel is on the bus
- ![The library: the groups on the left, and the picked one with its signals, bit positions and scaling](img/veh-group.webp) - scaling comes with the group
- ![The variables the two groups made, with their units, deadbands and comments](img/veh-variables.webp) - ready for screens, trends, alarms
- ![The diagnostics page: the tester pair, the fault variables and the values read over and over](img/veh-diagnostics.webp) - asking instead of overhearing
- ![The rung: the button, the UDS_DTC block and its two answers](img/veh-rung.webp) - fault codes on one rung

## Runs on
- A Linux device with a CAN interface: the reTerminal with its E10-1 expansion (in the pictures)
- The listening half works on any board with CAN; the asking half (diagnostics) needs the Linux runtime
- Any J1939 engine control unit - the numbers are the standard's, not one vendor's

## Facts to keep exact
- Project: `tutorials\vehicle_bus.prj32`
- 250 kbit/s on trucks, also marine and agricultural; 500 kbit/s on newer designs; no negotiation - wrong rate, nothing arrives
- The runtime brings the interface up itself
- One bus, one higher layer: J1939 and CANopen cannot share an interface; the editor will not offer both, the build refuses it; a Linux device has four CAN interfaces
- Tree: J1939 > Our node > engine (SA 0) > PGN 61444 EEC1; Diagnostics beside
- Address range for equipment like ours: 128 to 247; the lower NAME keeps the address
- NAME is 64 bits; Function 25 = display; Industry group 1 on-highway, 2 agriculture (makes it ISOBUS), 4 marine
- EEC1 = PGN 61444: engine speed 0.125 rpm per bit, driver's demand in percent, sent every few dozen milliseconds
- ET1 = PGN 65262: coolant temperature, one degree per bit minus forty
- Proprietary groups: 61184 and 65280 upward (DBC files)
- Diagnostics identifiers: ask on `0x7E0`, answer on `0x7E8` (usual engine pair); session `0` default, `3` extended; keep-alive a couple of seconds
- Engine speed is read twice on purpose (broadcast and asked) to expose a stale or differently-meant value
- `UDS_DTC` asks on the rising edge; `ECU` 0 = first unit on the Diagnostics node; `Done` = answered, `Error` = refused, silent, or no diagnostics on this device
- A refusal (e.g. clearing faults while the engine runs) is an answer - show it, do not retry in a loop
- Fault-finding table: nothing at all = bit rate or terminator; nothing from one unit = wrong SA; value never changes = start bit/width; wrong scale = gain/offset
- Related blocks: `UDS_DTC`, `UDS_CLEAR`, `UDS_READ`

## Call to action
Download the editor and open `tutorials\vehicle_bus.prj32`.
