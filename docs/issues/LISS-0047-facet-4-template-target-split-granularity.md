# LISS-0047: item-0012 facet 4's "explicit rule-level Template-owned/Target-owned split" is not actually delivered by ADR 0008 or WP-0015

## Metadata

- Local issue ID: LISS-0047
- GitHub issue: none
- Status: closed
- Phase: docs-only
- Type: review-finding
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt, no reclassification.
- Owner/agent: unassigned — Design & Review group (Planner) to triage at or
  before item-0012 facet 4 is treated as fully closed.
- Related branch: none yet

## Summary

- `docs/collaboration/agreements/2026-08-19-contract-sync-diff-records.md`
  (`DA-2026-08-19-07`), `docs/issues/LISS-0046-contract-sync-diff-records-and-agent-registry.md`,
  and `docs/work-plans/WP-0015-contract-sync-diff-records.md` all state, as
  settled research fact, that `docs/architecture/adr/0008-template-update-propagation.md`'s
  Tiered Sync Policy "already implements facet 4's Template-owned vs
  Target-owned split." On direct comparison of ADR 0008's actual Tier 1/
  Tier 2 definitions against `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
  facet 4's actual wording, this claim conflates two related but distinct
  classification axes.
- ADR 0008's Tier 1/Tier 2 is a **whole-file authority** split: Tier 1
  files are fully template-authoritative (template wins outright, no
  merge); Tier 2 files (the five agent-persona contract files) need
  AI-assisted reconciliation because they *may* carry adopter-filled
  placeholders. This is a per-file classification of "how much authority
  does the template have over this entire file," decided once, in
  `scripts/lib/collaboration-template-paths.sh`'s `is_contract_persona_file`.
- Facet 4's own wording asks for something narrower and content-level:
  "Split rules **explicitly** into Template-owned (shared path/phase/
  review/sync/logging conventions) versus Target-owned (adopter-specific
  language/domain/architecture/ADRs)" (emphasis in the original). Its own
  examples are kinds of *content within one file* — e.g. within `CLAUDE.md`
  itself (a Tier 2 file), the Phase Discipline / Review Rule sections are
  template-owned conventions, while the "Selected Stack" / "Project
  Boundaries" sections are target-owned facts. ADR 0008's Tier 1/Tier 2
  split does not classify content at this granularity, and no standing
  document in this repository does either.
- What actually performs this content-level separation today is dynamic
  and per-sync-event, not a standing declaration: `docs/templates/contract-file-sync-prompt.md`'s
  Steps 2-4 (diff the target's current content against the template's old
  content to find the adopter's facts; diff the template's old content
  against its new content to find the template's own changes; merge,
  flagging conflicts). WP-0015's own new Sync Diff Record
  (`docs/templates/sync-diff-record.md`) records the *outcome* of that
  per-event diffing after the fact — it is not a standing, ahead-of-time
  declaration a reader could consult to know, for an arbitrary rule not yet
  synced, whether it is template-owned or target-owned.
- Net effect: WP-0015 genuinely closes the *second* half of facet 4 (a
  structured diff record, and a canonical per-agent-tool registry) well —
  both were checked section-by-section against facet 4's own wording and
  match closely. But the *first* half of facet 4 — an explicit, standing
  Template-owned/Target-owned rule split — remains functionally
  unaddressed by both ADR 0008 and WP-0015; it is currently produced only
  implicitly, per sync event, not as a durable document.

## Acceptance Notes

- Whoever picks this up decides between (at least) two resolutions, and
  records the choice with reasoning — this issue does not prescribe which:
  1. Judge the dynamic, per-sync-event approach (Steps 2-4 of
     `contract-file-sync-prompt.md`, now recorded post-hoc in a Sync Diff
     Record) a sufficient and intentional answer to facet 4's "split rules
     explicitly" request, and correct `DA-2026-08-19-07`'s Direction
     section, `LISS-0046`'s Summary, and `WP-0015`'s Goal to state this
     precisely (e.g., "ADR 0008's Tier 1/Tier 2 addresses file-level
     authority; the content-level template-owned/target-owned split
     happens dynamically per sync event, not via a standing document") —
     a wording fix, not a new mechanism.
  2. Or, if the Director/Planner judges a genuinely standing, ahead-of-time
     rule-level split necessary (for example, so a reader can tell without
     waiting for the next sync whether a specific `CLAUDE.md` section is
     template- or target-owned), design that as new content — most likely
     inline annotations in the Tier 2 files themselves, or an extension of
     the new Per-Agent-Tool Rule Applicability Registry's table shape.
- Either resolution should also revisit whether item-0012 facet 4 can be
  marked fully closed on WP-0015 alone, or whether this residual scope
  needs to stay open against facet 4 until resolved.

## Review Finding Record

- Originating review record:
  `docs/collaboration/reviews/2026-08-19-wp-0015-contract-sync-diff-records-review.md`
  (substantive falsification scenario on ADR 0008 vs facet 4's wording)
- Affected artifact: `docs/collaboration/agreements/2026-08-19-contract-sync-diff-records.md`'s
  Direction section, `docs/issues/LISS-0046-contract-sync-diff-records-and-agent-registry.md`'s
  Summary, `docs/work-plans/WP-0015-contract-sync-diff-records.md`'s Goal —
  all three assert the "already implements" claim.
- Failure scenario: a later reader of `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
  treats facet 4 as fully closed by WP-0015 + ADR 0008, when the "split
  rules explicitly" half of facet 4's own wording is not actually
  delivered by either — only the diff-record and per-agent-tool-registry
  half is.
- Reviewer grounds: direct side-by-side reading of ADR 0008's Tier 1/Tier 2
  definitions (`docs/architecture/adr/0008-template-update-propagation.md`,
  "Tiered Sync Policy" section) against item-0012 facet 4's own wording
  (`docs/backlog/item-0012-document-and-log-lifecycle-management.md`,
  facet 4 paragraph) and against `docs/templates/contract-file-sync-prompt.md`'s
  Steps 2-4, which is where the actual content-level separation happens
  today, dynamically, not as a standing document.
- Dispute raised by: none yet — this is the first review of WP-0015.
- Arbiter decision record: none — not a deadlock; recorded as a real,
  non-blocking finding, per this repository's own precedent
  (`docs/collaboration/reviews/2026-08-19-wp-0014-document-log-lifecycle-model-review.md`'s
  Non-Blocking Observations, scenario 13) for a genuine gap that does not
  itself invalidate the artifacts already produced.
- Changed files: none yet.
- Deterministic verification output: none yet — this issue is a wording/
  scope-accuracy finding, not a code or script defect; its own resolution
  verification is a read-through diff of the corrected text once written.
- Separate Reviewer closure record: none yet.

## Dependencies

- Parent: none
- Depends on: none — actionable now (concerns already-landed document text,
  not blocked on any future work plan's own deliverable existing first).
- Blocks: none directly, but should be resolved before item-0012 facet 4 is
  treated as fully closed in any later summary or Director-close record.
- Related: `docs/backlog/item-0012-document-and-log-lifecycle-management.md`,
  `docs/architecture/adr/0008-template-update-propagation.md`,
  `docs/collaboration/agreements/2026-08-19-contract-sync-diff-records.md`,
  `docs/issues/LISS-0046-contract-sync-diff-records-and-agent-registry.md`,
  `docs/work-plans/WP-0015-contract-sync-diff-records.md`,
  `docs/templates/contract-file-sync-prompt.md`

## Decisions Not Settled by the Design Agreement

- Which of the two resolutions in Acceptance Notes is correct (wording fix
  vs. new standing-document mechanism) is left open — this issue does not
  pre-decide it.

## Context

- Included: `DA-2026-08-19-07`, `LISS-0046`, `WP-0015`, ADR 0008 in full,
  item-0012's facet 4 paragraph, `docs/templates/contract-file-sync-prompt.md`,
  `docs/templates/sync-diff-record.md`,
  `docs/collaboration/prompt-instruction-change-control.md`'s new registry
  section.
- Omitted: facets 5 and 6 (separate, later work plans; not relevant to this
  finding).
- Assumptions: none beyond direct reading of the cited documents.

## AI Planning Records

Not required — planning size `S`.

## References

- `docs/collaboration/reviews/2026-08-19-wp-0015-contract-sync-diff-records-review.md`
- `docs/architecture/adr/0008-template-update-propagation.md`
- `docs/backlog/item-0012-document-and-log-lifecycle-management.md`

## Work Notes

- 2026-08-19 — Reviewer (Design & Review group, separate context): opened
  this issue directly from the WP-0015 review's own substantive
  falsification finding, to satisfy `docs/collaboration/findings-reuse.md`'s
  rule that a finding "must change the system or be explicitly declined,"
  rather than leaving it as prose inside the review record alone.
  `Status: proposed` — real and actionable now, but not yet triaged into a
  work plan.
- 2026-08-19 — Design & Review group (Planner): triaged and resolved
  within the same session, choosing Resolution 1 from this issue's own
  Acceptance Notes. Judgment: item-0012 facet 4's own text reads, taken as
  one flowing sentence ("Split rules explicitly... Syncing should not
  mean... it should produce a diff record naming... the adopt/reject/
  defer decision for each"), as describing the split being made explicit
  *through* the diff-record process itself, at the moment a real sync
  happens — not necessarily as a separate, permanent, ahead-of-time
  lookup table that would need independent upkeep whether or not a sync
  ever occurs. Under this reading, the existing per-sync-event
  reconciliation process (`docs/templates/contract-file-sync-prompt.md`'s
  Steps 2-4), now durably recorded going forward by WP-0015's own new
  Sync Diff Record, is a sufficient and intentional answer — not a gap
  requiring new mechanism. Corrected the overstated wording in
  `DA-2026-08-19-07` (Direction section + new Settled Ambiguities row +
  Reopening Log entry), `LISS-0046` (Summary + a new Work Notes
  correction entry, original entry left in place per Invariant 2), and
  `WP-0015` (Goal). `Status: in_progress`, pending separate-context
  Reviewer confirmation of this correction under Minor Fix Path (none of
  the four edited files are ADR-0006 contract files — `docs/collaboration/agreements/`
  and `docs/issues/` and `docs/work-plans/` are all outside that list —
  but Minor Fix Path's own separate-Reviewer-confirmation requirement
  still applies).
  Resolution 2 (a new standing rule-level document) was not pursued —
  this issue's own Resolution 1 explicitly frames itself as a complete
  resolution path, not a placeholder pending further mechanism work; if a
  future session finds the dynamic-process answer insufficient in
  practice, that is a new finding against this same question, not a
  reopening of this one.

- 2026-08-19 — Design & Review group (Planner): separate-context Reviewer
  confirmed the correction —
  `docs/collaboration/reviews/2026-08-19-liss-0047-facet-4-split-wording-fix-review.md`,
  Approved. The Reviewer independently examined the Resolution-1
  substantive question itself (not only mechanical accuracy) and recorded
  its own honest assessment: Resolution 1 is "a genuinely defensible
  reading... not the only reading, and I would not call it the stronger
  of the two on the text alone" — confirmed on the basis that the
  reasoning is sound and disclosed, which is Minor Fix Path's actual
  charge, not a redesign-from-scratch review. `Status: closed` — the
  correction is confirmed and this finding's own lifecycle is complete;
  per `check_open_findings_gate` (item-0009/WP-0011), a review-finding
  referenced in a work plan's own findings table must reach `closed` or
  `wont_do`, not stop at `resolved`, before that work plan can be
  Director-closed without tripping the gate.

## Verification

- Read-through diff confirming the corrected wording in `DA-2026-08-19-07`,
  `LISS-0046`, and `WP-0015` accurately distinguishes ADR 0008's
  whole-file split from facet 4's content-level split and records the
  Resolution-1 judgment with its reasoning.
- Separate-context Reviewer confirmation:
  `docs/collaboration/reviews/2026-08-19-liss-0047-facet-4-split-wording-fix-review.md`
  — Approved. `check-contract-consistency.py` independently re-run by the
  Reviewer, clean.
