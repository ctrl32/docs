# Adding peripherals to a board

What those peripherals do at run time — mapping pins onto tags,
converter ranges — is described in
[Board peripherals and system services](peripherals-and-services.md).

```video
src: video/inocore32-peripherals.mp4
poster: video/inocore32-peripherals.jpg
title: Adding peripherals to a board
outline:
  - at: "0:00"
    text: A project open on the inoCORE32-TM board — the tree shows only
          the interfaces the board really has, and the green dot next to
          CAN is the live status read from the panel.
  - at: "0:02"
    text: The board node opens its page — the module card
          (ESP32-PICO-V3-02, Ethernet IP101GRI, 8 free pins) and the pin
          assignment from the catalog.
  - at: "0:05"
    text: Right-clicking I2C offers the chips for THAT bus — TCA9555 and
          ADS1115. POWERSTEP01 is SPI, so it is not offered.
  - at: "0:06"
    text: TCA9555 appears in the tree and its page opens — the expander
          pin table, every pin bindable to a tag.
  - at: "0:09"
    text: The same for the ADS1115 — four analog inputs, address 0x48.
  - at: "0:13"
    text: Back on the board page — both peripherals are listed with their
          addresses and the pin table has gained the pins they use.
```

> **Pins are not configured at run time.** A peripheral added in the
> editor is **compile-time** configuration: it goes into the pack and
> the panel reads it at startup. The pin assignment never changes while
> running — a deliberate decision that protects you from a badly
> uploaded project switching a pin that has something else on it.

<details>
<summary>How this clip was made</summary>

What gets recorded is the editor itself, not the screen: the input is
injected directly into ImGui before the frame is drawn. That makes it
deterministic — the same script always yields the same recording, so
the clip is not just a video but also a regression test of the
procedure.

</details>
