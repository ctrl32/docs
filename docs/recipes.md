# Recipes

A recipe is a named set of values for the variables an operator adjusts
per product: the setpoints, the times, the options. The device keeps the
sets in its own store, the operator saves and loads them from a screen,
and the program never knows a recipe exists - a load is an ordinary
operator write of every variable in the set, in one cycle.

## Defining a recipe

In the project tree, **Recipes** -> *Add recipe*. A definition has:

- a **name** - the name of the definition, not of a set (`product`,
  `cycle`, `dough`)
- the **variables** a set carries - `rw` variables of any numeric or
  boolean type; a variable may sit in several definitions
- **max sets** - how many sets the device keeps for this definition
  (default 20)

The build adds two hidden variables per definition, both integers:

| Variable | Meaning |
|---|---|
| `<name>.recipe` | the slot last loaded, `-1` = none; a program may read it (a comparison block, a screen value) |
| `<name>.recipe_sel` | the slot selected on the table; the buttons act on it |

The name is edited in place in the Recipes window; every table that
names the definition follows the rename.

A definition can be removed like any tree node; the sets stay in the
device's store until the next download compacts them.

## The screen

Drop a **recipe table** on the screen and type the definition's name
into its *Text* field; the table shows one row per slot with the set's
name, marks the loaded set and highlights the selected row. Beside it,
three ordinary **buttons** with the modes *recipe load*, *recipe save*
and *recipe delete* - they bind to the table of the same screen and need
no variable. A button with *confirm* asks first; on a delete that is the
right default.

What the operator does:

1. taps a row - the row is selected, nothing changes yet
2. **Save** - the current values of the definition's variables are
   written into that slot, under the name it has (or `Recipe N`)
3. **Load** - the slot's values land in the variables in one cycle and
   `<name>.recipe` shows the slot
4. **Delete** - the slot is emptied; the values in the variables stay

In WEBview a second tap on the selected row renames it - the name shows
on the panel's glass as well. A rename on the glass is not part of this
version.

The panel refuses a Save when the store is full and says so on the
screen and in WEBview; nothing is lost quietly.

## Where the sets live

| Target | Store |
|---|---|
| ESP32 | the assets partition of the flash; a journal that survives a power cut at any moment of a write |
| Linux runtime | a file beside the program (`<program>.recipes`), written the same way |
| STM32 | not in this version - a recipe definition is refused for an STM32 target |

A program download keeps the sets. The device page shows `rc=<definitions>,<sets>`.

When a variable of a definition is removed from the project, a load
writes the values it still has and says how many it dropped in the
diagnostic buffer; a variable added to the definition keeps its current
value until the set is saved again. Sets are matched by the variable's
name, so renaming a variable orphans its stored values.

## Limits

| | Standard | LITE (ESP32 without PSRAM) |
|---|---|---|
| Definitions per project | 8 | 4 |
| Variables per definition | 64 | 16 |
| Sets per definition | 64 | 8 |

A set costs `44 + 12 bytes per variable` in the store. The editor
refuses a definition beyond these limits before the download; a full
store refuses a Save on the device.

Recipes are not a safety function and not a substitute for an
interlock: a loaded value is a value the program checks like any other
operator input.
