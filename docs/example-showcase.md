# Showcase — STM32F746 Discovery

The same runtime on entirely different silicon: an STM32F7 with a 4.3"
landscape screen, ethernet and capacitive touch.

**Project:** `examples\f746_disco_example.yaml`
**Board:** ST 32F746G-DISCOVERY, 480×272 landscape
**Needs:** nothing wired up — it runs in simulation as it is

---

## What it shows

That a project is not tied to a chip family. The same languages, the
same widgets, the same pack format, the same editor — a different board
underneath, and nothing about the project has to know.

It is also the project that proves the small things work on a new
target: the font carries accented characters, the icons are sharp, the
clock is set, and bit access is atomic while three writers use one word.

---

## The screens

![The main screen: temperature, switches, icons and the brand mark](img/example-f7-0.png)

**Main.** A value in a large font — the fastest thing on any screen to
read — with vector icons and switches bound to variables. The bar under
the temperature is the same value again, because a number tells you what
and a bar tells you where in the range.

![The info screen: a line of accented text, a counter, the brand mark and a bit switch](img/example-f7-1.png)

**Info.** The line of accented text is deliberate: *Príliš žltučký kôň
úpel ďábelské ódy* is the proof that the font carries the characters
your language needs. That is a thing to find out at your desk rather
than on a finished board in front of somebody.

Below it, bit access — a switch writing **one bit** of a word the logic
is hammering at the same time, and neither losing the other's work.

![The states screen: four lamps on four bits of one word](img/example-f7-2.png)

**States.** The picture worth understanding: **four lamps on four bits
of one 16-bit variable**, with no logic between them.

Two bits are driven by the program at different rhythms, one by the
switch on the Info screen, one by the switch beside them. Three
independent writers into one word, and none of them can undo another.

That is exactly how a drive's status word is displayed — and it is one
variable, four widgets, no code.

---

## Online, on the real board

![The same rungs with live values from a running board: green power flow, 233 cycles counted](img/editor-online.png)

The program with the board running: **green is current flowing**, and
every pin carries its live value — the simulated temperature at 30.7,
the filter's output at 36.8, the counter at 233.

This board is on ethernet, so that view came over the network: the
editor takes an IP address anywhere it would take a COM port.

---

## Worth copying from it

- **a row of lamps reading a status word.** Four widgets, one variable,
  no logic — and it is how every fieldbus device's state is displayed.
- **an alarm shown twice**: as a lamp taking its colour from the alarm
  system, and in an alarm table. One definition, two ways to notice it.
- **a landscape layout that stays readable at arm's length** — one big
  number, everything else supporting it.
- **a test line of your own language's text** on a screen you keep. It
  costs one label and it catches the font problem that otherwise appears
  at the worst moment.

---

## Try changing

- flip bit 1 from the Info screen and watch the lamp on States follow —
  then flip bit 3 there and watch the number under the lamps change by 8
- change the sweep of `sim_temp` and watch the high alarm fire and clear
  itself
- open `http://<board>/` in a phone while it runs: the same screens,
  drawn by the browser

---

| | |
|:---|:---|
| [Examples](examples.md) | back to the list |
| [Thermostat — Olimex EVB](example-thermostat.md) | the ESP32 project |
| [Supported hardware](hardware.md) | what else the runtime runs on |
