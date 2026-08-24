# States and motion

Two things a widget can do beyond showing a value: **change colour with
a state**, and **move along a path as a value sweeps its range**. Both
are properties of the widget — no logic blocks, no extra variables, and
they behave identically on the board's display and in WEBview.

They earn their place on one picture: a row of lamps lit by the bits of
a status word, and a marker that walks a scale as a temperature climbs.

---

## States: one widget, three colours

A widget with a `state:` carries three colours — **true**, **false**
and **alarm** — and a variable that decides which one shows:

```yaml
- { type: led, rect: [24, 78, 38, 38],
    state: { var: running, true_color: "#22C55E",
             false_color: "#3A3F4B", alarm_color: "#EF4444" } }
```

`var` may be a bool, or an integer with `bit:` naming which bit to
watch. That is the whole trick behind lighting a panel from a status
word: one integer arrives from a drive, four lamps each watch one bit,
and there is no logic between them.

```yaml
- { type: led, rect: [24, 78, 38, 38],
    state: { var: status_word, bit: 0, style: Motor } }
- { type: led, rect: [74, 78, 38, 38],
    state: { var: status_word, bit: 1, style: Motor } }
```

### Named sets

Writing three colours on every lamp gets old. The project can carry
**named sets** and widgets point at them by name:

```yaml
states:
  - { name: Motor, true_color: "#22C55E", false_color: "#3A3F4B",
      alarm_color: "#EF4444" }
```

Recolouring every lamp in the project is then one edit — the same
argument that gives styles their existence, applied to the
true/false/alarm triple.

### Where the alarm colour comes from

The alarm state wins over true/false, and it has two sources:

- `alarm:` — a variable; anything non-zero forces the alarm colour,
- `alarm_ref:` — one of the project's own [alarms](visualisation.md),
  so a lamp goes red exactly when the alarm table says so.

### What the state paints

`paint:` decides which colour of the widget the state drives:

| `paint` | What changes | Typical widget |
|:---|:---|:---|
| `accent` (default) | the active colour | `led`, `switch` |
| `bg` | the background | `panel` — a strip that tints with RUN |
| `fg` | the text | `label` |

---

## Showing and hiding: `visible_if`

Sometimes recolouring is not enough — a control should not be on the
screen at all. Any widget may carry `visible_if:` with a boolean
variable: while the variable is false the widget does not draw
**and does not take touch**, which is the point — an invisible
switch that still switches would be worse than a visible one.

```yaml
- { type: switch, rect: [20, 142, 64, 28], tag: cmd_a, style: sw,
    visible_if: mode_man }
- { type: label, rect: [20, 146, 80, 20], text: "AUTO",
    style: auto, visible_if: nman_p }
```

That pair is the canonical use: in manual mode the switch exists, in
automatic a badge stands in its place — and nobody flips a heater
that is not there. The browser evaluates the same records, so the
phone shows and hides exactly with the glass. `visible_if` and
`state:` cannot share one widget; the [Hot tank](three-zone-thermostat.md)
shows the pattern at full scale.

---

## Motion: a widget that travels

`move:` makes a widget walk a straight path as a value sweeps a range:

```yaml
- { type: led, rect: [24, 212, 24, 24],
    state: { var: swing, style: Motor },
    move: { var: level, from: [24, 212], to: [420, 212],
            min: 0, max: 100 } }
```

At `min` the widget sits at `from`, at `max` it sits at `to`, and in
between it is proportionally along the line. Values outside the range
**clamp** — a bad scale never throws the element off the screen.

For two independent axes, `x:` and `y:` each take their own variable
and range:

```yaml
move:
  x: { var: pos_x, min: 0, max: 1500 }
  y: { var: pos_y, min: 0, max: 400 }
  from: [20, 40]
  to: [300, 200]
```

A filling level, a carriage on a rail, a position on a floor plan —
anything that is *somewhere between two points* reads better moving
than as a number.

---

## A complete example

A tank level as a moving marker, and a pump lamp from one bit of a
status word:

```yaml
project:
  name: tank_demo
  target: preset_s3_ssd1963
  resolution: [480, 272]

states:
  - { name: Pump, true_color: "#22C55E", false_color: "#3A3F4B",
      alarm_color: "#EF4444" }

tags:
  - { name: level,  datatype: f32, unit: "%", decimals: 0, init: 40 }
  - { name: status, datatype: i32 }

screens:
  - name: main
    widgets:
      - { type: label, rect: [20, 12, 200, 24], text: "Tank" }
      - { type: panel, rect: [40, 60, 8, 160] }
      - { type: led, rect: [28, 204, 32, 32],
          state: { var: status, bit: 0, style: Pump },
          move: { var: level, from: [28, 204], to: [28, 52],
                  min: 0, max: 100 } }
      - { type: value, rect: [100, 60, 140, 40], tag: level }
```

The marker rides the strip from the bottom at 0 % to the top at
100 %, and its colour is bit 0 of `status` — two behaviours, one
widget, no logic.

---

## Worth knowing

- **Deadband applies.** A state or a position only redraws when the
  driving variable really changes — a noisy value with no
  [deadband](variables.md) repaints for nothing, on the glass and over
  the network alike.
- **The browser matches the glass.** WEBview evaluates the same
  states and the same paths from the same project — what moves on the
  display moves in the browser.
- **Colour is never the only signal.** Roughly one man in twelve cannot
  separate red from green reliably; give important states a word or a
  shape as well. See [HMIview](hmiview.md).
