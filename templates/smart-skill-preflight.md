# Smart Skill Preflight

Begin every agent task by reporting:

```text
Scope: <repo, project/client, branch if relevant, target page/service/module, or ask if unclear>
Task type: <UI/CRO, SEO/schema, copy, media, connector, research, cleanup, deploy, validation, docs>
Selected skills: <1-4 relevant skills or instructions with reasons>
Skipped skills: <important skips only>
Approval needed: <yes/no and why>
Planned validation: <smallest checks that match the risk>
```

Rules:

- confirm scope before editing
- ask when scope is unclear
- do not load every skill, doc, or old conversation
- use targeted searches and file reads
- preview visual/CRO work before commit
- create a backup patch before cleanup or revert work
- require explicit approval before deploy, publish, DNS, CRM, connector, or destructive actions
- never expose secrets or private data
