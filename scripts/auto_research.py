from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "research-sources.yml"
DEFAULT_OUTPUT = ROOT / "research" / "auto-research-latest.md"
DEFAULT_CACHE_DIR = ROOT / ".cache" / "auto-research"
USER_AGENT = "smart-skill-user-auto-research/1.0"

SOURCE_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{1,80}$")
SOURCE_TYPES = {"github_user", "github_repo", "web_page"}
LICENSE_LEVELS = {"low", "medium", "high"}
FORBIDDEN_FETCH_WORDS = {"clone", "checkout", "full_repo", "full-repo"}


@dataclass(frozen=True)
class SourceResult:
    source_id: str
    label: str
    source_type: str
    status: str
    item_count: int
    cache_status: str
    fetch_strategy: str
    license_sensitivity: str
    notes: str
    focus: tuple[str, ...]


@dataclass(frozen=True)
class Idea:
    title: str
    impact: str
    risk: str
    effort: str
    source_id: str
    license_sensitivity: str
    rationale: str


def _strip_inline_comment(line: str) -> str:
    in_single = False
    in_double = False
    for index, char in enumerate(line):
        if char == "'" and not in_double:
            in_single = not in_single
        elif char == '"' and not in_single:
            in_double = not in_double
        elif char == "#" and not in_single and not in_double:
            return line[:index].rstrip()
    return line.rstrip()


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "":
        return ""
    if value in {"true", "True"}:
        return True
    if value in {"false", "False"}:
        return False
    if value in {"null", "None", "~"}:
        return None
    if value.startswith("[") and value.endswith("]"):
        inside = value[1:-1].strip()
        if not inside:
            return []
        return [_parse_scalar(part.strip()) for part in inside.split(",")]
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def load_config(path: Path = DEFAULT_CONFIG) -> dict[str, Any]:
    """Load the small YAML subset used by config/research-sources.yml."""
    config: dict[str, Any] = {"defaults": {}, "sources": []}
    section: str | None = None
    current_source: dict[str, Any] | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = _strip_inline_comment(raw_line)
        if not line.strip():
            continue

        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()

        if indent == 0 and stripped.endswith(":"):
            if current_source is not None:
                config["sources"].append(current_source)
                current_source = None
            section = stripped[:-1]
            config.setdefault(section, [] if section == "sources" else {})
            continue

        if indent == 0 and ":" in stripped:
            if current_source is not None:
                config["sources"].append(current_source)
                current_source = None
            key, value = stripped.split(":", 1)
            config[key.strip()] = _parse_scalar(value)
            section = None
            continue

        if section == "defaults":
            key, value = stripped.split(":", 1)
            config["defaults"][key.strip()] = _parse_scalar(value)
            continue

        if section == "sources":
            if stripped.startswith("- "):
                if current_source is not None:
                    config["sources"].append(current_source)
                current_source = {}
                rest = stripped[2:].strip()
                if rest:
                    key, value = rest.split(":", 1)
                    current_source[key.strip()] = _parse_scalar(value)
                continue

            if current_source is None:
                raise ValueError("Source entry property found before '- id'.")
            key, value = stripped.split(":", 1)
            current_source[key.strip()] = _parse_scalar(value)
            continue

        raise ValueError(f"Unsupported config line: {raw_line}")

    if current_source is not None:
        config["sources"].append(current_source)

    if not isinstance(config.get("sources"), list):
        raise ValueError("Config must contain a sources list.")
    if not isinstance(config.get("defaults"), dict):
        raise ValueError("Config defaults must be a mapping.")
    return config


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [str(value).strip()] if str(value).strip() else []


def _host(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    return parsed.netloc.lower()


def _validate_http_url(url: str, allowed_hosts: list[str], field: str) -> None:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise ValueError(f"{field} must be an http(s) URL.")
    if parsed.hostname is None:
        raise ValueError(f"{field} must include a host.")
    hostname = parsed.hostname.lower()
    if hostname not in set(allowed_hosts):
        raise ValueError(f"{field} host '{hostname}' is not in allowed_hosts.")


def validate_source(source: dict[str, Any]) -> None:
    source_id = str(source.get("id", ""))
    if not SOURCE_ID_RE.fullmatch(source_id):
        raise ValueError(f"Invalid source id: {source_id!r}")

    source_type = str(source.get("type", ""))
    if source_type not in SOURCE_TYPES:
        raise ValueError(f"{source_id}: unsupported source type {source_type!r}.")

    allowed_hosts = _as_list(source.get("allowed_hosts"))
    if not allowed_hosts or any("*" in host for host in allowed_hosts):
        raise ValueError(f"{source_id}: allowed_hosts must be explicit.")

    url = str(source.get("url", ""))
    _validate_http_url(url, allowed_hosts, f"{source_id}.url")

    api_url = source.get("api_url")
    if api_url:
        _validate_http_url(str(api_url), allowed_hosts, f"{source_id}.api_url")

    fetch_strategy = str(source.get("fetch_strategy", "")).lower()
    if any(word in fetch_strategy for word in FORBIDDEN_FETCH_WORDS):
        raise ValueError(f"{source_id}: fetch_strategy cannot request repo cloning.")

    license_sensitivity = str(source.get("license_sensitivity", "medium"))
    if license_sensitivity not in LICENSE_LEVELS:
        raise ValueError(f"{source_id}: license_sensitivity must be low, medium, or high.")

    if source_type == "github_user" and not source.get("user"):
        raise ValueError(f"{source_id}: github_user sources require user.")
    if source_type == "github_repo":
        repo = str(source.get("repo", ""))
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
            raise ValueError(f"{source_id}: github_repo sources require owner/name repo.")


def validate_config(config: dict[str, Any]) -> None:
    if int(config.get("version", 0)) != 1:
        raise ValueError("Config version must be 1.")
    if not config.get("sources"):
        raise ValueError("At least one research source is required.")
    for source in config["sources"]:
        validate_source(source)


def _safe_int(value: Any, default: int, minimum: int = 1, maximum: int = 100000) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return default
    return max(minimum, min(maximum, parsed))


def _github_user_url(source: dict[str, Any], max_items: int) -> str:
    if source.get("api_url"):
        return str(source["api_url"])
    query = urllib.parse.urlencode({"sort": "updated", "per_page": min(max_items, 30)})
    return f"https://api.github.com/users/{source['user']}/repos?{query}"


def _github_repo_url(source: dict[str, Any]) -> str:
    if source.get("api_url"):
        return str(source["api_url"])
    return f"https://api.github.com/repos/{source['repo']}"


def _cache_path(cache_dir: Path, url: str) -> Path:
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()
    return cache_dir / f"{digest}.json"


def _read_cache(cache_dir: Path, url: str, ttl_hours: int) -> tuple[str | None, str]:
    path = _cache_path(cache_dir, url)
    if not path.is_file():
        return None, "miss"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        fetched_at = dt.datetime.fromisoformat(payload["fetched_at"])
        age = dt.datetime.now(dt.UTC) - fetched_at
        status = "hit" if age <= dt.timedelta(hours=ttl_hours) else "stale"
        return str(payload["body"]), status
    except (KeyError, json.JSONDecodeError, ValueError):
        return None, "corrupt"


def _write_cache(cache_dir: Path, url: str, body: str) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "url_host": _host(url),
        "fetched_at": dt.datetime.now(dt.UTC).isoformat(),
        "body": body,
    }
    _cache_path(cache_dir, url).write_text(json.dumps(payload, indent=2), encoding="utf-8")


def fetch_bounded(
    url: str,
    *,
    offline: bool,
    cache_dir: Path,
    ttl_hours: int,
    timeout_seconds: int,
    max_bytes: int,
    refresh_cache: bool,
) -> tuple[str | None, str, str]:
    cached_body, cache_status = _read_cache(cache_dir, url, ttl_hours)
    if cached_body is not None and not refresh_cache and cache_status == "hit":
        return cached_body, cache_status, "ok"

    if offline:
        if cached_body is not None:
            return cached_body, f"offline-{cache_status}", "ok"
        return None, "offline-miss", "offline: no network access attempted"

    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            raw = response.read(max_bytes + 1)
    except urllib.error.URLError as exc:
        if cached_body is not None:
            return cached_body, f"fallback-{cache_status}", f"network warning: {exc.reason}"
        return None, "network-error", f"network warning: {exc.reason}"

    body = raw[:max_bytes].decode("utf-8", errors="replace")
    _write_cache(cache_dir, url, body)
    truncated = "truncated" if len(raw) > max_bytes else "ok"
    return body, "fetched", truncated


def _summarize_github_user(body: str, max_items: int) -> int:
    data = json.loads(body)
    if not isinstance(data, list):
        return 0
    return min(len(data), max_items)


def _summarize_github_repo(body: str) -> int:
    data = json.loads(body)
    return 1 if isinstance(data, dict) and data.get("full_name") else 0


def _summarize_web_page(body: str) -> int:
    title = re.search(r"<title[^>]*>(.*?)</title>", body, flags=re.IGNORECASE | re.DOTALL)
    return 1 if title else 0


def collect_source(
    source: dict[str, Any],
    defaults: dict[str, Any],
    *,
    offline: bool,
    cache_dir: Path,
    refresh_cache: bool,
) -> SourceResult:
    validate_source(source)
    source_id = str(source["id"])
    source_type = str(source["type"])
    enabled = bool(source.get("enabled", True))
    label = str(source.get("label", source_id))
    fetch_strategy = str(source.get("fetch_strategy", "metadata_only"))
    license_sensitivity = str(source.get("license_sensitivity", "medium"))
    focus = tuple(_as_list(source.get("research_focus")))
    notes = str(source.get("notes", ""))

    if not enabled:
        return SourceResult(
            source_id=source_id,
            label=label,
            source_type=source_type,
            status="disabled",
            item_count=0,
            cache_status="not-used",
            fetch_strategy=fetch_strategy,
            license_sensitivity=license_sensitivity,
            notes=notes,
            focus=focus,
        )

    max_items = _safe_int(
        source.get("max_items", defaults.get("max_items_per_source")),
        default=5,
        minimum=1,
        maximum=30,
    )
    max_bytes = _safe_int(defaults.get("max_bytes_per_item"), default=12000, maximum=50000)
    ttl_hours = _safe_int(defaults.get("cache_ttl_hours"), default=168, maximum=24 * 365)
    timeout_seconds = _safe_int(defaults.get("request_timeout_seconds"), default=10, maximum=60)

    if source_type == "github_user":
        url = _github_user_url(source, max_items)
    elif source_type == "github_repo":
        url = _github_repo_url(source)
    else:
        url = str(source["url"])

    body, cache_status, status = fetch_bounded(
        url,
        offline=offline,
        cache_dir=cache_dir,
        ttl_hours=ttl_hours,
        timeout_seconds=timeout_seconds,
        max_bytes=max_bytes,
        refresh_cache=refresh_cache,
    )

    item_count = 0
    if body is not None:
        try:
            if source_type == "github_user":
                item_count = _summarize_github_user(body, max_items)
            elif source_type == "github_repo":
                item_count = _summarize_github_repo(body)
            else:
                item_count = _summarize_web_page(body)
        except (json.JSONDecodeError, TypeError):
            status = "parse warning: cached or fetched body was not expected format"

    return SourceResult(
        source_id=source_id,
        label=label,
        source_type=source_type,
        status=status,
        item_count=item_count,
        cache_status=cache_status,
        fetch_strategy=fetch_strategy,
        license_sensitivity=license_sensitivity,
        notes=notes,
        focus=focus,
    )


def generate_ideas(results: list[SourceResult]) -> list[Idea]:
    ideas: list[Idea] = []

    for result in results:
        if result.status == "disabled":
            continue
        focus = set(result.focus)

        if result.source_type.startswith("github"):
            ideas.append(
                Idea(
                    title="Add source review cards before accepting external inspiration",
                    impact="high",
                    risk="low",
                    effort="small",
                    source_id=result.source_id,
                    license_sensitivity=result.license_sensitivity,
                    rationale="Capture source, license, what was learned, and what was not copied.",
                )
            )

        if {"teaching_style", "minimal_examples"} & focus:
            ideas.append(
                Idea(
                    title="Improve examples with smaller original before/after preflight transcripts",
                    impact="medium",
                    risk="medium",
                    effort="medium",
                    source_id=result.source_id,
                    license_sensitivity=result.license_sensitivity,
                    rationale="Use public teaching patterns as inspiration, then write new examples from scratch.",
                )
            )

        if {"repo_safety", "workflow_safety", "permissions"} & focus:
            ideas.append(
                Idea(
                    title="Keep self-improvement jobs artifact-only with read-only repository permissions",
                    impact="high",
                    risk="low",
                    effort="small",
                    source_id=result.source_id,
                    license_sensitivity=result.license_sensitivity,
                    rationale="Reports can inform humans without opening noisy issues or changing behavior.",
                )
            )

        if {"evaluation", "tests"} & focus:
            ideas.append(
                Idea(
                    title="Add deterministic routing fixtures for one-skill versus skill-stack decisions",
                    impact="high",
                    risk="low",
                    effort="medium",
                    source_id=result.source_id,
                    license_sensitivity=result.license_sensitivity,
                    rationale="Measure token-aware routing quality without live services or broad research.",
                )
            )

        if {"docs_quality", "artifacts"} & focus:
            ideas.append(
                Idea(
                    title="Publish report summaries as downloadable artifacts instead of committed churn",
                    impact="medium",
                    risk="low",
                    effort="small",
                    source_id=result.source_id,
                    license_sensitivity=result.license_sensitivity,
                    rationale="Preserve a review trail while keeping generated research out of version control.",
                )
            )

    unique: dict[tuple[str, str], Idea] = {}
    for idea in ideas:
        unique.setdefault((idea.title, idea.source_id), idea)
    return list(unique.values())


def _escape_cell(value: Any) -> str:
    text = html.escape(str(value), quote=False)
    return text.replace("|", "&#124;").replace("\n", " ")


def build_report(
    *,
    config_path: Path,
    results: list[SourceResult],
    ideas: list[Idea],
    offline: bool,
    dry_run: bool,
) -> str:
    generated_at = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat()
    mode = ", ".join(
        [
            "offline" if offline else "online-bounded",
            "dry-run" if dry_run else "report-only",
        ]
    )
    display_config = config_path.name if config_path.is_absolute() else config_path.as_posix()

    lines = [
        "# Auto-Research Improvement Report",
        "",
        f"- Generated: {generated_at}",
        f"- Mode: {mode}",
        f"- Config: {display_config}",
        "- Safety: No commits, pushes, PRs, releases, or issues are created by this script.",
        "- Network: Offline mode never attempts network access; online mode fetches bounded allowlisted metadata only.",
        "- License: External code is not copied. Behavior changes require license review and maintainer approval.",
        "",
        "## Approved Sources",
        "",
        "| Source | Type | Status | Items | Cache | Strategy | License sensitivity |",
        "| --- | --- | --- | ---: | --- | --- | --- |",
    ]

    for result in results:
        lines.append(
            "| "
            + " | ".join(
                [
                    _escape_cell(result.source_id),
                    _escape_cell(result.source_type),
                    _escape_cell(result.status),
                    _escape_cell(result.item_count),
                    _escape_cell(result.cache_status),
                    _escape_cell(result.fetch_strategy),
                    _escape_cell(result.license_sensitivity),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Improvement Ideas",
            "",
            "| Idea | Impact | Risk | Effort | Source | License sensitivity |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )

    if ideas:
        for idea in ideas:
            lines.append(
                "| "
                + " | ".join(
                    [
                        _escape_cell(idea.title),
                        _escape_cell(idea.impact),
                        _escape_cell(idea.risk),
                        _escape_cell(idea.effort),
                        _escape_cell(idea.source_id),
                        _escape_cell(idea.license_sensitivity),
                    ]
                )
                + " |"
            )
    else:
        lines.append("| No ideas generated | n/a | n/a | n/a | n/a | n/a |")

    lines.extend(
        [
            "",
            "## Review Gates",
            "",
            "- Treat every idea as a proposal, not an implementation instruction.",
            "- Confirm the source is public and allowlisted before deeper research.",
            "- Review licenses before adapting external code, structure, or examples.",
            "- Write original implementation and docs; cite sources when they materially influence decisions.",
            "- Require human approval before commits that change behavior, PRs, releases, publishing, or integrations.",
            "",
            "## Notes",
            "",
            "- The loop avoids whole-repository loading by default.",
            "- GitHub user sources use public repository metadata, not clones.",
            "- Reports are designed for human review and should not be auto-applied.",
        ]
    )
    return "\n".join(lines) + "\n"


def run(args: argparse.Namespace) -> Path:
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = ROOT / config_path
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = ROOT / output_path
    cache_dir = Path(args.cache_dir)
    if not cache_dir.is_absolute():
        cache_dir = ROOT / cache_dir

    config = load_config(config_path)
    validate_config(config)
    defaults = config.get("defaults", {})

    results = [
        collect_source(
            source,
            defaults,
            offline=args.offline,
            cache_dir=cache_dir,
            refresh_cache=args.refresh_cache,
        )
        for source in config["sources"]
    ]
    ideas = generate_ideas(results)
    report = build_report(
        config_path=Path(args.config),
        results=results,
        ideas=ideas,
        offline=args.offline,
        dry_run=args.dry_run,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return output_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a safe, optional auto-research improvement report."
    )
    parser.add_argument("--config", default="config/research-sources.yml")
    parser.add_argument("--output", default="research/auto-research-latest.md")
    parser.add_argument("--cache-dir", default=".cache/auto-research")
    parser.add_argument("--offline", action="store_true", help="Do not attempt network access.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Keep the run proposal/report-only. No behavior changes are ever applied.",
    )
    parser.add_argument(
        "--refresh-cache",
        action="store_true",
        help="Ignore fresh cache entries and refetch allowlisted sources when online.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        output_path = run(args)
    except Exception as exc:  # pragma: no cover - CLI guardrail
        print(f"auto-research failed: {exc}", file=sys.stderr)
        return 1
    display = output_path.relative_to(ROOT).as_posix() if output_path.is_relative_to(ROOT) else output_path.name
    print(f"Auto-research report written to {display}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
