# LISS-0032: Mandatory quality-gate hooks and branch/route coverage policy

## Metadata

- Local issue ID: LISS-0032
- GitHub issue: none
- Status: ready
- Phase: phase-0-design (produces an ADR and non-application-code contract
  updates)
- Type: architecture-decision
- Priority: high
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/quality-gate-hooks-and-coverage-policy

## Summary

- Write a new ADR (tentatively `0018`, confirm at execution time — see
  `DA-2026-08-18-05`'s Settled Ambiguities on the numbering coordination
  with WP-0004's `0017`) stating: (1) adopting projects must wire an
  actual, commit-blocking pre-commit hook per language — not merely
  document commands to run manually — covering lint, build/compile, unit
  tests, and coverage; (2) a branch/route coverage anti-gaming rule:
  partial-branch tests do not count, every route needs a test, and
  implementation must not be shaped merely to hit a coverage number; (3) no
  universal numeric coverage floor is mandated by the template — each
  adopting project may choose one locally, recorded in its own
  tooling-setup session.
- Update `docs/architecture/tooling.md` (hook-wiring requirement stated),
  `docs/architecture/testing-strategy.md` (new "Coverage Policy" section
  with the anti-gaming rule), `docs/collaboration/definition-of-done.md`
  (Universal/Phase 2/3 Done criteria gain the hook/coverage requirements —
  ADR-0006 contract file), and
  `scripts/lib/emit-tooling-setup-prompt.sh` (Section A/D explicitly ask
  for hook wiring and a coverage approach, with concrete per-stack
  examples).

## Acceptance Notes

- ADR states all three rules as testable requirements, with the
  numeric-floor non-decision and no-retroactive-`scripts/`-application
  decision both stated with grounds (per `DA-2026-08-18-05`'s Settled
  Ambiguities — copy the reasoning, do not re-derive it differently).
- `tooling.md`/`testing-strategy.md` changes do not require a trace (not
  ADR-0006 contract files) but must not contradict the ADR.
- `definition-of-done.md` change requires a trace; no existing Done
  criterion is weakened.
- `scripts/check-contract-consistency.py` passes.
- `scripts/init-loop-settings.sh --prompt-only` output visibly contains the
  strengthened hook/coverage language after the change.
- Self-review recorded (full form — planning size `M`, multiple files).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0006-quality-gate-hooks-and-review-perspectives-doc.md
- Depends on: none
- Blocks: LISS-0033 (perspectives document cites this ADR)
- Related: `docs/architecture/adr/0016-*.md` (numbering-coordination
  precedent, not content)

## Decisions Not Settled by the Design Agreement

- Exact ADR number: confirm at execution time (see Summary above). If
  genuinely conflicting with WP-0004's concurrent claim on `0017`, report
  as a reopening-worthy finding rather than silently resolving.

## Context

- Included: `docs/backlog/item-0006-*.md`, `docs/architecture/tooling.md`,
  `docs/architecture/testing-strategy.md`,
  `docs/collaboration/definition-of-done.md`,
  `scripts/lib/emit-tooling-setup-prompt.sh`, `DA-2026-08-18-05`.
- Omitted: `docs/collaboration/design-review-perspectives.md` (LISS-0033's
  own deliverable — read only its planned existence, not its content,
  which does not exist yet when this issue starts).
- Assumptions: none beyond the design agreement's own settled points.

## AI Planning Records

### AIP-0032-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Sonnet 5 via Claude Code, Design & Review
    group standing session
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: not surfaced in this environment
- Created at: 2026-08-18
- Planning size: M
- Intended execution route: Implementation-group agent, Architecture Path,
  one new ADR plus four coordinated file edits
- Compatibility state: Verified — confirmed by direct read that
  `tooling.md`'s stack table is all placeholders, `testing-strategy.md` has
  no coverage section, and `emit-tooling-setup-prompt.sh` does not mention
  hook enforcement
- Intended scope: `docs/architecture/adr/0018-*.md` (number pending),
  `docs/architecture/tooling.md`, `docs/architecture/testing-strategy.md`,
  `docs/collaboration/definition-of-done.md`,
  `scripts/lib/emit-tooling-setup-prompt.sh`
- Estimated token range: 8,000-18,000 tokens
- Estimated token midpoint: 12,000
- Token metric: approximate output tokens across the ADR and four file
  edits
- Estimation basis: comparable in scope to WP-0004's LISS-0029+LISS-0030
  combined (one ADR plus multi-file propagation), scaled for one fewer
  file but a more substantive prompt-script edit
- Assumptions: single execution attempt
- Confidence: medium
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/collaboration/agreements/2026-08-18-quality-gate-hooks-and-perspectives-doc.md`
  (`DA-2026-08-18-05`)
- `docs/architecture/adr/0008-template-update-propagation.md` (sibling
  precedent for a template-contract-level ADR with tiered/deferred
  specifics)

## Work Notes

- 2026-08-18 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0006-*.md`'s promotion, after resolving its flagged
  "[x] Human decision required" item to its narrow genuinely-open
  sub-question (see `DA-2026-08-18-05`'s Settled Ambiguities). Dispatched
  to the Implementation group together with LISS-0033.

## Verification

- Pending Implementation-group execution.
