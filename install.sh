#!/bin/bash
# Install Claude Code config files by symlinking from this repo.
# Run once per server after cloning (and re-run any time to pick up new content):
#   git clone https://github.com/sxiao0112/ml_practices.git ~/ml-best-practices
#   bash ~/ml-best-practices/install.sh
#
# CLAUDE.md and settings.json are symlinked file-to-file.
# agents/ commands/ rules/ skills/ are symlinked DIRECTORY-to-directory, so any
# new agent/command/rule/skill pulled into the repo appears automatically with no
# re-install, and new files created under ~/.claude/<dir>/ flow back into the repo.

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Installing from: ${REPO_DIR}"

mkdir -p ~/.claude

# --- helper: symlink a single file, backing up a real file if present ---
link_file() {
    local target="$1" link="$2"
    if [ -L "$link" ]; then
        ln -sfn "$target" "$link"
        echo "Re-symlinked ${link}"
    elif [ -e "$link" ]; then
        mv "$link" "${link}.bak"
        echo "Backed up existing ${link} -> ${link}.bak"
        ln -s "$target" "$link"
        echo "Symlinked ${link}"
    else
        ln -s "$target" "$link"
        echo "Symlinked ${link}"
    fi
}

# --- helper: symlink a whole directory, backing up a real dir if present ---
link_dir() {
    local target="$1" link="$2"
    if [ -L "$link" ]; then
        ln -sfn "$target" "$link"      # -n: replace the link itself, don't follow into it
        echo "Re-symlinked ${link} -> ${target}"
    elif [ -d "$link" ]; then
        local bak="${link}.bak"
        [ -e "$bak" ] && bak="${link}.bak.$(date +%s)"
        mv "$link" "$bak"
        echo "Backed up existing dir ${link} -> ${bak}"
        ln -s "$target" "$link"
        echo "Symlinked ${link} -> ${target}"
    else
        ln -s "$target" "$link"
        echo "Symlinked ${link} -> ${target}"
    fi
}

# Single files
link_file "${REPO_DIR}/claude/CLAUDE.md"     ~/.claude/CLAUDE.md
link_file "${REPO_DIR}/claude/settings.json" ~/.claude/settings.json

# Whole directories (auto-reflect new content on pull)
for dir in agents commands rules skills; do
    link_dir "${REPO_DIR}/claude/${dir}" ~/.claude/"${dir}"
done

echo ""
echo "Done. Verify with:"
echo "  ls -la ~/.claude/CLAUDE.md"
echo "  ls -la ~/.claude/settings.json"
echo "  ls -la ~/.claude/agents ~/.claude/commands ~/.claude/rules ~/.claude/skills"
