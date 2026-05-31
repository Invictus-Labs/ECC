# Runbook — ECC (everything-claude-code)

> On-call / operator reference. This repo is a content distribution + installer CLI, not a
> long-running service. "Operations" here means: installing content into harnesses, running
> the validation/CI gate, the optional `ecc2/` control plane, and the operator dashboard.

## Quick reference

| Action | Command |
|---|---|
| Install content into a harness | `npx ecc <profile>` (e.g. `npx ecc typescript`) |
| Plan an install (dry inspect) | `node scripts/install-plan.js` |
| List install profiles/components | `npm run catalog:check` / `node scripts/catalog.js --text` |
| Diagnose drifted/missing files | `node scripts/doctor.js` |
| Repair drifted/missing files | `node scripts/repair.js` |
| Show install state | `node scripts/status.js` / `node scripts/list-installed.js` |
| Uninstall | `node scripts/uninstall.js` |
| Full validation gate (CI parity) | `npm test` |
| Lint | `npm run lint` |
| Python LLM tests | `pytest` (from repo root, with `src/` on path) |
| Operator readiness dashboard | `npm run dashboard` (runs `python3 ecc_dashboard.py`) |
| Rust control plane | `cd ecc2 && cargo run` |

## Start / stop / restart

There is no daemon for the core repo. The only long-running process is the **`ecc2/`
session daemon**:

```bash
# Start the control-plane TUI (foreground)
cd ecc2 && cargo run

# Build a release binary
cd ecc2 && cargo build --release   # -> ecc2/target/release/ecc-tui

# Session daemon lifecycle is managed inside the TUI (start / stop / resume sessions).
```

The operator dashboard is a foreground TUI: `npm run dashboard` (Ctrl-C to exit).

## Health checks

```bash
# 1. Content + manifests are valid (this is the real health gate):
npm test

# 2. Install state is consistent on this machine:
node scripts/doctor.js          # exits non-zero / reports drift if managed files are missing

# 3. Python LLM layer imports and passes:
pytest -q

# 4. ecc2 builds and its tests pass:
cd ecc2 && cargo test
```

A "healthy" repo: `npm test` green, `eslint`/`markdownlint` clean, `cargo test` green,
`pytest` green, and `node scripts/doctor.js` reports no drift on installed targets.

## Common failure modes

| Symptom | Likely cause | Fix |
|---|---|---|
| `npm test` fails in `validate-skills.js` / `validate-agents.js` | A skill/agent/command/rule file has malformed frontmatter or violates a content rule | Read the validator's error (it names file + reason); fix the frontmatter/section. Re-run the single validator, e.g. `node scripts/ci/validate-skills.js`. |
| `npm test` fails in `check-unicode-safety.js` | Invisible/zero-width/homoglyph chars in a `.md` (prompt-injection guard) | Remove the offending unicode; the error prints file + offset. |
| `npm test` fails in `validate-no-personal-paths.js` | A hardcoded personal home path leaked into committed content | Replace it with a relative or placeholder path. |
| `catalog:check` / `command-registry:check` fails | Catalog or command registry is stale after adding content | Regenerate: `npm run catalog:sync` and `npm run command-registry:write`, then commit. |
| Install does nothing for a harness | Target harness dir not detected, or component not in that profile | `node scripts/install-plan.js` to inspect the resolved plan; confirm the harness adapter in `scripts/lib/install-targets/`. |
| `doctor` reports drift after manual edits | Managed files were edited outside ECC | `node scripts/repair.js` to restore, or re-run install. |
| Schema validation error during install | A manifest violates its JSON Schema | Validate the manifest against `schemas/install-*.schema.json`; fix the offending field. |
| `pytest` import errors | `src/` not on `PYTHONPATH` | Run from repo root; install dev extras: `pip install -e ".[dev]"`. |
| Provider auth error in LLM layer | Missing/invalid API key | Set the provider key (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`) or `.llm.env`; see `.env.example`. |
| `cargo` build fails on OpenSSL | System OpenSSL mismatch | `ecc2` defaults to `vendored-openssl`; ensure a C toolchain is installed. |

## Log locations

- **Installer:** writes to stdout/stderr; install-state persists in the SQLite store under
  the harness's ECC state dir (inspect via `node scripts/status.js`).
- **`ecc2/`:** uses `tracing` / `tracing-subscriber` with `env-filter`; set verbosity with
  `RUST_LOG=ecc_tui=debug cargo run`. Session output is captured by `session/output.rs`.
- **CI:** GitHub Actions logs under `.github/workflows/ci.yml` runs (and the reusable
  workflows). The release/maintenance/supply-chain workflows log under their own jobs.

## Escalation

1. **Content/validation break:** the failing CI validator names the file and rule. Fix the
   content; this is self-service — no escalation needed.
2. **Installer regression (`scripts/`):** reproduce with `node scripts/install-plan.js`;
   check the relevant `install-targets/*.js` adapter and `scripts/lib/install/` runtime.
3. **Supply-chain alert:** `npm run security:ioc-scan` + `npm run security:advisory-sources`;
   see `SECURITY.md` and `the-security-guide.md`.
4. **Release gate:** `npm run release:approval-gate` is the canonical gate; evidence syncs
   live under `docs/releases/`.
5. **Upstream:** this is a fork of `affaan-m/ECC`. For upstream bugs, cross-reference the
   upstream issue tracker; for local (Invictus-Labs) changes, open a PR on this fork.
