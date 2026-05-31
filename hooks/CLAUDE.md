# CLAUDE.md — hooks/

## Purpose
JSON hook configurations that wire harness lifecycle events (PreToolUse, PostToolUse, Stop,
…) to the executable handlers in `scripts/hooks/`. This is the *config* half of the hook
system; the *logic* half lives in `scripts/hooks/`.

## Key Files
| File | Role |
|---|---|
| `hooks.json` | Primary hook config: matchers → command/notification hooks with ids + descriptions |
| `memory-persistence/hooks.json` | Memory-persistence hook bundle |
| `README.md`, `memory-persistence/README.md` | Human docs for the hook sets |

## Internal Architecture
Each hook entry has a `matcher` (tool name regex, e.g. `Bash`, `Edit|Write`), a `hooks` array
of `{type: "command", command: …}`, an `id`, and a `description`. Commands bootstrap the ECC
plugin root (resolving `CLAUDE_PLUGIN_ROOT` across install layouts) then invoke a dispatcher
or handler under `scripts/hooks/`.

## Public Interface
Consumed by the harness after install. Validated by `scripts/ci/validate-hooks.js` against
`schemas/hooks.schema.json`.

## Dependencies
`scripts/hooks/*` handlers, `scripts/lib/hook-flags.js`, the harness's hook runtime.

## Dependents
Installed harness config; `tests/hooks/`, `tests/integration/hooks.test.js`.

## Conventions
- Every hook has a stable `id` and a clear `description`.
- Warn-only hooks exit 0 but must surface their message (PR #2084).
- Use the plugin-root bootstrap so hooks resolve regardless of install layout.

## Gotchas
- The inline bootstrap one-liner is intentionally verbose — it must locate the plugin root
  across `~/.claude`, `plugins/`, and cache layouts. Do not "simplify" it blindly.
- A malformed `hooks.json` fails `validate-hooks.js` in CI, not at runtime.

## Testing
`tests/hooks/hooks.test.js`, `tests/integration/hooks.test.js`; schema via `validate-hooks.js`.
