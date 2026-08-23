# Indicators

Three widgets that show a value without letting anyone change it: a lamp,
a bar and a gauge.

They are what somebody reads from across the room, so the question with
each is not "does it show the value" but "can it be understood in half a
second, by somebody who is not looking carefully".

---

## `led`

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `shape` | `round` / `rect` | round | how it is drawn |
| `tag` | variable | | what it follows |
| `color_on` | colour | | when the value is true |
| `color_off` | colour | | when it is not |
| `blink_hz` | number | 0 | blink rate; 0 = steady |
| `bit` | number | −1 | which bit of an integer; −1 = the whole value |

The workhorse of any screen. One variable, two colours, immediately
readable.

**`bit` turns one integer into a row of lamps.** A status word from a
drive, a mask the logic builds, a set of flags — point four lamps at the
same variable with bits 0 to 3 and the whole word is visible at once.

**`blink_hz` earns its place on things that need attention.** A steady
red lamp and a blinking red lamp say different things, and people read
the difference without being taught. Use blinking for "unacknowledged",
steady for "still present".

!!! tip "Three states are better than two"
    A lamp does not have to be limited to on and off. With
    [states](widgets.md) it takes a true, a false **and** an alarm
    colour, driven by a variable or by one bit — so one widget says
    running, stopped, or faulty, instead of two widgets and a hidden
    one.

---

## `bar`

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---:|
| `tag` | variable | | the value |
| `min`, `max` | number | 0, 100 | the range it spans |
| `orientation` | `vertical` / `horizontal` | | which way it fills |

A proportion, at a glance. Tank level, load, progress, how far through a
delay.

The strength of a bar is that it shows **where the value sits in its
range** without anybody doing arithmetic. "Forty-two" means nothing on
its own; a bar four-tenths full means something immediately.

!!! tip "Set min and max to what matters, not to what is possible"
    A pressure sensor may read 0–16 bar while the interesting range is
    4–6. A bar spanning the full sensor range is a bar that never moves.
    Span the range you care about and let it clip.

**Vertical bars read as level; horizontal ones read as progress.** It is
a small thing and it is worth following, because people bring the
expectation with them.

---

## `gauge`

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---:|
| `tag` | variable | | the value |
| `min`, `max` | number | 0, 100 | the range |
| `start_angle` | number | 135 | where the scale begins, degrees |
| `sweep` | number | 270 | how far it goes round |
| `thickness` | number | 0 | ring thickness; 0 = automatic |
| `needle` | yes/no | yes | draw a needle |
| `cache_background` | yes/no | yes | precompute the dial |

The dial. Slower to read than a bar and better at one thing: a person who
knows the equipment recognises the *position* of the needle without reading
the number at all.

**Leave `cache_background` on.** The dial — the ring, the ticks, the
gradient — is expensive to draw and never changes, so it is rendered once
at startup and reused. Turning the cache off means drawing it on every
update, and on a busy screen that is felt.

**`needle` off gives you a ring** instead: a filled arc with the value in
the middle. Cleaner, more modern, and easier to read at small sizes. The
needle is better when somebody watches for the value to move.

The default 135° start with a 270° sweep is the familiar shape — bottom
left, round the top, bottom right. Changing them gives you a half dial
(start 180, sweep 180) or a quarter.

---

## Choosing between them

| The question is | Use |
|:---|:---:|
| is it on? | **led** |
| how full, how far, how much of the way | **bar** |
| what is the value, roughly, at a glance | **gauge** |
| what is the value, exactly | a [`value`](widgets-text.md) widget |

And the honest answer is often the last one. A number in a large font is
the fastest thing to read on any screen — gauges and bars earn their
place when the *position within a range* matters more than the digits.

---

## What makes indicators expensive

An indicator redraws when its variable changes. An analog variable
without a deadband changes on every flicker of its last digit, so a
gauge bound to one repaints continuously and never sits still.

Set a deadband on the variable, not on the widget. Everything reading it
gets quieter at once — the board, the trend, the browser. See
[Variables](variables.md).
