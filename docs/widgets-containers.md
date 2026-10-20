# Containers

Six widgets that hold other widgets: a panel, a list, a set of tabs, a
popup, a tileview of swiped pages and a window.

Containers do not show data. They give a screen structure — and structure
is what makes the difference between a screen somebody reads and a screen
somebody searches.

---

![Two panels as cards grouping the values on a dark screen](img/gallery-cards.webp){: .sb-center}

## The widgets

<!-- w-index: begin -->

| Widget | What it is |
|:---|:---|
| [panel](w-panel.md) | A rectangle that groups other widgets, as a unit and as a visual card. |
| [list](w-list.md) | A scrolling container whose children are its rows. |
| [tabs](w-tabs.md) | Several pages in one place, one visible at a time. |
| [popup](w-popup.md) | A modal window over the screen that keeps touch from what is underneath. |
| [tileview](w-tileview.md) | Pages switched by a swipe to the left or right, with a dot for each page. |
| [window](w-window.md) | A body with a title bar whose X can close it, part of the screen rather than a moment. |

<!-- w-index: end -->

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
