<!-- smart-skill-user:start -->
# Global Codex Guidance

## Smart Skill Preflight

Before implementing any user request, run Smart Skill Preflight.

This is user-level instruction guidance, not a hook into Codex internals.

1. Confirm repo/project/client scope.
2. Identify the task type.
3. Choose the single best skill or smallest effective skill stack.
4. Do not load every skill by default.
5. Skip irrelevant skills.
6. Keep token usage low with targeted file reads and targeted searches.
7. Ask before editing if scope is unclear.
8. Require explicit approval before deploy, publish, DNS, CRM/live connector changes, destructive cleanup, or production-impacting work.
9. For visual/CRO work, preview/render and ask for approval before commit.
10. For cleanup/revert work, create a backup patch first.

Approval gates apply before risky actions.

Report briefly:

- scope
- selected skill or skill stack
- skipped skills if important
- approval needed or not
<!-- smart-skill-user:end -->
