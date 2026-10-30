---
title: "The project file"
slug: project-format
section: "Editor"
order: 15
sidebar_position: 15
generator: tools/docs_export.py
---

# The project file

A ctrl32 project is a **single YAML file**. Text, readable, declarative —
you can open it in any editor, read it without the tool that made it, and
put it in version control like source code.

That is not an implementation detail that leaked out. It is a deliberate
choice, and it gives you things a binary project format cannot.

---

## Why it matters

**You can diff it.** Two versions of a project, side by side, showing
exactly what changed: this setpoint, that rung, this screen. Ask anybody
who has tried to answer "what changed since Tuesday?" in a binary
engineering tool what that is worth.

**You can put it in git.** Branches for a variant, variables for what was
delivered, a history of who changed what and when. A project from two
years ago is a checkout away.

**You can review it.** A change to the logic is a change worth
reading before it is uploaded, and a text diff is something a second
person can actually read.

**You can generate it.** Twenty near-identical variants of one
installation are a script, not twenty afternoons of clicking.

**It outlives the tool.** Even with no ctrl32 installed, the file still
says what it does. Nothing about your work is locked inside a
format only one program understands.

---

## What is in it

The sections, in the order they usually appear:

| Section | Holds |
|:---|:---|
| `project` | name, target board, resolution, orientation — how the picture sits on the glass as it is mounted: `as_mounted`, `rot90`, `rot180`, `rot270` (the older `landscape` / `portrait` / `portrait_flipped` still read) |
| `themes` | colour sets the styles resolve against |
| `states` | reusable three-state colour sets |
| `tags` | every variable: type, unit, scaling, deadband, source |
| `pous` | program units — ladder, FBD or ST |
| `logic` | the blocks and how they are wired |
| `screen_tag` | the number variable whose change opens a screen - the program writes the screen's index |
| `alarms` | condition, limit, hysteresis, delay, priority, text |
| `icons` | which glyphs the project uses |
| `screens` | the board's own screens and their widgets |
| `web_screens` | the browser's screens |
| `assets` | fonts and images |

Peripherals, buses and services appear under their own keys as the
project uses them — `can_devices`, for example, holds the CANopen
devices and the PDO mapping that says which of their objects travel
each cycle.

One naming note: what the editor calls a *variable* is written in the
file under the key `tag` (and the section `tags:`) — the historical
name of a variable reference, kept because the meaning of an existing
key never changes. Widgets point at variables the same way:
`tag: temp`.

Everything is optional except `project`. A file with a `project` section
and nothing else is a valid, empty project.

---

## What it looks like

```yaml
project:
  name: thermostat
  target: olimex_esp32_evb
  resolution: [240, 320]   # the 2.8" module as mounted

tags:
  - { name: temp,    datatype: f32, unit: "°C", decimals: 1,
      deadband: 0.2 }
  - { name: setpoint, datatype: f32, unit: "°C", decimals: 1,
      init: 21, access: rw }
  - { name: heating,  datatype: bool, access: rw,
      source: { gpio: { pin: 32 } } }

logic:
  - { type: HYST, name: thermo, in: { IN: temp },
      param: { ON: 21, OFF: 20 }, out: { Q: heating } }

screens:
  - name: main
    widgets:
      - { type: value, rect: [20, 40, 200, 60], tag: temp }
      - { type: led,   rect: [20, 120, 40, 40], tag: heating }
```

That is a working thermostat: a measurement, a setpoint, a relay, a
comparator with hysteresis, and a screen showing both. Nine lines of
logic and layout.

---

## Compiled, not interpreted

The board does **not** read this file. The editor compiles it into a
binary pack (a `.visu` file) — string table, variable table, screens
and the compiled program — and the board maps that straight out of
flash.

The reasons are practical: parsing YAML on a microcontroller would cost
memory the board needs, and a screen has to be on the glass in under a
millisecond. So the readable form is what you keep, and the compiled form
is what runs.

**The consequence worth remembering:** the YAML is the source of truth.
The pack is a build artefact — regenerate it any time from the project,
and never edit it by hand.

---

## Compatibility

The format is versioned and the rules are strict, because a project you
made two years ago has to open today:

- **The meaning of an existing key never changes.** A key that meant
  something in one version means the same in every later one.
- **A newer editor keeps keys it does not recognise**, rather than
  dropping them. Opening a project in an older editor and saving it does
  not silently strip what the older one could not see.
- **New features are new keys**, with defaults chosen so that a file
  written before they existed still means what it meant.

Two version numbers exist and they are different things: the **schema
version** counts the vocabulary of this YAML file, the **pack format**
counts the layout of the compiled `.visu`. Both only ever grow, and
error messages name whichever one they mean.

The board is stricter than the editor on purpose: a pack from a **newer**
editor than the firmware is refused outright, rather than loaded with the
parts the firmware does not understand quietly missing. A screen without
the behaviour its author intended is worse than a screen that will not
load. See [Download to the board](/docs/deployment/deploy/).

---

## Working with it in version control

A few things make the diffs better:

**Commit the YAML, not the pack.** The pack is generated and changes
completely when anything does. `*.visu` belongs in `.gitignore`.

**Keep one thing per line where you can.** The flow style above (`- { …
}`) is compact and readable, and it means a changed variable is one changed
line rather than a moved block.

**Let the editor write it.** Round-tripping through the editor produces
stable, consistent output — the same project saved twice is byte for
byte identical, so a diff only ever shows what you actually changed.

---

## Assets live beside it

Fonts and images are separate files in an `assets/` folder next to the
project, referenced by name. They are binary and they do not diff — but
they change rarely, and keeping them out of the YAML keeps the part you
read and review textual.

---

## One file — `.prj32`

A project is **one file**: a `.prj32` package holding the versioned
YAML plus its assets, with its own icon — double-click opens the
editor, and it travels whole: to a colleague, to a customer, into an
archive. The editor opens and saves **`.prj32` only**; every example
and tutorial ships in the same form. A new project is written to
`<location>\<name>\<name>.prj32` — its own folder, named after the
project (the New project wizard's default location is
`Documents\ctrl32\projects`).

Nothing about the format changes inside the package: it is the same
YAML described on this page, versioned and migrated the same way. The
build tooling still reads a bare `.yaml` directly — that path exists
for repository work and automation, not for the editor.
