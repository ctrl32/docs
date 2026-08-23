# Text and values

Two widgets: one draws fixed text, the other draws a number that changes.

Between them they carry most of what a screen actually says, and the
number widget is the fastest thing on any screen to read — worth
remembering before reaching for a gauge.

---

## `label`

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---:|
| `text` | text | | what it says |
| `font` | font | | which face and size |
| `align` | `left` / `center` / `right` | left | within its rectangle |

Fixed text: a heading, a unit, a name beside a lamp, an instruction.

**Alignment matters more than it looks.** A column of labels aligned
right against a column of values aligned left reads as a table, and the
eye follows it without effort. The same labels aligned left produce a
ragged gap between name and number that the reader has to cross every
time.

!!! warning "Check your language's accented characters early"
    A font baked without the right character range drops accents
    silently — the text renders, just without the marks, and it is the
    kind of thing nobody notices in the editor and everybody notices on
    the board. Put one label with your worst-case word on a test screen
    and look at it on the glass.

---

## `value`

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---:|
| `tag` | variable | | what it shows |
| `font` | font | | which face and size |
| `show_unit` | yes/no | yes | append the variable's unit |
| `warn_above` | number | | draw differently above this |
| `warn_color` | colour | | the colour to use then |

A number, live. The decimals and the unit come from the **variable**, not
from the widget — set them once in the variable table and every screen
showing it agrees.

**`warn_above` is the cheapest alarm on any screen.** A temperature that
turns amber past 80 needs no alarm definition, no acknowledgement and no
extra widget — and it is read from across the room by somebody who is not
looking for it.

Use it for the soft limit, and a real [alarm](widgets-data.md) for the
hard one. Together they give a warning stage and an action stage.

!!! tip "Make the important number bigger than feels sensible"
    A screen with one number in a large font and everything else small is
    readable from a distance and instantly tells the reader what this
    screen is *about*. Five numbers of the same size is a screen with no
    subject.

---

## Where the decimals come from

Both widgets draw what the variable says. A variable with two decimals
and unit `bar` shows `4.25 bar` on the board, in the browser and in a
trend legend — no per-widget formatting, no disagreement between two
screens showing the same thing.

The corollary: if a value shows too many digits, fix the **variable**.
`show_unit` exists for the case where the unit is already in a label
beside it and repeating it would be noise.

---

## Deadband, again

A number without a deadband on its variable repaints on every flicker of
the last digit — and a value that will not sit still is harder to read
than one that updates twice a second.

Deadband is a property of the variable, so setting it quiets the screen,
the browser and the trend at once. See [Tags](tags.md).
