# Install Top 13 Skills

This install guide adds the curated top 13 Claude / Claude Code skills documented in [`docs/TOP_SKILLS.md`](../docs/TOP_SKILLS.md) to your local environment. Entries 1-10 are the foundational stack; entries 11-13 are May 2026 trending additions. It is additive — it does not modify Smart Skill User itself, and it does not push or deploy anything.

> Note: a fourth May-2026 candidate (`eugeniughelbur/obsidian-second-brain`) was removed during install verification after Snyk flagged Critical Risk with 4 alerts. See honorable mentions in `docs/TOP_SKILLS.md`.

Run the script on every machine where you use Claude Code (laptop, desktop, dev workstation, anywhere `~/.claude` lives). Claude on web / iOS / Android cannot host local skills, so this targets the Claude Code CLI / desktop install only.

---

## Quick Install

### macOS / Linux

```bash
bash scripts/install-top-skills.sh
```

Dry run first if you want to see actions only:

```bash
bash scripts/install-top-skills.sh --dry-run
```

### Windows (PowerShell)

```powershell
pwsh scripts/install-top-skills.ps1
```

Dry run:

```powershell
pwsh scripts/install-top-skills.ps1 -DryRun
```

---

## What the script does automatically

| # | Skill | Mechanism |
|---|---|---|
| 1 | `juliusbrussee/caveman` | `npx skills add` |
| 2 | `thedotmack/claude-mem` | `npx claude-mem install` |
| 3 | `coreyhaines31/marketingskills` | `npx skills add` |
| 4 | `karpathy/nanochat → read-arxiv-paper` | sparse `git clone` into `~/.claude/skills/read-arxiv-paper` |
| 11 | `safishamsi/graphify` | `npx skills add` (with manual fallback) |

**Important:** run the script from your home directory (`cd $HOME` first), not from inside the `smart-skill-user` repo. `npx skills add` writes to the current directory's `.claude/skills/` — running from a project installs scoped to that project only.

---

## What you must paste into Claude Code

`/plugin` slash commands run only inside an interactive Claude Code session. Open Claude Code, then paste this block:

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install marketing@anthropic-knowledge-work-plugins

/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@claude-seo

/plugin marketplace add multica-ai/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills

/plugin marketplace add obra/superpowers
/plugin install superpowers@claude-plugins-official

/plugin marketplace add AgriciDaniel/claude-blog
/plugin install claude-blog@claude-blog

/plugin marketplace add AgriciDaniel/claude-ads
/plugin install claude-ads@claude-ads
```

---

## MCP server: `zilliztech/claude-context`

This is a Model Context Protocol server, not a skill. Add it via the Claude Code CLI on each machine:

```bash
claude mcp add claude-context -- npx -y @zilliz/claude-context-mcp
```

Then configure the embedding provider and vector backend (Milvus/Zilliz) per the [project README](https://github.com/zilliztech/claude-context).

---

## Manual: SurgeGraph

There is no verified one-line installer for SurgeGraph's Claude Code Skill as of the May 2026 research. Sign in at <https://surgegraph.io> and follow their account flow. This skill is the one in the top 10 that cannot be automated yet — only install it if AI-citation tracking is a priority for you.

---

## Verification

In Claude Code, run:

```text
/skills list
```

You should see at least:

- `caveman`
- `claude-mem` (or its slash command)
- `marketingskills` (or sub-skills under it)
- `read-arxiv-paper`
- `marketing` (from the official knowledge-work-plugins)
- `claude-seo`
- `andrej-karpathy-skills`
- `superpowers`
- `graphify`
- `claude-blog`
- `claude-ads`

If a skill is missing, re-run the script with `--dry-run` to confirm the command, then run the failing command on its own to see the error.

---

## Uninstall

The script does not write to `CLAUDE.md` and does not back up files (it only adds skills under `~/.claude` and runs official installers). To remove a skill, use Claude Code's plugin manager or delete its folder under `~/.claude/skills/`.

---

## Approval gates honoured

- The script is local-only. It does not push, deploy, or modify product code.
- All installs come from canonical upstream sources — no copied code is added to this repo.
- SurgeGraph is left manual rather than auto-installed because its install path was not verifiable from public docs at the time of writing.
