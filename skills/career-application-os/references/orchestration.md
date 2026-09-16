# Orchestration rules

## Shared preflight

1. Detect intent from the user's scope instruction, not from the job title alone.
   - A complete or clearly recognizable JD defaults to APPLICATION even when the user does not say “我要投”.
   - Route to a read-only mode only when the user explicitly says “只研究”, “只是看看”, “先分析”, “不准备投”, “只想知道适不适合”, “不要做简历”, “explore only”, or an equivalent limitation.
   - Map the limitation to the closest mode: research-only → RESEARCH_COMPANY_ROLE; browse/not-applying → EXPLORE_ROLE; fit-only/first-analyze → FIT_ANALYSIS; comparison-only → COMPARE_ROLES.
   - Unconfirmed personal fields are `NEED_CONFIRMATION`; they do not downgrade routing or stop independent work.
2. Open Career Dashboard, My Profile when personal fit matters, and the four indexes.
3. Extract search keys: role family, archetype, company, industry, requirements, capabilities, keywords, evidence IDs, and dates.
4. Retrieve the smallest relevant set of normalized notes.
5. Make a missing-information list. Research or ask only for items that materially change the result.
6. Complete the selected mode and write back durable facts with sources and dates.

## EXPLORE_ROLE

- Resolve the title into primary and secondary role archetypes.
- Reuse generic role intelligence when present; update only stale or missing claims.
- Explain the actual weekly work, unpleasant work, incentives, stress, career path, and an ordinary Tuesday.
- Create or update a role note and source evidence. Do not generate application materials.

## RESEARCH_COMPANY_ROLE

- Retrieve generic role intelligence and existing company intelligence first.
- Research only the company-specific product, customer, team, KPI, process, culture evidence, interview pattern, and risk.
- Separate company facts, employee/candidate reports, community consensus, and inference.
- Create or update both the company note and the company-specific Role Reality Card.

## COMPARE_ROLES

- Compare role archetypes rather than labels.
- Use observed experiment feedback ahead of stated preference when they conflict, while showing the conflict.
- Compare capability, interest, lifestyle, stress, pain fit, income potential, learning value, optionality, and transition difficulty.
- Identify what remains unknowable without a real-world experiment.

## FIT_ANALYSIS

- Evaluate evidence-backed capability fit separately from interest and lifestyle fit.
- Show hard constraints before transferable strengths.
- Output Best Part, Worst Part, Hidden Work, Hidden Stress, Likely Pain Point, Biggest Upside, Biggest Risk, and uncertainty.
- Do not reduce fit to one pseudo-precise score.

## CAREER_EXPERIMENT

- Design a 7-day reality test that includes repetitive, uncomfortable, ambiguous, or rejection-heavy work typical of the role.
- Produce observable artifacts and a daily effort budget.
- Collect enjoyment, energy, curiosity, stress, resistance, and “Would I do this every week?” after completion.
- Store observed feedback separately from the pre-test hypothesis.

## APPLICATION

1. Preserve the JD verbatim in the application folder with source and retrieval date.
2. Parse must-haves, core responsibilities, nice-to-haves, ATS language, constraints, and interview signals.
3. Retrieve relevant role, company, experiment, profile, Master Resume, and personal evidence notes.
4. Research only missing or stale company/role/interview information. If Role Analysis or Company Research was just generated or remains fresh, reuse it and continue directly to downstream application steps.
5. Determine the role archetype and update reusable intelligence.
6. Produce fit analysis, evidence mapping, truthful experience translation, and at most two gap projects when a material gap is fillable in 1–7 days.
7. Apply the mapped ASu capabilities for job matching, experience/resume work, ATS review, interview preparation, and tracking where useful.
8. Produce an application-ready resume from VERIFIED and safe REFRAMED claims. Create a separate flagged enhanced draft only if INFERRED material would be useful for confirmation.
9. Produce the tailored application workspace through Tailor when candidate facts are sufficient.
10. Make one of: APPLY AGGRESSIVELY, APPLY AS EXPERIMENT, LOW PRIORITY, SKIP. Explain evidence, uncertainty, upside, risk, pain point, gap, and three-year optionality.
11. Consolidate all unresolved user fields into one Confirmation Checklist inside the application result.
12. Update Application Index. Do not submit a form or send a message unless the user explicitly asks for that separate action.

APPLICATION is not complete after Job Match. Unless a genuine blocker applies, it must continue through Role Analysis, Evidence Mapping, Resume Strategy, Tailored Resume, ATS Review, Interview Preparation, Application Decision, and a formal application folder; use Tailor for the workspace when available and factually safe.

If candidate fields such as graduation date, degree, CET-6, location preference, relocation, salary expectation, visa, or travel willingness are missing, complete all independent deliverables using visible `NEED_CONFIRMATION` placeholders. Never promote those placeholders into final facts, but do not stop the package at fit analysis.

The only normal blockers are: missing information makes a truthful resume impossible, the user explicitly requires confirmation before continuation, or there is no usable Personal Evidence. A blocker for one artifact does not cancel unrelated safe deliverables.

## INTERVIEW

- Retrieve the exact submitted resume version, JD, evidence map, role/company intelligence, and unresolved risks.
- Use ASu interview's Claim-driven predict/grill/review/retry workflow.
- Add company-specific, role-specific, scenario, case, pressure, and English questions when evidence supports their relevance.
- Flag claims most likely to be challenged and link each proposed answer to personal evidence.
