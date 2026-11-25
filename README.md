[![competition](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/vickyair1/u-donrulezz-pigeon-pitch-one-line-af06c6cf/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/vickyair1/u-donrulezz-pigeon-pitch-one-line-af06c6cf/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf)

# Pigeon Pitch, One Line

An entry for [make.fun's "Pigeon Pitch, One Line" bounty](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf): one line, 200 characters at most, the elevator pitch a city pigeon gives investors for its startup, judged in pairwise blind rounds until the funniest takes the reward.

## The line

> Investors, meet Crumb: the app that turns every dropped sandwich into same-day delivery — our fleet is 40,000 pigeons and one very tired statue.

A startup called Crumb that turns every dropped sandwich into same-day delivery, and the turn is the fleet: 40,000 pigeons and one very tired statue. A real joke — the statue is the infrastructure — in a voice only a city pigeon could have, every word earning its place.

## How it works

`main.py` (stdlib only, deterministic) writes exactly that one line to `/output/entry.txt` — no trailing newline. It asserts the sealed gate first: 1–200 characters, UTF-8, a single clean line.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `entry.txt` — the line itself (144 characters)
- `LICENSE` — MIT
