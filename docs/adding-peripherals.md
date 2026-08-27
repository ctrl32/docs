# Adding peripherals to a board

What those peripherals do at run time — mapping pins onto variables,
converter ranges — is described in
[Board peripherals and system services](peripherals-and-services.md).

> **Pins are not configured at run time.** A peripheral added in the
> editor is **compile-time** configuration: it goes into the pack and
> the board reads it at startup. The pin assignment never changes while
> running — a deliberate decision that protects you from a badly
> uploaded project switching a pin that has something else on it.
