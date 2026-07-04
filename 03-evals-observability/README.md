# 03 — Evals & Observability, Done Right (target: September 2026)

You already have the instinct (Braintrust tracing on the trading agent, a
custom scorer, a spend guard). This module upgrades instinct to rigor. Evals
are arguably the single most in-demand practical AI skill in 2026 hiring —
every team has agents; almost none can tell if they're getting better.

Maps to: **AI Engineering Techniques & Architectures**, and it's the beating
heart of your capstone.

## Part 1 — The mindset shift (one evening of reading)

Read, in order:
1. Hamel Husain, *Your AI Product Needs Evals* — https://hamel.dev/blog/posts/evals/
2. Eugene Yan, *Patterns for LLM Systems* (evals section) — https://eugeneyan.com/writing/llm-patterns/
3. Anthropic docs, *Define your success criteria* + eval guide — https://docs.claude.com/en/docs/test-and-evaluate/define-success

The core idea to extract: **evals come from failures, not imagination.**
You don't invent test cases; you harvest them from traces of the thing
actually screwing up.

## Part 2 — Build a real eval for your trading agent (2–3 weeks)

The exercise in `eval_exercise.py` walks the full arc in plain Python — no
framework — so you understand what Braintrust does *for* you before you go
back to letting it do it.

**Step 1 — Harvest.** Go through your Braintrust traces + `trade-log.md`.
Collect 20 real moments where the agent made a judgment call. For each,
record: the situation (inputs), what the agent did, what it *should* have
done. That's your golden dataset. Format: `dataset.jsonl`, one JSON object
per line. This step is 80% of the value and cannot be skipped or delegated.

**Step 2 — Score.** Write two scorers:
- A *code scorer* for anything mechanical (did it respect the no-buy list?
  did position size stay under 2% risk? did it lead with the snapshot?).
- An *LLM-judge scorer* for judgment quality — and then **evaluate the judge
  itself**: run it 3× on the same 5 cases. If it disagrees with itself,
  fix the rubric until it doesn't. (You hit this exact wall in your
  Braintrust eval commit — now you'll know why.)

**Step 3 — Baseline, then regress.** Run the eval against your current
SKILL.md prompt. Record the score. Now change the prompt (improve it, or
sabotage it slightly) and re-run. If your eval can't detect the sabotage,
your eval is decorative. Iterate until it isn't.

**Step 4 — The statistics of small n.** The part almost everyone skips.
With 20 cases, score 14/20 vs 16/20 — is that improvement or noise?
Work through it:
- Binomial confidence intervals (look up "Wilson score interval" — plug in
  your numbers: at n=20, a ±20% swing is easily luck)
- Same logic applied to your *trading* results: how many trades before
  P&L means anything? (Spoiler: more than you have.)
- 3Blue1Brown's Bayes video pairs well here: https://www.youtube.com/watch?v=HZGCoVF3YvM

**Step 5 — Wire it back into Braintrust.** Port your plain-Python eval into
Braintrust properly: dataset uploaded, scorers registered, run on every
prompt change. Now you have what real teams call a regression suite.

## Done when

- [ ] 20-case golden dataset harvested from real traces, committed
- [ ] Code scorer + LLM judge, and the judge passes its own consistency test
- [ ] You detected a deliberate prompt sabotage via score drop
- [ ] You can say, with an actual interval, whether a 14→16 improvement is real
- [ ] One paragraph in LOG.md: "how I'd explain evals to a hiring manager"
