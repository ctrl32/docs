# Home automation

Twelve blocks for a house: the wall button and what it drives. They live
in the `home` block library that ships with the editor, and the Toolbox
lists them under **Home** the moment a project uses the library (*File →
Libraries*, or `libraries: [ libraries/home.yaml ]` in the project file).
Every one of them is written in ST, the way you write your own blocks,
so you can open it, read it and copy it into a block of your own.

The idea behind the family is the **wall button**: one push-button on
the wall does everything a room needs. A short click switches a light,
a long press dims it, a double click sets a scene. The blocks below
understand that button and speak to lights, blinds and heating.

All times are `TIME` parameters (`T#400ms`, `T#3m`) and all of them
measure real milliseconds, never cycles. The defaults are the values a
house wants; the examples on this page use short ones so the pictures
and the tests fit in seconds.

![The lights of the shipped example: a PUSHBUTTON drives a TOGGLE, another one a STAIRLIGHT](img/home-lights.webp){: .sb-center}

---

## PUSHBUTTON — short, long

**Tells a short click from a long press on one wall contact.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `IN` | input, bool | the wall contact, TRUE while pressed |
| `T_LONG` | parameter, T#400ms | held longer than this = a long press |
| `T_DOUBLE` | parameter, T#300ms | two clicks closer than this belong together |
| `SHORT` | output, bool | ONE cycle after a single short click |
| `LONG` | output, bool | TRUE from T_LONG until the finger lifts |

`SHORT` waits `T_DOUBLE` after the release before it fires, so a double
click never counts as two shorts. A long press makes no `SHORT` at all.

```iecst
PROGRAM LIGHTS
VAR
  b_kitchen : PUSHBUTTON;
  l_kitchen : TOGGLE;
END_VAR
  b_kitchen(IN := btn_kitchen);
  l_kitchen(TRIG := b_kitchen.SHORT, SET := all_on, RESET := all_off);
  light_kitchen := l_kitchen.Q;
END_PROGRAM
```

## MULTICLICK — double, count

**Counts the clicks of a burst.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `IN` | input, bool | the wall contact |
| `T_DOUBLE` | parameter, T#300ms | the gap that ends a burst |
| `DOUBLE` | output, bool | one cycle when the burst had exactly two clicks |
| `CLICKS` | output, INT | the count of the burst that just ended, for one cycle; 0 otherwise |

A scene selector counts on `CLICKS`: one click the reading lamp, two the
whole room, three everything off.

## TOGGLE — the light switch

**Every rising edge of TRIG flips Q; SET and RESET are the central commands.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `TRIG` | input, bool | the button's SHORT |
| `SET` | input, bool | an edge switches on (all lights on) |
| `RESET` | input, bool | an edge switches off (leaving the house) |
| `Q` | output, bool | the light |

## STAIRLIGHT — the staircase light

**A pulse lights Q for PT; another pulse restarts the time; WARN blinks before the end.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `TRIG` | input, bool | the button (any edge starts or restarts) |
| `OFF` | input, bool | an edge ends it now |
| `PERMANENT` | input, bool | holds Q while TRUE (cleaning the stairs) |
| `PT` | parameter, T#3m | how long the light stays |
| `T_WARN` | parameter, T#30s | the last part of PT during which WARN blinks |
| `Q` | output, bool | the light |
| `WARN` | output, bool | blinks at 1 Hz in the last T_WARN; drive a second lamp or the same one through an OR |

## DIMMER — one button dims

**A short click switches between off and the remembered level; a long press ramps.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `BTN` | input, bool | the wall contact, straight in (the block has its own PUSHBUTTON) |
| `ON` | input, bool | an edge switches on to the remembered level |
| `OFF` | input, bool | an edge switches off |
| `SET` | input, number | applies a level when it changes (a scene, a slider) |
| `MIN` | parameter, 10 | the lowest level a long press ramps to |
| `MAX` | parameter, 100 | the highest |
| `T_RAMP` | parameter, T#4s | the time from 0 to 100 % |
| `LEVEL` | output, number | 0..100 %, ramping |
| `Q` | output, bool | LEVEL above zero |

The first long press ramps **up**, the next one **down**; the level
where the finger lifted is remembered and a short click comes back to
it. `LEVEL` moves at 100 % per `T_RAMP`, so a 0–10 V output or a PWM
lamp fades instead of jumping.

## PWM — a level into a slow square wave

**Q is TRUE for IN percent of every PERIOD.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `IN` | input, number | 0..100 % |
| `PERIOD` | parameter, T#10s | the period |
| `Q` | output, bool | the relay or the SSR |

For a floor-heating valve or a heater relay a period of seconds to
minutes is right. For a lamp use a PWM output of the board instead: the
`pwm_out` peripheral takes the DIMMER's `LEVEL` directly.

## BLINDS — a roller shutter with two keys

**UP and DOWN run the motor, the same key stops, the other key reverses, SAFETY drives up and locks.**

![The blinds of the shipped example: BLINDS and TRAVEL](img/home-blinds.webp){: .sb-center}

| Pin | Type | Meaning |
|:---|:---:|:---|
| `UP` | input, bool | the up key (an edge) |
| `DOWN` | input, bool | the down key (an edge) |
| `STOP` | input, bool | an edge stops |
| `SAFETY` | input, bool | wind or frost: drives up once and locks both keys while TRUE |
| `T_RUN` | parameter, T#25s | the full travel time; the motor runs one second longer so the end switch is reached |
| `T_REVERSE` | parameter, T#500ms | the pause between two directions, so the motor never reverses under load |
| `M_UP` | output, bool | the motor relay up |
| `M_DOWN` | output, bool | the motor relay down |

The two outputs are never TRUE together. Wire the end switches into the
motor as the manufacturer says — the block only times the run.

## TRAVEL — where the blind is

**Integrates the motor time into a position, 0 = up, 100 = down.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `M_UP` | input, bool | the motor relay up (from BLINDS) |
| `M_DOWN` | input, bool | the motor relay down |
| `T_RUN` | parameter, T#25s | the full travel time — the same number as in BLINDS |
| `POS` | output, number | 0..100 % |
| `MOVING` | output, bool | a motor runs |

A full run to either end resets the position exactly; between them it is
the motor time, good to a few percent. Show `POS` on a screen or use it
to decide a scene.

## PRESENCE — somebody is here

**Holds PRESENT for T_HOLD after the last motion.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `MOTION` | input, bool | the PIR sensor |
| `ENABLE` | input, bool | FALSE = the output stays off (a sleeping room at night) |
| `T_HOLD` | parameter, T#5m | how long after the last motion |
| `PRESENT` | output, bool | drive a light through an AND with TWILIGHT's DARK |

## TWILIGHT — it is dark

**DARK switches with hysteresis around THRESHOLD, filtered by T_FILTER so a cloud does not switch the garden.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `LUX` | input, number | the light sensor |
| `THRESHOLD` | parameter, 20 | the level |
| `HYST` | parameter, 5 | half the band: dark below THRESHOLD − HYST, light above THRESHOLD + HYST |
| `T_FILTER` | parameter, T#30s | the value must stay on one side this long |
| `DARK` | output, bool | |

## THERMOSTAT — a room

**Two-point heating with three setpoints, a boost and a window pause.**

![The room of the shipped example: PRESENCE, TWILIGHT, THERMOSTAT and DAYTIME](img/home-room.webp){: .sb-center}

| Pin | Type | Meaning |
|:---|:---:|:---|
| `PV` | input, number | the room temperature |
| `MODE` | input, INT | 0 = frost protection, 1 = eco, 2 = comfort |
| `WINDOW` | input, bool | the window contact: open longer than T_WINDOW pauses the heating |
| `BOOST` | input, bool | an edge raises the setpoint by 2 degrees for T_BOOST |
| `SP_COMFORT` | parameter, 21 | the comfort setpoint |
| `SP_ECO` | parameter, 18 | the eco setpoint |
| `SP_FROST` | parameter, 6 | the frost-protection setpoint |
| `HYST` | parameter, 0.3 | the switching band, half above and half below SP |
| `T_BOOST` | parameter, T#30m | the boost time |
| `T_WINDOW` | parameter, T#2m | an open window shorter than this is ignored |
| `HEAT` | output, bool | the valve or the relay |
| `SP` | output, number | the setpoint in force, for the screen |

Drive `MODE` from a DAYTIME block (comfort by day, eco at night) or from
a screen button; a PRESENCE block can drop it to eco while nobody is
home.

## DAYTIME — a window in the day

**Q while the clock is inside FROM..TO on one of DAYS.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `ENABLE` | input, bool | |
| `MINUTES` | input, INT | the minute of the day — bind `SYS.MINUTE_OF_DAY` |
| `WEEKDAY` | input, INT | 1 = Monday .. 7 = Sunday — bind `SYS.WEEKDAY` |
| `FROM` | parameter, 390 | the first minute (06:30) |
| `TO` | parameter, 1320 | the minute the window ends (22:00) |
| `DAYS` | parameter, 127 | a bit per day, Monday = 1, Sunday = 64; 127 = every day, 31 = Monday to Friday |
| `Q` | output, bool | |

A window over midnight (`FROM` 1320, `TO` 390) works as you expect. The
clock is the device's, in the project's time zone (*clock: tz*); while
the device has no valid time (`SYS.TIME_VALID` FALSE) the minute reads 0
and the weekday 0, so `Q` stays FALSE rather than guessing. See the
system variables in [Variables](variables.md).

---

## How many fit in one program

The timers and edge detectors inside these blocks are the runtime's own
(TON, TOF, R_TRIG ...), and a program holds **32** of them. PUSHBUTTON
uses 3, TOGGLE 3, STAIRLIGHT 4, DIMMER 6, BLINDS 5, MULTICLICK 2,
TWILIGHT 2, THERMOSTAT 2, PWM, TRAVEL and PRESENCE 1 each, DAYTIME
none. A house with many rooms is several programs — one per floor or
one per function (lights, blinds, heating), which is also how you want
to read it. The editor refuses a program that grows past the limit
and says so at the block.

## The example and the tests

`examples/home_blocks.prj32` is a small house on one screen: a kitchen
light with a wall button, a staircase light, a dimmed lamp, one blind
and a room with heating. Open it, start the simulation and press the
buttons on the screen.

Every block is held by a simulation test that presses the buttons in
milliseconds and expects the outputs — the same tests run before every
release, so a block's behaviour is a promise, not a description.
