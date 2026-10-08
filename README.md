# AIC-Archive

**Append-oriented public log of design decisions, rationale, and historical notes for Adaptive Intelligence Circle.**

Status: **pre-Covenant**, experimental, under-claim.  
This repository records *what was decided or documented and why*, in a reviewable form.  
It is **not** a blockchain, not an immutable court record, not a metrics dashboard, and not a claim of legal or operational finality.

## Purpose

- Keep an ordered trail of significant design and process decisions.
- Separate **decision/rationale history** from live metrics (see AIC-TransparencyDashboard).
- Help future contributors understand *why* boundaries (fail-closed, no token rule-power, pre-Covenant, entity ≠ immunity) were stated the way they were.
- Support under-claim accountability: statements can be dated and revisited without rewriting the past silently.

## Explicit non-goals

| This repository does | This repository does **not** |
|----------------------|------------------------------|
| Store dated decision and design-rationale entries | Replace git history of code repositories |
| Provide a human-readable index of major choices | Prove cryptographic immutability |
| Support corrections via *new* entries (append) | Quietly edit past entries to change meaning |
| Stay aligned with Third Path / under-claim | Certify compliance or Covenant readiness |

## Layout

```
AIC-Archive/
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── docs/
│   ├── overview.md
│   ├── entry-format.md
│   ├── process.md
│   └── limitations.md
├── entries/
│   ├── INDEX.md
│   ├── 2025/
│   └── 2026/
├── schemas/
│   └── archive-entry.schema.json
├── templates/
│   └── decision-entry.md
├── scripts/
│   └── validate_entries.py
└── examples/
```

## Entry rule (short)

1. **Prefer append** — new facts or reversals go in a **new** entry that references the old one.
2. **Date and scope** — every entry states when and what it covers.
3. **Under-claim** — no entry declares mainnet, Covenant, or legal immunity.
4. **Corrections** — factual typos may be fixed with a visible note; substantive changes require a new entry.

## Relationship to other AIC repositories

| Repository | Role vs Archive |
|------------|-----------------|
| **AIC-TransparencyDashboard** | Live / periodic metrics and audit *events* |
| **AIC-Archive** | Curated decision and design *rationale* log |
| **AIC-Legal / AIC-Policy-Tools** | Policy orientation; Archive may *point to* decisions, not replace counsel |
| **AIC-Formal / TestNet / Interop** | Technical artifacts; Archive records *why* a direction was chosen |
| **MyVision / Start-Here** | Narrative orientation; Archive is the dated decision trail |

## Principles observed

- **Under-claim**
- **Entity ≠ immunity**
- **No token rule-power**
- **Pre-Covenant**
- **Fail-closed spirit** — when unsure whether something belongs here, prefer a narrower entry or none

## License

GPL-3.0-or-later (see LICENSE).  
Entry text is part of the public materials; do not strip limitation notices when reusing.

## Maintenance note

During reduced maintainer availability the repository remains public.  
Append-only discipline and under-claim language are more important than volume.