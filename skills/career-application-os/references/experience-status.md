# Experience status rules

Every personal claim uses exactly one status.

## VERIFIED

The source explicitly supports the claim or the user directly confirmed it. Safe for final external materials, subject to accurate scope and date.

## REFRAMED

The underlying experience is VERIFIED; only its language or emphasis has changed for the target role. Safe for final materials when the factual core, ownership, scale, and result remain unchanged. Link both the source evidence and the original wording.

## INFERRED

The claim is plausible from available evidence but not explicit. It may appear only in an internal enhanced draft labeled “CONFIRM BEFORE APPLICATION”. It is excluded from the application-ready resume, cover letter, recruiter message, and interview answer until confirmed.

## PROJECT_TO_COMPLETE

A planned activity designed to produce missing evidence. It cannot be described as completed experience. After completion, evaluate artifacts and user confirmation before creating a new VERIFIED evidence record.

## Allowed transitions

- INFERRED → VERIFIED: direct evidence or explicit user confirmation is captured.
- VERIFIED → REFRAMED: a target-role expression is linked to the unchanged original fact.
- PROJECT_TO_COMPLETE → VERIFIED: the project is completed and deliverables are inspected or confirmed.
- Any status → CONFLICT FLAG: sources disagree; preserve the current status field and add conflict_status: OPEN until resolved.

Never upgrade ownership verbs without matching evidence.
