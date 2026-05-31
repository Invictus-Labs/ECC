# Examples

Copy-paste-ready, self-contained examples for ECC's executable surfaces. The `.py` examples
target the Python LLM abstraction in `src/llm/`; the `.sh` examples drive the Node operator
CLI in `scripts/`.

Run Python examples from the repo root after `pip install -e ".[dev]"` so `llm` is importable.

| File | What it shows |
|---|---|
| [`llm_basic_generate.py`](llm_basic_generate.py) | Minimal single-shot generation via `get_provider()` |
| [`llm_provider_resolution.py`](llm_provider_resolution.py) | How the resolver picks a provider (arg / env / `.llm.env` / default) |
| [`llm_tool_calling.py`](llm_tool_calling.py) | Register a tool, run it via `ToolRegistry` + `ToolExecutor` |
| [`llm_multi_provider.py`](llm_multi_provider.py) | Same prompt across Claude + OpenAI + Ollama |
| [`llm_custom_provider.py`](llm_custom_provider.py) | Implement and register a custom `LLMProvider` |
| [`cli_install_plan.sh`](cli_install_plan.sh) | Inspect/plan an install and read state with the operator CLI |
| [`cli_doctor_repair.sh`](cli_doctor_repair.sh) | Detect and repair drift in installed content |

> Existing templates retained: `product-capability-template.md`, `project-guidelines-template.md`.
