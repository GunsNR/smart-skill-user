---
name: smart-skill-user
description: Token-aware preflight router that selects the smallest relevant skill set before an AI coding agent starts work.
---

# Smart Skill User

Use this skill before an AI coding agent starts implementation, review, validation, cleanup, connector work, or release work.

## Smart Skill Preflight

Begin every agent task with a concise preflight:

```text
Scope: <repo, project/client, branch if relevant, target page/service/module, or ask if unclear>
Task type: <one or more categories>
Selected skills: <1-4 skills or instruction packs, with a short reason for each>
Skipped skills: <important skips only>
Approval needed: <yes/no and why>
Planned validation: <smallest checks that match the risk>
```

## 1. Confirm Scope

Confirm:

- repo
- project or client
- branch, when relevant
- target page, service, module, file, or output surface

Stop and ask if scope is unclear, multiple repos are mentioned, or the request could affect the wrong project.

## 2. Identify Task Type

Classify the request into the smallest useful set:

- UI/design/CRO
- SEO/metadata/schema
- copy/local SEO
- media/video/assets
- connector/tool usage
- research/source-truth
- cleanup/revert/debugging
- deploy/release
- tests/validation
- docs only

## 3. Select The Smallest Relevant Skill Set

Choose usually 1-4 skills or instruction packs.

- Do not load every skill.
- Summarize why each selected skill is needed.
- Skip irrelevant skills explicitly only when the skip prevents wasted work or wrong-scope action.
- If a better skill becomes relevant during discovery, update the selection before continuing.

## 4. Apply Selected Skills

Use selected skills as working constraints. Do not merely mention them.

Follow their safety rules, validation rules, and output expectations. If selected guidance conflicts, prefer scope safety, privacy, local-first work, and explicit approval gates.

## 5. Save Tokens

Preserve context for the actual task:

- avoid broad file reads
- avoid loading all docs
- avoid repeating old chat history
- avoid rendering previews unless needed
- avoid external tools unless required
- use targeted searches and targeted file reads
- summarize validation instead of dumping logs

## 6. Enforce Approval Gates

Require the right gate before risky action:

- visual/CRO work: preview before commit
- deploy/publish/DNS/CRM: explicit approval
- cleanup/revert: backup patch first
- destructive changes: explicit approval
- secrets/private data: never expose
- unclear scope: stop and ask

## 7. Report Concisely

Report only what helps the user decide what happens next:

- scope confirmed
- selected skills
- skipped skills, if important
- planned validation
- approval needed or not

Keep the preflight short. The goal is better routing, not another long ritual.
