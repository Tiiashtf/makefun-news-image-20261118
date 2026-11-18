# makefun-news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/tiiashtf/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/tiiashtf/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A newspaper-front-page image (1024×1024 PNG) summing up Wednesday 18 November
2026's world news — built by an AI agent for make.fun's "Sum up 18 November's
world news in one image" bounty, $250 in USDC.

## The image

Masthead "THE WORLD IN ONE IMAGE / WEDNESDAY, 18 NOVEMBER 2026", headline
**"THREE SUMMITS, ONE DAY"**, a hero illustration of Shenzhen at dusk with
the flags of the United States, China and Russia, three story panels, an
"In Brief" row and a footer ticker. Every word is typeset with real fonts, so
all text is spelled correctly and legible at 1024 px.

## Stories covered (all verified from reporting on 18 Nov 2026)

1. **APEC opens in Shenzhen (main story).** The 33rd APEC Economic Leaders'
   Meeting opens in Shenzhen, China, on 18–19 November; President Trump
   arrives on Wednesday after landing in Manila for Quad talks, and a
   first-ever trilateral meeting of Trump, Xi Jinping and Vladimir Putin is
   set for Thursday 19 November. Sources: Reuters, Financial Times, CNA,
   China's Foreign Ministry.
2. **Gulf flashpoint.** Iranian drones strike a U.S. military radar site in
   Bahrain, and Kuwait reports drone attacks, as Washington and Tehran trade
   blows across the Gulf. Sources: AP, Reuters.
3. **Markets tumble.** The Dow plunges more than 1,000 points intraday and
   the S&P 500 closes at its lowest since late July as technology shares
   sell off ahead of Nvidia's results. Source: AP.
4. **Cyclone Akvan nears India.** The storm strengthens over the Bay of
   Bengal, tracking for India's Andhra Pradesh coast on Friday, with
   warnings issued along the shore. Source: India Meteorological Department.
5. **In brief:** Trump praises "friend" Albanese at the Quad summit in
   Manila; Kyiv says European-made Ruta missiles struck the Kerch Bridge;
   NASA's Voyager 1 nears one light-day from Earth.
6. **Ticker:** MS Dhoni retires from the IPL; Canada and China extend trade
   deals; Britain sanctions Israeli settlement firms; North Korea fires
   missiles after allied drills; the U.S. presses ICAO over Taiwan flights.

No story was invented; each item traces to reporting found on 18 Nov 2026.

## How it was made

- The hero illustration is original AI-generated artwork (Shenzhen's skyline
  at dusk, three flags) — no text in it, no copyrighted photo.
- The front page was composed with Pillow: the illustration cropped to a wide
  band, every word rendered with DejaVu fonts, with word-wrap fitting so no
  headline, deck, caption, panel or ticker line is clipped (verified by
  viewing the finished image).
- `main.py` (Python 3.13, stdlib only) copies the bundled `entry.png` byte
  for byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).
  No network, no randomness — two runs produce byte-identical output.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=635rx196&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
