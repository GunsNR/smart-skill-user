# Smart Skill Preflight

Begin every agent task by reporting:

```text
Scope: <repo, project/client, branch if relevant, target page/service/module, or ask if unclear>
Task type: <UI/CRO, SEO/schema, copy, media, connector, research, cleanup, deploy, validation, docs>
Selected route: <best single skill, or smallest effective skill stack>
Why this route: <short reason each selected skill belongs>
Skipped skills: <irrelevant skills skipped when helpful>
Approval needed: <yes/no and why>
Planned validation: <smallest checks that match the risk>
```

Rules:

- confirm scope before editing
- classify the task before loading task-specific docs
- score available skills by relevance
- use 1 skill for narrow tasks
- use 2-4 skills for multi-part tasks
- use more than 4 only when the task explicitly spans multiple domains
- ask when scope is unclear
- do not load every skill, doc, or old conversation
- apply the selected skill or skill stack as constraints before work begins
- use targeted searches and file reads
- preview visual/CRO work before commit
- create a backup patch before cleanup or revert work
- require explicit approval before deploy, publish, DNS, CRM, connector, or destructive actions
- never expose secrets or private data
