# Example: SEO Schema Task

## User Prompt

> Add local business schema to the service page.

## Smart Skill Preflight

```text
Scope: confirm repo, business, service page, and source of truth for name, address, service area, and claims.
Task type: SEO/metadata/schema and source-truth.
Selected skill stack: SEO/schema for structured data; source-truth audit for factual claims; copy review only if page text changes.
Why this stack: schema work needs structured-data rules and source verification; copy review is conditional.
Skipped skills: deployment and media.
Approval needed: no deploy approval unless publishing is requested.
Planned validation: schema linting, tests if present, and diff review for factual claims.
```

## Guardrails

- Do not invent ratings, certifications, prices, or service areas.
- Do not add fake claims.
- Prefer sourced facts already present in the repo or approved by the user.
