#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Generates the notenwart brand kit: master SVGs, PNG exports, favicon.ico and the website's head icons.

The mark: a crest-shaped shield (the "Wart", the keeper) with staff lines and an eighth note in brass; navy on paper
(light) and paper on navy (dark). The drawing is here; the export is brandkit.py from falkoss/starterpack, which
stays as it is. notenwart adds to it: dark variants of the icons, the small marks, a maskable icon for the web app
and its manifest, and the dark GitHub avatar.

The wordmark is live text in Charter (bundled with macOS, free as Bitstream Charter elsewhere); OPEN: outlines, so
it needs no font where it is shown. Needs rsvg-convert (Homebrew: librsvg). Run from anywhere:
    python3 generate.py
Edit this file, not the exports.
"""
import os

from brandkit import export, render, svg, write

HERE = os.path.dirname(os.path.abspath(__file__))
NAME = "notenwart"
TAGLINE = ("Sheet music for schools, orchestras and bands –", "every player sees their own part.")

NAVY = "#1D2B45"         # ink: outline, lines, dark backgrounds
CREAM = "#F5EFE3"        # paper: light backgrounds, ink on dark
BRASS = "#B8862E"        # the note on light backgrounds
BRASS_LIGHT = "#D9A441"  # the note on dark backgrounds
SERIF = "Charter, 'Bitstream Charter', 'Iowan Old Style', Georgia, serif"
BOX = "0 0 1024 1024"

# The shield: a gentle arch on top, so it reads as a crest rather than a security badge.
SHIELD = ("M512 150 C620 196 720 222 820 232 V500 C820 690 690 818 512 884 "
          "C334 818 204 690 204 500 V232 C304 222 404 196 512 150 Z")

# Regular mark: five staff lines; small mark (16-48 px): three heavier lines, heavier outline, larger note.
REGULAR = dict(lines=(350, 440, 530, 620, 710), line=20, outline=48, scale=1.06, x=466, y=664, gap=18)
SMALL = dict(lines=(420, 560, 700), line=40, outline=76, scale=1.12, x=470, y=700, gap=26)


def note(g, color, halo=0):
    """An eighth note, stem up. With `halo`, a widened silhouette used to cut the staff lines around the note."""
    s, x, y = g["scale"], g["x"], g["y"]
    hx, top, tip = x + 62 * s, y - 330 * s, y - 160 * s
    w = 36 * s + 2 * halo
    flag = f"M{hx:.0f} {top:.0f} C{hx + 70 * s:.0f} {top + 30 * s:.0f} {hx + 120 * s:.0f} {top + 80 * s:.0f} {hx + 92 * s:.0f} {tip:.0f}"
    if halo:  # also clear the pocket between flag and stem
        flag += f" L{hx:.0f} {tip:.0f} Z"
    return (f'<ellipse cx="{x}" cy="{y}" rx="{74 * s:.0f}" ry="{55 * s:.0f}" transform="rotate(-22 {x} {y})" '
            f'fill="{color}" stroke="{color}" stroke-width="{2 * halo}"/>'
            f'<line x1="{hx:.0f}" y1="{y - 14 * s:.0f}" x2="{hx:.0f}" y2="{top:.0f}" stroke="{color}" '
            f'stroke-width="{w:.0f}" stroke-linecap="round"/>'
            f'<path d="{flag}" fill="{color if halo else "none"}" stroke="{color}" stroke-width="{w:.0f}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def mark(ink, note_color, p, small=False):
    """Shield outline with staff lines and the note; transparent, works on any background (the gap is a mask)."""
    g = SMALL if small else REGULAR
    lines = "".join(f'<line x1="150" y1="{y}" x2="880" y2="{y}"/>' for y in g["lines"])
    return (f'<defs><clipPath id="{p}clip"><path d="{SHIELD}"/></clipPath>'
            f'<mask id="{p}gap" maskUnits="userSpaceOnUse" x="0" y="0" width="1024" height="1024">'
            f'<rect width="1024" height="1024" fill="#fff"/>{note(g, "#000", g["gap"])}</mask></defs>'
            f'<g clip-path="url(#{p}clip)"><g mask="url(#{p}gap)" stroke="{ink}" stroke-width="{g["line"]}">{lines}</g></g>'
            f'<path d="{SHIELD}" fill="none" stroke="{ink}" stroke-width="{g["outline"]}" stroke-linejoin="round"/>'
            + note(g, note_color))


def light(p, small=False):
    return mark(NAVY, BRASS, p, small)


def dark(p, small=False):
    return mark(CREAM, BRASS_LIGHT, p, small)


def tile(bg, body):
    """Rounded app tile (the rounding most platforms apply themselves is drawn in, for previews and the web)."""
    return svg(BOX, f'<rect width="1024" height="1024" rx="224" fill="{bg}"/>{body}')


def square(bg, body, inset=1.0):
    """Edge to edge, for platforms that mask the icon (iOS, Android maskable): content in the safe zone."""
    t = f' transform="translate(512 512) scale({inset}) translate(-512 -512)"' if inset != 1 else ""
    return svg(BOX, f'<rect width="1024" height="1024" fill="{bg}"/><g{t}>{body}</g>')


def favicon():
    """Small mark that follows the browser's light or dark mode."""
    return svg(BOX, '<style>.d{display:none}@media (prefers-color-scheme: dark){.l{display:none}.d{display:inline}}'
               f'</style><g class="l">{light("fl-", True)}</g><g class="d">{dark("fd-", True)}</g>')


def wordmark(ink):
    return svg("0 0 760 200", f'<text x="10" y="150" font-family="{SERIF}" font-size="148" font-weight="600" '
               f'fill="{ink}" letter-spacing="1">{NAME}</text>', (760, 200))


def lockup(ink, note_color, p):
    """Mark and wordmark side by side (README, docs)."""
    return svg("0 0 1080 256", f'<g transform="scale(0.25)">{mark(ink, note_color, p)}</g>'
               f'<text x="268" y="166" font-family="{SERIF}" font-size="148" font-weight="600" fill="{ink}" '
               f'letter-spacing="1">{NAME}</text>', (1080, 256))


def social():
    return svg("0 0 1280 640", f'<rect width="1280" height="640" fill="{NAVY}"/>'
               f'<g transform="translate(80 140) scale(0.35)">{dark("s-")}</g>'
               f'<text x="480" y="318" font-family="{SERIF}" font-size="132" font-weight="600" fill="{CREAM}">{NAME}</text>'
               + "".join(f'<text x="484" y="{390 + 44 * i}" font-family="{SERIF}" font-size="31" fill="{CREAM}" '
                         f'opacity="0.8">{line}</text>' for i, line in enumerate(TAGLINE))
               + f'<rect x="484" y="472" width="120" height="8" rx="4" fill="{BRASS_LIGHT}"/>', (1280, 640))


# The web app's manifest: the light icon, and the maskable one for platforms that crop it.
MANIFEST = f"""{{
  "name": "{NAME}",
  "short_name": "{NAME}",
  "icons": [
    {{ "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" }},
    {{ "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" }},
    {{ "src": "/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }}
  ],
  "theme_color": "{NAVY}",
  "background_color": "{CREAM}",
  "display": "standalone"
}}
"""


def main():
    kit = {
        "icon": tile(CREAM, light("il-")),
        "icon-square": square(CREAM, light("ql-"), 0.9),
        "icon-small": tile(CREAM, light("isl-", True)),
        "mark-on-dark": svg(BOX, dark("md-")),
        "mark-on-light": svg(BOX, light("ml-")),
        "mark-black": svg(BOX, mark("#000000", "#000000", "gb-")),
        "mark-white": svg(BOX, mark("#FFFFFF", "#FFFFFF", "gw-")),
        "wordmark-on-dark": wordmark(CREAM),
        "wordmark-on-light": wordmark(NAVY),
        "lockup-on-dark": lockup(CREAM, BRASS_LIGHT, "ld-"),
        "lockup-on-light": lockup(NAVY, BRASS, "ll-"),
        "social": social(),
        "favicon": favicon(),
    }
    export(HERE, NAME, kit, NAVY)

    # notenwart's additions to the standard kit.
    extra = {
        "icon-dark": tile(NAVY, dark("id-")),
        "icon-square-dark": square(NAVY, dark("qd-"), 0.9),
        "icon-small-dark": tile(NAVY, dark("isd-", True)),
        "icon-maskable": square(CREAM, light("m-"), 0.78),
        "mark-small-on-dark": svg(BOX, dark("msd-", True)),
        "mark-small-on-light": svg(BOX, light("msl-", True)),
    }
    s = lambda key: os.path.join(HERE, "svg", f"{NAME}-{key}.svg")
    png = lambda folder, file: os.path.join(HERE, "png", folder, file)
    for key, content in extra.items():
        write(s(key), content)
    for size in (64, 128, 256, 512, 1024):
        render(s("icon-dark"), png("icon", f"{NAME}-icon-dark-{size}.png"), size)
        render(s("icon-square-dark"), png("icon-square", f"{NAME}-icon-square-dark-{size}.png"), size)
    for size in (16, 32, 48):
        render(s("icon-small-dark"), png("icon-small", f"{NAME}-icon-small-dark-{size}.png"), size)
    # The organisation's avatar stays dark, as it was before the standard kit.
    render(s("icon-square-dark"), png("social", "github-avatar-500.png"), 500)
    render(s("icon-maskable"), os.path.join(HERE, "web", "icon-maskable-512.png"), 512)
    write(os.path.join(HERE, "web", "site.webmanifest"), MANIFEST)


if __name__ == "__main__":
    main()
