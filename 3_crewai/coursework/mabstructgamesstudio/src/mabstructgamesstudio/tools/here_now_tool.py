import hashlib
import mimetypes
import os
from pathlib import Path

import requests

from crewai.tools import tool

HERENOW_BASE_URL = "https://here.now"
PROJECT_ROOT = Path(__file__).parents[3]


def _load_api_key() -> str | None:
    key = os.getenv("HERENOW_API_KEY")
    if key:
        return key.strip()

    credentials = Path.home() / ".herenow" / "credentials"
    if credentials.exists():
        return credentials.read_text(encoding="utf-8").strip() or None

    return None


def _guess_content_type(path: Path) -> str:
    content_type, _ = mimetypes.guess_type(path.name)
    return content_type or "application/octet-stream"


def _resolve_source(path: str) -> Path:
    source = Path(path)
    if not source.is_absolute():
        source = PROJECT_ROOT / source
    if not source.exists():
        raise FileNotFoundError(f"Artifact path not found: {source}")
    return source


def _collect_publish_files(source: Path) -> list[tuple[str, Path]]:
    if source.is_file():
        if source.suffix.lower() == ".html":
            return [("index.html", source)]
        return [(source.name, source)]

    if source.is_dir():
        pairs = [
            (file.relative_to(source).as_posix(), file)
            for file in sorted(source.rglob("*"))
            if file.is_file()
        ]
        if not pairs:
            raise ValueError(f"No files found in directory: {source}")
        return pairs

    raise ValueError(f"Unsupported artifact path: {source}")


def _publish_to_here_now(
    pairs: list[tuple[str, Path]],
    display_name: str | None = None,
) -> dict:
    manifest = []
    file_data: dict[str, bytes] = {}

    for publish_path, local_path in pairs:
        data = local_path.read_bytes()
        file_data[publish_path] = data
        manifest.append(
            {
                "path": publish_path,
                "size": len(data),
                "contentType": _guess_content_type(local_path),
                "hash": hashlib.sha256(data).hexdigest(),
            }
        )

    body: dict = {"files": manifest}
    if display_name:
        body["displayName"] = display_name[:80]

    headers = {
        "Content-Type": "application/json",
        "X-HereNow-Client": "crewai/mabstructgamesstudio",
    }
    api_key = _load_api_key()
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    create_response = requests.post(
        f"{HERENOW_BASE_URL}/api/v1/publish",
        json=body,
        headers=headers,
        timeout=60,
    )
    create_response.raise_for_status()
    created = create_response.json()

    upload_info = created["upload"]
    version_id = upload_info["versionId"]
    uploads_by_path = {item["path"]: item for item in upload_info["uploads"]}

    for publish_path, local_path in pairs:
        target = uploads_by_path.get(publish_path)
        if target is None:
            continue

        put_headers = dict(target.get("headers", {}))
        if not any(key.lower() == "content-type" for key in put_headers):
            put_headers["Content-Type"] = _guess_content_type(local_path)

        put_response = requests.put(
            target["url"],
            data=file_data[publish_path],
            headers=put_headers,
            timeout=120,
        )
        put_response.raise_for_status()

    slug = created["slug"]
    finalize_response = requests.post(
        f"{HERENOW_BASE_URL}/api/v1/publish/{slug}/finalize",
        json={"versionId": version_id},
        headers=headers,
        timeout=60,
    )
    finalize_response.raise_for_status()
    finalized = finalize_response.json()

    return {
        "slug": slug,
        "siteUrl": finalized.get("siteUrl") or created.get("siteUrl"),
        "anonymous": created.get("anonymous", api_key is None),
        "claimUrl": created.get("claimUrl"),
        "expiresAt": created.get("expiresAt"),
    }


@tool("Deploy to here.now")
def deploy_to_here_now(artifact_path: str, game_title: str = "") -> str:
    """
    Publish a browser game HTML file or folder to a live temporary here.now URL.

    Use this after the game HTML has been written. Pass the path to the game's
    HTML file (it will be published as index.html) or a directory containing
    the site files.

    Args:
        artifact_path: Path to game_development.html or a directory with the game files.
        game_title: Optional game title used as the here.now site display name.

    Returns:
        Deployment summary including the live site URL.
    """
    try:
        source = _resolve_source(artifact_path)
        result = _publish_to_here_now(
            _collect_publish_files(source),
            display_name=game_title or None,
        )
    except requests.HTTPError as exc:
        detail = exc.response.text if exc.response is not None else str(exc)
        return f"Deployment failed: HTTP {exc.response.status_code if exc.response else 'error'}: {detail}"
    except Exception as exc:
        return f"Deployment failed: {exc}"

    site_url = result["siteUrl"]

    lines = [
        f"Deployed to {site_url}",
        f"Slug: {result['slug']}",
        f"Temporary site: {'yes (24h)' if result.get('anonymous') else 'no'}",
    ]

    if result.get("claimUrl"):
        lines.append(f"Claim URL: {result['claimUrl']}")
    if result.get("expiresAt"):
        lines.append(f"Expires at: {result['expiresAt']}")

    return "\n".join(lines)
