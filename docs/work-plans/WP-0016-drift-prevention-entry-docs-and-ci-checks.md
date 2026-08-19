# Work Plan: Drift-Prevention Entry Documents and CI Checks (Scoped)

## Goal

- Close item-0012 facet 5's two most tractable deterministic checks (no
  retired terminology; no Archive document referenced from an Entry
  document), the Entry-document content requirement, and
  `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`, per
  `docs/backlog/item-0012-document-and-log-lifecycle-management.md` and
  `docs/collaboration/agreements/2026-08-19-drift-prevention-entry-docs-and-ci-checks.md`
  (`DA-2026-08-19-08`). The two harder checks facet 5 also names
  (single-canonical-per-theme, canonical-document-source-link) are
  explicitly deferred — see the design agreement's Deferred Questions.

## Scope

- In: `docs/collaboration/terminology-migration.md` (new),
  `scripts/check-contract-consistency.py` (two new check functions, a
  `RECORD_DIRS` entry, docstring update, `main()` registration),
  `docs/architecture/agent-quickstart.md` (new section),
  `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md` (closed),
  the synthetic-case verification (created and removed within this work
  plan, not left in the tree), the required AI work trace, self-review,
  Preflight, work-plan-level Reviewer pass.
- Out: the single-canonical-per-theme and canonical-source-link checks
  (deferred); any `docs/archive/` content actually persisting after this
  work plan closes; `CLAUDE.md` or its four mirrors; facet 6
  (review-summary packets); the retroactive-application work plan.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0048 | ready | M | M | AIP-0048-001 | - | - | process/drift-prevention-entry-docs-and-ci-checks |

## Plan-Owned Bug Records

None.

## AI Planning Records

See LISS-0048's own AIP-0048-001 (required, planning size `M`).

## Recommended Order

1. LISS-0048 (single issue).

## Current Next Issue

- Issue: LISS-0048
- Reason it is unblocked: no dependencies; `DA-2026-08-19-08` covers it
  fully, including exact code for both new checks.
- Reopening request needed: no.

## Minor Fix Path

Does not apply — this adds new deterministic checks and new contract
content, not a correction to an existing defect (except incidentally
closing LISS-0044, which is itself folded into this work plan's own full
design-agreement cycle rather than run as a separate Minor Fix Path
correction, since it shares one cohesive branch/verification unit with
the rest of this issue).

## Preflight Validation

- Result: `pass`
- Checks and command output:

  ```console
  $ python3 scripts/check-contract-consistency.py
  contract consistency: all checks passed
  ```

  Exit code: 0. First real-tree run (Implementer's own Task 4) correctly
  `fail`ed: the design agreement's own File 2 and File 3 contradicted
  each other — `check_no_archive_reference_from_entry`'s original bare
  substring match flagged File 3's own legitimate abstract mention of
  `docs/archive/`. `DA-2026-08-19-08` was amended with a corrected,
  file-shaped-path regex (`ENTRY_ARCHIVE_REFERENCE`), sent back to the
  same Implementation-group session, and re-applied (commit `d9fe2a2`).
  This run is against the merged result, independently re-verified in
  this worktree (fetched the Implementer's actual branch directly,
  diffed it against the corrected agreement text — matched exactly —
  before merging).
- Scope result: `git diff 3ae03d6..HEAD --stat` (`3ae03d6` is this work
  plan's own design-intake commit) shows exactly 7 files: this design
  agreement (the correction), the new terminology-migration table, the
  script edit, the agent-quickstart.md addition, the new trace file,
  LISS-0044 (closed), and LISS-0048's own Work Notes. `find docs/archive`
  confirms no `docs/archive/` path exists anywhere in the tree — the
  synthetic verification case was fully removed. No `CLAUDE.md`/mirror
  file touched. No open `Type: review-finding` issue affects this area.
- Next action: submit to the Design & Review group's work-plan-level
  Reviewer pass, in a context separate from both the Planner/Specifier
  context that wrote the design agreement and the Implementer context
  that transcribed and corrected it.

## Work-Plan Review

Reviewer's approval record:
`docs/collaboration/reviews/2026-08-19-wp-0016-drift-prevention-entry-docs-and-ci-checks-review.md`
— **Approved**, separate-context Reviewer session, all three constraints
satisfied. 18 failure scenarios searched (mechanical transcription
accuracy, LISS-0044's own resolution independently reconstructed from
scratch, and active attempts to break both new checks — not merely
confirming the Implementer's own test cases). Two real, reproducible gaps
found and made a binding condition of the Approval: `check_retired_terminology`'s
plain substring match could produce a large false-positive blast radius
for a short/common retired term (389 failures on the Reviewer's own
constructed case); `check_no_archive_reference_from_entry`'s per-line-only
scan misses a genuine reference split across a hard line-wrap (this
repository's own dominant prose convention). Both are latent (no-ops
against real content today) — same disposition as `LISS-0044`. Opened as
`LISS-0049` and `LISS-0050`.

`LISS-0049`'s word-boundary fix was confirmed Approved by a
separate-context Reviewer (`docs/collaboration/reviews/2026-08-19-liss-0049-liss-0050-word-boundary-and-line-wrap-fix-review.md`),
independently re-tested against a different, more adversarial real-tree
case (132 real files) than this work plan's own evidence — closed, with
one narrower follow-up condition (punctuation-edged retired terms) opened
as `LISS-0051` and resolved via a guidance-text mitigation.

`LISS-0050`'s first fix attempt (no-separator line concatenation) was
**Rejected** by that same Reviewer pass, which independently found and
reproduced a genuine new false positive (flagging a docstring-permitted
bare abstract mention of `docs/archive/` when followed by unrelated
next-line prose) and a silent under-suppression bug in its own
de-duplication logic. A corrected second attempt — backtick-delimited
cross-line matching, using this repository's own convention that every
specific-file reference is backtick-bounded — was applied and confirmed
Approved by a fresh separate-context Reviewer
(`docs/collaboration/reviews/2026-08-19-liss-0050-attempt2-liss-0051-review.md`),
which independently re-tested both of Attempt 1's defects with its own
wording plus additional adversarial probes (chained cross-line matches,
double-backtick escapes, a fenced code block) — closed, with one new,
narrower gap found (a reference split inside a fenced code block, not
inline backticks) opened as `LISS-0052` and deliberately left tracked
rather than actioned in this same correction cycle, per that issue's own
Disposition section (narrow practical exposure; a third immediate
correction round on the same function risks the kind of rushed fix
Attempt 1 turned out to be).

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
| LISS-0049 | closed | `check_retired_terminology` now matches with a word-boundary-anchored regex instead of a bare substring test; `terminology-migration.md` gained a caution against choosing an overly short/common retired term. Confirmed by a separate-context Reviewer with independently constructed evidence. |
| LISS-0050 | closed | Attempt 1 (no-separator line concatenation) Rejected by Reviewer — new false positive, under-suppression bug. Attempt 2 (backtick-delimited cross-line matching) applied and confirmed Approved by a fresh separate-context Reviewer, with independently worded reconfirmation of both Attempt-1 defects and further adversarial probing. |
| LISS-0051 | closed | `terminology-migration.md`'s guidance now warns against a retired term starting/ending in punctuation (word-boundary semantics can silently fail to match, or invert). Confirmed by a separate-context Reviewer against real `re.search` behavior. |

`LISS-0052` (the fenced-code-block gap the LISS-0050 Attempt-2 Reviewer
found) is intentionally **not** listed in the table above — it is a real,
tracked finding, but deliberately deferred rather than immediately
actioned (see its own Disposition section), the same disposition
`LISS-0044` originally received from WP-0014's Reviewer. All three
findings actually required to close this work plan are `closed`, so no
open finding blocks Director close.

## Work-Plan Close

- Date: 2026-08-20
- Result read: the Director read the Reviewer approval
  (`docs/collaboration/reviews/2026-08-19-wp-0016-drift-prevention-entry-docs-and-ci-checks-review.md`,
  Approved after three adversarial review rounds that caught two genuine
  bugs — a word-boundary false-positive and a line-wrap detection gap,
  both fixed and independently re-verified) via the Backlog thread, which
  independently confirmed the two new checks, LISS-0044's closure,
  LISS-0049/0050/0051's `closed` status, LISS-0052 correctly left
  non-blocking and tracked, and a clean
  `scripts/check-contract-consistency.py` run from a detached checkout.
- Next direction: closed with "クローズして". Merged content sits on
  `origin/process/item-0012-remaining-facets` (together with facet 6,
  still in progress — not itself approved by this close). Push/PR/
  merge-to-main remain separate explicit actions, deferred to a suitable
  batch point.
- New design agreement (if any): none opened by this close — the deferred
  checks (LISS-0052 and the three unbuilt facet-5 checks) and facet 6 each
  get their own when reached.

## Risks

- Medium (planning size `M`, new deterministic-check code — the class of
  change this repository's own review history shows is easiest to get
  subtly wrong, per `docs/collaboration/design-review-perspectives.md`'s
  precedent from the original `check-contract-consistency.py` review
  series). Mitigated by: exact code specified in the design agreement
  (Implementer transcribes, does not design), mandatory synthetic-case
  verification per check (not just a clean real-tree run), and a
  work-plan-level Reviewer pass that independently re-derives whether the
  new checks' own regexes/logic could produce a false positive or false
  negative, not only whether they currently pass.
