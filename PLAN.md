# The Plan v2 — MSAIE × Behavior Frontiers × Portfolio

**Who:** Joseph Bisaccia — AI Engineer, Behavior Frontiers (agents/workflows/staff training across departments, reporting into CTO orbit)
**Program:** Quantic MSAIE, starts **July 20, 2026** (~13 months)
**Calendar:** Build sessions weekdays 7:00–8:15am PT. Quarterly career check-in, first Friday of Oct/Jan/Apr/Jul.

Every hour spent should hit at least two of three goals:
1. **Foundation** — fix the weak layers (hand-written code, mechanisms, statistics)
2. **Job** — workflows, agents, and training programs Behavior Frontiers actually needs
3. **Program** — artifacts that become Quantic projects/assignments with light scrubbing

---

## ⚠️ The Work/School Firewall (read before anything else)

Behavior Frontiers is a **healthcare company** (ABA therapy). Client data is
PHI under HIPAA. The rules, absolute:

1. **Nothing crosses from work to personal — no data, no code, no docs, no
   client or employee names.** Not into this folder, not into GitHub, not into
   a Quantic submission, not into a chat with me on your personal machine.
2. The safe direction is the reverse: **build the generic version at home
   first, on synthetic/public data, then re-implement at work.** Home version
   is yours and submittable; work version stays at work.
3. Before ANY Quantic submission that references the job: **written OK from
   the CTO**, generalized numbers, synthetic examples, company named only
   with approval. Get a standing agreement about this early — week one
   conversation, in writing.
4. The existing secrets rule (~/.claude/CLAUDE.md) applies on top of all this.

This isn't just compliance hygiene — "I run an AI program inside HIPAA
constraints" is one of your strongest career sentences. The firewall IS the
portfolio piece.

---

## The three flagship projects

**P1 — The AI Adoption Program (work-native, document-shaped)**
Your actual job, run deliberately: department-by-department pain-point
discovery → prioritized workflow pipeline → pilots with success metrics →
staff training curriculum → governance. Module `10-work-playbook` has the
templates. *Feeds:* AI & Organizational Transformation **Presentation**,
Managing AI Engineering **Project**, "Adopting AI in Your Organization,"
"User-Centered Design," "Professionalism and Ethics" (HIPAA ethics = free
material), "AI Leadership and Management."

**P2 — "Companion": Staff Knowledge Assistant + Ops Dashboard (home-built, work-deployed)**
A RAG-powered internal assistant that answers staff questions from an
SOP/policy corpus, with citations, an eval suite, and a web dashboard
(usage, feedback, retrieval quality) on a relational DB. Built at home on a
**synthetic corpus**; pattern re-implemented at work on real SOPs. Modules
`08` + `09`. *Feeds:* AI Engineering Techniques **Project** (Prompt
Engineering + RAGs to Riches + AI Agents), the entire **Web Application &
Interface Design** unit (foundations, interactive pages, relational DBs,
back ends) and its **Project**, Software Testing & CI/CD, Microservices,
Cloud specialization. **Capstone candidate #1.**

**P3 — Trading Agent (personal lab)**
Stays alive as the no-stakes-for-work sandbox: bare-metal loop, evals,
security red-teaming, refactor target. **Capstone candidate #2 / fallback.**
Capstone decision: ~March 2027, pick whichever has the better story.
(Current lean: P2 — an org-deployed assistant with evals and HIPAA-aware
design beats a personal trading bot in front of a rubric *and* a hiring
manager.)

---

## Curriculum map — every unit covered

| Quantic unit (sub-courses) | Where it's built here |
|---|---|
| **Managing AI Engineering** (AI-assisted dev, Managing AI App Dev I/II, User-Centered Design, Cloud Foundations, Ethics) + Project | P1 / `10-work-playbook`; you literally manage AI app development at work |
| **Web Application & Interface Design** (foundations, interactive pages, relational DBs, back ends) + Project | `09-web-app-dashboard` (Companion's dashboard) |
| **Software Testing & CI/CD** (Git/GitHub, testing & agentic dev, CI/CD, performance monitoring) | `00-setup` (git), `06-shipping-and-cloud` (pytest, Actions, Datadog) |
| **AI Engineering Techniques & Architectures** (prompt eng, adopting AI in your org, LLM apps/RAG, agents) + Project | `02-bare-metal-agent`, `08-rag-knowledge-assistant`, `03-evals`, P1 discovery work |
| **Software Design & Architecture** (UML, paradigms & patterns, enterprise architectures, cloud services) | `04-software-design` (trading-agent refactor + UML/patterns additions) |
| **ML → Fine-Tuning** (intro ML, preprocessing, linear algebra, logistic regression, trees/forests, clustering, deep learning, fine-tuning) | `05-ml-and-fine-tuning` (now classical-ML-first) |
| **AI & Organizational Transformation** (business transformation, leadership, augmented productivity) + Presentation | P1 — your first 90 days at Behavior Frontiers, written up |
| **Microservices** (design/build, deploy/test, scaling & Kubernetes) | `04` part 3 + `06` (split Companion's retrieval service; containerize; k8s awareness) |
| **Math for AI Eng spec** (differentiation, optimization, probability ×3) | `05` part 1 (now probability-forward) + `03` step 4 (small-n stats) |
| **Cloud Apps spec** (AWS foundations, migrating a web app, serverless) | `06` — and migrating Companion IS "Migrating an Existing Web Application" |
| **Capstone** + Presentation | P2 or P3, decided ~Mar 2027 |

Specializations: **Mathematics for AI Engineering + Cloud Applications** (unchanged).

---

## Phases

**Phase 0 — ramp (Jul 6–19), unchanged and MORE important now.**
Week 1: `00-setup` + ex01–ex03. Week 2: ex04–ex05 + agent skeleton running.
Hands only. The job makes this non-negotiable: you'll be reviewing and
shipping code with the engineering team, and Quantic's git course assumes it.
*Job task in parallel:* draft the discovery-interview template (`10-work-playbook`)
and get the CTO firewall agreement in writing.

**Phase 1 (Jul 20 → Oct): agents + RAG + evals — the AI Engineering unit.**
Finish `02` (mid-Aug) → build `08` Companion v0 at home (Sep) → `03` evals on
it (Sep–Oct). *At work:* run discovery interviews across 2–3 departments; pick
the first pilot workflow; log everything in the P1 templates.

**Phase 2 (Oct → Feb): web, testing, design — the software units.**
`09` dashboard (Oct–Nov, timed to Web App unit) → `06` CI/CD + monitoring
(Nov–Dec) → `04` refactor + UML/patterns (Dec–Feb, timed to Software Design
unit). *At work:* deploy Companion-at-work v1 + first training cohort.

**Phase 3 (Feb → Jun): ML ladder + math + security.**
`05` classical ML → deep learning → fine-tune (timed to the unit) with math
spec running alongside; `07` security red-team (Mar–Apr). *At work:* the
governance/security review of everything you've deployed — which doubles as
the Professionalism & Ethics material.

**Phase 4 (Mar 2027 →): capstone + presentation + next-role positioning** (`CAREER.md`).

---

## Weekly rhythm

- 5 × 7:00–8:15am build blocks (on your calendar now).
- **Fridays: ship + 3 lines in `LOG.md`.** Work-project weeks: log the
  *pattern* learned, never the data.
- One no-AI hour/week, forever.
- When Quantic assigns a project: check the map above first — the answer
  should usually be "adapt an artifact I already have," not "start something."

## How to work with me

Module 01 hands-only ("hint only"). Modules 02+: pair freely; `# YOU:` blocks
are yours. For work material: bring me *patterns and synthetic examples*, never
real org data — same firewall, this machine is the personal side of it.

House rule (in ~/.claude/CLAUDE.md): anything new or unfamiliar — a terminal
command, an algorithm, an idiom — comes with a brief 101 breakdown, inline in
the docs and code, scaled to how much it matters. If something shows up
unexplained and it's not basic Python/git, call it out; that's a bug.
