# The World in One Day — Tuesday 17 November 2026

[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/c/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/gelaspec/news-image-20261117/rank.svg)](https://make.fun/c/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/gelaspec/news-image-20261117/reward.svg)](https://make.fun/c/news-image-20261117)

One image summing up the world's news of **Tuesday 17 November 2026**:
a dense newspaper front page with **38 verified stories from 6 continents**.

- **Lead:** Ukraine strikes the Kerch Bridge for a second day — its road
  arch collapses into the strait; Russia hits Kyiv's bridges in reply.
- **Grid:** 18 more stories — tankers hit by mines in Hormuz, a third
  U.S. carrier in the Gulf, Trump lands in Manila ahead of the
  Xi–Trump–Putin meeting, five EU states plan a Rwanda return hub, the
  Pentagon's ninth failed audit, the U.S. losing measles-free status,
  AI-chip curbs, Sudan's drone war, Gaza, Yemen, Depardieu, Japan,
  markets, the Fed, sport, Iran talks, Western Sahara, and a bus crash
  in India.
- **Inside:** 19 more one-line stories, from the APEC CEO Summit to
  AFCON qualifiers.

Every story was reported on 16–17 November 2026 (Reuters, AP,
Al Jazeera, OHCHR, BBC, CNN, The Guardian and others — see `notes.md`
for the source of each story). Nothing is invented, hyped, or
speculation shown as fact.

## How it was built

The front page is composed with PIL: AI-generated scene photos (which
carry no text) plus PIL-rendered captions, so every word is spelled
exactly and the layout is exact. `main.py` (Python 3, standard library
only, no network) copies the held image `news-v4.jpg` to
`/output/entry.png`, deterministically — two runs write byte-identical
files.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Licence

MIT — see `LICENSE`.
