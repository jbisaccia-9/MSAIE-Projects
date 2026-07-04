# 00 — Setup (~45 min, one clean run top to bottom)

One professional dev environment + this workspace published safely to GitHub.
Updated after the 2026-07-04 incident — the safety steps here are not optional.

## Step 0 — Disarm the home-folder repo (one-time)

Your home directory is itself a git repo (trading agent, local-only). It must
NEVER have a remote. Clear the stale one:

```bash
cd ~
git remote remove origin    # errors with "No such remote"? Even better — done.
git remote -v               # must print nothing
```

House rule (now in ~/.claude/CLAUDE.md): one project = one folder = one repo =
one remote. The home dir is never a project.

## Step 1 — Confirm uv

```bash
uv --version || curl -LsSf https://astral.sh/uv/install.sh | sh
```

✅ Done 2026-07-04: `uv 0.11.25`.

## Step 2 — Create THIS repo, and prove you're in the right one

```bash
cd "/Users/josephbisaccia/Desktop/AI Engineering Masters"
git init
git rev-parse --show-toplevel
```

That last command MUST print `/Users/josephbisaccia/Desktop/AI Engineering Masters`.
If it prints `/Users/josephbisaccia` — STOP, you're in the home repo. This
check is a reflex now: run it before any `git add`, anywhere, forever.

## Step 3 — Install the pre-push safety gate

Runs automatically on every push; blocks secrets, banned paths, and pushes
from the wrong repo root:

```bash
cat > .git/hooks/pre-push << 'EOF'
#!/bin/bash
fail=0
if git grep -nIE 'sk-ant-[A-Za-z0-9_-]{8,}|gho_[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{16,}|github_pat_|AKIA[A-Z0-9]{12,}|ASIA[A-Z0-9]{12,}|xox[baprs]-|AIza[A-Za-z0-9_-]{10,}|BEGIN [A-Z ]*PRIVATE KEY|eyJ[A-Za-z0-9_-]{20,}\.eyJ' -- .; then
  echo "🚫 BLOCKED: secret-looking content above."; fail=1
fi
if git ls-files | grep -iE '(^|/)(\.env(\..*)?|\.claude\.json|.*\.pem|.*\.key)$|(^|/)(Trading Agent|Medical|Finances|Mortgage|Personal|Professional)(/|$)'; then
  echo "🚫 BLOCKED: banned file/path tracked (above)."; fail=1
fi
case "$(git rev-parse --show-toplevel)" in
  *"AI Engineering Masters") ;;
  *) echo "🚫 BLOCKED: wrong repo root: $(git rev-parse --show-toplevel)"; fail=1 ;;
esac
exit $fail
EOF
chmod +x .git/hooks/pre-push
```

## Step 4 — First commit

```bash
git add .
git status    # modules + plan only; enrollment PDF must NOT appear (gitignored)
git commit -m "MSAIE workspace: plan, modules, exercises"
```

## Step 5 — Create the GitHub repo and push (terminal only, no web UI)

```bash
gh repo create MSAIE-Projects --public --source . --remote origin --push
```

Never use PyCharm "Share on GitHub" / VS Code "Publish" / github.com import —
those auto-detect enclosing repos, which is exactly how July 4th happened.

## Step 6 — Verify from the outside

```bash
cd "$(mktemp -d)" && git clone --depth 1 https://github.com/jbisaccia-9/MSAIE-Projects.git && ls -R MSAIE-Projects | head -40
```

You should see the modules and nothing else — no Trading Agent, no `.claude`,
no PDF. Local checks lie; the clone doesn't.

## Step 7 — The `ship` command (your Friday ritual)

```bash
git config alias.ship '!f(){ git add -A && git commit -m "${1:-ship: $(date +%F)}" && git push; }; f'
```

Usage: `git ship "week 1: ex01-ex03 done"` — stages, commits, pushes, with
the Step 3 gate screening every push.

## Step 8 — Git reflexes (10 min of reps)

```bash
git status          # what's changed
git diff            # read changes before committing
git add -p          # stage hunk-by-hunk (forces a re-read)
git log --oneline   # history
git rev-parse --show-toplevel   # WHICH repo am I in (the July 4th question)
```

## PyCharm

Fine as home IDE — but disable AI completion for module 01 (Settings →
disable AI Assistant / inline completion), and don't use its GitHub publish
buttons (see Step 5).

## Starting any OTHER project later?

Use `new-project-checklist.md` (same folder as this file) — the same
guardrails, generalized, ~3 minutes per project. Modules 04 and 06 will
point you back to it when their projects spin up.

## Done when

- [ ] Home repo has no remote (`cd ~ && git remote -v` → nothing)
- [ ] Workspace repo exists; root check prints the right path
- [ ] Pre-push hook installed and executable
- [ ] Pushed via `gh repo create`; fresh-clone verify shows modules only
- [ ] `git ship` alias works
