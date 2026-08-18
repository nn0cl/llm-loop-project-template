# LISS-0033: Create the living design & review perspectives document

## Metadata

- Local issue ID: LISS-0033
- GitHub issue: none
- Status: review
- Phase: phase-0-design (new contract document, no application code)
- Type: process-document
- Priority: high
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/quality-gate-hooks-and-coverage-policy (executed
  on LISS-0032's branch, not the originally planned
  `process/design-review-perspectives-doc` — see Work Notes for why)

## Summary

- Create `docs/collaboration/design-review-perspectives.md` (a new
  ADR-0006 contract file), organized by named, generalizable *perspective*
  (not chronologically by finding), seeded with at least 3 real
  perspectives distilled from this repository's own actual
  `docs/collaboration/reviews/*.md` history — read a representative sample
  (at minimum the 2026-08-02 contract-consistency review series and the
  2026-08-18 WP-0002/WP-0003 reviews) and generalize genuine findings from
  them, not invented examples. Each entry states: the perspective, when to
  apply it, and the originating finding(s)/review(s) it was distilled from
  (linked). Explicitly states how this document differs from
  `docs/collaboration/findings-reuse.md` (generalized perspectives vs.
  per-finding issue tracking) without duplicating its lifecycle rules.
- Wire the new document into required reading:
  `docs/architecture/agent-quickstart.md`'s "Required Area Documents" and
  `CLAUDE.md`'s reading list, alongside
  `docs/collaboration/source-code-quality.md`, per item-0006's own
  "becomes required reading during design intake" requirement.

## Acceptance Notes

- At least 3 real, generalizable perspectives, each traced to a real
  finding/review record (link, not invented).
- Document structure supports refinement (merging new evidence into an
  existing perspective) rather than only chronological appending — state
  this explicitly as the document's own editing rule, near its top.
- No duplication of `findings-reuse.md`'s lifecycle
  (`proposed -> accepted -> in_progress -> resolved -> closed`) — this
  document is not a tracker.
- `docs/architecture/agent-quickstart.md` and `CLAUDE.md` both list the new
  document.
- `scripts/check-contract-consistency.py` passes (new file's references
  resolve; it is correctly picked up by the mirror/reference checks the
  script runs).
- AI work trace(s) exist for every contract file touched by this issue
  (the new document itself, and `CLAUDE.md`).
- Self-review recorded (full form).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0006-quality-gate-hooks-and-review-perspectives-doc.md
- Depends on: LISS-0032 (cites ADR 0018 by number)
- Blocks: none
- Related: `docs/collaboration/findings-reuse.md`,
  `docs/collaboration/source-code-quality.md`

## Decisions Not Settled by the Design Agreement

- Exact wording/selection of which 3+ perspectives to seed is left to the
  Implementer's judgment, bounded by "real, traced to actual review
  records" — this is execution-level curation, not a planning ambiguity.

## Context

- Included: ADR 0018 (once LISS-0032 lands), `DA-2026-08-18-05`,
  `docs/collaboration/findings-reuse.md`,
  `docs/collaboration/source-code-quality.md`,
  `docs/architecture/agent-quickstart.md`, `CLAUDE.md`, a representative
  sample of `docs/collaboration/reviews/*.md`.
- Omitted: every review record in full detail — read for the generalizable
  lesson, not reproduced verbatim.
- Assumptions: LISS-0032's ADR exists and is stable before this issue
  starts (enforced by the dependency above).

## AI Planning Records

### AIP-0033-001

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
  one new document plus two required-reading-list edits
- Compatibility state: Verified — confirmed via directory listing that
  `docs/collaboration/reviews/` has a real, substantial history to distill
  from (2026-08-02 and 2026-08-18 series)
- Intended scope: `docs/collaboration/design-review-perspectives.md`
  (new), `docs/architecture/agent-quickstart.md`, `CLAUDE.md`
- Estimated token range: 6,000-14,000 tokens
- Estimated token midpoint: 9,000
- Token metric: approximate output tokens, dominated by reading review
  history and drafting the new document
- Estimation basis: comparable to a mid-sized new contract document plus
  two small wiring edits
- Assumptions: single execution attempt
- Confidence: medium
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/collaboration/agreements/2026-08-18-quality-gate-hooks-and-perspectives-doc.md`
  (`DA-2026-08-18-05`)
- `docs/collaboration/findings-reuse.md`

## Work Notes

- 2026-08-18 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0006-*.md`'s promotion. Dispatched to the
  Implementation group together with LISS-0032.
- 2026-08-18 (Implementer, Implementation group): executed on
  `process/quality-gate-hooks-and-coverage-policy` (the same branch as
  LISS-0032), not a separate `process/design-review-perspectives-doc`
  branch as this issue's own metadata originally named. Per the task
  handoff's explicit direction, both LISS-0032 and LISS-0033 are
  sequential, dependent issues (this issue cites LISS-0032's ADR 0018 by
  number) and were executed on one reviewable branch, mirroring how
  WP-0004's Implementer handled its own two sequential issues. Updated this
  issue's "Related branch" field above to reflect what actually happened
  rather than leaving a stale plan value.
- Read the five review records named in this issue's own Context/reading
  list (`2026-08-02-contract-consistency-review.md` through `-review-4.md`,
  and `2026-08-18-wp-0002-two-group-send-message-loop-review.md`) in full
  before drafting any perspective, per this issue's Acceptance Notes
  ("not invented examples"). Distilled four perspectives, each with a
  direct quote or close paraphrase from the specific review record it
  traces to (see `docs/collaboration/design-review-perspectives.md` itself
  for the full text and citations, and the LISS-0033 trace for a summary).
  Did not use the two illustrative perspective names quoted in
  `DA-2026-08-18-05`'s own "Perspectives document format" Settled-Ambiguity
  row ("verify claimed authority independently of its own claim," "a
  numeric target invites shaping the artifact to hit the number rather
  than to be correct") as literal titles to copy — the first is genuinely
  present in the WP-0002 review's "Provenance verification" section and
  became this document's fourth perspective in its own words; the second
  does not trace to any of the five sampled review records' actual text
  (it describes a coverage-gaming concern that belongs to ADR 0018 itself,
  not to a finding these specific review records made), so it was not used,
  per this issue's own instruction to verify each candidate is actually
  present before using it.

### Self-review (full form, planning size M)

**Command run:**

```text
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```

**Result:** passes cleanly, including all four of the new document's
`docs/collaboration/reviews/*.md` cross-references and the two
required-reading wiring edits (`agent-quickstart.md`, `CLAUDE.md`).

**Risks considered, and why each does not occur:**

1. *Are the perspectives document's entries actually traceable to real
   text, not paraphrased into something the source doesn't say?* Re-opened
   all five source review records immediately before writing this
   self-review and re-checked each of the four perspectives' quoted
   fragments word-for-word against the source: "the force-push the
   coordinator mentioned did not invalidate anything this record relies
   on" (round 2, Method) and the independent `git merge-base
   --is-ancestor` checks in rounds 2-4; "attacked the two surviving range
   rules (especially the separator whitelist, per the coordinator's own
   stated distrust of it)" (round 4, Method, verbatim); "the disclosure is
   written by the context that built the fix, and it names the limits that
   context could see, not the ones adversarial testing finds" (round 3,
   verbatim, inside the "Judging the disclosure" subsection); the
   "Provenance verification" section's full text (WP-0002 review, verbatim
   quotes preserved). No fragment was invented or stretched beyond what
   the source states. Does not occur.
2. *Does the document avoid duplicating `findings-reuse.md`'s lifecycle?*
   Re-read the "How this differs from `findings-reuse.md`" section against
   `findings-reuse.md`'s own "Must-apply rule" (the
   `proposed -> accepted -> in_progress -> resolved -> closed` lifecycle):
   confirmed the new document uses no status field, no lifecycle verb, and
   states explicitly that a perspective "has no status, no lifecycle, and
   is not closed when a finding is fixed." Does not occur.
3. *Does the document's own "how it is edited" rule actually support
   merge-not-append in practice, or is it aspirational prose with no
   structural backing?* Checked that each perspective is its own
   independently-editable `###` section with stable fields ("The lens,"
   "When to apply it," "Originating finding(s)/review(s)") that a future
   edit can extend in place, rather than a single running list or table
   that would structurally invite appending. Does not occur as a
   structural gap, though whether a future agent actually follows the rule
   in practice cannot be verified by this review — this is a documentation
   convention, not a mechanically enforced one, which the Reviewer pass
   should note as a residual, accepted risk rather than a defect in this
   issue's own deliverable.
4. *Does `CLAUDE.md`'s edit place the new line in a way consistent with
   the existing `source-code-quality.md` line's style, without disturbing
   any other line in the reading-sequence list?* Diffed `CLAUDE.md`: the
   only change is one inserted line, immediately after the
   `source-code-quality.md` line, in the same "- Label:
   `path`." format as every neighboring line; no other line in the list
   was reordered, reworded, or removed. Does not occur.
5. *Does the `agent-quickstart.md` edit correctly avoid claiming a trace is
   required for that file?* Re-read
   `docs/collaboration/prompt-instruction-change-control.md`'s Agent
   Operating Contract Files list directly (not from memory of the task
   instructions) before deciding: `docs/architecture/*.md` is absent from
   that list, so `agent-quickstart.md` is not a contract file and no trace
   is strictly required for its edit alone; the trace for this issue
   (`docs/collaboration/traces/2026-08-18-liss-0033-perspectives-doc-and-required-reading.md`)
   names the edit anyway, for completeness, and states explicitly that it
   is not ADR-0006-required for that one file. Does not occur as a
   miscategorization.

## Verification

```text
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
