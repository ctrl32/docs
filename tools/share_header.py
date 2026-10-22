#!/usr/bin/env python3
# =============================================================================
#  share_header.py — the SHARE PICTURE a documentation page declares
#
#  WHY THIS EXISTS. When somebody shares a page of the documentation, the
#  site sends a card: a title, a sentence and a picture.
#  every page sent the SAME picture (the site's own), so ten tutorials and
#  eight examples all looked like one page on Facebook. The web engine
#  now lets a page bring its own:
#
#      ---
#      image: img/example-f7-plc.webp
#      image_alt: The showcase reading a data block of a SIMATIC live
#      ---
#
#  and where a page declares nothing, its FIRST picture answers instead.
#  So a declaration is only needed where the first picture is the wrong
#  card — a settings page, a dialog, a toolbar strip — or where the page
#  has no picture at all.
#
#  IT HAS TO LIVE IN THE REPOSITORY. The web rewrites an imported page's
#  values WHOLE on every sync, so a picture chosen in the web's own back
#  office is erased the same night. The page says it with its words, here.
#
#  WHEN IT FAILS: a header with an unknown key, an `image` whose file is
#  not in docs/, or an `image` without `image_alt` is a hard error before
#  anything is written — the picture field on the other side refuses a
#  value with no alt, and a card that silently fell back to the site logo
#  is exactly the failure nobody notices.
# =============================================================================
from pathlib import Path

import yaml

# The keys a page may declare. Anything else is a typo or an invention
# the web would ignore in silence, which is worse than a refusal.
ALLOWED = {"image", "image_alt"}


def take_header(text: str, name: str, docs: Path = None):
    """Split an optional `---` header off the top of a page.

    Answers (declaration, body). The declaration is a dict with the keys
    above, empty when the page carries no header.
    """
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end < 0:
        raise SystemExit(f"ERROR {name}: the header opens with --- and "
                         f"never closes. Close it, or delete it.")
    block = text[4:end]
    rest = text[end + 4:].lstrip("\n")
    try:
        data = yaml.safe_load(block) or {}
    except yaml.YAMLError as e:
        raise SystemExit(f"ERROR {name}: the header is not YAML: {e}")
    if not isinstance(data, dict):
        raise SystemExit(f"ERROR {name}: the header must be keys and values.")
    unknown = sorted(set(data) - ALLOWED)
    if unknown:
        raise SystemExit(f"ERROR {name}: the header says "
                         f"{', '.join(unknown)} — only "
                         f"{', '.join(sorted(ALLOWED))} are read. A key "
                         f"nobody reads is a line that lies.")
    share = {k: str(data[k]).strip() for k in ALLOWED if data.get(k)}
    if share.get("image") and not share.get("image_alt"):
        raise SystemExit(f"ERROR {name}: image without image_alt. Every "
                         f"picture carries its words, and the field on "
                         f"the web refuses a value without one.")
    if share.get("image_alt") and not share.get("image"):
        raise SystemExit(f"ERROR {name}: image_alt without image.")
    img = share.get("image")
    if img and docs is not None and not (docs / img).is_file():
        raise SystemExit(f"ERROR {name}: the share picture '{img}' is not "
                         f"in docs/. A card cannot point at a file that "
                         f"does not travel with the page.")
    return share, rest


def share_lines(share: dict) -> str:
    """The two lines as the export's front matter carries them."""
    if not share:
        return ""
    out = f"image: {share['image']}\n"
    alt = share["image_alt"].replace('"', "'")
    return out + f'image_alt: "{alt}"\n'
