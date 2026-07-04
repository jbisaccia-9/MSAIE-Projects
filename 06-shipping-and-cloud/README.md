# 06 — Testing, CI/CD, Shipping & Cloud (~Nov 2026 onward)

Now maps to TWO full units plus a specialization:
- **Software Testing & CI/CD**: Git/GitHub (done in `00-setup`), Software
  Testing & Agentic Software Development, CI/CD & Software Maintenance,
  **Performance Monitoring**
- **Microservices** II–III: Deploying & Testing, Scaling & Kubernetes
- **Cloud Applications spec**: AWS Foundations, **Migrating an Existing Web
  Application I/II**, Serverless — note: migrating Companion's dashboard
  (module 09) to AWS *is* that course's project shape. Plan for reuse.

The gap this closes is unchanged: nothing you build runs without you yet.

## Rung 1 — Testing for real (Nov, with the Testing course)

pytest on Companion-Home and the dashboard — https://docs.pytest.org/
- Unit tests for chunking/retrieval/scoring logic (pure functions first).
- **Testing AI systems specifically** (the "Agentic Software Development"
  angle, where you have real experience): deterministic tests for tools and
  guards; eval suites (module 03) for model behavior; record/replay LLM
  responses so tests don't burn API calls. Write LOG.md notes on where
  each kind of test belongs — that taxonomy is course-exam material.

## Rung 2 — CI (Nov–Dec)

GitHub Actions: every push → pytest + a smoke run of the RAG eval's code
scorers. One YAML file. Then add the pre-push secret-scan as a CI step too —
automate your own CLAUDE.md rule:
https://docs.github.com/en/actions

## Rung 3 — The morning email (first unattended deploy — unchanged)

Portfolio summary, weekdays 6:30am PT, GitHub Actions scheduled workflow.
**Its own self-contained repo** (per `00-setup/new-project-checklist.md`) —
NOT inside this workspace, NOT in the home-repo-tracked Trading Agent folder,
and **private**, since a scheduled workflow's logs can echo portfolio details.
Secrets in Actions Secrets only — the code reads env vars; no key ever exists
in the repo, and the pre-push hook enforces it. Read-only broker access —
execution stays human-in-the-loop on your machine, by architecture not
discipline.

## Rung 4 — Performance monitoring (Dec, with that course)

You have a **Datadog** connection — use it for real: instrument the FastAPI
dashboard (request latency, error rate) and Companion (retrieval latency,
token cost per answer, answers/day). One dashboard, one alert ("error rate
> X% over 15 min → notify"). Braintrust already covers the *quality*
telemetry; Datadog covers the *systems* telemetry; knowing which goes where
is the Performance Monitoring course in one sentence.

## Rung 5 — Containers & the microservice split (with Microservices II–III)

- Docker: https://docs.docker.com/get-started/ — containerize the retrieval
  service you split from Companion (module 04 part 3), run the pair with
  `docker compose`.
- Deploy to a free-tier host (Fly.io / Railway / Render — pick the
  friendliest free tier when you arrive).
- **Kubernetes: awareness, not mastery.** Do one local tutorial round
  (kind or minikube, https://kubernetes.io/docs/tutorials/) so the course's
  k8s material lands on experience — but a two-service system does not need
  k8s, and *saying so with reasons* is the correct exam-and-interview take.

## Rung 6 — AWS (timed to the Cloud spec, likely 2027)

The spec includes **AWS Academy Cloud Foundations** — Quantic provides the
AWS path, so don't pre-study generic AWS; instead arrive with a thing to
migrate. When "Migrating an Existing Web Application" opens, migrate the
dashboard (EC2-or-ECS + RDS Postgres), then do the Serverless course by
rebuilding the morning-email job as a Lambda. Real app, both times, zero
invented busywork.

## Done when

- [ ] Test suite green in CI on every push, secret-scan step included
- [ ] Morning email arrives with the laptop closed; failures notify you
- [ ] Datadog dashboard live with one meaningful alert
- [ ] Two containers on a free-tier host; k8s tutorial done + a written
      "why we don't need it yet"
- [ ] Dashboard migrated to AWS during the spec (placeholder until 2027)
