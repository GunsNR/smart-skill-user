# Support

Smart Skill User is a community-driven open-source project. It is maintained as a lightweight instruction workflow for Codex, Claude Code, and AGENTS.md-compatible coding agents.

Before opening an issue, please check the project docs:

- [Install Quick Start](docs/INSTALL_QUICK_START.md)
- [Codex Global Install](install/codex-global.md)
- [Codex Repo-Level Install](install/codex-repo.md)
- [Claude Code Install](install/claude-code.md)
- [Generic AGENTS.md Install](install/generic-agents-md.md)
- [FAQ](docs/faq.md)
- [How It Works](docs/how-it-works.md)
- [Skill Routing Matrix](docs/skill-routing-matrix.md)
- [Safety and Approval Gates](docs/safety-and-approval-gates.md)
- [Token Efficiency](docs/token-efficiency.md)

## Installation And Setup Help

For Codex, start with the quick-start guide:

- Global install: use this when you want Codex instructed to run Smart Skill Preflight before each task or session.
- Repo-level install: use this when one project needs its own local rules.

For Claude Code or generic agent workflows, copy the matching template into your project guidance file.

If setup does not work, include this in your issue:

- operating system
- install path used: global Codex, repo-level Codex, Claude Code, or generic AGENTS.md
- whether the skill file exists in the expected location
- whether the guidance file contains `Smart Skill Preflight`
- the exact command you ran, with private paths and secrets removed

## Usage Questions

Good usage questions include:

- how to adapt Smart Skill Preflight for a specific repo structure
- how to keep repo guidance short
- how to choose approval gates for deploys, visual work, cleanup, or connectors
- how to verify that Codex is loading the user-level or repo-level guidance
- how to use the routing matrix for a new task type

Please avoid posting private project names, client names, local paths, screenshots, videos, logs with secrets, or credentials.

## Validation And Troubleshooting

Run the local validation checks before opening a bug when possible:

```bash
python scripts/validate-repo.py
python -m pytest
git --no-pager diff --check
```

For global Codex installs, use this verification prompt in a new Codex session:

```text
Before doing anything, list the instruction sources and skills you loaded. Then run Smart Skill Preflight for this task: update a mobile homepage hero. Do not edit files.
```

Expected behavior:

- Codex mentions Smart Skill Preflight or the relevant guidance.
- Codex confirms scope.
- Codex selects a relevant skill or skill stack.
- Codex skips irrelevant skills.
- Codex edits no files.

If validation fails, check:

- the intended install path: global or repo-level
- the current branch
- syntax in `AGENTS.md` or `CLAUDE.md`
- whether the agent supports the instruction file you edited

## Issues, Feedback, And Contributions

Use GitHub issues for:

- installation problems
- unclear docs
- missing examples
- confusing approval-gate behavior
- safe feature requests

Pull requests are welcome for:

- docs improvements
- install examples
- validation tests
- small templates that stay generic and public-safe

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening larger changes.

## Documentation

- [Launch Copy](docs/LAUNCH_COPY.md)
- [Launch Announcements](docs/LAUNCH_ANNOUNCEMENTS.md)
- [Auto-Research Loop](docs/auto-research-loop.md)
- [Self-Improvement Policy](docs/self-improvement-policy.md)
- [Codex vs Claude Code](docs/codex-vs-claude-code.md)

## Code Of Conduct

Participation is covered by the project [Code of Conduct](CODE_OF_CONDUCT.md). Keep discussions respectful, specific, and useful for maintainers and other users.

## License

Smart Skill User is MIT licensed. See [LICENSE](LICENSE).

## Support The Project

The best ways to support Smart Skill User are simple:

- star the repository
- share feedback from real workflows
- open clear issues when something is confusing
- contribute examples or documentation
- share the repo with developers who manage multi-project AI coding workflows

## Questions

If you cannot find an answer, search existing GitHub issues first, then open a focused issue with the relevant setup details.
