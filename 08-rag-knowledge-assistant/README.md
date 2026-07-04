# 08 — "Companion": RAG Staff Knowledge Assistant (Sep 2026, then ongoing)

Maps to: **LLM-Based Apps ("RAGs to Riches")**, **Prompt Engineering**, and
**AI Agents** in the AI Engineering unit — this project + module 02 + module 03
together are your **AI Engineering Techniques & Architectures Project**.
And it's Goal 2 incarnate: your job is staff training and workflow support
across departments; a cited, evaluated knowledge assistant is the
highest-leverage single thing you can ship there.

## The firewall version of this build

You build **Companion-Home** here: same architecture, synthetic corpus.
At work you re-implement **Companion-Work** on real SOPs, on work
infrastructure, in work repos. Code may be *similar* because you wrote both
from the same understanding — but nothing is copied across, and no work
document ever touches this repo. Quantic sees Companion-Home (always safe)
plus generalized results from work (with CTO sign-off).

## Step 0 — Build the synthetic corpus (with me — this is legit AI work)

Generate ~30 fake SOP/policy documents for an imaginary multi-clinic
healthcare-ish company ("Meadowlark Behavioral Services"): onboarding
procedures, scheduling policies, incident reporting, PTO rules,
documentation standards. Deliberately include the nasty real-world traits:
two docs that contradict each other, an outdated superseded version, jargon,
a 40-page monster. A RAG system that only works on clean docs is a demo,
not a system.

## Step 1 — Naive RAG, no framework (same philosophy as module 02)

Pipeline, plain Python: chunk docs → embed chunks (an embedding API) →
store vectors (start: a JSON file + cosine similarity in numpy — seriously,
at 30 docs you do NOT need a vector database, and knowing *when* you don't
is the senior-engineer take) → retrieve top-k for a query → stuff into a
prompt → answer **with citations to source docs**.

Prompt-engineering discipline (the Quantic course will cover theory; you'll
have practice): version your prompts in git, one change at a time, measured.

## Step 2 — Evaluate it (module 03 muscle, applied)

Build the eval BEFORE improving anything:
- 25 Q&A pairs from your synthetic corpus: easy lookups, cross-doc questions,
  questions hitting the contradictions, questions with NO answer in the corpus
  (the most important category — measure hallucinated answers).
- Metrics: retrieval hit rate (did the right chunk surface?), answer
  correctness, citation accuracy, refusal correctness on unanswerables.

## Step 3 — Improve with evidence

Now iterate, re-running the eval each change: chunking strategy, top-k,
query rewriting, reranking, "answer only from context" prompt hardening.
Keep a table in LOG.md: change → metric movement. That table is the single
most interview-impressive artifact this module produces.

## Step 4 — Agent-ify (bridges to module 02)

Wrap retrieval as a *tool* your bare-metal agent calls, so it can decide to
search, search again with a better query, or say "not in the docs." Compare
agentic-RAG vs. single-shot RAG on your eval. Now you understand the
architecture choice instead of following fashion.

## Step 5 — Take the pattern to work

Re-implement at work with the engineering team (their infra, their review).
Where home used JSON+numpy, work may want pgvector/managed search — evaluate
against the same eval *structure* (built from real staff questions, which
you'll harvest from your training sessions). Ship with: citations mandatory,
"I don't know" wired in, feedback button, usage logging (→ module 09's
dashboard), and a HIPAA rule — **the corpus is policies and procedures,
never client records.** Scope is a security control (module 07 vocabulary:
you're denying the trifecta a leg).

## Done when

- [ ] Companion-Home answers with citations and refuses unanswerables
- [ ] 25-case eval with the four metrics, baseline vs. improved table in LOG.md
- [ ] Agentic vs. single-shot comparison, measured
- [ ] Work version scoped, CTO-blessed, and piloted with one department
- [ ] Write-up drafted for the AI Engineering unit project (scrubbed)
