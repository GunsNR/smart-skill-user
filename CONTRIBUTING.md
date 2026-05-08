# Contributing

Thanks for improving Smart Skill User.

## Guidelines

- Keep the project generic and public-safe.
- Do not include private workspace paths, customer names, credentials, or unpublished customer material.
- Prefer short, practical examples over broad essays.
- Keep the skill itself concise; put longer explanation in `docs/`.
- Add or update tests when changing structure, install docs, privacy rules, or skill front matter.

## Local Validation

```bash
python scripts/validate-repo.py
python -m pytest
git --no-pager diff --check
```

## Pull Requests

Open a focused PR with:

- what changed
- why it helps agent routing, safety, or installability
- validation run
- any compatibility notes for Codex, Claude Code, or AGENTS.md workflows
