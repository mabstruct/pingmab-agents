from pathlib import Path

from crewai.tools import tool

from .game_context import require_game_title
from .game_validation import run_all_game_tests, write_test_report

PROJECT_ROOT = Path(__file__).parents[3]
SMOKE_SCRIPT = Path(__file__).parent.parent / "scripts" / "game_smoke_test.mjs"


def _game_html_path() -> Path:
    return PROJECT_ROOT / "output" / require_game_title() / "index.html"


def _testing_json_path() -> Path:
    return PROJECT_ROOT / "output" / require_game_title() / "game_testing.json"


@tool("Run game tests")
def run_game_tests() -> str:
    """
    Run automated Tier-0 (parse/structure) and Tier-1 (boot smoke) tests.

    Writes machine-checkable results to output/{game_title}/game_testing.json.
    The QA agent must call this tool before writing any test report.
    """
    try:
        html_path = _game_html_path()
        report = run_all_game_tests(html_path, SMOKE_SCRIPT)
        json_path = _testing_json_path()
        write_test_report(json_path, report)

        tier0 = report["tier0"]
        tier1 = report.get("tier1")
        lines = [
            f"overall={report['overall']}",
            f"artifact={json_path.relative_to(PROJECT_ROOT)}",
            f"tier0={'pass' if tier0['pass'] else 'fail'}",
        ]
        if tier0.get("issues"):
            lines.append("tier0 issues: " + "; ".join(tier0["issues"]))
        if tier1 is None:
            lines.append("tier1=skipped (tier0 failed)")
        else:
            lines.append(f"tier1={'pass' if tier1.get('pass') else 'fail'}")
            if tier1.get("issues"):
                lines.append("tier1 issues: " + "; ".join(tier1["issues"]))
        if report["overall"] != "pass":
            lines.append(
                "Do NOT claim the game is playable unless overall=pass. "
                "Report BLOCKED if tests failed."
            )
        return "\n".join(lines)
    except Exception as exc:
        return f"Run game tests failed: {exc}"


@tool("Check deployment gate")
def check_deployment_gate() -> str:
    """
    Verify game_testing.json exists and overall=pass before deploying.

    Deploy must not proceed unless this tool reports DEPLOY ALLOWED.
    """
    try:
        json_path = _testing_json_path()
        if not json_path.exists():
            return (
                "DEPLOY BLOCKED: missing game_testing.json. "
                "Run game tests must pass before deployment."
            )

        import json

        report = json.loads(json_path.read_text(encoding="utf-8"))
        overall = report.get("overall")
        if overall != "pass":
            tier0 = report.get("tier0", {})
            tier1 = report.get("tier1") or {}
            return (
                "DEPLOY BLOCKED: game_testing.json overall="
                f"{overall}. tier0={tier0.get('pass')}, tier1={tier1.get('pass')}. "
                "Send the game back to development/testing."
            )

        html_path = _game_html_path()
        if not html_path.exists():
            return f"DEPLOY BLOCKED: missing {html_path.relative_to(PROJECT_ROOT)}"

        return (
            "DEPLOY ALLOWED: game_testing.json overall=pass. "
            f"Artifact: {html_path.relative_to(PROJECT_ROOT)}"
        )
    except Exception as exc:
        return f"DEPLOY BLOCKED: gate check failed: {exc}"
