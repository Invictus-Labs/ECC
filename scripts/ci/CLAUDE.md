# CLAUDE.md — scripts/ci/

## Purpose
The content-validation and supply-chain gate. These scripts are the real correctness check
for the (non-executed) Markdown/JSON content — they run in `npm test` and CI (ADR-006).

## Key Files
| File | Validates / does |
|---|---|
| `validate-skills.js` / `validate-agents.js` / `validate-commands.js` / `validate-rules.js` / `validate-hooks.js` | Frontmatter + structure of each content type |
| `validate-install-manifests.js` | Manifests conform to `schemas/install-*.schema.json` |
| `validate-no-personal-paths.js` | No leaked personal filesystem paths |
| `check-unicode-safety.js` | No invisible/zero-width/homoglyph chars (injection guard) |
| `catalog.js` | Generates/checks the component catalog |
| `generate-command-registry.js` | Generates/checks the command registry |
| `scan-supply-chain-iocs.js` / `supply-chain-advisory-sources.js` | Supply-chain IOC scan |
| `validate-workflow-security.js` | GitHub Actions workflow hardening |

## Internal Architecture
Each validator walks a content directory, parses frontmatter/JSON, and exits non-zero with a
file + reason on the first violation. `catalog.js`/`generate-command-registry.js` support
`--check` (fail on drift) and `--write` (regenerate) modes.

## Public Interface
Run individually (`node scripts/ci/validate-skills.js`) or via `npm test`. `--write`/`--check`
flags on the generators.

## Dependencies
`ajv` for schema validation; Node stdlib otherwise.

## Dependents
`npm test`, `.github/workflows/ci.yml` and the reusable validate/test workflows.

## Conventions
- Fail closed with actionable messages (name the file and the rule).
- Keep validators dependency-light and fast; they run on every PR.

## Gotchas
- Adding content without regenerating catalog/command-registry breaks `--check`.
- `check-unicode-safety.js` will reject seemingly-fine text containing zero-width chars —
  paste content as plain ASCII where possible.

## Testing
`tests/ci/*.test.js` (validators.test.js, catalog.test.js, no-personal-paths.test.js,
command-registry.test.js, agent-instruction-safety.test.js, etc.).
