# Adding peripherals to a board

What those peripherals do at run time — mapping pins onto tags,
converter ranges — is described in
[Board peripherals and system services](peripherals-and-services.md).

<video id="klip-periferie" controls muted playsinline width="100%"
       poster="video/inocore32-peripherals.jpg">
  <source src="video/inocore32-peripherals.mp4" type="video/mp4">
  Your browser cannot play this video —
  <a href="video/inocore32-peripherals.mp4">download the file</a> (135 kB).
</video>

## What happens in the clip

Click a timestamp to jump to that point in the recording.

<ul class="klip-kroky">
  <li><button type="button" data-t="0">0:00</button>
    <div><strong>A project open on the inoCORE32-TM board.</strong>
    The tree shows only the interfaces the board actually has — CAN,
    RS485, Ethernet, I2C. It has no display, so there is none here. The
    green dot next to CAN is the live status read from the panel.</div></li>

  <li><button type="button" data-t="1.9">0:02</button>
    <div><strong>Clicking the board node opens its page.</strong>
    The module card (ESP32-PICO-V3-02, Ethernet IP101GRI, 8 free pins)
    and the pin assignment from the <code>boards/</code> catalog.</div></li>

  <li><button type="button" data-t="4.9">0:05</button>
    <div><strong>Right-clicking I2C offers the chips for that bus.</strong>
    TCA9555 and ADS1115. POWERSTEP01 is SPI, so it is not offered — the
    list is filtered by the bus the chip belongs to.</div></li>

  <li><button type="button" data-t="5.9">0:06</button>
    <div><strong>TCA9555 appears in the tree and its page opens.</strong>
    The expander pin table: every pin can be bound to a tag.</div></li>

  <li><button type="button" data-t="9.9">0:09</button>
    <div><strong>The same for the ADS1115.</strong>
    Four analog inputs, address 0x48.</div></li>

  <li><button type="button" data-t="12.9">0:13</button>
    <div><strong>Back on the board page.</strong>
    Both peripherals are in the list together with their addresses, and
    the pin table has gained the pins they use.</div></li>
</ul>

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

<style>
/* Step list with clickable timestamps. Deliberately without colours —
   the page should look like the rest of the documentation, the theme
   is set by MkDocs. */
.klip-kroky { list-style: none; padding: 0; margin: 0; }
.klip-kroky li {
  display: grid; grid-template-columns: 4.2rem minmax(0, 1fr);
  gap: 0 1rem; padding: .55rem 0;
  border-top: 1px solid rgba(128, 128, 128, .28);
}
.klip-kroky li:last-child { border-bottom: 1px solid rgba(128, 128, 128, .28); }
.klip-kroky button {
  font: inherit; font-variant-numeric: tabular-nums;
  color: inherit; background: none; border: 0; padding: 0;
  text-align: left; cursor: pointer; text-decoration: underline;
  text-underline-offset: .2em;
}
.klip-kroky button:hover { text-decoration-thickness: 2px; }
</style>

<script>
/* Jump to a timestamp in the recording. Once the scripts move into
   extra_javascript in mkdocs.yml, the function body is enough — with
   Material and instant loading, bind to document$ instead of load. */
(function () {
  var v = document.getElementById("klip-periferie");
  if (!v) return;
  document.querySelectorAll(".klip-kroky button").forEach(function (b) {
    b.addEventListener("click", function () {
      v.currentTime = parseFloat(b.dataset.t);
      v.play();
    });
  });
})();
</script>
