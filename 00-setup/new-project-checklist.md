# New Project Checklist — every project, every time

The self-contained-projects rule (~/.claude/CLAUDE.md), operationalized.
Run these six blocks for ANY new project — school, work-pattern, side build.
Total time: ~3 minutes. Skipping them is how July 4th happens.

## 1. Dedicated folder, never the home dir

```bash
mkdir -p ~/Desktop/"Fun Projects"/PROJECT-NAME   # or wherever it belongs
cd ~/Desktop/"Fun Projects"/PROJECT-NAME
```

## 2. Own repo + prove the root

```bash
git init
git rev-parse --show-toplevel   # MUST print this project's folder.
                                # Home dir or any parent? STOP.
```

## 3. .gitignore BEFORE the first commit

```bash
cat > .gitignore << 'EOF'
.env
.env.*
*.pem
*.key
.venv/
__pycache__/
*.pyc
.pytest_cache/
.DS_Store
*.pdf
EOF
```

Add project-specific lines for anything sensitive (logs with real data,
local databases, exports).

## 4. The pre-push gate (generalized — works in any repo)

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
top="$(git rev-parse --show-toplevel)"
if [ "$top" = "$HOME" ] || [ "$top" = "$HOME/Desktop" ]; then
  echo "🚫 BLOCKED: repo root is $top — never push from here."; fail=1
fi
exit $fail
EOF
chmod +x .git/hooks/pre-push
```

## 5. First commit, then create the remote FROM HERE (no web UI, no IDE buttons)

```bash
git add .
git status                      # read it. Anything surprising? Stop.
git commit -m "initial scaffold"
gh repo create PROJECT-NAME --public --source . --remote origin --push
#                            ^^^^^^^^ use --private for anything with real
#                            personal/financial/work-adjacent content
```

## 6. Verify from the outside

```bash
cd "$(mktemp -d)" && git clone --depth 1 https://github.com/jbisaccia-9/PROJECT-NAME.git && ls -R PROJECT-NAME | head -30
```

## Public or private? (decide in step 5, not after)

- **Public:** portfolio work built on synthetic/public data — the MSAIE
  workspace, Companion-Home, exercise repos.
- **Private:** anything touching real money, real accounts, or scheduled
  jobs whose logs could echo personal data — the morning-email job,
  trading-agent-v2 (until scrubbed and reviewed for a portfolio cut).
- **Neither (no remote at all):** anything work-related. Behavior Frontiers
  work lives on work infrastructure, full stop.
