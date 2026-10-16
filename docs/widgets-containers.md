# Containers

Six widgets that hold other widgets: a panel, a list, a set of tabs, a
popup, a tileview of swiped pages and a window.

Containers do not show data. They give a screen structure — and structure
is what makes the difference between a screen somebody reads and a screen
somebody searches.

---

![Two panels as cards grouping the values on a dark screen](img/gallery-cards.webp){: .sb-center}

## `panel`

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---:|
| `radius` | number | 0 | corner rounding |

A rectangle with children inside it. Children are positioned **relative
to the panel**, so moving the panel moves the group, and a panel that is
hidden hides everything in it.

That last part is the useful bit: one `visible_if` on a panel hides an
entire section of a screen — a manual-control block that only appears in
manual mode, a set of settings that only makes sense for one recipe.

**Use panels as visual grouping too.** A card around related values, with
a heading label at the top, does more for readability than any amount of
careful spacing.

!!! tip "Rounded corners are not free"
    Anti-aliased rounding is computed, not copied. On a screen with a few
    cards it is invisible; on one with thirty small rounded panels it is
    felt. Round the containers, not every element inside them.

---

## `list`

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---:|
| `item_height` | number | | height of one row |
| `inertia` | yes/no | yes | flick scrolling |

A scrolling container. The children are the rows, and only the visible
ones are drawn — so a long list costs what fits on the screen, not what
it contains.

`inertia` gives the flick-and-glide behaviour a phone has. Leave it on
for capacitive glass; on resistive touch, which wants a firm press, it is
less natural and turning it off can feel more controlled.

---

## `tabs`

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---:|
| `active` | number | 0 | which page is shown |

Several pages in one place, one visible at a time. The children are the
pages.

**Tabs versus screens** is a real decision, not a matter of taste:

- **Tabs** keep everything in one screen — the header, the navigation and
  the status stay put while the middle changes. Good for a few closely
  related views of the same thing.
- **Screens** are separate places, reached with a [`nav`
  button](widgets-controls.md). Good when the views have nothing to do
  with each other.

If somebody would say "go to the settings *page*", use a screen. If they
would say "look at the *other* tab", use tabs.

---

## `popup`

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---:|
| `radius` | number | 8 | corner rounding |

A modal window over the screen. While it is visible, **touch does not reach
what is underneath** — which is the whole point: a question that can be
ignored by pressing something else is not a question.

Popups are hidden by default and shown by binding `visible_if` to a
variable the logic sets.

**Use one for:** a confirmation the logic itself raises, a fault that
must be seen before anything else, a value that has to be entered before
a sequence can start.

!!! warning "A popup that appears while somebody is pressing something"
    If the logic can raise a popup at any moment, it can raise one under
    a finger that is already moving — and the press lands on the popup
    instead of the button. For anything raised automatically, make the
    dismiss button somewhere a finger is unlikely to already be.

---

## `tileview`

![A tileview on its first page of three, the dots underneath](img/wl-tileview.webp){: .sb-center}

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `tag` | variable | | the number of the page shown |
| `active` | number | 0 | the page shown first, without a variable |

Pages — its children — switched by a **swipe** to the left or right,
with a dot for each page underneath. On a phone this is the most natural
way through a handful of similar pages: one zone per page, one pump per
page.

With a variable, the variable **is** the page number: a swipe writes it,
and the logic or another widget can turn the page — a fault on pump 3
can bring pump 3's page forward on its own.

Every child is one page, laid out in the tileview's own frame. Make each
page a [`panel`](#panel) and put the page's widgets inside it:

```yaml
- type: tileview
  rect: [872, 396, 368, 140]
  tag: page
  children:
    - type: panel
      rect: [0, 0, 368, 140]
      children:
        - { type: value, rect: [16, 50, 300, 60], tag: temp_a }
    - type: panel
      rect: [0, 0, 368, 140]
      children:
        - { type: value, rect: [16, 50, 300, 60], tag: temp_b }
```

---

## `window`

![A window with its title bar and the X that closes it](img/wl-window.webp){: .sb-center}

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `text` | text | | the title in the bar |
| `tag` | variable | | written FALSE by the X |
| `bar_height` | px | 32 | the height of the title bar |
| `font` | font | | how the title is drawn |

A body with a title bar in the accent. Its children sit under the bar,
in the window's own frame.

With a variable the bar carries an **X**, and the X writes the variable
false. Give the window `visible_if` with the same variable and the X
closes it; anything that sets the variable true again — a button, a
checkbox, the logic reacting to an event — opens it.

```yaml
- type: window
  rect: [872, 548, 368, 146]
  text: "Window"
  tag: win_open
  visible_if: win_open
  children:
    - { type: label, rect: [12, 48, 340, 22], text: "X closes me" }
```

!!! tip "A window or a popup?"
    A [`popup`](#popup) belongs to a moment — a question, a confirmation —
    and covers the screen. A window is part of the screen: a detail
    that can be put away and brought back, while everything around it
    stays usable.

---

## How nesting works

Children are positioned relative to their parent, and a hidden parent
hides its children. That is the whole model, and two things follow from
it:

**Grouping is cheap.** Wrap a section in a panel and you can move it,
hide it or disable it as a unit, without touching anything inside.

**Depth costs nothing to draw but plenty to read.** A screen four
containers deep is hard to reason about in the editor tree, and the
person maintaining it in a year will be you.

Keep the [limits](limits.md) in view: 64 widgets per screen, and the
containers count.
