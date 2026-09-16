# Tailor Job Application integration

Tailor is an optional independent skill named `tailor-job-application`. Discover its location through the current session's skill catalog; no Tailor source code is bundled here.

Use Tailor as the job-specific output layer after the Career OS has assembled a factual candidate set and JD analysis. Read its SKILL.md plus only the references required to build the workspace.

## Reused capabilities

- dependency-free local workspace.html
- six views: overview, JD analysis, resume, supporting materials, interview preparation, application tracking
- classic, modern, and compact resume layouts
- local browser storage for tracking and JSON export
- workspace JSON validation and deterministic HTML rendering

## Handoff contract

Pass only:

- preserved JD and requirement/evidence matrix
- VERIFIED and safe REFRAMED candidate facts
- explicitly marked pending research or confirmation
- selected application-ready resume content
- factual cover letter and greeting content
- interview material with evidence links
- real application records or an empty array

Do not pass INFERRED claims as final resume facts. Do not let Tailor's application-specific analysis overwrite reusable role/company notes or the Master Resume. Render temporary JSON outside the skill source and save the final workspace.html in the application folder.

Tailor does not scrape job listings or perform company research. career-application-os supplies researched context and source classifications.
