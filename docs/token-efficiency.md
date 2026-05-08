# Token Efficiency

Smart Skill User is token-aware because it delays context spending until the task is understood.

## Principles

- Read the routing instruction first.
- Confirm scope before reading implementation files.
- Use skill names and summaries before full skill docs.
- Prefer targeted search over broad browsing.
- Avoid repeating old conversation history.
- Avoid previews, renders, or live tools unless they answer the task.

## Not The Goal

The goal is not to starve the agent of context. The goal is to load the right context at the right time.

## Practical Model

```text
small preflight -> targeted reads -> selected skills -> focused implementation -> bounded validation
```

This usually produces better work than:

```text
load all docs -> inspect unrelated files -> guess scope -> edit -> discover approval problem late
```
