# Skill Routing Matrix

Use this matrix as a starting point. Smart Skill User should automatically choose the best skill for narrow tasks and the smallest effective skill stack for multi-part tasks. Repositories should adapt the skill names to their own ecosystem.

| Task type | Best skill or skill stack | Skip by default | Approval gate |
| --- | --- | --- | --- |
| UI/design/CRO | visual quality, accessibility, CRO, copy | deploy, database, connector | preview before commit |
| SEO/metadata/schema | schema, source-truth, copy | deploy, media | no fake claims |
| Copy/local SEO | copy, source-truth, local SEO | database, deploy | approval for claim-sensitive edits |
| Media/video/assets | media extraction, asset policy, visual QA | CRM, database | no hotlinking; preview before commit |
| Connector/tool usage | connector routing, task skill | unrelated live tools | approval for production actions |
| Research/source-truth | research, citations, decision log | implementation skills | cite sources; mark uncertainty |
| Cleanup/revert/debugging | review, backup patch, validation | visual unless affected | backup patch first |
| Deploy/release | CI, release, hosting | unrelated docs | explicit approval |
| Tests/validation | test workflow, risk review | deploy | run smallest meaningful checks |
| Docs only | writing, repo guidance | product code | no product-code edits |

Skill selection rule:

- Use 1 skill for narrow tasks.
- Use 2-4 skills for multi-part tasks.
- Use more than 4 only when the task explicitly spans multiple domains.
- Never load every skill by default.

Keep selections small. Most tasks need 1-4 skills, not every available skill.
