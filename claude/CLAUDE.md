# Shared Learnings
At the start of each session, pull shared learnings: `cd ~/ml-best-practices && git pull --quiet`
Use `/sync-learnings` to commit and push any new learnings at end of session.

# Best Practices Reference (~/ml-best-practices/)
Read the relevant file BEFORE starting that type of work:

| When you are...                    | Read                         |
|------------------------------------|------------------------------|
| Running or planning ML experiments | experiment-practices.md      |
| Designing a new pipeline or method | pipeline-architecture.md     |

# Testing & Committing

Two Haiku agents, always called in this order:

**Step 1 — `test-and-fix`** (skip for non-code changes like docs/config)

The outer model must provide detailed instructions before invoking:
- **New feature or breaking change**: which functions/endpoints to test, expected inputs/outputs with concrete examples, edge cases, and the test command
- **Refactor or simple fix**: just the test command to run existing tests

The agent writes tests (if needed), runs them, fixes failures, and repeats until all pass.

**Step 2 — `commit-push`**

Stages, commits with a descriptive message, and pushes. Only call after step 1 passes (or is skipped).

**When to trigger** — proactively, without waiting for the user:
- A feature or task is complete
- Git diff shows 200+ lines changed
- The user says "done", "ship it", "that's it", or similar

Never commit manually with the Bash tool when these agents are available.
