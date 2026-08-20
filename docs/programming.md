# Programming

The logic is written in the languages a PLC programmer already knows.
Ladder and FBD are two views of the same program — switch between them
any time — and everything compiles into one bytecode that the panel
executes. The device never parses text: uploading a program is uploading
data, never firmware.

- [Ladder (LD)](ladder.md) — rungs, contacts, coils and blocks with
  EN/ENO, the way an electrician reads them
- [Function block diagram (FBD)](fbd-composites.md) — the same logic as
  networks of blocks, plus composite blocks you build yourself
- [Structured Text (ST)](st-language.md) — the textual language
  underneath, with the full block library callable from it
