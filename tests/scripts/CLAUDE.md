# CLAUDE.md — tests/scripts/

## Purpose
Tests for top-level scripts in scripts/ (dispatcher and operator commands).

## Key Files
top-level script test files

## Internal Architecture
Plain Node test files discovered by `../run-all.js` (aggregated into `npm test`). Each file
sets up fixtures, exercises the target, and asserts; failures print the failing file.

## Public Interface
Run all via `npm test` / `node tests/run-all.js`, or a single file directly:
`node tests/scripts/<file>.test.js`.

## Dependencies
Node built-in assertions; mocks for filesystem/SDK/network where needed.

## Dependents
CI gate and the `c8` coverage check (80% floor on `scripts/**`).

## Conventions
- Mock external effects; keep tests deterministic and fast.
- Add a regression test before fixing a bug in scripts/*.js.
- Name files `<subject>.test.js`.

## Gotchas
- These run inside `npm test` after the CI validators; a validator failure aborts before
  these tests run.
- Tests asserting catalog/registry/docs consistency fail if content was added without
  regenerating (`catalog:sync`, `command-registry:write`).

## Testing
This directory contains tests for scripts/*.js. No production logic lives here.
