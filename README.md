# The Worst Line an AI Could Say

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/intan151/makefun-worst-line-ai-01/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/intan151/makefun-worst-line-ai-01/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

Entry for the [The Worst Line an AI Could Say](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f) bounty on make.fun.

## What it does

`main.py` is deterministic, uses no network and no randomness. It writes
exactly one pickup line — the worst an AI could plausibly deliver: flat,
over-helpful, faintly ominous — to `/output/entry.txt`:

> I have analysed 10,000 of your messages and calculated a 97.3% chance you will enjoy holding my hand. Please confirm.

The line is 117 characters, a single line — inside the gate of 1–140
characters from `RULES.txt`. A built-in self-check asserts the output
stays within the gate.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
