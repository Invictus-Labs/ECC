# CLAUDE.md — tests/ci/

## Purpose
Tests for the content validators and supply-chain/registry generators in scripts/ci/.

## Key Files
`validators.test.js`, `catalog.test.js`, `command-registry.test.js`, `no-personal-paths.test.js`, `agent-instruction-safety.test.js`, `scan-supply-chain-iocs.test.js`, `validate-workflow-security.test.js`, `code-reviewer-false-positive-guard.test.js`

## Internal Architecture
Plain Node test files discovered by `../run-all.js` (aggregated into `npm test`). Each file
sets up fixtures, exercises the target, and asserts; failures print the failing file.

## Public Interface
Run all via `npm test` / `node tests/run-all.js`, or a single file directly:
`node tests/ci/<file>.test.js`.

## Dependencies
Node built-in assertions; mocks for filesystem/SDK/network where needed.

## Dependents
CI gate and the `c8` coverage check (80% floor on `scripts/**`).

## Conventions
- Mock external effects; keep tests deterministic and fast.
- Add a regression test before fixing a bug in scripts/ci/*.
- Name files `<subject>.test.js`.

## Gotchas
- These run inside `npm test` after the CI validators; a validator failure aborts before
  these tests run.
- Tests asserting catalog/registry/docs consistency fail if content was added without
  regenerating (`catalog:sync`, `command-registry:write`).

## Testing
This directory contains tests for scripts/ci/*. No production logic lives here.
