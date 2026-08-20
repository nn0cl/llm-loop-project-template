# Work Plan: Contract-Sync Diff Records and Per-Agent-Tool Rule Registry

## Goal

- Close item-0012 facet 4's diff-record and per-agent-tool-registry pieces
  by adding a structured Sync Diff Record template and a canonical
  Per-Agent-Tool Rule Applicability Registry, extending ADR 0008's
  already-existing Tier 1/Tier 2 sync mechanism rather than rebuilding it,
  per `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
  and
  `docs/collaboration/agreements/2026-08-19-contract-sync-diff-records.md`
  (`DA-2026-08-19-07`). Facet 4's own "split rules explicitly" wording is
  resolved as satisfied by the existing per-sync-event reconciliation
  process, now durably recorded by this work plan's own Sync Diff Record —
  see `docs/issues/LISS-0047-facet-4-template-target-split-granularity.md`
  (a Reviewer finding raised and resolved within this same work plan) for
  the full reasoning; no separate standing document was needed.

## Scope

- In: `docs/templates/sync-diff-record.md` (new), a new "Per-Agent-Tool
  Rule Applicability Registry" section plus a shortened cross-referencing
  edit to the existing Cursor bullet in
  `docs/collaboration/prompt-instruction-change-control.md`, one new
  cross-referencing paragraph plus a Step 6 addition in
  `docs/templates/contract-file-sync-prompt.md`, the required AI work
  trace (all three touched files are ADR-0006 contract files), self-review,
  Preflight, work-plan-level Reviewer pass.
- Out: any change to `docs/architecture/adr/0008-template-update-propagation.md`
  itself, `scripts/update-ai-collaboration-files.sh`,
  `scripts/copy-ai-collaboration-files.sh`, `CLAUDE.md`, or any of its
  four mirrors. No new ADR (see Settled Ambiguities in the covering
  agreement). Facets 5 (drift-prevention entry documents and CI checks)
  and 6 (review-summary packets) — later, separate work plans.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0046 | ready | M | M | AIP-0046-001 | - | - | process/contract-sync-diff-records |

## Plan-Owned Bug Records

None.

## AI Planning Records

See LISS-0046's own AIP-0046-001 (required, planning size `M`).

## Recommended Order

1. LISS-0046 (single issue).

## Current Next Issue

- Issue: LISS-0046
- Reason it is unblocked: no dependencies; `DA-2026-08-19-07` covers it
  fully, including exact content for all three files.
- Reopening request needed: no.

## Minor Fix Path

Does not apply — this adds new contract content (a new template file, a
new registry section), not a correction to an existing defect. Full
design-agreement + work-plan + Reviewer-pass cycle applies.

## Preflight Validation

- Result: `pass`
- Checks and command output:

  ```console
  $ python3 scripts/check-contract-consistency.py
  contract consistency: all checks passed
  ```

  Exit code: 0. Run by the Design & Review group after fast-forward-merging
  the Implementation group's branch `process/contract-sync-diff-records`
  (commit `10b19df`) into `process/item-0012-remaining-facets`.
- Scope result: `git diff a68563d..HEAD --stat` (`a68563d` is this work
  plan's own design-intake commit) shows exactly 5 files: the two edited
  contract files (`docs/collaboration/prompt-instruction-change-control.md`,
  `docs/templates/contract-file-sync-prompt.md`), the one new template
  file (`docs/templates/sync-diff-record.md`), the new trace file, and
  LISS-0046's own Work Notes addition. No edit to
  `docs/architecture/adr/0008-*.md`, any sync script, `CLAUDE.md`, or a
  mirror file. No open `Type: review-finding` issue affects this area
  (all `docs/issues/LISS-*.md` `Status` fields checked; LISS-0044 remains
  `proposed` but is unrelated to this work plan's own scope).
- Next action: submit to the Design & Review group's work-plan-level
  Reviewer pass, in a context separate from both the Planner/Specifier
  context that wrote the design agreement and the Implementer context
  that transcribed it.

## Work-Plan Review

Reviewer's approval record:
`docs/collaboration/reviews/2026-08-19-wp-0015-contract-sync-diff-records-review.md`
— **Approved**, separate-context Reviewer session, all three constraints
satisfied. 14 failure scenarios searched (9 mechanical, 5 substantive —
this review tested not only transcription accuracy but whether the
design agreement's central research claim actually held). One real,
substantive finding: `DA-2026-08-19-07`/`LISS-0046`/this work plan's own
Goal overstated that ADR 0008's Tier 1/Tier 2 split "already implements"
facet 4's Template-owned/Target-owned split — it addresses whole-file
authority, not the content-level rule split facet 4's wording describes.
Opened as `LISS-0047`; resolved within this same work plan by a wording
correction (Resolution 1: the existing per-sync-event process, now
durably recorded by the new Sync Diff Record, is judged sufficient and
intentional) and confirmed by a separate-context Reviewer under Minor Fix
Path (`docs/collaboration/reviews/2026-08-19-liss-0047-facet-4-split-wording-fix-review.md`,
Approved — the Reviewer independently examined the Resolution-1 judgment
itself, not only mechanical accuracy, and recorded it as "a genuinely
defensible reading... not the only reading," confirmed on the grounds
that the reasoning is sound and disclosed). Neither finding invalidates
the two artifacts WP-0015 actually built (Sync Diff Record, Per-Agent-Tool
Rule Applicability Registry), both correctly delivered to spec.

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
| LISS-0047 | closed | Wording correction applied to `DA-2026-08-19-07`, `LISS-0046`, and this work plan's own Goal, distinguishing ADR 0008's whole-file split from facet 4's content-level split and recording the Resolution-1 judgment; confirmed by a separate-context Reviewer under Minor Fix Path (Approved). |

## Work-Plan Close

- Date: 2026-08-20
- Result read: the Director read both Reviewer approvals
  (`docs/collaboration/reviews/2026-08-19-wp-0015-contract-sync-diff-records-review.md`
  and `docs/collaboration/reviews/2026-08-19-liss-0047-facet-4-split-wording-fix-review.md`,
  both Approved) via the Backlog thread, which independently confirmed the
  Sync Diff Record template, the Per-Agent-Tool Rule Applicability
  Registry, LISS-0047's `closed` status, and a clean
  `scripts/check-contract-consistency.py` run from a detached checkout.
  The Director was explicitly shown the disclosed ambiguity — a second
  Reviewer called the adopted facet-4 reading "defensible... not the only
  reading, and not the stronger of the two on the text alone" — and chose
  to proceed with it rather than redirect.
- Next direction: closed with "はい。クローズ". Merged content sits on
  `origin/process/item-0012-remaining-facets` (together with facets 5/6,
  still in progress — not themselves approved by this close). Push/PR/
  merge-to-main remain separate explicit actions, deferred to a suitable
  batch point.
- New design agreement (if any): none opened by this close — facets 5 and
  6 each get their own when reached.

## Risks

- Low-medium (planning size `M`). Main risk: scope creep into rebuilding
  ADR 0008's already-working Tier 1/Tier 2 mechanism instead of only
  extending it — explicitly fenced off in Scope and checked directly in
  Preflight's scope-result step. Secondary risk: the new registry table
  in `prompt-instruction-change-control.md` could drift from the actual
  current mirror-sync behavior if not kept in sync with future changes —
  named as a standing maintenance expectation in the new section's own
  text, not a one-time artifact.
