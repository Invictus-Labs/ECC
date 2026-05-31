# CLAUDE.md — scripts/lib/install/

## Purpose
The core install runtime: turns a resolved component plan into actual on-disk writes for a
selected harness target, handling config merges and request shaping.

## Key Files
| File | Role |
|---|---|
| `apply.js` | Executes the plan (copy/merge component files into target paths) |
| `config.js` | Resolves install configuration / options |
| `request.js` | Builds the install request from CLI args + manifests |
| `runtime.js` | Shared runtime state/context for an install run |

## Internal Architecture
`request.js` assembles what was asked for; `config.js` resolves options/profiles; `apply.js`
performs the writes through the chosen target adapter (`../install-targets/`); `runtime.js`
carries shared context (paths, dry-run flag, state-store handle) across the run.

## Public Interface
Functions consumed by `scripts/install-apply.js` / `install-plan.js` and
`scripts/lib/install-executor.js`.

## Dependencies
`../install-targets/`, `../state-store/`, `../install-manifests.js`, Node `fs`/`path`.

## Dependents
`install-apply.js`, `install-plan.js`, `install-executor.js`, `install-lifecycle.js`.

## Conventions
- Honor a dry-run/plan mode — `install-plan.js` must produce no writes.
- All writes go through a target adapter; never write target paths directly here.

## Gotchas
- Config/profile merge order matters; a later profile may override an earlier component.
- Writes must stay inside the resolved target root (foreign-path tests enforce this).

## Testing
Exercised via `tests/lib/*` and `tests/integration/`; install-target tests assert path safety.
This directory is logic-only (no persistent server/daemon).
