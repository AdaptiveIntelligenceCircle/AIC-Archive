# Entry format

## Filename

```
entries/YYYY/YYYY-MM-DD-short-slug.md
```

Examples:

- `entries/2026/2026-10-08-default-deny-bridge.md`
- `entries/2025/2025-04-founding-orientation.md`

Use UTC or clearly stated local calendar dates. Prefer ISO order for sorting.

## Required sections

1. **Title**
2. **Metadata** — date, status (active / superseded), authors/roles (optional), related repos
3. **Context** — what problem or question prompted the entry
4. **Decision or statement** — concise
5. **Rationale** — why
6. **Non-claims** — what this entry does *not* mean (under-claim)
7. **References** — links to PRs, specs, formal models, prior entries

## Optional sections

- Alternatives considered  
- Supersedes / superseded by  
- Follow-up actions  

## Front matter (optional YAML)

```yaml
---
id: 2026-10-08-default-deny-bridge
date: 2026-10-08
status: active
tags: [interop, parallel-testnet, fail-closed]
related: [AIC-Interop, AIC-Formal]
---
```

## Language

English is preferred for archive entries so that technical history stays aligned with canonical specs.  
Translations may be linked from Localization; they do not replace the archive entry.