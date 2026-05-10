# Install For Claude Code

Smart Skill User works with Claude Code as a portable instruction pack. Copy the preflight workflow into your project `CLAUDE.md` and optionally install the skill for richer routing guidance.

---

## Quick Install (copy-paste prompt)

Open Claude Code in your project and paste:

```text
Install Smart Skill User in this repo. Copy the skill to .agents/skills/smart-skill-user/SKILL.md, add Smart Skill Preflight as the first step in CLAUDE.md, validate, and do not modify product code.
```

Claude Code will:

1. Create `.agents/skills/smart-skill-user/SKILL.md` with the full routing rules.
2. Add Smart Skill Preflight as the first section of your `CLAUDE.md`.
3. Validate without touching product code.

---

## Manual Install

### Step 1 — Copy the skill

Copy `skills/smart-skill-user/SKILL.md` to:

```text
your-repo/.agents/skills/smart-skill-user/SKILL.md
```

### Step 2 — Add the preflight to CLAUDE.md

Open or create `CLAUDE.md` at your project root and add:

```markdown
## Smart Skill Preflight

Before work, produce a brief preflight:

\`\`\`text
Scope: <repo, project/client, branch if relevant, target page/service/module, or ask if unclear>
Task type: <UI/CRO, SEO/schema, copy, media, connector, research, cleanup, deploy, validation, docs>
Selected route: <best single skill, or smallest effective skill stack>
Why this route: <short reason each selected skill belongs>
Skipped skills: <irrelevant skills skipped when helpful>
Approval needed: <yes/no and why>
Planned validation: <smallest checks that match the risk>
\`\`\`

Full routing rules: \`.agents/skills/smart-skill-user/SKILL.md\`

Use the selected skill stack as constraints. Do not read every document by default.
```

### Step 3 — Validate

Ask Claude Code to verify the install without editing product code:

```text
Before doing anything, list the instruction sources and skills you loaded.
Then run Smart Skill Preflight for this task: update a mobile homepage hero.
Do not edit files.
```

Expected result:

- Claude Code runs a preflight and reports scope, task type, selected route, and approval gates.
- Claude Code does not edit any files.

---

## What You Get

Before every task, Claude Code will confirm:

- **Scope** — repo, client, branch, and target surface
- **Task type** — UI, SEO, copy, media, connector, research, cleanup, deploy, validation, or docs
- **Selected route** — the single best skill, or the smallest effective skill stack
- **Approval gates** — preview, backup patch, deploy approval, or secret-safety rules
- **Planned validation** — the smallest checks that match the risk

---

## Recommended Use

Smart Skill User is most useful when your project has:

- Multiple instruction sets, skills, or client notes
- Visual, cleanup, connector, or deploy approval gates
- A risk of wrong-scope edits across repos or clients

For simpler single-purpose projects, the preflight block in `CLAUDE.md` alone is enough.

---

## See Also

- [Repo-level Codex install](codex-repo.md)
- [Global Codex install](codex-global.md)
- [Generic AGENTS.md install](generic-agents-md.md)
- [skills.sh / npx skills install](../docs/SKILLS_SH_INSTALL.md)
