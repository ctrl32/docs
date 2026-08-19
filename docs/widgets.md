<!-- AUTOMATICALLY GENERATED from schema/visu-schema.yaml -->

# Widgets

Schema version: **20**

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

# Function blocks (logic)

A program = a list of block instances in execution order. A pin input is a tag or a constant, an output writes into a tag. Times are always in ms.

## `TON`

On-delay timer — Q switches on once IN has been held continuously for PT ms.

| Pin | Direction | Type |
|---|---|---|
| `IN` | input | bool |
| `Q` | output | bool |
| `ET` | output | f32 |
| `PT` (ms) | parameter | f32, default `1000` |

## `TOF`

Off-delay timer — Q stays on for another PT ms after IN drops.

| Pin | Direction | Type |
|---|---|---|
| `IN` | input | bool |
| `Q` | output | bool |
| `ET` | output | f32 |
| `PT` (ms) | parameter | f32, default `1000` |

## `TP`

Pulse — a rising edge of IN fires Q for exactly PT ms (non-retriggerable).

| Pin | Direction | Type |
|---|---|---|
| `IN` | input | bool |
| `Q` | output | bool |
| `ET` | output | f32 |
| `PT` (ms) | parameter | f32, default `1000` |

## `CTU`

Up counter — a rising edge of CU increments, R resets, Q = CV >= PV.

| Pin | Direction | Type |
|---|---|---|
| `CU` | input | bool |
| `R` | input | bool |
| `Q` | output | bool |
| `CV` | output | f32 |
| `PV` | parameter | f32, default `10` |

## `CTD`

Down counter — a rising edge of CD decrements, LD loads CV = PV, Q = CV <= 0.

| Pin | Direction | Type |
|---|---|---|
| `CD` | input | bool |
| `LD` | input | bool |
| `Q` | output | bool |
| `CV` | output | f32 |
| `PV` | parameter | f32, default `10` |

## `R_TRIG`

Rising edge — Q is TRUE for one cycle after CLK rises.

| Pin | Direction | Type |
|---|---|---|
| `CLK` | input | bool |
| `Q` | output | bool |

## `F_TRIG`

Falling edge — Q is TRUE for one cycle after CLK drops.

| Pin | Direction | Type |
|---|---|---|
| `CLK` | input | bool |
| `Q` | output | bool |

## `SR`

Flip-flop with SET priority.

| Pin | Direction | Type |
|---|---|---|
| `S1` | input | bool |
| `R` | input | bool |
| `Q1` | output | bool |

## `RS`

Flip-flop with RESET priority.

| Pin | Direction | Type |
|---|---|---|
| `S` | input | bool |
| `R1` | input | bool |
| `Q1` | output | bool |

## `SCALE`

Linear scaling of IN from IN_MIN..IN_MAX to OUT_MIN..OUT_MAX.

| Pin | Direction | Type |
|---|---|---|
| `IN` | input | f32 |
| `OUT` | output | f32 |
| `IN_MIN` | parameter | f32, default `0` |
| `IN_MAX` | parameter | f32, default `100` |
| `OUT_MIN` | parameter | f32, default `0` |
| `OUT_MAX` | parameter | f32, default `100` |

## `LIMIT`

Clamps IN into the MN..MX range.

| Pin | Direction | Type |
|---|---|---|
| `IN` | input | f32 |
| `OUT` | output | f32 |
| `MN` | parameter | f32, default `0` |
| `MX` | parameter | f32, default `100` |

## `HYST`

Comparator with hysteresis — Q switches on at IN >= ON, off at IN <= OFF.

| Pin | Direction | Type |
|---|---|---|
| `IN` | input | f32 |
| `Q` | output | bool |
| `ON` | parameter | f32, default `100` |
| `OFF` | parameter | f32, default `90` |

## `RAMP`

Rate limiter — OUT follows IN at most RATE units per second.

| Pin | Direction | Type |
|---|---|---|
| `IN` | input | f32 |
| `OUT` | output | f32 |
| `RATE` (1/s) | parameter | f32, default `10` |

## `PT1`

First-order filter — OUT approaches IN with time constant T ms.

| Pin | Direction | Type |
|---|---|---|
| `IN` | input | f32 |
| `OUT` | output | f32 |
| `T` (ms) | parameter | f32, default `1000` |

## `BLINK`

Blinker — while RUN, Q alternates T_ON ms on / T_OFF ms off.

| Pin | Direction | Type |
|---|---|---|
| `RUN` | input | bool |
| `Q` | output | bool |
| `T_ON` (ms) | parameter | f32, default `500` |
| `T_OFF` (ms) | parameter | f32, default `500` |

## `ADD`

OUT = IN1 + IN2 + IN3 + IN4 (unconnected inputs are 0).

| Pin | Direction | Type |
|---|---|---|
| `IN1` | input | f32 |
| `IN2` | input | f32 |
| `IN3` | input | f32 |
| `IN4` | input | f32 |
| `OUT` | output | f32 |

## `SUB`

OUT = IN1 - IN2.

| Pin | Direction | Type |
|---|---|---|
| `IN1` | input | f32 |
| `IN2` | input | f32 |
| `OUT` | output | f32 |

## `MUL`

OUT = IN1 * IN2.

| Pin | Direction | Type |
|---|---|---|
| `IN1` | input | f32 |
| `IN2` | input | f32 |
| `OUT` | output | f32 |

## `DIV`

OUT = IN1 / IN2; division by zero yields 0 (no crash).

| Pin | Direction | Type |
|---|---|---|
| `IN1` | input | f32 |
| `IN2` | input | f32 |
| `OUT` | output | f32 |

## `MIN`

OUT = the smaller of IN1, IN2.

| Pin | Direction | Type |
|---|---|---|
| `IN1` | input | f32 |
| `IN2` | input | f32 |
| `OUT` | output | f32 |

## `MAX`

OUT = the larger of IN1, IN2.

| Pin | Direction | Type |
|---|---|---|
| `IN1` | input | f32 |
| `IN2` | input | f32 |
| `OUT` | output | f32 |

## `ABS`

OUT = |IN|.

| Pin | Direction | Type |
|---|---|---|
| `IN` | input | f32 |
| `OUT` | output | f32 |

## `AND`

Q = IN1 AND IN2.

| Pin | Direction | Type |
|---|---|---|
| `IN1` | input | bool |
| `IN2` | input | bool |
| `Q` | output | bool |

## `OR`

Q = IN1 OR IN2.

| Pin | Direction | Type |
|---|---|---|
| `IN1` | input | bool |
| `IN2` | input | bool |
| `Q` | output | bool |

## `XOR`

Q = IN1 XOR IN2.

| Pin | Direction | Type |
|---|---|---|
| `IN1` | input | bool |
| `IN2` | input | bool |
| `Q` | output | bool |

## `NOT`

Q = NOT IN.

| Pin | Direction | Type |
|---|---|---|
| `IN` | input | bool |
| `Q` | output | bool |

## `GT`

Q = IN1 > IN2.

| Pin | Direction | Type |
|---|---|---|
| `IN1` | input | f32 |
| `IN2` | input | f32 |
| `Q` | output | bool |

## `GE`

Q = IN1 >= IN2.

| Pin | Direction | Type |
|---|---|---|
| `IN1` | input | f32 |
| `IN2` | input | f32 |
| `Q` | output | bool |

## `LT`

Q = IN1 < IN2.

| Pin | Direction | Type |
|---|---|---|
| `IN1` | input | f32 |
| `IN2` | input | f32 |
| `Q` | output | bool |

## `LE`

Q = IN1 <= IN2.

| Pin | Direction | Type |
|---|---|---|
| `IN1` | input | f32 |
| `IN2` | input | f32 |
| `Q` | output | bool |

## `EQ`

Q = |IN1 - IN2| <= EPS (comparison with tolerance).

| Pin | Direction | Type |
|---|---|---|
| `IN1` | input | f32 |
| `IN2` | input | f32 |
| `Q` | output | bool |
| `EPS` | parameter | f32, default `0` |

## `SEL`

OUT = G ? IN1 : IN0 (binary selector as in IEC).

| Pin | Direction | Type |
|---|---|---|
| `G` | input | bool |
| `IN0` | input | f32 |
| `IN1` | input | f32 |
| `OUT` | output | f32 |

## `MOTOR`

Start/stop with feedback: FB must confirm running within T_FB ms, otherwise FAULT (latched, command dropped). ACK acknowledges only at standstill. STOP overrides START.

| Pin | Direction | Type |
|---|---|---|
| `START` | input | bool |
| `STOP` | input | bool |
| `FB` | input | bool |
| `ACK` | input | bool |
| `CMD` | output | bool |
| `FAULT` | output | bool |
| `T_FB` (ms) | parameter | f32, default `3000` |

## `VALVE`

Valve: OPEN opens, CLOSE has priority; FB (end position) must arrive within T_FB ms, otherwise a latched FAULT; ACK acknowledges.

| Pin | Direction | Type |
|---|---|---|
| `OPEN` | input | bool |
| `CLOSE` | input | bool |
| `FB` | input | bool |
| `ACK` | input | bool |
| `CMD` | output | bool |
| `FAULT` | output | bool |
| `T_FB` (ms) | parameter | f32, default `5000` |

## `PID`

PID controller: OUT = KP·e + I + D within OUT_MIN..OUT_MAX (anti-windup — the integrator never runs beyond the limits). AUTO=FALSE: OUT follows MAN and the integrator tracks it — switching back to AUTO is bumpless. TI=0 disables the I term, TD=0 the D term (derivative from PV with a TD/8 filter, not from the error — a setpoint step does not kick the output). LIM signals saturation.

| Pin | Direction | Type |
|---|---|---|
| `SP` | input | f32 |
| `PV` | input | f32 |
| `MAN` | input | f32 |
| `AUTO` | input | bool |
| `OUT` | output | f32 |
| `LIM` | output | bool |
| `KP` | parameter | f32, default `1` |
| `TI` (s) | parameter | f32, default `60` |
| `TD` (s) | parameter | f32, default `0` |
| `OUT_MIN` | parameter | f32, default `0` |
| `OUT_MAX` | parameter | f32, default `100` |

## `MC_POWER`

PLCopen: axis on/off. Status = axis ready and operational.

_Bound to an axis (AXIS) — not to a tag._

| Pin | Direction | Type |
|---|---|---|
| `Enable` | input | bool |
| `Status` | output | bool |
| `Error` | output | bool |

## `MC_MOVEVELOCITY`

PLCopen: constant-velocity motion (i550). Ramps up to Velocity using the drive ramp; InVelocity when reached. Direction 0 = forward, 1 = reverse.

_Bound to an axis (AXIS) — not to a tag._

| Pin | Direction | Type |
|---|---|---|
| `Execute` | input | bool |
| `Velocity` | input | f32 |
| `InVelocity` | output | bool |
| `Busy` | output | bool |
| `Direction` | parameter | f32, default `0` |

## `MC_STOP`

PLCopen: controlled stop along the decel ramp (Decel in seconds).

_Bound to an axis (AXIS) — not to a tag._

| Pin | Direction | Type |
|---|---|---|
| `Execute` | input | bool |
| `Done` | output | bool |
| `Busy` | output | bool |
| `Decel` (s) | parameter | f32, default `5` |

## `MC_RESET`

PLCopen: axis fault acknowledge (fault reset).

_Bound to an axis (AXIS) — not to a tag._

| Pin | Direction | Type |
|---|---|---|
| `Execute` | input | bool |
| `Done` | output | bool |
| `Error` | output | bool |

## `MC_READACTVEL`

PLCopen: reads the actual axis velocity.

_Bound to an axis (AXIS) — not to a tag._

| Pin | Direction | Type |
|---|---|---|
| `Enable` | input | bool |
| `Velocity` | output | f32 |
| `Valid` | output | bool |

## `MC_READSTATUS`

PLCopen: axis state — Running, Error (fault).

_Bound to an axis (AXIS) — not to a tag._

| Pin | Direction | Type |
|---|---|---|
| `Enable` | input | bool |
| `Running` | output | bool |
| `Error` | output | bool |

## `MC_MOVEABS`

PLCopen: move to an absolute position (POWERSTEP01 backend).

_Bound to an axis (AXIS) — not to a tag._

| Pin | Direction | Type |
|---|---|---|
| `Execute` | input | bool |
| `Position` | input | f32 |
| `Velocity` | input | f32 |
| `Done` | output | bool |
| `Busy` | output | bool |
| `Accel` | parameter | f32, default `100` |
| `Decel` | parameter | f32, default `100` |

## `MC_MOVEREL`

PLCopen: move by a relative distance (POWERSTEP01 backend).

_Bound to an axis (AXIS) — not to a tag._

| Pin | Direction | Type |
|---|---|---|
| `Execute` | input | bool |
| `Distance` | input | f32 |
| `Velocity` | input | f32 |
| `Done` | output | bool |
| `Busy` | output | bool |
| `Accel` | parameter | f32, default `100` |
| `Decel` | parameter | f32, default `100` |

## `MC_HOME`

PLCopen: homing run (POWERSTEP01 backend).

_Bound to an axis (AXIS) — not to a tag._

| Pin | Direction | Type |
|---|---|---|
| `Execute` | input | bool |
| `Done` | output | bool |
| `Busy` | output | bool |

## `MC_READACTPOS`

PLCopen: reads the actual axis position.

_Bound to an axis (AXIS) — not to a tag._

| Pin | Direction | Type |
|---|---|---|
| `Enable` | input | bool |
| `Position` | output | f32 |
| `Valid` | output | bool |

## `CO_CIA402`

CANopen: the CiA402 state-machine core over an axis — building block for MC_* and the DRIVE_i550 composite. Ready = operation_enabled.

_Bound to an axis (AXIS) — not to a tag._

| Pin | Direction | Type |
|---|---|---|
| `Enable` | input | bool |
| `Ready` | output | bool |
| `Fault` | output | bool |

## `CO_SDOWRITE`

CANopen: writes an object on the axis — at STARTUP only (packbuild compiles it into an SdoInitRec, never in the cycle). INDEX/SUB/SIZE parameterize the object.

_Bound to an axis (AXIS) — not to a tag._

| Pin | Direction | Type |
|---|---|---|
| `IN` | input | f32 |
| `INDEX` | parameter | f32, default `0` |
| `SUB` | parameter | f32, default `0` |
| `VALUE` | parameter | f32, default `0` |
| `SIZE` | parameter | f32, default `1` |

## `CO_SDOREAD`

CANopen: reads an object from the axis at startup. INDEX/SUB select the object.

_Bound to an axis (AXIS) — not to a tag._

| Pin | Direction | Type |
|---|---|---|
| `OUT` | output | f32 |
| `INDEX` | parameter | f32, default `0` |
| `SUB` | parameter | f32, default `0` |

## `CO_RAMPTIME`

CiA402: ACC/DEC ramp times in seconds (0 -> target rpm). Written to the drive (0x6048/0x6049) ONLY when the axis is at standstill and only on change — the cycle never touches SDO while running. For the i550 with WEBview ACC/DEC inputs.

_Bound to an axis (AXIS) — not to a tag._

| Pin | Direction | Type |
|---|---|---|
| `ACC` | input | f32 |
| `DEC` | input | f32 |
| `REF` | input | f32 |

## `IR_SEND`

Sends an infrared code from the project's IR key table on the rising edge of Execute. KEY = table index. Done pulses while Execute holds after a successful transmit; Error = no IR transmitter configured or KEY out of range.

| Pin | Direction | Type |
|---|---|---|
| `Execute` | input | bool |
| `Done` | output | bool |
| `Error` | output | bool |
| `KEY` | parameter | f32, default `0` |

## `SMS_SEND`

Sends an SMS from the project's message table (gsm: messages) on the rising edge of Execute. MSG = message index (0-7 as numbered on the modem page), NUM = recipient: 0 = every configured number, 1-4 = one number (#1-#4 on the modem page). Done holds while Execute holds after the SMS was queued; Error = no modem service, an empty message/number or the service is busy (retry on the next edge).

| Pin | Direction | Type |
|---|---|---|
| `Execute` | input | bool |
| `Done` | output | bool |
| `Error` | output | bool |
| `MSG` | parameter | f32, default `0` |
| `NUM` | parameter | f32, default `0` |

## `GSM_INFO`

Modem service state for the program: Ready = registered on the network (SMS possible), Signal = last +CSQ reading 0-31 (0 also while not measured yet — the modem polls it every 30 s). Without a configured modem both outputs stay 0. The v36 status tag stays the screen-facing path; this block is the logic-facing one (interlocks, retry gating).

| Pin | Direction | Type |
|---|---|---|
| `Enable` | input | bool |
| `Ready` | output | bool |
| `Signal` | output | f32 |

## `MOVE`

OUT = IN — the IEC assignment as a block. In the LD editor it is the plain EN result box (commit a value while the rung conducts), in FBD a tag-to-tag copy.

| Pin | Direction | Type |
|---|---|---|
| `IN` | input | f32 |
| `OUT` | output | f32 |

