# How It Works

Smart Skill User adds one lightweight step before implementation.

1. Confirm scope.
2. Classify the task.
3. Select only relevant skills or instruction packs.
4. Apply those skills as constraints.
5. Enforce approval gates.
6. Plan validation.

The preflight should be short. Its purpose is to route the agent, not to create a second project plan.

## Good Preflight

```text
Scope: repo confirmed, homepage hero, mobile breakpoint.
Task type: UI/CRO.
Selected skills: visual QA for layout; copy review for CTA.
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
