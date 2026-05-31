# CLAUDE.md — config/

## Purpose
Static configuration data used by the installer/tooling. Currently the project→stack
mappings that let `consult.js` recommend components from a project description.

## Key Files
| File | Role |
|---|---|
| `project-stack-mappings.json` | Maps project/tech signals → recommended ECC components/profiles |

## Internal Architecture
Plain JSON consumed at runtime by recommendation/consult logic. No code here.

## Public Interface
Read by `scripts/consult.js` and related recommendation tooling.

## Dependencies
None (data). May be validated against a schema in `schemas/`.

## Dependents
`scripts/consult.js`; install profile recommendation.

## Conventions
- Keep mappings declarative and additive.
- Validate JSON shape before relying on new keys.

## Gotchas
- Stale mappings produce poor recommendations but never break installs.
- Keep component IDs here consistent with `manifests/` and the catalog.

## Testing
Exercised via consult/catalog tests; pure data directory.
