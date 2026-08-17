# Editor

ctrl32 Editor is an **installed application**, not a web page. The reason is
simple: it draws exactly the pixels you will see on the panel — the same
renderer as in the firmware is built into it, fonts, roundings and colours
included. What you see is what gets downloaded.

## Layout

| Part | Where | What is in it |
|---|---|---|
| **Menu** | top | File, Edit, View, Project, Build, Online, Debug, Tools, Window, Help |
| **Toolbar** | under the menu | new, save, undo/redo, TEST, ONLINE, download |
| **Project tree** | left | the board and everything running on it |
| **Documents** | centre | every tree node has a **page**, opened as a tab |
| **Status bar** | bottom | the result of the last build, the connection state |

The **bug icon at the top right** opens mail to `bugs@ctrl32.com` —
reporting a fault should be one click from wherever you hit it.

## The tree follows the hardware, not the protocols

```
project
  board
    Application          programs, variables, visualizations, axes
    CAN                  the bus itself: bitrate, termination
      Raw CAN            frame-to-tag mapping
      CANopen master     + devices
    RS485                the line: baud, parity, stop bits
      Modbus RTU master  + devices
      Modbus RTU slave   the panel as a slave
    Ethernet             DHCP/static IP, mDNS
      Modbus TCP         master and slave
      MQTT               telemetry / Home Assistant
    I2C, SPI             local buses and chips
    Settings
```

One wire can carry several protocols, and the same protocol can run on two
wires (Modbus on RS485 **and** on Ethernet). Sorting by protocol could not
express that; this way matches both the hardware and CoDeSys.

!!! note "Settings live on pages, not in the right-click menu"
    A context menu holds **actions** — add, delete, rename. Never settings.
    The bus speed is on the bus page, where a person looks for it. A popup
    is only for **picking from a catalog** (boards, devices, dictionary
    objects).

Nodes for features that are not finished yet are in the tree as well — their
page says so. A customer has to see what the panel can have, not guess it.

## Toolbar

| Icon | What it does |
|---|---|
| ⊞ | new project |
| 💾 | save project |
| ↶ ↷ | undo / redo (both unlimited; the count is in the Edit menu) |
| ▶ / ■ | **TEST** — simulation inside the editor, without a panel |
| ⏸ ⏭ | pause and single-cycle step (during a test) |
| 🔌 | **ONLINE** — connect to a real panel |
| **⭳** | **download to the panel** (F5) — the only coloured icon in the bar |

There is deliberately only one blue icon. Downloading into a machine is an
action that must not be confused with any other; everything else is a flat
icon like in any ordinary application.

## TEST — simulation without a panel

The ▶ button switches the editor into running: the PLC cycle runs on the PC,
screens react, blocks compute, tags change. It can be paused and stepped
cycle by cycle (*Debug → Step*).

What runs is **the same bytecode and the same block library** as in the
panel — the VM is compiled for the PC as well. So logic can be debugged at
your desk and reach the machine finished.

The difference from [online monitoring](online.md): TEST computes the
values, ONLINE **reads them from the machine**.

## Build (F7) and download (F5)

**F7** only builds the project and reports the result. **F5** builds and
downloads it.

When a build fails, a window opens with the **whole** output — the text can
be selected and copied with a button, and the same text is in
`build\last_build_error.txt`. A truncated line in the status bar was never
enough for anyone to help you with.

## Language and theme

*View → Language* and *View → Dark theme*. The choice is remembered between
runs.

## Licence

- **talking to a real panel** — download and online alike — is paid.

## Updates

*Help → Check for updates* looks at our web and tells you whether a newer
version exists. Downloading is manual — the editor never updates itself
behind your back, because the editor version is tied to what is running in
customers' panels.
