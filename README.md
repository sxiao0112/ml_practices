# ML/LLM Best Practices

Shared knowledge base for ML experiment workflows. Synced across servers via Git
and loaded into Claude Code sessions automatically.

## Contents

- **[experiment-practices.md](experiment-practices.md)** — Output structure, logging,
  diagnostics, monitoring, run ordering, early stopping, vLLM optimization. Read this
  before running or planning ML experiments.

- **[pipeline-architecture.md](pipeline-architecture.md)** — Modular pipeline design,
  type contracts, config management, stage caching. Read this when designing a new
  pipeline or adding a new method.

- **[research-methodology.md](research-methodology.md)** — Agent instruction iteration,
  structured paper extraction, external adversarial review, evidential hierarchy,
  contradiction detection. Read this when conducting literature review or planning
  research directions with AI agents.

- **[templates/paper-cards/](templates/paper-cards/)** — Reusable YAML schema and
  agent instructions for extracting structured methods cards from academic papers.
  Links claims to specific experiments with full provenance (models, datasets,
  evaluation methods, hyperparams).

- **[templates/lit-review/](templates/lit-review/)** — Multi-agent deep literature
  review skill. Orchestration loop with iterative follow-up, citation graph traversal
  (OpenAlex/Semantic Scholar), convergence-based stopping, and tiered reading.
  Includes search agent protocol, state tracking, and report templates.

## What Gets Synced

```
claude/
├── CLAUDE.md              → ~/.claude/CLAUDE.md          # Global instructions
├── settings.json          → ~/.claude/settings.json      # Hooks, theme, status line
├── commands/*.md          → ~/.claude/commands/           # Slash commands
└── rules/                 → ~/.claude/rules/             # Auto-loaded rules
    ├── coding-style.md    #   uv, fail-fast, logging, evidence preservation
    ├── experiment-runs.md #   smoke test, complete-each-run, post-run checks
    └── decisions.md       #   when to ask vs decide
```

## Setup

```bash
git clone https://github.com/sxiao0112/ml_practices.git ~/ml-best-practices
bash ~/ml-best-practices/install.sh
```

This symlinks all Claude Code config files so every session inherits shared rules,
commands, hooks, and settings.

### OpenAlex API key (recommended for lit reviews)

The lit-review and citation skills call the OpenAlex API. Without a key, every machine on your IP
shares a $0.10/day budget; a free key gives you $1/day. Create an account at https://openalex.org,
copy the key from https://openalex.org/settings/api, and save it to a private file:

```bash
mkdir -p ~/.config/openalex && printf %s "your-key" > ~/.config/openalex/api_key && chmod 600 ~/.config/openalex/api_key
```

A SessionStart hook in `settings.json` exports it as `OPENALEX_API_KEY` in every new Claude Code
session. (A plain `export` in `~/.bashrc` is not enough: Claude Code sessions launched by the
desktop app inherit their environment from a long-running server process, not from your shell.)

### Notifications (optional)

Hooks send push notifications via [ntfy.sh](https://ntfy.sh) when Claude Code
completes a task. This works over tmux/mosh/SSH where desktop notifications don't.

```bash
# Add to your shell profile (~/.bashrc or ~/.zshrc):
export NTFY_TOPIC="your-unique-topic"
```

Then subscribe to `ntfy.sh/your-unique-topic` on your phone or browser.
If `NTFY_TOPIC` is unset, the notification hook is a no-op.

## Usage

- Best practices are loaded into Claude Code sessions via the routing table in
  `claude/CLAUDE.md`
- Rules in `claude/rules/` are auto-loaded by Claude Code from `~/.claude/rules/`
- Use `/sync-learnings` at end of session to commit and push new learnings
- `runs.yaml` in each project repo tracks run stability (see experiment-practices.md
  section 11)
