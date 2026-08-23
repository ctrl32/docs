# Thermostat — Olimex ESP32-EVB

A wall thermostat on a 2.8" portrait screen, driving the two relays the
board has. There is no temperature sensor on it: a simulated measurement
sweeps the range, so the heating relay audibly clicks around the setpoint
the moment you download it.

**Project:** `examples\olimex_evb_example.yaml`
**Board:** Olimex ESP32-EVB with a MOD-LCD2.8RTP, 240×320 portrait
**Needs:** nothing wired up — it runs in simulation as it is

---

## What it shows

A complete small project, of the kind most first projects turn out to
be: ladder logic with hysteresis, a screen somebody can operate, a
manual mode, a trend, alarms — and a WEBview page shaped for a phone
rather than copied from the board.

---

## The screens

![The thermostat screen: a gauge, the setpoint, and the buttons](img/example-evb-0.png)

**Home.** The gauge is the measurement, the buttons below adjust the
setpoint, and the switch turns automatic mode on and off. One screen
that answers "what is it doing" and "make it do something else".

![Manual control: both relays, individually](img/example-evb-2.png)

**Manual.** Every actuator on its own. This is what you want during
commissioning, and what you want when something has stopped and you need
to find out which part still works.

Note that manual heating only acts while automatic mode is **off** — the
interlock is in the logic, not in the screen, so it holds however the
value is written.

![The trend screen, moments after starting: the chart still filling, the two values below it](img/example-evb-3.png)

**Trend.** Two traces recorded in the board, so the history exists
whether or not anybody is watching. The current values sit under the
chart, where they can be read without interpreting the lines.

![The states screen: lamps from a variable, a panel background, a marker on a scale](img/example-evb-5.png)

**States and motion.** Two lamps on one variable — one taking its
colours from a named set, one with its own — a panel whose *background*
is the state, and a marker that travels the scale as the setpoint moves.

---

## The logic

![The ladder editor: five rungs of the thermostat, blocks in the rungs](img/editor-ladder.png)

Five rungs, and the shape is worth reading:

1. **A heartbeat** — one BLINK on a spare output. The cheapest
   diagnostic there is: anybody at the board can see the program is
   running, without a laptop.
2. **A simulated temperature** — SEL, RAMP and PT1 producing something
   that behaves like a real measurement, so the thermostat has something
   to do on a bench.
3. **The thermostat itself** — a HYST comparator. Two parameters, and
   the entire control loop.
4. **The relay** — automatic AND cold, OR manual AND commanded.
5. **The setpoint buttons** — a rising edge into an addition, so holding
   the button does not run the setpoint away.

---

## Worth copying from it

- **the hysteresis block driving a relay.** The smallest complete
  control loop there is, and the answer to a surprising share of
  problems.
- **a manual screen that mirrors the automatic one.** Costs an
  afternoon, saves a day the first time something misbehaves.
- **a heartbeat on a spare output.** One block.
- **a WEBview page designed for a phone**, not a copy of the board's
  screen — a big number, the state, and the two controls that matter.

---

## Try changing

- the hysteresis gap (`ON` and `OFF` on the HYST block) — watch the
  relay's rhythm change in the trend
- the filter constant on PT1 — a bigger `T` makes the measurement
  smoother and later, which is the whole trade-off in one number
- add a second alarm at a lower limit and watch it appear in the alarm
  table by itself

---

| | |
|:---|:---|
| [Examples](examples.md) | back to the list |
| [Showcase — STM32F746](example-showcase.md) | the same runtime on other silicon |
| [Tutorial projects](tutorials.md) | eleven small ones, a single idea each |
