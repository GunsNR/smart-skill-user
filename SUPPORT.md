# Support

Smart Skill User is an open-source project maintained by the community. Here's how to get help, report issues, and contribute.

## Installation & Setup Help

If you need help installing Smart Skill User, start here:

- **[Quick Start Install Guide](docs/INSTALL_QUICK_START.md)** — step-by-step instructions for Codex, Claude Code, and AGENTS.md agents
- **[Codex Global Install](install/codex-global.md)** — detailed guide for global Codex setup
- **[Codex Repo-Level Install](install/codex-repo.md)** — team or project-specific setup
- **[Claude Code Install](install/claude-code.md)** — portable instruction setup
- **[Generic AGENTS.md Install](install/generic-agents-md.md)** — any compatible agent framework

## Usage Questions

Check the main [README.md](README.md) for:

- **What it does** — the preflight workflow and routing logic
- **How it works** — step-by-step process
- **Examples** — real task scenarios (mobile, SEO, media, cleanup, deploy)
- **Safety model** — approval gates and validation rules
- **Token efficiency** — context optimization principles
- **Limitations** — what it can and cannot do

See [docs/skill-routing-matrix.md](docs/skill-routing-matrix.md) for the full routing reference.

## Validation & Troubleshooting

Run these commands to verify your setup:

```bash
# Validate repository integrity
python scripts/validate-repo.py

# Run tests
python -m pytest

# Check for whitespace issues
git --no-pager diff --check
```

Expected result:

- Smart Skill Preflight appears in your agent's loaded instructions
- Your agent confirms scope before starting
- Your agent selects a relevant skill stack
- Your agent skips irrelevant skills
- No files are edited during the preflight step

If validation fails, check:

1. Correct file paths (global vs. repo-level)
2. Correct branch (usually `master` or `main`)
3. Correct syntax in your `AGENTS.md` or `CLAUDE.md`
4. Agent version compatibility

## Report Issues

Found a bug or have a suggestion?

1. **Search existing issues** — your question might already be answered
2. **Check the FAQ** — common questions and answers
3. **Open a new issue** — describe:
   - What you tried
   - What you expected
   - What happened instead
   - Your agent framework (Codex, Claude Code, other AGENTS.md)
   - Your OS and shell (if relevant)

## Share Feedback & Examples

Help others by:

- **Adding examples** — submit a focused example of a task your team runs frequently
- **Improving docs** — fix typos, clarify steps, add screenshots
- **Sharing your skill routing** — if you've customized the matrix for your workflow, consider sharing it
- **Testing in new environments** — let us know if you've set this up with Cursor, Continue, or other agents

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Documentation

- **[Launch Copy & Announcements](docs/LAUNCH_ANNOUNCEMENTS.md)** — share the project
- **[Skill Routing Matrix](docs/skill-routing-matrix.md)** — full task-to-skill reference
- **[Safety & Approval Gates](docs/safety-and-approval-gates.md)** — approval rules and validation
- **[Token Efficiency Model](docs/token-efficiency.md)** — context optimization
- **[Auto-Research Loop](docs/auto-research-loop.md)** — optional self-improvement workflow
- **[Self-Improvement Policy](docs/self-improvement-policy.md)** — guardrails for research

## Community & Code of Conduct

Smart Skill User is committed to fostering a welcoming, inclusive community.

- **[Code of Conduct](CODE_OF_CONDUCT.md)** — community guidelines
- **[Contributing](CONTRIBUTING.md)** — how to contribute code, examples, and docs
- **[Security Policy](SECURITY.md)** — reporting security issues responsibly

## Support the Project

You can support Smart Skill User by:

- **Starring the repo** — helps others discover it
- **Sharing feedback** — open issues, suggest improvements, share your use cases
- **Contributing** — add examples, improve docs, submit fixes
- **Spreading the word** — share in your team, community, or social networks

See [docs/LAUNCH_ANNOUNCEMENTS.md](docs/LAUNCH_ANNOUNCEMENTS.md) for ready-to-share copy.

## License

Smart Skill User is open-source under the [MIT License](LICENSE). You are free to use, modify, and distribute it in commercial and personal projects.

## Questions?

If you can't find an answer:

1. Search [closed issues](https://github.com/GunsNR/smart-skill-user/issues?q=is%3Aissue+is%3Aclosed)
2. Open a new [discussion or issue](https://github.com/GunsNR/smart-skill-user/issues)
3. Check the [README](README.md) examples and routing matrix

Thanks for using Smart Skill User.
