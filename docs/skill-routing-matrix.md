# Skill Routing Matrix

Use this matrix as a starting point. Repositories should adapt it to their own skill names.

| Task type | Select | Skip by default | Approval gate |
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

Keep selections small. Most tasks need 1-4 skills, not every available skill.
