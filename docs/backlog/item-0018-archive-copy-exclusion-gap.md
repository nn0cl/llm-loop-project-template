# Backlog item: item-0018-archive-copy-exclusion-gap

## Metadata

- Item ID: item-0018
- Title: Add `docs/archive/` to the template's copy-exclusion list and its
  checker exemption pattern
- Status: promoted
- Created: 2026-08-20
- Updated: 2026-08-20
- Priority hint: high
- Suggested planning size: S
- Owner/agent (optional): unassigned

## Summary

PR #21 (WP-0019, item-0016's first ADR-0020 archival batch) fails CI's
"Repository sanity" / "Check template copy smoke test": 26 dangling-reference
failures, all of the shape `docs/archive/...`, which does not exist' —
`docs/architecture/adr/0016-*.md`, `docs/collaboration/design-review-perspectives.md`,
and `docs/collaboration/restoration-ledger.md` correctly cite real files
now living under `docs/archive/` (created for the first time by WP-0019),
but `docs/archive` is not yet in `scripts/lib/collaboration-template-paths.sh`'s
`collaboration_template_paths` (so it never gets copied to an adopter
target) or in its `collaboration_template_exclude_paths` (so
`check-contract-consistency.py`'s copy-exclusion exemption logic — built
for exactly this pattern by item-0011/LISS-0040 for `agreements/*.md`,
`reviews/*.md`, etc. — doesn't yet recognize `docs/archive/*` references as
expected-absent on a copy).

This is precisely the trigger condition `LISS-0044`
(`docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`, opened
during WP-0014's Reviewer pass, "not actionable... tracked for whichever
later work plan first creates archive content under `docs/archive/`")
predicted. WP-0019 is that later work plan.

## Why it might matter

Blocks PR #21 (already Director-closed) from merging. Also the first real
exercise of ADR 0020's own archival mechanism against CI — confirms whether
the copy/exclusion machinery this template relies on for its own history
(LISS-*.md, item-*.md, WP-*.md, agreements/*.md, reviews/*.md) correctly
generalizes to the new `docs/archive/` class, or needs its own bespoke
handling.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes
- Boundaries or non-goals:
  - `docs/archive/` should almost certainly go in
    `collaboration_template_exclude_paths` (never copied), the same
    treatment as the template's other own-history directories — but
    confirm this against ADR 0020's own stated intent (archived content is
    this template's own history, not adopter-owned content) rather than
    assuming.
  - This closes `LISS-0044` — resolve it as part of this item rather than
    leaving it open once the fix lands, per the finding's own stated
    trigger condition.
  - Reuse `check_dangling_references`'s existing copy-exclusion exemption
    machinery (`_copy_exclusion_patterns()` / `_is_copy_excluded_reference()`,
    from item-0011/LISS-0040) rather than building a second mechanism.

## Uncertainty

- [x] Spec can be written now — reproducible via PR #21's own CI failure,
      root cause identified precisely.
- [ ] Spike required first
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case: none
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: none — related: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`,
  `scripts/lib/collaboration-template-paths.sh`,
  `scripts/check-contract-consistency.py` (`_copy_exclusion_patterns`,
  from LISS-0040), `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`,
  PR #21 CI run
  (https://github.com/nn0cl/llm-loop-project-template/actions/runs/32329294706)

## Promotion notes

- Date: 2026-08-20
- Decision: Promoted, in the Backlog-layer thread, immediately at capture.
  Per ADR 0016 Rule 2, Design & Review proceeds autonomously from here.
- Reason: Blocking PR #21's merge; narrow, well-evidenced, root cause
  already identified, closes a finding already anticipating this exact
  trigger; ready to run.
