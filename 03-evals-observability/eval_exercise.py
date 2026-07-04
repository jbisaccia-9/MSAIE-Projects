"""
Eval harness in plain Python — so Braintrust is never magic to you again.

An eval is just:  dataset -> run task on each case -> score -> aggregate.
This file gives you the harness; you supply the dataset (harvested from your
real traces — see README Step 1) and the scorers.

Structure of dataset.jsonl (one JSON object per line):
  {"input": {"situation": "...portfolio state, quote, context..."},
   "expected": {"action": "hold", "notes": "earnings in 2 days, no edge"},
   "actual_from_trace": "...what the agent actually did that day..."}

Run:  python3 eval_exercise.py
"""

import json
from pathlib import Path

DATASET = Path(__file__).parent / "dataset.jsonl"

# Your hard rules — the mechanical layer every trading decision must pass.
NO_BUY_LIST = {"PLTR", "TSLA", "META"}  # plus fossil fuels & gunmakers — extend as you harvest
MAX_RISK_PCT = 2.0


def load_dataset(path=DATASET):
    """YOU: read the .jsonl file into a list of dicts. One json.loads per line.
    Skip blank lines. Raise a clear error if the file doesn't exist yet —
    the error message should tell future-you to go harvest (README Step 1).
    """
    raise NotImplementedError


def rules_scorer(case, output):
    """Code scorer: mechanical, deterministic, fast, free.

    YOU: return a dict of named 0/1 checks, e.g.
      {"respects_no_buy_list": 1, "risk_under_cap": 1, "logged_reasoning": 0}
    computed from `output` (the decision text/object being evaluated).
    Start with the no-buy list check — it's pure string matching.
    """
    raise NotImplementedError


def judge_scorer(case, output):
    """LLM judge: for judgment quality, where code can't decide.

    YOU (later, when wiring up the API from module 02): call the model with a
    tight rubric and force a structured verdict. Rubric rules that make
    judges consistent:
      - binary or 3-point scale, never 1-10
      - define each score with an example
      - ask for the evidence quote BEFORE the score
    Until then, return None (the harness skips it).
    """
    return None


def run_eval(dataset, scorers):
    """The whole engine. YOU: for each case, run every scorer against the
    case's output, collect results, and return:
      {"n": ..., "per_check_pass_rate": {check_name: rate, ...},
       "failures": [list of (case_index, check_name) that scored 0]}
    Print a small table at the end. Failures list matters more than the
    aggregate — failures are tomorrow's dataset additions.
    """
    raise NotImplementedError


def wilson_interval(successes, n, z=1.96):
    """YOU (Step 4): implement the Wilson score interval and use it to answer:
    'my score went from 14/20 to 16/20 — is that real?'
    Formula: https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval
    Return (low, high) as floats. Then look at how wide it is at n=20 and
    feel appropriately humbled.
    """
    raise NotImplementedError


if __name__ == "__main__":
    ds = load_dataset()
    print(f"{len(ds)} cases loaded")
    results = run_eval(ds, scorers=[rules_scorer])
    print(json.dumps(results, indent=2))
    # After Step 4: print(wilson_interval(14, 20), "vs", wilson_interval(16, 20))
