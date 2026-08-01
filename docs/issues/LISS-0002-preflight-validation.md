# LISS-0002: Preflight Validation before independent review

## Metadata

- Local issue ID: LISS-0002
- GitHub issue: N/A
- Status: done
- Phase: Architecture Path
- Type: process
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A
- Owner/agent: Implementer
- Related branch: process/reviewer-rejection-fixes

## Summary

Add a cheap, evidence-producing Preflight Validation step before the separate
Reviewer, without turning self-checking into approval.

## Acceptance Notes

- Covered by `DA-2026-08-02-05`.
- Specification: `docs/specs/preflight-validation.feature.md`.
- ADR: `docs/architecture/adr/0013-preflight-validation-before-independent-review.md`.

## Dependencies

- Parent: LISS-0001
- Depends on: DA-2026-08-02-05
- Blocks: N/A
- Related: `docs/collaboration/model-tool-capability-matrix.md`

## Context

- Included: review workflow, deterministic verification, routing, traces,
  review records, and agent contracts.
- Omitted: application source, provider SDKs, and datastore schemas.
- Assumptions: independent Reviewer approval remains mandatory.

## Verification

- Contract synchronization complete.
- Preflight `pass` recorded with literal command output.
- Independent Reviewer approved specification conformance, phase correctness,
  boundary conformance, and evidence sufficiency.
