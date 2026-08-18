# LISS-0035: Catch document-consistency drift deterministically

## Metadata

- Local issue ID: LISS-0035
- GitHub issue: none
- Status: ready
- Phase: phase-0-design (tooling extension, no application code)
- Type: tooling-enhancement
- Priority: high
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/document-consistency-drift-checks

## Summary

- Make `.github/workflows/ci.yml`'s "Check architecture decision records"
  step dynamic (glob `docs/architecture/adr/*.md` instead of a hardcoded
  `for n in 0001 ... 0016` list), eliminating the recurring manual-bump
  problem at its source.
- Add `check_id_range_collisions` to `scripts/check-contract-consistency.py`:
  compares currently-live numbered files (`LISS-*`, `WP-*`, `item-*`,
  ADR `NNNN-*`) against every number ever assigned per `git log --all
  --diff-filter=A --name-only`, flagging a live file whose number was
  previously used by a different, deleted file.
- Add `check_issue_status_sync`: cross-references each
  `docs/issues/LISS-*.md`'s `Status:` field against its row's status
  column in the work plan(s) whose Issue Graph table names that issue ID.
- Add a `SUPERSEDING_PHRASE_REQUIREMENTS` registration table and
  `check_superseding_phrases` function, modeled exactly on
  `ENTRY_DOCUMENT_ADR_STATEMENTS`/`check_adr_range`, registering ADR 0016's
  three known real supersession instances
  (`docs/collaboration/design-agreement.md`,
  `docs/collaboration/ai-human-scheme.md`, `docs/at-tdd/process.md`).
- Update the script's module docstring to list the new checks alongside
  the existing five.

## Acceptance Notes

- CI step reproduced locally passes against the current ADR set with no
  hardcoded numbers remaining.
- `check_id_range_collisions`: passes clean on current `HEAD`; a
  constructed synthetic collision (e.g. a temp copy with a duplicate
  historical number reintroduced) produces a clear failure message, with
  actual command output pasted in Work Notes.
- `check_issue_status_sync`: same pattern — clean pass on `HEAD`, clear
  failure on a constructed mismatch.
- `check_superseding_phrases`: clean pass on `HEAD` with the three
  registered instances (confirm their exact current anchor wording by
  reading each file first, do not guess it); a constructed removal of one
  registered anchor produces a clear failure, not a silent pass.
- Module docstring's numbered check list updated to match the actual set
  of checks after this change.
- Full `python3 scripts/check-contract-consistency.py` passes.
- Self-review recorded (full form — planning size `M`, four distinct
  additions).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0009-document-consistency-drift-on-completion.md
- Depends on: none
- Blocks: none
- Related: `task_76618661` (superseded by Task 1 of this issue — the
  Design & Review group dismisses it once this issue's CI fix is verified,
  per `DA-2026-08-18-06`'s Deferred Questions), `task_cdbaa1ce` (pattern 5,
  explicitly out of scope here)

## Decisions Not Settled by the Design Agreement

- None identified at design time.

## Context

- Included: `docs/backlog/item-0009-*.md`,
  `scripts/check-contract-consistency.py` (whole file — it is short enough
  to read in full and the new functions must match its existing style),
  `.github/workflows/ci.yml` (the one step only), `DA-2026-08-18-06`.
- Omitted: application-level specs (none apply); pattern 5's own fix
  (tracked elsewhere).
- Assumptions: `docs/architecture/adr/0016-*.md`'s three cited files
  (`design-agreement.md`, `ai-human-scheme.md`, `docs/at-tdd/process.md`)
  still contain the qualifying phrase WP-0002/LISS-0027 added — verify by
  reading each before writing the anchor pattern, per the acceptance notes
  above; if any has since changed, that is a reopening-worthy finding, not
  a silent adjustment.

## AI Planning Records

### AIP-0035-001

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
  one CI-file edit plus three new functions and a docstring update in one
  script
- Compatibility state: Verified — confirmed via full read of
  `scripts/check-contract-consistency.py` that the anchored-registration
  pattern (`ENTRY_DOCUMENT_ADR_STATEMENTS`/`check_adr_range`) is a real,
  reusable template for the superseding-phrase mechanism, not an assumption
- Intended scope: `.github/workflows/ci.yml` (one step),
  `scripts/check-contract-consistency.py` (three new functions, one
  registration table, docstring update)
- Estimated token range: 10,000-20,000 tokens
- Estimated token midpoint: 15,000
- Token metric: approximate output tokens, including synthetic-test
  construction and verification output
- Estimation basis: three new, moderately complex Python functions plus
  synthetic verification for each, larger than WP-0004/0005's single-file
  changes but smaller than a full new subsystem
- Assumptions: single execution attempt
- Confidence: medium
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/collaboration/agreements/2026-08-18-document-consistency-drift-checks.md`
  (`DA-2026-08-18-06`)
- `scripts/check-contract-consistency.py` (existing `check_adr_range`/
  `ENTRY_DOCUMENT_ADR_STATEMENTS` as the direct structural precedent)

## Work Notes

- 2026-08-18 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0009-*.md`'s promotion, after a full read of
  `scripts/check-contract-consistency.py`'s actual structure (not assumed
  from the backlog item's own framing — found the real ADR-range gap is in
  a separate CI file, not the script itself). Dispatched to the
  Implementation group.

## Verification

- Pending Implementation-group execution.
