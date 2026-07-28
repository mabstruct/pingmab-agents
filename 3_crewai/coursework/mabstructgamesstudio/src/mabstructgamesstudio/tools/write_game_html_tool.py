from pathlib import Path

from crewai.tools import tool

PROJECT_ROOT = Path(__file__).parents[3]
MAX_CHUNK_CHARS = 6000

_current_game_title: str | None = None


def set_game_title(game_title: str) -> None:
    global _current_game_title
    _current_game_title = game_title.strip() or None


def _require_game_title() -> str:
    if not _current_game_title:
        raise ValueError(
            "game_title is not set. This is configured automatically at crew kickoff."
        )
    return _current_game_title


def _game_html_path() -> Path:
    return PROJECT_ROOT / "output" / _require_game_title() / "index.html"


def _validate_content(content: str) -> str | None:
    if content is None or not str(content).strip():
        return (
            "content is empty — do NOT retry with empty arguments. "
            f"Pass a non-empty string under {MAX_CHUNK_CHARS} characters."
        )
    if len(content) > MAX_CHUNK_CHARS:
        return (
            f"chunk too large ({len(content)} chars). "
            f"Split into smaller pieces under {MAX_CHUNK_CHARS} chars each."
        )
    return None


@tool("Write game HTML")
def write_game_html(content: str, mode: str = "overwrite") -> str:
    """
    Write browser game HTML directly to disk at output/{game_title}/index.html.

    game_title is bound automatically from crew inputs — only pass content and mode.
    Use mode=overwrite for the first chunk, then mode=append for later chunks.
    Keep each chunk under 6000 characters to avoid tool-call failures.
    """
    try:
        error = _validate_content(content)
        if error:
            return f"Write rejected: {error}"

        path = _game_html_path()
        path.parent.mkdir(parents=True, exist_ok=True)

        normalized_mode = mode.strip().lower()
        if normalized_mode not in {"overwrite", "append"}:
            raise ValueError('mode must be "overwrite" or "append"')

        if normalized_mode == "overwrite":
            path.write_text(content, encoding="utf-8")
        else:
            existing = path.read_text(encoding="utf-8") if path.exists() else ""
            path.write_text(existing + content, encoding="utf-8")

        data = path.read_text(encoding="utf-8")
        return (
            f"Wrote {path.relative_to(PROJECT_ROOT)} "
            f"({len(data)} bytes, {data.count(chr(10)) + 1} lines, mode={normalized_mode})"
        )
    except Exception as exc:
        return f"Write failed: {exc}"


@tool("Verify game HTML")
def verify_game_html() -> str:
    """Check that output/{game_title}/index.html exists and looks complete."""
    try:
        path = _game_html_path()
        if not path.exists():
            return f"Missing file: {path.relative_to(PROJECT_ROOT)}"

        data = path.read_text(encoding="utf-8")
        stripped = data.rstrip()
        issues: list[str] = []

        if not stripped.lower().startswith("<!doctype html") and not stripped.lower().startswith("<html"):
            issues.append("missing <!DOCTYPE html> or <html> at start")
        if "</html>" not in stripped.lower():
            issues.append("missing closing </html>")
        if "</script>" not in stripped.lower():
            issues.append("missing closing </script>")
        if "<body" not in stripped.lower():
            issues.append("missing <body>")

        status = "complete" if not issues else "incomplete"
        summary = (
            f"{status}: {path.relative_to(PROJECT_ROOT)} "
            f"({len(data)} bytes, {data.count(chr(10)) + 1} lines)"
        )
        if issues:
            summary += "\nIssues: " + "; ".join(issues)
            summary += f"\nTail: ...{stripped[-80:]!r}"
        return summary
    except Exception as exc:
        return f"Verify failed: {exc}"
