# CLAUDE.md — tests/

## Purpose
The combined test suite for both code surfaces: JavaScript tests for the Node installer/CLI
and Python tests for the `src/llm/` package. The JS suite is the CI gate (`tests/run-all.js`
runs from `npm test`); the Python suite runs under `pytest`.

## Key Files
| File / Dir | Role |
|---|---|
| `run-all.js` | JS test runner aggregating all `*.test.js` |
| `ci/` | Tests for the CI validators + supply-chain/registry checks |
| `lib/` | Tests for `scripts/lib/*` (install runtime, targets, state store, cost) |
| `commands/` | Command frontmatter + specific command tests |
| `docs/` | Docs-surface tests (asserts docs/manifests stay in sync) |
| `hooks/` | Hook handler tests |
| `integration/` | Cross-module integration (e.g. hooks end-to-end) |
| `scripts/` | Top-level script tests |
| `test_*.py`, `conftest.py` | Python LLM-layer tests |

## Internal Architecture
JS tests are plain Node test files discovered by `run-all.js`. Python tests use `pytest`
(+ `pytest-asyncio`, `pytest-mock`); `conftest.py` provides fixtures. Coverage: `c8` for JS
(80% floor on `scripts/**`), `pytest-cov` for Python (`src/llm`).

## Public Interface
`node tests/run-all.js` (or `npm test`), `pytest`. Run a single JS test directly:
`node tests/lib/install-targets.test.js`.

## Dependencies
JS: Node built-in test patterns. Python: `pytest`, `pytest-asyncio`, `pytest-cov`,
`pytest-mock` (dev extras).

## Dependents
CI (`.github/workflows/ci.yml`, reusable test workflow) and the coverage gate.

## Conventions
- Bug fixes ship a regression test first.
- Mock external SDKs/network in Python provider tests — never hit live APIs.
- Keep tests fast and deterministic (they run on every PR).

## Gotchas
- `npm test` also runs the CI validators before `run-all.js`; a content lint failure looks
  like a "test" failure.
- Python tests need `src/` importable (`pip install -e ".[dev]"`).

## Testing
This IS the test directory. Run `npm test` and `pytest` together before pushing.
