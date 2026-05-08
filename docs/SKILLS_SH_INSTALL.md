# skills.sh And npx skills Install

Smart Skill User is packaged as an Agent Skills-compatible repository. The core skill lives at:

```text
skills/smart-skill-user/SKILL.md
```

The parent directory matches the frontmatter name:

```yaml
name: smart-skill-user
```

## Direct GitHub Install

Use the `skills` CLI to install from GitHub directly. List available skills first:

```bash
DISABLE_TELEMETRY=1 npx skills add GunsNR/smart-skill-user --list
```

Expected available skills:

- `smart-skill-user`
- `auto-research-loop`

Install only the core Smart Skill User skill for Codex at the project level:

```bash
npx skills add GunsNR/smart-skill-user --skill smart-skill-user --agent codex --copy --yes
```

Install the core skill globally for Codex:

```bash
npx skills add GunsNR/smart-skill-user --skill smart-skill-user --agent codex --global --copy --yes
```

Equivalent shorthand:

```bash
npx skills add GunsNR/smart-skill-user -s smart-skill-user -a codex -g --copy -y
```

`--copy` avoids symlink-permission issues on systems where symlinks are restricted. Omit `--copy` if you prefer the CLI default install method.

## Important Codex Note

The `skills` CLI makes the skill available to the target agent. To make Smart Skill Preflight run as the first step on every Codex task, also add the Codex guidance from one of these docs:

- [Codex Global Install](../install/codex-global.md)
- [Codex Repo-Level Install](../install/codex-repo.md)

In short:

- `npx skills add ...` installs the skill.
- `AGENTS.md` guidance tells Codex to run Smart Skill Preflight first.

## Compatibility Status

Last checked: 2026-05-08.

Verified:

- `npx skills --help` supports `--list`, `--skill`, `--agent`, `--global`, `--copy`, and `--yes`.
- `npx skills add GunsNR/smart-skill-user --list` finds `smart-skill-user`.
- A temporary Codex project install with `--skill smart-skill-user --agent codex --copy --yes` created `.agents/skills/smart-skill-user/SKILL.md`.
- The installed `SKILL.md` preserved the expected `name` and `description` frontmatter.

Not verified:

- skills.sh search/indexing. `npx skills find smart-skill-user` did not return Smart Skill User when last checked.
- skills.sh detail pages for this repo returned 404 when last checked.
- The public skills.sh API search endpoint returned `authentication_required` in this environment, despite the docs describing public unauthenticated access.

Do not claim Smart Skill User is indexed on skills.sh until `npx skills find smart-skill-user` or a skills.sh listing page returns it.

## Registry And Discovery Strategy

The skills.sh FAQ says leaderboard listing happens automatically through anonymous CLI telemetry when users run `npx skills add <owner/repo>`. The docs did not show a separate manual submission form.

Safe next steps:

1. Keep direct GitHub install commands in the README and install docs.
2. Ask early users to install from `GunsNR/smart-skill-user` if they want to try the skill.
3. Re-check discovery after public installs:

```bash
npx skills find smart-skill-user
```

4. If discovery still does not show the repo, ask the maintainer before opening an external issue.

Draft issue, only if approved:

````markdown
Title: skills.sh search does not find GunsNR/smart-skill-user after direct GitHub discovery works

Hi, I maintain Smart Skill User at https://github.com/GunsNR/smart-skill-user.

Direct GitHub discovery works:

```bash
npx skills add GunsNR/smart-skill-user --list
```

The CLI finds:

- smart-skill-user
- auto-research-loop

The core skill path is:

```text
skills/smart-skill-user/SKILL.md
```

The frontmatter includes:

```yaml
name: smart-skill-user
description: Token-aware preflight router that automatically chooses the best skill or smallest effective skill stack before an AI coding agent starts work.
```

However, this search did not find it:

```bash
npx skills find smart-skill-user
```

Could you confirm whether indexing is expected to happen automatically after installs, or whether another repository metadata step is required?
````

## Source Docs To Re-check

- [skills.sh CLI docs](https://skills.sh/docs/cli)
- [skills.sh FAQ](https://skills.sh/docs/faq)
- [skills CLI repository](https://github.com/vercel-labs/skills)
- [Agent Skills specification](https://agentskills.io/specification)
