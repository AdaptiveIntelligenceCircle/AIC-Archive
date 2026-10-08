# Process

## Adding an entry

1. Draft from `templates/decision-entry.md`.
2. Choose a stable slug; do not reuse slugs for different decisions.
3. Add the file under `entries/YYYY/`.
4. Add a row to `entries/INDEX.md` (newest first or chronological — keep consistent; this repo uses **newest first**).
5. Open a PR. Discussion happens on the PR; the merged entry is the record.

## Superseding

Do **not** delete or rewrite the old entry’s decision section to invert meaning.

Instead:

1. Keep the old entry; set `status: superseded` if desired.
2. Add a new entry with `supersedes: <old-id>`.
3. Update the index.

## Corrections

| Kind | Handling |
|------|----------|
| Typo, broken link | Minimal edit; mention in commit message |
| Wrong date on a new entry before merge | Fix in PR |
| Substantive change to meaning | New entry |

## What not to archive

- Every chat message or minor wording tweak.
- Secrets, private personal data, privileged material.
- Speculative roadmap items presented as decisions.