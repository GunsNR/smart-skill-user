# Install For Repo-Level Codex

Use this when one repository needs its own team or project-specific Smart Skill Preflight workflow.

Repo-level install is best when the project has local rules, approval gates, active surfaces, or team conventions. It does not modify Codex internals; it gives Codex repo instructions through `AGENTS.md` and a repo-local skill.

## Steps

1. Copy:

```text
skills/smart-skill-user/SKILL.md
```

To:

```text
your-repo/.agents/skills/smart-skill-user/SKILL.md
```

2. Add the Smart Skill Preflight section from `templates/AGENTS.md` to:

```text
your-repo/AGENTS.md
```

3. Restart or refresh Codex for the repository.

4. Ask Codex to verify the install without editing product code.

## Copy-Paste Install Prompt

```text
Install Smart Skill User in this repo. Copy the skill to .agents/skills/smart-skill-user/SKILL.md, add Smart Skill Preflight as the first step in AGENTS.md, validate, and do not modify product code.
```

## Verification Prompt

```text
Before doing anything, list the instruction sources and skills you loaded. Then run Smart Skill Preflight for this task: update a mobile homepage hero. Do not edit files.
```

Expected result:

- Codex mentions Smart Skill Preflight or repo-level guidance.
- Codex confirms scope.
- Codex selects a relevant skill stack.
- Codex skips irrelevant skills.
- Codex edits no files.

## Recommended Repo Guidance

Keep the repo guidance specific:

- name the correct repository path or workspace root
- list active surfaces, such as frontend, backend, docs, or infrastructure
- identify approval gates for visual, cleanup, deploy, connector, and destructive work
- tell the agent to stop when scope is unclear
