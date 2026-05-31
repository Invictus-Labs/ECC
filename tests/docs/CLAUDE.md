# CLAUDE.md — tests/docs/

## Purpose
Docs-surface tests: assert documentation, manifests, and identifiers stay consistent (e.g. install identifiers, ecc2 release surface, copilot support).

## Key Files
`install-identifiers.test.js`, `ecc2-release-surface.test.js`, `mcp-management-docs.test.js`, `copilot-support.test.js`, `harness-adapter-compliance.test.js`, `evaluator-rag-prototype.test.js`

## Internal Architecture
Plain Node test files discovered by `../run-all.js` (aggregated into `npm test`). Each file
sets up fixtures, exercises the target, and asserts; failures print the failing file.

## Public Interface
Run all via `npm test` / `node tests/run-all.js`, or a single file directly:
`node tests/docs/<file>.test.js`.

## Dependencies
Node built-in assertions; mocks for filesystem/SDK/network where needed.

## Dependents
CI gate and the `c8` coverage check (80% floor on `scripts/**`).

## Conventions
- Mock external effects; keep tests deterministic and fast.
- Add a regression test before fixing a bug in docs/* and manifests.
- Name files `<subject>.test.js`.

## Gotchas
- These run inside `npm test` after the CI validators; a validator failure aborts before
  these tests run.
- Tests asserting catalog/registry/docs consistency fail if content was added without
  regenerating (`catalog:sync`, `command-registry:write`).

## Testing
This directory contains tests for docs/* and manifests. No production logic lives here.
