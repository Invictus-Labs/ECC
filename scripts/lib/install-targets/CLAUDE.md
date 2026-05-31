# CLAUDE.md — scripts/lib/install-targets/

## Purpose
Per-harness install adapters. Each module knows ONE harness's on-disk layout and how to map
ECC components into it. This is the extension point for supporting a new harness (ADR-002).

## Key Files
| File | Harness |
|---|---|
| `claude-home.js` / `claude-project.js` | Claude Code (user-home / per-project) |
| `cursor-project.js` | Cursor |
| `codex-home.js` | Codex |
| `gemini-project.js` | Gemini |
| `opencode-home.js` | OpenCode |
| `zed-project.js`, `qwen-home.js`, `codebuddy-project.js`, `joycode-project.js`, `antigravity-project.js` | Other harnesses |
| `helpers.js` | Shared path/write helpers |
| `registry.js` | Maps target id → adapter module |

## Internal Architecture
`registry.js` resolves a target id to an adapter. Each adapter exposes a uniform contract
(resolve target paths, map components, write) and uses `helpers.js` for safe writes confined
to the target root.

## Public Interface
The adapter registry + each adapter's `apply`/path-resolution functions, consumed by
`../install/apply.js`.

## Dependencies
`helpers.js`, Node `fs`/`path`, `os` (home dir resolution).

## Dependents
`scripts/lib/install/apply.js`, `install-executor.js`.

## Conventions
- New harness = new adapter file + a `registry.js` entry; do not edit existing adapters.
- Never write outside the resolved target root; use `helpers.js`.
- Home-based vs project-based targets are distinct adapters (e.g. `claude-home` vs `claude-project`).

## Gotchas
- A regression where an adapter writes a "foreign path" is explicitly tested against
  (see git history: claude-project foreign-path test).
- Codex uses TOML config merge (`@iarna/toml`) — different shape from Markdown harnesses.

## Testing
`tests/lib/*` and install-target-specific tests assert path containment and correct mapping.
