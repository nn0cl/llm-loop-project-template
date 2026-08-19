# LISS-0041: Self-directed branch/worktree cleanup rule at merge time

## Metadata

- Local issue ID: LISS-0041
- GitHub issue: none
- Status: proposed
- Phase: phase-0-design
- Type: architecture
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A
- Owner/agent: unassigned (persona: Implementer)
- Related branch: process/copy-target-refs-and-branch-cleanup

## Summary

- Contract file: `docs/collaboration/branch-commit-pr-discipline.md`
  (governed by ADR 0006).
- Across WP-0002 through WP-0011, every Implementation and Design & Review
  sub-agent left its own worktree and branch behind after its content
  merged upstream; by WP-0011's close, 11 worktrees and over a dozen
  redundant branches had accumulated, cleaned up once, manually, by the
  Backlog thread — not as each work plan actually closed.
- Add a rule: once a session's branch has been merged into whatever it was
  feeding (Implementation into Design & Review's branch; Design & Review's
  branch into the shared `process/*` branch), removing the now-redundant
  branch and worktree is that same session's own next step, performed
  immediately once it confirms its own content has landed — not something
  a later thread sweeps up.
- Placement: extend the existing "Implementation-group worktree, per work
  plan" subsection's "When removed" bullet to state *who* removes it (the
  session whose content it held) and *when in that session's own flow* (as
  part of the same completion step, immediately after confirming the merge
  landed), and add a short new subsection generalizing the same expectation
  to the Design & Review group's own working branch — the existing
  subsection is scoped to the Implementation group only.
- Do not change existing branch-naming or PR rules, and do not change the
  existing merge-timing rule (worktree removed after the branch merges or
  the work plan closes, whichever governs today) — this issue only makes
  explicit who performs the removal and when, closing the gap between
  "worktrees get removed eventually" and "worktrees get removed as part of
  the same session's own completion step."

## Acceptance Notes

- The document states, for both groups, that branch/worktree removal is a
  self-directed step at merge time, not a deferred sweep.
- No existing branch/PR rule is weakened or contradicted (in particular:
  the "not removed while issues in that plan are still in progress" timing
  constraint is preserved, not overridden).
- AI work trace filed under `docs/collaboration/traces/`, per
  `docs/collaboration/prompt-instruction-change-control.md`'s Traceability
  Rule, naming: which contract file changed, why the change was needed,
  and what agent behavior is expected to change as a result.
- `scripts/check-contract-consistency.py --repo .` clean pass (mirror
  parity and references checks are the ones this change could plausibly
  affect; `branch-commit-pr-discipline.md` is referenced, not mirrored, by
  `AGENTS.md`/`CLAUDE.md`/etc., so no new `EXTRA_MIRRORED_RULES` entry is
  required — confirmed by inspection, not assumed).
- Self-review recorded (short form — planning size S, single contract-file
  addition).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/work-plans/WP-0012-copy-target-refs-and-branch-cleanup.md
- Depends on: none
- Blocks: none
- Related: `docs/backlog/item-0011-copy-target-references-and-branch-cleanup.md`,
  LISS-0024 (the existing Implementation-group worktree rule this issue
  extends), `docs/collaboration/cross-session-messaging.md`

## Decisions Not Settled by the Design Agreement

- None identified.

## Context

- Included: `docs/backlog/item-0011-*.md`, `DA-2026-08-19-04`,
  `docs/collaboration/branch-commit-pr-discipline.md` (whole file),
  `docs/collaboration/prompt-instruction-change-control.md` (whole file),
  `docs/collaboration/cross-session-messaging.md` (read for a possible
  cross-reference, not duplicated from).
- Omitted: the full WP-0002–WP-0011 history of which specific worktrees
  existed — the backlog item's own count (11 worktrees, over a dozen
  branches) is sufficient grounding; re-deriving the exact list is not
  needed to write a forward-looking rule.
- Assumptions: none beyond what is stated in Summary.

## AI Planning Records

### AIP-0041-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code, Design & Review group standing session
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A (not displayed in this environment)
  - N/A reason: this environment does not surface a reasoning-effort label
- Created at: 2026-08-19
- Planning size: S
- Intended execution route: direct edit of one contract file, plus a new
  trace file
- Compatibility state: N/A — documentation-only change, no code path
- Intended scope: `docs/collaboration/branch-commit-pr-discipline.md`,
  `docs/collaboration/traces/`
- Estimated token range: low thousands
- Estimated token midpoint: N/A (not tracked in this environment)
- Token metric: N/A
- Estimation basis: single contract file, bounded addition to one existing
  subsection plus one new subsection
- Assumptions: see Context above
- Confidence: high
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- N/A.

## Work Notes

- 

## Verification

- 
