# LISS-0051: `check_retired_terminology`'s `\b` boundary can misbehave for a punctuation-edged retired term

## Metadata

- Local issue ID: LISS-0051
- GitHub issue: none
- Status: in_progress
- Phase: docs-only
- Type: review-finding
- Priority: low
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt, no reclassification.
- Owner/agent: Design & Review group (Planner) — resolved directly via a
  guidance-text mitigation, confirmed by a separate-context Reviewer.
- Related branch: process/item-0012-remaining-facets

## Summary

- `docs/collaboration/reviews/2026-08-19-liss-0049-liss-0050-word-boundary-and-line-wrap-fix-review.md`
  (its LISS-0049 section) independently found, and required as a condition
  of approving LISS-0049's own word-boundary fix, a narrower follow-up gap:
  `\b` fires only at a transition between a `\w` character and a
  `\W`/boundary — for a retired term that itself starts or ends in
  punctuation (the Reviewer's own examples: `C++`, `->`), this produces
  either a silent total no-op against the term's own natural usage
  (`C++` written in ordinary prose is never flagged), or the *reverse* of
  the intended semantics (`->` is not flagged in its natural spaced usage
  but is flagged only when fused directly to word characters on both
  sides — the opposite of standalone-should-flag/fused-should-not).
- Narrower practical exposure than LISS-0049/LISS-0050: it only manifests
  when a future retirement chooses a punctuation-edged term, which is a
  less typical choice than a plain word or multi-word phrase, and the
  guidance `terminology-migration.md` already carries (from LISS-0049's
  own resolution) already steers toward multi-word phrases generally.

## Acceptance Notes

- `docs/collaboration/terminology-migration.md`'s guidance explicitly
  names this class of term (starts/ends in punctuation) as one to avoid,
  with the reasoning (word-boundary semantics), so a future term-retirer
  is warned before choosing such a term, rather than discovering the
  silent failure after the fact.
- This issue is resolved via the guidance mitigation, not a regex rewrite
  — the Reviewer's own assessment judged the practical exposure narrow
  enough that a documented warning is a proportionate response; a deeper
  fix (e.g., detecting a punctuation-edged term and switching to a
  different boundary strategy for it) is recorded as a Deferred Question
  below, not built now.

## Review Finding Record

- Originating review record:
  `docs/collaboration/reviews/2026-08-19-liss-0049-liss-0050-word-boundary-and-line-wrap-fix-review.md`
  (LISS-0049 section, "Independent gap search beyond the issue's own
  testing"; required as a condition of that section's own Approval)
- Affected artifact: `scripts/check-contract-consistency.py`'s
  `check_retired_terminology` function (the underlying `\b`-boundary
  mechanism, unchanged by this issue); `docs/collaboration/terminology-migration.md`'s
  guidance (changed by this issue).
- Failure scenario: a future session retires a term that starts or ends
  in punctuation; the check then either never flags the term's own normal
  usage, or flags only the fused/wrong case — silently under-enforcing or
  inverting the intended rule.
- Reviewer grounds: independently constructed and reproduced both failure
  shapes (`C++` never flagged; `->` flagged only when fused, not in
  normal spaced usage), pasted actual Python `re` session output.
- Dispute raised by: none — a real, reproduced finding, not disputed.
- Arbiter decision record: none — not a deadlock.
- Changed files: `docs/collaboration/terminology-migration.md`.
- Deterministic verification output: see this issue's own Verification
  section.
- Separate Reviewer closure record: pending — dispatched as a fresh agent.

## Dependencies

- Parent: none
- Depends on: none — actionable immediately.
- Blocks: none
- Related: `docs/issues/LISS-0049-retired-terminology-substring-false-positive.md`,
  `docs/collaboration/reviews/2026-08-19-liss-0049-liss-0050-word-boundary-and-line-wrap-fix-review.md`

## Decisions Not Settled by the Design Agreement

- None — a documentation-only mitigation within already-accepted scope.

## Context

- Included: the originating review's LISS-0049 section in full, including
  its `re` session transcript reproducing both failure shapes.
- Omitted: LISS-0050 (a different function; tracked separately).
- Assumptions: none beyond what the review record states directly.

## AI Planning Records

Not required — planning size `S`.

## References

- `docs/collaboration/reviews/2026-08-19-liss-0049-liss-0050-word-boundary-and-line-wrap-fix-review.md`
- `docs/collaboration/terminology-migration.md`

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should `check_retired_terminology` detect a punctuation-edged term and apply a different matching strategy (e.g., plain substring for such a term, with its own narrower false-positive risk accepted as a tradeoff) instead of relying on guidance alone? | Not built now — the Reviewer's own assessment judged this gap's practical exposure narrow given how atypical a punctuation-edged term choice is, and the guidance mitigation is proportionate. Revisit only if a real future retirement actually needs a punctuation-edged term despite the guidance's warning. |

## Work Notes

- 2026-08-19 — Design & Review group (Planner): opened this issue directly
  from the LISS-0049 review's own required condition of approval, and
  resolved it in the same session via a guidance-text addition (not a
  regex rewrite, per the Reviewer's own proportionality assessment).
  `Status: in_progress`, pending separate-context Reviewer confirmation
  under Minor Fix Path.

## Verification

- Read-through diff confirming `terminology-migration.md`'s new guidance
  sentence accurately describes the failure mode (word-boundary
  transition semantics) and names both example shapes the Reviewer
  reproduced.
- `python3 scripts/check-contract-consistency.py` — clean on the real
  tree (documentation-only change, no check logic touched).
- Separate-context Reviewer confirmation: pending — dispatched as a fresh
  agent, per Minor Fix Path.
