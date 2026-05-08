# AGENTS.md

## Smart Skill Preflight

Before implementation, review, validation, cleanup, connector use, or release work:

```text
Scope: <repo, project/client, branch if relevant, target page/service/module, or ask if unclear>
Task type: <UI/CRO, SEO/schema, copy, media, connector, research, cleanup, deploy, validation, docs>
Selected skills: <1-4 relevant skills with reasons>
Skipped skills: <important skips only>
Approval needed: <yes/no and why>
Planned validation: <smallest checks that match the risk>
```

Rules:

- confirm repo path before editing
- stop and ask when scope is unclear
- do not load every skill or doc
- use targeted searches and targeted file reads
- require preview before committing visual/CRO work
- require backup patch before cleanup/revert work
- require explicit approval before deploy, publish, DNS, CRM, connector, or destructive work
- never expose secrets or private data
