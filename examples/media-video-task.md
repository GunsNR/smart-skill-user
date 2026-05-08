# Example: Media And Video Task

## User Prompt

> Add the new homepage background video and make sure mobile has a fallback.

## Smart Skill Preflight

```text
Scope: confirm repo, page, asset source, licensing, and mobile behavior.
Task type: media/video/assets and UI validation.
Selected skill stack: media asset extraction for formats and poster image; visual QA for responsive behavior.
Why this stack: video work needs asset handling plus visual fallback checks.
Skipped skills: database, deploy, CRM.
Approval needed: preview before commit.
Planned validation: local preview, poster fallback check, reduced-motion behavior if supported.
```

## Guardrails

- Do not hotlink private or third-party assets without permission.
- Provide a poster or static fallback.
- Keep media optional and bounded; do not make live capture mandatory.
