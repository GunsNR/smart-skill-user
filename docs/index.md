# Smart Skill User

**Automatically choose the best skill or smallest effective skill stack before your AI coding agent starts.**

Smart Skill User is a lightweight preflight workflow for Codex, Claude Code, and AGENTS.md-compatible coding agents. It helps an agent confirm scope, classify the task, choose the right skill route, skip irrelevant guidance, and apply approval gates before editing.

[GitHub Repo](https://github.com/GunsNR/smart-skill-user) · [README](https://github.com/GunsNR/smart-skill-user#readme) · [Quick Start](INSTALL_QUICK_START.md) · [Support](https://github.com/GunsNR/smart-skill-user/blob/master/SUPPORT.md)

## Install

Choose the install path that matches your workflow:

- [Top 14 Skills](TOP_SKILLS.md): curated companion skills — token savers, SEO/marketing depth, Karpathy guardrails, plus May 2026 trending additions (graphify, claude-blog, claude-ads, obsidian-second-brain). Install with `bash scripts/install-top-skills.sh`.
- [npx skills Direct GitHub Install](SKILLS_SH_INSTALL.md): best when you want the standard `skills` CLI to install from `GunsNR/smart-skill-user`.
- [Codex Global](https://github.com/GunsNR/smart-skill-user/blob/master/install/codex-global.md): best when you want Codex instructed to run Smart Skill Preflight before each task or session.
- [Codex Repo-Level](https://github.com/GunsNR/smart-skill-user/blob/master/install/codex-repo.md): best when one project needs team or repo-specific guidance.
- [Claude Code](https://github.com/GunsNR/smart-skill-user/blob/master/install/claude-code.md): portable instructions through `CLAUDE.md`.
- [Generic AGENTS.md](https://github.com/GunsNR/smart-skill-user/blob/master/install/generic-agents-md.md): plain Markdown for compatible coding agents.

Direct CLI install:

```bash
npx skills add GunsNR/smart-skill-user --skill smart-skill-user --agent codex --copy --yes
```

Start here:

```text
Before doing anything, list the instruction sources and skills you loaded. Then run Smart Skill Preflight for this task: update a mobile homepage hero. Do not edit files.
```

## Before And After

Without preflight, an agent may read unrelated backend notes, deployment rules, old workspace context, and every available skill before touching a narrow task.

With Smart Skill User:

```text
Scope: repo confirmed, homepage hero, mobile breakpoint.
Task type: UI/CRO.
Selected skill stack: visual QA for layout; copy review for CTA.
Skipped skills: deployment, database.
Approval needed: preview before commit.
Planned validation: responsive screenshot and test suite.
```

## Features

- Chooses the single best skill for narrow tasks.
- Chooses the smallest effective skill stack for multi-part tasks.
- Confirms repo, project, client, branch, and target surface before editing.
- Skips unrelated skills and docs.
- Keeps context focused with targeted file reads and searches.
- Works with Codex, Claude Code, and AGENTS.md-compatible workflows.
- Uses plain Markdown instructions and small installer scripts.
- Includes validation tests and privacy checks.

## Safety Model

Smart Skill User does not replace tests, review, or permissions. It makes the agent pause long enough to choose the right safety rule.

- Visual/CRO work: preview or render before commit.
- Deploy, publish, DNS, CRM, and live connector work: explicit approval first.
- Cleanup or revert work: backup patch first.
- Secrets and private data: never expose.
- Unclear scope: stop and ask.

See [Safety and Approval Gates](safety-and-approval-gates.md).

## Token Efficiency

Automatic routing does not mean loading everything. The workflow starts with a short preflight, then loads only the smallest useful skill stack and the files needed for the task.

See [Token Efficiency](token-efficiency.md) and the [Skill Routing Matrix](skill-routing-matrix.md).

## Optional Auto-Research Loop

Smart Skill User includes an optional report-only auto-research loop. It can study approved public sources and generate improvement ideas without committing changes, opening PRs, publishing releases, or copying external code.

See [Auto-Research Loop](auto-research-loop.md) and [Self-Improvement Policy](self-improvement-policy.md).

## GitHub Pages

This page is ready for GitHub Pages from the `/docs` folder. If Pages is not enabled yet, turn it on manually:

1. Open repository Settings.
2. Go to Pages.
3. Set Source to `Deploy from a branch`.
4. Set Branch to `master`.
5. Set Folder to `/docs`.

No analytics, tracking scripts, or external assets are required.

## Share And Improve

- Star the repo if it helps.
- Try the verification prompt above.
- Open an issue with feedback or unclear setup steps.

More links:

- [Install Quick Start](INSTALL_QUICK_START.md)
- [skills.sh / npx skills Install](SKILLS_SH_INSTALL.md)
- [Release Notes v0.1.0](RELEASE_NOTES_v0.1.0.md)
- [Social Share Kit](SOCIAL_SHARE_KIT.md)
- [Repo Discovery Checklist](REPO_DISCOVERY_CHECKLIST.md)
