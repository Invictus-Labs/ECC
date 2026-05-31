#!/usr/bin/env python3
"""Minimal single-shot LLM generation using ECC's provider-agnostic layer.

Run from the repo root after: pip install -e ".[dev]"
Requires ANTHROPIC_API_KEY (default provider is "claude") or set LLM_PROVIDER.
"""

from __future__ import annotations

import sys

from llm import LLMInput, Message, get_provider
from llm.core.interface import AuthenticationError, LLMError
from llm.core.types import Role


def main() -> int:
    # get_provider() resolves: explicit arg -> LLM_PROVIDER env -> .llm.env -> "claude".
    try:
        provider = get_provider()  # or get_provider("openai")
    except ValueError as exc:
        print(f"Provider resolution failed: {exc}", file=sys.stderr)
        return 2

    request = LLMInput(
        messages=[
            Message(role=Role.SYSTEM, content="You are a terse assistant."),
            Message(role=Role.USER, content="Name three primary colors."),
        ],
        max_tokens=128,
        temperature=0.2,
    )

    try:
        output = provider.generate(request)
    except AuthenticationError as exc:
        print(f"Auth error (set your API key): {exc}", file=sys.stderr)
        return 3
    except LLMError as exc:
        print(f"LLM call failed: {exc}", file=sys.stderr)
        return 1

    print(output.content)
    if output.usage:
        print(f"[usage] {output.usage}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
