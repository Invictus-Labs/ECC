# CLAUDE.md — scripts/codex-git-hooks/

## Purpose
The git hook scripts installed by the Codex workflow (`../codex/install-global-git-hooks.sh`)
to enforce checks at commit/push time.

## Key Files
| File | Role |
|---|---|
| `pre-commit` | Runs checks before a commit is created |
| `pre-push` | Runs checks before pushing |

## Internal Architecture
Standard git hook executables. They run validation/guardrail logic and exit non-zero to block
the git operation on failure.

## Public Interface
Invoked by git, not called directly. Installed globally or per-repo by the Codex setup script.

## Dependencies
A POSIX shell; whatever validators the hooks invoke.

## Dependents
The user's git workflow once installed; the Codex setup scripts.

## Conventions
- Exit non-zero to block; print a clear reason.
- Keep hooks fast — they run on every commit/push.

## Gotchas
- These modify git behavior on the user's machine; document clearly and make opt-in.
- A `--no-verify` bypass is independently discouraged by `../hooks/block-no-verify.js`.

## Testing
Exercised via the Codex workflow tests; hooks are shell scripts (no unit harness here).
This directory holds no stateful service — only git lifecycle scripts.
