[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/supernyx002-dotcom/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/supernyx002-dotcom/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117)

[make.fun bounty: news-image-20261117](https://make.fun/bounty/news-image-20261117)

# The World in One Page — Tuesday, 17 November 2026

make.fun bounty **news-image-20261117** · $250 · deadline Thu 19 Nov 2026 07:00 WIB (00:00 UTC)
Account: **@tidy-gecko-68**

A newspaper front page summing up the world's news of Tuesday, 17 November 2026
in one 1024×1024 image. Lead story: the U.S. strikes on Iran and the burning
tankers in the Strait of Hormuz.

## The day's stories (as shown on the page)

| # | Story | Fact shown |
|---|-------|------------|
| Lead | U.S. strikes Iran as Gulf shipping burns | US warplanes hit a missile site on Qeshm Island; a fourth tanker was hit by a mine; Oman evacuated 24 seafarers from the burning gas tanker *Tara Gas*. |
| 1 | Ukraine hits Kerch Bridge; Russia strikes Kyiv bridges | Ukrainian drones/missiles struck the Crimea link; Moscow calls the damage minor. |
| 2 | Zaporizhzhia toll rises to 40; aid centre hit kills 26 | Russian strikes on Zaporizhzhia and a school used as a humanitarian aid centre. |
| 3 | Nvidia posts record $115.8bn quarter after Huang exit | Revenue more than doubled year on year; board says it will not bring Jensen Huang back as CEO. |
| 4 | U.S. loses measles elimination status | First time since 2000, after a year of uninterrupted spread. |
| 5 | Trump heads to China for Xi–Putin trilateral | First-ever three-way summit of the U.S., Chinese and Russian leaders, set for Thursday in Shenzhen. |
| 6 | Japan scrambles jets over Russian planes | Tokyo protests after two suspected Russian aircraft reportedly violated its airspace. |
| 7 | COP31 draft: faster fossil-fuel exit, $120bn finance | Antalya draft raises adaptation finance for developing nations by 2035. |

By the numbers strip: 4 tankers hit · 24 seafarers evacuated · $115.8bn Nvidia
revenue · 40 killed in Zaporizhzhia.

## Sources (web search, 18 Nov 2026)

- https://www.profilenews.com/en/november-17-2026-world-news/ — day roundup
  (Reuters: Qeshm strike; UKMTO tanker strike; Oman evacuation of 24 seafarers;
  Trump "dirty bomb" report; PAHO measles announcement; Kerch Bridge strike)
- https://podcastrex.com/shows/world-news-tonight-with-david-muir/full-episode-tuesday-november-17-2026
  — ABC World News Tonight episode summary, 17 Nov 2026
- http://newstrendtodaypk.blogspot.com/2026/11/morning-headlines-roundup-petrol-diesel.html
  — overnight roundup (Zaporizhzhia 40 / aid centre 26, via Al Jazeera; COP31 draft;
  Xi–Trump–Putin summit Thu 19 Nov)
- https://asaspress.com/en/news/world-news-digest-top-stories-of-november-17-2026
  — Gaza aid call, Depardieu, Japan jets, Houthi advance, Kerch Bridge
- https://allthingsrandom.net/ — World Brief, 17 Nov 2026 (JPMorgan/Zelle outage,
  United outage, third US carrier, EU Rwanda return hub)
- https://lifenewsagency.com/nvidia-q3-fy2027-results-record-revenue-vera-rubin/
  and https://www.fool.com/earnings/call-transcripts/2026/11/18/nvidia-nvda-q3-2027-earnings-call-transcript/
  — Nvidia Q3 FY2027: $115.8bn revenue (+103% YoY), data centre $107.6bn,
  Huang resigned 12 Nov, board will not reinstate him

**Honesty note.** Most day-roundup sources above are AI-generated news
aggregators that cite Reuters / AP / AFP / Al Jazeera; the underlying wire
reporting was not re-fetched from the wires themselves. No casualty figure
on the page comes from a single uncorroborated source: the Zaporizhzhia 40
and aid-centre 26 figures are attributed via Al Jazeera in the roundup, and
the Nvidia figures are confirmed across the earnings release, the Motley Fool
transcript and multiple reports. No quotes are invented; the "dirty bomb"
report is deliberately NOT given a number or presented as fact (it was
reported as unverified, and Iran denied it). The Depardieu story was
confirmed in search but cut from the page for space — it is not shown.

## Design

- 1024×1024 PNG, 121,185 bytes (< 1 MiB). Masthead with the date, one big
  lead story with a drawn illustration (Strait of Hormuz at dusk: tanker,
  smoke, sun — drawn with Pillow shapes, no external photos, no copyrighted
  images), 7 secondary stories with headline + one-line summary, and a
  "By the numbers" strip.
- Fonts: DejaVu Serif / DejaVu Sans (system fonts on the build VM, freely
  licensed). Nothing else is embedded.

## How it works

**main.py** is **pure Python 3 standard library** — no third-party imports,
no network. It copies the pre-generated image `assets/entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) byte-for-byte and
validates it first (PNG signature, dimensions ≤ 1024×1024, size ≤ 1 MiB,
every PNG chunk CRC, ends in IEND). This is the "simplest program" the
bounty page explicitly allows: *"the simplest program copies an image the
repository holds."*

The image itself was generated once at build time with Pillow
(`PIL 10.2.0`) by a local generator script (build-time only, not part of
the submitted program) and committed as `assets/entry.png`. The grader
runs `main.py` with stdlib only — it never needs Pillow.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # run again: identical bytes (see TRANSCRIPT.md)
```

## Submit checklist (still to do — nothing submitted yet)

- [ ] Create a public GitHub repo from this folder (`main.py` at root,
      `assets/entry.png`, `LICENSE`, `README.md`)
- [ ] Push to GitHub (no push has been made)
- [ ] On make.fun, enter the bounty `news-image-20261117`, paste the repo URL,
      include the AI transcript (see TRANSCRIPT.md)
- [ ] Submit before Thu 19 Nov 2026 07:00 WIB (00:00 UTC)

## CORRECTION 23:15 WIB 18 Nov 2026 (verified profile check)
- GitHub linked to the make.fun account is **supernyx002-dotcom**. The entry repo must be owned by supernyx002-dotcom, public, OSI licence, created after this bounty opened, at a named commit.
- Escrowed bounty: the linked Solana wallet must sign "make.fun entry v1" at submit.
- Submit via the bounty kit (`/c/<bounty>/kit`, RULES.txt) after `makefun login`. Limit usually 5 submissions per UTC day, 10 total; last before deadline is final. Transcripts via `makefun bundle` or loose upload ≤200 MB.
