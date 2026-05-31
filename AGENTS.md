# Everything Claude Code (ECC) — Agent Instructions

This is a **production-ready AI coding plugin** providing 63 specialized agents, 249 skills, 79 commands, and automated hook workflows for software development.

**Version:** 2.0.0-rc.1

## Core Principles

1. **Agent-First** — Delegate to specialized agents for domain tasks
2. **Test-Driven** — Write tests before implementation, 80%+ coverage required
3. **Security-First** — Never compromise on security; validate all inputs
4. **Immutability** — Always create new objects, never mutate existing ones
5. **Plan Before Execute** — Plan complex features before writing code

## Available Agents

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| planner | Implementation planning | Complex features, refactoring |
| architect | System design and scalability | Architectural decisions |
| tdd-guide | Test-driven development | New features, bug fixes |
| code-reviewer | Code quality and maintainability | After writing/modifying code |
| security-reviewer | Vulnerability detection | Before commits, sensitive code |
| build-error-resolver | Fix build/type errors | When build fails |
| e2e-runner | End-to-end Playwright testing | Critical user flows |
| refactor-cleaner | Dead code cleanup | Code maintenance |
| doc-updater | Documentation and codemaps | Updating docs |
| cpp-reviewer | C/C++ code review | C and C++ projects |
| cpp-build-resolver | C/C++ build errors | C and C++ build failures |
| fsharp-reviewer | F# functional code review | F# projects |
| docs-lookup | Documentation lookup via Context7 | API/docs questions |
| go-reviewer | Go code review | Go projects |
| go-build-resolver | Go build errors | Go build failures |
| kotlin-reviewer | Kotlin code review | Kotlin/Android/KMP projects |
| kotlin-build-resolver | Kotlin/Gradle build errors | Kotlin build failures |
| database-reviewer | PostgreSQL/Supabase specialist | Schema design, query optimization |
| python-reviewer | Python code review | Python projects |
| django-reviewer | Django code review | Django apps, DRF APIs, ORM, migrations |
| django-build-resolver | Django build, migration, and setup errors | Django startup, dependency, migration, collectstatic failures |
| java-reviewer | Java and Spring Boot code review | Java/Spring Boot projects |
| java-build-resolver | Java/Maven/Gradle build errors | Java build failures |
| loop-operator | Autonomous loop execution | Run loops safely, monitor stalls, intervene |
| harness-optimizer | Harness config tuning | Reliability, cost, throughput |
| rust-reviewer | Rust code review | Rust projects |
| rust-build-resolver | Rust build errors | Rust build failures |
| pytorch-build-resolver | PyTorch runtime/CUDA/training errors | PyTorch build/training failures |
| mle-reviewer | Production ML pipeline review | ML pipelines, evals, serving, monitoring, rollback |
| typescript-reviewer | TypeScript/JavaScript code review | TypeScript/JavaScript projects |

## Agent Orchestration

Use agents proactively without user prompt:
- Complex feature requests → **planner**
- Code just written/modified → **code-reviewer**
- Bug fix or new feature → **tdd-guide**
- Architectural decision → **architect**
- Security-sensitive code → **security-reviewer**
- Autonomous loops / loop monitoring → **loop-operator**
- Harness config reliability and cost → **harness-optimizer**

Use parallel execution for independent operations — launch multiple agents simultaneously.

## Security Guidelines

**Before ANY commit:**
- No hardcoded secrets (API keys, passwords, tokens)
- All user inputs validated
- SQL injection prevention (parameterized queries)
- XSS prevention (sanitized HTML)
- CSRF protection enabled
- Authentication/authorization verified
- Rate limiting on all endpoints
- Error messages don't leak sensitive data

**Secret management:** NEVER hardcode secrets. Use environment variables or a secret manager. Validate required secrets at startup. Rotate any exposed secrets immediately.

**If security issue found:** STOP → use security-reviewer agent → fix CRITICAL issues → rotate exposed secrets → review codebase for similar issues.

## Coding Style

**Immutability (CRITICAL):** Always create new objects, never mutate. Return new copies with changes applied.

**File organization:** Many small files over few large ones. 200-400 lines typical, 800 max. Organize by feature/domain, not by type. High cohesion, low coupling.

**Error handling:** Handle errors at every level. Provide user-friendly messages in UI code. Log detailed context server-side. Never silently swallow errors.

**Input validation:** Validate all user input at system boundaries. Use schema-based validation. Fail fast with clear messages. Never trust external data.

**Code quality checklist:**
- Functions small (<50 lines), files focused (<800 lines)
- No deep nesting (>4 levels)
- Proper error handling, no hardcoded values
- Readable, well-named identifiers

## Testing Requirements

**Minimum coverage: 80%**

Test types (all required):
1. **Unit tests** — Individual functions, utilities, components
2. **Integration tests** — API endpoints, database operations
3. **E2E tests** — Critical user flows

**TDD workflow (mandatory):**
1. Write test first (RED) — test should FAIL
2. Write minimal implementation (GREEN) — test should PASS
3. Refactor (IMPROVE) — verify coverage 80%+

Troubleshoot failures: check test isolation → verify mocks → fix implementation (not tests, unless tests are wrong).

## Development Workflow

1. **Plan** — Use planner agent, identify dependencies and risks, break into phases
2. **TDD** — Use tdd-guide agent, write tests first, implement, refactor
3. **Review** — Use code-reviewer agent immediately, address CRITICAL/HIGH issues
4. **Capture knowledge in the right place**
   - Personal debugging notes, preferences, and temporary context → auto memory
   - Team/project knowledge (architecture decisions, API changes, runbooks) → the project's existing docs structure
   - If the current task already produces the relevant docs or code comments, do not duplicate the same information elsewhere
   - If there is no obvious project doc location, ask before creating a new top-level file
5. **Commit** — Conventional commits format, comprehensive PR summaries

## Workflow Surface Policy

- `skills/` is the canonical workflow surface.
- New workflow contributions should land in `skills/` first.
- `commands/` is a legacy slash-entry compatibility surface and should only be added or updated when a shim is still required for migration or cross-harness parity.

## Git Workflow

**Commit format:** `<type>: <description>` — Types: feat, fix, refactor, docs, test, chore, perf, ci

**PR workflow:** Analyze full commit history → draft comprehensive summary → include test plan → push with `-u` flag.

## Architecture Patterns

**API response format:** Consistent envelope with success indicator, data payload, error message, and pagination metadata.

**Repository pattern:** Encapsulate data access behind standard interface (findAll, findById, create, update, delete). Business logic depends on abstract interface, not storage mechanism.

**Skeleton projects:** Search for battle-tested templates, evaluate with parallel agents (security, extensibility, relevance), clone best match, iterate within proven structure.

## Performance

**Context management:** Avoid last 20% of context window for large refactoring and multi-file features. Lower-sensitivity tasks (single edits, docs, simple fixes) tolerate higher utilization.

**Build troubleshooting:** Use build-error-resolver agent → analyze errors → fix incrementally → verify after each fix.

## Project Structure

```
agents/          — 63 specialized subagents
skills/          — 249 workflow skills and domain knowledge
commands/        — 79 slash commands
hooks/           — Trigger-based automations
rules/           — Always-follow guidelines (common + per-language)
scripts/         — Cross-platform Node.js utilities
mcp-configs/     — 14 MCP server configurations
tests/           — Test suite
```

`commands/` remains in the repo for compatibility, but the long-term direction is skills-first.

## Success Metrics

- All tests pass with 80%+ coverage
- No security vulnerabilities
- Code is readable and maintainable
- Performance is acceptable
- User requirements are met

---

# Codebase Map for AI Agents

This section is the territory map for an agent working *on this repository's own code* (as
opposed to the agents shipped for end users above). See `docs/architecture.md` for the full
system model and `docs/decisions/` for ADRs.

## File-territory map

| Territory | Path | Nature |
|---|---|---|
| Harness content (data) | `skills/`, `agents/`, `commands/`, `rules/`, `contexts/`, `mcp-configs/` | Markdown/JSON, never executed by ECC; validated by CI |
| Install declarations | `manifests/` | Data; source of truth for what installs |
| Schemas | `schemas/` | JSON Schemas that gate the data layer |
| Installer / operator CLI | `scripts/`, `scripts/lib/` | Node.js code (the main executable surface) |
| Content validators | `scripts/ci/` | Node.js code — the CI gate |
| Hook handlers | `scripts/hooks/` (logic) + `hooks/` (JSON config) | Node.js code + config |
| Python LLM layer | `src/llm/` | Python code |
| Rust control plane | `ecc2/` | Rust code (alpha, isolated) |
| Operator dashboard | `ecc_dashboard.py` | Python code |
| Integrations | `integrations/` | Opt-in Python adapters (e.g. AURA) |
| Tests | `tests/` (+ `tests/test_*.py`) | JS + Python tests |

Every source directory has a `CLAUDE.md` with its own deep map.

## Safe-to-modify zones (normal PR review)

- Adding a skill/agent/command/rule (then `npm run catalog:sync` + `command-registry:write`).
- Adding a new harness adapter in `scripts/lib/install-targets/` + a registry entry.
- Adding an LLM provider in `src/llm/providers/` + `register_provider`.
- Adding tests anywhere; improving docs.
- `ecc2/` changes (alpha — isolated from the stable installer).

## Require-human-review zones

- **`schemas/` + `manifests/`** — changing a schema can invalidate existing data; change
  schema + data + any state-store migration together.
- **`scripts/lib/state-store/`** — install-state persistence; schema changes need migrations.
- **`hooks/hooks.json` + `scripts/hooks/`** — guardrails that gate user tool calls; the
  plugin-root bootstrap is deliberately verbose, do not "simplify" it.
- **`scripts/ci/`** — these validators are the security/quality gate; weakening them is a
  trust decision (especially `check-unicode-safety.js`, `scan-supply-chain-iocs.js`,
  `validate-no-personal-paths.js`).
- **`integrations/aura/`** — security boundary; fail-open vs fail-closed is a real decision
  (see `THREAT_MODEL.md`).
- **`mcp-configs/`** — never commit real credentials (placeholders only).
- **Release/CI workflows** (`.github/workflows/`, `release-approval-gate.js`).

## Testing strategy

- **Always run `npm test` before pushing** — it runs the content validators, catalog +
  command-registry consistency checks, then `tests/run-all.js`. A content lint failure
  surfaces here, not at runtime.
- Python: `pytest -q` (mock SDKs/network in provider tests).
- Rust: `cd ecc2 && cargo test`.
- Coverage floors: JS 80% on `scripts/**` (`npm run coverage`); Python `pytest-cov` on `src/llm`.
- Bug fixes ship a regression test first.

## Common-task playbook

- **Add a slash command:** create `commands/<name>.md` (with `description` frontmatter) →
  `npm run command-registry:write` → `npm test`.
- **Add a skill:** create `skills/<name>/SKILL.md` (When to Use / How It Works / Examples) →
  add to `package.json` `files` if it should ship → `npm run catalog:sync` → `npm test`.
- **Add a harness target:** add `scripts/lib/install-targets/<harness>.js` + register in
  `registry.js` → add a `tests/lib/*` test asserting path containment → `npm test`.
- **Add an LLM provider:** subclass `LLMProvider` in `src/llm/providers/` → `register_provider`
  in `resolver.py` → add `tests/test_*_provider.py` (mock the SDK) → `pytest`.
- **Fix a bug:** reproduce, add a failing test, fix minimally, re-run the relevant suite.
- **Add a test:** mirror the target's location under `tests/` (`tests/lib/`, `tests/ci/`,
  `tests/test_*.py`); keep it deterministic and mocked.

## Gotchas / footguns

- Content is data — there is no runtime to catch a malformed file; the validators are the
  only line of defense (ADR-006).
- Catalog/command-registry drift fails CI's `--check` even when your content is "fine".
- `src/llm/providers/__init__.py` imports every provider eagerly — all SDKs must be importable.
- The package is imported as `llm`, not `src.llm` (`PYTHONPATH=src` or `pip install -e .`).
- `ecc2/` is NOT in the npm `files` list — do not assume installer changes affect it or vice versa.
- The hook bootstrap one-liner resolves the plugin root across several install layouts; it
  looks redundant but each branch matters.
- Never introduce zero-width/homoglyph unicode or personal paths — both are CI-blocked.
