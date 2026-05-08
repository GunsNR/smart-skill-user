# Token Efficiency

Smart Skill User is token-aware because it delays context spending until the task is understood and then automatically chooses the best skill or smallest effective skill stack.

Automatic does not mean "load everything." It means Codex is instructed to run a short preflight first, then load only the smallest useful context for the actual task.

## Principles

- Run a short preflight every task.
- Read the routing instruction first.
- Confirm scope before reading implementation files.
- Score skill names and summaries before loading full skill docs.
- Choose one skill when one is enough, or a 2-4 skill stack when the task needs more.
- Avoid loading every skill.
- Prefer targeted search over broad browsing.
- Avoid re-reading docs unnecessarily.
- Avoid broad research unless asked.
- Avoid preview/render unless visual QA is needed.
- Avoid repeating old conversation history.
- Avoid previews, renders, or live tools unless they answer the task.

## Not The Goal

The goal is not to starve the agent of context. The goal is to load the right context at the right time: best skill first, skill stack only when needed.

## Practical Model

```text
small preflight -> score skills -> best skill stack -> targeted reads -> focused implementation -> bounded validation
```

This usually produces better work than:

```text
load all docs -> inspect unrelated files -> guess scope -> edit -> discover approval problem late
```
