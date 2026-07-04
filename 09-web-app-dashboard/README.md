# 09 — Companion Ops Dashboard (Oct–Nov 2026, timed to the Web App unit)

Maps to: the entire **Web Application & Interface Design** unit — Web
Application Foundations, Interactive Web Pages, **Relational Databases**,
**Back Ends** — and its **Project**. Also feeds User-Centered Design
(Managing AI Engineering unit): your users are Behavior Frontiers staff and
leadership, and you can actually interview them.

The build: a web app showing how Companion is doing — questions asked,
answer feedback, retrieval quality over time, eval scores per release, and a
"what are staff actually struggling with?" view (which is discovery-interview
gold for P1). Home version runs on Companion-Home's logs; work version, same
pattern, work infra.

## The stack (boring on purpose — the unit is about fundamentals)

- **Database: SQLite → Postgres.** Design a real relational schema first, on
  paper: `questions`, `answers`, `sources`, `feedback`, `eval_runs`. Learn
  actual SQL — joins, aggregates, indexes — not just an ORM. (The Quantic
  course is *Relational Databases*; ORMs hide exactly what it teaches.)
  Practice: https://sqlbolt.com/ (free, interactive, excellent).
- **Back end: FastAPI** serving both HTML pages and a small JSON API.
  https://fastapi.tiangolo.com/tutorial/
- **Front end: server-rendered HTML (Jinja2) + one vanilla-JS interactive
  chart page.** No React yet — the unit is called *Interactive Web Pages*,
  not *SPA Frameworks*, and vanilla first means frameworks later make sense.
  MDN is the canon: https://developer.mozilla.org/en-US/docs/Learn
- **Charts:** Chart.js (simple) — https://www.chartjs.org/

## Build order

1. Schema on paper → SQLite + a seed script loading Companion-Home's logs.
2. Five SQL queries answered at the `sqlite3` prompt before any web code:
   busiest topics? worst-rated answers? retrieval hit rate by week? etc.
3. FastAPI read-only pages: questions list, answer detail with sources & feedback.
4. The interactive page: eval scores over time, filterable, Chart.js.
5. Write: feedback submission form (POST, validation, redirect — the whole
   old-school form cycle once, so you understand what SPAs abstract).
6. Auth-lite: a single shared admin password via env var (real auth is
   module 06/cloud territory; note the gap explicitly in the README).
7. User-centered design pass: show it to 2 real humans (work: your CTO and
   one department lead; the point of the course is you have real users) —
   watch them use it silently, write down where they stumble, fix the top 3.

## Done when

- [ ] Schema diagram committed; you can defend every table and index out loud
- [ ] The five questions answerable in raw SQL from memory-ish
- [ ] Dashboard runs locally: lists, detail, chart, working form
- [ ] Usability notes from 2 real users + the fixes shipped
- [ ] Write-up mapped to the Web App unit Project requirements (when Quantic
      publishes the rubric, gap-check against this and fill)
