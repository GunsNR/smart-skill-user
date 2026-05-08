# Install For Repo-Level Codex

Use this when one repository needs its own preflight workflow.

## Steps

1. Copy `skills/smart-skill-user/` to:

```text
.agents/skills/smart-skill-user/
```

2. Add the content from `templates/AGENTS.md` to the repository `AGENTS.md`.

3. Ask Codex to run Smart Skill Preflight before implementation, review, validation, cleanup, connector work, or release work.

## Recommended Repo Guidance

Keep the repo guidance specific:

- name the correct repository path or workspace root
- list active surfaces, such as frontend, backend, docs, or infrastructure
- identify approval gates for visual, cleanup, deploy, connector, and destructive work
- tell the agent to stop when scope is unclear
