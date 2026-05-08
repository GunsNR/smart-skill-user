# Optional Auto-Research Loop

The auto-research loop is a report-only way to study approved public sources and turn them into reviewable improvement ideas for Smart Skill User.

It is intentionally small and conservative:

- sources must be listed in `config/research-sources.yml`
- generated reports go under `research/`
- GitHub sources use public metadata by default, not repository clones
- web sources are read as bounded excerpts
- reports classify ideas by impact, risk, effort, source, and license sensitivity
- network failures are reported as warnings instead of blocking normal validation
- no commits, pushes, pull requests, releases, publishing, or issue creation happen by default

## Local Use

Run an offline dry run:

```bash
python scripts/auto_research.py --offline --dry-run --output research/auto-research-latest.md
```

Run a bounded online report:

```bash
python scripts/auto_research.py --dry-run --output research/auto-research-latest.md
```

Use `--refresh-cache` only when you want to re-fetch allowlisted public metadata instead of reusing `.cache/auto-research`.

## Source Rules

Every source must declare:

- `id`
- `type`
- `url`
- explicit `allowed_hosts`
- `fetch_strategy`
- `license_sensitivity`
- `research_focus`

Supported source types are:

- `github_user`: reads public repository metadata for one GitHub user
- `github_repo`: reads public metadata for one repository
- `web_page`: reads a bounded public page excerpt

The initial config includes `karpathy-public-github` as a configurable public GitHub user source. It is marked `metadata_only` with high license sensitivity, so the loop can learn from public repository-level signals without cloning repositories or copying code.

## Report Format

Reports include:

- run mode and safety summary
- approved source table
- cache status
- improvement ideas table
- human review gates

Ideas are proposals. They do not change the repo and should not be treated as implementation instructions until a maintainer approves the next step.

## GitHub Action

`.github/workflows/auto-research.yml` can be run manually and also runs on a quiet weekly schedule. It has read-only repository permissions, uses the script cache, uploads the report as an artifact, and does not push changes.

Manual runs default to offline mode. Maintainers can choose a bounded online run from the workflow dispatch form when they want to refresh public metadata.

## Cache Behavior

Online runs store bounded source responses in `.cache/auto-research`. Later runs reuse fresh cache entries based on `cache_ttl_hours` in the config. This keeps research inexpensive and avoids repeatedly reading the same public sources.

The cache and generated reports are local artifacts. They are not intended to be committed.
