---
name: auto-research-loop
description: Optional report-only self-improvement loop that studies approved public sources, classifies improvement ideas, and preserves human approval gates before any behavior changes.
---

# Auto-Research Loop

Use this skill when a maintainer explicitly asks for optional auto-research or self-improvement reports.

## Scope

This skill is for report generation and idea triage only. It does not authorize commits, pull requests, releases, publishing, new integrations, or copied external code.

## Workflow

1. Run Smart Skill Preflight first and confirm the target repository.
2. Read `config/research-sources.yml`.
3. Prefer offline or cached runs unless the maintainer asks for bounded online research.
4. Generate a report under `research/`.
5. Classify ideas by impact, risk, effort, source, and license sensitivity.
6. Ask for explicit maintainer approval before implementing any idea that changes behavior.

## Safety Rules

- Use only approved public sources.
- Do not clone whole external repositories by default.
- Do not copy external code or distinctive examples without license review.
- Do not include private client data, local paths, secrets, screenshots, or videos in reports.
- Do not create issues, pull requests, releases, or published packages by default.
- Treat network failures as report warnings, not normal validation failures.

## Local Command

```bash
python scripts/auto_research.py --offline --dry-run --output research/auto-research-latest.md
```
