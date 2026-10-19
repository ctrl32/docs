# What's new

Every release replaces the previous one — the editor's update check
offers it automatically, and a project saved in an older version always
opens in a newer one.

Versions are plain numbers in the form `generation.feature.build`:
the last field counts builds, the middle one grows with new
capabilities, the first one practically never moves.

## ctrl32 is free (19 October 2026)

## 1.06.000

The first release of free ctrl32 (see above) - and a new line: every
device takes a new runtime (over the network or over USB, as always -
[Download to the board](deploy.md)) before it accepts a project saved by
this editor.

- **PLCopen Motion Control Part 1, whole and exact** ([Motion
  blocks](blocks-motion.md)): every block of the specification with its
  names, inputs, outputs and the standard `ErrorID` table; the axis state
  machine, buffer modes and blending, override, the parameter numbers; a
  Linux device runs the whole library, a panel the part a frequency drive
  needs. The old block names stay as aliases - a saved project opens and
  builds as it did.
- **Cams, profiles and cam switches** on a Linux device: the new **Motion**
  item of the device tree opens a page where the tables are made - a cam
  (master position to slave position, periodic or not), a profile (time to
  position, velocity or acceleration) and a cam switch table (tracks of an
  output over a position range, with lead and lag). A block names its table
  by number within its kind. See [the Motion
  page](blocks-motion.md#the-motion-page).
- **An axis counts in revolutions per minute** when its project says so
  (`velocity_per: rpm`): positions in increments, speeds in rpm - the shape
  every drive project was written in.
- **Every output of a block in Ladder**: `Active`, `CommandAborted`, `Error`
  and `ErrorID` of a motion block can be bound on the rung like `Done` and
  `Busy` (a box used to show two outputs only).
- **A new row in the VAR table is a BOOL** - the type most variables of a
  control program are; before, it was a REAL and had to be changed on
  every row.
- **The variable picker says why**: a variable the pin cannot take (a REAL
  on a contact, a BOOL on a numeric pin) is listed greyed with the reason,
  and a name the language does not take (a diacritic, a space, a digit
  first) is said under the field and in the status bar instead of "name
  taken" or silence.
- **A freshly placed chart shows a sample** of its shape on the editor
  canvas (offline a chart used to be an empty frame).
- **ONLINE over WiFi holds through a slow hop**: the editor ends the online
  session only after three seconds of silence, not after one missed poll.
- **A car cockpit example** ([Car cockpit](example-car-cockpit.md)): an
  instrument cluster on the MaTouch ESP32-P4 7" on a J1939 vehicle bus -
  the gauges and lamps, six round instruments with needles for the oils
  and the pressures, the control units and every signal they send, the
  engine's fault code in words, the driver's parameters, and a drive cycle
  that runs it all without a vehicle.

## 1.05.000

A new line: every device takes a new runtime (over the network or over
USB, as always - [Download to the board](deploy.md)) before it accepts a
project saved by this editor, and the editor grows the round below.

- **Twenty new widgets** complete the visualization library
  ([Visualisation](visualisation.md)): checkbox, dropdown, roller,
  spinbox and button matrix, an arc, a calendar and a menu on
  [Controls](widgets-controls.md); a tile view and a window on
  [Containers](widgets-containers.md); a table, a scale, a spinner and a
  QR code on [Indicators](widgets-indicators.md); a line, a shape and an
  animated image on [Images and icons](widgets-graphics.md); a text area
  and rich text on [Text and values](widgets-text.md). Every one is
  pictured on its page and works the same on the glass and in WEBview.
- **Charts as widgets** ([Charts](widgets-charts.md)): an energy flow, a
  bar chart, a donut, a sparkline and a scatter plot - and a **panel can
  be translucent** (its opacity), so a card lets a photograph show through.
- **The Toolbox is in groups** - Basic, Controls, Indicators, Charts,
  Layout, Text - open at the start; a click folds one. The Hierarchy shows
  a widget's text of several lines on one row.
- **Turning and circling**
  ([Images and icons](widgets-graphics.md#turning-and-circling)): an icon,
  an image, a shape or a line turns to the angle a variable gives or spins
  at a speed (a propeller at the fan's rpm), and a moving widget can run
  on a circle - a marker round a dial.
- **The wheel and the knob** ([Controls](widgets-controls.md#wheel)): a
  ring of icons for a round screen, the chosen one at the top; and a
  rotary encoder with a push button drives the whole screen - a turn moves
  the highlight from control to control, a press presses a button or
  opens a value for editing, a long press goes home. In WEBview the arrow
  keys, Enter and Escape do the same.
- **Round screens**: a panel whose glass is round is drawn round in the
  editor and in WEBview. Two round knob panels join the hardware catalog
  ([Supported hardware](modules.md)) - the **M5Stack Dial** and the
  **Waveshare ESP32-S3 Knob 1.8"** - with a knob example project; their
  pin maps come from the manufacturers' documentation and wait for a
  bench check.
- **A label aligns vertically** too (top, centre, bottom), and a style
  picks its font by the font's name.
- **Very large digits** (a clock of 96 px) draw on every panel; a panel
  with little memory used to restart on the first such screen.
- **A button or a switch on a variable that is not a BOOL** is refused at
  the desk unless it names a bit, instead of doing nothing on the panel.
- **The clocks**: a leading zero sits level with the digits.
- **The MaTouch Lite's colours** are true now (the panel's gamma tables
  travel with the project).
- **The capacitive touch of an ESP32-P4 panel recovers on its own** when
  its controller stops answering mid-run - it is found again, reset if
  need be, and the diagnostic buffer says what happened; before, only a
  restart brought the touch back.
- **The STM32 panel watches its own picture loop**: a stall restarts the
  panel after sixteen seconds and the next start says why (`wdt=` in the
  device information, the place of the stall in the diagnostic buffer).
- **A CANopen node that boots after the panel, reboots or drops to
  pre-operational** is configured again and started; before, a fieldbus
  module that came up late stayed pre-operational until the panel was
  restarted ([CANopen](canopen.md)).
- **Save and Save as** always write a `.prj32` named after the project in
  its own folder, and a name with diacritics lands on disk as typed.
- **Find devices: Use on a network row** puts the device's address into
  the port box.
- **Three example projects**: a house dashboard on the MaTouch ESP32-P4
  7" (heating, climate, lights, energy and weather on photographs with
  glass cards), a weather station on the MaTouch Lite ESP32-S3 3.95" with
  a [node's](node.md) BME280 as its outdoor sensor, and the knob example
  for the M5Stack Dial.

## 1.04.000

A new line: every device takes a new runtime (over the network or over
USB, as always - [Download to the board](deploy.md)), and the editor
grows the round below.

- **Two Makerfabs MaTouch panels join the hardware catalog**
  ([Supported hardware](modules.md)): the **MaTouch ESP32-P4 7"** - a
  1024 x 600 MIPI-DSI glass with capacitive touch, ethernet and WiFi 6 -
  and the **MaTouch Lite ESP32-S3 3.95"** - a 480 x 320 SPI glass with
  resistive touch. Each comes with its example project, and every bus
  (I2C, SPI, serial, CAN, RS-485) is wired on the pins of its connectors;
  a pin the panel itself uses is refused with its name.
- **A capacitive touch controller configured for another resolution than
  its glass** is scaled into the glass, so a touch lands under the finger
  on the whole screen.
- **The panel as CANopen master sends its own heartbeat** when the bus
  page asks for it (node-ID and period in ms). A drive set to watch it
  stops with a fault when the panel goes silent, instead of running on
  with the last command.
- **A CANopen device with a fixed PDO layout** - a safety controller's
  fieldbus module, many I/O modules - is marked in its window ("The device
  has a fixed PDO layout"): the panel only reads its frames and writes no
  mapping, so the cyclic traffic of the other devices on the bus goes on.
- **The Parker AC30 CANopen EDS files** are in the device library.
- **ONLINE with a project that has no variables** works; before, it said
  "the panel runs a different program" however often it was downloaded.
- **ONLINE, a normally closed contact that does not conduct** draws its
  slash dashed like its bars.
- **The Messages pane sorts what the editor says** into errors (red),
  warnings (orange) and information, with a switch and a count for each:
  a refusal such as "A VAR with that name already exists" is a warning.
- **The chips soldered on a board** show in the tree under the name they
  get in the project, without a note behind them; a tooltip says a click
  adds them, and why the on-board memory is grey.
- **The ladder bar's P, N, S and R** sit in the middle of their buttons.
- **A Linux device's page is in tabs** - Network, Buses and chips,
  Display, Operating system, Clock and power - under one header with the
  device's address, a login and **Read from the device**. Every tab
  starts from what the device uses now and writes only its own settings;
  before, writing the buses from an untouched page cleared them on the
  device ([The Linux runtime](linux-runtime.md#the-device-from-the-editor)).
- **CAN and serial controllers on SPI as a list** - any mix of MCP2515,
  MCP2517/2518 and SC16IS750/752 on every SPI bus the device has, each
  with its own chip-select pin; the editor counts how many more fit and
  sets them up on the device
  ([Setting up a Linux device](linux-setup.md#the-operating-system-from-the-editor)).
- **The Terminal is this PC's command prompt** too: `cmd`, or no port,
  in its port field; the arrow keys bring earlier lines back and Ctrl+C
  stops what runs. The Terminal and Messages tabs sit beside Properties
  at every start.
- **An unbound output of a block inside a ladder rung** (the elapsed time
  of a TON) is blank now, like the outputs of a block on its own rung.

## 1.03.000

A new line: every device takes a new runtime (over the network or over
USB, as always - [Download to the board](deploy.md)), and the editor
grows the round below.

- **A disconnected CAN bus costs the program nothing.** A panel whose
  program uses no CAN device never transmits on the bus, so it cannot go
  bus-off. A bus that is configured but unplugged is said once in the
  diagnostic buffer ("CAN: bus down ... nobody answers"), tried again
  every ten seconds and said once more when it answers; the program runs
  on and the axes read offline meanwhile. The system variable
  `SYS.CAN_FAULT` is "a bus-off being handled or the bus down".
- **The editor no longer freezes on a device address nobody answers.** A
  connection gives up after 1.5 s and says what to look at (another
  network, the device off, the console busy); an address that did not
  answer is left alone for ten seconds before the next try.
- **Buses on the header and the real-time kernel from the editor.** The
  *Operating system* section of a Linux device switches SPI, I2C and the
  UART on and off, puts a CAN controller on SPI0 (the chip, its chip
  select, its interrupt pin and its crystal) and installs the
  distribution's real-time kernel with a core kept for EtherCAT. The same
  section sits on the device's board page -
  [Setting up a Linux device](linux-setup.md#the-operating-system-from-the-editor).
- **Prepare a Linux device is a page**, not a window in the way: the
  project stays at hand while a device installs or restarts, and every
  line the work prints goes to Messages as well.
- **The Terminal is a console for a Linux device.** Type the device's
  address into the Terminal's port field and the tab is its shell: the
  editor's key logs in on a device the editor prepared, a user name and
  password where it did not - [Online](online.md#the-serial-console-keeps-working).
- **Messages comes to the front by itself** whenever a line is pushed to
  it, and the Terminal and Messages tabs land beside Properties even with
  a window layout from an older version.
- **Download to device.** The dialog is a statement; a Linux device offers
  the network road only, there is no USB road to it.
- **Find devices fits the screen.** The dialog's width follows its table
  up to the screen, the address column is bounded and *Use* is always in
  reach.
- **An unbound output of a ladder box is blank** - the pin and its name
  stay, no red marks; ONLINE paints the live value above a bound output
  as before.
- **The browser's gauge** starts its arc where the panel's does.

## 1.02.001

An editor release inside line 1.02: the devices keep the runtime they
have.

- **The wheel over the screen canvas zooms in every window layout.** On
  some computers it stayed silent while every other panel scrolled. If
  it ever stays silent again, the editor keeps a note of what it saw in
  `canvas_wheel.txt` beside its settings (the ctrl32 folder in the
  user's local application data) - send it to us.
- **The canvas bar fits a narrow window.** When its tools do not fit the
  width, they continue on a second row instead of being cut off at the
  right edge, so the zoom percentage and *Fit* are always in reach. The
  bar carries no status text any more.

## 1.02.000

A new line: every runtime is rebuilt and the devices take 1.02.000 over
the network or over USB (Upload runtime); a device nobody updates keeps
running its program.

- **The ladder editor, reworked.** Networks on a grid, each with its
  number, its comment line and a fold arrow; a cursor you drive with the
  arrows and the function keys (F2/F3 a contact, F7 a coil, F8 a branch,
  Enter the sheet, Tab the next open operand); an operand typed straight
  into its red `??.?` with the list of fitting variables under it; the
  right button opens the menu, a double-click the sheet; tiles and
  elements dragged onto a cell; Ctrl + wheel zooms. A branch may stand
  anywhere and a lower row may end in a coil of its own or carry a block.
  New elements: the **compare contact** (`level > 10`, typed or picked),
  the **jump** to a later network and the **return**. **Where used** on
  any operand lists every place of its variable and jumps there. The
  **Messages** tab under the canvas keeps what the editor said, errors in
  red, a double-click goes to the network; the **Terminal** tab beside it
  is the device's console. The page: [Ladder](ladder.md).
- **The screen canvas zooms.** The mouse wheel over an HMI or WEB
  screen zooms it from 25 to 400 % around the pointer; at 200, 300 and
  400 % every panel pixel is a square block, so the picture stays the
  panel's. The bar above the canvas shows the percentage and offers
  *Fit*; a picture larger than the window pans with the scrollbars.
  The page: [Controls and shortcuts](editor-controls.md).
- **The node - an ESP32-C3 or ESP32-C6 as remote I/O.** A module with
  no program of its own: its inputs and outputs are variables the main
  device owns through net32, with a table of reflexes that act when the
  main device is away, a safe state, a WEBview page, Modbus and MQTT
  transports, deep sleep on batteries. Every C3 and C6 module of the
  catalog runs the node image; the New project wizard offers it. The
  page: [The node](node.md).
- **A Linux device's board page** carries *Prepare this device* beside
  *Flash runtime*, with that device already chosen.
- Help › About names the graphics renderer and the frame time, and the
  editor warns when it runs without acceleration (a slow notebook is
  recognisable at once).
- Smaller: the Toolbox's duplicate group of in-network blocks is gone
  (a block the power can flow through lands in the network from its own
  group); a comment of a network sits under its header; the Flash
  runtime dialog, the devkit and module pin pickers from the first
  testing round of 1.01.010.

## 1.01.010

An editor build inside line 1.01 - the devices keep their 1.01.000
runtime.

- **Properties in sections.** The Properties panel shows a list of
  sections on the left and the chosen section's fields on the right, with
  a short summary beside each section. A variable has General, I/O source,
  Sensor (on an analog input), Scaling and Use - where the variable is
  read, on screens, in alarms, in blocks and in ST. A widget, an FBD block
  (Block, Inputs, Parameters, Outputs) and a ladder contact or coil use the
  same panel. The section picked last stays picked for the next object of
  the same kind.
- **A converter channel in Properties.** Click a channel of an ADS1115,
  ADS1118 or another converter on its page: Properties shows Channel,
  Sensor and Scaling - the same sensor card the variable has.

## 1.01.009

An editor build inside line 1.01 - the devices keep their 1.01.000
runtime.

- **Every Espressif module checked against its datasheet.** Each module
  now knows exactly which GPIOs it brings out to its pads and which its
  own flash and PSRAM take: an ESP32-S3 has no GPIO 22-25, the octal-PSRAM
  S3 modules give 35-37 to the memory, a WROVER gives 16 and 17 to its
  PSRAM, an ESP32-MINI-1 brings out 9, 10, 37 and 38 but not 16 and 17,
  a PICO-V3-ZERO brings out five pins. The pin lists offer only those,
  and the build refuses a pin that is not there, or an output on a pin
  that can only read.
- **Analog inputs on a module.** The pin list of an ADC input offers the
  ADC1 pins the device reads (GPIO 1-10 on an S3, 32-39 on an ESP32).
- **Digital inputs and outputs on a module.** The pin list of a GPIO
  variable was empty on every module target (ESP32-S3, ESP32 and the
  rest): a module lists no pins of its own. It now offers every usable
  GPIO of the chip, leaving out the lines the module's flash and PSRAM
  take, and for an output (access rw) the pins that can only read.

## 1.01.008

An editor build inside line 1.01 - the devices keep their 1.01.000
runtime.

## 1.01.007

An editor build inside line 1.01 - the devices keep their 1.01.000
runtime.

- **A Linux device typed without a port.** The network roads - the
  deploy to a device and *Flash runtime* - took an address without a
  port as port 80, and a Linux device answers on 8080: the deploy and
  the runtime update stopped at "asking /devinfo" with nothing more. A
  Linux device is 8080 unless the address says otherwise.

## 1.01.006

An editor build inside line 1.01 - the devices keep their 1.01.000
runtime.

- **The EtherCAT axis window is the CANopen one.** It showed an SPI chip
  select that belongs to the stepper chips and hid the positioning
  section; now it carries the slave position, *Open device (PDO
  mapping)* - the slave's window on its PDO tab, where the mapping, the
  start-up writes and the signals live - and the positioning section
  like a CANopen axis.

## 1.01.005

An editor build inside line 1.01 - the devices keep their 1.01.000
runtime.

- **Flash runtime on a Linux device finds its runtime.** 1.01.003 added
  the button; an installed editor then answered "none for this board",
  because it looked for the Linux runtime under the name the checkout
  uses and the installer lays it under another. Both spellings are found
  now, and the release check runs in the installed layout.

## 1.01.003

An editor build inside line 1.01 - the devices keep their 1.01.000
runtime.

- **Flash runtime on a Linux device.** The board page of a Linux device
  (reTerminal, Raspberry Pi, the DK2) now carries the *Flash runtime*
  button like every other board; it was missing, so a Linux device
  could not take a new runtime from the editor at all. The runtime
  travels over the network: the device's address goes into the port
  field, the device checks the new binary before it switches and falls
  back by itself if the new one does not come up.
- **The devices tree of a Linux device with two network ports** no
  longer raises an error window over its adapter rows.

## 1.01.002

An editor build inside line 1.01 - the devices keep their 1.01.000
runtime.

- **J1939 and the diagnostics on any CAN bus that has no CANopen
  device.** The menu of a CAN bus used to grey *Add J1939* and *Add
  diagnostics* whenever the project had the CANopen master role, and
  every further bus of a Linux device counted as a CANopen bus by
  itself - so a device with three buses and no CANopen device could put
  a vehicle network nowhere. The rule is now the one the build applies:
  one bus, one higher layer. A bus that carries a CANopen device refuses
  J1939 and the diagnostics, a bus that carries a vehicle network
  refuses *Add CAN device* and *Add Axis*; the greyed item says why. The
  CANopen role can be removed while no CANopen device or CAN axis is
  left, whatever the number of buses.

## 1.01.001

An editor build inside line 1.01 - the devices keep their 1.01.000
runtime.

- **The update check says what it found.** Help now shows the result of
  the last check under *Check for updates* - the latest version
  confirmed, no connection to www.ctrl32.com (with the error number), a
  bad answer - and the same line lands in `update_check.txt` beside the
  editor's settings, the file to send us when "no new version" looks
  wrong. *Check for updates* runs even when the automatic check is
  switched off in Settings.
- **The update window is a dialog** in the centre like every other, its
  middle button reads *Download page*, and the digits on the progress
  bar stay readable as the bar passes under them.
- **Only projects in the examples.** The installed Examples and
  Tutorials folders carry `.prj32` files and nothing else - the
  internal test files that travelled with them until now are gone, and
  the editor no longer copies them into your Documents folder. A copy an
  earlier version left under Documents\ctrl32\examples is yours to
  delete.
- **The context menu of a second CAN bus on a Linux device** offered
  *Add CAN device* and *Add Axis* twice, which made the editor show a
  "message from Dear ImGui" and close the menu before *Add J1939* could
  be clicked. Each action is in the menu once now.

## 1.01.000

The first number after the dot is the **runtime line**: every device
runtime of a line carries the same number, and an editor build inside
the line (the last three digits) ships without new runtimes. A new line
means the devices get a runtime update; the editor offers it the usual
way.

- **64-bit variables everywhere a value travels.** ONLINE the editor
  shows the whole value on a widget, a ladder contact or an FBD pin. On
  a Linux device the **OPC UA client** reads one from an Int64, UInt64
  or Double node; over **+7** it is the S7-1200/1500's LInt, ULInt or
  LReal, eight bytes read and written whole; over **net32** a 64-bit
  variable is published and subscribed like any other (it takes two of
  a device's wire slots). An **input** widget on one shows every digit
  and the keypad takes every digit back - on the glass and in the
  browser. A 64-bit variable in the retain list survives a restart
  whole, on every device. See [Variables](variables.md#64-bit-values).
- **The vehicle network's icon says what the vehicle is.** The industry
  group of the panel's NAME decides: an engine for a vehicle, a tractor
  for ISOBUS, a ship for a boat.
- **An idle editor no longer takes the graphics card.** The editor drew
  frames back to back when nothing moved; it waits for your next click
  now.
- **About says what ctrl32 is** - the panel, the logic, the buses, the
  browser - instead of a build note.
- The installer's last page speaks the language you chose for the
  installation.
- Should the editor ever report an internal drawing error, it also
  writes it to a file beside its settings - the one file to send us.

## 1.00.057

- **64-bit variables, on every device.** Three kinds more - `LINT`,
  `ULINT` and `LREAL` - for an energy meter's counter, a totaliser, a
  serial number. A value widget shows the whole number, the browser
  shows it digit for digit, MQTT publishes it, a Linux device serves
  it over OPC UA as an Int64 / UInt64 / Double, and the Modbus master
  reads and writes it in **four registers** (the word order as for
  32-bit values; the slave serves it the same way). A program reads a
  64-bit variable as a `REAL` and writes one from a `REAL` - about seven
  significant digits reach the program, the device and the buses carry
  the whole value. See [Variables](variables.md#64-bit-values).
- **A vision block that cannot run no longer blanks the blocks after
  it.** A *Mask* with no mask picture, a *Difference* with one wire, a
  picture of the wrong kind: the block's own outputs stay empty and its
  window says why, the blocks that do not depend on it keep their
  pictures. Until now every block after the failing one lost its output,
  whatever branch it was on.
- **A connection on the vision canvas is removed on its own.** A wire
  is a thing of its own now: click it and press Delete, right-click it
  and pick **Remove connection**, or drag it off the input dot - drop it
  on another input to move the connection, or let it go. Until now the
  only road was a right-click on the input dot, which also opened the
  block's menu, so a connection looked removable only with its block.
  See [the canvas](vision.md#the-canvas).
- **Every vision block has its own page.** The documentation's Vision
  section is a section of its own now: the editor's page with every
  field, button and gesture, the camera's page, and one page per block -
  what it does, when to use it, every input, output and setting with its
  range and default, the block's window on a test picture and the block
  as it stands on the canvas. The index of the 89 blocks names what the
  trade calls each one.
- **The camera's page is aligned.** Every field is the same width, so the
  labels read in one column; width and height are one row and the stream
  is a list like the other fields.
- **The outputs of a block's window explain themselves.** Hold the mouse
  on an output's name and it says what the value is.
- **Every dialog opens in the centre with the frame.** The two
  system-device dialogs (rename, delete) had neither; the editor's own
  check now refuses a dialog without them.
- An ONNX model shows as what it is in the Assets list.
- **Find pattern and Fixture on a plain background.** A picture with an
  area of one shade - a blank belt, a plain tray - could make both
  blocks report the part in the picture's corner with a full score;
  such areas are no match now. A camera's picture, with its noise,
  never showed it; a drawn or an overexposed one did.

- **A vision block's window is a dialog.** It opens in the middle of the
  screen, the same size for every block, the settings aligned in columns
  on the left and the picture large on the right - the area is drawn and
  the colour picked on that large picture.

## 1.00.056

- **Measuring with the camera.** New vision blocks for the checks a
  packaging or a parts line asks for: **Fill level** (the liquid in a
  bottle, the powder in a jar), **Circle (fit)** (a diameter, a centre,
  roundness), **Line (fit)**, **Angle** and **Distance of points**,
  **Part in place** (a cap on its bottle, a seal in its seat, a label
  where it belongs), **Colour of object** (coloured parts sorted in one
  pass) and the **Laser line profile** (a cheap line laser and the
  ordinary camera measure a height, a step, a groove). Every measuring
  block answers in pixels and, with a scale wired in, in millimetres;
  every one takes a tolerance and answers *ok*. The **Caliper** answers
  the pitch of its edges and hands every edge on as an object. See
  [Measuring](vision.md#measuring).
- **Coordinates.** A **Fixture** block finds the part by a picture
  taught with one drag and shifts (and turns) every later picture so the
  part sits where it was taught - the windows of the blocks after it
  stay where they were drawn. A **Plane from a board** block is taught
  once from a chessboard lying on the working plane and draws every
  picture as a top view with a known number of pixels per millimetre.
  The laser profile's baseline is taught the same way, from the empty
  plane. See [Coordinates](vision.md#coordinates).
- **The bottle example and a measuring tutorial.** The new
  [Bottle check](example-bottle-check.md) example checks a bottle's fill
  level in millimetres, its cap through a Fixture and its label with a
  code, and [Measuring, step by step](tutorial-measuring.md) builds it
  block by block — on the desk with the drawn bottle the editor ships,
  no camera needed.
- **A people counter with a shipped model.** The new
  [People counter](example-people-counter.md) example carries a small
  trained detection network inside the project (YOLOX-Nano, Apache 2.0)
  and counts the people the camera sees; the **Detect (model)** block
  reads that model's raw export (*layout* `yolox`) and keeps only one
  class when asked (*only*), so a counter of people counts people and
  not the chairs.
- A project saved with an imported model keeps the model: the file is
  written beside the project with its own extension.

## 1.00.055

- **Cameras on a Linux device.** Plug a USB camera into the device, add
  it under the new **Cameras** node of the tree and draw a **camera**
  element on a screen: the live picture appears on the device's screen
  and in the browser. The camera's page takes a picture from the device,
  the quickest check of focus and direction; the device also serves the
  picture and a live stream on its own address. The camera never slows
  the PLC - under load a picture is dropped, not a cycle. See
  [Cameras](cameras.md).
- **Vision on a Linux device.** A vision program is drawn from blocks -
  the camera, what is done with its picture, what is measured - under
  the new **Vision** node of the tree, and its answers are variables:
  presence, colour check, edge position and reading a QR code or a
  barcode are ready tools, with cropping, colour ranges, thresholds,
  filters and counting objects to build your own. Every block has its
  own window with its settings and the picture it makes - at the desk
  on a test picture, online from the device; an area is set by a drag
  on the picture, a colour by a right click on it. Blocks that find
  objects and circles give a list the program picks from, or crops to -
  the check follows the part wherever it lies. A pattern taught by a
  drag over the part is found wherever it appears, with its score. Equalize light, Sharpen, the Difference of two pictures and Motion
  (what changed since the last look) join the filters. A Ruler taught by a drag along a known length
  gives millimetres per pixel to the Scale block, Straighten takes a
  rectangle seen at an angle by four clicks, Find lines gives the edges
  of a sheet with their angles. Check objects says whether the found
  objects are the right number and every one the right size. Any number or yes/no
  setting of a block can come from a variable, read before every run -
  a recipe changes the check. An **ST code** block takes a few
  lines of ST inside the vision program for the calculation the blocks
  do not have. A program runs on a rising
  edge of a variable (with BUSY and DONE for the rung that waits) or
  periodically, below the PLC. See [Vision](vision.md) and
  [Vision, step by step](tutorial-vision.md).
- **A camera's exposure, gain and white balance** can be fixed on its
  page - a check wants the same picture every time.
- **The assistant reaches everything.** The MCP server has two more
  tools: `run_commands` runs editor commands in order - the same
  operations your clicks perform, from a camera or a vision block to a
  ladder rung, a variable, a task or a recipe, each one Ctrl+Z away -
  and `vision_info` reads the cameras and the vision programs with
  their blocks, settings, links, results and test-picture values.
- **The Linux runtime's limits, substantially larger:** 20480 variables
  (5120), 4096 alarms, 1024 screens, 1024 elements on a screen, 40960
  program blocks, 128 programs (32), 256 function-block instances in one
  program (32), 64 axes, 32 trend traces, 16 browsers at once, 4 MB of
  compiled program and 4 MB of instance data (64 kB and 256 kB per
  program). The panels keep their numbers. (A variable's name is a
  string of the project file; the string limit that quietly held a
  Linux project to about 1900 variables is gone. A program whose
  instance data would not fit its 256 kB is refused at the desk with
  the number - it used to be cut silently.)
- **The update dialog** shows the download's percent in the middle of
  its bar.
- **Read code reads every code.** The block knows *datamatrix*,
  *pdf417*, *aztec* and *any* beside *qr* and *barcode*, and *barcode*
  now means every one-dimensional code — Code 128, Code 39, ITF,
  Codabar and GS1 DataBar beside EAN and UPC; a new *format* output
  says which kind was read. A small label at arm's length reads where
  it did not before. See [Vision](vision.md).
- **A block's picture on a screen.** A camera element may name a vision
  block as `program.block` and then shows that block's picture, live,
  on the glass and in the browser — the camera and the picture after
  the filters side by side. See [Cameras](cameras.md).
- **The reTerminal example reads codes.** Its new Codes screen shows
  what a QR code, a barcode and a DataMatrix in front of the line's
  camera say — three Read code blocks on a picture the operator tunes
  with three sliders (brightness, contrast, sharpen) while watching it
  beside the camera's, their text in STRING variables. See
  [the example](example-reterminal-ecat.md#reading-codes).
- **32 vision programs** in a project (8 before), **256 blocks and 128
  results** in a program (64 and 32 before).
- **A text setting from a STRING variable.** The expected text of Read
  code (the lot of a recipe) and a model's labels can be read from a
  STRING variable before every run, like the numbers.
- **Any camera size.** The camera page takes a width and a height
  beside the presets.
- **RTSP cameras.** A network camera's H.264 stream (`rtsp://...`) is a
  camera of the project; the device needs `ffmpeg` installed once.
- **Lens calibration.** The *Lens correction* block fills its numbers
  from a chessboard picture with one button.
- **77 vision blocks.** The palette grew by 36: smoothing that keeps
  edges, contrast stretching and local contrast, gamma, white balance,
  one colour channel, the adaptive threshold, top-hat / black-hat,
  outline, fill holes, the distance map, gradient and Laplacian edges,
  turn and shift by any angle, unroll a ring, halve, lens correction,
  combine and mask pictures, filter objects by shape, object shape,
  nearest object, corners, fill from a point, find by features (a
  taught picture at any angle or distance), ArUco / AprilTag markers,
  chessboard corners, a caliper, brightness statistics, a histogram,
  sharpness, distance between points, compare with a taught area, and
  match a taught shape. Every one with its own window and its test.
- **Cameras and vision are for 64-bit Linux devices** - the reTerminal,
  a Raspberry Pi 4 / 5, a PC-class device; the STM32MP1 device is too
  slow for it and its runtime carries none.
- **IP cameras.** A camera of a Linux device can be the MJPEG stream of
  a network camera (`http://.../stream.mjpg`) - the device reads the
  stream itself and the picture works everywhere a USB camera's does.
- **Text variables on Linux devices.** A STRING variable holds a text
  of up to 80 characters - what a camera read off a code, a product
  name: on the screens and in the browser as a value element, on OPC UA
  as a String node, on MQTT as text.
- **The browser keeps up while it is open.** A browser showing a Linux
  device's screens no longer holds up a program download or the
  editor's device queries.
- **The M5Stack StamPLC's relays and inputs.** A new I/O expander in the
  peripheral library, the AW9523B: on a StamPLC it is fitted at 0x59 and
  added with one click - the four relays on pins 0-3, the eight isolated
  inputs on pins 4-7 and 12-15 - beside the RS485 and CAN lines the board
  already had. The chip must answer its own ID before anything is
  written to it.
- **The M5Stack StamPLC's display.** The 1.14-inch screen (240x135)
  works like any board's glass: draw screens for it and they appear on
  the device; its backlight, which sits on an I/O expander rather than
  a pin, comes on by itself.
- **The StamPLC talks over its USB-C.** It has a runtime of its own:
  the runtime upload, the program download, going online and the console
  all use the board's USB-C, and the CAN line and the buzzer keep the
  pins they are wired to.

## 1.00.054

- **Servo inverters on EtherCAT in cyclic position mode.** A slave's
  window takes an operation mode - velocity, or *cyclic position (csp)*
  for a servo - and, for a servo, the byte offsets of its 32-bit words.
  The device ramps the velocity the program asked for, integrates it
  into the position setpoint every cycle and sends it with the velocity
  feed-forward; the drive's own position loop follows. The same motion
  blocks command a servo and a frequency inverter. *Add from library*
  lays a servo out from its description with only the csp process data
  assigned, and a double inverter carries two axes in one slave - the
  axis picks A or B. The reTerminal EtherCAT example carries the bench's
  two Lenze i700s this way, on the distributed clock at 1 ms. Linux
  runtime bundle.
- **Torque and position on a servo, and the line shaft's feed-forward.**
  `MC_SETTORQUELIMIT` holds a torque limit on the drive every cycle,
  `MC_TORQUECONTROL` commands the torque of a servo declared in cyclic
  torque mode, `MC_MOVEABS` / `MC_MOVEREL` / `MC_HOME` run on a servo in
  cyclic position mode with the profile on the setpoint, and
  `MC_TORQUEFF` writes the acceleration feed-forward as the drive's
  torque offset: exact from the axis's own ramp or move and from the
  master's through the ratio, measured over a short window from an
  encoder-fed virtual master. `MC_GEARINPOS` gears a follower in at a
  defined relation of the positions, so a job's phases are numbers a
  recipe keeps and the same relation comes back after a job change and
  a restart; a changed ratio is applied at standstill. A slave's window
  names the torque words; *Add from library* finds them in the
  description. Linux runtime bundle.
- **The Linux runtime installs as prebuilts only.** The installer lays
  the runtimes for the reTerminal, any 64-bit Raspberry Pi and the DK2
  under `%ProgramData%\ctrl32\linux`; the source archive is no longer
  part of it. For another Linux device, write to us.
- **A virtual master axis.** An axis with no drive behind it, added on
  the EtherCAT node: the program commands it like any axis, the device
  runs its profile every bus cycle, and the followers of a line shaft
  gear to its position - one clock for the whole line - while a drum
  that takes only a speed follows its velocity. It can instead follow
  a counter variable (the drum's encoder as a process-data signal) and
  be the measured drum. The reTerminal EtherCAT example's line screen
  has the source switch and a second register, the followers against
  the drum. Linux runtime bundle.
- **Torque and positioning on a servo.** Two motion blocks:
  `MC_SETTORQUELIMIT` holds a torque limit (per cent of rated) on the
  drive every bus cycle while it is enabled - the tension of a winder,
  a gentle approach against a stop - and `MC_TORQUECONTROL` commands the
  torque itself on a servo declared in cyclic torque mode, the drive
  limiting the speed. A servo added from its description carries the
  torque-limit object beside its cyclic pair; without the block the
  drive keeps its own limits. `MC_MOVEABS` / `MC_MOVEREL` on a servo in
  cyclic position mode run their profile on the setpoint in the bus
  cycle and end exactly on the target, `MC_HOME` takes the position the
  axis stands on as zero. Measured on the bench: a 10-revolution move
  settles at 10.000; a 3 % limit holds an axis commanded 300 rpm at a
  few rpm with the torque flat on the limit. The reTerminal EtherCAT
  example has a *Position* screen for both. Linux runtime bundle.
- **A line shaft: one axis follows another.** Three motion blocks -
  `MC_GEARIN`, `MC_GEAROUT`, `MC_PHASING` - couple a servo in cyclic
  position mode to a master axis at a rational ratio from the master's
  measured position every bus cycle, with the master's velocity as the
  follower's feed-forward, the chain delay compensated live, a phase
  shift ramped in, and the register (the follower against the master,
  in increments) as an output. Measured on the bench at 1:1 from 60 to
  600 rpm and from 2 ms to 250 µs of bus cycle: without the
  compensation the error is the velocity times a chain delay that grows
  with the cycle (−1058 increments at 300 rpm on 1 ms, −1993 at 600);
  with the measured delay in and the position loop at 80 1/s a follower
  stays within about a hundred increments of its master through ramps
  and holds, the rest being the drives' own loops. The reTerminal
  EtherCAT example has a line-shaft screen with the numbers live and
  ships the measured delay and the gain. Linux runtime bundle.
- **The library's start-up writes declare the process data assignment.**
  A device added from its description carries the assignment of the
  objects that travel among its start-up writes, so the offsets the
  window shows hold on the wire at every start.
- **An EtherCAT drive comes back from a power cycle.** The master now
  waits for the drive's own application to answer before it writes the
  start-up parameters, and a parameter set the drive refused in part is
  written again every few seconds until it takes. Before, a drive
  switched off and on while the line was running could reach the
  operational state without its control mode and its network-enable
  bits - alive on the bus and impossible to start. The console and the
  diagnostic buffer say "configuration incomplete" while it lasts and
  "configuration complete" when it is done. Linux runtime bundle.
- **Several drives on one EtherCAT line.** The reTerminal example comes
  in a four-drive form (`reterminal_ecat_4x` in the examples: four
  i550s daisy-chained, position on the line = axis number, a screen
  with a column per drive). A line takes up to 32 devices and a Linux
  device drives up to 32 axes; each drive carries its own start-up
  parameters and its own signals, and every extra axis has its own
  program.
- **The device's position always arrives whole.** In the ctrl32
  telemetry mode `lat` and `lon` are never split across two messages
  when a large set of values does not fit one.
- **EtherCAT: the distributed clock and a cycle in microseconds.** The
  EtherCAT page has a *Cycle µs* field and a *Distributed clock* switch:
  devices with a clock get SYNC0, the master locks its cycle to the
  line's reference clock, and the device page shows the worst wake-up
  lateness of the last minute - the figure a fast servo line lives by.
  What the hardware under the runtime must offer for a sub-millisecond
  cycle is on the [EtherCAT](ethercat.md) page.
- **A real-time kernel recipe for sub-millisecond EtherCAT.** The Linux
  runtime bundles carry `ctrl32run-rt.conf` and the interrupt mover; with
  the distribution's `-rt` kernel and one core kept for the bus, a
  Raspberry Pi device runs the line at 200 µs without a lost frame. The
  recipe is on the [EtherCAT](ethercat.md) page. The line's lost-frame
  and overrun counters start once every device is operational, so a
  start-up no longer reads as a fault, and the master waits for the
  port's link before it looks for devices.
- **The Lenze i700, i750 and i950 servo inverters in the EtherCAT
  library.** Their device descriptions (with the object dictionaries of
  the current firmware where Lenze publishes them) ship beside the i550's, so an axis on either is added from
  the library like any other device.
- **The vendor's engineering tool reaches a drive through the Linux
  device.** A slave takes an *EoE address* and the EtherCAT page an *EoE
  gateway*; the runtime becomes the Ethernet-over-EtherCAT gateway, so a
  tool on the PC talks to every drive by IP while the line runs. The
  EtherCAT page says the two network settings it takes.
- **An axis window lists the ST calls on its axis.** Beside the FBD and
  LD blocks, every ST call that names the axis - `AXIS := 2`, and
  `Master := 4` for a follower's master - is listed with its program,
  so a line written in ST no longer reads as an axis nothing uses.
- **A new tutorial: the line shaft.** Two servos geared to a virtual
  master, the delay compensation, a job as a recipe with its speed,
  ratios and phases - step by step on the reTerminal EtherCAT example,
  whose Jobs screen was listed twice and is now listed once.
- **Twenty more boards in the hardware catalog.** KinCony KC868-A4,
  A8, A16 and A32; LaskaKit ESP32-DEVKit, LPKit, RoboBoard,
  ESP-VINDRIKTNING and ESP32-S3-DEVKit; Olimex ESP32-DevKit-LiPo,
  ESP32-S3-DevKit-LiPo and ESP32-P4-DevKit; M5Stack StamPLC; Makerfabs
  8-channel relay and button boards, AC dimmer, DC motor, weather
  station, WiFi AC dimmer switch and energy meter. Each is picked like
  any board - its buses, Ethernet and relay pins set, its free pins
  listed - and runs the runtime of the module it carries.
- **A board's soldered chips are added with one click again** - the
  expander and the analog inputs of an inoCORE32-TM1.1, for instance,
  were listed but never offered.

## 1.00.053

- **A device sends to ctrl32 telemetry.** The MQTT page has a third
  publish mode, *ctrl32 telemetry*: pick it, type the device's id and
  token from the platform, tick the variables — the values arrive on
  the datastreams of [telemetry.digital](https://telemetry.digital) or
  of a local instance of the platform. Update the runtime on the boards
  that use it: an older runtime sends the old message shape, which the
  platform keeps as a raw message. The page: [MQTT telemetry](mqtt.md).
- **MQTT on Linux devices.** A Linux runtime publishes over MQTT like
  every other board now - every mode, TLS included (the system's
  certificate store judges the broker, so a public certificate needs
  nothing from you). The device page and the console carry the
  connection state (`mqtt=`), and `SYS.MQTT_OK` is real on Linux.
- **MQTT over TLS on the STM32 F7.** The Discovery reaches an
  encrypted broker too - telemetry.digital included - verifying the
  server against a built-in set of public roots and checking its
  name, like the S3 and the P4. A failed handshake says why in the
  diagnostic buffer. The board's RAM budget moved with it: the
  FreeRTOS heap lives in SDRAM now, which left the runtime 50 kB of
  internal heap instead of 20.
- **The editor speaks Bulgarian.** Български joins the eleven
  languages of *View → Language*; a Windows set to Bulgarian starts
  the editor in it, and the installer speaks it too. The translation
  was made with the product glossary — a wrong word in your language
  is worth a message, it gets fixed in the next release.
- **An EtherCAT drive that lost its PDO assignment comes back.** A
  drive switched off and on while the master was configuring it could
  be left with an empty output assignment; from then on the bus never
  reached OPERATIONAL ("Invalid output configuration") and the drive
  sat in fault. The master now finishes that write in every case,
  names an empty assignment on the console and in the diagnostic
  buffer, and the reTerminal EtherCAT example declares both PDO
  assignments in its SDO list, so a drive that lost one is set right at
  the next start. Update the Linux runtime bundle to get it.
- **A planned restart tells the broker.** Before a pack upload, a
  runtime update or saved settings restart the board, the MQTT client
  now sends a proper disconnect, so the broker closes the old session
  at once instead of holding it until its keepalive runs out. Without
  it a device that came back within seconds with the same client id
  could be attached to a session the broker had already closed - it
  looked connected on the device and offline on the platform.
- **STM32 F7: a runtime update over the network with MQTT running.**
  The telemetry tick kept reading variable names out of the pack while
  the new image was being written into QSPI, and the board reset in the
  middle of every network update. The tick waits like the screen does.
  This one needs the ST-LINK road once, the network road works from
  the next update on.

## 1.00.052

- **Update the runtime on your boards with this version.** The
  program pack format moved (62), so a board still running an
  older runtime refuses a pack built here and says so - it keeps
  running what it has, nothing is lost. Upload the runtime first
  (over the network or USB), then deploy the project. A board you
  are not updating is unaffected: it keeps running its own pack.
- **Analog inputs read real values.** An analog channel now says WHAT
  IS WIRED TO IT and the device does the arithmetic: a 0-10 V or 0-5 V
  sensor through its divider, a 4-20 or 0-20 mA loop through its
  shunt, an NTC thermistor (by R25 and B, or by Steinhart-Hart
  coefficients) and a Pt100 or Pt1000 through the standard curve. Pick
  the sensor on the variable's sheet and the usual numbers are filled
  in - a 165 ohm shunt, a 10k reference, 3.3 V - and every one of them
  can be overwritten for another board. A line under the fields says
  what a reading WOULD mean, so an upside-down divider shows up at the
  desk. A 4-20 mA loop that breaks is refused rather than read as a
  large negative value: the variable keeps what it had and the
  diagnostic buffer says why. It works on every analog input - the
  ADS1115, the ADS1118 and the board's own ADC - and a channel with
  no type keeps the gain and offset it always had. The page:
  [Reading real values](analog-inputs.md), the example:
  `examples\analog_inputs.prj32`.
- **Vehicle buses: J1939, and the two worlds built on it.** A CAN bus
  can now carry a vehicle network, and the device is a **node** on it:
  it has its own NAME, claims an address and defends it, reads the
  parameter groups the control units broadcast and sends its own. A
  group is picked from the library the editor ships — the engine, the
  fuel, the speed, the fault-code message, the boats' engine, tank and
  navigation groups, the tractor's hitches, power take-offs and valves —
  and every ticked signal becomes a variable, already scaled, in one
  step you can undo. Where the library does not reach, the vendor's own
  **DBC file** does. Long messages arrive whole or not at all, over
  either transport: J1939's own or the boats' **Fast Packet**.
  **NMEA 2000 compatible** and **ISOBUS** are the same layer with their
  own groups — the marine names and the agricultural ones, the industry
  group in the NAME set for you. It runs on Linux devices (any of their
  four CAN interfaces) and on boards with CAN. The page:
  [Vehicle buses](vehicle-buses.md).
- **Vehicle diagnostics: asking a control unit.** Under a CAN bus of a
  Linux device sits **Diagnostics**, and under it the control units you
  ask — the usual 0x7E0 / 0x7E8 pair, or whatever the unit's document
  names. The values you list are read over and over by their period and
  land in variables with no program at all; the **fault codes** go into
  variables AND into the diagnostic buffer with the time they were
  read, which is the record a service engineer reads afterwards. What a
  person sets off — read the faults, clear them, ask for one value now —
  is the three new blocks `UDS_DTC`, `UDS_CLEAR` and `UDS_READ`, which
  work like the other service blocks. The page:
  [Vehicle diagnostics](vehicle-diagnostics.md).
- **The tree shows the network adapters, and EtherCAT hangs under the
  one that carries it.** A device scan lists the adapters the device
  really has; the EtherCAT master sits under the port it runs on
  instead of beside it, so a machine with two ports says which one is
  the bus.
- **The EtherCAT process data reads the way every EtherCAT tool writes
  it.** The slave's tab shows its sync managers, the assignment and the
  contents of the picked process data object — the same names and
  numbers the vendor's own documentation uses.
- **A CAN device keeps its own mark in the tree.** The circle with the
  arrow stays with the drives on CAN and EtherCAT.

## 1.00.050
- **EtherCAT devices from their ESI files, the way CAN devices come
  from EDS.** The device library holds the vendors' EtherCAT
  descriptions (ESI) beside the EDS files — *Tools › Device library*
  lists them and imports more — and the EtherCAT page's **Add from
  library** turns a picked device into a slave: its identity (vendor,
  product, the revision the file describes), the sizes of its process
  images, the CiA 402 layout when the device is a drive, and one signal
  with its variable for every other entry of the default process data
  (the i550's error code, for instance). The Lenze i550 Cabinet ships
  in the library with its object dictionaries.
- **The reTerminal EtherCAT example shows current, torque, DC link and
  frequency.** The i550 lets a master map its user-configurable
  process data; the example does it with SDO writes at start (the
  assignment cleared, the mapping written, the assignment set to both
  PDOs) and the screen shows the same numbers as the CAN twin.
- **What a slave is told at start, and what it sends, are now set in
  the editor.** The EtherCAT page shows a slave's **start-up writes**
  (they travelled in projects before, with no window to see or change
  them) and adds them from the device's own object dictionary — picked
  by name, sized by the vendor. **Map from the device** goes further:
  tick the values the drive or terminal should send or receive, and the
  editor writes the whole plan — the mapping, the assignment in the
  order the standard wants, the signals behind the device's own data,
  their variables and the image size. Mapping again replaces that plan
  instead of adding to it.
- **An EtherCAT device has the window a CAN device has.** Double-click a
  slave in the tree and it opens with the same tabs: the device (its
  identity from the vendor's description, the process image, the CiA 402
  layout), its variables, the PDO mapping in both directions, the
  start-up writes, the I/O mapping and the device log. The EtherCAT page
  keeps what a master page keeps, the cycle and the list of slaves.
- **One CAN node on a Linux device, not two.** There the bus *is* the
  interface, so the tree says *CAN (can0)* and the devices and axes hang
  directly under it. The separate *CANopen master* row belonged to the
  boards, where CAN is the board's own peripheral, and stays there.
- **CAN buses and RS-485 lines share one budget on a Linux device.**
  Each one past the board's own is a chip on the SPI bus, and a
  Raspberry's standard SPI has four selects: four CAN, four RS-485, or
  two of each. The fifth is refused, with the reason.
- **A refused start-up SDO says why.** When a slave refuses one of the
  project's SDO writes at start, the runtime prints the slave's abort
  reason with it — before, the line said only *rejected*.
- **The reTerminal example.** `reterminal_example` — the board's own
  project: a Lenze i550 driven over CANopen from one screen (the dial,
  START/STOP with a confirmation, setpoint, direction, ramps, current,
  torque, DC link, frequency, error code, the CiA 402 lamps, a trend),
  the RS-485 pair with two slaves, the device's UPS and sensors, and
  the alarms — on the glass and on a phone. The page:
  [reTerminal](example-reterminal.md).
- **Settings.** *Tools -> Settings* holds the three things a person
  actually changes - the language, the theme, and whether the editor
  looks for a new version and says so. Turned off, the editor never
  reaches the network on its own. The language and the theme moved here
  from two different menus.
- **The reTerminal example as the panel of a SIMATIC.**
  `reterminal_s7_example` — the same board with no fieldbus at all: a
  data block of an S7-1200 read live with the controller's own
  addresses beside the values, one INT typed back, the PLC's clock bit
  as the link lamp and the panel's own counter beside it, so a stopped
  controller cannot be mistaken for a stopped panel. The page:
  [reTerminal — the panel of a SIMATIC](example-reterminal-s7.md).
- **The STM32F746 showcase in daylight, with a SIMATIC on it.** The
  example starts in the light theme and its screens were relit — an
  unlit lamp, a track and a field used to be drawn black, which nobody
  saw while the screens were dark. Two screens are new: the data block
  of an S7-1200 read live with one value written back, and a trend
  carrying the board's own value beside the controller's with the
  alarm list under them. The page:
  [Showcase — STM32F746 Discovery](example-showcase.md).
- **A value typed into a +7 variable always reaches the PLC.** A change
  made while the client was inside its cycle could be undone by that
  cycle's own read, and the write then never left — about two in every
  eight on a busy screen, with nothing said anywhere. A pending change
  now owns the variable until it has been sent, and a write the
  controller refuses is said once in the diagnostic buffer and the
  variable goes back to showing what the controller really holds.
- **The rows of an alarm table are readable on a light screen.** Their
  text was a fixed white, so an alarm list on a light theme was an
  empty box with a coloured stripe; the colour now comes from the
  style, and from the table's own background when the style does not
  name one. The recipe table had the same fixed white.
- **The reTerminal example with the drive on EtherCAT.**
  `reterminal_ecat_example` — the same project with the i550 as an
  EtherCAT slave on the E10-1's second network port: the axis names
  the EtherCAT backend, an `ethercat:` section describes the slave and
  its signals, the rest is untouched. The page:
  [reTerminal, drive on EtherCAT](example-reterminal-ecat.md).
- **EtherCAT master: the PDO assignment written to the slave.** A
  slave that expects its master to write the PDO assignment (the
  Lenze i550 raised "PDO mapping error" and sent zeros) gets it at
  every start; a slave's state is read after the bus comes up, so a
  drive is under program control from the first cycle.
- **EtherCAT: a slave that comes back.** A slave that was switched
  off and on (a drive after a reset by hand) is configured again and
  rejoins the cycle instead of flapping between lost and found twice a
  second; a drive found in fault when the line starts gets one fault
  reset, so START works without a visit to the drive.
- **net32 over UDP keeps its multicast membership.** A device asks for
  its multicast group again every half minute — a network that forgot
  the membership had left a device sending for a day and hearing
  nothing.
- **`SYS.MB_OK` and `SYS.CAN_OK` on a Linux device.** Both facts follow
  the Modbus master and the CAN interface as on every ESP32 board; they
  read false before, whatever the buses did.
- **The New project wizard lists the boards by manufacturer** again,
  with a heading per manufacturer and ours first; the filter searches
  across all of them.
- **An RS-485 system example.** `rs485_system` — a reTerminal with the
  E10-1 as the Modbus RTU master of two slaves on one pair (an
  inoCORE32-TM8.6 with three RTD zones, an inoCORE32-TM1.1 panel),
  and the CANopen master of an i550 on the E10-1's CAN. The master's
  screen shows every slave, writes their setpoints and starts their
  machines; each slave keeps its own program. One project, deployed as
  one. The page: [RS-485 system](example-rs485.md).
- **RS-485 direction from GPIO lines.** A Linux device whose serial
  port has no RTS on the wire (the reTerminal E10-1) drives its
  transceiver from the GPIO lines the board wires — the editor writes
  them with the port, the device's console says which. Proven with the
  E10-1 on a live pair.
- **32-bit integers over Modbus, both ways.** A master's `i32`/`u32`
  variable is read from two registers, as the documentation always
  said (it read one before), and a master WRITES a 32-bit value —
  a setpoint, a counter — as two registers in one request, which a
  ctrl32 slave (and every other) accepts; before, such a write was
  silently not made.
- **Modbus RTU timing per the specification.** The silence between
  frames is the standard's 3.5 characters at the line's baud rate, on
  the master (before a request that follows a reply) and on every
  slave (the end of a frame) — before, a master polling several slaves
  could lose the first request after another slave's reply. Devices on
  one pair should carry this version together.
- **A CAN interface left in listen-only mode is set right.** A device's
  CAN interface found listen-only (a passive look with `candump` that
  was never undone) is brought back to a normal link when the runtime
  starts — before, every request to a drive timed out with nothing
  saying why.

- **CAN on a Linux device needs nobody at its shell.** The runtime
  sets the CAN interface's bitrate from the project and brings the
  interface up itself when it starts — every bus its own speed, bus-off
  recovery included. The commented `ip link` line in the service unit
  is gone; a runtime started by hand from a shell still prints the line
  to run once as root. The log says which it did: *set by the runtime*
  or *as found*.
- **Modbus TCP slave on Linux.** A Linux device answers a SCADA, a PLC
  or another ctrl32 device as a Modbus TCP slave on port 502 (or the
  port the project sets), up to four connections at once — as every
  ESP32 board has. Before this release the Linux runtime served Modbus
  RTU only and said so.
- **The operating system of a Linux device, from the editor.** Under
  *Prepare a Linux device*, after a Look, the editor sets what a
  project cannot: the boot lines an expansion board needs (a preset
  for the reTerminal E10-1), the login console off the serial port,
  the I2C driver at every start, the device name and the network
  (DHCP or a fixed address). It lists the steps before Apply, checks
  each on the device afterwards, restarts the device only when a boot
  setting changed, and refuses in words what the device cannot take.
- **The UPS as system variables.** A Linux device with a battery
  (the reTerminal with its E10-1) reports `SYS.ON_BATTERY`,
  `SYS.CHARGING`, `SYS.BATTERY_PRESENT`, `SYS.BATTERY_VOLTAGE`,
  `SYS.INPUT_VOLTAGE` and `SYS.BATTERY_PERCENT` (-1 where the device
  has no gauge) — a program saves, warns or stops when the supply
  goes. The device page's scan shows the same line.
- **Three more chips in the peripheral library.** `LIS3DH` (a 3-axis
  accelerometer, the reTerminal's own), `LIS331DLH` (its sibling) and
  `BQ25790` (the buck-boost battery charger of the reTerminal E10-1
  UPS: supply and battery voltage and current, charge state, supply
  present, die temperature) - as project peripherals with their own
  drivers, named by the device scanner, listed as fitted on the
  reTerminal and proven on it.
- **The device's own sensors as system variables.** Where the device
  has them (the reTerminal): `SYS.ACCEL_X/Y/Z` in g, `SYS.TILT` in
  degrees, `SYS.SHOCK_G` (the largest acceleration of the last two
  seconds — a knock, a drop, a vibrating machine) and `SYS.LIGHT` in
  lux (-1 without a light sensor).
- **Bus problems in words.** A serial port the runtime may not open
  says which group it needs; a port that does not exist says what
  driver or overlay would make it; a port that is the device's own
  login console — the Raspberry Pi default — is named the moment it
  opens, because a login shell on the same UART answers Modbus frames
  with a prompt and the slave "never answers". An EtherCAT interface
  with only a link-local address (nobody configured it) is accepted,
  and one that is down is brought up.

## 1.00.049

- **Modbus RTU on RS485 works on every ESP32 board.** The RS485 line
  opens the moment a project uses it: a device on the RS485 line, or
  the panel answering as a Modbus RTU slave. Before this release the
  line stayed closed on every ESP32 board (a compiled switch nobody
  could reach), so Modbus RTU worked only on the Linux runtime. Proven
  on two boards over one A/B pair: a master reads a slave's temperature
  bit for bit. Headless boards report the state of every Modbus device
  on the console as the display boards do. The F7 Discovery has no RS485
  transceiver, so the hardware table says so.

## 1.00.048

- **Home automation blocks.** The `home` block library brings the wall
  button and what it drives: PUSHBUTTON (short, long), MULTICLICK,
  TOGGLE, STAIRLIGHT, DIMMER with PWM, BLINDS with TRAVEL (roller
  shutter or venetian), PRESENCE, TWILIGHT, THERMOSTAT and DAYTIME - and
  the house around them: SUNTIMES and ASTRO (sunrise and sunset for a
  place), SCHEDULE, SCENE, GATE, VENT, CENTRAL and ENERGY. They are ST
  blocks you can read and copy, the Toolbox lists them under *Home*,
  and every one is held by a simulation test. See
  [Home automation](blocks-home.md) and the example `home_blocks.prj32`.
- **Maths in ST.** `SQRT`, `SIN`, `COS`, `TAN`, `ASIN`, `ACOS`, `ATAN`,
  `EXP`, `LN`, `LOG` and `EXPT` on REAL. A project using them needs this
  version's runtime on the device (pack format 61).
- **Your own block takes parameters.** A `VAR_INPUT` with a default
  (`PT : TIME := T#3m;`) in an ST function block is a parameter row
  inside the box - a literal or a bound variable - and a block may use
  another block of the project inside. Program and block variables
  take initial values (`x : INT := 5;`).
- **The clock as variables.** `SYS.HOUR`, `SYS.MINUTE`, `SYS.WEEKDAY`,
  `SYS.MINUTE_OF_DAY`, `SYS.DAY`, `SYS.MONTH`, `SYS.YEAR` and
  `SYS.DAY_OF_YEAR` in the project's time zone (*clock: tz*), on every
  device. See [Variables](variables.md).
- **The simulation counts exact milliseconds** when a test drives it, so
  a timing test gives the same answer on every PC.
- **The STM32 F7 updates its runtime over the network.** The board keeps
  a small loader that never changes and swaps the runtime through its
  QSPI memory: the running one is kept aside, the new one is written and
  verified, a runtime that does not confirm itself is put back at the
  next start. Type the board's address instead of a COM port in *Flash
  runtime*; the one-time move onto this layout is a *Flash runtime* over
  the ST-LINK, which writes both parts. See [Quick start](quickstart.md).
- **The F7 console says what happened.** A fault reports where it
  happened and restarts the board; lines printed by several parts of
  the runtime at once no longer garble each other.

## 1.00.047

- **The editor speaks eleven languages.** Czech, Polish, Hungarian,
  German, Italian, Romanian and Ukrainian join English, Slovak, Spanish
  and Turkish (*View → Language*; the first start picks the language
  your Windows runs in). The translations were made with the product
  glossary — a wrong word in your language is worth a message.
- **A rung calls a program.** The box menu of a rung and the palette
  offer the other programs of the project under *Programs*; the program
  runs while the rung conducts, the same way an FBD box or `STATS();` in
  ST calls it. See [Ladder](ladder.md).
- **Tasks on every device.** The third and fourth task report their
  cycle time and overruns (`SYS.CYCLE3_US` … `SYS.OVERRUNS4`), the
  Diagnostics page shows every task and the Resources page lists the
  programs of each.
- **Room on 4 MB devices.** The two 4 MB display runtimes are compiled
  for size and no longer carry the largest built-in font; a project that
  draws with the 36 px face carries it in its own pack. See
  [Limits](limits.md).

## 1.00.046

- **System variables.** Every project has a `SYS.` set the device
  writes each cycle — the uptime, the cycle time and its overruns, the
  state of CAN, Ethernet, WiFi, MQTT, Modbus and the +7 connection, the
  retentive store, the clock — usable from LD, FBD, ST and every screen
  like any variable. `SYS.RETAIN_SAVE` writes the retentive values to
  the chip the moment it is set (put it on a keypad's OK), and the
  project's Application page sets how often they are written otherwise.
  See [Variables](variables.md).
- **Tasks like a PLC.** Up to four cyclic tasks with their periods,
  priority by period, the programs of a task in the order they run, and
  a program that calls another program (`STATS();` in ST, a program box
  in FBD). A program nothing calls stays in the project and does not
  run; the tree says so. See [Editor](editor.md).
- **The WEBview keypad speaks the variable's unit.** A `TIME` was shown
  and taken in milliseconds in the browser while the board's keypad
  spoke seconds, and a widget without limits clamped every entry to
  zero. The browser follows the board's rules now.
- **The board card names the processor** — its type, RAM, flash and
  PSRAM come from the module the board carries, and the analog input
  pins get their variable from the pin row.

## 1.00.045

- **The Toolbox and the insert menu offer every in-rung block.** The
  right-click palette on a rung already did. The other two ways of
  reaching the same blocks kept an older list of five, so which blocks
  you could drop into a rung depended on where you asked for them. All
  three now offer the same set, grouped by category.

## 1.00.044

- **A block on an empty rung runs.** A timer, a blinker or an addition
  dropped on a rung with nothing in front of it was gated by a rail the
  program never switched on: the block did nothing, showed nothing, and
  the ladder looked right. It runs now, and the two engines are compared
  on exactly that shape before every release.
- **Every block, with EN/ENO or in the rung.** The palette used to offer
  the in-rung form for five blocks; it offers it for every block whose
  power flow can pass through it — triggers, flip-flops, the blinker,
  the motor and valve blocks, the whole motion set. A block with a
  number on either end stays a box, and the menu says which is which.
- **The variable list under a pin scrolls.** It drew the first eight
  candidates and stopped, so a variable created later — always the last
  one — could not be picked at all. It now holds every candidate, in the
  order the variable table shows them, and opens on the one that is
  bound.
- **An unfinished rung survives leaving the page.** A rung the build
  still refuses lives only in the drawing; switching to another window
  and back used to throw it away as soon as anything else in the project
  had moved.
- **A time parameter reads `T#1s` everywhere.** The box form of a block
  printed the bare millisecond number.
- **The editor updates itself, safely.** *Help → New version* downloads
  the installer and checks it twice before it may run: its fingerprint
  against the signed notice, and the publisher's signature. Install
  closes the editor and starts it — only with the project saved.
- **The editor speaks four languages.** English, Slovak, Spanish and
  Turkish, chosen in *View → Language*; the first start follows Windows.
  More are being translated.
- **Modules with a headless runtime** — the PICO-V3-02 class — create,
  build and flash. They used to be refused both ways round.
- **Every function block in pictures.** Each block's page shows it on a
  rung, its Structured Text as text you can copy, and its card on a
  WEBview screen, all from one project that ships with the examples.

## 1.00.043

- **Durations read as `T#1s500ms`.** Every time parameter — on the
  block's stub in a rung, in the sheet, in the block-diagram field, in
  the ST a diagram renders to, and the live `ET` while online — is
  written the IEC way. A bare number typed into a time field still
  means milliseconds.
- **A block's pin takes the variable you click.** Picking a variable
  from the list under a pin field binds it; the list used to close on
  the click. Typing a new name and Enter creates the variable.
- **The Properties panel follows the page in front.** A page opened
  from the tree takes the tab at once and the panel shows its selection
  — nothing while a page without a sheet (styles, a device, WiFi) is
  in front.
- **Rungs and comments.** A rung's comment sits on a grey plate across
  the whole rung; a variable's description is centred above its name.
  A block inserted before or after a contact inside a parallel branch
  goes into that branch.
- **The variable table** centres every column but the name; the
  Text/Table switch works with Modbus variables, also over edited text.
  The register maps of the shipped Modbus meters create their
  variables.
- **The simulation runs what the panel runs.** Test mode executes the
  same program the download would carry — ladder and block diagrams
  rendered to structured text, your own function blocks included — and
  every axis of the project gets a simulated drive: Enable brings it to
  operation, the velocity follows the setpoint with the ramps you set,
  the gauge and the trend move. A timer's `ET` or a blinker's `REM`
  shows its running value in the simulation as it does online.
- **Smaller things.** The new-project list names the processor module
  beside every board; the Toolbox groups open with +/-; the ladder
  toolbar symbols sit centred; the Serial, I2C and SPI nodes add a
  device from the right-click menu only; a Modbus device window states
  its transport instead of offering a switch; the Resources bars centre
  their numbers. The application icon is a white "32" on a dark plate
  so it reads on any desktop and taskbar; the window's title bar keeps
  the blue one.

## 1.00.042

- **Step by step.** Four procedures with pictures: [a new project](tutorial.md)
  through the wizard, [your own function block](own-block.md), [downloading
  a program](deploy.md) over USB and over the network, and [a drive over
  CAN](tutorial-i550-can.md) from the wiring and the DIP switches to the
  first turn of the motor. The three projects they build ship as tutorials
  (`first_light`, `own_block`, `i550_axis`). Every screenshot in the
  documentation is regenerated from this version.
- **A TIME reads as a duration.** A screen shows a `TIME` variable as
  `900ms`, `2s500ms`, `10s`, `1m5s` — on the glass and in the browser; the
  keypad still takes the number in the variable's unit. The editor opens
  in its light face. ONLINE, in ladder and FBD, a wire, a contact, a
  block frame or a coil that does not conduct is drawn as a fine dashed
  line; what conducts is solid green, as before.
- **FBD has networks, not a canvas.** An FBD program is a stack of
  numbered networks like ladder rungs: *+ Network*, a comment lane on a
  grey plate, blocks inside the strip, the strips packed top-down;
  insert, move (the execution order follows), delete with the blocks.
  A page you open docks into the tab bar at once. A tree node with
  nothing under it is a leaf, never a `+`. Every `x` button sits on
  its row's line.
- **Variables are typed, not hunted.** Every variable field of a contact,
  a coil or a block pin, in the sheet and in Properties, in ladder and in
  FBD, is a text field with a filtered list under it; Enter binds the
  match or creates the variable under the typed name. The coil is drawn
  as `( )`; rung comments sit on a grey plate in black; pin names sit on
  the height of their stubs; the rung toolbar and every dropdown arrow
  follow the toolbar rule.
- **A function block drawn in ladder stays ladder.** A saved project
  reopened its LD blocks as FBD, rungs gone; the language is now saved
  with the block. The block sheet lists each parameter once. A device the
  axis wizard makes no longer repeats the node in its name.
- **Properties for every block.** Click a contact, coil or block in a
  ladder rung or an FBD diagram and the Properties panel shows its
  variables, parameters and axis, editable - one table, pin by pin, the
  same in the double-click sheet. An unfinished rung survives a
  visit to another program. The Toolbox opens folded. A program keeps the
  language it was created in (the view switch is gone). The interface
  pane lists only variables you created. The pin rule holds everywhere: a
  BOOL pin takes a BOOL or one bit of an integer variable, a numeric pin
  or parameter takes a number and never a BOOL. A time or count
  parameter fed from a REAL variable compiles now — every shipped block
  is built with every pin bound to a variable of its type in the release
  gate.
- **CAN axis wizard.** Adding a CAN axis makes the axis, its CAN device
  with the PDOs the runtime exchanges and the variables the MC blocks
  bind to, in one dialog - single-word names, a prefix for a second
  axis. See [Motion blocks](blocks-motion.md).
- **Editor: what was made can be changed.** The bit of a contact or
  coil on `mask.3` has its own field in the element's sheet; a recipe
  definition is renamed in place; changing a CAN device's node-ID or a
  Modbus device's unit moves the device's variables (and its axis) with
  it instead of leaving them behind.
- **Recipes.** A recipe definition names the variables a set carries;
  the device keeps the sets in its own store, through power cuts and
  program downloads. A recipe table and three button modes (load, save,
  delete) go on any screen; WEBview renames a set with a tap. Every
  ESP32 and Linux target; STM32 refuses a definition for now. New page
  [Recipes](recipes.md).
- **The Linux runtime updates over the network too.** *Flash runtime* with
  the device's IP sends the runtime out of the installer's bundle; the
  device verifies it is built for its processor, runs it once as a
  self-check, switches, and rolls back by itself if the new runtime does
  not come up. The device page shows `ota=1`, the build (`env=`) and the
  slot it runs from.

## 1.00.041

- **The runtime updates over the network.** Boards with 8 MB or 16 MB of
  flash carry two runtime slots: *Flash runtime* with the board's IP in the
  port selector sends the runtime the way a program is sent, the board
  writes the slot it is not running from, verifies it is a runtime for its
  own chip and memory, restarts and confirms itself once the program has
  loaded; a runtime that does not come up is rolled back by the bootloader.
  The one USB flash that brings a board onto the two-slot layout keeps its
  program and retentive values. 4 MB boards keep the USB road.
- The device page and the scanner show `ota=`, the runtime's build (`env=`)
  and the slot it runs from.

## 1.00.040

- **The editor starts empty and New project is a wizard.** One window
  asks for the name, the folder (`Documents\ctrl32\projects` unless you
  browse elsewhere), the board or the processor module, and what the
  project does — visualization, WEBview, ladder or ST, CAN, Modbus,
  MQTT, net32 — and creates the whole project from those ticks. See
  [Quick start](quickstart.md#3-your-own-project).
- **Your own board with a display.** A project on a module declares its
  glass on the board tab: the catalog board with the same display
  controller, the size as mounted, the display and touch pins. The
  editor checks the pins and builds the same display record the catalog
  board gets.
- **A module can run headless.** Every processor module now has two
  runtimes: with a display, or headless with the bigger program limits
  (64 kB program, 24 kB instances, 1024 blocks) for a project that shows
  its screens in WEBview only. The wizard's *Visualization* tick picks
  it; the board tab lets you change it. See
  [Modules](modules.md) and [Performance and limits](limits.md).
- **The LITE class.** A classic module without extra memory carries 128
  variables, 32 alarms, 128 blocks and one axis — with those limits the
  same board runs its display, WiFi with the access point, CAN and
  WEBview together. The catalog says which boards it covers.
- **Ladder blocks.** Every pin of a block is drawn always; a motion block
  carries its axis on the rung (one axis assigns itself, more need the
  choice on the block); a block dropped inside a function block binds to
  the block's own inputs and outputs; blocks without outputs work as
  boxes; a box on an empty rung stays a box.
- **The device reports what it was built for.** The runtime tells the
  editor its variable, alarm and axis capacities, and the editor's
  checks compare them with the catalog.

## 1.00.035

- **net32 — our device network.** ctrl32 devices now work as one
  system — the backbone for home automation. One
  device owns a variable, others subscribe to it by node and name;
  writes travel to the owner as commands. Works over WiFi, ethernet
  and CAN; a silent peer marks its variables stale, drops its health
  flag and never fires queued writes — local logic keeps running.
  The whole story: [net32](net32.md).
- **One project for the whole system.** A single `.prj32` can hold
  every device of an installation: switch devices in the tree, wire
  their shared variables on the net32 canvas by dragging between
  cards — both sides of every subscription are generated for you —
  and **Deploy all** uploads every device over its own connection.
  See [the system project](net32.md#the-system-project).
- **An AI assistant can join your editor session.** Tools → MCP
  server connects an AI assistant (any MCP client) to the project you
  have open: it reads variables, screens and programs, builds, and
  makes edits you can undo with Ctrl+Z — on this computer only, off
  by default, behind a per-session token, with live-board writes
  behind an extra consent switch. See
  [the editor page](editor.md#ai-assistant-connection-mcp-server).
- **4 MB display boards get a slightly larger firmware area.** The
  update itself repartitions the flash — after this runtime update,
  upload the program to the board again (one extra step, one time).

## 1.00.034

- **+7 — the panel talks to an S7 PLC.** A ctrl32 panel can
  replace the operator panel on an existing S7 installation: it reads
  and writes data blocks and flag bits over ethernet, the PLC program
  stays untouched, no GSD files and no TIA project needed. S7-300/400
  work as delivered; an S7-1200/1500 needs PUT/GET enabled and
  non-optimized DBs. Runs on P4, STM32 F7 and Linux devices. The
  whole story: [+7 (S7 PLC)](plus7.md).
- **The device tree shows the +7 link state live** — connected /
  connecting / link down, with request and error counters, on the
  node and on the +7 page.
- **Programs saved by editor 1.00.032 load correctly again.** A
  1.00.033 board could refuse such a program as "corrupted" after a
  runtime update — nothing was corrupted, the reader mis-measured
  the older file's header. Rebuilding the program was never needed;
  updating the runtime to 1.00.034 is the fix.

## 1.00.033

- **A device that answers Modbus TCP now frees a dead connection on
  its own.** A client that vanished without closing (power cut, WiFi
  drop) used to hold the slave's single slot until a restart; an idle
  connection is now dropped after 60 s and the next client gets
  served.
- **Going online no longer asks for a download it does not need.**
  The installed editor compared its own build of the project against
  the panel without the board's facts and kept demanding a new
  program; the comparison now builds with the full board card, and a
  permanent test guards it.
- **Buttons wired through the touch controller's I2C pins work
  again** on boards where the display and the buttons share the bus.
- **The Devices scanner ages its information honestly** — a board's
  address and firmware line fade out when they stop being fresh
  instead of pretending to be live.

## 1.00.032

- **A boot splash.** The panel puts a picture on the glass right
  after power-on — your own image or the ctrl32 mark — and holds it
  until the runtime is up and the configured minimum has passed, so
  the display no longer flickers dark while WiFi or the broker
  connect. Pick the image and the time on the HMIview page
  (0 s turns it off).
- **A button can change its caption when ON.** A latching button
  says START while off and STOP while lit — set *text when ON* in
  the inspector; the ON colour is the style's accent, as before.
- **The gauge's centre number is optional.** On small glass it often
  crowds the dial — one checkbox (*Center number*) hides it, and a
  separate value widget can take its place.
- **Projects are `.prj32` files.** The editor opens and saves the
  package form only, and every example and tutorial ships as one —
  the Welcome page, the Examples menu and the recent list all speak
  it. See [Project format](project-format.md).
- **OPC UA with certificates.** The Linux runtime offers Basic256Sha256
  (and AES) sign-and-encrypt endpoints; the certificate is managed
  from the OPC UA page — self-signed, your own PEM/DER pair, or
  encryption off. A variable can also be kept **off the server**
  with one checkbox. See [The Linux runtime](linux-runtime.md).
- **A USB mouse on a Linux device just works** — plug it in, a cursor
  appears, a click presses like a finger. The on-screen keypad now
  scales with the glass.
- **The Modbus device card creates its variables.** One button makes
  a variable for every register (and keeps them in step with the map
  when it changes); a `+` on a row creates just that one. See
  [Modbus](modbus.md).
- **Limits follow the target everywhere.** A Linux project shows and
  uses the ten-fold numbers in every editor check, not only at build
  time. See [Limits](limits.md).
- Boards that physically carry SPI, I²C or a serial line now say so
  in the catalogue — the device tree offers what the hardware has.

## 1.00.031

!!! warning "Update the boards first"
    The program pack format moved again: **flash the new runtime onto
    a board before sending it a program built by this editor.** The
    board refuses a newer pack loudly and keeps running the old one.

- **One runtime reads another over OPC UA.** A Linux target can name
  an OPC UA server and source variables from its nodes
  (`source: opcua`) — browse the server on the OPC UA page, import,
  and the values are polled in at runtime. See
  [The Linux runtime](linux-runtime.md).
- **The Linux runtime.** ctrl32 now also runs as a Linux program on
  catalogue devices — Seeed reTerminal (5", Raspberry Pi CM4) and
  the ST STM32MP157C-DK2. Same project file, same editor; the device
  boots into the visualisation, takes downloads over the network,
  goes online like any board, and serves **every variable over OPC
  UA**. Limits are roughly **ten times** the microcontroller
  numbers. See [The Linux runtime](linux-runtime.md).
- **MQTT over TLS.** The broker connection can be encrypted on S3,
  P4 and STM32 boards — the editor refuses the combination the
  hardware cannot carry, at your desk. See [MQTT](mqtt.md).
- **Set up WiFi and MQTT on the glass.** Two reserved screens —
  `sys_settings` and `sys_terminal` — let an operator repoint a
  board to a different network or broker, and watch the MQTT
  traffic live, without the editor. See [MQTT](mqtt.md).
- **Bus pins on the board page.** CAN, RS485, I²C and SPI positions
  are assigned on the board page from a list of **allowed pins** —
  pins the chip cannot give you are simply not offered, and boards
  that route a bus themselves show it fixed.
- **The MQTT page.** The whole MQTT configuration sits on its page
  now — no dialog in between.
- **HMIview settings.** Clicking HMIview in the tree opens its
  settings — the resolution (free on targets that scale, fixed
  where the glass decides) and the WEBview canvas size.
- **The scanner sees more.** Linux runtimes appear in the device
  scanner next to the boards; a device reachable over two networks
  shows as one row, not two.

## 1.00.029

!!! warning "Update the boards first"
    This release changes the program pack format: **flash the new
    runtime onto a board before sending it a program built by this
    editor.** The board refuses a newer pack loudly and keeps running
    the old one — nothing breaks, it just tells you to update.

- **Home Assistant.** A board can now publish its variables over MQTT
  and appear in Home Assistant on its own — switches, numbers and
  sensors, discovered automatically, no YAML on the Home Assistant
  side. Two step-by-step tutorials ship with the editor: a thermostat
  that reads its temperature from a Zigbee sensor, and a light panel
  that switches and dims real bulbs. See
  [Home Assistant](home-assistant.md).
- **Buses on the pins you choose.** CAN, RS485, I²C and SPI pins are
  part of the project now — set them in the editor and they travel
  with the program; leave them alone and the board's own defaults
  apply. RS485 works in three wiring shapes: separate DE and RE, the
  two tied together, or an auto-direction converter with just TX/RX.
- **Headless boards take bigger programs.** A board without a display
  spends no memory on drawing, so it holds twice the program: 64 kB of
  compiled logic, 24 kB of block instances, 1024 ladder blocks. The
  editor knows which type it is building for and checks the right
  limits at the desk. See [Limits](limits.md).
- **Analog inputs.** A variable can read the board's own ADC —
  calibrated millivolts, with gain and offset for a battery divider or
  a potentiometer. For real measurement duty an external ADS1115-class
  converter is still the answer, and the editor says so.
- **WEBview is a choice.** A project can mirror the display screens to
  the browser, draw an independent set for it — or switch WEBview off
  entirely and give its memory to the program. The smallest boards
  gain the most: the thermostat tutorial runs on a board where the
  browser server and MQTT would not fit together.
- **A vanished Modbus device no longer freezes the display.** On STM32,
  a slave that stopped answering could hold the screen and the console
  hostage for tens of seconds while the program ran on underneath.
  Communication now waits in its own lane; the glass never rides along.
- **Remembered values check their type.** A retained variable is
  restored only when its stored type matches — a new project reusing a
  name from an old one starts from its own initial value instead of
  inheriting foreign bits, and the diagnostic buffer says when that
  happened.
- WiFi joining is more patient: a board whose access point comes up
  late — a paired board restarting, a router rebooting — retries and
  falls back instead of giving up.

## 1.00.028

- **Find devices.** The :ti-eyeglass: button next to the port picker
  sweeps every COM port and the local network and lists what answered:
  which board, **which program it runs**, its firmware version and its
  address. *Use* on a row points the editor at that board — and opens
  the matching project when it is in your recent list. See
  [Finding your boards](find-devices.md).
- **Boards introduce themselves by program name.** The project's name
  travels with the download, so ten identical boards stop being
  identical — each one says which job it holds, in the scanner and to
  anything else that asks.
- **One version, everywhere.** The editor and every runtime it installs
  now carry the same version number, and the dialogs check it: the
  runtime flasher refuses a stale file, the download dialog says when
  the board should be updated first. "Half of it left old" can no
  longer happen quietly.
- **States and motion now behave on the glass.** A widget driven only
  by a state or a path never redrew on the board's display — the
  marker sat still while the browser moved. Both renderers now agree,
  in both directions: state lamps light in the browser too.
- **Live ladder on STM32.** Online mode on an STM32 board now shows the
  power flow and the values inside a rung — the wires between blocks
  were frozen on this family; they animate exactly as on ESP32 now.
- **A CAN fault no longer restarts the board.** A bus nobody answers —
  a broken transceiver, a shorted pair — used to reboot the whole
  board in a loop. It now recovers on its own and keeps the program
  running; communication is never worth the logic.
- Network program upload is offered only on boards with the memory to
  take it; the smallest ones say so plainly and keep the USB path.

## 1.00.027

- **States and motion on any widget.** A widget can now carry three
  states — true, false and alarm — with a colour for each, driven by a
  variable or by **one bit of an integer**. Four lamps on four bits of a
  status word, no logic between them. And any widget can **travel a
  path** as a value sweeps its range: along a line, or with X and Y
  driven by two values independently. Drawn in the editor, identical on
  the board and in the browser.
- **Vector icons.** Icons are outlines rather than baked bitmaps, so
  they are sharp at any size — a 16-pixel status glyph and a
  screen-filling symbol come from the same entry. A full-screen icon
  used to cost a couple of hundred kilobytes; it now costs tens of
  bytes, and the browser draws them too, which it never could before.
- **Buttons work in online mode.** Pressing a control on the editor's
  canvas while connected now reaches the running board, instead of
  writing into the editor's own copy of the values. Screens switched
  before; everything else looked dead.
- **STM32 boards are written by the editor.** No external tools: the
  editor speaks to the ST-LINK probe directly and writes the board over
  SWD, verifying every byte it wrote before resetting.
- **Colours written as `#RRGGBB` work.** The web spelling everybody
  reaches for used to yield black, silently. Both spellings parse now —
  worth re-checking any colour in an older project that never looked
  right.

## 1.00.026

- **The first STM32 board.** The runtime now runs on STM32F7-class
  hardware (bring-up board: the ST 32F746G-DISCOVERY — 480×272 touch
  glass, ethernet, 8 MB RAM, 16 MB flash). The same project, the same
  pack, the same editor: pick the board and upload. The PLC dispatch
  loop executes from the chip's zero-wait instruction RAM and the
  display is pushed by the 2D DMA engine, so the logic cycle and the
  glass never fight for time.
- **Everything over ethernet.** A network board now serves the full
  WEBview from its own address, accepts program uploads over the wire
  (*Download → Network* in the editor, no cable swap), and — new — the
  editor's **online mode works over ethernet too**: type the board's
  IP where you would pick a COM port and watch live values, the
  console, the scope and forcing exactly as over USB. One protocol,
  two wires.
- **The board knows the time.** With ethernet up it sets its clock
  from the internet automatically (NTP), and the browser can set it
  by hand on a closed network. Alarm and diagnostic timestamps mean
  something now.
- **Retentive values without extra chips.** On the STM32 the variables
  marked *persist* survive restarts and program uploads in the
  processor's own battery-domain memory — no EEPROM wiring, no wear,
  and with a backup battery fitted they survive power loss outright.

## 1.00.023

- **A classic board with a display gets the network.** Boards without
  PSRAM that light a screen used to skip the network stage entirely —
  the memory simply was not there. The firmware stopped paying for a
  demo it never shows, and the freed memory carries an ethernet-only
  WEBview: one viewer, straight from the board. The Olimex EVB wall
  thermostat now serves its Home Assistant banner from the glass.

## 1.00.022

- **Every network board answers Modbus TCP.** Headless runtimes (the
  Olimex PoE family, the generic presets and friends) now run the
  same Modbus TCP slave the display boards always had — a SCADA can
  read and write the variable map on port 502 without a screen attached.
  A pack asking for RTU on a board with no RS485 wired says so on
  the console instead of listening on nothing.
- **The P4 showcase demonstrates bit access live.** A new *Bit
  access* screen (reached from Control): the logic blinks one bit,
  the lamp test drives another, and six switches — on the glass and
  in the browser at once — own the middle of the same word. Proven
  under fire: hundreds of browser toggles against the running logic
  with not one lost write.
- The bench tooling is a single program now; the sample-project
  headers name it instead of retired scripts.

## 1.00.020

- **Bits, everywhere.** Every bit of an integer variable is addressable on
  its own: `IF status.5 THEN` and `mask.0 := ready;` in ST, contacts
  and coils on `variable.bit` in ladder and FBD, the widgets as before —
  one meaning across all of them. The index is checked against the
  variable's width at build time, in the spelling your fingers
  already know.
- **A bit write never loses a neighbour.** Writing one bit from the
  logic while a browser switch flips another and a Modbus master
  rewrites the word is safe — every bit write is atomic. This also
  fixes a real race: a browser switch used to write the whole word
  back from a stale snapshot and could wipe bits the PLC or a Modbus
  master had just changed.
- **Bitwise toolbox.** On integers, `AND`/`OR`/`XOR`/`NOT` are
  bitwise and `SHL`/`SHR` shift — as operators and as functions.
  Building LED masks no longer needs arithmetic gymnastics.
- Program packs are format 48; the board needs this release's
  runtime (the editor tells you, in orange, when it does not have it).

## 1.00.019

- **Every board's firmware is current.** Nine runtimes had lagged
  behind since mid-August (the Olimex PoE family, the generic
  presets, inoCORE32-TM1.0); all nineteen in the catalog are now
  built from the same day's firmware, at the full 240 MHz.
- **The project-vs-board check works in the installed editor.** The
  full validation — display and resolution, buses, pins, peripheral
  limits, pack size against the flash slot — runs inside every build,
  with the same wording everywhere. Until now the installed editor
  silently skipped parts of it that only worked in our development
  tree.
- The documentation gained screenshots of the editor on every major
  page, and its web navigation is grouped into sections.
- Sample projects speak English throughout, including the variable names
  in the seal-in classic.

## 1.00.018

- The bold icon actually reaches the editor now — a stale build cache
  kept the first, timid draft inside the program while the installer
  already wore the new one. If Windows still shows the old icon after
  updating, that is Explorer's icon cache; it refreshes on its own
  (or after a sign-out).

## 1.00.017

- The icon got bold: the dots sit one pixel apart and the "32" fills
  the full width of every size — it now holds its own next to any
  other program's icon.

## 1.00.016

- **ctrl32 has a face.** The dotted "32" in the project's own
  typeface and the brand blue is now the icon of the installer, of
  the editor itself, of its window and taskbar entry and of the Start
  menu shortcuts. Every icon size is drawn dot by dot — the logo
  stays crisp from 16 px up.

## 1.00.015

- **The bare-arc gauge works in the editor too.** A gauge with the
  needle switched off and a custom arc thickness drew correctly on
  the board but grew a needle back in the editor's canvas — the
  editor now carries both properties end to end: drawing, project
  files, download, and the inspector (a Thickness field and a Needle
  switch under the gauge angles).
- **Navigation buttons dropped the arrow.** The chevron took 14 px
  from every nav button's text; the text now gets the whole button —
  on the board, in the browser and in the editor alike.
- **The EVB thermostat example got its dial.** The main screen is the
  familiar thermostat-card look: two nested arcs (room temperature in
  blue, setpoint in orange), whole-degree numbers in the center, a
  +/- setpoint spinner — and the numeric design stays one nav button
  away. The program opens cleanly in the ladder editor, spinner
  included (a rising-edge contact, the ladder-native shape).
- **Every installer now passes the full test gate first.** The engine
  comparison across all example programs, the block and language test
  suites and the editor self-tests run before the installer is built
  — a red test means no installer exists to ship.

## 1.00.014

- **Olimex ESP32-EVB drives a display.** The MOD-LCD2.8RTP module
  (2.8" 320×240 with resistive touch) plugs into the board's UEXT
  connector and the same board id covers both uses: a project with
  HMI screens lights the glass, a project without them keeps the
  board headless with WEBview, exactly as before. Picture and touch
  are verified on real hardware, touch calibration included, and the
  board comes with its own example project sized for the small glass:
  a wall **thermostat** — the board's two relays driven by a ladder
  hysteresis controller with auto/manual, a simulated temperature
  until a sensor is wired, and a portrait web banner prepared for a
  Home Assistant dashboard.
- **One honest limit that comes with it:** this board runs the
  display *or* the WEBview, not both — the classic ESP32 with a
  display project has no memory left for the network stack. The
  board says so plainly at startup and keeps logic, glass and USB
  download running; the headless use keeps its WEBview as always.
  (The groundwork for a display-plus-ethernet mode is in place and
  planned for a future release.)
- The USB download listener now starts earlier and reports loudly if
  it ever cannot start — on a tightly loaded board it could
  previously die silently, leaving no way to download over the
  cable.
- Display boards start a little lighter on internal memory — two
  large fixed buffers moved out of the static segment (no behavior
  change; it is what made the EVB combination fit).

## 1.00.013

- Fixed a red "conflicting ID" warning (and the ambiguous click
  behind it) in the ladder FB menu — the timers and counters appear
  there twice by design, once for the rung and once as a box, and
  the two halves now identify themselves properly.

## 1.00.012

**Download over the network, straight from the editor.** The download
dialog now offers two targets: the USB cable, or the board's network
address (IP or `name.local`, prefilled from the project). The same
pack, the same guarantees — inactive slot, full validation, the old
program stays on any error — just without walking to the equipment.

- **Headless boards accept network uploads too.** Boards without a
  display (inoCORE32-TM1.x and friends) take a pack over Ethernet or
  WiFi the same way the display boards do. Flash the runtime from
  this release once over USB; from then on the network works.
- **And the security switch that belongs with it:** the WEBview
  settings page has *Allow program upload over the network*. Switched
  off, the board never even registers the upload endpoint — for a
  deployed equipment on a shared network. USB always works. The board
  belongs on its own equipment network either way; the browser
  interface rides the same server, so treat network access to the
  board as operator access.
- A landscape project on a portrait glass (the 10.1" board) no longer
  trips the board check — the board rotates, and now the check knows.

## 1.00.011

- Live rows in the block editor got more air — on blocks with two
  outputs the first output's name and the second output's value no
  longer touch, and block parameters line up with their stretched
  rows instead of clustering at the top of the block.

## 1.00.010

**Important fix — download your project again.** The editor's
download stamped packs with an outdated format label, and from
1.00.008 on a board with the new runtime could reject or fault the
program because of it — online monitoring then showed nothing.
Install this build and download the project once (F5); nothing else
is needed. Runtimes flashed from 1.00.008/9 are fine as they are.

## 1.00.009

**A clean start.** A new project begins truly empty — no pre-made
program in the tree; you add LD, FBD or ST yourself. And a program
opened in ladder always has its first rung waiting: the bare arrow,
ready for the first contact.

- The diagnostics page no longer shows memory bars or heap numbers —
  cycle times, overruns and project consumption stay.
- The standing "online — switch to offline" note is gone from the
  editor toolbars; the grayed controls say it.
- Ladder drawing polish: a parallel branch connects to the run wire
  to the pixel (no tick above, no stub poking left of the branch) and
  block frames have sharp, fully joined corners.
- A saved project reloads its internal connection variables exactly
  as it saved them — a reopened ladder program keeps its rung shape
  instead of decomposing into helper-variable rungs.

## 1.00.008

**The blinker counts down for you.** BLINK blocks have a new `REM`
output pin: the time left in the current phase, live on the right
stub in online and simulation — next to the timers' `ET` and the
counters' `CV`, every block with an inner value now shows it. Loading
projects that use `REM` needs the runtime from this release; existing
projects and runtimes keep working unchanged.

- Variable declarations can be edited during a running simulation —
  applying re-binds the program on the fly. (Connected to a real
  board they stay read-only, as everything does.)
- Ladder breathes less air: tighter comment lane, tighter spacing
  between rungs, and rungs with blocks no longer reserve an empty
  row below them.
- Toolbox tiles of the motion, CAN and communication blocks got
  short marks that fit the tile — no more clipped names.

## 1.00.007

**One program, one owner.** A program edited in ladder is a read-only
view in the block editor (and the other way round after taking it
over with one click) — so an edit in one view can never be silently
overwritten by a save from the other. Previously a comment written in
LD could wipe blocks that had just been drawn in FBD; that cannot
happen any more, and the two views finally stay in step.

- **Comments are shared.** Rung comments and network comments are the
  same text — write it in either editor, switch, and it is there.
- **Arrange respects networks.** With network dividers present the
  Arrange button lays blocks out inside their own network — dataflow
  columns per band, band heights to fit — instead of scattering the
  whole canvas.

## 1.00.006

**Function blocks get a proper interface pane.** Above the canvas of
every LD and FBD tab sits a variables table in the PLCopen shape:
`VAR_INPUT` and `VAR_OUTPUT` rows of a function block (name and type
edited right there, ports added with one button) and a `VAR` section
listing the local connection variables the diagrams create. Building
your own block is now the standard flow: add a POU of the *function
block* kind, define its inputs and outputs in the pane, draw the
inside — in FBD **or in ladder** — and place it as a block in any
program. Interface changes bump the block's version automatically so
existing instances migrate cleanly.

- **Toolbox sorted.** Blocks are grouped the same way everywhere —
  Boolean, Math, Timers, **Counters**, General, **Motion**, **CAN**
  and **GSM/GPS** — in the Toolbox of both editors and in every
  add-block menu. Motion and CAN blocks were missing from the block
  palette entirely; now every group is one click away. Groups start
  collapsed each time the editor opens.
- In FBD the operand names sit **below** the wire line (values stay
  above it) — a connection passing a pin row no longer runs through
  the text.

## 1.00.005

**Comments are written straight on the canvas.** Every ladder rung has
a comment line above it — click it and type, multiple lines welcome;
click away and it stays. Network comments in the block diagram work
the same way. No dialog anywhere.

- A network in the block diagram can be **selected** like a rung in
  ladder — click its empty area and it highlights with the same quiet
  grey background.
- The rung comment no longer touches the blocks below it, and while
  connected a conducting block's frame is drawn as thick as the
  conducting wires — the active path reads at a glance.

## 1.00.004

**A rung does not need a coil.** A ladder rung can now end without an
output coil — the run wire simply ends in a small arrow, the standard
notation. A new rung starts that way: just the arrow, and you build
from there. Blocks placed on a bare rail get a TRUE contact drawn in
front of them, and contacts before a block act as its EN condition —
no helper variable needed. Everything still converts cleanly between
LD and FBD, both directions.

- **Clean networks in FBD.** A connection never crosses a network
  divider any more: across networks the signal travels by its
  variable name, shown at both pins — for a direct block-to-block
  link that name is `instance.PIN`. Generated FBD layouts also got
  proper spacing: band heights follow the tallest block and columns
  leave room for the operand labels.
- Live values in ladder now sit above the pin variables of blocks
  placed inside a rung too — inputs, parameters and the second
  output alike, matching the boxes.
- Thinner connection and block lines in the editors — the drawing is
  lighter; symbols keep their weight, and the live power flow is
  still thick and green.
- Selecting a rung highlights it with a quiet grey background
  instead of a bright frame over the rung comment.

## 1.00.003

**The block diagram mirrors the ladder.** A program edited in LD shows
its FBD view organized in numbered networks — one horizontal band per
rung, in rung order, with the rung comments on the network dividers.
Every ladder save refreshes the layout, so the two views never drift
apart. A diagram with no dividers yet is network 1 and says so.

- Online mode is now read-only without exceptions: the context menus
  and edit popups of both editors stay closed while the connection is
  live. The one thing that still switches online is the LD/FBD/ST view.

## 1.00.002

- Live values in LD and FBD are drawn **above each pin variable** —
  inputs, parameters and outputs alike — where they cannot collide
  with names or connection wires; live rows stretch to make room.
- The view switch (LD ↔ FBD) moved to the front of the toolbar and
  stays available during online monitoring.
- The status bar shows the version number instead of the build date.

## 1.00.001

- Online values placed clear of labels and wires.
- A ladder element cut in one rung pastes into any other rung.
