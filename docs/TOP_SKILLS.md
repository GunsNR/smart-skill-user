# Top 13 Skills (May 2026)

Curated reference list of the absolute best Claude / Claude Code skills to add on top of Smart Skill User. Selected for a solo operator working on SEO, marketing, AI learning, and token-efficient workflows. Entries 1-10 are the foundational stack; entries 11-13 are May 2026 trending additions verified active in the past 30 days.

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

## May 2026 Trending Additions

Skills with verified shipping activity April 26 - May 26, 2026. Each is graded A on novelty vs entries 1-10, maintenance, and fit. A fourth candidate (`eugeniughelbur/obsidian-second-brain`) was demoted to honorable mentions after Snyk flagged Critical Risk during install — see below.

### 11. `safishamsi/graphify`

- Source: <https://github.com/safishamsi/graphify> ([releases](https://github.com/safishamsi/graphify/releases))
- Dates: 12 releases (v0.8.9 - v0.8.20) shipped May 17 - 26, 2026.
- One-line: builds a queryable local knowledge graph of any codebase (AST + Leiden community detection) so Claude reads the graph instead of grepping; 6.8x - 49x token reduction.
- Why: 54k stars, daily-ship cadence, distinct from `claude-context` (vector search) — Graphify is local-only, no Milvus / embedding API costs. Doubles as a token-saver and an AI-learning aid.

### 12. `AgriciDaniel/claude-blog`

- Source: <https://github.com/AgriciDaniel/claude-blog>
- Dates: v1.9.0 May 18, 2026; v1.9.1 May 20, 2026.
- One-line: blog production suite (30 sub-skills, 5 agents) with a 5-gate Blog Delivery Contract dual-optimized for Google rankings and AI citations.
- Why: complements `claude-seo` (audit) with production; same maintainer's CI-enforced quality gates. Fills the "actually write the post" gap.

### 13. `AgriciDaniel/claude-ads`

- Source: <https://github.com/AgriciDaniel/claude-ads>
- Dates: v1.7.1 May 18, 2026.
- One-line: paid-ads audit + optimization across Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, Apple Ads — 250+ checks, parallel agents, AI creative generation.
- Why: 5.3k stars, fills the paid-channel gap in entries 4-7 (which all skew organic). Same maintainer pattern as `claude-seo` / `claude-blog`.

---

## Honorable Mentions (skipped from top 13)

| Skill | Why not in top 13 |
|---|---|
| `uditgoenka/autoresearch` | Overlaps your existing `auto-research-loop`. |
| `kfchou/wiki-skills` | Excellent for knowledge bases, but niche. |
| `aaron-he-zhu/seo-geo-claude-skills` | Largely covered by #5 + #6. |
| `anthropics/skills → skill-creator` | Install when you start packaging your own SOPs. |
| `hesreallyhim/awesome-claude-code` | Bookmark for ongoing discovery, not a skill. |
| `AgriciDaniel/claude-obsidian` | Last release April 24, 2026 — 2 days outside the 30-day trending window. Re-evaluate next cycle. |
| `remotion-dev/skills` | May 7, 2026 update verified, but video-production focus is weak fit for stated areas. |
| `anthropics → Skill Creator` | May 2026 release, meta-tool for building skills — install only when you start packaging your own. |
| `eugeniughelbur/obsidian-second-brain` | v0.8.0 May 15, 2026 — Snyk flagged Critical Risk (4 alerts) during install verification; scheduled-agent + vault-write surface raises blast radius. Re-evaluate when maintainer addresses Snyk alerts. |

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
