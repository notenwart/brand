# notenwart – brand kit

notenwart's look: the mark, the wordmark, colours, icons and social images. Every falkOSS project has its own name,
logo, colours and look; falkOSS appears only as publisher.

**The mark:** a crest-shaped shield (the *Wart*, the keeper) with staff lines and an eighth note in brass. Two
weights:

- **Regular** – five staff lines; 64 px and up.
- **Small** – three heavier lines, heavier outline, slightly larger note; 16–48 px (favicon, tabs, small app slots).

Every variant exists **light** (navy on paper) and **dark** (paper on navy). The note is always brass. The gap
between the note and the staff lines is a mask, so the transparent marks work on any background.

Everything here is generated: edit `generate.py` (the drawing) – `brandkit.py` (the export, from
[falkoss/starterpack](https://github.com/falkoss/starterpack)) stays as it is – then run `python3 generate.py` (needs
`rsvg-convert` from Homebrew `librsvg`; the wordmark, lockup and social PNGs use the Charter font). It writes `svg/`,
`png/` and `web/`.

## Colours

| Name | Hex | Use |
|---|---|---|
| Navy (ink) | `#1D2B45` | outline and lines on light, dark backgrounds, text |
| Paper (cream) | `#F5EFE3` | light backgrounds, ink on dark |
| Brass | `#B8862E` | the note on light backgrounds, accents |
| Brass light | `#D9A441` | the note on dark backgrounds, accents on dark |

## Type

**Charter** for the wordmark and headings (bundled with macOS and iOS; free as *Bitstream Charter*), with the stack
`Charter, "Bitstream Charter", "Iowan Old Style", Georgia, serif`. Body text uses the system sans-serif. No fonts are
loaded from other servers. **OPEN:** the wordmark as outlines, so it needs no font where it is shown.

## Name

Always written in lowercase – **notenwart**, also at the start of a sentence, in titles and in the wordmark; the same
in handles and domains. Don't write *Notenwart* or *NOTENWART* in running text (environment variables such as
`NOTENWART_PUBLIC_URL` follow their own convention).

## What to use where

| Use | File |
|---|---|
| GitHub organisation avatar | `png/social/github-avatar-500.png` (dark) |
| GitHub social preview, link previews | `png/social/notenwart-social-1280x640.png`, `web/social.png` |
| Website and web app head | `web/` – favicon.svg (follows light/dark), favicon.ico, apple-touch-icon.png, icon-192/512.png, icon-maskable-512.png, social.png, site.webmanifest |
| Headers, documents, profile | `svg/notenwart-lockup-on-dark.svg`, `-on-light.svg` (PNG: `png/lockup/`) |
| Wordmark alone | `svg/notenwart-wordmark-on-dark.svg`, `-on-light.svg` |
| Mark alone (transparent) | `svg/notenwart-mark-on-dark.svg`, `-on-light.svg`; small: `-mark-small-on-…`; one colour: `-black.svg`, `-white.svg` |
| App-like icon | `png/icon/` (rounded), `png/icon-square/` (edge to edge), `png/icon-small/` (16–48 px) – light, and `-dark` |

Website head:

```html
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
```

## Where it is used

This repository is the brand's one source; the others carry copies of what they show and are updated by copying,
never edited there:

| Repository | Copies |
|---|---|
| `notenwart/website` | `web/`, the lockup and mark on dark and light (`assets/`) |
| `notenwart/.github` | the lockups in the organisation profile |
| `notenwart/notenwart` | `web/favicon.*` and the lockups and mark in `docs/assets/`; `web/` and the marks in the web app's `web/public/` |

## Licences and rights

| Files | Licence |
|---|---|
| `generate.py`, `brandkit.py`, this README | [MIT](LICENSES/MIT.txt) |
| the artwork: `svg/`, `png/`, `web/` | [CC BY-ND 4.0](LICENSES/CC-BY-ND-4.0.txt) |

The artwork may be copied and passed on – also in apps distributed through app stores and in other software – as it
is and naming falkOSS; changed versions may not be passed on. The licence covers the artwork's copyright, not the
name: notenwart's name and brand belong to falkOSS – Falcon Lake Open Source Software gUG (haftungsbeschränkt) i. G.,
the publisher of notenwart. They may be used to refer to notenwart, not for other products or in a way that suggests
endorsement. **OPEN**: trademark search and registration, and a review of these terms by someone who knows the law.
