---
title: "Web data"
slug: web-data
section: "Protocols"
order: 309
sidebar_position: 309
generator: tools/docs_export.py
---

# Web data

The device reads a web address on a period and puts fields of the answer
into its variables. The weather from a forecast service, an electricity
price, an exchange rate, the state of anything behind a web service that
answers in JSON - without a server of yours in between.

![The Web data page: two sources, the weather and the air quality, each with its address, period and status variable, and the eighteen fields of the selected one under them](img/web-page.webp){: .sb-center}

## A source

A source is a web address and a period. In the tree, open the context
menu of **Ethernet** or **WiFi** and pick **Add web data...**; the page
**Web data** opens.

| Column | Meaning |
|:---|:---|
| **Source** | A name of your own - letters, digits, `_` and `-`, up to 32 characters |
| **Address** | The full address, `http://` or `https://`, with its query. No spaces - write a space as `%20` |
| **Period [s]** | How often the device asks: 60 s to 24 hours |
| **Status variable** | Optional. A BOOL that is TRUE after a successful read and FALSE after a failed one - put it on a lamp |
| **Fields** | How many fields the source fills |

A project reads up to four sources.

## The fields

Select a source and its fields show under it. A field names a
**variable** and the **place in the answer** the value comes from:

```
current.temperature_2m
daily.weather_code[0]
data[2].price
```

Keys are separated by a dot, an element of a list by its index in
brackets, counted from 0. A field takes a number or a yes/no (`true` /
`false`) into a numeric or BOOL variable; a text in the answer is not a
value a field can take. A field whose place is not in the answer keeps
the variable's last value and is noted once in the diagnostic buffer.

Up to 32 fields per source, 64 in a project.

## The Weather preset

**Weather (Open-Meteo)...** on the page makes a complete source from
your coordinates: the latitude, the longitude, how many forecast days
(0 to 5) and whether the current weather is wanted. It makes the
variables too:

| Variable | Value |
|:---|:---|
| `web_t`, `web_h`, `web_p`, `web_wind` | the current temperature, humidity, sea-level pressure and wind |
| `web_code`, `web_day` | the current weather code and day (TRUE) or night |
| `fc0_code`, `fc0_tmax`, `fc0_tmin`, `fc0_rain` | today's code, high, low and precipitation; `fc1_…` tomorrow, and so on |
| `web_ok` | the status variable |

The code is the **WMO weather code**: 0 clear, 1 to 3 partly cloudy to
overcast, 45 and 48 fog, 51 to 67 drizzle and rain, 71 to 77 snow, 80 to
82 showers, 85 and 86 snow showers, 95 to 99 thunderstorm. A program
turns the code into the picture the screen shows - the weather station
example does it in a few lines of ST.

Pressing the preset again with other coordinates replaces the source
and keeps the variables, so the screens and the program need no change
when the station moves.

Open-Meteo asks for no key. Its forecast is free for non-commercial use
and asks for an attribution on the page that shows it; a commercial
installation takes their API subscription and puts the key into the
address. The preset writes a plain address; edit it as you need.

### The forecast model

Open-Meteo answers with the value of a **forecast model** at the grid
point nearest your coordinates, at the model's own elevation - not a
measurement from a weather station. Its default, `best_match`, picks a
model per region; the models differ from each other by a few degrees at
the same moment, and a forecast on your phone comes from yet another one.
If the station should agree with the forecast you trust, name that
model with one more word at the end of the address:

| Address ends with | Model |
|:---|:---|
| (nothing) | `best_match`, the service's choice for the region |
| `&models=icon_eu` | ICON-EU of the German weather service |
| `&models=ecmwf_ifs025` | ECMWF IFS |
| `&models=gfs_seamless` | GFS of the American weather service |
| `&models=meteofrance_seamless` | Météo-France |
| `&models=ukmo_seamless` | the UK Met Office |
| `&models=gem_seamless` | GEM of the Canadian weather service |

A regional model that does not cover your coordinates answers
`HTTP 400`; the source then says so in the diagnostic buffer and the
status variable stays FALSE - take the word out again.

## Any other service

Any address that answers JSON works the same way: paste the address,
add the fields. A service that wants a key usually takes it in the
query (`...&apikey=...`). A service that wants the key in a header, or
XML, is not covered.

## A secure address, step by step

What `https://` needs on the device, in the order the device needs it.

1. **A network that reaches the internet.** Open **WiFi** (or
   **Ethernet**) in the tree. On WiFi the mode is *STA* - the device
   joins your network - with the **Wi-Fi name (SSID)** and the **Wi-Fi
   password** of a network with internet access. The device's own access
   point is a network without internet: a device that only raises its
   own AP, or falls back to it because the join failed, reads no web
   data.
2. **The clock.** Open **Clock** in the tree, turn **NTP time sync** on,
   keep the **NTP server** (`pool.ntp.org`) unless your network has its
   own, and pick the **Timezone**. A certificate is valid from a date to
   a date, and a device that does not know the date can verify nothing:
   every secure read waits until the time is set and looks again every
   five seconds while it waits. A plain `http://` address needs no
   clock.
3. **The source.** Right-click **WiFi** (or **Ethernet**) and pick
   **Add web data...**. On the page **Web data** either press
   **Weather (Open-Meteo)...** and fill in the coordinates, or press
   **Add source** and type the **Address** beginning with `https://`,
   the **Period** and, if a lamp should show it, the **Status
   variable**. A port other than 443 goes after the host:
   `https://host:8443/path`.
4. **The fields.** Press **Add field** for every value: the
   **Variable** that takes it and the **Field in the answer**. Open the
   address in a browser first and read the names from the answer - a
   path is spelled exactly as the service spells it, case included.
5. **Deploy** (F5). The device joins the network, sets its clock and
   reads the source. On WiFi the first secure read is typically ten
   seconds after the start; from then on every period.

What the device checks on a secure address: the server's certificate
chain against the public roots the device carries (the roots the
browsers trust, among them the root behind the free certificates most
services use), the name in the certificate against the host in the
address, and the validity dates against the clock. A self-signed
certificate, or one issued for another name, is refused and said in the
diagnostic buffer. The secure session lives for the read alone - opened,
the answer taken, closed; between reads the device holds no connection
and no memory for it.

## Watching it

- **The status variable** is TRUE after a good read and FALSE after a
  failed one - a lamp on the screen is the simplest check.
- **The diagnostic buffer** says each change once: `web weather: ok (18
  fields)` after the first good read, `web weather: failed - <reason>`
  when a read fails, and `ok` again when it recovers.
- **The INFO line** carries `web=<ok>/<sources>,<reads>,<failures>`:
  `web=1/1,48,0` is one source, read 48 times, never failed;
  `web=0/1,0,0` is a source that has not read yet - the device is still
  waiting for the network or, on a secure address, for the clock.

## When it does not read

| The diagnostic buffer says | Why | What to do |
|:---|:---|:---|
| nothing, and the INFO line says `web=0/1,0,0` | waiting for the network, or for the clock on a secure address | `wifi=` / `eth=` on the INFO line, the Clock page |
| `failed - <host> is not a host the DNS knows` | no internet behind the network, or a misspelled host | the network, the address |
| `failed - no connection to <host>` | the server is unreachable or the port is closed | a firewall, the port in the address |
| `failed - no secure connection to <host>` | the secure handshake failed: a certificate the device cannot verify, a certificate for another name, a clock far off | the Clock page; open the address in a browser and look at its padlock |
| `failed - HTTP 400` (401, 403, 404, 429) | the service refused the query | open the address in a browser: a wrong parameter, a missing key; 429 means too many requests - a longer period |
| `failed - not the JSON expected - no '<path>'` | the answer carries none of the fields | compare the paths with the answer in a browser |
| `3 of 18 fields missing (no '<path>')` | some paths are wrong; the rest were filled | fix the named path |
| `failed - an empty answer`, `not an HTTP answer` | the service answered with no body, or not over HTTP | the address |
| `web: skipped (... under the 12 kB bar)` | the device has no free internal memory for a read beside its screens | fewer screens or fonts in the project, or a board with more memory |

A failed read is retried after 30 seconds, then a minute, two minutes,
up to the period; the first failure and the recovery are each said once.

## On the device

The device asks on its own, on a task of its own - the program's cycle
and the screen never wait for the web. The first read happens as soon as
the network is up (and the clock is set, for `https://`), then every
period.

## Which devices

ESP32-S3, ESP32-P4, STM32 and Linux devices. The classic ESP32 has no
memory for the secure connection and is refused at the desk; a C3/C6
node reads no web data - its head does.

See also: [MQTT](/docs/buses/mqtt/) for pushing values out. The weather station
example on the Examples pages reads its forecast and the air quality this
way - two sources, each with its status variable.
