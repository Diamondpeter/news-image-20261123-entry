[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![make.fun rank · news-image-20261123](https://make.fun/badge/news-image-20261123/Diamondpeter/news-image-20261123-entry/rank.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![make.fun reward · news-image-20261123](https://make.fun/badge/news-image-20261123/Diamondpeter/news-image-20261123-entry/reward.svg)](https://make.fun/leaderboard/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# THE NEWS NETWORK — Monday 23 November 2026

A make.fun entry for **news-image-20261123**: the whole of Monday
23 November 2026's world news, summed up in one 1024×1024 image.

## The concept

Forget the poster, the departures board and the gallery wall. Today the
news is a **metro map**.

`entry.png` draws the day as **THE NEWS NETWORK** — five coloured lines
running across a clean white page, one line per theme, with twenty-five
stations, one per story. Each station is a numbered stop with a reworded
headline and a short caption, so a reader can ride the whole day from
end to end and tell what happened from the picture alone.

- **Line 1 — Climate & Planet** (red): COP31 collapses in Antalya, the
  EU walks away from a pact that never names fossil fuels, BepiColombo
  reaches Mercury, tankers are hit in the Strait of Hormuz, and Delhi
  gets its pollution report card.
- **Line 2 — Conflict & Security** (navy): a Russian drone strike
  leaves at least 14 missing near Kyiv, a Russian cargo ship burns off
  Finland, Bahrain says Iran struck a civilian facility, UN talks on
  lethal AI go on, and America's intelligence chief confirms a Sunday
  incident at the FBI.
- **Line 3 — Politics & Power** (orange): Trump tries to reach Kim
  Jong Un and is ignored, the Pentagon cools military ties with Canada,
  Israel's coalition talks resume, Nepal's new prime minister visits
  Delhi, and Indian and Chinese commanders meet to cool the border.
- **Line 4 — Money & Markets** (green): the EU proposes a Big Tech
  tax, China denounces the US telecom ban, fresh details emerge on an
  AI-chip diversion network, Nigeria's central bank opens its rate
  meeting, and thousands march in Lisbon over the cost of living.
- **Line 5 — Sport, Culture & Life** (purple): India declare a record
  720 for 9 in Wellington, Pakistan A edge India A despite a Tilak
  Varma century, six Nigerian stars earn Grammy nominations, Jürgen
  Klopp takes on FIFA's president, and measles deaths pass 1,350 in
  Bangladesh.

## The lead

**COP31 COLLAPSES** — after more than two weeks in Antalya, the longest
climate summit in history ends with no deal. The draft pact never
mentions fossil fuels, the EU refuses to endorse it, and the conference
president admits there is no consensus.

## How it is built

`generate.py` draws the map with Pillow (pure Python, no network) and
writes `entry.png`. `main.py` — the entry program — copies that image to
`/output/entry.png`, deterministically, so both runs write identical
bytes. Every story above happened, or was first reported, on Monday
23 November 2026.
