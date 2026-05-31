# CLAUDE.md — scripts/codex/

## Purpose
Codex-specific helpers: merging Codex TOML config and MCP config, and installing global git
hooks for the Codex workflow.

## Key Files
| File | Role |
|---|---|
| `merge-codex-config.js` | Merge ECC content into Codex's TOML config |
| `merge-mcp-config.js` | Merge MCP server entries into Codex config |
| `install-global-git-hooks.sh` | Install the global git hooks |
| `check-codex-global-state.sh` | Inspect Codex global state |

## Internal Architecture
TOML merges use `@iarna/toml` to preserve existing user config while adding ECC entries
idempotently. The shell scripts wire git hooks (`../codex-git-hooks/`) globally.

## Public Interface
`merge-codex-config.js` / `merge-mcp-config.js` are shipped in the npm `files` list and used
by the Codex install path; the `.sh` scripts are run during Codex setup.

## Dependencies
`@iarna/toml`, Node stdlib, bash.

## Dependents
Codex install-target adapter and Codex setup flow.

## Conventions
- Merges must be idempotent and must not clobber user config.
- Keep TOML round-tripping lossless.

## Gotchas
- Codex config is TOML, unlike the Markdown-first harnesses — different merge semantics.
- Global git hook install affects the user's machine globally; treat as a deliberate action.

## Testing
`tests/codex-config.test.js`, `tests/ci/codex-skill-surface.test.js`.
