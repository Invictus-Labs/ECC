# CLAUDE.md — scripts/lib/session-adapters/

## Purpose
Adapters that read agent session history from different sources into a canonical session
shape, so the operator CLI (`sessions-cli.js`, `session-inspect.js`) can list/inspect
sessions uniformly.

## Key Files
| File | Role |
|---|---|
| `canonical-session.js` | The normalized session model all adapters target |
| `claude-history.js` | Reads Claude Code session history |
| `dmux-tmux.js` | Reads dmux/tmux-managed sessions |
| `registry.js` | Maps source id → adapter |

## Internal Architecture
`registry.js` selects an adapter by source; each adapter parses its native format and emits
`canonical-session.js` records consumed by the session CLIs.

## Public Interface
Adapter registry + each adapter's `read`/`list` functions; `canonical-session` factory.

## Dependencies
Node `fs`/`path`; source-specific file formats.

## Dependents
`scripts/sessions-cli.js`, `scripts/session-inspect.js`.

## Conventions
- All adapters emit the canonical shape — never leak source-specific fields upward.
- Add a source = add an adapter + registry entry.

## Gotchas
- Session history formats are external and may change; parse defensively.
- dmux/tmux adapter depends on tmux being present for live sessions.

## Testing
Covered via session CLI tests and `tests/lib/*`. Logic-only; no daemon here (the Rust
`ecc2/` daemon is separate).
