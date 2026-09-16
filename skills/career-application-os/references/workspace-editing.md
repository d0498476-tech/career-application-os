# Editable application workspace

Read when a user requests local confirmation editing or resume-version editing. Adapt the existing workspace; do not re-research the role or rebuild unrelated pages.

## Confirmations

- Collect NEED_CONFIRMATION, NEED CONFIRMATION, uncertain values, and placeholders into one editable confirmation panel.
- Use text inputs, selectors, radio/multi-select controls, and notes. Do not require editing JSON.
- Long-term personal fields belong in the private Vault's `00_Home/My Profile.md`; job-specific choices belong in the current application's `Confirmation.md` or equivalent.
- Preserve uncertainty until the user confirms a value. External company research is not a source for candidate facts.

## One confirmation, multiple views

After a successful save, update supported placeholders in the selected resume, its Markdown, the preview, and affected fit/interview fields. The source of truth is the private Profile plus application confirmations plus the selected resume version, not browser localStorage alone.

A standalone file cannot silently promise filesystem write-back. When write-back is requested, use a bounded localhost service or an explicit supported file-access mechanism; identify the files that will change. Keep authentication, origin checks, and allowed output paths proportional to the chosen local mechanism. Do not expose candidate data to a remote service by default.

## Editable resume versions

- Allow Summary, education, bullet text/emphasis, skills, and ordering to be edited visually.
- Empty sections hide automatically. Keep language versions independent and identify the version selected by each application.
- Confirmation values may initialize or update managed fields, but they must not undo a user's intentional deletion.
- Store exclusions in the affected resume version. Deleting a managed education bullet hides it in that version while keeping the underlying Profile fact intact. Subsequent hydration, saves, reloads, version selection, and confirmation updates must respect the exclusions.
- Restoring the same managed field explicitly can clear its exclusion. Never infer that removing a bullet means the underlying personal fact is false or should be erased.
- Preserve evidence links and user edits; formatting changes must not regenerate factual content.

## Save safety and tests

Create a `.history` backup before changing existing files, and show the written files and save result. Failed writes must not be reported as success. Refresh dependent views only after a successful save; keep unsaved work when an error occurs.

Test the complete chain: delete/edit → save → read disk → reload preview. Include managed auto-filled bullet deletion, deletion of all bullets, an empty section, and a confirmation update after a deletion. Verify changes in an isolated test Vault, not in published examples or another person's active application.
