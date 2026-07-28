"""Persist and resolve the active game_title across kickoff, replay, and tools."""

from __future__ import annotations

import json
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parents[3]
CONTEXT_FILE = PROJECT_ROOT / "output" / ".studio_context.json"

_current_game_title: str | None = None


def set_game_title(game_title: str) -> None:
    global _current_game_title
    title = game_title.strip()
    _current_game_title = title or None
    if title:
        CONTEXT_FILE.parent.mkdir(parents=True, exist_ok=True)
        CONTEXT_FILE.write_text(
            json.dumps({"game_title": title}, indent=2),
            encoding="utf-8",
        )


def load_persisted_game_title() -> str | None:
    if CONTEXT_FILE.exists():
        try:
            data = json.loads(CONTEXT_FILE.read_text(encoding="utf-8"))
            title = str(data.get("game_title", "")).strip()
            if title:
                return title
        except (json.JSONDecodeError, OSError):
            pass
    return None


def infer_game_title_from_outputs() -> str | None:
    output_root = PROJECT_ROOT / "output"
    if not output_root.is_dir():
        return None

    candidates: list[tuple[float, str]] = []
    for child in output_root.iterdir():
        if not child.is_dir() or child.name.startswith("."):
            continue
        index_html = child / "index.html"
        if index_html.is_file():
            candidates.append((index_html.stat().st_mtime, child.name))

    if not candidates:
        return None

    candidates.sort(reverse=True)
    return candidates[0][1]


def resolve_game_title() -> str | None:
    global _current_game_title

    if _current_game_title:
        return _current_game_title

    for source in (
        lambda: os.getenv("GAME_TITLE", "").strip() or None,
        load_persisted_game_title,
        infer_game_title_from_outputs,
    ):
        title = source()
        if title:
            _current_game_title = title
            return title

    return None


def require_game_title() -> str:
    title = resolve_game_title()
    if not title:
        raise ValueError(
            "game_title is not set. Run the crew with kickoff inputs, "
            "replay with: crewai replay -t <task_id> \"The Big Swallow\", "
            "or set GAME_TITLE."
        )
    return title
