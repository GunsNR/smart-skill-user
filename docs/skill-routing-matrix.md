# Skill Routing Matrix

Smart Skill User picks the best skill (or smallest stack) per task. Repositories adapt names to their own ecosystem; defaults below name the top-10 skills from [`TOP_SKILLS.md`](TOP_SKILLS.md).

## Always-On Stack (Token Savers)

Active on every task — no opt-in needed.

| Skill | What it does | Mechanism |
| --- | --- | --- |
| `caveman` (lite) | Terse bullet output, no preamble | SessionStart hook (`.claude/settings.json`) + `CLAUDE.md` directive |
| `claude-mem` | Compressed prior-session context | SessionStart hook (installed via `scripts/install-top-skills.sh`) |
| `claude-context` | Semantic code search, ~40% token cut | MCP server |
| Subagent delegation | Offload large reads/research | Built-in `Agent` tool — preflight chooses when |

The preflight always assumes these four are active and does not re-list them in `Selected route`.

## Task → Skill Routing

| Task type | Best skill / stack | Skip by default | Approval gate |
| --- | --- | --- | --- |
| SEO technical audit | `AgriciDaniel/claude-seo` + Ahrefs/GSC MCP | marketing copywriting | no fake claims; cite sources |
| SEO content brief | `coreyhaines31/marketingskills` (seo-content-brief, ai-seo) + Semrush MCP | deploy, media | source-truth required |
| SEO schema/structured data | `AgriciDaniel/claude-seo` (schema sub-skill) | copy, ads | validate via rich-results |
| Marketing copy / draft content | `knowledge-work-plugins/marketing` (draft-content) + `coreyhaines31/marketingskills` (copywriting) | SEO technical, deploy | brand-voice check |
| Landing-page CRO | `coreyhaines31/marketingskills` (page-cro, signup-flow-cro) | deploy, database | preview before commit |
| Ad creative (Google/Meta/LinkedIn) | `coreyhaines31/marketingskills` (ad-creative) | technical SEO | preview before publish |
| Email sequence / cold outreach | `coreyhaines31/marketingskills` (email-sequence, cold-email) | technical SEO | spam-policy check |
| Competitor teardown | `coreyhaines31/marketingskills` (competitor-profiling) + Semrush MCP | unrelated live tools | source-truth required |
| AI-citation / GEO tracking | SurgeGraph skill | classic-SEO-only tools | no fake metrics |
| Brand-voice / brand review | `knowledge-work-plugins/marketing` (brand-review) | technical SEO | brand-style enforced |
| Performance reporting | `knowledge-work-plugins/marketing` (performance-report) + GSC MCP | deploy | source-truth required |
| Research / source-truth | `auto-research-loop` + `read-arxiv-paper` | implementation skills | cite sources; report-only |
| Read an arXiv paper | `karpathy/nanochat → read-arxiv-paper` | implementation skills | summarize then link |
| AI / LLM learning task | `read-arxiv-paper` + `andrej-karpathy-skills` | product code | think before coding |
| Code work (general) | `obra/superpowers` (plan + TDD) + `andrej-karpathy-skills` (anti-pitfalls) | marketing skills | plan before code |
| Large-codebase search | rely on `claude-context` MCP; subagent for spread reads | broad file reads | none |
| Cleanup / revert | `obra/superpowers` (systematic-debugging) | visual unless affected | backup patch first |
| Deploy / release | repo CI conventions only | unrelated docs | explicit approval |
| Tests / validation | repo test workflow | deploy | smallest meaningful checks |
| Docs only | repo writing conventions | product code | no product-code edits |

## Selection Rules

- 1 skill for narrow tasks.
- 2–4 skills for multi-part tasks.
- More than 4 only when the task explicitly spans multiple domains.
- Never load every skill by default.
- The always-on stack does not count toward this budget.

## Updating the Matrix

When adding a new skill to your local ecosystem:

1. Add a row above with `task type → skill`, `skip`, `approval gate`.
2. If it's a token-saver that auto-runs, add it to the Always-On Stack table.
3. Re-run the preflight on a representative task to confirm the route picks it.
