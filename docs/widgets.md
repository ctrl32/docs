<!-- AUTOMATICALLY GENERATED from schema/visu-schema.yaml -->

# Widgets

Schema version: **27**

## Common properties (widget_base)

| Property | Type | Default |
|---|---|---|
| `id` | str |  |
| `x` | i16 |  |
| `y` | i16 |  |
| `w` | i16 |  |
| `h` | i16 |  |
| `anchor_x` | WidgetAnchorX | `start` |
| `anchor_y` | WidgetAnchorX | `start` |
| `margin` | i16 | `0` |
| `style` | style_ref |  |
| `visible_if` | tag_ref |  |
| `enabled_if` | tag_ref |  |
| `children` | list |  |
| `state` | map |  |
| `move` | map |  |
| `animations` | list |  |

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
| `align` | LabelAlign | `left` |

## `value`

| Property | Type | Default |
|---|---|---|
| `tag` | tag_ref |  |
| `font` | font_ref |  |
| `show_unit` | bool | `True` |
| `warn_above` | f32 |  |
| `warn_color` | color |  |

## `button`

| Property | Type | Default |
|---|---|---|
| `text` | str |  |
| `tag` | tag_ref |  |
| `mode` | ButtonMode |  |
| `value` | f32 | `1.0` |
| `icon` | image_ref |  |
| `confirm` | bool | `False` |
| `confirm_text` | str |  |

## `switch`

| Property | Type | Default |
|---|---|---|
| `tag` | tag_ref |  |
| `label_on` | str | `ON` |
| `label_off` | str | `OFF` |
| `bit` | i16 | `-1` |

## `led`

| Property | Type | Default |
|---|---|---|
| `shape` | LedShape | `round` |
| `tag` | tag_ref |  |
| `color_on` | color |  |
| `color_off` | color |  |
| `blink_hz` | f32 | `0.0` |
| `bit` | i16 | `-1` |

## `slider`

| Property | Type | Default |
|---|---|---|
| `tag` | tag_ref |  |
| `min` | f32 | `0.0` |
| `max` | f32 | `100.0` |
| `step` | f32 | `1.0` |

## `bar`

| Property | Type | Default |
|---|---|---|
| `tag` | tag_ref |  |
| `min` | f32 | `0.0` |
| `max` | f32 | `100.0` |
| `orientation` | BarOrientation |  |

## `gauge`

| Property | Type | Default |
|---|---|---|
| `tag` | tag_ref |  |
| `min` | f32 | `0.0` |
| `max` | f32 | `100.0` |
| `start_angle` | i16 | `135` |
| `sweep` | i16 | `270` |
| `cache_background` | bool | `True` |
| `thickness` | i16 | `0` |
| `needle` | bool | `True` |

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
| `tag` | tag_ref |  |
| `src_active` | icon_ref |  |
| `color_active` | color |  |

## `input`

| Property | Type | Default |
|---|---|---|
| `tag` | tag_ref |  |
| `keypad` | InputKeypad |  |
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
| `filter` | AlarmTableFilter |  |
| `min_priority` | AlarmPriority |  |
| `rows` | i16 | `8` |
| `show_time` | bool | `True` |
| `show_ack_button` | bool | `True` |
| `sort` | AlarmTableSort | `newest_first` |
| `font` | font_ref |  |

## `trace`

| Property | Type | Default |
|---|---|---|
| `tag` | tag_ref |  |
| `color` | color |  |

## `logo`

| Property | Type | Default |
|---|---|---|
| `color` | color |  |

---

**Looking for the function blocks?** They have their own reference, grouped by what they do: see [Function blocks](blocks.md).

