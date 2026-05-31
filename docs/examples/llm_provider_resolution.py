#!/usr/bin/env python3
"""Demonstrate how ECC resolves which LLM provider to use.

Resolution order (see src/llm/providers/resolver.py):
  1. explicit argument to get_provider(...)
  2. LLM_PROVIDER environment variable
  3. LLM_PROVIDER key in a local .llm.env file
  4. default: "claude"

Run from repo root: python docs/examples/llm_provider_resolution.py
"""

from __future__ import annotations

import os

from llm import get_provider
from llm.core.types import ProviderType


def show(label: str) -> None:
    try:
        provider = get_provider()
        print(f"{label}: resolved -> {provider.provider_type.value}")
    except ValueError as exc:
        print(f"{label}: error -> {exc}")


def main() -> int:
    print("Valid provider types:", [p.value for p in ProviderType])

    # 1. Default (no arg, no env) -> claude
    os.environ.pop("LLM_PROVIDER", None)
    show("default")

    # 2. Explicit env var wins over default
    os.environ["LLM_PROVIDER"] = "openai"
    show("env=openai")

    # 3. Explicit argument wins over everything
    try:
        p = get_provider("ollama")
        print(f"explicit-arg: resolved -> {p.provider_type.value}")
    except ValueError as exc:
        print(f"explicit-arg: error -> {exc}")

    # 4. Unknown provider fails closed with the list of valid types
    os.environ["LLM_PROVIDER"] = "not-a-provider"
    show("env=not-a-provider")

    os.environ.pop("LLM_PROVIDER", None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
