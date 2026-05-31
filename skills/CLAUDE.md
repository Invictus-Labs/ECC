# CLAUDE.md — skills/

## Purpose
The skill library — by far the largest content area (200+ skill directories). Skills encode
workflows and domain knowledge (coding standards, language patterns, testing, security,
research, content, ops). Curated skills live here; generated/imported skills go under
`~/.claude/skills/` (see `docs/SKILL-PLACEMENT-POLICY.md`).

## Key Files
Each subdirectory is one skill, conventionally containing a `SKILL.md` (and optional
`references/`, `scripts/`, `tests/`, `fixtures/`). Examples: `tdd-workflow/`,
`security-review/`, `python-patterns/`, `react-patterns/`, `deep-research/`,
`content-engine/`, `skill-comply/` (which itself has `scripts/`, `tests/`, `fixtures/`).

## Internal Architecture
A skill is Markdown with clear sections: When to Use, How It Works, Examples. Some skills
bundle helper scripts or reference docs. Skills are validated, indexed into the catalog, and
installed per-harness; their evolution/health is tracked by `scripts/lib/skill-evolution/`.

## Public Interface
One skill per directory, referenced by directory name. The `package.json` `files` list
enumerates which skills ship in the npm package.

## Dependencies
Data only. Validated by `scripts/ci/validate-skills.js`; catalogued by `scripts/catalog.js`.

## Dependents
`agents/` and `commands/` reference skills; the installer ships them; skill-health/evolution
tooling reasons about them.

## Conventions
- lowercase-with-hyphens directory names.
- Include the standard sections; keep examples runnable/realistic.
- After adding a skill, run `npm run catalog:sync`.

## Gotchas
- This directory is huge — navigate by name/catalog, not by listing.
- Not every skill dir is in the npm `files` list; shipping requires adding it there.
- `skill-comply/` and a few others contain executable `scripts/`+`tests/` — those are real code.

## Testing
`scripts/ci/validate-skills.js`, `npm run catalog:check`, plus per-skill tests where present
(e.g. `skills/skill-comply/tests/`). Coverage tracked via `tests/ci/mle-workflow-coverage.test.js`.
