# LISS-0001: Review issues, Minor Fix Path, and capability routing

## Metadata

- Local issue ID: LISS-0001
- GitHub issue: N/A
- Status: done
- Phase: Architecture Path
- Type: process
- Priority: high
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Status authority: Metadata `Status` is the sole lifecycle field; this issue is not a review-finding.
- Owner/agent: Planner / Specifier / Implementer as assigned by the agreement
- Related branch: process/reviewer-rejection-fixes

## Summary

Extend the contract so actionable review findings become durable ISSUE records,
disputes become grounded Arbiter decisions, minor corrections have a
proportionate path, and tasks route to the smallest safe model capability class.

## Acceptance Notes

- Covered by `DA-2026-08-02-04`.
- Scenarios are in `docs/specs/review-issue-and-minor-fix-path.feature.md`.
- ADR: `docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md`.

## Dependencies

- Parent: N/A
- Depends on: DA-2026-08-02-04
- Blocks: N/A
- Related: `docs/collaboration/model-tool-capability-matrix.md`

## Decisions Not Settled by the Design Agreement

- Concrete provider/model names remain deferred until provider selection is an
  explicit ADR.

## Context

- Included: review records, local issue planning, model routing, phase rules,
  templates, and ADR index.
- Omitted: application source, datastore schemas, provider SDKs, and private
  review content.
- Assumptions: the repository's existing `LISS-*` ledger is the canonical ISSUE
  ledger.

## Work Notes

- Design agreement and architecture decision recorded.
- Contract and template updates are being synchronized.

## Verification

- `git diff --check`: passed.
- Required-file, ADR-index, lifecycle, capability, and date-basis checks:
  passed; outputs are recorded in the trace and Arbiter decision.
- Reviewer and Arbiter records: complete.
