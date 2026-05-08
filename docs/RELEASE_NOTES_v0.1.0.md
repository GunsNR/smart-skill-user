# Smart Skill User v0.1.0

Smart Skill User is an MIT-licensed preflight workflow for AI coding agents.

It helps Codex, Claude Code, and AGENTS.md-compatible workflows start with a short routing step before implementation: confirm scope, identify task type, choose the best skill or smallest effective skill stack, skip unrelated guidance, and apply approval gates.

## What Is Included

- Core `smart-skill-user` skill.
- Global Codex install guidance.
- Repo-level Codex install guidance.
- Claude Code portable instruction template.
- Generic AGENTS.md template.
- Task examples for UI, SEO, media, cleanup, deploy, and wrong-scope work.
- Skill routing matrix.
- Safety and approval-gate docs.
- Token-efficiency docs.
- Validation script and pytest coverage.
- Support, launch copy, and quick-start documentation.
- skills.sh / npx skills direct GitHub install documentation.
- Optional report-only auto-research loop.

## Quick Start

Global Codex install:

```powershell
cd "<path-to-smart-skill-user>"
.\scripts\install-codex-global.ps1
```

Repo-level install:

```text
Copy skills/smart-skill-user/SKILL.md to your-repo/.agents/skills/smart-skill-user/SKILL.md
Add Smart Skill Preflight to your-repo/AGENTS.md
```

npx skills direct GitHub install:

```bash
npx skills add GunsNR/smart-skill-user --skill smart-skill-user --agent codex --copy --yes
```

Verification prompt:

```text
Before doing anything, list the instruction sources and skills you loaded. Then run Smart Skill Preflight for this task: update a mobile homepage hero. Do not edit files.
```

## Documentation

- [README](../README.md)
- [Install Quick Start](INSTALL_QUICK_START.md)
- [skills.sh / npx skills Install](SKILLS_SH_INSTALL.md)
- [GitHub Pages landing page](index.md)
- [Skill Routing Matrix](skill-routing-matrix.md)
- [Safety and Approval Gates](safety-and-approval-gates.md)
- [Support](../SUPPORT.md)

## Feedback

Feedback is welcome through GitHub issues:

- unclear install steps
- missing examples
- confusing approval gates
- suggested docs improvements

Please keep reports public-safe: no secrets, private client names, local paths, screenshots, videos, or credentials.
