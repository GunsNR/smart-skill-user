from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate-repo.py"
NEW_DOCS = [
    ROOT / "SUPPORT.md",
    ROOT / "docs" / "LAUNCH_COPY.md",
    ROOT / "docs" / "INSTALL_QUICK_START.md",
    ROOT / "docs" / "LAUNCH_ANNOUNCEMENTS.md",
    ROOT / "docs" / "index.md",
    ROOT / "docs" / "RELEASE_NOTES_v0.1.0.md",
    ROOT / "docs" / "SOCIAL_SHARE_KIT.md",
    ROOT / "docs" / "REPO_DISCOVERY_CHECKLIST.md",
]
VERIFICATION_PROMPT = (
    "Before doing anything, list the instruction sources and skills you loaded. "
    "Then run Smart Skill Preflight for this task: update a mobile homepage hero. "
    "Do not edit files."
)


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_repo", VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_required_files_exist():
    validator = load_validator()
    validator.validate_required_files()


def test_skill_frontmatter():
    validator = load_validator()
    validator.validate_skill_frontmatter()


def test_no_private_leakage():
    validator = load_validator()
    validator.validate_privacy()


def test_readme_mentions_required_ecosystem_terms():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for phrase in [
        "Codex",
        "Claude Code",
        "AGENTS.md",
        "token-aware",
        "best skill",
        "skill stack",
        "Token-Efficiency Model",
        "approval gates",
    ]:
        assert phrase in text


def test_readme_links_new_support_and_launch_docs():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for phrase in [
        "Install Quick Start",
        "GitHub Pages-ready Docs",
        "SUPPORT.md",
        "docs/index.md",
        "docs/RELEASE_NOTES_v0.1.0.md",
        "docs/SOCIAL_SHARE_KIT.md",
        "docs/REPO_DISCOVERY_CHECKLIST.md",
        "docs/LAUNCH_COPY.md",
        "docs/LAUNCH_ANNOUNCEMENTS.md",
        "Star this repo if it helps",
    ]:
        assert phrase in text


def test_readme_documents_global_run_first_codex_install():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for phrase in [
        "Make it run first in Codex",
        "run on every Codex task/session",
        "$HOME/.codex/AGENTS.md",
        "$HOME/.agents/skills",
        "does not modify Codex internals",
        "Repo-level install",
        "repo `AGENTS.md`",
        "repo `.agents/skills`",
        VERIFICATION_PROMPT,
    ]:
        assert phrase in text


def test_skill_promises_best_skill_stack_selection():
    text = (ROOT / "skills" / "smart-skill-user" / "SKILL.md").read_text(encoding="utf-8")
    for phrase in [
        "automatically choose the best skill or best skill stack",
        "smallest effective skill stack",
        "Score available skills",
        "Use 1 skill for narrow tasks",
        "Never load every skill by default",
    ]:
        assert phrase in text


def test_install_docs_templates_examples_and_scripts_exist():
    validator = load_validator()
    required = validator.REQUIRED_FILES
    for prefix in ["install/", "templates/", "examples/", "scripts/"]:
        matches = [path for path in required if path.startswith(prefix)]
        assert matches, f"No required files registered for {prefix}"
        for rel in matches:
            assert (ROOT / rel).is_file(), rel


def test_codex_global_install_doc_has_paths_restart_and_verification_prompt():
    text = (ROOT / "install" / "codex-global.md").read_text(encoding="utf-8")
    for phrase in [
        "$HOME/.codex/AGENTS.md",
        "$HOME/.agents/skills",
        "Restart Codex",
        "Verification Prompt",
        VERIFICATION_PROMPT,
        "Codex edits no files",
    ]:
        assert phrase in text


def test_repo_level_install_doc_has_copy_paths_and_install_prompt():
    text = (ROOT / "install" / "codex-repo.md").read_text(encoding="utf-8")
    for phrase in [
        "skills/smart-skill-user/SKILL.md",
        "your-repo/.agents/skills/smart-skill-user/SKILL.md",
        "your-repo/AGENTS.md",
        "Install Smart Skill User in this repo. Copy the skill to .agents/skills/smart-skill-user/SKILL.md, add Smart Skill Preflight as the first step in AGENTS.md, validate, and do not modify product code.",
        VERIFICATION_PROMPT,
    ]:
        assert phrase in text


def test_global_codex_template_has_required_preflight_rules():
    text = (ROOT / "templates" / "global-codex-AGENTS.md").read_text(encoding="utf-8")
    for phrase in [
        "Smart Skill Preflight",
        "Before implementing any user request",
        "single best skill",
        "smallest effective skill stack",
        "Do not load every skill",
        "Approval gates",
        "deploy, publish, DNS, CRM/live connector",
        "preview/render",
        "backup patch",
        "This is user-level instruction guidance, not a hook into Codex internals.",
    ]:
        assert phrase in text


def test_install_scripts_describe_backup_idempotency_and_verification_prompt():
    for rel in ["scripts/install-codex-global.ps1", "scripts/install-codex-global.sh"]:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for phrase in [
            "Backup created",
            "no duplicate insertion",
            "verification prompt",
            "Restart Codex",
            VERIFICATION_PROMPT,
        ]:
            assert phrase in text


def test_token_efficiency_says_automatic_does_not_load_everything():
    text = (ROOT / "docs" / "token-efficiency.md").read_text(encoding="utf-8")
    for phrase in [
        "Automatic does not mean",
        "Run a short preflight every task",
        "Avoid loading every skill",
        "Avoid broad research unless asked",
        "Avoid preview/render unless visual QA is needed",
    ]:
        assert phrase in text


def test_support_doc_is_community_focused_and_non_monetized():
    text = (ROOT / "SUPPORT.md").read_text(encoding="utf-8")
    for phrase in [
        "community-driven open-source project",
        "Installation And Setup Help",
        "Usage Questions",
        "Validation And Troubleshooting",
        "Issues, Feedback, And Contributions",
        "Code Of Conduct",
        "MIT licensed",
        "Support The Project",
        "star the repository",
        "contribute examples or documentation",
    ]:
        assert phrase in text
    assert "GitHub Sponsors" not in text
    assert "pricing" not in text.lower()


def test_install_quick_start_has_four_install_paths():
    text = (ROOT / "docs" / "INSTALL_QUICK_START.md").read_text(encoding="utf-8")
    for phrase in [
        "Global Codex Install",
        "Repo-Level Codex Install",
        "Claude Code Install",
        "Generic AGENTS.md Install",
        'cd "<path-to-smart-skill-user>"',
        ".\\scripts\\install-codex-global.ps1",
        "bash ./scripts/install-codex-global.sh",
        "your-repo/.agents/skills/smart-skill-user/SKILL.md",
        "templates/CLAUDE.md",
        "templates/smart-skill-preflight.md",
    ]:
        assert phrase in text


def test_launch_copy_has_required_channels_and_claims():
    text = (ROOT / "docs" / "LAUNCH_COPY.md").read_text(encoding="utf-8")
    for phrase in [
        "Primary Headline",
        "Tagline",
        "One-Liner",
        "Elevator Pitch",
        "X/Twitter Copy",
        "LinkedIn Post",
        "Reddit / Hacker News Post",
        "Email / Newsletter Pitch",
        "Mastodon / Bluesky Copy",
        "GitHub Repository Description",
        "Press / Speaking Points",
        "SEO Keywords",
        "https://github.com/GunsNR/smart-skill-user",
        "automatically chooses the best skill or smallest effective skill stack",
        "MIT licensed",
    ]:
        assert phrase in text


def test_launch_announcements_are_ready_to_edit_not_auto_publish():
    text = (ROOT / "docs" / "LAUNCH_ANNOUNCEMENTS.md").read_text(encoding="utf-8")
    for phrase in [
        "Do not post them automatically",
        "GitHub Release Note Draft",
        "X/Twitter Launch Thread",
        "LinkedIn Announcement",
        "Reddit / Hacker News Announcement",
        "Newsletter Announcement",
        "Community Post",
        "Maintainer Note",
        "do not imply affiliation with OpenAI, Anthropic, or GitHub",
        "do not promise measured token reductions unless you have current public data",
    ]:
        assert phrase in text


def test_pages_landing_page_exists_and_links_core_docs():
    text = (ROOT / "docs" / "index.md").read_text(encoding="utf-8")
    for phrase in [
        "Smart Skill User",
        "Automatically choose the best skill or smallest effective skill stack before your AI coding agent starts.",
        "Codex Global",
        "Codex Repo-Level",
        "Claude Code",
        "Generic AGENTS.md",
        "Before And After",
        "Safety Model",
        "Token Efficiency",
        "Optional Auto-Research Loop",
        "GitHub Pages",
        "Settings",
        "Source to `Deploy from a branch`",
        "Branch to `master`",
        "Folder to `/docs`",
        "Star the repo if it helps",
        "Try the verification prompt",
        "Open an issue",
    ]:
        assert phrase in text


def test_release_notes_v010_are_public_safe_and_useful():
    text = (ROOT / "docs" / "RELEASE_NOTES_v0.1.0.md").read_text(encoding="utf-8")
    for phrase in [
        "Smart Skill User v0.1.0",
        "What Is Included",
        "Quick Start",
        "Documentation",
        "Feedback",
        "Install Quick Start",
        "GitHub Pages landing page",
        "Skill Routing Matrix",
    ]:
        assert phrase in text


def test_social_share_kit_exists_and_discourages_auto_posting():
    text = (ROOT / "docs" / "SOCIAL_SHARE_KIT.md").read_text(encoding="utf-8")
    for phrase in [
        "Social Share Kit",
        "Best image to attach: `assets/social-preview.png`",
        "Short X Post",
        "X Thread",
        "LinkedIn Post",
        "Reddit / Hacker News Post",
        "Email / Newsletter Blurb",
        "Discord / Slack Blurb",
        "Ask Friends Or Developers To Star/Test",
        "Do Not Spam",
        "Do not post automatically",
        "Do not automate this",
    ]:
        assert phrase in text
    assert "automatically post" not in text
    assert "browser automation" not in text.lower()


def test_repo_discovery_checklist_tracks_manual_publication_steps():
    text = (ROOT / "docs" / "REPO_DISCOVERY_CHECKLIST.md").read_text(encoding="utf-8")
    for phrase in [
        "Repo Discovery Checklist",
        "Repo description",
        "Topics added manually",
        "Social preview image exists at `assets/social-preview.png`",
        "GitHub social preview manually uploaded",
        "Docs landing page exists at `docs/index.md`",
        "GitHub Pages enabled manually",
        "Settings -> Pages -> Source: Deploy from a branch",
        "Branch: `master`",
        "Folder: `/docs`",
        "GitHub release created manually",
        "No aggressive monetization copy",
    ]:
        assert phrase in text


def test_new_docs_are_clean_of_editor_artifacts_and_forbidden_language():
    forbidden = [
        "Make these code changes?",
        "Please confirm you want Copilot",
        "GunsNR accepted the action",
        "\nCode\n",
        "\nText\n",
        "\nPowerShell\n",
        "\nbash\n",
        "Gumroad",
        "pricing tier",
        "enterprise licensing",
        "PyPI",
        "npm publishing",
        "Marketplace",
        "official OpenAI",
        "official Anthropic",
        "official GitHub",
        "official Claude",
        "guaranteed virality",
        "guaranteed token savings",
        "fake adoption",
        "pricing tiers",
        "paid package",
        "paid-package",
        "automatically post to",
        "auto-post to",
    ]
    for path in NEW_DOCS:
        text = path.read_text(encoding="utf-8")
        for phrase in forbidden:
            assert phrase not in text, f"{path.name} contains forbidden phrase {phrase!r}"
