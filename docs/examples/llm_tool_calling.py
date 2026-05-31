#!/usr/bin/env python3
"""Register a local tool and execute LLM-requested tool calls.

Shows ToolDefinition + ToolRegistry + ToolExecutor from src/llm/tools/executor.py.
The executor never raises on a bad tool call; it returns a ToolResult with is_error=True.

Run from repo root: python docs/examples/llm_tool_calling.py
"""

from __future__ import annotations

from llm import ToolDefinition, ToolExecutor, ToolRegistry
from llm.core.types import ToolCall


def add_numbers(a: float, b: float) -> float:
    return a + b


def main() -> int:
    registry = ToolRegistry()
    registry.register(
        ToolDefinition(
            name="add_numbers",
            description="Add two numbers and return the sum.",
            parameters={
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
                "required": ["a", "b"],
            },
        ),
        add_numbers,
    )

    executor = ToolExecutor(registry)

    # A well-formed tool call (as an LLM would emit it).
    good = ToolCall(id="call_1", name="add_numbers", arguments={"a": 2, "b": 40})
    result = executor.execute(good)
    print(f"add_numbers(2, 40) -> {result.content} (is_error={result.is_error})")

    # An unknown tool: returns an error result instead of raising.
    bad = ToolCall(id="call_2", name="nonexistent", arguments={})
    err = executor.execute(bad)
    print(f"unknown tool -> {err.content!r} (is_error={err.is_error})")

    # Inspect what tools are registered (this is what you'd pass to LLMInput.tools).
    print("registered tools:", [t.name for t in registry.list_tools()])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
