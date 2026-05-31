# CLAUDE.md — scripts/codemaps/

## Purpose
Generates "codemaps" — structured maps of a codebase used to give agents fast orientation.

## Key Files
| File | Role |
|---|---|
| `generate.ts` | Codemap generation (TypeScript) |

## Internal Architecture
`generate.ts` walks a target tree and emits a structured map (modules, exports, relationships)
consumable by agents/tooling.

## Public Interface
Run via the TypeScript toolchain (`tsx`/`ts-node`) or a compiled build. Output is a codemap
artifact.

## Dependencies
Node + TypeScript (`typescript` devDependency).

## Dependents
Agent orientation tooling; optional/auxiliary to the main installer.

## Conventions
- TypeScript here (most of `scripts/` is CommonJS JS) — keep types explicit.
- Output should be deterministic for diff-ability.

## Gotchas
- This is one of the few `.ts` files in `scripts/`; ensure the TS toolchain is available
  before running.

## Testing
Covered by the broader test suite where wired; logic-only generator (no runtime service).
