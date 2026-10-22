---
title: "Controls: recipe_table"
slug: w-recipe_table
section: "Visualisation"
order: 44
sidebar_position: 44
generator: tools/docs_export.py
---

# recipe_table

**Controls** · in a project file: `type: recipe_table`

The slots of one recipe definition, for selecting, saving, loading and deleting sets.

## Properties

| Property | Type | Default | Meaning |
|:---|:---:|:---:|:---|
| `font` | font | - | how the rows are drawn |

Every widget also has its place (`x`, `y`, `w`, `h`), a `style`, `visible_if` / `enabled_if` and the state colours and motion of [States and motion](/docs/visualisation/states-motion/) - see the [Property reference](/docs/visualisation/widgets/).

## Description

Drop a **recipe table** on the screen and type the recipe
definition's name into its *Text* field; the table shows one row per
slot with the set's name, marks the loaded set and highlights the
selected row. When a definition is renamed in the Recipes window,
every table that names it follows the rename.

Beside it, three ordinary **buttons** with the modes *recipe load*,
*recipe save* and *recipe delete* — they bind to the table of the same
screen and need no variable. A button with *confirm* asks first; on a
delete that is the right default.

What the operator does:

1. taps a row — the row is selected, nothing changes yet
2. **Save** — the current values of the definition's variables are
   written into that slot, under the name it has (or `Recipe N`)
3. **Load** — the slot's values land in the variables in one cycle
   and `<name>.recipe` shows the slot
4. **Delete** — the slot is emptied; the values in the variables stay

The selected slot is the hidden variable `<name>.recipe_sel`; the
buttons act on it.

In WEBview a second tap on the selected row renames it — the name
shows on the panel's glass as well. A rename on the glass is not part
of this version.

The panel refuses a Save when the store is full and says so on the
screen and in WEBview; nothing is lost quietly. Recipes are kept on
the ESP32 and the Linux runtime; a recipe definition is refused for an
STM32 target. See [Recipes](/docs/operation/recipes/).

---

Every widget of the family: [Controls](/docs/visualisation/widgets-controls/) · every widget: [Property reference](/docs/visualisation/widgets/)
