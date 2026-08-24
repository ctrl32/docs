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

### ONLINE and Deploy are locked

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
