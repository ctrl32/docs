# Controls and shortcuts

**Properties** (the panel at the bottom) follows what you click: a widget
on a screen, a contact, coil or block on a ladder rung, a block in an FBD
diagram — name, variables, parameters, axis, all editable there. The
**Toolbox** on the right opens folded; expand the group you need.

Everything the editor can do is reachable with the mouse; the
shortcuts exist for the handful of actions you repeat all day. This
page is the complete reference — menus, keys, and what the mouse
does on each kind of canvas.

![The editor: device tree left, canvas centre, Toolbox and inspector right, Resources below the tree](img/editor-layout.webp){: .sb-center}

## Keyboard

| Keys | Action |
|:---|:---|
| `Ctrl+N` | new project |
| `Ctrl+O` | open project |
| `Ctrl+S` | save |
| `Ctrl+Shift+S` | save as |
| `Ctrl+Z` / `Ctrl+Y` | undo / redo — unlimited, across every editor (canvas, ladder, FBD, variables); the Edit menu shows how many steps each way |
| `F7` | build — compile and report, touch nothing |
| `F5` | download to the panel — build first, then send |
| `Ctrl+D` | duplicate the selected widget (with its children) |
| `Delete` | delete the selection — widgets on the canvas, blocks and contacts in ladder, blocks and wires in FBD |
| `Esc` | drop the selection |
| `←` `→` `↑` `↓` | nudge the selected widget by 1 px |
| `Shift` + arrows | nudge by 10 px |
| `Ctrl+Enter` | apply the declaration pane (variables edited as text) |
| `Alt+F4` | exit |

Shortcuts stay out of the way while you type into a field — `Delete`
inside a name edits the name, not the screen.

## The menus

| Menu | What lives there |
|:---|:---|
| **File** | New (`Ctrl+N`), Open (`Ctrl+O`), **Examples** (every shipped example and tutorial, one click), Save (`Ctrl+S`), Save as (`Ctrl+Shift+S`), Download to panel (`F5`), Exit |
| **Edit** | Undo / Redo, each with its step count |
| **View** | Language |
| **Project** | Add device — the same list the tree's right-click offers |
| **Build** | Compile (`F7`) |
| **Online** | Download to panel (`F5`), Find devices, Scope, Force, **Simulation** start/stop |
| **Debug** | Pause and single-cycle Step — enabled while a simulation runs |
| **Tools** | Device library (the Modbus and EDS catalogues) |
| **Window** | Close all tabs, Reset layout — the cure for a panel dragged somewhere unrecoverable |

## The toolbar, left to right

| Icon | Action |
|:---|:---|
| :ti-file-plus: :ti-folder-open: :ti-device-floppy: | new, open, save |
| :ti-arrow-back-up: :ti-arrow-forward-up: | undo, redo |
| :ti-terminal-2: | the serial [terminal](online.md) — the board's console |
| :ti-wave-square: | the scope (trace) |
| :ti-eyeglass: | [find devices](find-devices.md) — COM and network sweep |
| *port picker* | which COM port or address the editor talks to — nothing is preselected, ever |
| :ti-plug: | **ONLINE** — connect to the running board (:ti-plug-connected: while connected) |
| :ti-download: | **download to the panel** (`F5`) — the only coloured icon in the bar, on purpose |

While a **simulation** runs (started from *Online → Simulation*),
a transport appears after the download icon: :ti-player-stop: stop,
:ti-player-pause: pause, :ti-player-track-next: one PLC cycle.
The rest of the time the bar carries no player icons — ONLINE is a
different mode and the two never mix.

## The mouse on the screen canvas

The canvas is **1 : 1** — the pixels you drag are the panel's
pixels; there is no zoom to lie about sizes.

| Gesture | Action |
|:---|:---|
| click | select a widget — the inspector follows |
| drag a widget | move it |
| drag the corner grip | resize (the primary selection carries the grip) |
| `Shift` + click | add to the selection |
| drag on empty canvas | rubber-band select everything inside |
| click empty canvas / `Esc` | select nothing |

Text is edited in the **inspector**, never on the canvas — what the
canvas shows is exactly what the panel will draw. With several
widgets selected, the bar above the canvas aligns, centres and
distributes them, and a drag moves the whole selection together.
The inspector always edits the primary selection — the one with the
strong outline and the resize grip.

## The mouse in ladder and FBD

Both program editors — [Ladder](ladder.md) and
[FBD](fbd-composites.md) — work the same way: **right-click is the whole
menu**. On a rung or the empty diagram it offers what can be added
there — contacts, coils, function blocks, branches; on an element
it offers cut, copy, paste and delete. `Delete` removes the
selection, `Ctrl+Z` takes anything back.

- **Ladder**: *+ Rung* adds a rung (and creates its variable when
  none is picked). Contacts and coils bind to a variable on the
  element itself - type its name, pick from the list under the field,
  or Enter a new name to create it; a block placed on a rung joins it
  with its EN pin.
- **FBD**: blocks come from the **Toolbox** (click adds into the
  selected network); wires are drawn **pin to pin** — click an
  output, click an input. A wire that would cross networks is
  refused.
- **ST**: a plain text editor with completion; the declaration pane
  above applies with `Ctrl+Enter`.

The block palette is grouped the same way in both editors and in
the [function block reference](blocks.md).

## The tree

Right-click is the builder: on **Application** it adds VAR lists,
POUs, alarms, libraries and axes; on a bus it adds the devices that
bus can carry ([adding a peripheral](adding-peripherals.md));
on a device it offers its card. Single click opens the page of
whatever is clicked — board, bus, device, screen, program. The
**Resources** panel under the tree expands into the full
diagnostics page with the :ti-arrows-maximize: button.

## Panels and layout

Every panel — tree, Toolbox, inspector, Resources — docks: drag its
title to move it, drop it on another edge, and **double-click a
floating panel's title to send it back** where it came from.
*Window → Reset layout* restores the factory arrangement when a
panel ends up somewhere unrecoverable.

## Where the rest lives

- Values are **written** to a running board from the
  [force page](force.md), never by typing into the canvas — online
  the canvas is read-only, deliberately.
- The [scope](online.md) records variables against the PLC cycle.
- Board pages hold everything hardware: pins, network, *Flash
  runtime*.
