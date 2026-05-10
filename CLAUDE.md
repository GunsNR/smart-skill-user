# CLAUDE.md

## Smart Skill Preflight

Before work, produce a brief preflight:

```text
Scope: <repo, project/client, branch if relevant, target page/service/module, or ask if unclear>
Task type: <UI/CRO, SEO/schema, copy, media, connector, research, cleanup, deploy, validation, docs>
Selected route: <best single skill, or smallest effective skill stack>
Why this route: <short reason each selected skill belongs>
Skipped skills: <irrelevant skills skipped when helpful>
Approval needed: <yes/no and why>
Planned validation: <smallest checks that match the risk>
```

Full routing rules: `.agents/skills/smart-skill-user/SKILL.md`

Use the selected skill stack as constraints. Do not read every document by default.

## Repo Context

This is the Smart Skill User project: a token-aware preflight router for Claude Code, Codex, and AGENTS.md-compatible coding agents.

Active surfaces:

- `skills/` — core skill definitions (do not modify without review)
- `templates/` — install templates for Claude Code, Codex, and generic agents
- `install/` — per-platform install guides
- `docs/` — supporting docs and release notes
- `scripts/` — install scripts and optional auto-research loop
- `tests/` — repo integrity and auto-research tests
- `examples/` — example task walkthroughs

## Approval Gates

- deploy/publish/push: explicit approval
- destructive cleanup or revert: backup patch or explicit approval
- secrets or private data: never expose
- unclear scope: stop and ask
- product code changes: do not modify without explicit instruction

## Release Safety

Do not publish packages, create remotes, push to GitHub, or deploy anything without explicit maintainer approval.
