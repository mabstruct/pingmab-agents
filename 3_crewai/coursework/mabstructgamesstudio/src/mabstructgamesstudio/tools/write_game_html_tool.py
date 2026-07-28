from pathlib import Path

from crewai.tools import tool

from .game_context import require_game_title, set_game_title
from .game_validation import run_static_validation

PROJECT_ROOT = Path(__file__).parents[3]
MAX_JS_CHUNK_CHARS = 6000

_buffer: list[str] = []


def _game_html_path() -> Path:
    return PROJECT_ROOT / "output" / require_game_title() / "index.html"


def _forbidden_js_tags(content: str) -> str | None:
    lower = content.lower()
    for tag in ("<script", "</script>", "</html>", "<!doctype", "</body>", "<body"):
        if tag in lower:
            return tag
    return None


@tool("Write game HTML part")
def write_game_html_part(content: str, part: str) -> str:
    """
    Assemble a single-file HTML game safely across multiple calls.

    game_title is bound automatically from crew inputs.

    Args:
        content: HTML or JavaScript source for this part.
        part: One of:
            - start: <!DOCTYPE html> through opening <script> (no closes yet)
            - js: raw JavaScript only (repeatable)
            - end: final JavaScript plus </script></body></html>, then writes file
    """
    global _buffer

    try:
        if not content or not str(content).strip():
            return (
                "Write rejected: content is empty. Do NOT call with empty arguments. "
                f"Pass a non-empty string under {MAX_JS_CHUNK_CHARS} characters."
            )

        normalized_part = part.strip().lower()
        if normalized_part not in {"start", "js", "end"}:
            return 'Write rejected: part must be "start", "js", or "end".'

        if normalized_part in {"start", "js"} and len(content) > MAX_JS_CHUNK_CHARS:
            return (
                f"Write rejected: chunk too large ({len(content)} chars). "
                f"Split into pieces under {MAX_JS_CHUNK_CHARS} characters."
            )

        if normalized_part == "start":
            _buffer.clear()
            lower = content.lower()
            if not lower.lstrip().startswith("<!doctype html"):
                return "Write rejected: start must begin with <!DOCTYPE html>"
            if "<script" not in lower:
                return "Write rejected: start must open exactly one <script> block"
            if "</script>" in lower or "</html>" in lower:
                return (
                    "Write rejected: start must NOT close </script> or </html>. "
                    "Use part=js for code and part=end for closing tags."
                )
            _buffer.append(content)
            return (
                f"Buffered start ({len(content)} chars). "
                "Next: part=js for JavaScript chunks, then part=end to finalize."
            )

        if normalized_part == "js":
            if not _buffer:
                return "Write rejected: call part=start before part=js."
            forbidden = _forbidden_js_tags(content)
            if forbidden:
                return (
                    f"Write rejected: js part must be raw JavaScript only "
                    f"(found {forbidden}). Never open a new <script> block."
                )
            _buffer.append(content)
            total = sum(len(piece) for piece in _buffer)
            return f"Buffered js ({len(content)} chars). Assembly total: {total} chars."

        if not _buffer:
            return "Write rejected: call part=start before part=end."
        lower = content.lower()
        if "</script>" not in lower or "</html>" not in lower:
            return "Write rejected: end must include </script></body></html>."
        if lower.count("<script") > lower.count("</script>"):
            return "Write rejected: end must not open a new <script> block."

        _buffer.append(content)
        full = "".join(_buffer)
        path = _game_html_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(full, encoding="utf-8")
        _buffer.clear()

        validation = run_static_validation(path)
        status = "PASS" if validation["pass"] else "FAIL"
        lines = [
            f"Wrote {path.relative_to(PROJECT_ROOT)} ({len(full)} bytes)",
            f"Tier-0 validation: {status}",
        ]
        if validation["issues"]:
            lines.append("Issues: " + "; ".join(validation["issues"]))
        else:
            lines.append("Single inline script block parsed successfully.")
        if not validation["pass"]:
            lines.append("Fix issues and rewrite using part=start again.")
        return "\n".join(lines)
    except Exception as exc:
        return f"Write failed: {exc}"


@tool("Verify game HTML")
def verify_game_html() -> str:
    """Run Tier-0 validation on output/{game_title}/index.html (structure + node --check)."""
    try:
        path = _game_html_path()
        validation = run_static_validation(path)
        status = "PASS" if validation["pass"] else "FAIL"
        lines = [
            f"Tier-0 validation: {status}",
            f"File: {path.relative_to(PROJECT_ROOT)}",
        ]
        checks = validation.get("checks", {})
        if checks:
            lines.append(
                "Checks: "
                + ", ".join(f"{key}={value}" for key, value in sorted(checks.items()))
            )
        issues = validation.get("issues", [])
        if issues:
            lines.append("Issues:")
            lines.extend(f"- {issue}" for issue in issues)
        return "\n".join(lines)
    except Exception as exc:
        return f"Verify failed: {exc}"


# Re-export for crew kickoff hook
__all__ = ["set_game_title", "write_game_html_part", "verify_game_html"]
