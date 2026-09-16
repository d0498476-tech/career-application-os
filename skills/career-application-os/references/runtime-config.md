# Runtime configuration

This distributable skill contains no person's Vault, credentials, fixed home directory, or installed dependency locations.

## Resolve locations

1. An explicit user-selected Vault path takes precedence.
2. Otherwise use the `CAREER_OS_VAULT` environment variable when set.
3. Otherwise use a `Career-OS` directory in the current project. Keep it outside the skill's public source repository when possible; if it is inside a repository, verify it is ignored before storing personal data.

The main skill location is the folder containing this `SKILL.md`. Find optional skills through the current session's skill catalog, not through an author's fixed paths. For local checks, `CODEX_HOME` determines the installed skills directory; otherwise the checker uses the current account's `.codex/skills` directory.

On first use, create a blank Vault with `scripts/init_vault.py --vault <selected-private-vault>`. The initializer creates only missing files and never overwrites existing data. Set the Vault environment variable or pass `--vault` to the checker for subsequent runs.

## Optional integrations

ASu and Tailor are independent optional installations. Follow each installed skill's own instructions and license; do not copy its source into this package. Never modify an upstream checkout for user-specific behavior.

A missing integration does not block safe Career OS work. Use a truthful local fallback, disclose what was unavailable, and never claim an upstream skill ran when it did not.

Machine-specific paths and preferences belong in private local configuration or the private Vault, not in published skill instructions. Do not assume another user has granted delegation, external publishing, recruiter contact, or form-submission permission.
