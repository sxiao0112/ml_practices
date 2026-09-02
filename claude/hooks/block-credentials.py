#!/usr/bin/env python3
"""PreToolUse guard: block the assistant from ever reading credential / session
stores — most importantly the Playwright browser-profile directory that holds
LinkedIn login cookies and saved credentials.

Threat model
------------
The user logs into LinkedIn themselves in a real browser window; the assistant
never sees that. The residual leak vector is the *persisted session*: the
``.browser-profile/`` dir (cookies, tokens, "Login Data" DBs). If the assistant
ever cat/grep/Read that, it effectively sees credentials. This hook denies any
tool call that would read those locations.

It deliberately still ALLOWS passing ``.browser-profile`` as a
``--user-data-dir`` value to playwright / linkedin-connect, because that is how
collection works — it hands the dir to the browser without exposing its bytes.

Contract: read the PreToolUse JSON on stdin. Exit 2 (+ stderr) to block; exit 0
to allow. On unexpected input we fail OPEN (exit 0) so this global hook can never
brick unrelated work — the threat surface here is narrow and specific.
"""

from __future__ import annotations

import json
import os
import re
import sys

# --- sensitive locations (edit here to extend) ------------------------------
# Substrings that mark a credential / browser-session store anywhere in a path.
SENSITIVE_SUBSTRINGS = (
    ".browser-profile",      # this project's Playwright session store
    "/.aws/credentials",
    "/.netrc",
    "/.ssh/id_",             # private keys: id_rsa, id_ed25519, ...
)
# Exact file basenames that are credential databases (e.g. Chromium stores).
SENSITIVE_BASENAMES = {"Cookies", "Login Data", "Web Data"}

# In a Bash command, the ONLY allowed reference to the browser profile is as a
# --user-data-dir value handed to the browser. Strip those before scanning.
_USER_DATA_DIR_ARG = re.compile(r"--?user-data-dir[=\s]+\S*\.browser-profile\S*")


def _is_sensitive_path(p: str) -> bool:
    if not p:
        return False
    if any(s in p for s in SENSITIVE_SUBSTRINGS):
        return True
    return os.path.basename(p.rstrip("/")) in SENSITIVE_BASENAMES


def _bash_touches_sensitive(command: str) -> bool:
    # Allow the legitimate browser-launch / collect usage, then scan the rest.
    cleaned = _USER_DATA_DIR_ARG.sub(" ", command)
    if any(s in cleaned for s in SENSITIVE_SUBSTRINGS):
        return True
    return any(b in cleaned for b in SENSITIVE_BASENAMES)


def main() -> int:
    raw = sys.stdin.read()
    try:
        event = json.loads(raw)
    except (json.JSONDecodeError, ValueError):
        return 0  # fail open on unparseable input

    tool = event.get("tool_name", "")
    ti = event.get("tool_input", {}) or {}

    blocked_path: str | None = None
    if tool == "Bash":
        if _bash_touches_sensitive(str(ti.get("command", ""))):
            blocked_path = ".browser-profile / credential store"
    else:
        # Read / Edit / Write / NotebookEdit / Grep / Glob path-bearing fields.
        for key in ("file_path", "path", "notebook_path"):
            val = ti.get(key)
            if isinstance(val, str) and _is_sensitive_path(val):
                blocked_path = val
                break

    if blocked_path is None:
        return 0

    sys.stderr.write(
        "Blocked by block-credentials hook: this tool call would access a "
        f"credential/session store ({blocked_path}). The assistant is not "
        "permitted to read your login cookies or saved credentials. Passing "
        ".browser-profile as a --user-data-dir to playwright/linkedin-connect is "
        "allowed; reading its contents is not.\n"
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
