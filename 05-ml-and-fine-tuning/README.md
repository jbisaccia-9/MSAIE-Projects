# 05 — The ML Ladder: Classical ML → Deep Learning → Fine-Tuning
*(~Feb → Jun 2027, timed to the unit — which is classical-first, so we are too)*

Maps to the **ML → Fine-Tuning** unit's actual sub-courses: Intro to ML,
**Data Preprocessing**, Linear Algebra for ML, **Logistic Regression**,
**Decision Trees & Random Forests**, **Clustering**, Intro to Deep Learning,
AI Model Fine-Tuning. Plus the **Mathematics for AI Engineering**
specialization: Advanced Differentiation, **Optimization Models**,
**Probability Fundamentals & Distributions** (×2 — Quantic is telling you
where the weight is: probability).

## Part 0 — Math intuition (start ~4 weeks before the unit)

Probability-forward now, matching the spec:
- **3Blue1Brown probability/Bayes/central-limit videos** + *Essence of
  Linear Algebra* + *Essence of Calculus* (derivative chapters = Advanced
  Differentiation's intuition layer): https://www.3blue1brown.com/
- **Seeing Theory** (interactive probability, gorgeous): https://seeing-theory.brown.edu/
- Optimization = "derivatives, applied": gradient descent is the bridge
  between the two math courses. When you meet it in Part 2, you're doing
  Optimization Models homework whether Quantic knows it or not.
- Rigor reference: *Mathematics for ML* (free): https://mml-book.github.io/
- You already met Wilson intervals in module 03 — that was Probability
  Fundamentals in disguise. Connect the dots explicitly in LOG.md.

## Part 1 — Classical ML on ONE dataset you care about (the unit's spine)

Pick one tabular dataset and ride it through every sub-course. Two options:
- **Home:** your trading journal (by now hundreds of structured decisions
  from module 04's SQLite) — predict "trade hit its target?" from features.
- **Public healthcare-flavored** (safe, job-relevant, submittable):
  no-show appointments dataset or similar from https://archive.ics.uci.edu/
  or Kaggle. NOT work data. Ever.

Then the ladder, in scikit-learn (https://scikit-learn.org/stable/), one
rung per sub-course:
1. **Preprocessing:** missing values, encoding, scaling, leakage (the
   trading dataset teaches leakage viscerally: sneak tomorrow's price into a
   feature and watch fake glory), train/test/*time-based* splits.
2. **Logistic regression:** fit, read the coefficients, understand it IS
   the sigmoid + cross-entropy you'll meet again in deep learning.
3. **Trees & random forests:** overfit a single tree on purpose, watch the
   forest fix it, read feature importances skeptically.
4. **Clustering (unsupervised):** cluster your trades or patients-like
   records; confront "what even is k?"; learn why unsupervised results are
   where analytics goes to overclaim.
5. **The honest bake-off:** logistic vs. forest vs. "always predict the
   majority class." If the dumb baseline nearly wins, say so in LOG.md —
   that finding is more employable than a fake 95%.

## Part 2 — Deep learning from scratch (the rite of passage, unchanged)

**Karpathy, *Zero to Hero*** — https://karpathy.ai/zero-to-hero.html
micrograd (backprop by hand = Advanced Differentiation, applied) + makemore
part 1 minimum. Type every line yourself. This is the no-AI hour for weeks.

## Part 3 — Fine-tune something real (with the fine-tuning sub-course)

- Concepts: Hugging Face LLM course — https://huggingface.co/learn/llm-course
- Do: LoRA fine-tune of a small open model via Unsloth's free Colab
  notebooks — https://docs.unsloth.ai/
- **Job-shaped dataset idea:** fine-tune a small model to draft in "Meadowlark
  house style" (your synthetic SOP corpus from module 08 — internal comms,
  procedure summaries). Then module-03 it: **eval vs. few-shot prompting of a
  frontier model.** Whichever wins, the comparison memo is the artifact —
  and it's the exact build-vs-prompt decision you'll be asked to make at
  Behavior Frontiers with real money.

## Part 4 — The decision memo (unchanged, now with better ammo)

One page: prompt vs. RAG vs. fine-tune vs. classical ML — you'll have
personally built all four by now. When each wins, with your own numbers.
This memo doubles as a CTO-facing artifact at work.

## Done when

- [ ] One dataset ridden through preprocessing → logistic → forest → clustering, with the honest bake-off table
- [ ] micrograd + makemore typed and pushed
- [ ] One LoRA fine-tune, evaluated against prompting
- [ ] The four-way decision memo, in your words, with your numbers
