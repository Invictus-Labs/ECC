# CLAUDE.md — schemas/

## Purpose
JSON Schemas that validate the repo's data files — install manifests, hook configs,
install-state, provenance, package-manager config, and plugin manifests. These make the
manifest/data layer fail-closed (ADR-002, ADR-006).

## Key Files
| File | Validates |
|---|---|
| `install-profiles.schema.json` / `install-modules.schema.json` / `install-components.schema.json` | `manifests/*` |
| `ecc-install-config.schema.json` | Install config |
| `hooks.schema.json` | `hooks/*.json` |
| `install-state.schema.json` / `provenance.schema.json` | State store records |
| `state-store.schema.json` | State store shape |
| `package-manager.schema.json` | Package-manager config |
| `plugin.schema.json` | Plugin manifest |

## Internal Architecture
Standard JSON Schema documents. Validated at runtime with `ajv` by the installer and by CI
validators.

## Public Interface
Consumed by `scripts/ci/validate-install-manifests.js`, install runtime, and `.mcp.json`/
config tooling.

## Dependencies
`ajv` (consumer). Schemas themselves are data.

## Dependents
`manifests/`, `hooks/`, `scripts/lib/install*`, `scripts/lib/state-store/`.

## Conventions
- Tighten schemas (additionalProperties false where safe) so bad data fails early.
- Version schema changes alongside the data + migrations they govern.

## Gotchas
- A schema change can retroactively invalidate existing manifests — update both together.
- State-store schema changes also need a `state-store/migrations.js` migration.

## Testing
`scripts/ci/validate-install-manifests.js`; `tests/ci/validators.test.js`,
`tests/lib/install-manifests.test.js`.
