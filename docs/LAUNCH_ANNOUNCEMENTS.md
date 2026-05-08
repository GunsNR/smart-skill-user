# Launch Announcements

Ready-to-post announcement templates and distribution guidance for Smart Skill User.

---

## X / Twitter Threads

### Thread 1: Problem → Solution → Call to Action

**Tweet 1**
```
Stop loading every instruction into your AI coding agent.

Smart Skill User is a tiny preflight workflow for Codex, Claude Code, and AGENTS.md agents: 
confirm scope, classify the task, automatically choose the best skill or minimal skill stack, 
and enforce approval gates before editing.

It's open source, MIT licensed, and built for teams that want less context waste and fewer 
wrong-scope edits.

https://github.com/GunsNR/smart-skill-user
```

**Tweet 2**
```
The problem: agents load unrelated backend docs, deployment notes, database schemas, and old 
client context before touching the actual task.

Token waste. Wrong scope. Longer execution. Stale guidance.

Sound familiar?
```

**Tweet 3**
```
The fix: run a 30-second preflight before the agent starts.

✓ Confirm: repo, project, branch, target page/service
✓ Identify: task type (UI, SEO, copy, deploy, cleanup, etc.)
✓ Select: the best single skill or smallest effective skill stack
✓ Enforce: approval gates (preview, backup, explicit approval)
```

**Tweet 4**
```
Supports:
• Codex global install
• Codex repo-level install  
• Claude Code portable instructions
• Generic AGENTS.md workflows

Includes: routing matrix, examples, safety rules, token-efficiency docs, and tests.
```

**Tweet 5**
```
Open source, MIT licensed, zero monetization.

Try it: https://github.com/GunsNR/smart-skill-user

Feedback welcome, especially from people running multi-project AI agent setups.
```

---

### Thread 2: Quick & Casual

**Tweet 1**
```
Just released Smart Skill User: a preflight router for AI coding agents.

Think of it as a "confirm scope → pick the right tool → start working" workflow before your 
Codex or Claude Code agent touches a file.

Fewer wrong edits. Less token waste. https://github.com/GunsNR/smart-skill-user
```

**Tweet 2**
```
Why this exists:
- Agents often load docs unrelated to the task
- Context bloat → slower execution
- Wrong scope = wrong edits
- Token costs add up fast

Smart Skill User asks agents to pause and route correctly before starting.
```

**Tweet 3**
```
Works with: Codex, Claude Code, any AGENTS.md-compatible agent

What's included: 1 skill, 4 install methods, routing matrix, examples, safety rules, validation tests

Open source, MIT licensed, no ads, no paywalls.

https://github.com/GunsNR/smart-skill-user
```

---

### Thread 3: Technical Deep Dive

**Tweet 1**
```
Building a token-aware preflight router for AI coding agents.

Smart Skill User automatically selects the best skill or smallest effective skill stack before 
agents start work. It's now available for Codex, Claude Code, and generic AGENTS.md workflows.

https://github.com/GunsNR/smart-skill-user
```

**Tweet 2**
```
Architecture:
1. Confirm working scope (repo, project, branch, target page/service/module)
2. Classify task type (UI/CRO, SEO, copy, media, connector, cleanup, deploy, validation, docs)
3. Score available skills by relevance, risk, and validation needs
4. Auto-select best single skill or minimal effective stack
5. Apply skill constraints + approval gates + validation rules
```

**Tweet 3**
```
Safety model:

Visual/CRO work → preview before commit
Deploy/publish → explicit approval required
Cleanup/revert → backup patch first
Secrets/private data → never expose
Unclear scope → stop and ask

Approval gates + validation = fewer surprises.
```

**Tweet 4**
```
Token efficiency:

Goal: spend context only after understanding the task.

Facts:
- Short preflight on every task
- Targeted searches over broad file reads
- Best skill stack over every skill doc
- Avoid broad research unless asked
- Skip preview/render unless visual QA needed
```

**Tweet 5**
```
What's in the box:
- 1 focused skill for preflight routing
- Install templates (Codex global/repo, Claude, generic AGENTS.md)
- Routing matrix (task type → skill stack)
- Real-world examples
- Safety and approval gate rules
- Token efficiency docs
- Python validation + pytest suite

MIT licensed, open source, no dependencies.

https://github.com/GunsNR/smart-skill-user
```

---

## LinkedIn Post

**Full Post**

Smart Skill User: A Lightweight Preflight Router for AI Coding Agents

AI coding agents need better first steps.

I've built Smart Skill User, an open-source preflight workflow for Codex, Claude Code, and AGENTS.md-compatible agents. It helps agents confirm scope, classify tasks, automatically select the best skill or minimal skill stack, and enforce approval gates before editing code.

**The Problem**

If you're managing AI coding agents across multiple projects, you've probably noticed:
- Agents load instructions unrelated to the current task
- Context bloat slows down execution and wastes tokens
- Wrong-scope edits are easier when scope isn't confirmed upfront
- Teams need consistent routing rules across different task types

**The Solution**

A 30-second preflight that asks agents to:

1. Confirm scope: What repo, project, branch, and target page/service?
2. Identify task type: Is this UI work, SEO, copy, media, cleanup, deployment, or something else?
3. Automatically select the best skill or minimal skill stack
4. Enforce approval gates: Does this need preview, backup, or explicit approval?
5. Validate and report: Did we accomplish the goal safely?

**What's Included**
- One focused skill for Codex and AGENTS.md workflows
- Installation templates for global and repo-level Codex setup
- Claude Code portable instruction templates
- Full routing matrix (task type → skill recommendations)
- Real-world examples (mobile UI, SEO, media, cleanup, deployment, etc.)
- Safety and approval gate documentation
- Token-efficiency principles and validation rules
- Open-source tests and validation scripts

**Why It Matters**
- Less context waste: spend tokens after understanding the task
- Fewer wrong-scope edits: confirm repo, project, branch, target page
- Faster execution: agents focus on relevant skills
- Consistent routing: all agents use the same skill matrix
- Explicit approval gates: reduce risk for deploy, publish, and destructive work

**Who Should Use It**
- Teams running Codex, Claude Code, or AGENTS.md agents
- Multi-project repositories with shared agent workflows
- Organizations managing AI coding across different scopes and task types
- Anyone concerned about token efficiency and agent safety

**Technical Details**
- Open source, MIT licensed
- Python + shell scripts for installation and validation
- No external dependencies
- Works with Codex (global and repo-level), Claude Code, and generic AGENTS.md
- Intentionally small: ~500 lines total

**Get Started**
- Repository: https://github.com/GunsNR/smart-skill-user
- Quick start: https://github.com/GunsNR/smart-skill-user/blob/master/docs/INSTALL_QUICK_START.md
- Documentation: https://github.com/GunsNR/smart-skill-user/blob/master/README.md

Feedback welcome, especially from people maintaining multi-project AI coding setups.

---

## Reddit / Hacker News Post

**Title:** Smart Skill User – A Token-Aware Preflight Router for AI Coding Agents

**Body**

I built an open-source tool called Smart Skill User. It's a preflight workflow for Codex, Claude Code, and AGENTS.md-compatible agents that automatically routes tasks to the best skill before agents start work.

**The Problem**

Agents often load too many instructions at once:
- Unrelated backend docs, database schemas, deployment notes
- Old client context that isn't relevant to this task
- Token waste from loading irrelevant skills
- Higher chance of wrong-scope edits
- Slower execution

**The Solution**

A 30-second preflight that asks agents to:

1. Confirm scope (repo, project, branch, target page/service)
2. Classify task type (UI, SEO, copy, media, cleanup, deploy, etc.)
3. Auto-select the best single skill or minimal skill stack
4. Enforce approval gates (preview, backup, explicit approval)
5. Validate and report

**What's Included**
- One focused skill for routing
- Install templates for Codex (global and repo-level), Claude Code, and generic AGENTS.md
- Full routing matrix for common task types
- Real-world examples (mobile UI, SEO, media, cleanup, deployment, etc.)
- Safety and approval gate rules
- Token-efficiency documentation
- Python validation scripts and pytest suite

**Why This Matters**
- Less context waste (spend tokens only after understanding the task)
- Fewer wrong-scope edits (confirm scope before starting)
- Faster execution (agents focus on relevant docs)
- Consistent safety rules across all agents

**Technical Details**
- Open source, MIT licensed
- Zero external dependencies
- ~500 lines total
- Works with Codex, Claude Code, and any agent that reads AGENTS.md

**Try It**

https://github.com/GunsNR/smart-skill-user

Feedback welcome, especially from people maintaining multi-project AI coding setups.

---

## Email / Newsletter Announcement

**Subject Line:** New Tool: Smart Skill Preflight Router for AI Coding Agents

**Body**

Hi [Recipient],

I wanted to share a new open-source tool I built: Smart Skill User.

If you're managing AI coding agents (Codex, Claude Code, or similar) across multiple projects, you've probably noticed they often load instructions unrelated to the current task. This wastes tokens, slows down execution, and increases the chance of wrong-scope edits.

Smart Skill User fixes this by adding a 30-second preflight step that asks agents to:

1. Confirm scope (repo, project, branch, target page/service)
2. Identify task type (UI, SEO, copy, media, cleanup, deploy, etc.)
3. Automatically select the best skill or minimal skill stack
4. Enforce approval gates (preview, backup patch, explicit approval)

The preflight reduces token waste, catches scope issues early, and makes agent edits safer.

It's open source, MIT licensed, and built for teams like yours.

**What's Included**
- Installation for Codex (global + repo-level), Claude Code, and generic AGENTS.md
- Routing matrix for common task types
- Real-world examples
- Safety and approval gate rules
- Validation scripts and tests

**Get Started**
- Repository: https://github.com/GunsNR/smart-skill-user
- Quick Start: https://github.com/GunsNR/smart-skill-user/blob/master/docs/INSTALL_QUICK_START.md
- Full Docs: https://github.com/GunsNR/smart-skill-user/blob/master/README.md

I'd love your feedback, especially if you're running multi-project AI agent setups.

Best,
[Your Name]

---

## Slack / Discord Community Announcement

**Channel:** #announcements or #tools

**Message**

:rocket: New open-source tool: Smart Skill User

A preflight router for Codex, Claude Code, and AGENTS.md agents. It automatically selects the best skill before agents start work.

**Why it helps:**
- Agents confirm scope before editing (catches wrong-scope issues early)
- Automatically selects relevant skills (reduces token waste)
- Enforces approval gates (reduces risky edits)
- Works with Codex global, repo-level, and Claude Code setup

**Get Started:**
GitHub: https://github.com/GunsNR/smart-skill-user
Docs: https://github.com/GunsNR/smart-skill-user/blob/master/docs/INSTALL_QUICK_START.md

Open source, MIT licensed. Feedback welcome!

---

## Mastodon / Bluesky Post

Stop loading every instruction into your AI coding agent.

Smart Skill User is a tiny preflight workflow for Codex, Claude Code, and AGENTS.md agents. Before your agent starts work, it confirms scope, classifies the task, and automatically chooses the best skill or minimal skill stack.

Open source, MIT licensed.

https://github.com/GunsNR/smart-skill-user

---

## Product Hunt Post (Optional)

**Title:** Smart Skill User – Reduce AI Agent Token Waste with Intelligent Skill Routing

**Tagline:** A preflight router that automatically selects the best skill before your AI coding agent starts work.

**Description**

Stop loading every instruction into your AI coding agent.

Smart Skill User is a lightweight preflight workflow for Codex, Claude Code, and AGENTS.md-style agents. Before your agent touches a file, it:

1. Confirms scope (repo, project, branch, target page/service)
2. Classifies the task (UI, SEO, copy, media, cleanup, deploy, etc.)
3. Automatically selects the best skill or minimal skill stack
4. Enforces approval gates (preview, backup, explicit approval)
5. Validates and reports

**Why People Love It**
- Reduces token waste by focusing on relevant skills
- Catches scope issues before agents make wrong edits
- Works with Codex (global and repo-level), Claude Code, and any AGENTS.md agent
- Open source, MIT licensed
- Tiny, focused, intentional design

**What's Included**
- One focused routing skill
- Install templates for 4 different agent setups
- Full routing matrix and real-world examples
- Safety rules and approval gates
- Validation scripts and pytest suite

Get started: https://github.com/GunsNR/smart-skill-user

---

## Distribution Timeline & Tips

**Phase 1: Soft Launch (Day 1)**
- Share with early beta testers
- Post in relevant Discord/Slack communities
- Email to close collaborators
- Gather initial feedback

**Phase 2: Public Launch (Day 2–3)**
- Post to X (multiple tweets, then thread daily for 3–5 days)
- Post LinkedIn article
- Post to Reddit and Hacker News
- Share with relevant mailing lists and communities

**Phase 3: Sustained Engagement (Week 2+)**
- Share real-world examples and use cases
- Write a blog post about token efficiency and agent safety
- Monitor issues and respond quickly
- Share community feedback and contributions

**Timing Tips**
- Launch on a weekday morning (8–10 AM your timezone)
- Post to X in waves: first announcement, then 1–2 follow-ups per day
- Space out LinkedIn, Reddit, and Hacker News by 1–2 hours
- Re-post to the same communities after 1 week (different angle)

**Customization**
- Add your name, contact info, or GitHub profile link
- Include your own examples or use cases if you have them
- Adjust tone for each platform (technical for HN, more casual for Twitter)
- Link to your blog or website if applicable
- Use your own social media handles and links

---

## Copy Summary

| Platform | Best For | Tone | Length |
| --- | --- | --- | --- |
| X/Twitter | Quick discovery, engagement | Casual, punchy | 280 chars per tweet |
| LinkedIn | Professional reach, credibility | Professional, thoughtful | 1–3 paragraphs |
| Reddit/HN | Technical audience, deep discussion | Honest, straightforward | 2–3 paragraphs |
| Email | Direct outreach, relationship building | Friendly, informative | 2–3 paragraphs |
| Slack/Discord | Community members, team updates | Casual, brief | 1–2 paragraphs |
| Mastodon/Bluesky | Fediverse communities | Concise, friendly | 1–2 paragraphs |

---

## Key Messages (Use These Everywhere)

- "Stop loading every instruction into your AI agent."
- "Confirm scope, classify the task, automatically select the best skill."
- "Less context waste. Fewer wrong-scope edits. Faster execution."
- "Open source, MIT licensed, zero monetization."
- "Works with Codex, Claude Code, and AGENTS.md agents."

---

**Questions?** See [LAUNCH_COPY.md](LAUNCH_COPY.md) for more copy and [SUPPORT.md](../SUPPORT.md) for help.
