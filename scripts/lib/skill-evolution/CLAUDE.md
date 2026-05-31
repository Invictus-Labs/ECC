# CLAUDE.md — scripts/lib/skill-evolution/

## Purpose
Tracks how skills evolve over time: health, versioning, and provenance, surfaced through a
dashboard. Supports the continuous-learning workflow that promotes session patterns into
durable skills.

## Key Files
| File | Role |
|---|---|
| `tracker.js` | Records skill change events |
| `versioning.js` | Skill version bookkeeping |
| `provenance.js` | Where a skill/observation came from |
| `health.js` | Skill health scoring |
| `dashboard.js` | Renders evolution status |
| `index.js` | Facade |

## Internal Architecture
`tracker.js` logs events; `versioning.js` + `provenance.js` attribute and version them;
`health.js` scores; `dashboard.js` aggregates for display. `index.js` is the entrypoint.

## Public Interface
Facade functions from `index.js` consumed by skill health/improvement tooling and
`scripts/skills-health.js`.

## Dependencies
`../state-store/` (persistence), Node stdlib.

## Dependents
`scripts/skills-health.js`, skill-improvement, continuous-learning skills.

## Conventions
- Attribute provenance for every tracked change (auditability).
- Version bumps follow the skill's declared versioning scheme.

## Gotchas
- Health scores are heuristic; treat as advisory, not a hard gate.
- Provenance must not record secrets or personal paths.

## Testing
`tests/lib/*` and skill-surface tests under `tests/ci/`. Logic-only module.
