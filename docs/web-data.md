# Web data

The device reads a web address on a period and puts fields of the answer
into its variables. The weather from a forecast service, an electricity
price, an exchange rate, the state of anything behind a web service that
answers in JSON - without a server of yours in between.

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

Open-Meteo asks for no key. Its forecast is free for non-commercial use
and asks for an attribution on the page that shows it; a commercial
installation takes their API subscription and puts the key into the
address. The preset writes a plain address; edit it as you need.

## Any other service

Any address that answers JSON works the same way: paste the address,
add the fields. A service that wants a key usually takes it in the
query (`...&apikey=...`). A service that wants the key in a header, or
XML, is not covered.

## On the device

The device asks on its own, on a task of its own - the program's cycle
and the screen never wait for the web. The first read happens as soon as
the network is up, then every period. A failed read is retried after 30
seconds, then a minute, two minutes, up to the period; the failure and
the recovery are each said once in the diagnostic buffer with the reason
(no connection, the server's answer, not the JSON expected).

`https://` checks the server's certificate against the roots the device
carries and needs the clock - with `clock: { ntp: true }` the first
secure read follows the time sync; `http://` needs no clock.

The status line (`INFO`) carries `web=<ok>/<sources>,<reads>,<failures>`.

## Which devices

ESP32-S3, ESP32-P4, STM32 and Linux devices. The classic ESP32 has no
memory for the secure connection and is refused at the desk; a C3/C6
node reads no web data - its head does.

See also: [MQTT](mqtt.md) for pushing values out. The weather station
example on the Examples pages reads its forecast this way.
