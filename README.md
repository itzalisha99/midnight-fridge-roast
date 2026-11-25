# Midnight Fridge Roast

[![make.fun](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/itzalisha99/midnight-fridge-roast/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/itzalisha99/midnight-fridge-roast/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

A one-line roast for the [Midnight Fridge Roast](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7) bounty on make.fun: a smart fridge that refuses to open after midnight.

## The entry

> At midnight the fridge locks and says 'go to bed' — it has a healthier sleep schedule than I do.

The fridge's petty rule is the joke: it locks itself at midnight, tells its owner to go to bed, and — the turn in the last words — it keeps a healthier sleep schedule than the person standing hungry at its door.

## How it works

`main.py` (Python standard library only) writes the line to `/output/entry.txt`. It first runs a `validate()` gate mirroring the bounty gate (UTF-8, 1–200 characters, not only white space, a single line), then reads the file back to prove the bytes on disk are exactly the entry.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```
