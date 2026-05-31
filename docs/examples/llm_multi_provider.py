#!/usr/bin/env python3
"""Send the same prompt to multiple providers behind one interface.

Each provider is constructed only if its dependency/key is available; failures are caught
per-provider so one missing key does not abort the whole run.

Run from repo root: python docs/examples/llm_multi_provider.py
"""

from __future__ import annotations

from llm import LLMInput, Message, get_provider
from llm.core.interface import LLMError
from llm.core.types import Role

PROMPT = LLMInput(
    messages=[Message(role=Role.USER, content="Reply with a single word: ready")],
    max_tokens=16,
    temperature=0.0,
)


def main() -> int:
    for name in ("claude", "openai", "ollama"):
        try:
            provider = get_provider(name)
        except (ValueError, Exception) as exc:  # provider construction may need a key/SDK
            print(f"[{name}] skipped: {exc}")
            continue

        try:
            out = provider.generate(PROMPT)
            print(f"[{name}] {out.content.strip()}")
        except LLMError as exc:
            print(f"[{name}] call failed: {exc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
