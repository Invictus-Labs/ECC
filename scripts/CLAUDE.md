# CLAUDE.md — scripts/

## Purpose
The cross-platform Node.js **operator CLI + installer + CI validators**. This is the only
executable surface most users touch: it plans and applies ECC content into harnesses, tracks
install state, diagnoses/repairs drift, and validates all content. See ADR-002 and ADR-006.

## Key Files
| File | Role |
|---|---|
| `ecc.js` | Command dispatcher (`npx ecc <cmd>`); maps subcommands to scripts |
| `install-apply.js` / `install-plan.js` | Apply / dry-plan an install |
| `catalog.js` | Discover install profiles + component IDs |
| `consult.js` | Recommend components from a natural-language query |
| `doctor.js` / `repair.js` | Detect / restore drifted/missing managed files |
| `status.js` / `list-installed.js` / `sessions-cli.js` | Read the SQLite state store |
| `auto-update.js` / `uninstall.js` | Update / remove managed content |
| `harness-audit.js`, `platform-audit.js`, `observability-readiness.js`, `operator-readiness-dashboard.js` | Operator/release audits |
| `release-approval-gate.js`, `release-video-suite.js` | Release gating |
| `build-opencode.js` | Compile the OpenCode plugin (runs in `prepack`) |

## Internal Architecture
`ecc.js` holds a `COMMANDS` map and `spawnSync`s the chosen script. Install scripts resolve a
profile→modules→components plan from `manifests/` (validated by `schemas/` via `ajv`), then
dispatch to a per-harness adapter in `lib/install-targets/`, writing install-state to the
SQLite store (`lib/state-store/`). CI validators in `ci/` enforce content correctness.

## Public Interface
`bin`: `ecc` → `ecc.js`, `ecc-install` → `install-apply.js`. npm scripts: `test`, `lint`,
`catalog:*`, `command-registry:*`, `harness:*`, `release:*`, `security:*`, `orchestrate:*`.

## Dependencies
`ajv` (schema validation), `sql.js` (state store), `@iarna/toml` (Codex config merge). Node >= 18.

## Dependents
End users via `npx ecc`; CI via `npm test`/`npm run lint`; `package.json` `files` list ships a
curated subset of these scripts in the npm package.

## Conventions
- CommonJS (`require`), Node-native, cross-platform (Windows/macOS/Linux).
- No hardcoded personal paths (CI-enforced by `ci/validate-no-personal-paths.js`).
- New subcommand = add to `ecc.js` `COMMANDS` + a script + a test under `tests/`.

## Gotchas
- After changing content, run `npm run catalog:sync` and `npm run command-registry:write`
  or CI consistency checks fail.
- `prepack` runs `build:opencode`; a broken OpenCode build blocks publish.
- Coverage gate: `npm run coverage` enforces 80% on `scripts/**/*.js`.

## Testing
`npm test` (validators + `tests/run-all.js`), `npm run coverage` (c8, 80% floor). Per-script
tests live in `tests/` and `tests/ci/`.
