# ASu-skills integration

ASu is an optional, independently installed skill collection; no ASu source code is bundled here. Discover available skills through the current session's skill catalog. Read the installed SKILL.md for any capability used; upstream instructions remain authoritative for that specialized operation unless they conflict with the user's current request or the Career OS evidence boundary.

## Actual capability map

| Skill | Reuse in Career OS |
| --- | --- |
| job-match | JD requirements, evidence matrix, hard gates, expression/evidence/real gaps, explainable apply recommendation |
| great-resume | truthful positioning, bullet rewriting, project highlights, resume summary, HR opener, claim-evidence audit |
| make-resume | editable HTML/PDF resume generation, ASu templates when shared assets are available, print-preview QA |
| interview | Claim-driven predict, grill, review, retry; ownership, metric, technical, architecture, and result challenges |
| offer | evidence-backed application and offer status tracking |
| evidence-recap | normalize AI project conversations and delivery records into a verifiable evidence chain |
| project-guide | extract technical project learning paths, source evidence, interview material, and handoff summaries |
| contributor | optional real open-source contribution workflow when the user explicitly wants it; never present an unmerged PR as merged |
| job-apply | browser form filling for one explicitly authorized application; stop for review before final submission |

## Routing boundary

The orchestrator may apply job-match, great-resume, make-resume, interview, and offer as stages of an APPLICATION without asking the user to invoke each skill. Do not automatically use job-apply or contributor: they create external side effects or separate project work and require explicit user intent.

ASu does not own the Vault, career exploration, company/role research, reality testing, long-term career comparison, or incremental retrieval. Those stay in career-application-os.

Shared templates and scripts remain with the independent installation. Do not modify them. Resolve resources relative to that installed skill as its instructions require. If a resource is unavailable, follow its documented fallback and state which capability could not be used.
