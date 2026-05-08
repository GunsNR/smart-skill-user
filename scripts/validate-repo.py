from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "AGENTS.md",
    "install/codex-global.md",
    "install/codex-repo.md",
    "install/claude-code.md",
    "install/generic-agents-md.md",
    "skills/smart-skill-user/SKILL.md",
    "templates/AGENTS.md",
    "templates/global-codex-AGENTS.md",
    "templates/CLAUDE.md",
    "templates/smart-skill-preflight.md",
    "examples/mobile-hero-task.md",
    "examples/seo-schema-task.md",
    "examples/media-video-task.md",
    "examples/cleanup-revert-task.md",
    "examples/deployment-task.md",
    "examples/wrong-scope-task.md",
    "docs/how-it-works.md",
    "docs/skill-routing-matrix.md",
    "docs/token-efficiency.md",
    "docs/safety-and-approval-gates.md",
    "docs/auto-research-loop.md",
    "docs/self-improvement-policy.md",
    "docs/codex-vs-claude-code.md",
    "docs/faq.md",
    "config/research-sources.yml",
    "scripts/install-codex-global.ps1",
    "scripts/install-codex-global.sh",
    "scripts/validate-repo.py",
    "scripts/auto_research.py",
    "tests/test_repo_integrity.py",
    "tests/test_auto_research.py",
    "assets/social-preview.svg",
    ".github/workflows/ci.yml",
    ".github/workflows/auto-research.yml",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/pull_request_template.md",
    "skills/auto-research-loop/SKILL.md",
    "research/.gitignore",
]

PRIVATE_PATTERNS = [
    "Way" + "ne",
    "Stage" + "ItUS",
    "Tooth" + "ology",
    "Rank" + "Logic",
    "Atlas" + " Care",
    "C:" + "\\Users",
]

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"(?i)(api[_-]?key|secret|password)\s*=\s*['\"][^'\"]+['\"]"),
    re.compile(r"(?i)(private|customer|client)[ -]?(asset|video|screenshot)s?"),
    re.compile(r"(?i)\.env\s+(value|file|content)s?"),
    re.compile(r"(?i)phone\s+number\s*[:=]\s*\+?\d"),
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def iter_text_files() -> list[Path]:
    ignored_parts = {".git", "__pycache__", ".pytest_cache", ".cache"}
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and not any(part in ignored_parts for part in path.parts)
        and path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".gif", ".webp"}
    ]


def validate_required_files() -> None:
    missing = [rel for rel in REQUIRED_FILES if not (ROOT / rel).is_file()]
    if missing:
        raise AssertionError(f"Missing required files: {missing}")


def validate_skill_frontmatter() -> None:
    skill = read_text(ROOT / "skills/smart-skill-user/SKILL.md")
    expected = (
        "---\n"
        "name: smart-skill-user\n"
        "description: Token-aware preflight router that automatically chooses the best skill or smallest effective skill stack before an AI coding agent starts work.\n"
        "---"
    )
    if not skill.startswith(expected):
        raise AssertionError("SKILL.md front matter is missing or incorrect")


def validate_readme_sections() -> None:
    readme = read_text(ROOT / "README.md")
    required = [
        "Install: Codex Global",
        "Install: Repo-Level Codex",
        "Install: Claude Code",
        "Install: Generic AGENTS.md",
        "Make it run first in Codex",
        "Token-Efficiency Model",
        "Safety Model",
        "Optional Auto-Research Loop",
        "Launch Copy",
    ]
    missing = [section for section in required if section not in readme]
    if missing:
        raise AssertionError(f"README missing sections: {missing}")


def validate_privacy() -> None:
    leaks: list[str] = []
    for path in iter_text_files():
        text = read_text(path)
        rel = path.relative_to(ROOT).as_posix()
        for pattern in PRIVATE_PATTERNS:
            if pattern in text:
                leaks.append(f"{rel}: {pattern}")
        for regex in SECRET_PATTERNS:
            if regex.search(text):
                leaks.append(f"{rel}: {regex.pattern}")
    if leaks:
        raise AssertionError("Privacy scrub failed:\n" + "\n".join(leaks))


def main() -> None:
    validate_required_files()
    validate_skill_frontmatter()
    validate_readme_sections()
    validate_privacy()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
