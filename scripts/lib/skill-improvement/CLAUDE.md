# CLAUDE.md — scripts/lib/skill-improvement/

## Purpose
Evaluates skills and proposes/apply improvements ("amendify"), driven by observations from
real sessions. Complements skill-evolution (which tracks) by acting on the data.

## Key Files
| File | Role |
|---|---|
| `observations.js` | Collects observations about skill usage |
| `evaluate.js` | Scores/evaluates a skill against observations |
| `amendify.js` | Proposes/applies skill amendments |
| `health.js` | Improvement-oriented health metrics |

## Internal Architecture
`observations.js` gathers signals → `evaluate.js` scores → `amendify.js` proposes concrete
edits. `health.js` summarizes improvement status.

## Public Interface
Functions consumed by skill tooling and continuous-learning commands.

## Dependencies
`../skill-evolution/`, `../state-store/`, Node stdlib.

## Dependents
Continuous-learning skills/commands, `scripts/skills-health.js`.

## Conventions
- Improvements are proposals first; applying edits should be explicit and reviewable.
- Keep amendments minimal and attributed.

## Gotchas
- Auto-amendment can drift a skill from its author's intent — prefer human review on apply.
- Evaluation depends on having enough observations; small samples are noisy.

## Testing
`tests/lib/*` and `tests/ci/*` skill surface tests. Logic-only module.
