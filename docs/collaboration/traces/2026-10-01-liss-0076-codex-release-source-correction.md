# LISS-0076 source correction trace

- Active persona: Implementer.
- Agreement: DA-2026-10-01-01; WP-0027; docs-only Architecture Path, size S.
- Scope: correct the independent Reviewer finding LISS-0076 without changing accepted behavior or authority.
- Original defect: Reviewer retrieval of the unified changelog found no 0.156.0 entry; see the original independent review and finding.
- Correction: attach official versioned release links to each CLI claim and retain release page date/tag/commit grounds in `case-0005/evidence/codex-versioned-release-grounds.md`.
- Omitted context: no runtime implementation, paid API, entitlement changes or full-loop certification.
- Deterministic verification: `case-0005/evidence/source-correction-check.txt` records commands, output, source-link presence and refreshed target-copy equality. These checks cannot prove vendor runtime behavior.
- Failure scenarios: generic changelog unavailable is covered by versioned links; copying stale guide is checked by byte equality; claim expansion is left to separate-context review.
- Contract approval: none by this producer. ADR 0006 requires independent correction confirmation.
