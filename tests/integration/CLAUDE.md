# CLAUDE.md — tests/integration/

## Purpose
Cross-module integration tests that exercise multiple components together (e.g. hook dispatch end-to-end).

## Key Files
`hooks.test.js`

## Internal Architecture
Plain Node test files discovered by `../run-all.js` (aggregated into `npm test`). Each file
sets up fixtures, exercises the target, and asserts; failures print the failing file.

## Public Interface
Run all via `npm test` / `node tests/run-all.js`, or a single file directly:
`node tests/integration/<file>.test.js`.

## Dependencies
Node built-in assertions; mocks for filesystem/SDK/network where needed.

## Dependents
CI gate and the `c8` coverage check (80% floor on `scripts/**`).

## Conventions
- Mock external effects; keep tests deterministic and fast.
- Add a regression test before fixing a bug in multiple scripts/ modules.
- Name files `<subject>.test.js`.

## Gotchas
- These run inside `npm test` after the CI validators; a validator failure aborts before
  these tests run.
- Tests asserting catalog/registry/docs consistency fail if content was added without
  regenerating (`catalog:sync`, `command-registry:write`).

## Testing
This directory contains tests for multiple scripts/ modules. No production logic lives here.
