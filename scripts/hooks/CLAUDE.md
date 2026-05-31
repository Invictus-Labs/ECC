# CLAUDE.md — scripts/hooks/

## Purpose
Executable hook handlers invoked by harness hook events (PreToolUse/PostToolUse/Stop/etc).
These back the JSON hook configs in the repo's `hooks/` directory and enforce guardrails
(no `--no-verify`, console-log checks, cost tracking, doc-file warnings, desktop notify).

## Key Files
| File | Role |
|---|---|
| `bash-hook-dispatcher.js` | Routes a bash tool event to the right handler |
| `block-no-verify.js` | Blocks `git commit --no-verify` style bypasses |
| `check-console-log.js` | Warns/blocks stray `console.log` |
| `check-hook-enabled.js` | Gates a hook on its enabled flag |
| `config-protection.js` | Protects sensitive config files from edits |
| `cost-tracker.js` | Records per-tool cost into the cost cache |
| `design-quality-check.js` | Frontend/design guardrail |
| `desktop-notify.js` | Desktop notification on events |
| `doc-file-warning.js` | Warns when writing doc files |
| `auto-tmux-dev.js` | Dev tmux automation |

## Internal Architecture
A harness fires a hook event; the dispatcher (or a direct handler) reads the event payload
from stdin/env, decides allow/warn/block, and exits with the convention the harness expects
(non-zero or structured output to block). Cost data flows into `../lib/cost-estimate.js`.

## Public Interface
Each script is a standalone CLI entrypoint invoked by the harness with the event on stdin.

## Dependencies
`../lib/hook-flags.js`, `../lib/cost-estimate.js`, Node stdlib.

## Dependents
The harness runtime (via `hooks/hooks.json` and installed hook configs).

## Conventions
- Honor exit-code semantics: 0 = allow, non-zero/structured = block; warn-only hooks must
  surface (see PR #2084 "surface warn-only PreToolUse hooks").
- Respect the per-hook enabled flag (`check-hook-enabled.js`).
- Never leak secrets in notifications or logs.

## Gotchas
- Hook scripts run in the harness's environment — keep them fast and dependency-light.
- Blocking too aggressively breaks developer flow; prefer warn unless it is a real guard.

## Testing
`tests/hooks/hooks.test.js`, `tests/integration/hooks.test.js`.
