# Backlog item: item-0016-retroactive-adr-0020-lifecycle-application

## Metadata

- Item ID: item-0016
- Title: Retroactively apply ADR 0020's document/log lifecycle rules to
  this repository's own existing history
- Status: promoted
- Created: 2026-08-20
- Updated: 2026-08-20
- Priority hint: medium
- Suggested planning size: L
- Owner/agent (optional): unassigned

## Summary

ADR 0020 (`docs/architecture/adr/0020-document-and-log-lifecycle-model.md`,
landed via item-0012/WP-0014) defines the four-layer document model
(Entry/Canonical/Evidence/Archive), the `draft|active|canonical|
superseded|archived` status vocabulary, consolidation triggers, the
in-tree `docs/archive/` mechanism, and the restoration ledger — but no
existing document in this repository has actually been classified,
consolidated, or archived under it yet. `docs/collaboration/restoration-ledger.md`
is still empty.

This item is the deliberately-deferred second half of item-0012: apply
ADR 0020 to this repository's own existing history — most acutely, the
history this very session produced (WP-0001 through WP-0018, 50+ local
issues, a dozen-plus review records, a dozen-plus AI work traces, 15
backlog items, 20 ADRs), which is exactly the volume-growth pattern the
original `qpex` feedback (item-0012's own trigger) warned about.

Concretely, in scope:

- Classify existing `docs/architecture/adr/*.md`, `docs/issues/LISS-*.md`,
  `docs/work-plans/WP-*.md`, `docs/collaboration/traces/*.md`, and
  `docs/collaboration/reviews/*.md` files against the status vocabulary
  (which are `canonical`/`active` vs. candidates for `superseded`/
  `archived`).
- Apply the consolidation triggers ADR 0020 Rule 4 defines (a decided ADR
  superseded by a later one; a closed work plan's issues/traces with no
  further action; duplicate or near-duplicate records) to actually move
  qualifying records into `docs/archive/`, each with a restoration-ledger
  entry (`source_path, source_commit, source_tag, canonical_destination,
  classification, reason`).
- Confirm the drift-prevention checks from facet 5 (WP-0016) — including
  the still-not-fully-built three of the five originally proposed checks,
  per that work plan's own scope note — correctly validate the result once
  real archive content exists (this is also where `LISS-0044`'s
  `RECORD_DIRS` exclusion gap and `LISS-0052`'s fenced-code-block gap
  become concretely testable, not just theoretical).

## Why it might matter

Without this, ADR 0020 is a rule that exists but has never been exercised
— exactly the risk the Reviewer already flagged in WP-0014's own review
(LISS-0044): untested until something real needs it. This repository's own
history is now large enough (per item-0012's own "Why it might matter"
section) that applying the rules here is both a genuine need and the most
realistic test of whether the rules work as designed.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes
- Boundaries or non-goals:
  - Do not archive or reclassify anything from before this repository's
    own template-founding history (the original v1.0.0-era consolidation,
    commit `cf9da58`/`9fcb2d2`, already noted in WP-0007/LISS-0035's own
    `KNOWN_HISTORICAL_ID_REUSE` registry) without explicit care — that
    consolidation already happened once, under different rules; don't
    double-consolidate or contradict its own restoration story.
  - Do not change ADR 0020's own rules as part of applying them — if
    applying the rules surfaces a real gap or ambiguity in ADR 0020 itself,
    that is a reopening trigger / new backlog item, not something to
    silently patch mid-application.
  - Coordinate with `docs/backlog/item-0011-*.md`'s own branch-cleanup
    concerns and `docs/collaboration/branch-commit-pr-discipline.md` — this
    work will touch a large number of files across many commits; keep the
    same commit/branch discipline already established this session.

## Uncertainty

- [ ] Spec can be written now
- [x] Spike required first (options, feasibility, or quality unknown) —
      this repository's own history is large (50+ issues, dozens of
      reviews/traces, 15 backlog items); decide a manageable batching
      strategy (e.g., by work plan, oldest-first, or by artifact type)
      before attempting a single sweep, and confirm the restoration-ledger
      format actually scales to this volume before committing to it.
- [x] Human decision required (value, policy, budget, legal) — how
      aggressive the initial pass should be (archive everything that
      qualifies immediately, vs. a conservative first batch limited to,
      say, WP-0001 through WP-0009, with later batches as follow-ups) is a
      judgment call the Director may want to weigh in on once Design &
      Review proposes a concrete plan, even though the backlog-gate model
      would otherwise let this run fully autonomously.

## Links

- Spike case: none yet
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
  (existing, this item applies it); related:
  `docs/collaboration/restoration-ledger.md` (existing, empty),
  `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`,
  `docs/issues/LISS-0052-entry-archive-reference-fenced-code-block-gap.md`,
  `docs/backlog/item-0012-document-and-log-lifecycle-management.md`

## Promotion notes

- Date: 2026-08-20
- Decision: Promoted, in the Backlog-layer thread ("残件を進めて"). Per
  ADR 0016 Rule 2, Design & Review proceeds autonomously from here on the
  spike and the batching strategy — but given the Uncertainty section's
  flagged human-decision point (initial-pass aggressiveness), Design &
  Review should propose a concrete batching plan and check with the
  Backlog thread before executing a large first sweep, rather than
  archiving this repository's entire qualifying history in one pass
  unprompted.
- Reason: The deliberately-deferred second half of item-0012, now that all
  six rule-defining facets are closed; ready to begin with the spike.
- Date: 2026-08-20
- Decision: Backlog thread authorizes continuing to batch 2, following the
  exact same process batch 1 used — Design & Review proposes a concrete
  batch-2 plan (batching unit, candidate work plans, fresh eligibility
  re-verification per ADR 0020 Rule 2/4, treatment of any items whose
  already-done status is uncertain rather than assumed) as a new check-in
  issue mirroring `docs/issues/LISS-0055-retroactive-adr-0020-batching-aggressiveness-decision.md`'s
  own shape, the Backlog thread records its decision in that issue's own
  Work Notes (same as LISS-0055's second Work Notes entry did for batch
  1), and only then does an execution work plan and design agreement open.
  This entry itself is the recorded authorization to begin that proposal
  step — it is not itself the batch-2 scope decision, which per this
  item's own Promotion notes above remains a human-decision point reserved
  for the check-in issue once Design & Review's concrete plan exists to
  decide against.
- Reason: `SendMessage` alone is not a durable, independently-checkable
  record of a Director decision in this repository's own model (Prime
  Directive: "no execution without a recorded design agreement"; "every
  decision produces a document"). Design & Review correctly declined to
  proceed on batch 2 from an unbacked message and asked for the same kind
  of artifact every prior decision in this thread has had — this commit is
  that artifact.
