from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "auto_research.py"


def load_auto_research():
    spec = importlib.util.spec_from_file_location("auto_research", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_config_includes_safe_karpathy_public_source():
    auto_research = load_auto_research()
    config = auto_research.load_config(ROOT / "config" / "research-sources.yml")
    auto_research.validate_config(config)

    karpathy = next(source for source in config["sources"] if source["id"] == "karpathy-public-github")
    assert karpathy["type"] == "github_user"
    assert karpathy["user"] == "karpathy"
    assert karpathy["fetch_strategy"] == "metadata_only"
    assert karpathy["license_sensitivity"] == "high"
    assert "api.github.com" in karpathy["allowed_hosts"]


def test_offline_dry_run_writes_report_without_network(tmp_path, monkeypatch):
    auto_research = load_auto_research()

    def fail_urlopen(*args, **kwargs):
        raise AssertionError("offline mode must not attempt network access")

    monkeypatch.setattr(auto_research.urllib.request, "urlopen", fail_urlopen)
    output = tmp_path / "report.md"

    exit_code = auto_research.main(
        ["--offline", "--dry-run", "--output", str(output), "--cache-dir", str(tmp_path / "cache")]
    )

    assert exit_code == 0
    report = output.read_text(encoding="utf-8")
    assert "Mode: offline, dry-run" in report
    assert "karpathy-public-github" in report
    assert "offline: no network access attempted" in report
    assert "No commits, pushes, PRs, releases, or issues" in report
    assert "| Idea | Impact | Risk | Effort | Source | License sensitivity |" in report


def test_source_validation_rejects_clone_strategy():
    auto_research = load_auto_research()
    source = {
        "id": "unsafe-source",
        "label": "Unsafe",
        "type": "github_repo",
        "repo": "example/project",
        "url": "https://github.com/example/project",
        "api_url": "https://api.github.com/repos/example/project",
        "allowed_hosts": ["github.com", "api.github.com"],
        "fetch_strategy": "full_repo_clone",
        "license_sensitivity": "high",
    }

    try:
        auto_research.validate_source(source)
    except ValueError as exc:
        assert "repo cloning" in str(exc)
    else:
        raise AssertionError("clone-style fetch strategies must be rejected")


def test_auto_research_workflow_is_report_only():
    workflow = (ROOT / ".github" / "workflows" / "auto-research.yml").read_text(encoding="utf-8")
    forbidden = ["contents: write", "git push", "gh pr", "gh issue", "create-pull-request"]

    assert "permissions:\n  contents: read" in workflow
    assert "actions/upload-artifact" in workflow
    assert "workflow_dispatch" in workflow
    assert "pull_request:" not in workflow
    for phrase in forbidden:
        assert phrase not in workflow
