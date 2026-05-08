# Install For Codex Global

Use this when you want Smart Skill User available across Codex workspaces and instructed to run Smart Skill Preflight as the first step on every Codex task or session.

This does not modify Codex internals. It installs user-level guidance and a user-level skill:

- `$HOME/.codex/AGENTS.md`
- `$HOME/.agents/skills/smart-skill-user/SKILL.md`

## PowerShell

```powershell
cd "<path-to-smart-skill-user>"
.\scripts\install-codex-global.ps1
```

The script copies the skill to:

```text
$HOME/.agents/skills/smart-skill-user/SKILL.md
```

It also creates or updates:

```text
$HOME/.codex/AGENTS.md
```

Existing files are backed up before modification. The installer skips duplicate Smart Skill Preflight insertion if your global `AGENTS.md` already contains it.

## macOS/Linux

```bash
cd "<path-to-smart-skill-user>"
bash ./scripts/install-codex-global.sh
```

The script copies the skill to:

```text
$HOME/.agents/skills/smart-skill-user/SKILL.md
```

It also creates or updates:

```text
$HOME/.codex/AGENTS.md
```

## Manual Install

1. Copy `skills/smart-skill-user/SKILL.md` into your user skills directory.
2. Add `templates/global-codex-AGENTS.md` to your global Codex guidance.
3. Restart Codex.
4. Paste the verification prompt below in a new Codex session.

## Verification Prompt

```text
Before doing anything, list the instruction sources and skills you loaded. Then run Smart Skill Preflight for this task: update a mobile homepage hero. Do not edit files.
```

Expected result:

- Codex mentions Smart Skill Preflight or the global/user-level guidance.
- Codex confirms scope.
- Codex selects a relevant skill stack.
- Codex skips irrelevant skills.
- Codex edits no files.
