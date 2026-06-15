# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This is a shared knowledge base for ML experiment workflows, synced across servers via Git and auto-loaded into Claude Code sessions. It contains best-practices docs, Claude Code configuration, reusable templates, and agent/skill definitions — not runnable application code.

## Setup

```bash
git clone https://github.com/sxiao0112/ml_practices.git ~/ml-best-practices
bash ~/ml-best-practices/install.sh
```

`install.sh` symlinks everything under `claude/` into `~/.claude/` so all sessions inherit shared rules, agents, commands, skills, and settings.

## Remotes

This repo is a fork. Two remotes are configured:

- **`origin`** — `https://github.com/sxiao0112/ml_practices.git` — your fork; day-to-day changes are pushed here. The SessionStart hook **auto-pulls from `origin` only**.
- **`upstream`** — `git@github.com:ecfm/ml-best-practices.git` — the original repo. **Not auto-pulled** — sync from it manually when you want upstream changes.

Pull upstream changes into your fork manually (keeps your own commits on top):

```bash
git fetch upstream
git rebase upstream/main
git push origin main --force-with-lease
```

## Repository Layout

```
claude/                     # Symlinked to ~/.claude/ on install
├── CLAUDE.md               # Global session instructions (routing table for best-practices docs)
├── settings.json           # Hooks (auto-pull, ruff format, ntfy notifications), status line
├── agents/                 # Haiku/Sonnet sub-agents invoked by Claude
│   ├── commit-push.md      # Stage → commit → push (rebase fallback)
│   ├── test-and-fix.md     # Run tests, fix implementation only
│   └── write-tests.md      # Write new tests, run until passing
├── commands/
│   └── sync-learnings.md   # /sync-learnings: commit + push learnings, then pull
├── rules/                  # Auto-loaded into every session
│   ├── coding-style.md     # uv, fail-fast, file logging, evidence preservation
│   ├── experiment-runs.md  # Smoke test first, complete each run, post-run checks
│   ├── decisions.md        # When to decide vs ask
│   └── report-writing.md   # Confidence levels, reasoning transparency
└── skills/
    └── deep-lit-review/    # /deep-lit-review skill: multi-agent orchestrated lit review

templates/
├── paper-cards/            # YAML schema + agent instructions for structured paper extraction
└── lit-review/             # Launch templates, search agent protocol, state tracking, report template

experiment-practices.md     # Output structure, logging, diagnostics, monitoring, vLLM
pipeline-architecture.md    # Modular pipeline design, type contracts, config management
research-methodology.md     # Agent iteration, evidential hierarchy, contradiction detection
```

## Key Agents & Commands

| Invocation | Agent/Command | When to use |
|---|---|---|
| `commit-push` agent | `claude/agents/commit-push.md` | All commits and pushes — never commit manually |
| `test-and-fix` agent | `claude/agents/test-and-fix.md` | After changes that could break existing behavior |
| `write-tests` agent | `claude/agents/write-tests.md` | New features with non-trivial logic |
| `/sync-learnings` | `claude/commands/sync-learnings.md` | End of session to push new learnings |
| `/deep-lit-review` | `claude/skills/deep-lit-review/` | Comprehensive literature exploration |

## Hooks (settings.json)

- **SessionStart** — pulls latest from this repo automatically
- **PostToolUse (Edit/Write)** — runs `ruff format` on modified Python files
- **Notification** — sends push notification via `ntfy.sh/$NTFY_TOPIC` when Claude stops (no-op if unset)

## Adding New Content

- **New best-practice rule** → add to `claude/rules/` (auto-loaded) and run `/sync-learnings`
- **New reusable agent** → add to `claude/agents/` and document in `claude/CLAUDE.md` routing table
- **New template** → add to `templates/` with a `SCHEMA.yaml` or `AGENT_INSTRUCTIONS.md`
- **Update knowledge bases** → edit `experiment-practices.md`, `pipeline-architecture.md`, or `research-methodology.md` directly
