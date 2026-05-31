# Onboarding — ECC (everything-claude-code)

Welcome. This guide gets a new contributor productive on the `ecc-universal` repo. Read it
top to bottom once, then keep `docs/architecture.md` and `AGENTS.md` open while you work.

## Prerequisites

- **Node.js >= 18** (CI/dev pin: `nodejs 20.19.0` in `.tool-versions`). The package manager
  is **yarn 4** (`packageManager` field), but `npm`/`pnpm`/`bun` all work for scripts.
- **Python >= 3.11** (pin: `python 3.12.8`) — for `src/llm/`, `ecc_dashboard.py`, AURA.
- **Rust (stable)** — only if you touch `ecc2/`.
- **git**, a POSIX shell (or PowerShell on Windows — `install.ps1` is supported).
- Optional: `asdf` or `mise` — `asdf install` reads `.tool-versions`.

## Local setup (numbered)

1. Clone and enter the repo:
   ```bash
   git clone https://github.com/Invictus-Labs/everything-claude-code.git
   cd everything-claude-code
   ```
2. Install Node deps:
   ```bash
   npm install         # or: yarn install
   ```
3. (If working on the LLM layer) install Python dev deps:
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -e ".[dev]"
   ```
4. Run the full validation gate (this is what CI runs):
   ```bash
   npm test
   ```
5. Run the Python tests:
   ```bash
   pytest -q
   ```
6. (Optional) Build the Rust control plane:
   ```bash
   cd ecc2 && cargo test && cargo build
   ```
7. (Optional) Try an install into a scratch target to see the installer work:
   ```bash
   node scripts/install-plan.js     # inspect what would be installed
   ```

## The 3–5 mental models to internalize

1. **Content is data; the installer is the only "code path" most users hit.** Skills,
   agents, commands, rules, hooks are Markdown/JSON. They are validated, not executed.
2. **Profiles → modules → components.** What gets installed is declared in `manifests/`
   and validated by `schemas/`. Nothing is installed that isn't in a manifest.
3. **One adapter per harness.** `scripts/lib/install-targets/<harness>.js` knows that
   harness's on-disk layout. Supporting a new harness = adding one adapter, not editing core.
4. **Validation is the gate, not runtime.** A broken skill fails `npm test`, never silently
   at use time. Always run `npm test` before pushing.
5. **Four independent surfaces.** Node installer, Python LLM layer, Rust `ecc2/`, Python
   dashboard. They share the repo but not a process; change one without fearing the others.

## Team conventions

- **Branching:** never commit to `main`. Feature branch → PR. Conventional commits are
  enforced (`commitlint.config.js`); commit titles like `feat(skills): …`, `fix(hooks): …`.
- **File naming:** lowercase-with-hyphens (`python-reviewer.md`, `tdd-workflow.md`).
- **Agent files:** Markdown + YAML frontmatter (`name`, `description`, `tools`, `model`).
- **Skill files:** Markdown with clear sections (When to Use, How It Works, Examples).
- **No personal paths, no invisible unicode** — both are CI-enforced.
- **Prompt Defense Baseline** header appears on agent/CLAUDE files — keep it.
- After adding content: run `npm run catalog:sync` and `npm run command-registry:write`.

## Directory map (where things live)

| Path | What |
|---|---|
| `skills/` | The skill library (200+ skills), one dir each |
| `agents/` | Subagent definitions (Markdown + frontmatter) |
| `commands/` | Slash-command definitions |
| `rules/` | Per-language/always-follow rule sets |
| `contexts/` | Reusable context presets (dev/research/review) |
| `hooks/` | Hook configs (`hooks.json`) + memory-persistence hooks |
| `mcp-configs/` | MCP server catalog (`mcp-servers.json`) |
| `manifests/` | Install profiles/modules/components (data) |
| `schemas/` | JSON Schemas validating manifests/configs |
| `scripts/` | Node installer + operator CLI + CI validators |
| `scripts/lib/` | Installer internals (adapters, state store, lifecycle) |
| `src/llm/` | Python provider-agnostic LLM abstraction |
| `ecc2/` | Rust alpha control plane (TUI + session daemon) |
| `ecc_dashboard.py` | Python operator-readiness TUI |
| `tests/` | JS + Python test suites |
| `docs/` | English + localized docs, architecture, releases |
| `examples/` | Reference prototypes (RAG evaluator, GAN harness) |

## Who/what to ask

- **Architecture & data flow:** `docs/architecture.md`.
- **Working as an AI agent in this repo:** `AGENTS.md` (root) and root `CLAUDE.md`.
- **Per-directory specifics:** the `CLAUDE.md` inside each source directory.
- **Security posture:** `SECURITY.md`, `the-security-guide.md`, `docs/security/`.
- **Contribution mechanics:** `CONTRIBUTING.md`.
- **Upstream project:** this is a fork of `affaan-m/ECC`; upstream README/discussions for
  product-level questions.
