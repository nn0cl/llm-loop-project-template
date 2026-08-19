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
| LISS-0029 | review | M | M | AIP-0029-001 | - | LISS-0030 | process/adr-0017-portable-loop |
| LISS-0030 | review | M | M | AIP-0030-001 | LISS-0029 | - | process/adr-0017-portable-loop |

Branch note (Implementer, 2026-08-18): both issues landed on the single
branch `process/adr-0017-portable-loop` rather than the two separate branches
originally listed, because LISS-0030 strictly depends on LISS-0029 landing
first and the two together form one small, sequential, reviewable unit; the
`Branch` column above has been updated to match what was actually done.

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

- Result: `pass`
- Checks and command output: `python3 scripts/check-contract-consistency.py`
  (run from the Implementation-group worktree, branch
  `process/adr-0017-portable-loop`, after both LISS-0029 and LISS-0030 were
  self-reviewed and their Status fields set to `review`):

  ```
  contract consistency: all checks passed
  ```

  Also verified, per the same run: `git diff --stat` against the branch
  point (`d9c6e6b`) shows the five mirror-file edits (`AGENTS.md`,
  `CLAUDE.md`, `.github/copilot-instructions.md`,
  `.grok/rules/03-collaboration-and-completion.md`,
  `.cursor/rules/03-collaboration-and-completion.mdc`) are insertion-only
  (0 deletions), and `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
  and `docs/collaboration/cross-session-messaging.md` do not appear in the
  diff at all — confirming this work plan's own Boundaries and
  Falsification Criteria (no edit to either file).
- Scope result: both LISS-0029 and LISS-0030 self-reviewed and complete
  (self-review records in each issue's own Work Notes/Self-Review section);
  no open `Type: review-finding` issues affect this area; no implementation
  issue in this work plan is blocked on an open spike case. In scope for
  this Preflight: ADR 0017 (LISS-0029), the five mirror-file edits and
  their trace (LISS-0030). Out of scope, and confirmed untouched: ADR 0016,
  `docs/collaboration/cross-session-messaging.md`.
- Next action: submit the whole work plan to the Design & Review group's
  separate-context Reviewer pass.

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
