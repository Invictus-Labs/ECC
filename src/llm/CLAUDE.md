# CLAUDE.md — src/llm/

## Purpose
The provider-agnostic LLM abstraction. One normalized request/response contract over
Anthropic, OpenAI, Ollama, and Astraflow backends, with tool-calling and prompt-building
support. See ADR-004 for the design rationale.

## Key Files
| File | Role |
|---|---|
| `__init__.py` | Public exports + `gui()` launcher |
| `__main__.py` | `python -m llm` entrypoint |
| `core/interface.py` | `LLMProvider` ABC + error hierarchy |
| `core/types.py` | `Message`, `LLMInput`, `LLMOutput`, `ToolDefinition`, `ToolCall`, `ToolResult`, `ModelInfo`, enums |
| `providers/resolver.py` | `get_provider()` factory + `register_provider()` |
| `providers/{claude,openai,ollama,astraflow}.py` | Concrete adapters |
| `tools/executor.py` | `ToolRegistry`, `ToolExecutor`, `ReActAgent` |
| `prompt/builder.py` | Prompt assembly from templates |
| `cli/selector.py` | Interactive provider/model selector |

## Internal Architecture
`core/` defines the contract; everything else depends inward on it. `providers/resolver.py`
holds a `ProviderType -> class` map and resolves the active provider from arg → `LLM_PROVIDER`
env → `.llm.env` file → default `claude`. Providers convert `LLMInput` to their SDK shape and
back to `LLMOutput`. `tools/` executes tool calls returned by a provider; `ReActAgent` loops
generate→execute→feed-back up to `max_iterations`.

## Public Interface
- `get_provider(provider_type: ProviderType|str|None = None, **kwargs) -> LLMProvider`
- `register_provider(provider_type, provider_cls)` — add a backend without editing core.
- `LLMProvider.generate(input) -> LLMOutput`, `.list_models()`, `.validate_config()`,
  `.supports_tools()`, `.supports_vision()`, `.get_default_model()`.
- `ToolDefinition.to_openai_tool()` / `.to_anthropic_tool()`.

## Dependencies
`anthropic`, `openai` SDKs. `astraflow` reuses the OpenAI SDK against a custom `base_url`.

## Dependents
`docs/examples/llm_*.py`, the `llm-select` CLI, repo tooling.

## Conventions
- New provider = subclass `LLMProvider`, set `provider_type`, register in resolver map.
- Raise typed `LLMError` subclasses, never bare exceptions, from providers.
- Keep value types frozen and `to_dict()`-serializable.

## Gotchas
- `providers/__init__.py` imports all providers eagerly → all SDKs must be importable.
- `_resolve_provider_type` lowercases and strips quotes; `.llm.env` values may be quoted.
- Default model strings (e.g. `claude-sonnet-4-7`) are hardcoded per provider — update when
  model names change.

## Testing
`tests/test_resolver.py`, `test_types.py`, `test_executor.py`, `test_builder.py`,
`test_claude_provider.py`, `test_astraflow_provider.py`, `test_provider_tools.py`.
