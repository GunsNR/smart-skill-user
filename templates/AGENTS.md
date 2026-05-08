# AGENTS.md

## Smart Skill Preflight

At the start of every Codex prompt or session in this repository, run Smart Skill Preflight as the first instructed preflight step before implementation, review, validation, cleanup, connector use, or release work.

This repo-level guidance does not modify the Codex platform. It works through this repository's `AGENTS.md` plus `.agents/skills/smart-skill-user/SKILL.md`.

Begin with this concise report:

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
- choose the single best skill for narrow tasks, or the smallest effective skill stack for multi-part tasks
- skip irrelevant skills when skipping prevents wasted context or wrong-scope work
- stop and ask when scope is unclear
- do not load every skill, doc, or old conversation by default
- avoid unnecessary file reads, searches, renders, and tool calls
- use targeted searches and targeted file reads after the route is clear
- require explicit approval before deploy, publish, DNS, CRM, live connector, production connector, destructive cleanup, or revert work
- for visual/CRO work, preview or render first and ask for approval before commit
- for cleanup/revert work, create a backup patch before changing files
- never expose secrets or private data
- report the selected skill or skill stack concisely before implementation
