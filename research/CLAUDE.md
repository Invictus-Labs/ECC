# CLAUDE.md — research/

## Purpose
Internal research/analysis notes that inform ECC's direction. Currently a codebase analysis
of the `ecc2/` control plane.

## Key Files
| File | Role |
|---|---|
| `ecc2-codebase-analysis.md` | Analysis of the ecc2 (Rust control plane) codebase |

## Internal Architecture
Plain Markdown research documents. No code, no runtime role.

## Public Interface
None — reference material for maintainers/contributors.

## Dependencies
None.

## Dependents
Architecture/roadmap discussions; informs `ecc2/` and `docs/architecture/`.

## Conventions
- Date and scope research docs; mark conclusions vs open questions.
- Keep research separate from normative docs (`docs/`).

## Gotchas
- Research may describe aspirational or past states — do not treat as current spec.

## Testing
Not test-bearing; consistency is covered by docs-surface tests where referenced
(e.g. `tests/docs/ecc2-release-surface.test.js`).
