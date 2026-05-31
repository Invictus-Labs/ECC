# CLAUDE.md — agents/

## Purpose
Specialized subagent definitions (63 files) for delegation — planner, code-reviewer,
architect, tdd-guide, build-error-resolver, etc. Each is Markdown with YAML frontmatter and a
prompt body; harnesses load them as named subagents.

## Key Files
| File (examples) | Role |
|---|---|
| `code-reviewer.md` | Proactive quality/security review agent |
| `architect.md`, `code-architect.md` | Architecture/design agents |
| `build-error-resolver.md` | Fixes build errors |
| `code-explorer.md`, `comment-analyzer.md`, `conversation-analyzer.md` | Analysis agents |
| `chief-of-staff.md` | Orchestration/coordination agent |

## Internal Architecture
Frontmatter: `name`, `description` (with "MUST BE USED"/"Proactively" cues that drive
auto-invocation), `tools` (allowed tool list), `model` (e.g. `sonnet`). Body begins with the
shared **Prompt Defense Baseline**, then the agent's role and process.

## Public Interface
Each file = one invokable subagent (by `name`). Installed into the harness's agents location
by the relevant target adapter.

## Dependencies
None at runtime (data). Validated by `scripts/ci/validate-agents.js`.

## Dependents
Harness agent runtime; `commands/` that spawn agents; `tests/ci/agent-*` tests.

## Conventions
- File naming: lowercase-with-hyphens matching `name`.
- Keep the Prompt Defense Baseline header intact.
- `tools` should be the minimal set the agent needs.

## Gotchas
- `description` wording drives proactive invocation — be precise; over-eager phrasing causes
  unwanted auto-spawns.
- Agent instruction-safety is CI-checked (`tests/ci/agent-instruction-safety.test.js`).

## Testing
`scripts/ci/validate-agents.js`, `tests/ci/agent-yaml-surface.test.js`,
`tests/ci/code-reviewer-false-positive-guard.test.js`.
