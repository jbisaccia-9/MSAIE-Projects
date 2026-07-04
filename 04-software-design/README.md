# 04 — Software Design & Architecture (~Oct 2026 → Feb 2027)

Maps to: **Software Design & Architecture** (Design & UML, Paradigms &
Patterns ×2, Enterprise Architectures ×2, Cloud Services & Architectures)
and **Microservices I**.
This module is where you stop being "someone who directs AI to write code"
and become someone who can *judge* the code — which is the actual job.

## Part 1 — Reading, paced with the course

Two books, in this order:

1. **John Ousterhout, *A Philosophy of Software Design*** (~170 pages, readable).
   The single best book for your exact situation: it's about *judgment* —
   deep vs. shallow modules, where complexity comes from, when comments lie.
   Read one chapter per session; after each, find one violation of it in the
   Trading Agent codebase (there will be plenty; I wrote a bunch of it fast).

2. **Martin Kleppmann, *Designing Data-Intensive Applications*** — selected
   chapters only: 1 (reliability/scalability/maintainability), 2 (data models),
   5 (replication), 8 (distributed trouble). It's the canonical interview-prep
   text for systems thinking; don't grind all 600 pages.

Supplement when the Microservices course starts: https://microservices.io/patterns/
(free pattern catalog by Chris Richardson) — and know the counter-argument:
search "monolith first" (Martin Fowler). A candidate who can argue *against*
microservices intelligently stands out more than one who can recite them.

**Course-specific add-ons (match the sub-courses):**
- **Design & UML:** don't study UML abstractly — draw the refactored trading
  agent and Companion as you build them: one class diagram, one sequence
  diagram (the agent loop is a *great* sequence diagram), one component
  diagram each. Tool: https://mermaid.js.org/ (diagrams as code, lives in
  git, renders on GitHub — the modern take Quantic will accept happily).
- **Paradigms & Patterns:** as you refactor, name the patterns you're already
  using (adapter — literally your `adapters/` layer; strategy; repository;
  factory). https://refactoring.guru/design-patterns for the catalog. Rule:
  never introduce a pattern the refactor didn't demand; name what emerged.
- **Enterprise Architectures:** your P1 governance register + the
  work/school data boundaries ARE enterprise architecture in miniature.
  When the course opens, sketch Behavior Frontiers' systems-and-data-flows
  map (at work, generalized version for submission) — that's the assignment
  they'll ask for, drawn from a real org you actually mapped.

## Part 2 — The centerpiece: refactor the Trading Agent (the big one)

Today the trading agent is: a SKILL.md prompt + MCP servers + Claude Code as
runtime + markdown files as a database. That was the right way to prototype.

**⚠️ Location rule (self-contained-projects rule applies):** the existing
`~/Desktop/Trading Agent/` folder is tracked by the HOME-DIRECTORY repo —
do NOT grow the refactor there and never push from it. Start fresh:
create `~/Desktop/Fun Projects/trading-agent-v2/` following
`00-setup/new-project-checklist.md` (own `git init`, own `.gitignore`, own
pre-push hook, root-check before every add). Copy reference material IN
selectively (SKILL.md rules, trade-log for the journal import) — after
scanning it; the trade log stays out of any public repo. The old folder
stays behind as the archive.

Now rebuild it as software:

```
trading_agent/
  core/
    portfolio.py      # your ex04 Portfolio class, grown up
    rules.py          # no-buy list, risk caps — pure functions, zero I/O
    sizing.py         # ex03, grown up
  adapters/
    broker.py         # wraps Robinhood MCP/API — the ONLY file that talks to it
    market_data.py
    llm.py            # your module-02 agent loop lives here
  journal/
    log.py            # structured trade journal (SQLite, not markdown)
  cli.py              # entry point: `python -m trading_agent morning-loop`
  tests/              # pytest; core/ gets tested hard, adapters get mocked
```

Design rules to hold yourself to (all from Ousterhout):
- `core/` imports nothing from `adapters/`. Ever. Business logic must be
  testable without a network. This one constraint teaches half of software
  architecture.
- Every module's docstring says what it *hides* from its callers.
- When you can't decide where something goes, that's a design smell —
  bring me the question, we'll reason through it together. Design dialogue
  with AI is legitimate; typing skills you don't have yet isn't the risk here.

Learn **pytest** here (you've earned real tooling now):
https://docs.pytest.org/en/stable/getting-started.html — your ex01–ex05
hand-rolled test runners were pytest's job all along; feel the upgrade.

## Part 3 — Microservices, honestly (when that course starts)

Split ONE thing out of the refactored agent into a separate service — the
market-data fetcher is the natural cut. Give it a small FastAPI HTTP interface
(https://fastapi.tiangolo.com/), run it as a second process, and make the agent
call it over HTTP. Then write 500 words in LOG.md: what did the split cost you
(latency, deploy complexity, two things to monitor)? What did it buy? That
essay — "I split a service and here's what it actually cost" — is a better
interview answer than any diagram.

## Done when

- [ ] Ousterhout read, with one "violation found" note per chapter in LOG.md
- [ ] Trading agent refactored to the structure above, `core/` fully tested
- [ ] The old SKILL.md flow still works, now calling your package
- [ ] One service split out, and the honest cost/benefit essay written
