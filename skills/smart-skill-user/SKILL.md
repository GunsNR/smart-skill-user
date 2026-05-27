---
name: smart-skill-user
description: Token-aware preflight router that automatically chooses the best skill or smallest effective skill stack before an AI coding agent starts work.
---

# Smart Skill User

Use this skill before an AI coding agent starts implementation, review, validation, cleanup, connector work, or release work. Its core behavior is to automatically choose the best skill or best skill stack before the AI coding agent starts work.

One skill when one is enough. A stack when the task needs more.

## Smart Skill Preflight

Begin every agent task with a concise preflight:

```text
Scope: <repo, project/client, branch if relevant, target page/service/module, or ask if unclear>
Task type: <one or more categories>
Selected route: <best single skill, or smallest effective skill stack>
Why this route: <short reason each selected skill belongs>
Skipped skills: <irrelevant skills skipped when helpful>
Approval needed: <yes/no and why>
Planned validation: <smallest checks that match the risk>
```

The preflight route is:

```text
Preflight -> scope -> task type -> best skill stack -> safer execution
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

## 3. Choose The Best Skill Or Skill Stack

Score available skills or instruction packs by relevance before loading them:

- direct match to task type
- target surface or file type
- risk and approval gates
- validation needs
- source-truth or privacy needs

Then choose the best route:

- Use the single best skill when the task is narrow.
- Use a minimal skill stack when the task is multi-part.
- Explain why the selected skill or stack was chosen.
- Explicitly skip irrelevant skills when the skip prevents wasted context or wrong-scope action.
- Avoid loading every skill.
- If a better skill becomes relevant during discovery, update the selection before continuing.

Skill selection rule:

- Use 1 skill for narrow tasks.
- Use 2-4 skills for multi-part tasks.
- Use more than 4 only when the task explicitly spans multiple domains.
- Never load every skill by default.

## 4. Apply The Selected Skill Stack

Apply the selected skill or skill stack as working constraints before work begins. Do not merely mention them.

Follow their safety rules, validation rules, and output expectations. If selected guidance conflicts, prefer scope safety, privacy, local-first work, and explicit approval gates.

## 5. Save Tokens

The always-on stack is active on every task — never re-list it in `Selected route`:

- `caveman` (lite) — terse bullet output, set by SessionStart hook
- `claude-mem` — compressed prior-session context (once installed)
- `claude-context` — semantic code search MCP (once installed)
- Subagent delegation — offload large reads/research to keep main context clean

On top of that, preserve context for the actual task:

- avoid broad file reads
- avoid loading all docs
- avoid repeating old chat history
- avoid rendering previews unless needed
- avoid external tools unless required
- use targeted searches and targeted file reads
- summarize validation instead of dumping logs
- delegate any read or search that returns more than ~200 lines to a subagent

For task → skill mapping, consult [`docs/skill-routing-matrix.md`](../../docs/skill-routing-matrix.md). It names the top-10 skills from [`docs/TOP_SKILLS.md`](../../docs/TOP_SKILLS.md) per task type.

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
- selected best skill or skill stack, with reasons
- skipped irrelevant skills, if important
- planned validation
- approval needed or not

Keep the preflight short. The goal is automatic skill routing, better execution quality, and fewer wasted tokens, not another long ritual.
