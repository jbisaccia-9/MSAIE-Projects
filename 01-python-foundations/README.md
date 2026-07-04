# 01 — Python Foundations (Jul 7–15, hands only)

Five exercises, all in your domain (trading), all self-checking. No Claude, no
Copilot, no AI completion. Docs are allowed and encouraged — reading
[docs.python.org](https://docs.python.org/3/) is a skill, not cheating.
Search engines allowed; pasting the exercise into anything is not.

## How it works

Each file has functions with `# YOU: implement this` and a test suite at the
bottom. Run it:

```bash
python3 exercises/ex01_parse_trades.py
```

You'll see which tests fail. Make them pass. When you see
`ALL TESTS PASSED ✅` you're done — commit and move on.

**Stuck >30 min?** Ask Claude for a *hint only* ("hint only, don't write code").
That's the deal.

## The exercises

| File | Teaches | Time |
|---|---|---|
| `ex01_parse_trades.py` | strings, slicing, splitting, f-strings | 60–90 min |
| `ex02_positions.py` | lists, dicts, loops, accumulation patterns | 60–90 min |
| `ex03_position_sizing.py` | functions, edge cases, exceptions | 60–90 min |
| `ex04_portfolio_class.py` | classes, methods, state, `__repr__` | 90 min |
| `ex05_trade_report.py` | csv/json/datetime/pathlib — real files in, real files out | 90–120 min |

Order matters — each builds on the previous.

## After each exercise (5 min, do not skip)

1. `git add -p` — re-read every line you wrote as you stage it.
2. Commit with a real message.
3. In one sentence at the top of the file (a comment), write the thing that
   surprised you. If nothing surprised you, the exercise was too easy — tell
   Claude and we'll make a harder variant.

## Reference material (read as needed, not cover-to-cover)

- Official tutorial, ch. 3–5 & 9: https://docs.python.org/3/tutorial/
- *Automate the Boring Stuff* (free online): https://automatetheboringstuff.com/ — ch. on files & dicts
- Exercism Python track for daily reps: https://exercism.org/tracks/python

## When you're done

You should be able to answer these cold (say your answers out loud, then ask
Claude to grade you):
1. What's the difference between a list and a dict, and when do you reach for each?
2. What does `d.get(k, 0)` do that `d[k]` doesn't?
3. Why does `try/except` around *everything* make code worse, not safer?
4. What's `self`, actually?
5. Why did `round()` not do what you expected in ex05? (You'll see.)
