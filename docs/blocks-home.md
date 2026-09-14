# Home automation

Twenty blocks for a house: the wall button and what it drives, the clock
and the sun. They live
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
| `T_TILT` | parameter, T#0s | venetian blinds: the motor time of one tilt step; 0 = a roller shutter |
| `T_LONG` | parameter, T#400ms | venetian blinds: a key held longer than this runs to the end |
| `M_UP` | output, bool | the motor relay up |
| `M_DOWN` | output, bool | the motor relay down |

The two outputs are never TRUE together. Wire the end switches into the
motor as the manufacturer says — the block only times the run.

With `T_TILT` at zero the block is a **roller shutter**: a click on a
key runs to the end. With `T_TILT` set it is a **venetian blind**: a
short click on a key turns the slats one step (the motor runs `T_TILT`),
a key held past `T_LONG` runs to the end, and a click during a run stops
it as before.

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

## SUNTIMES — today's sunrise and sunset

**The minutes of the local day the sun rises and sets at a place.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `DOY` | input, INT | the day of the year — bind `SYS.DAY_OF_YEAR` |
| `UTC_OFF` | input, INT | the device's offset to UTC in minutes, summer time included — bind `SYS.UTC_OFFSET` |
| `LAT` | parameter, 48.15 | latitude, degrees north |
| `LON` | parameter, 17.11 | longitude, degrees east |
| `SUNRISE` | output, INT | minute of the day, 0..1439 |
| `SUNSET` | output, INT | minute of the day |

The defaults are Bratislava. The block computes the standard
approximation, good to a few minutes; a polar night gives 0 and 0, a
midnight sun 0 and 1439. Show the two numbers on a screen or feed them
to a DAYTIME through variables.

## ASTRO — day and dark by the sun

**DAY between sunrise and sunset, DARK outside, each edge shifted by an offset.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `ENABLE` | input, bool | |
| `MINUTES` | input, INT | bind `SYS.MINUTE_OF_DAY` |
| `DOY` | input, INT | bind `SYS.DAY_OF_YEAR` |
| `UTC_OFF` | input, INT | bind `SYS.UTC_OFFSET` |
| `LAT`, `LON` | parameters | the place, as in SUNTIMES |
| `OFS_RISE` | parameter, 0 | minutes added to the sunrise (−30: the day starts half an hour before) |
| `OFS_SET` | parameter, 0 | minutes added to the sunset (+20: the garden light waits for real dusk) |
| `DAY` | output, bool | |
| `DARK` | output, bool | NOT DAY while enabled — the garden light, the blinds at dusk |

TWILIGHT measures the light where the sensor is; ASTRO knows it from
the calendar and needs no sensor. Both give a DARK, use the one you
have.

## SCHEDULE — two windows a day, a value

**VALUE is V_IN inside either window on the listed days and V_OUT outside.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `ENABLE` | input, bool | |
| `MINUTES` | input, INT | bind `SYS.MINUTE_OF_DAY` |
| `WEEKDAY` | input, INT | bind `SYS.WEEKDAY` |
| `DAYS` | input, INT | a bit per day, Monday = 1 .. Sunday = 64; 127 every day, 31 Monday to Friday |
| `FROM1`, `TO1` | parameters, 360, 480 | the first window, 06:00–08:00 |
| `FROM2`, `TO2` | parameters, 960, 1320 | the second, 16:00–22:00 |
| `V_IN` | parameter, 2 | the value inside — comfort for THERMOSTAT's MODE |
| `V_OUT` | parameter, 1 | the value outside — eco |
| `VALUE` | output, INT | |
| `Q` | output, bool | inside a window |

Wire `VALUE` into THERMOSTAT's `MODE` and the room heats by the clock.
A different weekend: a second SCHEDULE with `DAYS` 96 and a SEL block
on `Q`.

## SCENE — two channels, three scenes

**An APPLY edge sets A and B to the levels of scene SEL; OFF clears both.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `SEL` | input, INT | the scene, 1..3 (0 = off) |
| `APPLY` | input, bool | an edge applies it |
| `OFF` | input, bool | an edge sets both channels to 0 |
| `S1_A`, `S1_B` | parameters, 100, 100 | scene 1 |
| `S2_A`, `S2_B` | parameters, 60, 30 | scene 2 |
| `S3_A`, `S3_B` | parameters, 20, 0 | scene 3 |
| `A`, `B` | outputs, number | the two levels — into DIMMER's SET |

MULTICLICK's `CLICKS` into `SEL` and a GT block (`CLICKS > 0`) into
`APPLY` make one click scene 1, two clicks scene 2, three clicks scene
3 on one wall button. More channels: another SCENE on the same `SEL`
and `APPLY`.

## GATE — a garage door or a gate

**One impulse key cycles open – stop – close – stop; the photocell reverses a closing gate.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `TRIG` | input, bool | the impulse key (the remote, the keypad) |
| `OPEN` | input, bool | an edge opens; the same direction stops |
| `CLOSE` | input, bool | an edge closes |
| `SAFETY` | input, bool | the photocell or the safety edge: a closing gate reverses and stays open while TRUE |
| `T_RUN` | parameter, T#20s | the travel time; the motor runs one second longer |
| `T_REVERSE` | parameter, T#500ms | the pause before the other direction |
| `T_AUTO` | parameter, T#0s | a fully open gate closes by itself after this; 0 = never |
| `M_OPEN` | output, bool | |
| `M_CLOSE` | output, bool | |

The two outputs are never TRUE together. The gate drive's own safety
devices stay wired as the manufacturer says — the block is the key
logic, not the protection.

## VENT — the bathroom fan

**Runs with the light after a delay, runs on after it, runs on humidity, or by hand.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `LIGHT` | input, bool | the bathroom light |
| `HUM` | input, number | relative humidity, % |
| `MANUAL` | input, bool | an edge toggles the fan by hand |
| `T_DELAY` | parameter, T#2m | the light must be on this long first (a short visit runs no fan) |
| `T_RUNON` | parameter, T#10m | after the light went off |
| `T_MAX` | parameter, T#1h | the longest humidity or manual run |
| `H_ON` | parameter, 70 | humidity that starts the fan |
| `H_OFF` | parameter, 60 | humidity that ends the demand |
| `FAN` | output, bool | |
| `HUMID` | output, bool | the humidity demand, for a screen |

## CENTRAL — everything on, everything off, leaving

**ON and OFF edges make a pulse; LEAVE makes the off pulse T_LEAVE later.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `ON` | input, bool | an edge: ALL_ON pulses |
| `OFF` | input, bool | an edge: ALL_OFF pulses now |
| `LEAVE` | input, bool | an edge: ALL_OFF pulses after T_LEAVE — time to reach the door |
| `CANCEL` | input, bool | an edge forgets a pending LEAVE (so does ON) |
| `T_LEAVE` | parameter, T#30s | |
| `T_PULSE` | parameter, T#200ms | the pulse length |
| `ALL_ON` | output, bool | into TOGGLE's SET and DIMMER's ON |
| `ALL_OFF` | output, bool | into TOGGLE's RESET, STAIRLIGHT's OFF and DIMMER's OFF |

## ENERGY — kilowatt-hours from a power

**E counts kWh from a power in kW, once a second; COST is E times PRICE.**

| Pin | Type | Meaning |
|:---|:---:|:---|
| `P` | input, number | the power, kW (a meter's reading) |
| `RESET` | input, bool | an edge starts from 0 |
| `E_IN` | input, number | the count to continue from — bind the SAME variable as E |
| `PRICE` | parameter, 0.25 | per kWh |
| `E` | output, number | kWh |
| `COST` | output, number | |

The count lives in the variable bound to `E`: bind it to `E_IN` as
well and mark it retained (*Variables → retain*), and the counter
survives a restart. Without the `E_IN` wire the block counts one
second at a time and forgets.

## Standard functions in your own blocks

The blocks above are ST you can read. SUNTIMES uses the standard
functions `SIN`, `COS`, `TAN` and `ACOS`; `SQRT`, `ASIN`, `ATAN`,
`EXP`, `LN`, `LOG` and `EXPT(base, exponent)` are there as well, all on
REAL. See [Structured Text](st-language.md).

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
