# Self-Improvement Policy

Smart Skill User can suggest ways to improve itself, but it must stay human-reviewed and source-safe.

## Allowed

- read approved public sources listed in `config/research-sources.yml`
- generate local or artifact-only reports under `research/`
- classify ideas by impact, risk, effort, source, and license sensitivity
- reuse cached public metadata to avoid repeated research
- propose docs, tests, examples, and routing improvements for maintainer review

## Not Allowed By Default

- cloning whole external repositories
- copying external code, examples, prompts, or structure without license review
- claiming official OpenAI, Anthropic, GitHub, or maintainer affiliation
- committing behavior changes without human approval
- opening pull requests, issues, releases, or publishing packages
- using private client data, local paths, screenshots, videos, secrets, or credentials
- running broad research on every push or small task

## Public Source Handling

Public does not mean free to copy. The loop should prefer metadata, summaries, links, and original synthesis. If an idea depends on source code, examples, or distinctive documentation structure, pause and require license review before implementation.

High-sensitivity sources, including public GitHub accounts with many separately licensed repositories, should produce ideas such as "study the pattern" or "create an original fixture" rather than "port this code."

## Approval Gates

Human approval is required before:

- commits that change behavior
- pull requests
- releases or package publishing
- new integrations
- use of copied or adapted external code
- changes to the allowlisted source policy

Reports can be reviewed, discussed, and discarded without changing the repository.
