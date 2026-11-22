# THE WORLD IN ONE FRAME — Saturday 21 November 2026

A single 1024x1024 PNG that sums up the world's news of Saturday 21 November
2026. Four stories, drawn as a newspaper front page in a 2x2 grid.

## The four stories

- **STRAIT OF HORMUZ — Iran runs a tanker convoy.** More than 14 tankers wait
  at Kharg Island, crews and flags assigned, to test the US naval blockade;
  oil revenue is set to reach zero by mid-December.
- **THE HAGUE — ICJ: Myanmar guilty of genocide.** For the first time a court
  holds a state responsible for genocide against the Rohingya, and orders
  Myanmar to investigate.
- **LUBLIN, POLAND — Russian missile lands in Poland.** An X-101 missile fell
  in a village in Lublin Voivodeship; the defence minister said nobody was
  injured.
- **WASHINGTON — Trump puts Iran strikes on hold.** The president said he is in
  no rush and will take up new strikes after the New Year; Israel keeps pressing
  for action.

Each panel carries a tag, a headline, a short body, and a small drawn icon
(tanker on a blockade line, courthouse with scales, missile trail with an
impact point, calendar with a pause sign).

## Files

- `build_image.py` — renders `entry.png` with Pillow primitives only.
- `entry.png` — the checked-in result (1024x1024, RGB, < 1 MiB).
- `main.ts` — copies the checked-in `entry.png` into the output directory.
- `README.md`, `LICENSE` — this file and the MIT license.

## Determinism

The image is fully deterministic: no network, no randomness, no timestamps.
`build_image.py` uses only Pillow primitives and a fixed DejaVu font, and every
string is wrapped with `draw.textlength` so nothing overflows its panel. Two
runs produce byte-identical PNGs.

## Build

```bash
python3 build_image.py      # writes entry.png
```

## Run

`main.ts` places the checked-in image into the output directory.

```bash
MAKEFUN_OUTPUT_DIR=/output tsx main.ts
```

`MAKEFUN_OUTPUT_DIR` defaults to `/output`. The directory is created if it does
not exist, and the copied `entry.png` is byte-identical to the repo copy.

## License

MIT — see `LICENSE`.
[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/axedotid/makefun-news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/axedotid/makefun-news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

## License

MIT - see LICENSE.
