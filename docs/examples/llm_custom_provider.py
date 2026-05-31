#!/usr/bin/env python3
"""Implement and register a custom LLMProvider.

Subclass the LLMProvider ABC (src/llm/core/interface.py), then register it with the
resolver so get_provider() can return it. This is how you add a new backend without
editing existing provider code (see ADR-004).

Run from repo root: python docs/examples/llm_custom_provider.py
"""

from __future__ import annotations

from llm import LLMInput, LLMOutput, Message
from llm.core.interface import LLMProvider
from llm.core.types import ModelInfo, ProviderType, Role
from llm.providers.resolver import register_provider


class EchoProvider(LLMProvider):
    """A trivial provider that echoes the last user message. Useful for offline tests."""

    provider_type = ProviderType.OLLAMA  # reuse an existing enum value for the demo

    def generate(self, input: LLMInput) -> LLMOutput:
        last_user = next(
            (m.content for m in reversed(input.messages) if m.role == Role.USER),
            "",
        )
        return LLMOutput(content=f"echo: {last_user}", model="echo-1", stop_reason="stop")

    def list_models(self) -> list[ModelInfo]:
        return [ModelInfo(name="echo-1", provider=self.provider_type)]

    def validate_config(self) -> bool:
        return True

    def get_default_model(self) -> str:
        return "echo-1"


def main() -> int:
    register_provider(ProviderType.OLLAMA, EchoProvider)

    from llm import get_provider

    provider = get_provider(ProviderType.OLLAMA)
    out = provider.generate(
        LLMInput(messages=[Message(role=Role.USER, content="hello world")])
    )
    print(out.content)            # -> echo: hello world
    print("models:", [m.name for m in provider.list_models()])
    print("config valid:", provider.validate_config())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
