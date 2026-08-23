# LISS-0073: Stale "ADR 0002" references in external-resource-adoption-contract.md

## Metadata

- Local issue ID: LISS-0073
- GitHub issue: none
- Status: ready
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: Fast Path
- Type: bug
- Priority: medium (blocks WP-0026's Preflight)
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt.
- Owner/agent: Implementation group (dispatched from
  `docs/work-plans/WP-0026-mirror-file-parity-gaps.md`)
- Related branch: process/promote-item-0022 (or the same execution branch
  LISS-0070/0071/0072 already run on)

## Summary

Discovered mid-execution of LISS-0072 (not part of `docs/backlog/item-0022-...md`'s
original scope): `docs/architecture/external-resource-adoption-contract.md`
consistently mislabels ADR 0003 as "ADR 0002" in four places. Confirmed by
direct read:

- The actual current ADR numbering is `docs/architecture/adr/0002-design-first-ai-request-routing.md`
  (a different topic — AI request routing) and
  `docs/architecture/adr/0003-input-output-reasoning-contracts.md` (the
  IO/reasoning-contracts topic this file is actually extending). ADR 0003's
  own text (line 10) correctly says "ADR 0002 defines design-first payload
  routing," confirming the two ADRs are correctly numbered themselves — the
  drift is confined to this one file's own references.
- Four instances in `docs/architecture/external-resource-adoption-contract.md`
  (pre-LISS-0072-rewrap line numbers) say "ADR 0002" when they mean ADR
  0003:
  1. Lines 14-15 (a `` `docs/architecture/adr/0002-input-output-reasoning-contracts.md` ``
     code-span reference — this file does not exist. This is the one
     `scripts/check-contract-consistency.py` flags as a broken reference,
     and was invisible to the checker only because LISS-0072's own defect
     (the code span split across a line break) meant the checker's
     `CODE_PATH` regex never matched it as a reference at all, before
     LISS-0072's fix.
  2. Line 16: "does not modify ADR 0002 for any other AI-assisted task
     type."
  3. Line 60: "Reuse ADR 0002's source-reference and review-status shape."
  4. Line 63: "(matches ADR 0002's source reference shape: ...)."
- Independently re-`grep`ped the whole repository for "ADR 0002" — no other
  file has this same drift (`docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md`'s
  "Existing ADR 0002/ADR 0010" mention and
  `docs/collaboration/reviews/2026-08-02-contract-first-edition-review.md`'s
  "# ADR 0002: Design-First AI Request Routing" both correctly refer to the
  real ADR 0002 — not touched by this issue).

This is a genuinely new fact the covering design agreement did not
originally settle. Per the design agreement's own Reopening Log entry
(2026-08-23), the Design & Review group decided to extend the agreement's
scope by exactly this one bounded fix, rather than leaving a known-broken
reference in place or expanding into an unrelated repository-wide pass.

## Acceptance Notes

In `docs/architecture/external-resource-adoption-contract.md` only, replace
every occurrence of "ADR 0002" with "ADR 0003", and replace the one
`docs/architecture/adr/0002-input-output-reasoning-contracts.md` code-span
filename with `docs/architecture/adr/0003-input-output-reasoning-contracts.md`.
That is exactly 4 edits in this one file (line numbers will differ slightly
from those listed above depending on whether LISS-0072's rewrap has already
landed on this branch — locate each instance by its "ADR 0002" text, not by
a hardcoded line number). Do not touch any other file, and do not touch any
other sentence in this file. Do not edit
`docs/architecture/adr/0002-design-first-ai-request-routing.md` or
`docs/architecture/adr/0003-input-output-reasoning-contracts.md` themselves.

### Required reproduction (before and after)

1. `grep -n "ADR 0002" docs/architecture/external-resource-adoption-contract.md` —
   before: 4 matches; after: 0 matches.
2. `python3 scripts/check-contract-consistency.py` — before (on top of
   LISS-0072's own fix, before this issue's fix): reports the one
   `docs/architecture/adr/0002-input-output-reasoning-contracts.md` broken
   reference; after this issue's fix: that failure is gone.
3. `git diff docs/architecture/external-resource-adoption-contract.md` for
   this issue's own commit, confirming exactly the 4 "ADR 0002" ->
   "ADR 0003" substitutions and nothing else.
4. `grep -rn "ADR 0002" docs/ AGENTS.md CLAUDE.md .github/copilot-instructions.md .grok .cursor` —
   confirm the only remaining "ADR 0002" mentions in the repository are the
   two pre-existing, correct ones already identified above (the 2026-08-02
   agreement and review record, both genuinely about the real ADR 0002),
   unaffected by this issue's fix.

## Dependencies

- Parent: `docs/work-plans/WP-0026-mirror-file-parity-gaps.md`
- Depends on: LISS-0072 (this issue's fix is easiest to apply after
  LISS-0072's rewrap has landed on the same file, though the fix itself is
  independent of the rewrap's own line-break placement)
- Blocks: WP-0026's Preflight Validation (the checker's one failure)
- Related: `docs/backlog/item-0022-mirror-file-parity-gaps.md` (this issue
  is outside that item's original stated scope, but bundled into the same
  work plan per the design agreement's 2026-08-23 Reopening Log entry),
  `docs/architecture/adr/0002-design-first-ai-request-routing.md`,
  `docs/architecture/adr/0003-input-output-reasoning-contracts.md`

## Decisions Not Settled by the Design Agreement

- None as of this issue's creation — the scope extension is itself recorded
  in the design agreement's own Reopening Log (2026-08-23 entry), which
  this issue implements.

## Context

- Included: the design agreement's Reopening Log entry in full; direct read
  of `docs/architecture/external-resource-adoption-contract.md`'s full
  current content; direct read of both
  `docs/architecture/adr/0002-design-first-ai-request-routing.md` and
  `docs/architecture/adr/0003-input-output-reasoning-contracts.md` to
  confirm which ADR each of the 4 instances actually means; a
  repository-wide `grep -rn "ADR 0002"` to confirm no other file shares
  this drift.
- Omitted: the two pre-existing, correct "ADR 0002" mentions elsewhere in
  the repository (2026-08-02 agreement and review record) — confirmed
  correct, not touched.
- Assumptions: none — every one of the 4 instances was individually
  confirmed to be about the IO/reasoning-contracts topic (matching ADR
  0003's own title and content), not the routing topic (ADR 0002's actual
  title), before concluding all 4 are drift rather than 3 drift + 1
  legitimate reference.

## References

- `docs/collaboration/agreements/2026-08-23-mirror-file-parity-gaps.md`
  (Reopening Log)
- `docs/work-plans/WP-0026-mirror-file-parity-gaps.md`
- `docs/architecture/external-resource-adoption-contract.md`
- `docs/architecture/adr/0002-design-first-ai-request-routing.md`
- `docs/architecture/adr/0003-input-output-reasoning-contracts.md`
- `docs/issues/LISS-0072-inline-code-span-line-wrap-fixes.md`

## Work Notes

- 2026-08-23 — Design & Review group (Planner/Specifier persona). Issue
  opened after the Implementation-group subagent working LISS-0070/0071/0072
  correctly stopped short of fixing this defect (outside its authorized
  scope) and reported it in
  `docs/collaboration/traces/2026-08-23-wp-0026-mirror-file-parity-gaps.md`'s
  own "Next Safe Action" section. Independently re-verified the finding
  (ADR numbering, all 4 instances' topic match, repository-wide grep for
  other occurrences) before opening this issue and amending the design
  agreement.

## Verification

- Before-fix `grep -n "ADR 0002"` count on the target file: 4.
- After-fix: 0.
- `python3 scripts/check-contract-consistency.py`: the one broken-reference
  failure is gone; no new failure introduced.
- `git diff` confined to exactly the 4 substitutions in the one file.
