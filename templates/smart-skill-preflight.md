# Smart Skill Preflight

Begin every Codex prompt or agent task by running Smart Skill Preflight as the first instructed preflight step. Report:

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

- confirm repo, project/client, and target scope before editing
- identify the task type before choosing tools or reading files
- score available skills by relevance, risk, and validation needs
- choose the single best skill for narrow tasks
- choose the smallest effective skill stack for multi-part tasks, usually 2-4 skills
- use more than 4 only when the task explicitly spans multiple domains
- ask when scope is unclear
- do not load every skill, doc, or old conversation
- avoid unnecessary file reads, searches, renders, and tool calls
- apply the selected skill or skill stack as constraints before work begins
- use targeted searches and file reads
- require explicit approval before deploy, publish, DNS, CRM, live connector, production connector, destructive cleanup, or revert work
- for visual/CRO work, preview or render first and ask for approval before commit
- for cleanup/revert work, create a backup patch before changing files
- never expose secrets or private data
- report the selected skill or skill stack concisely before implementation
