# Work Plan: AI tool support status survey (item-0021)

## Goal

- Deliver the two outputs `docs/backlog/item-0021-...md` requested: a
  status report covering Claude Code, Codex, Cursor, Grok Build, and
  Antigravity (`docs/architecture/ai-tool-support-status.md`, already
  drafted by the Design & Review group from
  `docs/spike/case-0004-ai-tool-support-status-survey/case.md`'s own
  primary-source research), and the one concrete, fixable gap the
  survey found: Antigravity's `AGENTS.md`-native status is undocumented
  in `docs/collaboration/prompt-instruction-change-control.md`.

## Scope

- In:
  - `docs/architecture/ai-tool-support-status.md` (already drafted;
    committed as part of this work plan's own opening).
  - `docs/spike/case-0004-ai-tool-support-status-survey/case.md` (already
    committed).
  - LISS-0069: an independent re-verification of the report's own key
    citations, plus the Antigravity registry-entry addition to
    `docs/collaboration/prompt-instruction-change-control.md`.
- Out:
  - No redesign of ADR 0016/0017's own topology.
  - No new mirror file for Codex or Antigravity (both read `AGENTS.md`
    natively — the survey's own finding, not a gap to fill).
  - No content change to `.cursor/rules/*.mdc` or `.grok/rules/*.md` —
    both confirmed current by the survey (checker-parity pass plus
    primary-source re-verification of the underlying mechanism).
  - Live-testing inside any tool other than Claude Code — out of this
    session's own reach, named as a limitation, not attempted.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0069 | ready | M | M | N/A | - | - | process/item-0021-status-survey |

## Recommended Order

1. LISS-0069 (the only remaining issue — the status report and spike
   case are already committed as this work plan's own opening artifacts).

## Current Next Issue

- Issue: LISS-0069
- Reason it is unblocked: the spike (`case-0004`) is closed; every piece
  of content LISS-0069 must insert is specified verbatim in its own
  Acceptance Notes.
- Reopening request needed: no.

## Minor Fix Path

Not applicable — LISS-0069 edits an agent operating contract file under
ADR 0006; contract-file changes are never self-reviewed and always
require a separate-context Reviewer plus a trace, regardless of size.

## Preflight Validation

Recorded by the Implementation group, LISS-0069 self-reviewed and
complete, on branch `wp-0025-execution` (commit `76d04e4`, branched from
`process/item-0021-status-survey` at `7d61ab5`). Result: **pass**.

1. **Independent URL re-fetches** (LISS-0069's own Acceptance Notes
   requirement):

   - `https://ai.google.dev/gemini-api/docs/antigravity-agent` — found:
     "you can mount files like `AGENTS.md` for instructions and skills
     under `.agents/skills/` directly into the sandbox." Matches
     `docs/architecture/ai-tool-support-status.md` and
     `docs/spike/case-0004-.../case.md` exactly.
   - `https://antigravity.google/docs/subagents/` — found: "A maximum
     nesting depth of **10 levels**... is strictly enforced," and
     "Agents can communicate with parent agents, subagents, or peer
     agents whose ID is known." Matches both source documents exactly,
     word for word.
   - **Confirmation, no discrepancy.** Full detail in
     `docs/issues/LISS-0069-antigravity-contract-registry-entry.md`'s
     Work Notes.

2. **`python3 scripts/check-contract-consistency.py`** — full output:

   ```text
   references:
     docs/architecture/ai-tool-support-status.md:67 names '.cursor/worktrees.json', which does not exist
     docs/architecture/ai-tool-support-status.md:91 names 'github.com/xai-org/grok-build/.../16-subagents.md', which does not exist
     docs/architecture/ai-tool-support-status.md:110 names 'ANTIGRAVITY.md', which does not exist

   contract consistency: 3 failure(s)
   ```

   These 3 failures are **pre-existing**, confined entirely to
   `docs/architecture/ai-tool-support-status.md` (out of LISS-0069's own
   scope; already committed at `7d61ab5`, this work plan's own opening
   commit, before LISS-0069 started). Confirmed via `git stash` A/B
   comparison: byte-identical checker output with and without
   LISS-0069's changes staged. **No regression introduced by LISS-0069.**
   The 3 failures are the checker's `check_references` path-existence
   check flagging backtick-quoted strings that are not actual repository
   file paths (a Cursor-side config filename mentioned in prose, a
   GitHub URL fragment, and a hypothetical filename the source document
   explicitly states was *not* found) — not a broken cross-reference.
   Not fixed here: the owning file is outside LISS-0069's scope by this
   work plan's own explicit boundary. Named here as a candidate follow-up
   item, not resolved by this work plan.

3. **`git diff` scope check** — confined to exactly the three permitted
   files:

   ```text
    docs/collaboration/prompt-instruction-change-control.md           |   5 +
    docs/issues/LISS-0069-antigravity-contract-registry-entry.md      | 113 +++++-
    docs/collaboration/traces/2026-08-20-ai-tool-support-status-survey.md | new file
   ```

   No other file touched by LISS-0069's own commit (`76d04e4`).

**Result: pass.** Permits submission to the independent, separate-context
Reviewer. This is not itself an approval and does not set any issue to
`wont_do` or `closed` beyond LISS-0069's own `done` status already
recorded in its own file.

## Review Summary Packet

Filled in by the Implementation group once Preflight passes.

- **Scope**: delivered the status report and spike case (already
  committed), and added Antigravity's `AGENTS.md`-native status to
  `docs/collaboration/prompt-instruction-change-control.md`.
- **Current canonical documents**:
  `docs/architecture/ai-tool-support-status.md` is a new, current
  reference document; `prompt-instruction-change-control.md` is amended
  in place (one bullet, one table row), not superseded.
- **Changed files**: `docs/collaboration/prompt-instruction-change-control.md`,
  the new trace file, `docs/issues/LISS-0069-...md`, this work plan's own
  file. (`docs/architecture/ai-tool-support-status.md` and
  `docs/spike/case-0004-...md` land in this work plan's own opening
  commit, not as part of LISS-0069's own diff.)
- **Findings**: none opened or resolved by this work plan.
- **Disposition**: Preflight Validation passed. LISS-0069 is
  self-reviewed (full form, planning size M) and complete on branch
  `wp-0025-execution` (commit `76d04e4`). Ready for the work-plan-level
  Reviewer pass, in a separate context.
- **Remaining blockers**: none found. The 3 pre-existing
  `check-contract-consistency.py` failures in
  `docs/architecture/ai-tool-support-status.md` are out of LISS-0069's
  own scope and were confirmed (via `git stash` A/B comparison) to
  predate this work plan's LISS-0069 diff entirely — not a blocker this
  work plan introduced, though worth flagging to the Reviewer as a
  candidate follow-up item outside this work plan's own boundary.
- **Verification result**: see this file's own "Preflight Validation"
  section above (populated 2026-08-20) for the full pasted output of all
  three required checks.
- **Next approval required**: evidence-sufficiency (are the report's own
  claims genuinely sourced and independently re-confirmed, not merely
  asserted) and boundary-conformance (does the contract-file edit stay
  within its own narrow, specified scope).

## Work-Plan Review

Reviewer's approval record: <link, filled in after the Reviewer pass>

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves — not performed
by the Design & Review group itself.

- Date:
- Result read:
- Next direction:
- New design agreement (if any):

## Risks

- The status report was drafted by the same Design & Review context that
  ran the underlying spike, rather than a fully separate context — this
  is normal for spike/research deliverables (the spike itself is Design &
  Review's own job, per `docs/spike/README.md`), but this work plan
  deliberately requires an independent re-fetch of the report's own key
  citations (LISS-0069's own Acceptance Notes) as a genuine falsification
  check, and the work-plan-level Reviewer independently re-verifies again
  — not a single-context rubber stamp at either layer.
- Antigravity's own documentation is newer and less stable than the other
  four tools' — a sooner-than-usual re-check cadence is a reasonable
  future expectation, named in the spike's own "Open risks after close,"
  not a defect in this work plan.

## Verification Plan

- Independent URL re-fetch confirming the report's own key citations.
- `python3 scripts/check-contract-consistency.py` — no regression.
- `git diff` confined to the stated scope.
- Independent work-plan-level Reviewer approval, in a separate context.
