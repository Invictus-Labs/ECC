# CLAUDE.md — src/llm/core/

## Purpose
The contract layer of the LLM abstraction: the provider interface and all normalized value
types. Everything else in `src/llm/` depends inward on this directory; `core/` depends on
nothing in the package.

## Key Files
| File | Role |
|---|---|
| `interface.py` | `LLMProvider` ABC; `LLMError` and subclasses |
| `types.py` | Frozen dataclasses + enums for messages, IO, tools, models |

## Internal Architecture
`interface.py` declares the abstract `generate()`, `list_models()`, `validate_config()`
methods plus capability defaults (`supports_tools`, `supports_vision`). `types.py` defines
`Role`/`ProviderType` enums and the frozen dataclasses (`Message`, `ToolDefinition`,
`ToolCall`, `ToolResult`, `LLMInput`, `LLMOutput`, `ModelInfo`), each with `to_dict()` and,
for tools, OpenAI/Anthropic renderers.

## Public Interface
- `LLMProvider` (ABC) — implement to add a backend.
- `LLMError(message, provider=None, code=None, details=None)` + `AuthenticationError`,
  `RateLimitError`, `ContextLengthError`, `ModelNotFoundError`, `ToolExecutionError`.
- `LLMInput.to_dict()`, `LLMOutput.has_tool_calls`, `ToolDefinition.to_anthropic_tool()`.

## Dependencies
Standard library only (`abc`, `dataclasses`, `enum`, `typing`). No third-party imports —
this keeps the contract installable/testable without provider SDKs.

## Dependents
`providers/*`, `tools/executor.py`, `prompt/builder.py`, `cli/selector.py`, and all tests.

## Conventions
- All value types are `@dataclass(frozen=True)` — treat as immutable.
- Unions use PEP 604 (`X | None`); module starts with `from __future__ import annotations`.
- `to_dict()` merges `metadata` last so callers can pass provider-specific extras.

## Gotchas
- `Message.tool_calls` and `ToolCall` reference each other; forward refs rely on the
  `__future__` annotations import.
- `LLMInput.to_dict()` does NOT emit `model` when it is `None` — providers must supply a
  default model themselves.

## Testing
`tests/test_types.py` exercises serialization and tool-schema rendering. No stateful
behavior here beyond pure value construction.
