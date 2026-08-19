# LISS-0041: Self-directed branch/worktree cleanup rule at merge time

## Metadata

- Local issue ID: LISS-0041
- GitHub issue: none
- Status: done
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

- `docs/collaboration/traces/2026-08-19-liss-0041-branch-worktree-cleanup-rule.md`
  (AI work trace required by the Traceability Rule, since this issue changes
  an ADR-0006 contract file).

## Work Notes

- Persona: Implementer.
- Fix: extended `docs/collaboration/branch-commit-pr-discipline.md`'s
  existing "Implementation-group worktree, per work plan" subsection with a
  new "Who removes it, and when" bullet, and added a new subsection,
  "Self-directed branch and worktree cleanup at merge time", generalizing
  the same rule to the Design & Review group's own working branch merging
  into the shared `process/*` branch, per `DA-2026-08-19-04`'s placement
  decision. Neither addition changed the existing merge-timing constraint
  (worktree/branch removed after merge or work-plan close, whichever is
  first; never while issues in that plan are still in progress) — both
  restate it, then add who performs the removal and when in that session's
  own flow.
- Judgment call (own, per Invariant 3): added a one-sentence
  cross-reference to `docs/collaboration/cross-session-messaging.md` at the
  end of the new subsection, rather than omitting it or duplicating its
  content. Read that file first, per the parent task's own instruction —
  it documents the `SendMessage`/`ListAgents` handoff protocol and the
  two-group topology the new rule generalizes over, but does not itself
  discuss branch/worktree cleanup, so the cross-reference is a pointer for
  readers who want the full handoff context, not a dependency needed to
  understand the rule itself (the rule is fully self-contained without
  opening that file). Full reasoning recorded in this issue's own trace,
  under "Decisions Carried".
- AI work trace filed: see References above.

### Self-review (short form, planning size S)

Phase / finding: Architecture Path, single contract-file addition (no
Red/Green/Refactor — documentation-only change, per this issue's own AI
Planning Record).

Command run: `python3 scripts/check-contract-consistency.py --repo .`

Result (actual pasted output, after the edit):

```
contract consistency: all checks passed
```

Risks considered:
- The new rule contradicts or weakens the existing "when removed" timing
  constraint already stated in the Implementation-group worktree
  subsection (the exact falsification criterion `DA-2026-08-19-04` names).
- The change trips `check_mirror_parity` or `check_parity_completeness`,
  since `branch-commit-pr-discipline.md` is read by agents but its content
  is not one of the files `check-contract-consistency.py` treats as a full
  mirror.
- The contract-file change lands without its required trace or without a
  separate-context Reviewer approval.
- A new `EXTRA_MIRRORED_RULES` entry is silently needed because
  `branch-commit-pr-discipline.md` is referenced by, or partially
  duplicated into, `AGENTS.md`/`CLAUDE.md`/etc.

Why each does not occur:
- Read the new text directly against the pre-existing "When removed" bullet
  and the pre-existing "not removed while issues in that plan are still in
  progress" sentence: both are quoted/restated verbatim in the new
  material, never replaced or narrowed. The new bullet and subsection only
  add who performs the removal and when in that session's own flow — no
  existing sentence was deleted or reworded to say something different.
- `branch-commit-pr-discipline.md` is not a key in `FULL_MIRRORS` in
  `scripts/check-contract-consistency.py`, and none of
  `MIRRORED_SECTIONS`/`AGENTS_ONLY_SECTIONS`/`EXTRA_MIRRORED_RULES` names
  it — confirmed by direct inspection of that script's configuration
  section, not assumed. `check_mirror_parity` and `check_parity_completeness`
  both operate over `AGENTS.md` and the files in `FULL_MIRRORS`, neither of
  which this change touched.
- This issue's own Reference section names the trace file, and this
  Work Notes section records the same three required contents the
  Traceability Rule asks for (which file changed, why, what agent
  behavior changes) — cross-checked against
  `prompt-instruction-change-control.md`'s exact wording immediately before
  writing this record. Status stays `review`, not `done`/`closed`, per this
  session's own instructions — the separate-context Reviewer approval is
  still pending.
- Ran `python3 scripts/check-contract-consistency.py --repo .` after the
  edit (pasted above): `contract consistency: all checks passed`, with no
  new "mirror parity" failure — confirmed by running the actual command,
  not by reasoning about `EXTRA_MIRRORED_RULES`'s contents alone, per this
  issue's own Acceptance Notes instruction to verify rather than assume.

## Verification

- Read-through of the new rule against the Traceability Rule's three
  required contents (which file, why, what changes) — satisfied, see the
  trace file and Work Notes above.
- Read-through of the new rule against the existing merge-timing
  constraint — not weakened or contradicted, see Risks/Why above.
- `python3 scripts/check-contract-consistency.py --repo .`:
  `contract consistency: all checks passed` (mirror parity and references
  both unaffected) — pasted above.
- Work-plan-level Reviewer approval:
  `docs/collaboration/reviews/2026-08-19-wp-0012-copy-target-refs-and-branch-cleanup-review.md`
  (Approved). The Reviewer independently confirmed the new text preserves
  the pre-existing merge-timing constraint verbatim and that the trace
  satisfies `prompt-instruction-change-control.md`'s exact wording.
