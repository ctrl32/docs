<!-- AUTOMATICALLY GENERATED from schema/visu-schema.yaml -->

# Widgets

Schema version: **45** — the vocabulary of the project file. The compiled pack carries its own format number; error messages name whichever one they mean.

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

| Property | Type | Default |
|---|---|---|
| `radius` | i16 | `0` |

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

---

**Looking for the function blocks?** They have their own reference, grouped by what they do: see [Function blocks](blocks.md).

