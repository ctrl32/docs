---
title: Two boards over Modbus
source: docs/tutorial-modbus-pair.md
hero: img/modbus-slave-map.png
---

# A process board and an operator panel, joined by nothing but Modbus TCP

One board measures three PT100 temperatures and switches three heaters; the other shows the temperatures and takes the commands. A complete, working pair you can open side by side and copy.

## Who it is for
- Integrators splitting a system into a field board and an operator panel
- Anyone who needs a robust Modbus TCP master/slave design that survives a WiFi dropout
- PLC programmers who want to compare ladder, ST and FBD on the same logic

## What you get
- Two real bench projects: a Modbus **slave** at the process and a Modbus **master** at the operator
- The design worth copying: **the board at the process owns its outputs, the panel only requests and displays** - the slave's interlock refuses to heat a zone whose probe reads like a broken one, whatever the master asks
- A register map that enforces ownership: only the commands are writable, the real outputs are exposed read-only right after them so the master compares "what I asked" with "what is happening"
- The editor's *Modbus TCP slave* page shows the map as the integrator on the other side reads it, in both address notations
- The same interlock in three languages - ladder, ST and FBD - compiling to the same bytecode
- A master that is **pure HMI with no program at all**: write-through variables push a switch change to the slave instantly, the cyclic read brings the truth back
- Three alarms with a 3-second delay report a failed probe to both screens
- WEBview on both boards: any phone sees what the master sees - "is it the slave or the link?" becomes a thirty-second question

## How it works
1. Download the slave project over USB first - it carries the WiFi credentials; it joins the network as a station.
2. Find it with the device scanner: it answers on its COM port and from its WiFi address, with its program name.
3. Reserve that IP on the router (DHCP reservation) and make sure the master's `ip:` fields name it.
4. Download the master over Ethernet or USB - temperatures appear on the glass within a second or two.
5. Prove the interlock: flip a Command switch, the Output LED follows and the SSR clicks; pull the PT100 and the alarm fires after three seconds, the output drops, the switch stays where it was - with a dark LED telling the truth.

## Pictures
- ![The slave map page: temperatures in holding 0-5, commands in coils 0-2 writable, real outputs in coils 3-5 read-only](img/modbus-slave-map.png) - the slave's register map in the editor
- ![The slave program in ladder: per zone, a GT compare writes ok_x, then two series contacts - the command and the interlock - drive the heat coil](img/modbus-pair-lad.png) - the interlock in ladder
- ![The same interlock in Structured Text: ok_a := temp_a > 2.0; heat_a := cmd_a AND ok_a; - twice more for B and C](img/modbus-pair-st.png) - the same interlock in ST
- ![The same interlock in FBD: GT into AND per zone, wired through the ok variables](img/modbus-pair-fbd.png) - the same interlock in FBD
- ![The master's screen in the editor: three zone cards, each with the temperature, a command switch and an output LED](img/modbus-pair-screen.png) - the master's operator screen
- ![The scanner during the pair bring-up: the TM8.6 answering from 192.168.0.233 with its program name, the F7 from 192.168.0.225](img/find-devices-scan.png) - the device scanner finding both boards

## Runs on
- At the process: **inoCORE32-TM8.6**, WiFi, Modbus slave - `tm8_6_modbus_slave.prj32`
- At the operator: **STM32F746-DISCO**, Ethernet, Modbus master - `f7_modbus_master.prj32`
- Protocol: Modbus TCP

## Facts to keep exact
- Files installed in `examples\modbus_pair`; plus `slave_logic_ld.prj32`, `slave_logic_st.prj32`, `slave_logic_fbd.prj32` with identical variables, one language each
- Slave: twelve variables in three groups - temperatures `temp_a/b/c` (f32 °C, 1 decimal, deadband 0.1, from MAX31865 drivers), commands `cmd_a/b/c` (bool rw), interlocks `ok_a/b/c`, outputs `heat_a/b/c` on GPIO pins 7, 8, 19 (SSR relays)
- Modbus slave: TCP, port 502, unit 1, word order big; nine variables exposed; addresses in list order, `bool` = coil, others = holding register, `f32` takes two
- Map: temp_a holding 0-1 (40001), temp_b 2-3 (40003), temp_c 4-5 (40005); cmd_a/b/c coils 0-2 writable; heat_a/b/c coils 3-5 read-only (the real output state)
- A master writing anywhere not writable gets exception 03
- Interlock: output follows the command only while the probe reads above 2 °C (a loose or broken PT100 reads far below zero); ST `ok_a := temp_a > 2.0; heat_a := cmd_a AND ok_a;`
- Ladder: six rungs, two per zone (GT compare into `ok_x`, then `cmd_x AND ok_x` into `heat_x`)
- Ladder and FBD compile through the same path as ST, into the same bytecode
- Slave network `mode: sta`, address from DHCP - give it a DHCP reservation; bench address `192.168.0.233` (F7 at `192.168.0.225`)
- Master: f32 = two holding registers each, `word_order` must match the slave (big on both ends); a variable that is `access: rw` and has a Modbus source is write-through (a coil write for a bool); master's `heat_a` is display-only of coil 3
- Master screen: three zone cards - temperature, *Command* switch bound to `cmd_x`, *Output* LED bound to `heat_x`; a WEBview copy serves phones
- Troubleshooting points: nonsense values = word order mismatch; values shifted by one = an address from a 1-based manual (the map is 0-based); stops after a router restart = DHCP reservation skipped

## Call to action
Download the editor and open `tm8_6_modbus_slave.prj32` and `f7_modbus_master.prj32` from `examples\modbus_pair` side by side.
