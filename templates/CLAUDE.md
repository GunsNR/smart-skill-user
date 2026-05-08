# CLAUDE.md

## Smart Skill Preflight

Before work, produce a brief preflight:

```text
Scope: <repo, project/client, branch if relevant, target page/service/module, or ask if unclear>
Task type: <UI/CRO, SEO/schema, copy, media, connector, research, cleanup, deploy, validation, docs>
Selected instructions: <1-4 relevant docs/skills/rules with reasons>
Skipped instructions: <important skips only>
Approval needed: <yes/no and why>
Planned validation: <smallest checks that match the risk>
```

Use the selected instructions as constraints. Do not read every document by default.

Approval gates:

- visual/CRO: preview before commit
- deploy/publish/DNS/CRM: explicit approval
- cleanup/revert/destructive work: backup patch or explicit approval as appropriate
- secrets/private data: never expose
- unclear scope: stop and ask
