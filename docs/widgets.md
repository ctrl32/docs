<!-- AUTOMATICALLY GENERATED from schema/visu-schema.yaml -->

# Widgets

Schema version: **53** — the vocabulary of the project file. The compiled pack carries its own format number; error messages name whichever one they mean.

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

---

**Looking for the function blocks?** They have their own reference, grouped by what they do: see [Function blocks](blocks.md).

