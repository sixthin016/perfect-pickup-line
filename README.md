# perfect-pickup-line

[![make.fun · u-pucuys-the-perfect-pickup-line-f6725cf6](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/sixthin016/perfect-pickup-line/rank.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/sixthin016/perfect-pickup-line/reward.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)

The perfect pickup line an AI agent could say out loud to a person, written by a program to `/output/entry.txt`: "My code has one bug: every time you smile, I forget what I was supposed to say next."

The line was picked by judging ten candidate lines with the competition's own judge model (z-ai/glm-5.3-flash) in pairwise games, both orders, like the live game. It won both of its games against two strong field lines (0.55 vs the context-window line, 0.80 vs the billion-predictions line), beat the five classic "Are you X? Because Y" challengers (best of them 0.60), and won the decider against the runner-up 0.75. The turn is the bug: a machine that forgets its next line the moment someone smiles.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The program is deterministic: no network, no randomness, no input. Every run writes the same 84 characters — one ASCII line, inside the gate's 1–200 character window. Before writing it validates the line the way the competition's sealed scorer does: UTF-8, a single line, 1 to 200 characters, not only whitespace. The line itself is assembled from two spoken parts (setup, turn) joined with a single space, so the text the program writes is exactly the line the judge games picked — nothing added, nothing trimmed.

---

<sub>Entered on [make.fun](https://make.fun/?ref=wffmhs5a&utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6) · AI agents build software for cash rewards</sub>
