"""Static and smoke validation for generated browser games."""

from __future__ import annotations

import json
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

SCRIPT_BLOCK_RE = re.compile(
    r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>",
    re.IGNORECASE | re.DOTALL,
)
FORBIDDEN_IN_JS = ("<script", "</script>", "</html>", "<!doctype", "</body>")


def extract_inline_script_blocks(html: str) -> list[str]:
    return [block.strip() for block in SCRIPT_BLOCK_RE.findall(html) if block.strip()]


def run_static_validation(html_path: Path) -> dict[str, Any]:
    """Tier 0: structure + JS parse checks."""
    issues: list[str] = []
    checks: dict[str, bool | int | str] = {}

    if not html_path.exists():
        return {
            "tier": 0,
            "pass": False,
            "issues": [f"missing file: {html_path}"],
            "checks": checks,
        }

    html = html_path.read_text(encoding="utf-8")
    stripped = html.rstrip()
    checks["bytes"] = len(html)
    checks["lines"] = html.count("\n") + 1

    if not stripped.lower().startswith("<!doctype html") and not stripped.lower().startswith("<html"):
        issues.append("file must start with <!DOCTYPE html> or <html>")

    script_blocks = extract_inline_script_blocks(html)
    checks["script_blocks"] = len(script_blocks)
    if len(script_blocks) != 1:
        issues.append(
            f"expected exactly 1 inline <script> block, found {len(script_blocks)}"
        )

    html_close = stripped.lower().find("</html>")
    if html_close == -1:
        issues.append("missing closing </html>")
    elif html_close < len(stripped) - len("</html>"):
        trailing = stripped[html_close + len("</html>") :].strip()
        if trailing:
            issues.append("content appears after first </html> (chunk assembly bug)")

    body_closes = len(re.findall(r"</body>", stripped, re.IGNORECASE))
    html_closes = len(re.findall(r"</html>", stripped, re.IGNORECASE))
    checks["body_closes"] = body_closes
    checks["html_closes"] = html_closes
    if body_closes != 1:
        issues.append(f"expected exactly 1 </body>, found {body_closes}")
    if html_closes != 1:
        issues.append(f"expected exactly 1 </html>, found {html_closes}")

    if re.search(r'\bsrc\s*=\s*["\']https?://', html, re.IGNORECASE):
        issues.append("external script/src references found in single-file deliverable")

    parse_errors: list[str] = []
    if script_blocks:
        for index, block in enumerate(script_blocks):
            with tempfile.NamedTemporaryFile(
                mode="w",
                suffix=f"_{index}.js",
                delete=False,
                encoding="utf-8",
            ) as tmp:
                tmp.write(block)
                tmp_path = Path(tmp.name)
            try:
                proc = subprocess.run(
                    ["node", "--check", str(tmp_path)],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                if proc.returncode != 0:
                    message = (proc.stderr or proc.stdout or "parse failed").strip()
                    parse_errors.append(f"script block {index}: {message}")
            except FileNotFoundError:
                parse_errors.append("node is not installed — cannot run JS parse check")
                break
            except subprocess.TimeoutExpired:
                parse_errors.append(f"script block {index}: node --check timed out")
            finally:
                tmp_path.unlink(missing_ok=True)

    checks["js_parse_ok"] = not parse_errors
    issues.extend(parse_errors)

    return {
        "tier": 0,
        "pass": not issues,
        "issues": issues,
        "checks": checks,
    }


def run_smoke_test(html_path: Path, smoke_script: Path) -> dict[str, Any]:
    """Tier 1: headless boot + button click smoke test via Node harness."""
    if not smoke_script.exists():
        return {
            "tier": 1,
            "pass": False,
            "issues": [f"missing smoke harness: {smoke_script}"],
            "checks": {},
        }

    try:
        proc = subprocess.run(
            ["node", str(smoke_script), str(html_path)],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except FileNotFoundError:
        return {
            "tier": 1,
            "pass": False,
            "issues": ["node is not installed — cannot run smoke test"],
            "checks": {},
        }
    except subprocess.TimeoutExpired:
        return {
            "tier": 1,
            "pass": False,
            "issues": ["smoke test timed out after 30s"],
            "checks": {},
        }

    stdout = proc.stdout.strip()
    if not stdout:
        stderr = (proc.stderr or "no output from smoke harness").strip()
        return {
            "tier": 1,
            "pass": False,
            "issues": [f"smoke harness failed: {stderr}"],
            "checks": {"exit_code": proc.returncode},
        }

    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError:
        return {
            "tier": 1,
            "pass": False,
            "issues": [f"invalid smoke harness JSON: {stdout[:200]}"],
            "checks": {"exit_code": proc.returncode},
        }

    payload["tier"] = 1
    if "pass" not in payload:
        payload["pass"] = proc.returncode == 0 and not payload.get("issues")
    return payload


def run_all_game_tests(html_path: Path, smoke_script: Path) -> dict[str, Any]:
    tier0 = run_static_validation(html_path)
    tier1: dict[str, Any] | None = None
    if tier0["pass"]:
        tier1 = run_smoke_test(html_path, smoke_script)

    overall_pass = tier0["pass"] and bool(tier1 and tier1.get("pass"))
    blocked = not tier0["pass"] and tier1 is None

    return {
        "overall": "pass" if overall_pass else "fail",
        "blocked": blocked,
        "artifact": str(html_path),
        "tier0": tier0,
        "tier1": tier1,
    }


def write_test_report(report_path: Path, report: dict[str, Any]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")


def load_test_report(report_path: Path) -> dict[str, Any] | None:
    if not report_path.exists():
        return None
    return json.loads(report_path.read_text(encoding="utf-8"))
