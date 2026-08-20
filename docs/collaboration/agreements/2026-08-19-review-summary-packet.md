# Design Agreement: Review Summary Packet

## Identity

- Agreement ID: DA-2026-08-19-09
- Date: 2026-08-19
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code, Design & Review group standing session
- Supersedes agreement (if any): none.

## Direction

Per `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
(`Status: promoted`) facet 6 ("Review records as summary packets"), whose
Promotion notes are this agreement's Director authorization under ADR 0016
Rule 2: give the work-plan-level Reviewer, as its canonical review input,
a small structured packet — scope, current canonical documents, changed
files, findings, disposition, remaining blockers, verification result,
next approval required — with detailed traces linked as evidence for
falsification, not the review's own entry point. This closes item-0012's
last rule-defining facet; facets 1-5 already closed via WP-0014 through
WP-0016.

## Scope

- In scope:
  - `docs/templates/work-plan.md`: a new "## Review Summary Packet"
    section, exact content in "Exact Content to Produce" -> "File 1"
    below, positioned between the existing "Preflight Validation" and
    "Work-Plan Review" sections.
  - `docs/collaboration/design-agreement.md`: a new "## Review Summary
    Packet" section, exact content in "File 2" below, positioned between
    the existing "Reopening the agreement" and "Closing a work plan"
    sections.
  - The required AI work trace (both files are ADR-0006 contract files).
- Explicitly out of scope:
  - A separate `docs/templates/review-summary-packet.md` template file —
    the packet is embedded as a section within the existing work plan
    document, matching this repository's own established convention
    (e.g., "AI Planning Records" is an embedded work-plan section, not a
    separate template file).
  - Retroactively adding the packet section to any already-closed work
    plan (`WP-0013` through `WP-0016`) — a later, separate
    retroactive-application work plan's own concern, per item-0012's own
    Promotion notes.
  - Any edit to `CLAUDE.md` or its four mirrors.
  - Weakening the Reviewer's existing three constraints (context
    separation, deterministic precondition, falsification burden) — the
    new section explicitly preserves them; see Falsification Criteria.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Add the "Review Summary Packet" section to `docs/templates/work-plan.md` | Implementer | Architecture Path (content fully specified; Implementer transcribes) | Matches "Exact Content to Produce" -> "File 1" verbatim, at the specified insertion point; no other part of the file changes | read-through diff |
| 2 | Add the "Review Summary Packet" section to `docs/collaboration/design-agreement.md` | Implementer | Architecture Path | Matches "File 2" verbatim, at the specified insertion point; no other part of the file changes | read-through diff |
| 3 | AI work trace | Implementer | Architecture Path | States both contract files changed, why, what agent behavior changes | trace file present |
| 4 | Self-review | Implementer | Architecture Path | Short-form self-review per `docs/templates/self-review.md` (size `S`), recorded in LISS-0053 Work Notes | self-review record |
| 5 | Preflight Validation | Implementer / deterministic tool | Architecture Path | `pass` recorded with `scripts/check-contract-consistency.py` output and an explicit scope check | Preflight section in WP-0017 |
| 6 | Work-plan-level Reviewer pass | Reviewer (Design & Review group, separate context) | Architecture Path | Review record confirms mechanical accuracy and that the new sections do not weaken the Reviewer's existing constraints | review record under `docs/collaboration/reviews/` |

Sequencing: Tasks 1 and 2 may proceed in either order (independent
files). Both block Task 3. Task 3 blocks 4. Task 4 blocks 5. Task 5
blocks 6.

## Exact Content to Produce

### File 1: `docs/templates/work-plan.md` — new section

Insert this new section immediately after the existing `## Preflight
Validation` section (after its own paragraph, "`pass` permits submission
only; it never replaces the separate-context Reviewer.") and before `##
Work-Plan Review`:

```markdown
## Review Summary Packet

Filled in once Preflight Validation passes, before submitting to the
work-plan-level Reviewer — the Reviewer's own canonical review input, per
`docs/backlog/item-0012-document-and-log-lifecycle-management.md` facet 6
and `docs/collaboration/design-agreement.md`'s own "Review Summary
Packet" section. Detailed traces, self-reviews, and issue Work Notes are
linked as evidence for a deeper falsification search, not required
reading to start the review.

- **Scope**: what this work plan actually changed, in one or two
  sentences.
- **Current canonical documents**: which ADRs, contract files, or specs
  this work plan's content is now the current source for (or which
  existing ones it extends/amends).
- **Changed files**: the exact file list (new/edited/moved), matching
  the actual diff — not a paraphrase.
- **Findings**: any `Type: review-finding` issue this work plan resolved
  or opened, each with its own current status.
- **Disposition**: what happened — resolved cleanly, resolved with
  tracked follow-ups, blocked, etc.
- **Remaining blockers**: anything still open that could affect the
  Reviewer's decision.
- **Verification result**: the actual Preflight command output (or a
  pointer to its exact location in this same file), not a restated
  summary.
- **Next approval required**: which of the four approval types
  (specification-conformance, phase-correctness, boundary-conformance,
  evidence-sufficiency — per `CLAUDE.md`'s "Approval Model") this work
  plan actually needs, given what changed.
```

Do not change anything else anywhere in this file.

### File 2: `docs/collaboration/design-agreement.md` — new section

Insert this new section immediately after the existing `## Reopening the
agreement` section (after its own final paragraph, "Either the agreement
covers the case, or the agreement is reopened with the gap named.") and
before `## Closing a work plan`:

```markdown
## Review Summary Packet

Before the work-plan-level Reviewer pass — after Preflight Validation
passes, per `CLAUDE.md`'s "Work-Plan Review" — the work plan's own
"Review Summary Packet" section (`docs/templates/work-plan.md`) is
filled in as the Reviewer's canonical review input. Per item-0012 facet 6
("Review records as summary packets"): making the Reviewer read every
trace in full raises cognitive load without a matching audit benefit for
what changed since the last review. A Reviewer session should read the
packet first, and treat detailed traces, self-reviews, and issue Work
Notes as linked evidence to consult for falsification, not as the
review's own entry point.

This does not weaken the Reviewer's own falsification burden or the
deterministic-precondition/context-separation constraints in
`CLAUDE.md`'s "Constraints" — a Reviewer that finds the packet's own
claims insufficient, or needs to verify a specific detail, still reads
the underlying trace or issue file directly, the same way it would
independently re-run a deterministic check rather than trust a pasted
claim (per `docs/collaboration/design-review-perspectives.md`'s
"Re-verify state that could have changed underneath you"). The packet
changes where the review *starts*, not how rigorously it must actually
search.
```

Do not change anything else anywhere in this file.

## Specifications

- None. Documentation/process-governance change; no application
  specification.

## Boundaries

- Both touched files are ADR-0006 contract files — trace and
  separate-context Reviewer approval are mandatory.
- No retroactive application to any already-closed work plan.
- No edit to `CLAUDE.md` or its four mirrors.
- No push, PR, or merge to `main`; nothing marked `done`/`closed` (in the
  Director-facing sense) until the Director's own work-plan-close action.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Separate `docs/templates/review-summary-packet.md` file, or a section embedded in `work-plan.md`? | Embedded section — matches this repository's own established convention (e.g., "AI Planning Records" is an embedded work-plan section, not a separate template file) and keeps the packet physically next to the Preflight output it summarizes, in the same document a Reviewer already opens first. | Design & Review group (Planner) |
| Should this session's own prior Reviewer dispatches (WP-0013 through WP-0016, which told the Reviewer to read everything in full) be retroactively corrected? | No — out of scope, per item-0012's own explicit sequencing (rules first, retroactive application later, as its own separate work plan). The new convention applies going forward. | Design & Review group (Planner), per the Director's own sequencing decision at item-0012's promotion |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should a deterministic check verify a work plan's "Review Summary Packet" section is actually filled in (not left as template placeholders) before the Reviewer pass? | Not built now — this facet is a documentation/process convention, not a new CI check; item-0012's own facet 5 (drift-prevention CI checks) already covers the CI-check-building concern, and this section does not ask for one. Revisit only if a future work plan is found to have skipped filling in the packet despite this rule. |

## Verification

- `scripts/check-contract-consistency.py`.
- Read-through diff confirming both changes match "Exact Content to
  Produce" verbatim, and that no other repository file changed.
- Work-plan-level Reviewer approval, separate context.

## Falsification Criteria

- Either new section's wording states or implies that the Reviewer's
  three existing constraints (context separation, deterministic
  precondition, falsification burden) are weakened, optional, or
  satisfied by the packet alone without independent verification.
- Any already-closed work plan (`WP-0013` through `WP-0016`) is edited to
  retroactively add the new section.
- `CLAUDE.md` or a mirror file is edited.
- No AI work trace is recorded for this contract-file-touching work plan.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. Recorded basis:
      `docs/backlog/item-0012-document-and-log-lifecycle-management.md`,
      `Status: promoted`, Promotion notes, per ADR 0016 Rule 2.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Made fresh by the Design & Review group
      against this actual plan.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
