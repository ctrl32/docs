---
title: OPC UA server
source: docs/tutorial-opcua.md
hero: img/opcua-page.webp
---

# Every variable on OPC UA, without a line of mapping

A ctrl32 Linux device serves every variable of its project over OPC UA under its own name - add one node in the tree, deploy, and any OPC UA client reads and writes it.

## Who it is for
- SCADA and MES integrators who need data from the shop floor
- Engineers tired of mapping the same variable twice
- Sites with their own certificate policy

## What you get
- An OPC UA server switched on by adding one node under Ethernet
- Every project variable served automatically, node id = the variable's own name
- Renaming in the project renames on the server - nothing to keep in sync
- Writes from a client on read/write variables, taking the same road as a screen button
- Device certificates applied to the running device: self-signed, own PEM/DER files, or no encryption
- The certificate belongs to the device, not the project - two devices with one project keep separate identities
- The other direction too: *Import variables from a server* brings another OPC UA server's variables into the project
- Tested on every release by the test wall

## How it works
1. Under the device's Ethernet in the tree, add OPC UA.
2. Deploy - the server runs on port 4840 from then on.
3. Point any OPC UA client at `opc.tcp://<address>:4840` and open Objects > ctrl32.
4. Read a value with a click, or address it directly as `ns=1;s=<variable name>`.
5. Write setpoints marked read/write; actual values stay the program's.
6. Before the device leaves the desk: in Device certificate type its address, pick a mode, press *Apply to device*.

## Pictures
- ![The OPC UA page: the server, its port and what it serves](img/opcua-page.webp) - one node turns the server on
- ![The project's variables: every one of them is a node on the server, under its own name](img/opcua-vars.webp) - nothing to map
- ![The certificate section: the address of the running device, the three modes and Apply to device](img/opcua-cert.webp) - security on the running device

## Runs on
- A Linux device running a project - e.g. the reTerminal; the test wall also checks the DK2
- Any OPC UA client (a browser client is enough for checking)

## Facts to keep exact
- Port 4840; endpoint `opc.tcp://<address>:4840`
- All variables under one folder named `ctrl32`; node id example `ns=1;s=z_temp_a`
- Bench: the reTerminal serves 46 variables - zone temperatures, drive values, the device's own sensors and the system variables
- A client write on a read/write variable: the program owns the variable again on its next cycle; a client writing an actual value is overwritten immediately
- Certificate modes: Self-signed (generated on the device, normal choice, client trusts it once); Own certificate (PEM/DER files, for sites issuing certificates centrally); No encryption (plain endpoint only, for an isolated network behind a panel and a switch nobody else reaches)
- Apply to device: the runtime stores it and restarts; the page shows what it answered
- Test wall, every release: connects to the reTerminal and the DK2 over OPC UA, reads a temperature, writes a setpoint, reads it back and restores it
- Troubleshooting: deploy first (the server starts with the project that declares it); port 4840 must be reachable; a host-name connection needs the device's name, the address always works; a device serves the project it runs, not the one open in the editor

## Call to action
Download the editor, prepare a Linux device and add OPC UA under its Ethernet.
