# CLAUDE.md — src/llm/prompt/

## Purpose
Prompt assembly: build structured prompts/messages from reusable templates so call sites do
not hand-concatenate strings.

## Key Files
| File | Role |
|---|---|
| `builder.py` | Prompt/message builder logic |
| `templates/__init__.py` | Template definitions package |
| `__init__.py` | Package surface |

## Internal Architecture
The builder composes system/user/assistant `Message` objects from named templates and
parameters, producing inputs ready to wrap in `LLMInput`.

## Public Interface
Builder functions/classes from `builder.py` (imported via `llm.prompt`). Templates are
registered under `templates/`.

## Dependencies
`core/types` (`Message`, `Role`). Standard library otherwise.

## Dependents
LLM callers constructing multi-part prompts; `tests/test_builder.py`.

## Conventions
- Templates are data; the builder is the only logic. Keep template text free of secrets.
- Produce `Message` objects (frozen) rather than raw dicts so downstream stays typed.

## Gotchas
- Templates must round-trip through `Message.to_dict()` cleanly; avoid unsupported fields.
- No I/O or network here — keep it pure so it is trivially testable.

## Testing
`tests/test_templates.py`, `tests/test_builder.py` cover template rendering and assembly.
This directory holds no stateful runtime behavior — it is pure string/Message composition.
