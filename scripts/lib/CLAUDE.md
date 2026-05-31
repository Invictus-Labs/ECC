# CLAUDE.md — scripts/lib/

## Purpose
The internals behind the operator CLI: install runtime, per-harness target adapters, the
SQLite state store, session adapters, cost estimation, and skill evolution/improvement logic.

## Key Files
| File / Dir | Role |
|---|---|
| `install/` | Install runtime (`apply.js`, `config.js`, `request.js`, `runtime.js`) |
| `install-targets/` | One adapter per harness (claude/cursor/codex/gemini/opencode/zed/qwen/…) |
| `install-executor.js`, `install-lifecycle.js`, `install-manifests.js` | Plan→apply pipeline |
| `state-store/` | SQLite schema, migrations, queries (`sql.js`) |
| `session-adapters/` | Canonical session + claude-history + dmux-tmux adapters |
| `skill-evolution/`, `skill-improvement/` | Skill health/versioning/provenance + improvement |
| `cost-estimate.js` | Per-harness cost cache + estimation |
| `harness-adapter-compliance.js`, `inspection.js`, `hook-flags.js`, `github-discussions.js` | Audits/helpers |

## Internal Architecture
`install-manifests.js` resolves profiles→modules→components; `install-lifecycle.js` /
`install-executor.js` orchestrate the apply; `install-targets/registry.js` selects the
harness adapter; results persist via `state-store/`. Skill evolution tracks provenance and
versions so `doctor`/health checks can reason about drift.

## Public Interface
Modules consumed by `scripts/*.js`. Notable: `listAvailableLanguages` (used by `ecc.js`),
target adapter registry, `StateStore` queries.

## Dependencies
`sql.js`, `@iarna/toml`, `ajv` (transitively). Node stdlib.

## Dependents
Every top-level installer/operator script in `scripts/`.

## Conventions
- Add a harness by adding `install-targets/<harness>.js` + registering it — do not edit core.
- State-store changes require a migration in `state-store/migrations.js`.

## Gotchas
- Target adapters must use foreign-path-safe writes; tests assert no writes escape the target.
- The cost cache prefers the freshest entry (PR #2054) — stale caches were a past bug.

## Testing
`tests/lib/*.test.js` plus `tests/ci/*` and integration tests under `tests/integration/`.
