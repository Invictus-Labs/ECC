# ADR-004: Provider-agnostic LLM interface with resolver

## Status
Accepted

## Context
Tooling and examples in this repo need to call LLMs across providers (Anthropic, OpenAI,
Ollama, Astraflow) without scattering provider-specific request shapes throughout call
sites, and without forcing a hard choice of provider at import time.

## Decision
Define an abstract `LLMProvider` interface (`src/llm/core/interface.py`) with normalized
`LLMInput`/`LLMOutput`/`Message`/`ToolDefinition` dataclasses (`src/llm/core/types.py`).
Concrete providers live in `src/llm/providers/`. A `get_provider()` factory
(`providers/resolver.py`) resolves the provider in priority order: explicit arg →
`LLM_PROVIDER` env var → `.llm.env` file → default `claude`. `ToolDefinition` knows how to
render itself to both OpenAI (`to_openai_tool`) and Anthropic (`to_anthropic_tool`) shapes.

## Consequences
- Call sites depend only on the interface; switching providers is a config change.
- New providers register via `register_provider()` without editing existing code.
- Tool-call schemas are translated centrally, so a tool is defined once.
- The layer is alpha (`0.1.0`); the `astraflow` provider targets a specific gateway.
