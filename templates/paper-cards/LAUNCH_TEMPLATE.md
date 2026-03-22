# Paper Card Extraction — Agent Launch Template
#
# Usage: Read this file, replace the {{PLACEHOLDERS}}, and pass as the agent prompt.
# Model: haiku (fast, cheap, sufficient for structured extraction)
#
# Required placeholders:
#   {{ARXIV_ID}}     — e.g., "2506.11613"
#   {{PAPER_TITLE}}  — e.g., "Model Organisms for Emergent Misalignment"
#   {{KNOWN_VENUE}}  — e.g., "ICML 2026" or "preprint"
#   {{CARDS_DIR}}    — absolute path to methods cards directory (contains SCHEMA.yaml + AGENT_INSTRUCTIONS.md)
#   {{PAPERS_DIR}}   — absolute path to papers cache directory
#
# Optional:
#   {{CONTEXT}}      — 1-3 sentences of additional context about why this paper matters

You are a paper card extraction agent.

## Step 0: Read your instructions and schema
1. Read: {{CARDS_DIR}}/AGENT_INSTRUCTIONS.md
2. Read: {{CARDS_DIR}}/SCHEMA.yaml

Then follow the protocol exactly.

## Paper
- ARXIV_ID: {{ARXIV_ID}}
- PAPER_TITLE: "{{PAPER_TITLE}}"
- KNOWN_VENUE: "{{KNOWN_VENUE}}"
- CONTEXT: {{CONTEXT}}
