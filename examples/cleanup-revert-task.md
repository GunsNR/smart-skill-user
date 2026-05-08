# Example: Cleanup Or Revert Task

## User Prompt

> Clean up the old generated files and revert the broken homepage change.

## Smart Skill Preflight

```text
Scope: confirm repo, branch, files to clean, and exact change to revert.
Task type: cleanup/revert/debugging and validation.
Selected skills: review-output for risk review; validation workflow for test selection.
Skipped skills: visual design unless UI output is affected.
Approval needed: yes, backup patch before destructive cleanup.
Planned validation: inspect diff, run targeted tests, and check no unrelated files were removed.
```

## Guardrails

- Create a backup patch first.
- Do not run destructive commands without explicit approval.
- Do not revert unrelated user changes.
