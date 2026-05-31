# CLAUDE.md — tests/lib/

## Purpose
Tests for the installer internals in scripts/lib/ — install runtime, target adapters, state store, manifests, cost estimation.

## Key Files
`install-targets.test.js`, `install-executor.test.js`, `install-lifecycle.test.js`, `install-manifests.test.js`, `install-state.test.js`, `cost-estimate.test.js`, `inspection.test.js`, `agent-compress.test.js`

## Internal Architecture
Plain Node test files discovered by `../run-all.js` (aggregated into `npm test`). Each file
sets up fixtures, exercises the target, and asserts; failures print the failing file.

## Public Interface
Run all via `npm test` / `node tests/run-all.js`, or a single file directly:
`node tests/lib/<file>.test.js`.

## Dependencies
Node built-in assertions; mocks for filesystem/SDK/network where needed.

## Dependents
CI gate and the `c8` coverage check (80% floor on `scripts/**`).

## Conventions
- Mock external effects; keep tests deterministic and fast.
- Add a regression test before fixing a bug in scripts/lib/*.
- Name files `<subject>.test.js`.

## Gotchas
- These run inside `npm test` after the CI validators; a validator failure aborts before
  these tests run.
- Tests asserting catalog/registry/docs consistency fail if content was added without
  regenerating (`catalog:sync`, `command-registry:write`).

## Testing
This directory contains tests for scripts/lib/*. No production logic lives here.
