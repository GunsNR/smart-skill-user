# Smart Skill User

**Stop loading every instruction. Start with the right ones.**

[![CI ready](https://img.shields.io/badge/CI-ready-blue.svg)](.github/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

![Smart Skill User social preview](assets/social-preview.svg)

**Automatically choose the best skill or smallest effective skill stack before your AI coding agent starts.**

Smart Skill User automatically chooses the best skill or smallest effective skill stack before your AI coding agent starts work. It gives Codex, Claude Code, and AGENTS.md-style workflows a token-aware preflight: confirm scope, classify the task, score available skills by relevance, choose one skill when one is enough or a stack when the task needs more, enforce approval gates, and avoid loading the entire instruction universe into context.

It is for developers who manage AI coding agents across multiple repos, clients, products, or instruction sets and want the agent to start focused instead of reading everything by default.

Quick start:

- [skills.sh / npx skills Install](docs/SKILLS_SH_INSTALL.md)
- [Install Quick Start](docs/INSTALL_QUICK_START.md)
- [GitHub Pages-ready docs](docs/index.md)
- [Release Notes v0.1.0](docs/RELEASE_NOTES_v0.1.0.md)

Direct GitHub install with the `skills` CLI:

```bash
npx skills add GunsNR/smart-skill-user --skill smart-skill-user --agent codex --copy --yes
```

List the available skills without installing:

```bash
npx skills add GunsNR/smart-skill-user --list
```

Global Codex install:

```powershell
cd "<path-to-smart-skill-user>"
.\scripts\install-codex-global.ps1
```

Star this repo if it helps your AI coding workflow. Feedback and docs improvements are welcome.

## Why This Exists

AI coding agents are powerful, but many repositories now contain layered instructions, skills, templates, client notes, deployment rules, and workflow docs. Loading all of it by default wastes context and increases the chance of wrong-repo, wrong-client, or wrong-tool drift.

Smart Skill User turns that messy first minute into a repeatable preflight that routes each task to the right skill stack before execution begins.

## The Problem

- Agents load too many instructions before they know the task.
- Agents often need one excellent skill, not a pile of unrelated ones.
- Long-running repos accumulate stale or unrelated guidance.
- Multi-client workspaces make wrong-scope edits easier.
- Visual, cleanup, connector, and deploy tasks need different approval gates.
- Token waste makes agents slower and less focused.

## What It Does

Smart Skill User asks an agent to start every task by reporting:

- confirmed scope: repo, project/client, branch, page/service/module
- task type: UI, SEO, copy, media, connector, research, cleanup, deploy, validation, or docs
- selected route: the best single skill for narrow tasks, or the smallest effective skill stack for multi-part work
- relevance reason: why each selected skill belongs in the stack
- skipped skills: irrelevant skills explicitly skipped when skipping prevents wasted work
- approval gates: preview, backup patch, deploy approval, or secret-safety rules
- planned validation: the smallest checks that match the risk

## How It Works

1. Read only the preflight instruction.
2. Confirm the working scope.
3. Classify the request.
4. Score available skills by task relevance, risk, and validation needs.
5. Automatically choose the best skill or minimal skill stack.
6. Apply the selected skill stack as constraints, not as decoration.
7. Validate and report concisely.

```text
Preflight -> scope -> task type -> best skill stack -> safer execution
```

## Make it run first in Codex

Install Smart Skill User globally so Codex is instructed to run Smart Skill Preflight before each task or session. This does not modify Codex internals; it uses Codex's user-level instruction and skill locations.

There are two supported Codex modes:

- **Global Codex install:** best for "run on every Codex task/session." Uses `$HOME/.codex/AGENTS.md` and `$HOME/.agents/skills`.
- **Repo-level install:** best for team or project-specific behavior. Uses repo `AGENTS.md` and repo `.agents/skills`.

Verification prompt:

```text
Before doing anything, list the instruction sources and skills you loaded. Then run Smart Skill Preflight for this task: update a mobile homepage hero. Do not edit files.
```

Expected result:

- Codex mentions Smart Skill Preflight or the global/user-level guidance.
- Codex confirms scope.
- Codex selects a relevant skill stack.
- Codex skips irrelevant skills.
- Codex edits no files.

## Quick Links

- [Install Quick Start](docs/INSTALL_QUICK_START.md)
- [skills.sh / npx skills Install](docs/SKILLS_SH_INSTALL.md)
- [GitHub Pages-ready Docs](docs/index.md)
- [Support](SUPPORT.md)
- [FAQ](docs/faq.md)
- [Release Notes v0.1.0](docs/RELEASE_NOTES_v0.1.0.md)
- [Social Share Kit](docs/SOCIAL_SHARE_KIT.md)
- [Repo Discovery Checklist](docs/REPO_DISCOVERY_CHECKLIST.md)
- [Launch Copy](docs/LAUNCH_COPY.md)
- [Launch Announcements](docs/LAUNCH_ANNOUNCEMENTS.md)

## Before And After

**User prompt**

> Update the mobile homepage hero.

**Without preflight**

The agent may read unrelated backend docs, deployment notes, database schemas, and old client context before touching the UI.

**With Smart Skill User**

```text
Scope: unclear: which repo/client/page?
Task type: UI/CRO
Selected route: visual-quality + CRO review + copy/local SEO
Why this stack: mobile UI work needs layout, conversion, and copy checks
Skipped: deployment, database, connector tools
Approval needed: yes, preview before commit
```

## Install: Codex Global

Use this when you want Smart Skill User available across your Codex workspaces and instructed to run as the first preflight step on every Codex task.

```powershell
cd "<path-to-smart-skill-user>"
.\scripts\install-codex-global.ps1
```

```bash
cd "<path-to-smart-skill-user>"
bash ./scripts/install-codex-global.sh
```

Manual install:

1. Copy `skills/smart-skill-user/SKILL.md` to `$HOME/.agents/skills/smart-skill-user/SKILL.md`.
2. Add the guidance from `templates/global-codex-AGENTS.md` to `$HOME/.codex/AGENTS.md`.
3. Restart Codex.
4. Paste the verification prompt from "Make it run first in Codex."

See [install/codex-global.md](install/codex-global.md).

## Install: npx skills

Use this when you want the standard `skills` CLI to install Smart Skill User from GitHub.

List available skills:

```bash
npx skills add GunsNR/smart-skill-user --list
```

Install only the core skill for Codex:

```bash
npx skills add GunsNR/smart-skill-user --skill smart-skill-user --agent codex --copy --yes
```

Install it globally for Codex:

```bash
npx skills add GunsNR/smart-skill-user --skill smart-skill-user --agent codex --global --copy --yes
```

The `skills` CLI installs the skill. To make Smart Skill Preflight run first on every Codex task, also add the Codex guidance from the global or repo-level install docs.

See [docs/SKILLS_SH_INSTALL.md](docs/SKILLS_SH_INSTALL.md).

## Install: Repo-Level Codex

Use this when a repository needs team or project-specific Smart Skill Preflight behavior.

1. Copy `skills/smart-skill-user/SKILL.md` to `your-repo/.agents/skills/smart-skill-user/SKILL.md`.
2. Add the Smart Skill Preflight section from `templates/AGENTS.md` to `your-repo/AGENTS.md`.
3. Ask Codex to validate the install without modifying product code.

Copy-paste prompt:

```text
Install Smart Skill User in this repo. Copy the skill to .agents/skills/smart-skill-user/SKILL.md, add Smart Skill Preflight as the first step in AGENTS.md, validate, and do not modify product code.
```

See [install/codex-repo.md](install/codex-repo.md).

## Install: Claude Code

Smart Skill User is portable to Claude Code through `CLAUDE.md`. This repo does not claim native Claude skill support; it provides a compatible instruction pack.

Copy the relevant parts of [templates/CLAUDE.md](templates/CLAUDE.md) into your project `CLAUDE.md`.

See [install/claude-code.md](install/claude-code.md).

## Install: Generic AGENTS.md

For any agent that reads `AGENTS.md`, copy the preflight from [templates/smart-skill-preflight.md](templates/smart-skill-preflight.md) into your repository guidance.

See [install/generic-agents-md.md](install/generic-agents-md.md).

## Examples

- [Mobile hero task](examples/mobile-hero-task.md)
- [SEO schema task](examples/seo-schema-task.md)
- [Media and video task](examples/media-video-task.md)
- [Cleanup or revert task](examples/cleanup-revert-task.md)
- [Deployment task](examples/deployment-task.md)
- [Wrong-scope task](examples/wrong-scope-task.md)

## Routing Matrix Preview

| Task | Best skill or stack | Skip | Gate |
| --- | --- | --- | --- |
| Mobile hero | visual + CRO + copy | deployment, database | preview before commit |
| SEO schema | schema + source-truth + copy | deploy, media | no fake claims |
| Media/video | media extraction + asset policy | database, CRM | no hotlinking |
| Cleanup/revert | review + backup + validation | visual unless affected | backup patch first |
| Deploy/release | release + CI + hosting | unrelated docs | explicit approval |

See [docs/skill-routing-matrix.md](docs/skill-routing-matrix.md).

## Safety Model

Smart Skill User does not make changes safer by magic. It makes the agent pause long enough to choose the right safety rule:

- visual/CRO: preview before commit
- deploy/publish/DNS/CRM: explicit approval
- cleanup/revert/destructive work: backup patch first
- secrets/private data: never expose
- unclear scope: stop and ask

See [docs/safety-and-approval-gates.md](docs/safety-and-approval-gates.md).

## Token-Efficiency Model

The goal is not to minimize context at all costs. The goal is to spend context only after the task is understood.

Smart Skill User favors:

- a short preflight on every task
- targeted searches over broad file reads
- the best skill or smallest effective skill stack over every skill doc
- avoiding broad research unless asked
- avoiding preview/render unless visual QA is needed
- current repo state over old chat history
- bounded validation over unnecessary renders or live tools

See [docs/token-efficiency.md](docs/token-efficiency.md).

## Optional Auto-Research Loop

Smart Skill User now includes an optional self-improvement loop that generates reviewable research reports from approved public sources. It is report-only by default: it does not commit changes, push branches, open pull requests, publish releases, create issues, or copy external code.

Run an offline dry run locally:

```bash
python scripts/auto_research.py --offline --dry-run --output research/auto-research-latest.md
```

The source allowlist lives in [config/research-sources.yml](config/research-sources.yml). It includes a configurable `karpathy-public-github` source for public GitHub repository metadata from the GitHub user `karpathy`. That source is marked `metadata_only` with high license sensitivity, so the loop can generate original improvement ideas without cloning repositories or copying code.

Generated reports are written under `research/` and classify ideas by impact, risk, effort, source, and license sensitivity. Online runs use bounded public metadata and `.cache/auto-research` to avoid repeated source reads.

The GitHub Action in [.github/workflows/auto-research.yml](.github/workflows/auto-research.yml) can be run manually and also runs on a quiet weekly schedule. It has read-only repository permissions and uploads the report as an artifact instead of changing the repository.

See [docs/auto-research-loop.md](docs/auto-research-loop.md) and [docs/self-improvement-policy.md](docs/self-improvement-policy.md).

## Limitations

- It is an instruction workflow, not a permissions sandbox.
- It cannot prevent a tool from running if your agent ignores instructions.
- It depends on clear repo guidance and honest scope reporting.
- It does not replace tests, code review, or deployment controls.
- Claude Code support is provided through portable instructions, not native skill packaging.

## Roadmap

- More routing examples for backend, data, and security tasks
- More optional source adapters for safe, public research reports
- More install helpers for team templates
- Example pull request showing a before/after agent workflow

## Launch Copy

**Short X post**

Stop loading every instruction into your AI coding agent.

Smart Skill User is a tiny preflight workflow for Codex, Claude Code, and AGENTS.md agents: confirm scope, classify the task, automatically choose the best skill or minimal skill stack, and enforce approval gates before work starts.

**LinkedIn post**

AI coding agents need better first steps. Smart Skill User is a lightweight, open-source preflight workflow for Codex, Claude Code, and AGENTS.md-compatible agents. It helps agents confirm scope, identify task type, automatically choose the best skill or smallest effective skill stack, and apply safety gates for visual work, cleanup, connectors, and deploys.

It is intentionally small: one skill, install templates, examples, validation tests, and docs for teams that want less context waste and fewer wrong-scope edits.

**Reddit/Hacker News style post**

I made a small open-source workflow called Smart Skill User. It is a token-aware preflight router for AI coding agents. The idea is simple: before an agent reads half your repo docs, it should confirm scope, classify the task, automatically pick the best skill or minimal skill stack, and identify approval gates.

It supports Codex skill installs, repo-level AGENTS.md, Claude Code instructions, and generic agent workflows. Feedback welcome, especially from people maintaining multi-project AI coding setups.

**GitHub repo description**

Token-aware skill routing for Codex, Claude Code, and AGENTS.md coding agents.

**SEO keywords**

Codex skills, Claude Code instructions, AGENTS.md, AI coding agents, agent skills, prompt engineering, token optimization, developer workflow automation, coding agent safety.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md), keep examples generic, and avoid adding private customer or workspace data.

For setup help, usage questions, and feedback guidance, see [SUPPORT.md](SUPPORT.md).

## License

MIT. See [LICENSE](LICENSE).
