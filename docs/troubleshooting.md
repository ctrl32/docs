# Troubleshooting

A list of the actual messages the system prints and what is really behind
them. When a build fails, the editor opens a window with the **whole**
output — the text can be selected with the mouse and copied with a button,
and the same text is in `build\last_build_error.txt`.

## Downloading a program

### "variable 'NOT' has the name of an ST keyword"

A variable becomes an **identifier** in the generated program, so a name like
`NOT`, `VAR`, `REAL` or `TIME` means something else there. Rename the variable —
the message says which one.

### "EQ 'b30': its parameters have no ST form yet"

A block the editor can draw but the generator cannot yet translate. The
message always names both the **type and the name** of the block. Report it
to `bugs@ctrl32.com` — it is usually a small fix.

### "the logic cannot be compiled for the board: … did not compile"

The generated program failed to compile — that is **our fault, not your
project's**. The editor prints the whole generated source with line numbers;
send that output.

### "project has N blocks, the limit is 512"

A real limit. See [Performance and limits](limits.md); usually the variable table
runs out first.

## The board

### The browser says SSL_ERROR_RX_RECORD_TOO_LONG (or "unsupported protocol")

The browser silently upgraded the address to **https** — Firefox in
HTTPS-Only mode does it to every bare address, Chrome shows
`ERR_SSL_PROTOCOL_ERROR` for the same reason. The panel's pages are
served **deliberately without TLS** (see
[Network and security](security.md)): an encrypted server would eat
the RAM the visualization needs, and the pages belong on the
equipment's own network, not on the internet.

Type the address with the scheme spelled out — `http://192.168.0.31`
— or add an HTTPS-Only exception for the panel's address in the
browser. Nothing is wrong on the device; the plain page is one
`http://` away.

### No COM port appears when the board is plugged in

Exactly two causes, and both live on the PC, not the board: the USB
bridge's **driver is missing** (Device Manager shows an unknown
device — a hall notebook without internet cannot fetch it), or the
cable is a **charging cable** that carries power and no data. The
driver table and the habit of carrying both are in
[A board from zero](first-run.md).

### Flash runtime is red: "does not match the editor"

One version for everything: the editor writes only a runtime that
carries **its own version number**, and the dialog shows the
**folder** the offered runtime came from. A runtime older than the
editor in that folder is almost always a leftover from an earlier
installation shadowing the fresh files — reinstall with the current
installer (it removes the leftover locations itself) and the dialog
offers the right build.

### The board refused the pack ("invalid pack")

The pack failed verification — most often **the target board does not
match** (the project is for another board), or the runtime is older than the
pack format.

Important: **the old pack stays and keeps running**. A download cannot
disable the board. The fix: check the board in the project, or flash the
runtime.

### "!! N FB RECORDS – this pack predates the one-engine build"

The board holds a pack from a very old editor. Its **logic does not run** —
the board says so on the console and in the diagnostic buffer. Rebuild the
project with the current editor and download it again.

### The board answers but `seq` does not move

`seq` is the sample counter in the ONLINE tooltip — one tick per batch
of values the board sends. The connection is fine; **the PLC cycle has
stopped**. Look at the
diagnostic buffer (*Debug → diagnostics*) — the reason is usually there (a
VM fault, a cycle overrun).

## Online monitoring

### The plug icon is red

The board runs a **different program** than the editor. Values are
deliberately not shown — they travel by index, and under a different program
they would appear as real numbers under the wrong names. The editor offers
to download straight away.

### It keeps asking to send the program

Two different situations wear this face. A board that is **still
starting** answers the "same program?" question a few seconds late —
the editor keeps asking, so waiting out the restart is enough. But
when the question comes back **after an upload the board accepted**,
believe it: the project open in the editor is not the one that was
sent — a second copy of the project is the usual culprit. *Download
from the panel* fetches what the board really runs and settles it.

### The icon is amber and nothing happens

The port cannot be opened: another program is holding it (a terminal,
another editor), the board is restarting, or the cable is unplugged. It
retries once a second, so plugging the cable back in is enough.

### The port list is empty, or nothing is selected

No port is preselected on purpose. Pick one in the toolbar or in the
transfer dialog — the download and flash buttons stay disabled until you do.

### I see variables but no values on the wires between blocks

The symbols could not be verified — the editor uses them only when the
compiled program matches the one in the board **byte for byte**. It writes
the state into the status bar; the usual cause is that the board holds a
different build.

## The editor

### A new project will not take a rung

This was a bug and it is **fixed**: the *+ Rung* button now creates a BOOL
variable itself and says which one. If it still does not work, you have an old
binary.

### A comment next to a variable disappeared

Also fixed. The comment is written at the end of the line after `//` and
read back; leaving the line without one deletes the comment — the text is
the whole truth for its list.

### An opened project has an empty ladder

A fixed import bug (the project was being loaded through a pack without
block records). Update the editor.

---

If a problem does not fit here, send the **whole error output** (the *Copy
message* button) to `bugs@ctrl32.com` — the bug icon at the top right of the
menu opens the mail directly.
