# Work Plan: Review issues and Minor Fix Path

## Goal

- Make review findings durable, disputable with grounds, and proportionately
  executable while routing each operation to the smallest safe capability class.

## Scope

- In: review-finding ISSUE lifecycle, Minor Fix Path, capability routing,
  templates and contract documentation.
- Out: provider selection and application-specific persistence.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0001 | done | M | M | N/A | DA-2026-08-02-04 | N/A | process/reviewer-rejection-fixes |

## Recommended Order

1. Synchronize the contract, ADR index, issue template, and work-plan template.
2. Run deterministic document and reference checks.
3. Obtain separate Reviewer approval naming falsification searches.

## Current Next Issue

- Issue: none
- Reason it is unblocked: LISS-0001 is complete.
- Reopening request needed: no, unless verification exposes an ambiguity.

## Risks

- A future adopter may interpret capability classes as concrete provider
  choices; the contract must keep that selection explicitly deferred.
- Minor Fix Path may be over-applied; boundary and one-attempt criteria are
  mandatory escalation triggers.

## Verification Plan

- `git diff --check`
- referenced-file existence checks
- repository search for all lifecycle and capability terms
- existing repository-sanity checks from CI
