---
title: "HMIview — the panel screen"
slug: hmiview
section: "Visualisation"
order: 18
sidebar_position: 18
generator: tools/docs_export.py
---

# HMIview — the board's own screen

The screen on the front of the device. What you see when you walk up to
something you built and want to know what it is doing.

HMIview is drawn in the same editor as everything else, from the same
variables, and travels in the same file. This page is how it works and how to
draw one that helps; the [Property reference](/docs/visualisation/widgets/) lists every
widget and its properties.

---

## Screens, not pages

A project has up to **32 screens** and up to **64 widgets on each**
(the [Linux runtime](/docs/hardware/linux-runtime/) carries 320 and 256). One is shown at
a time; the operator moves between them with `nav` widgets.

That is generous for a project and deliberately not unlimited. An
installation that needs forty screens usually needs three good ones
instead — an operator who has to remember where something lives will
not find it in a hurry.

**A useful default shape:**

| Screen | Holds |
|:---|:---|
| Home | the state of the equipment in one glance, and the two controls that matter |
| Manual | every actuator, individually, for commissioning and fault-finding |
| Settings | setpoints, times, recipe values |
| Alarms | what is wrong and what was wrong |
| Trend | how a value has behaved |

---

## Placing a widget

Open a screen under **HMIview** in the tree: the Toolbox on the right
lists the widgets. A click on one adds it into the selection; drag it
where it belongs and bind it in **Properties**. A widget holds no value
of its own — its variable field names the variable it shows or writes:

| Widget | Bound to | Typical settings |
|:---|:---|:---|
| **button** | a BOOL with access `rw` | text; `mode` `momentary` (TRUE while held), `toggle`, `set` or `reset`; `confirm: true` for a command that moves something |
| **led** | a BOOL, or one bit of an integer | a [state](/docs/visualisation/states-motion/) colour set |
| **input** | a number or a `TIME` with access `rw` | `min` and `max` in the variable's unit |
| **value** | any variable | unit and decimals come from the variable |
| **label** | — | its text |

A variable the program alone writes (no `rw`) cannot be written from a
screen. The complete list of widgets and properties is the
[Property reference](/docs/visualisation/widgets/).

## The resolution

Clicking **HMIview** in the device tree opens its settings page. On a
board with glass there is nothing to decide — the screen's pixels are
the board's pixels, and the page says so. On a target that scales
(the [Linux runtime](/docs/hardware/linux-runtime/)), the page offers the common
resolutions and a custom size: author at whatever suits the design,
and the runtime fits it to its glass with the shape kept.

The same page sets the **orientation** — how the picture sits on the
glass as it is mounted: as mounted, or rotated 90°, 180° or 270°.
Choosing 90° or 270° swaps the resolution, and the board draws the
picture that way (rotated 180° exists for SPI glasses only) — and
the **WEBview canvas**, the size the browser screens are drawn for,
usually a phone in portrait.

![The HMIview settings page: resolution, orientation, WEBview canvas](img/hmiview-settings.webp){: .sb-center}

## The boot splash

A board that connects to WiFi or a broker takes a few seconds to come
up, and without help the glass spends them dark. The **Boot splash**
section on the same page fills that gap: the panel puts a picture on
the screen the moment the display is alive — one of the project's
images, or the ctrl32 mark if none is picked — and holds it until the
runtime is up **and** the configured minimum time has passed. The
default is two seconds; `0` turns the splash off and the first screen
appears as soon as it can.

---

## Drawing is exact

The editor canvas is not an approximation. It runs **the board's own
rasteriser** — the same code, the same fonts, the same rounding, the same
colours — so what you place is what appears on the glass.

This is worth more than it sounds. Text that fits by two pixels in the
editor fits by two pixels on the board; a font that renders your
language's diacritics correctly on screen renders them correctly on the
equipment.

!!! tip "Test at the real size"
    A screen designed on a 27" monitor and shown on a 4.3" board is
    always smaller than you expected. Keep the canvas at the board's real
    resolution while you work, and stand back from the monitor
    occasionally.

---

## Touch is not a mouse

A finger is about **10 mm** across and arrives with a person attached to
it.

- **Resistive touch** (the cheaper glass) wants a firm press and is
  accurate. It works with gloves and wet hands, which on many projects
  decides the matter.
- **Capacitive touch** is light and precise, and does not work through
  most gloves.

Make targets **big**. A button 40 px tall on a 480×272 board is
comfortable; 30 px is possible on capacitive glass and unkind on
resistive. Space them so that a press slightly off-centre still hits the
right one.

!!! warning "Confirm anything that moves something real"
    Capacitive touch near a frequency drive can register presses that
    nobody made. A `confirm` on a command that starts a motor is not
    decoration — it is the difference between electrical noise and an
    axle turning.

---

## Colour carries meaning

**Eight themes ship with the editor** - dark, light, night, steel, forest,
sand, contrast and ocean - each a full set of the same style names
(screen, card, title, value, input, led, button, nav, trend, gauge, table,
recipes and the rest). The New project dialog starts a project on one of
them; *Styles and themes* in the project tree adds another from the
library or replaces the active one, and a variable can switch the panel
between the project's themes at run time. Your own theme file in
`Documents\ctrl32\themes` appears in the same list.

A second variable on the same page, *Screen switched by VAR*, lets the
program open a screen: when it changes the variable to a screen's index
(the order of the screens in the tree, the first is 0), that screen
comes to the front on the panel and in the browser - a ring at the door
opens the Door screen. A value outside the screens does nothing, and a
tap on a navigation button is never undone: to bring a screen back
after the operator tapped away, the program writes the variable again
(write -1 in between, or any value that is no screen).

The screen is read by somebody who is tired, in a hurry, and possibly
holding a torch. Colour does more work than text.

Use [states](/docs/visualisation/states-motion/) rather than drawing one widget per
condition: a lamp with a true, false and alarm colour is one widget
that says three things, driven by a variable or by one bit of an
integer.

**A convention worth keeping:** green means running as intended, grey
means off and correct, red means it needs a person, amber means it will
need one soon. Then keep it identical on every screen — an operator
learns the colours once and reads every screen afterwards.

!!! tip "Never let colour be the only signal"
    Roughly one man in twelve cannot separate red from green reliably.
    Give the important states a shape or a word as well as a colour.

---

## What redraws, and why it matters

The board does not repaint the screen continuously. A widget whose value
changed marks its own rectangle, the rectangles are merged into bands and
only those are sent to the display.

Repainting a whole 800×480 frame costs 20–25 ms; repainting the part that
changed costs almost nothing. That is why a busy screen still feels
immediate — and why an analog value **without a deadband** is expensive:
it marks itself dirty on every flicker of its last digit and repaints
forever.

Set a deadband on every analog variable. It is the single most effective thing
you can do for a screen's responsiveness. See [Variables](/docs/editor-overview/variables/).

!!! note "Flat colours cost almost nothing; gradients do not"
    Filled areas, text and lines cost almost nothing. Gradients, shadows
    and anti-aliased rounded corners are expensive to compute. Use them
    where they earn their place — a header, a title bar — and not
    everywhere.

---

## Graphics never delay control

The rule is **logic before communication before graphics**. The renderer
takes a snapshot of the variable table and works from that; it never holds
anything the PLC cycle needs.

Under load, frames are dropped. The cycle is never extended. A screen may
stutter while the program is doing something demanding — control never
waits for a picture.

---

## Patterns that work

- **Interlocks belong in the logic, not on the screen.** A manual
  command that may act only while automatic mode is off is gated in
  the program, so it holds however the value is written — from the
  glass, the browser or a bus.
- **Setpoint buttons through a rising edge.** A `+` button wired through
  `R_TRIG` into an addition steps once per press; holding the button
  does not run the setpoint away.
- **A heartbeat.** One `BLINK` on a spare output or a lamp: anybody at
  the equipment sees that the program runs, without a laptop.
- **A test line of your own language.** One label with the accented
  letters your language needs, on a screen you keep, proves the font
  carries them — at your desk, not in front of a customer.
- **A link lamp beside a life counter** (or beside a bit of the other
  controller's clock byte): together they say which of the two sides
  stopped.
- **The other controller's address in the label** (`DB120.DBW4`) costs
  nothing and doubles the screen as the map between the two sides.
- **Trends are recorded in the device**, whether or not anybody is
  watching; put the current values under the chart, where they can be
  read without interpreting the lines.

## The board with no screen

Plenty of installations have no display at all. The logic runs, the
fieldbuses run, and the visualisation lives in a browser — see
[WEBview](/docs/visualisation/webview/).

If you draw no WEBview screens, the browser is served the HMI ones. So a
headless controller can still have a full visualisation, and a board with
a display can be watched from a phone, from the same project.

---

## Where to go next

| | |
|:---|:---|
| [Property reference](/docs/visualisation/widgets/) | every widget, every property |
| [States and motion](/docs/visualisation/states-motion/) | colour from a state, movement from a value |
| [Variables](/docs/editor-overview/variables/) | what the screens are drawing, and deadband |
| [WEBview](/docs/visualisation/webview/) | the same project in a browser |
| [Performance and limits](/docs/operation/limits/) | how many screens, widgets and variables fit |
