# CLAUDE.md — src/

## Purpose
Root of the Python `llm-abstraction` package (`pyproject.toml` name `llm-abstraction`,
version `0.1.0`). It contains a single package, `src/llm/`, a provider-agnostic LLM layer
used by tooling/examples in this repo. Packaged via hatchling (`packages = ["src/llm"]`).

## Key Files
| Path | Role |
|---|---|
| `llm/__init__.py` | Public package surface; re-exports types, `get_provider`, tool classes |
| `llm/core/` | Interface ABC + dataclass types (the contract) |
| `llm/providers/` | Concrete providers + resolver/factory |
| `llm/tools/` | Tool registry, executor, ReAct loop |
| `llm/prompt/` | Prompt builder + templates |
| `llm/cli/` | Interactive provider selector (`llm-select` entrypoint) |

## Internal Architecture
`Message[] → LLMInput → get_provider() → LLMProvider.generate() → LLMOutput`. Types are
frozen dataclasses; providers translate the normalized request into provider-specific SDK
calls. `ToolDefinition` renders to both OpenAI and Anthropic tool schemas.

## Public Interface
- `get_provider(provider_type=None, **kwargs) -> LLMProvider`
- `LLMInput(messages, model=None, temperature=1.0, max_tokens=None, tools=None, ...)`
- `LLMOutput(content, tool_calls=None, model=None, usage=None, stop_reason=None)`
- `ToolRegistry`, `ToolExecutor`, `interactive_select`

## Dependencies
`anthropic>=0.25`, `openai>=1.30` (runtime); `pytest`, `ruff`, `mypy` (dev). Python `>=3.11`
(uses `from __future__ import annotations` + PEP 604 unions).

## Dependents
`docs/examples/llm_*.py`, repo tooling, and the `llm-select` console script. Not imported
by the Node installer or `ecc2/`.

## Conventions
- `from __future__ import annotations` at top of every module.
- Frozen dataclasses for all value types; `to_dict()` for serialization.
- Errors subclass `LLMError` (`AuthenticationError`, `RateLimitError`, …).

## Gotchas
- Importing `llm` pulls in `openai` (via `astraflow`) and `anthropic` at module load — both
  SDKs must be installed even if you only use one provider.
- The package is imported as `llm`, not `src.llm`; run with `PYTHONPATH=src` or `pip install -e .`.

## Testing
`pytest` (tests in `tests/test_*.py`). Coverage source is `src/llm` (`pyproject.toml`).
`asyncio_mode = auto` for the ReAct agent tests.
