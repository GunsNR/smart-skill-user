# How It Works

Smart Skill User adds one lightweight step before implementation: automatically choose the best skill or smallest effective skill stack for the task.

1. Confirm scope.
2. Classify the task.
3. Score available skills by relevance.
4. Choose one skill when one is enough, or a stack when the task needs more.
5. Apply the selected skill stack as constraints.
6. Enforce approval gates.
7. Plan validation.

The preflight should be short. Its purpose is to route the agent to the right skills, not to create a second project plan.

```text
Preflight -> scope -> task type -> best skill stack -> safer execution
```

## Skill Selection Rule

- Use 1 skill for narrow tasks.
- Use 2-4 skills for multi-part tasks.
- Use more than 4 only when the task explicitly spans multiple domains.
- Never load every skill by default.

## Good Preflight

```text
Scope: repo confirmed, homepage hero, mobile breakpoint.
Task type: UI/CRO.
Selected skill stack: visual QA for layout; copy review for CTA.
Why this stack: mobile hero work needs visual execution and message fit.
Skipped skills: deployment, database.
Approval needed: preview before commit.
Planned validation: responsive screenshot and test suite.
```

## Bad Preflight

- loads every skill
- summarizes the whole repository
- repeats old chat history
- starts editing before confirming scope
- treats approval gates as optional
