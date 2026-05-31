# CLAUDE.md — manifests/

## Purpose
The declarative source of truth for *what* the installer installs: the profile→module→
component hierarchy. Editing these (not the installer code) changes install behavior
(ADR-002).

## Key Files
| File | Role |
|---|---|
| `install-profiles.json` | Named install profiles (e.g. a language stack) |
| `install-modules.json` | Modules grouping related components |
| `install-components.json` | Individual installable components (skills/agents/rules/etc.) |

## Internal Architecture
A profile references modules; a module references components; a component points at concrete
content (a skill dir, agent file, rule set, …). Resolved by `scripts/lib/install-manifests.js`
and validated against `schemas/install-*.schema.json` via `ajv`.

## Public Interface
Read by `install-plan.js`/`install-apply.js`, `catalog.js`, and `consult.js`.

## Dependencies
Validated by `schemas/`. Components must point at real content paths.

## Dependents
The entire install pipeline; the catalog and command registry.

## Conventions
- Keep IDs stable and consistent with the catalog and `config/project-stack-mappings.json`.
- After editing, run `npm run catalog:sync` and `npm test`.

## Gotchas
- A manifest that violates its schema blocks installs (fail-closed) — intentional.
- Referencing a component path that doesn't exist breaks the install for that profile.

## Testing
`scripts/ci/validate-install-manifests.js`, `tests/lib/install-manifests.test.js`,
`tests/docs/install-identifiers.test.js`.
