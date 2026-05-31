# CLAUDE.md — src/llm/providers/

## Purpose
Concrete `LLMProvider` adapters and the resolver/factory that selects one at runtime. Each
adapter translates the normalized `LLMInput` into a provider SDK call and the response back
into `LLMOutput`.

## Key Files
| File | Role |
|---|---|
| `resolver.py` | `get_provider()` factory, `register_provider()`, `.llm.env` reading |
| `claude.py` | Anthropic adapter (`ClaudeProvider`) |
| `openai.py` | OpenAI adapter |
| `ollama.py` | Local Ollama adapter |
| `astraflow.py` | Astraflow / Astraflow-CN gateway (OpenAI-compatible base_url) |
| `constants.py` | Shared model/endpoint constants |
| `__init__.py` | Re-exports `get_provider`; imports all providers eagerly |

## Internal Architecture
`resolver.py` keeps `_PROVIDER_MAP: dict[ProviderType, type[LLMProvider]]`. Resolution order:
explicit arg → `LLM_PROVIDER` env → `LLM_PROVIDER` in `.llm.env` → default `"claude"`. String
provider names are coerced to `ProviderType`, failing closed with the valid list on a bad name.

## Public Interface
- `get_provider(provider_type=None, **kwargs) -> LLMProvider`
- `register_provider(provider_type, provider_cls) -> None`
- Each provider exposes `generate`, `list_models`, `validate_config`, `get_default_model`.

## Dependencies
`anthropic` (claude), `openai` (openai + astraflow). `core/` for the interface + types.

## Dependents
`resolver.get_provider` is the entrypoint for all callers; `__init__` re-exports it.

## Conventions
- Read API keys from constructor arg first, then env (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`).
- Map SDK exceptions to `core` error subclasses (auth/rate-limit/context-length).
- Hardcoded default model per provider; keep current with model releases.

## Gotchas
- `__init__.py` imports every provider → all SDKs must be installed to import the package.
- `astraflow` uses the OpenAI SDK against a custom `base_url`; a missing `openai` install
  breaks the whole `providers` import, not just astraflow.
- `_strip_env_value` strips matching surrounding quotes — `.llm.env` values may be quoted.

## Testing
`tests/test_resolver.py`, `tests/test_claude_provider.py`, `tests/test_astraflow_provider.py`,
`tests/test_provider_tools.py`. Tests mock SDK clients rather than hitting the network.
