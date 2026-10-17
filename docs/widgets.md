<!-- AUTOMATICALLY GENERATED from schema/visu-schema.yaml -->

# Widgets

Schema version: **56** — the vocabulary of the project file. The compiled pack carries its own format number; error messages name whichever one they mean.

## Common properties (widget_base)

| Property | Type | Default |
|---|---|---|
| `id` | str |  |
| `x` | i16 |  |
| `y` | i16 |  |
| `w` | i16 |  |
| `h` | i16 |  |
| `anchor_x` | one of `start` / `end` / `center` / `stretch` | `start` |
| `anchor_y` | one of `start` / `end` / `center` / `stretch` | `start` |
| `margin` | i16 | `0` |
| `style` | style_ref |  |
| `visible_if` | variable |  |
| `enabled_if` | variable |  |
| `children` | list |  |
| `state` | map — see [States and motion](states-motion.md) |  |
| `move` | map — see [States and motion](states-motion.md) |  |
| `rotate` | map |  |
| `animations` | list — event-bound animations |  |

## `panel`

A card that groups widgets: its fill (bg), its border (fg) and its corner radius. With `opacity` between 1 and 99 the card is translucent - the picture under it shows through (a glass card over a photograph); 0 or 100 is the solid card.

| Property | Type | Default |
|---|---|---|
| `radius` | i16 | `0` |
| `opacity` | i16 | `0` |

## `list`

| Property | Type | Default |
|---|---|---|
| `item_height` | i16 |  |
| `inertia` | bool | `True` |

## `tabs`

| Property | Type | Default |
|---|---|---|
| `active` | i16 | `0` |

## `popup`

| Property | Type | Default |
|---|---|---|
| `radius` | i16 | `8` |

## `label`

| Property | Type | Default |
|---|---|---|
| `text` | str |  |
| `font` | font_ref |  |
| `align` | one of `left` / `center` / `right` | `left` |
| `valign` | one of `top` / `center` / `bottom` | `top` |

## `value`

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `font` | font_ref |  |
| `show_unit` | bool | `True` |
| `warn_above` | f32 |  |
| `warn_color` | color |  |

## `button`

| Property | Type | Default |
|---|---|---|
| `text` | str |  |
| `text_on` | str | `` |
| `tag` | variable |  |
| `mode` | one of `momentary` / `toggle` / `set` / `reset` / `recipe_load` / `recipe_save` / `recipe_delete` |  |
| `value` | f32 | `1.0` |
| `icon` | image_ref |  |
| `confirm` | bool | `False` |
| `confirm_text` | str |  |

## `switch`

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `label_on` | str | `ON` |
| `label_off` | str | `OFF` |
| `bit` | i16 | `-1` |

## `led`

| Property | Type | Default |
|---|---|---|
| `shape` | one of `round` / `rect` | `round` |
| `tag` | variable |  |
| `color_on` | color |  |
| `color_off` | color |  |
| `blink_hz` | f32 | `0.0` |
| `bit` | i16 | `-1` |

## `slider`

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `min` | f32 | `0.0` |
| `max` | f32 | `100.0` |
| `step` | f32 | `1.0` |

## `bar`

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `min` | f32 | `0.0` |
| `max` | f32 | `100.0` |
| `orientation` | one of `vertical` / `horizontal` |  |

## `gauge`

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `min` | f32 | `0.0` |
| `max` | f32 | `100.0` |
| `start_angle` | i16 | `135` |
| `sweep` | i16 | `270` |
| `cache_background` | bool | `True` |
| `thickness` | i16 | `0` |
| `needle` | bool | `True` |
| `show_value` | bool | `True` |

## `image`

| Property | Type | Default |
|---|---|---|
| `src` | image_ref |  |
| `tint` | color |  |

## `nav`

| Property | Type | Default |
|---|---|---|
| `text` | str |  |
| `target` | str |  |
| `icon` | image_ref |  |

## `icon`

| Property | Type | Default |
|---|---|---|
| `src` | icon_ref |  |
| `color` | color |  |
| `tag` | variable |  |
| `src_active` | icon_ref |  |
| `color_active` | color |  |

## `input`

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `keypad` | one of `numeric` / `integer` / `alphanumeric` / `password` |  |
| `min` | f32 |  |
| `max` | f32 |  |
| `title` | str |  |
| `font` | font_ref |  |

## `trend`

| Property | Type | Default |
|---|---|---|
| `series` | list |  |
| `timespan_s` | i32 | `300` |
| `sample_ms` | i32 | `1000` |
| `autoscale` | bool | `True` |
| `min` | f32 |  |
| `max` | f32 |  |
| `grid` | bool | `True` |
| `show_legend` | bool | `True` |
| `scroll_mode` | bool | `True` |

## `alarm_table`

| Property | Type | Default |
|---|---|---|
| `filter` | one of `active` / `unacked` / `history` / `all` |  |
| `min_priority` | one of `info` / `warning` / `fault` / `critical` |  |
| `rows` | i16 | `8` |
| `show_time` | bool | `True` |
| `show_ack_button` | bool | `True` |
| `sort` | one of `newest_first` / `priority` | `newest_first` |
| `font` | font_ref |  |

## `trace`

A live oscilloscope-style curve of one variable, drawn as values arrive — the on-screen counterpart of the editor's Scope. For the recorded, multi-curve history see `trend`.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `color` | color |  |

## `logo`

The ctrl32 mark, drawn as a crisp vector at whatever size the rect gives it. Colourable; empty means the brand blue.

| Property | Type | Default |
|---|---|---|
| `color` | color |  |

## `recipe_table`

| Property | Type | Default |
|---|---|---|
| `font` | font_ref |  |

## `camera`

The live picture of one of the project's cameras - the text names the camera. Or the picture a vision block makes, live, when the text names the block as program.block (the picture after a filter, what a reader sees): the operator watches the camera and the prepared picture side by side while turning the settings.

(no properties of its own)

## `energy_flow`

Circles with an icon, a value and a name, joined by lines along which dots run in the direction the energy flows - solar, grid, battery and the house in one picture. Each node shows its own variable; each link has a variable whose sign says the direction (positive = from `from` to `to`) and whose size sets the speed; a link at zero stands still and dims. `max` is the value at which the dots run fastest.

| Property | Type | Default |
|---|---|---|
| `nodes` | list |  |
| `links` | list |  |
| `max` | f32 | `10.0` |
| `font` | font_ref |  |

## `bar_chart`

Columns. Either one column per variable of `series` (the rooms' temperatures, three phases, the consumers of a house), each in its own colour with its label under it, or - with `history` - the last samples of the widget's own variable, one column per `sample_ms` (each hour's energy today). The scale runs from `min` to `max`; the value is printed over each column when there is room.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `series` | list |  |
| `history` | bool | `False` |
| `sample_ms` | i32 | `3600000` |
| `bars` | i16 | `24` |
| `min` | f32 | `0.0` |
| `max` | f32 | `100.0` |
| `show_value` | bool | `True` |
| `font` | font_ref |  |

## `donut`

A ring. With a variable alone it fills from `min` to `max` (a battery's charge, a self-sufficiency in %) and prints the value in the middle; with `series` the ring is cut into slices in the ratio of their variables (what the house's power goes into), each in its colour. `thickness` is the ring's width in px (0 = a quarter of the radius).

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `series` | list |  |
| `min` | f32 | `0.0` |
| `max` | f32 | `100.0` |
| `thickness` | i16 | `0` |
| `show_value` | bool | `True` |
| `font` | font_ref |  |

## `sparkline`

A small curve of one variable's recent history - no axes, no grid - to sit in a card beside the number. It scales itself to what it shows unless `min` and `max` are given; `fill` shades the area under the curve.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `timespan_s` | i32 | `3600` |
| `sample_ms` | i32 | `30000` |
| `min` | f32 |  |
| `max` | f32 |  |
| `fill` | bool | `True` |

## `chart_item`

One part of a chart (a node, a link, a column, a slice) - written by the build from the chart's own lists, never by hand.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `color` | color |  |
| `label` | str |  |

## `checkbox`

A box with a tick and a label beside it. A tap toggles the variable - a BOOL, or one bit of an integer with `bit`. The accent fills the ticked box.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `text` | str |  |
| `bit` | i16 | `-1` |
| `font` | font_ref |  |

## `dropdown`

The selected option in a box with an arrow. A tap opens the list over the screen; a pick writes the option's NUMBER (0 = the first line) into the variable. `options` is one option per line.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `options` | str |  |
| `font` | font_ref |  |

## `roller`

A drum of options; the middle row is the value. Drag it, or tap above or below the middle, and the option's NUMBER is written into the variable. `rows` is how many rows are shown (odd, 3 to 9).

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `options` | str |  |
| `rows` | i16 | `3` |
| `font` | font_ref |  |

## `spinbox`

The value between a minus and a plus button: each tap moves it by `step` within `min` and `max`; a tap on the number opens the keypad.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `min` | f32 | `0.0` |
| `max` | f32 | `100.0` |
| `step` | f32 | `1.0` |
| `font` | font_ref |  |

## `button_matrix`

A grid of buttons of which one is selected - a segmented control (Auto / Manual / Off). A tap writes the button's NUMBER into the variable; the selected one is drawn in the accent. `buttons` is one caption per line, `columns` how many sit in a row (0 = all in one row).

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `buttons` | str |  |
| `columns` | i16 | `0` |
| `font` | font_ref |  |

## `arc`

A round knob: the track, the value as an arc in the accent and a handle at its end. Dragging along the arc writes the value between `min` and `max`; the number sits in the middle.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `min` | f32 | `0.0` |
| `max` | f32 | `100.0` |
| `start_angle` | i16 | `135` |
| `sweep` | i16 | `270` |
| `thickness` | i16 | `0` |
| `show_value` | bool | `True` |
| `font` | font_ref |  |

## `table`

Rows of cells. Each row is its `cells` text, the cells separated by a vertical bar; a row with a variable shows its value with the unit as its last cell. `header` (cells separated the same way) is the first row, drawn in the accent.

| Property | Type | Default |
|---|---|---|
| `header` | str |  |
| `rows` | list |  |
| `font` | font_ref |  |

## `scale`

A straight scale from `min` to `max` with `major` numbered ticks and `minor` ticks between each pair. With a variable a pointer in the accent shows where its value sits.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `min` | f32 | `0.0` |
| `max` | f32 | `100.0` |
| `major` | i16 | `5` |
| `minor` | i16 | `4` |
| `orientation` | one of `horizontal` / `vertical` | `horizontal` |
| `font` | font_ref |  |

## `spinner`

A turning arc that says "wait". With a variable it turns only while the variable is true and is empty otherwise. `period_ms` is one turn.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `period_ms` | i16 | `1000` |
| `thickness` | i16 | `0` |

## `anim_image`

A picture made of `frames` (images of the project). Without a variable it shows them one after another, `period_ms` each; with a variable the variable's value picks the frame (0 = the first) - a motor drawn stopped, running or faulted.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `frames` | list |  |
| `period_ms` | i16 | `500` |

## `line`

A line through `points` (x, y pairs in the widget's own frame), in the fg colour, `width` px wide; `closed` joins the last point to the first.

| Property | Type | Default |
|---|---|---|
| `points` | list |  |
| `width` | i16 | `2` |
| `closed` | bool | `False` |

## `shape`

A rectangle (with `radius` corners) or an ellipse that fills the widget: filled with bg when `fill` is on, outlined in fg `border_width` px wide.

| Property | Type | Default |
|---|---|---|
| `shape` | one of `rect` / `ellipse` | `rect` |
| `fill` | bool | `True` |
| `border_width` | i16 | `1` |
| `radius` | i16 | `0` |

## `qrcode`

A QR code of `text` (a web address, a WiFi login, a manual's link), as large as the widget allows, fg on bg.

| Property | Type | Default |
|---|---|---|
| `text` | str |  |

## `scatter`

Points of recent pairs: x is the widget's variable, y each series' variable, sampled together every `sample_ms`; the last `points` pairs are shown. `x_min`/`x_max` and `min`/`max` are the two axes.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `series` | list |  |
| `x_min` | f32 | `0.0` |
| `x_max` | f32 | `100.0` |
| `min` | f32 | `0.0` |
| `max` | f32 | `100.0` |
| `sample_ms` | i32 | `1000` |
| `points` | i16 | `60` |

## `tileview`

Pages (its children) switched by a swipe to the left or right, with dots under them. With a variable the variable holds the page number - a swipe writes it, a program can turn the page.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `active` | i16 | `0` |

## `window`

A body with a title bar (`text`, the accent). Its children sit under the bar. With a variable the bar carries an X that writes the variable false - give the window `visible_if` the same variable and the X closes it.

| Property | Type | Default |
|---|---|---|
| `text` | str |  |
| `tag` | variable |  |
| `bar_height` | i16 | `32` |
| `font` | font_ref |  |

## `menu`

Rows, each with an optional icon. A row with a `target` opens that screen; a row with a `value` writes it into the menu's variable and is drawn selected while the variable holds it.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `items` | list |  |
| `row_height` | i16 | `40` |
| `font` | font_ref |  |

## `calendar`

A month. The variable is a date written as YYYYMMDD (20261015); its day is drawn in the accent, a tap on another day writes it, the arrows in the header change the month shown.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `font` | font_ref |  |

## `textarea`

Text over several lines, wrapped at the widget's width (a new line in the text starts a new line). With a text (STRING) variable - a Linux device - it shows the variable, and with `editable` a tap opens the keyboard.

| Property | Type | Default |
|---|---|---|
| `text` | str |  |
| `tag` | variable |  |
| `editable` | bool | `False` |
| `align` | one of `left` / `center` / `right` | `left` |
| `font` | font_ref |  |

## `rich_text`

One paragraph made of `spans`, each with its own colour and font - a word in red, a value in a larger face; a span with a variable shows its live value with the unit. The spans flow on and wrap at the widget's width.

| Property | Type | Default |
|---|---|---|
| `spans` | list |  |

## `wheel`

A ring of icons with their captions - the home screen of a round glass with a knob. The SELECTED item sits at 12 o'clock and the ring turns to bring the next one there: a knob turn, a drag along the ring or a tap on an icon selects, and the item's `value` (its index when it has none) is written to the variable at once; the selected item's caption is drawn in the centre. A knob press, a tap on the centre or a second tap on the selected icon ACTIVATES it: an item with a `target` opens that screen.

| Property | Type | Default |
|---|---|---|
| `tag` | variable |  |
| `items` | list |  |
| `icon_size` | i16 | `40` |
| `font` | font_ref |  |

---

**Looking for the function blocks?** They have their own reference, grouped by what they do: see [Function blocks](blocks.md).

