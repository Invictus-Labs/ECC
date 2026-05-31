# ADR-006: CI validation, not runtime, is the content gate

## Status
Accepted

## Context
Because content is data and never executed by ECC (ADR-001), there is no runtime that would
catch a malformed skill, an agent with bad frontmatter, a hardcoded personal path, or a
prompt-injection unicode payload. Yet correctness of this content is exactly what users
depend on. We also distribute to LLM harnesses, so adversarial/invisible-unicode content is
a real supply-chain risk.

## Decision
Make `npm test` a comprehensive **validation gate** that must pass before merge. It runs:
`check-unicode-safety.js`, `validate-agents.js`, `validate-commands.js`, `validate-rules.js`,
`validate-skills.js`, `validate-hooks.js`, `validate-install-manifests.js`,
`validate-no-personal-paths.js`, catalog + command-registry consistency checks, and the JS
test suite (`tests/run-all.js`). A dedicated supply-chain IOC scanner
(`scripts/ci/scan-supply-chain-iocs.js`) and advisory-source check run in CI as well.

## Consequences
- Malformed content fails loudly at PR time with file + reason, never silently at use time.
- Catalog and command registry must be regenerated (`catalog:sync`, `command-registry:write`)
  when content changes, or CI fails the consistency check.
- The validators are themselves code with their own tests under `tests/ci/`.
- Coverage thresholds (80% lines/functions/branches via `c8`) guard the installer logic.
