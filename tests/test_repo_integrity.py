from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate-repo.py"


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
