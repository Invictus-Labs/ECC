# ADR-001: Content-as-data, installer-as-code

## Status
Accepted

## Context
ECC ships skills, agents, commands, rules, hooks, and MCP configs to many AI coding
harnesses (Claude Code, Codex, Cursor, OpenCode, Gemini, Zed, Qwen, …). These harnesses
each have their own on-disk conventions but all consume essentially declarative,
human-reviewable instruction content. We needed a representation that is portable,
diffable, reviewable in PRs, and that does not require executing arbitrary code to "use" a
skill or agent.

## Decision
Author all harness content as **Markdown (with YAML frontmatter) or JSON data**. The only
executable surfaces are: the Node installer/operator CLI (`scripts/`), the CI validators
(`scripts/ci/validate-*.js`), the Python LLM abstraction (`src/llm/`), the Rust control
plane (`ecc2/`), and the dashboard (`ecc_dashboard.py`). Content files are never executed
by ECC itself — they are validated, then copied/merged into a harness's layout.

## Consequences
- Content is reviewable and diffable; a skill change is a readable Markdown diff.
- A single source library can target 7+ harnesses without per-harness rewrites.
- Correctness must be enforced by validators (see ADR-006), since there is no runtime to
  catch a malformed file.
- The repo is content-heavy (2,000+ Markdown files); navigation relies on the catalog and
  per-directory CLAUDE.md files.
