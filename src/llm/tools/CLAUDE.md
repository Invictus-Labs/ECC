# CLAUDE.md — src/llm/tools/

## Purpose
Tool registration and execution for LLM tool/function calling, plus a minimal ReAct agent
loop that ties generation and tool execution together.

## Key Files
| File | Role |
|---|---|
| `executor.py` | `ToolRegistry`, `ToolExecutor`, `ReActAgent` |
| `__init__.py` | Re-exports `ToolExecutor`, `ToolRegistry` |

## Internal Architecture
`ToolRegistry` maps a tool name to both its `ToolDefinition` (schema) and a Python callable.
`ToolExecutor.execute(ToolCall)` looks up the callable, invokes it with the call's
`arguments`, and wraps the result (or any exception) in a `ToolResult`. `ReActAgent.run`
loops: provider.generate → if tool calls, execute all → append results as `TOOL` messages →
repeat up to `max_iterations`.

## Public Interface
- `ToolRegistry.register(definition, func)`, `.get(name)`, `.list_tools()`, `.has(name)`
- `ToolExecutor.execute(tool_call) -> ToolResult`, `.execute_all(calls) -> list[ToolResult]`
- `ReActAgent(provider, executor, max_iterations=10).run(input) -> LLMOutput` (async)

## Dependencies
`core/` types and `ToolExecutionError`. Standard library only otherwise.

## Dependents
LLM callers that want tool use; `docs/examples/llm_tool_calling.py`.

## Conventions
- Tool callables receive keyword args expanded from `ToolCall.arguments`.
- The executor NEVER raises on a missing/failing tool — it returns `ToolResult(is_error=True)`.
- Tool result content is coerced to `str` if the callable returns non-string.

## Gotchas
- `ReActAgent.run` is `async`; the underlying `provider.generate` is sync — wrap accordingly.
- A registered tool whose signature does not match the schema's `arguments` will surface as
  an error result, not a validation failure at registration time.

## Testing
`tests/test_executor.py`, `tests/test_provider_tools.py`. ReAct tests use `pytest-asyncio`.
