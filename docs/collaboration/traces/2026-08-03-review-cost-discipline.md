# AI Work Trace

## Request

Director instruction: fix the diagnosed review-cost problem, skip
independent review this time, apply immediately. Covering design agreement:
`docs/collaboration/agreements/2026-08-03-review-cost-discipline.md`
(DA-2026-08-03-02).

## What changed

- Added `docs/templates/self-review.md` (short + full forms) and
  `docs/architecture/adr/0015-review-cost-discipline.md`.
- Propagated into all nine contract files (the self-review paragraph now
  points to the short form by default; the Preflight paragraph now says a
  finding-response record answers one finding, not the whole change). Found
  and fixed one pre-existing gap while doing this: `CLAUDE.md` was missing
  the "contract-file changes are never self-reviewed" note that the other
  four Preflight-carrying files already had.
- Updated `llm-cost-reduction.md`'s Warning Signs with the three concrete
  patterns this diagnosis found.
- Bumped the ADR count 14→15 everywhere it's stated (README, both
  QUICKSTART files, `docs/architecture/README.md`, CI's ADR loop). Found and
  fixed one more pre-existing gap: `README.md`'s "What this template gives
  you" section still described a per-phase Reviewer-approval workflow, missed
  in ADR 0014's own propagation.
- Added `docs/templates/self-review.md` to CI's `required_files`.

## Verification

- `python3 scripts/check-contract-consistency.py --repo .`: pass, on the
  working tree and inside a fresh copy-script target (confirmed
  `self-review.md` distributes).
- `required_files`: 70, 0 missing. ADR loop `0001`-`0015`: pass. `bash -n`:
  OK. Conflict markers: none.

## Review status

**Skipped, per explicit Director instruction, for this change only.** No
review record exists and none is fabricated. ADR 0006's requirement is
unchanged for future contract changes.

## Next safe action

None required. If the Director wants this reviewed after the fact, submit
`docs/architecture/adr/0015-review-cost-discipline.md` and its propagation to
a fresh-context Reviewer — which would itself be the first real exercise of
this ADR's own rule 3.
