# Install For Codex Global

Use this when you want Smart Skill User available across Codex workspaces.

## PowerShell

```powershell
pwsh ./scripts/install-codex-global.ps1
```

The script copies the skill to:

```text
$HOME\.agents\skills\smart-skill-user\SKILL.md
```

It also creates or updates:

```text
$HOME\.codex\AGENTS.md
```

Existing files are backed up before modification.

## macOS/Linux

```bash
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
4. In a new workspace, ask Codex to run Smart Skill Preflight before work.
