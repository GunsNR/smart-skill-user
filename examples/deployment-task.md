# Example: Deployment Task

## User Prompt

> Deploy the current site.

## Smart Skill Preflight

```text
Scope: confirm repo, branch, hosting target, environment, and release intent.
Task type: deploy/release and validation.
Selected skill stack: release workflow; hosting provider guidance if relevant; CI validation.
Why this stack: deployment spans release intent, hosting behavior, and CI confidence.
Skipped skills: UI design unless the deploy includes visual changes.
Approval needed: yes, explicit deployment approval required.
Planned validation: status check, tests, build, and deploy dry run if available.
```

## Guardrails

- Do not deploy from an unclear branch.
- Do not modify DNS, production settings, credentials, or live connectors without explicit approval.
- Do not push or publish unless the user approves.
