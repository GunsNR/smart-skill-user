# FAQ

## Is this an official OpenAI package?

No. Smart Skill User is an independent open-source instruction workflow.

## Does it replace tests or code review?

No. It helps route the agent before work starts. Tests and review still matter.

## Does it hook into Codex internals?

No. Smart Skill User uses supported instruction locations: user-level `$HOME/.codex/AGENTS.md`, user-level `$HOME/.agents/skills`, repo `AGENTS.md`, and repo `.agents/skills`.

## Can it run first on every Codex task?

As much as Codex follows user-level instructions, yes. The global install tells Codex to run Smart Skill Preflight before implementing each user request. The practical outcome is "first instructed preflight step," not a platform-level hook.

## How do I verify the global install?

Paste this into a new Codex session:

```text
Before doing anything, list the instruction sources and skills you loaded. Then run Smart Skill Preflight for this task: update a mobile homepage hero. Do not edit files.
```

Codex should mention Smart Skill Preflight or global/user-level guidance, confirm scope, select a relevant skill stack, skip irrelevant skills, and edit no files.

## Does it guarantee lower token usage?

No. It encourages more intentional context use, but actual usage depends on the agent, task, and repository.

## Can I rename the skill?

Yes, but keep the folder name, front matter, and install docs consistent.

## Should every task use the same skill stack?

No. That is the point. The agent should choose the best single skill for narrow tasks and the smallest effective skill stack for multi-part tasks.

## Can I use this in private repos?

Yes. Keep private details in your private repo guidance, not in this public package.
