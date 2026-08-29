# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`mabstruct_studio` is an experimental **multi-agent game studio** built on LangGraph: a pipeline that turns a single game title into a playable single-file HTML5 browser game.

```
PRODUCER --> IDEATION --> DESIGN --> DEVELOP <--> TEST --> DEPLOYMENT
```

Everything lives in two Jupyter notebooks — there is no package, module, or entrypoint. `mabstruct_studio` is a subdirectory of the larger `pingmab-agents` course repo (the parent `.venv`, `pyproject.toml`, and `.env` are shared).

- **`mabstruct_studio.ipynb`** — the maintained, cleaned-up notebook. Currently covers IDEATION → DESIGN → DEVELOP (single idea, no fan-out). The test phase was deliberately removed (commit `beb5eae8`); `game_tests` / `test_result` / `deployment_url` remain commented out in `GameStudioState`.
- **`mabstruct_experimenting.ipynb`** — the spike/scratch notebook. Keeps the code that was pulled out of the studio notebook: `Send`-based parallel fan-out (`fan_out_develop` → `develop_one`), the Tier-1 test node, and `run_static_validation_full`. Look here first when re-adding a feature; port from here rather than rewriting.

## Running

**Python environment:** the parent repo's venv, `/Users/mab/dev/agents/pingmab-agents/.venv` (Python 3.12.12, managed by `uv`). There is no venv inside `mabstruct_studio/`. Both notebooks are already pinned to it — kernelspec `python3`, display name `.venv` — and it is the only registered Jupyter kernel. If the kernel picker offers anything else (system Python, a Cursor-created env), it is the wrong one and imports like `langchain_anthropic` will fail.

```bash
cd /Users/mab/dev/agents/pingmab-agents   # parent repo owns the venv and pyproject.toml
uv sync                                    # install/refresh deps
.venv/bin/jupyter lab                      # or open the notebook in Cursor/VS Code
```

Run project code outside Jupyter with that same interpreter — `.venv/bin/python`, never bare `python3` (only stdlib-only one-liners like the one below are safe with the system Python). Add dependencies with `uv add <pkg>` from the parent repo, not `pip install`.

Read a notebook's code without launching Jupyter:

```bash
python3 -c "import json; nb=json.load(open('mabstruct_studio.ipynb')); print('\n'.join(''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code'))"
```

Notebooks no longer depend on the kernel's cwd: `NOTEBOOK_DIR` is resolved from the notebook file's own location (see *The develop phase* below), so `dev-output/` always lands next to the notebook.

There is no test suite and no linter. The only automated checks are the in-notebook validation tiers (below). `node` must be on PATH — Tier-0 shells out to `node --check`.

### API keys

`load_dotenv(override=True)` reads the parent repo's `.env`. Used: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `TAVILY_API_KEY` (web search), `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` (push notifications via the `send_push_notification` tool), and `LANGSMITH_*` for tracing (cell 3 prints whether tracing is live).

## Architecture

### State

One `GameStudioState` TypedDict flows through every graph. List fields use `Annotated[list[...], operator.add]` so parallel workers can append without clobbering. Records are joined by **`idea_id`** — a UUID assigned in `ideation_node` after the LLM returns (the LLM never generates it). `GameIdea → GameDesignRecord → GameDevelopRecord` all carry it.

### Per-phase models

Models are declared in one cell and swapped by reassigning a single variable (`LLM_DEVELOP_MODEL = LLM_DEVELOP_OPUS_MODEL`). Keep that pattern — don't inline model IDs in nodes.

The develop model is the delicate one, and the comments in that cell record hard-won constraints:

- Use `ChatAnthropic(...)`, **not** the `"anthropic:claude-opus-5"` string form — the string defaults to `max_tokens=4096`, which truncates tool arguments mid-JSON.
- `streaming=True` is required at large `max_tokens` or the HTTP request times out.
- `ModelRetryMiddleware` retries transport faults (`DEVELOP_TRANSPORT_ERRORS`) because those surface while the SSE body streams — outside the SDK's own retry window.
- `AnthropicPromptCachingMiddleware` is appended **only** when the model is a `ChatAnthropic`; on other providers it warns every turn and caches nothing.
- `gpt-5.6-sol` rejects any `reasoning_effort` other than `"none"` when tools are bound on chat completions.

### The develop phase (the interesting part)

The develop agent never writes HTML into chat. It calls `write_game_html_part(content, part)` in a strict `start → js × N → end` sequence, built by `make_dev_tools(game_title, idea_id)` — a closure so each parallel worker gets its own buffer. The tool aggressively rejects malformed input (chunks over `MAX_JS_CHUNK_CHARS = 6000`, a `start` that closes `</script>`, a `js` chunk containing HTML tags) and only writes to disk on `part=end`.

Output path is anchored to the **notebook's own directory**, not the kernel's cwd: `_resolve_notebook_dir()` reads `__vsc_ipynb_file__` (VS Code/Cursor), then `__session__` / `JPY_SESSION_NAME` (JupyterLab, Notebook 7), then falls back to walking up from cwd looking for the notebook file. `STUDIO_OUTPUT_DIR = NOTEBOOK_DIR / "dev-output"`, giving `/Users/mab/dev/agents/pingmab-agents/mabstruct_studio/dev-output/<game_title>/<idea_id>/index.html` (the test node writes `game_testing.json` beside it). The cell prints the resolved directory and how it was resolved, and warns loudly if it had to fall back to cwd — that fallback is the one case where output could land outside the `.gitignore` rule `mabstruct_studio/dev-output*/`. `develop_node` deletes any stale `index.html` before the run so a leftover file can't be mistaken for this run's output.

**Validation tiers:**
- **Tier 0** (`run_static_validation`) — exactly one inline `<script>` block + `node --check` on it. Runs automatically on write and via the `verify_game_html` tool.
- **Tier 1** (`scripts/game_smoke_test.mjs`, deleted from the working tree but in git history; driven by the test node in the experimenting notebook) — executes the game JS in a hand-rolled DOM/canvas shim in `node:vm`, simulates a start click, and reports JSON.

On Tier-0 failure `develop_node` issues exactly **one** repair turn that continues the same conversation — never a second full build. Failures are recorded in `GameDevelopRecord.tier0_pass` + `summary` rather than raised.

### Known rough edge

The studio notebook's develop phase is currently driven **manually** (cell 48 hand-assembles `dev_state` from `ideas` and `brief`), not by the composed graph. `develop_node` therefore reads `state["game_ideation"][0]` and `design.game_sub_title` — shapes that match that hand-built state, not `GameIdeaList` / `GameDesignRecord`. Fix this when wiring ideation → design → develop into one graph.

## Conventions

- Prompts are module-level f-strings named `<PHASE>_SYSTEM_PROMPT` / `<PHASE>_HUMAN_PROMPT`, all sharing `MABSTRUCT_GAMESTUDIO_BACKGROUNDER` (sci-fi, cosmic, slightly surreal single-player browser games). Keep new phases on that naming.
- Agents are built with `create_agent(model=..., system_prompt=..., tools=..., response_format=SomePydanticModel)` and read back via `agent_result["structured_response"]`.
- Each phase gets a node function plus a small standalone `StateGraph` for testing it in isolation (`dev_builder` / `dev_studio`) before it joins the main graph.
- Every graph cell ends with `display(Image(graph.get_graph().draw_mermaid_png()))`.
- `_message_text(message)` exists because Anthropic models return content as a list of blocks (thinking + text); never assume `message.content` is a string.
- Commit messages follow `type(mabstruct): summary`.

## Notes

- `.venv/` is at the parent repo root, not here.
- `memory.db` (SQLite checkpointer) is written next to the notebook and is disposable.
- The "Persisting to SQLite" / "Adding a UI" / "Recap" cells at the end are leftover course scaffolding referencing a `graph`/`spanish` state that this notebook doesn't define — they are not part of the studio pipeline.
