# tabs

**Containers** · in a project file: `type: tabs`

Several pages in one place, one visible at a time.

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `active` | integer | `0` | which page is shown |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](states-motion.md) - see the [Property reference](widgets.md).

## Description

Several pages in one place, one visible at a time. The children are
the pages.

**Tabs versus screens** is a real decision, not a matter of taste:

- **Tabs** keep everything in one screen — the header, the navigation
  and the status stay put while the middle changes. Good for a few
  closely related views of the same thing.
- **Screens** are separate places, reached with a `nav` button. Good
  when the views have nothing to do with each other.

If somebody would say "go to the settings *page*", use a screen. If
they would say "look at the *other* tab", use tabs.

---

Every widget of the family: [Containers](widgets-containers.md) · every widget: [Property reference](widgets.md)
