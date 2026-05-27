# Top 10 Skills (May 2026)

Curated reference list of the absolute best Claude / Claude Code skills to add on top of Smart Skill User. Selected for a solo operator working on SEO, marketing, AI learning, and token-efficient workflows.

To install all of them on a machine, run:

```bash
bash scripts/install-top-skills.sh
```

See [`install/top-skills.md`](../install/top-skills.md) for full details and the manual paste-block for `/plugin` commands.

---

## Token-Saving

### 1. `juliusbrussee/caveman`

- Source: <https://www.skills.sh/juliusbrussee/caveman/caveman>
- One-line: cuts agent output verbosity ~75% without losing substance; toggle with "stop caveman".
- Why: single biggest per-session token win on the marketplace. Stacks on top of every other skill.

### 2. `thedotmack/claude-mem`

- Source: <https://github.com/thedotmack/claude-mem>
- One-line: compresses session transcripts to SQLite + FTS5 and injects an index at SessionStart.
- Why: eliminates the "re-explain the project" tax on every new session.

### 3. `zilliztech/claude-context`

- Source: <https://github.com/zilliztech/claude-context>
- One-line: MCP server providing semantic code search via AST chunking + Milvus hybrid retrieval.
- Why: benchmarked ~40% token reduction vs grep-only workflows on large repos.

---

## SEO and Marketing

### 4. `anthropics/knowledge-work-plugins → marketing`

- Source: <https://github.com/anthropics/knowledge-work-plugins/tree/main/marketing>
- One-line: official Anthropic marketing plugin — `/draft-content`, `/campaign-plan`, `/brand-review`, `/competitive-brief`, `/performance-report`, `/seo-audit`, `/email-sequence`.
- Why: first-party baseline with enforced brand-voice config.

### 5. `coreyhaines31/marketingskills`

- Source: <https://github.com/coreyhaines31/marketingskills>
- One-line: 32 marketing skills covering the full funnel (SEO audits, programmatic SEO, CRO, ad creative, cold email, sequences, competitor profiling, schema, AI-SEO).
- Why: shared `product-marketing-context` keeps brand voice consistent across every output.

### 6. `AgriciDaniel/claude-seo`

- Source: <https://github.com/AgriciDaniel/claude-seo>
- One-line: deepest technical SEO suite — 25 sub-skills, 18 specialist agents, parallel execution.
- Why: Core Web Vitals, hreflang, JSON-LD, AI-Overview eligibility, GEO citability; native Ahrefs MCP + GSC URL Inspection integration.

### 7. SurgeGraph Claude Code Skill

- Source: <https://surgegraph.io>
- One-line: scores pages for ChatGPT / Perplexity / Gemini / AI-Mode citation readiness and tracks LLM share-of-voice.
- Why: closes the one gap Ahrefs, Semrush, and GSC cannot see — AI-search visibility.

---

## Karpathy / AI Learning

### 8. `karpathy/nanochat → read-arxiv-paper`

- Source: <https://github.com/karpathy/nanochat/blob/master/.claude/skills/read-arxiv-paper/SKILL.md>
- One-line: downloads arXiv LaTeX source, summarizes the paper, ties findings back to your codebase.
- Why: the only Claude Code skill Karpathy himself ships — live proof of his workflow.

### 9. `multica-ai/andrej-karpathy-skills`

- Source: <https://github.com/multica-ai/andrej-karpathy-skills>
- One-line: Karpathy's anti-pitfall principles distilled into a single CLAUDE.md guardrail.
- Why: think-before-coding, simplicity-first, surgical-changes, goal-driven execution — token-light by design.

---

## Methodology

### 10. `obra/superpowers`

- Source: <https://github.com/obra/superpowers>
- One-line: 7-phase TDD methodology, subagent orchestration, plan-before-code workflow.
- Why: the most production-proven community framework; plan-first prevents wasted agent loops.

---

## Honorable Mentions (skipped from top 10)

| Skill | Why not in top 10 |
|---|---|
| `uditgoenka/autoresearch` | Overlaps your existing `auto-research-loop`. |
| `kfchou/wiki-skills` | Excellent for knowledge bases, but niche. |
| `aaron-he-zhu/seo-geo-claude-skills` | Largely covered by #5 + #6. |
| `anthropics/skills → skill-creator` | Install when you start packaging your own SOPs. |
| `hesreallyhim/awesome-claude-code` | Bookmark for ongoing discovery, not a skill. |

---

## Honest Gaps

- **No LLM-internals teaching skill** exists on Skills.sh or as a verified Claude Code skill. For transformers / nanoGPT walkthroughs you still want Karpathy's YouTube + repos directly.
- **No mature open-source AI brand-mention tracker** besides SurgeGraph — every other option is paid SaaS.
- **Karpathy has not published a Zero-to-Hero skill suite**; the items above are the closest verified equivalents.

---

## Composition Notes

These skills compose well with the Smart Skill User preflight router:

- The preflight in `skills/smart-skill-user/SKILL.md` runs first.
- `caveman` then constrains output length on the final reply.
- `claude-mem` injects compressed prior-session context at SessionStart.
- The selected route from the preflight loads only the relevant SEO / marketing / Karpathy skill subset, so installed-but-idle skills stay near-zero token cost (~100 tokens for name + description until invoked).

Approval gates from your repo's `CLAUDE.md` still apply: nothing here authorizes deploys, pushes, releases, or copied external code without explicit maintainer approval.
