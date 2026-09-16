# Index-first retrieval policy

Never scan the full Vault by default.

## Read order

1. 00_Home/Career Dashboard.md
2. Evidence Index.md, Role Index.md, Company Index.md, Application Index.md
3. My Profile.md only for personal fit, applications, interviews, experiments, or preference-aware comparisons
4. Exact notes linked from the indexes
5. Nearby notes found with narrow filename, property, tag, capability, role, company, or evidence-ID search
6. 99_Raw only when a normalized note lacks an exact metric, wording, provenance, or conflict resolution detail

## Retrieval keys

For a JD, extract role family, primary/secondary archetype, company, industry, product, customer, must-have requirements, named tools, domain language, and date. Search those keys in indexes before note bodies.

Personal evidence retrieval should first match capabilities and target_roles, then keywords. A title mismatch does not exclude transferable evidence.

## Freshness and missing knowledge

- Stable role mechanics can be reused until evidence suggests the role has changed.
- Company products, leadership, strategy, openings, compensation, and interview reports are time-sensitive; check dates and refresh only relevant claims.
- If a note is current enough and directly answers the need, do not research it again.
- If information is missing, record a precise research question before searching.

## Conflicts

Do not silently overwrite conflicting facts. Preserve both statements, their sources, dates, and confidence; add conflict_status: OPEN and request confirmation when the conflict affects an external claim.

## Search mechanics

Prefer narrow filename and content search. Use rg for local text search when available. Avoid loading whole directories or raw archives into model context.
