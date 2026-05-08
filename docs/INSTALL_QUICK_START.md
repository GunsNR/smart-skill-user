# Install Quick Start

Smart Skill User can be installed four ways. Choose the smallest install path that matches your workflow.

## 1. Global Codex Install

Use this when you want Codex instructed to run Smart Skill Preflight before each task or session.

This installs:

- `$HOME/.codex/AGENTS.md`
- `$HOME/.agents/skills/smart-skill-user/SKILL.md`

Windows PowerShell:

```powershell
cd "<path-to-smart-skill-user>"
.\scripts\install-codex-global.ps1
```

macOS/Linux:

```bash
cd "<path-to-smart-skill-user>"
bash ./scripts/install-codex-global.sh
```

Restart Codex after installation.

Verification prompt:

```text
Before doing anything, list the instruction sources and skills you loaded. Then run Smart Skill Preflight for this task: update a mobile homepage hero. Do not edit files.
```

Expected result:

- Codex mentions Smart Skill Preflight or user-level guidance.
- Codex confirms scope.
- Codex selects a relevant skill stack.
- Codex skips irrelevant skills.
- Codex edits no files.

## 2. Repo-Level Codex Install

Use this when one repository needs project-specific guidance.

Copy:

```text
skills/smart-skill-user/SKILL.md
```

To:

```text
your-repo/.agents/skills/smart-skill-user/SKILL.md
```

Then add the Smart Skill Preflight section from:

```text
templates/AGENTS.md
```

To:

```text
your-repo/AGENTS.md
```

Copy-paste prompt for Codex:

```text
Install Smart Skill User in this repo. Copy the skill to .agents/skills/smart-skill-user/SKILL.md, add Smart Skill Preflight as the first step in AGENTS.md, validate, and do not modify product code.
```

## 3. Claude Code Install

Use this when your project uses `CLAUDE.md`.

1. Open or create `CLAUDE.md` at your project root.
2. Copy the relevant content from `templates/CLAUDE.md`.
3. Keep project-specific rules concise.
4. Ask Claude Code to run Smart Skill Preflight before work.

Example prompt:

```text
Add Smart Skill Preflight to this project's CLAUDE.md using the template from Smart Skill User. Keep it concise and do not modify product code.
```

Smart Skill User does not claim native Claude skill packaging. It provides portable Markdown instructions.

## 4. Generic AGENTS.md Install

Use this when your agent reads `AGENTS.md` or similar repo guidance.

1. Open or create `AGENTS.md` at your repository root.
2. Copy the content from `templates/smart-skill-preflight.md`.
3. Add project-specific scope rules and approval gates.
4. Keep the guidance short enough to run before every task.

Example prompt:

```text
Add Smart Skill Preflight to this repository's AGENTS.md using the Smart Skill User template. Keep it generic, validate the docs, and do not modify product code.
```

## What The Preflight Should Do

Every install path should make the agent start with:

- confirmed repo/project/client scope
- task type
- selected best skill or smallest effective skill stack
- skipped skills, if important
- approval needed or not
- planned validation

The workflow should avoid loading every skill, reading unrelated docs, or running broad research unless the task needs it.
