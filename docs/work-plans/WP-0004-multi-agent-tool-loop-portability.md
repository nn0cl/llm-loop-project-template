# Work Plan: Portable Three-Layer Loop Across AI Coding Tools

## Goal

- Make ADR 0016's three-layer concept (Backlog / Design & Review /
  Implementation) and its parent-child-spawn-plus-worktree baseline handoff
  adoptable by AI coding tools other than Claude Code, without changing ADR
  0016 or `cross-session-messaging.md` themselves, per
  `docs/backlog/item-0007-multi-agent-tool-loop-portability.md` and
  `docs/collaboration/agreements/2026-08-18-multi-agent-tool-loop-portability.md`
  (`DA-2026-08-18-03`).

## Scope

- In: a new ADR 0017; portable-wording propagation across `AGENTS.md`,
  `CLAUDE.md`, `.github/copilot-instructions.md`, `.grok/rules/*.md`,
  `.cursor/rules/*.mdc`; a trace for the mirror-file change; self-review;
  Preflight; separate-context Reviewer pass.
- Out: any change to ADR 0016 or `cross-session-messaging.md`; a new
  cross-tool live-notification mechanism.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0029 | ready | M | M | AIP-0029-001 | - | LISS-0030 | process/adr-0017-portable-loop |
| LISS-0030 | ready | M | M | AIP-0030-001 | LISS-0029 | - | process/mirror-portable-loop-wording |

## Plan-Owned Bug Records

None.

## AI Planning Records

See each issue's own AI Planning Records section (both are planning size
`M`: LISS-0029 touches one new architectural document with real design
content beyond a mechanical edit; LISS-0030 touches five files at once).

## Recommended Order

1. LISS-0029 (ADR 0017) — LISS-0030's mirror wording cites it by number.
2. LISS-0030 (mirror propagation).

## Current Next Issue

- Issue: LISS-0029
- Reason it is unblocked: no dependencies; `DA-2026-08-18-03` covers it
  fully, including the exact `docs/collaboration/handoffs/` file format.
- Reopening request needed: no.

## Minor Fix Path

Not applicable to initial execution (both issues are Architecture Path,
planning size `M`). May apply later to small corrections against this work
plan's accepted result.

## Preflight Validation

- Result: _pending Implementation-group execution_
- Checks and command output: _to be recorded by the Implementer_
- Scope result: _to be recorded_
- Next action: _to be recorded_

## Work-Plan Review

Reviewer's approval record: _pending_

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

- Date: _pending Director action_
- Result read:
- Next direction:
- New design agreement (if any):

## Risks

- Five mirror files edited together risk drifting out of "equivalent
  effective content" with each other; mitigated by
  `scripts/check-contract-consistency.py` and an explicit side-by-side
  read-through in both self-review and the Reviewer pass.
- The new `docs/collaboration/handoffs/` convention is unused until a real
  non-Claude-Code session or intervention exercises it; its format is
  fixed by this agreement in advance of any real use, which is a known risk
  (mirrors ADR 0016's own "Rule 4 is new and untested" risk note).

## Verification Plan

- `scripts/check-contract-consistency.py`.
- Side-by-side read-through of all five mirror files.
- Trace file existence check.
- Separate-context Reviewer approval.
