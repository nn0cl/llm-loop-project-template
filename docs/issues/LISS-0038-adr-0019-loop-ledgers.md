# LISS-0038: Write ADR 0019 (process ADR for loop ledgers)

## Metadata

- Local issue ID: LISS-0038
- GitHub issue: none
- Status: review
- Phase: phase-0-design
- Type: architecture-decision
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/adr-0019-loop-ledgers

## Summary

- Write `docs/architecture/adr/0019-loop-ledgers.md` (or a fuller
  descriptive slug the Implementer chooses, matching this repo's existing
  ADR filename style) stating the five ledgers (spike, backlog,
  loop-settings, post-hoc-audit, findings-must-apply) are an accepted,
  unified process decision, pointing at each source document for its own
  operational detail rather than restating it, and stating explicitly it
  supersedes nothing in ADR 0012-0015 or ADR 0016-0018.

## Acceptance Notes

- Confirms `0019` is genuinely the next-free ADR number at execution time
  (`ls docs/architecture/adr/`) before creating the file.
- Points at, rather than restates, each of the five source documents'
  operational content.
- States explicitly no supersession of ADR 0012-0015/0016-0018.
- Not an ADR-0006 contract file — no trace required.
- Self-review recorded (short form).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0002-adr-loop-ledgers.md
- Depends on: none
- Blocks: none
- Related: `docs/spike/README.md`, `docs/backlog/README.md`,
  `docs/collaboration/loop-settings.md`,
  `docs/collaboration/post-hoc-audit.md`,
  `docs/collaboration/findings-reuse.md`

## Decisions Not Settled by the Design Agreement

- None identified.

## Context

- Included: `docs/backlog/item-0002-*.md`, `DA-2026-08-19-02`, the five
  source documents (read for what to point at, not restate), ADR
  0012-0015, ADR 0016-0018.
- Omitted: application code (none applies).
- Assumptions: none beyond the design agreement's own settled points.

## AI Planning Records

Not required — planning size `S`.

## References

- `docs/collaboration/agreements/2026-08-19-adr-loop-ledgers.md`
  (`DA-2026-08-19-02`)

## Work Notes

- 2026-08-19 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0002-*.md`'s promotion. Confirmed no numbering or
  supersession conflict against ADR 0012-0015/0016-0018. Dispatched to the
  Implementation group.
- 2026-08-19 (Implementation group, Implementer): re-confirmed `0019` was
  next-free (`ls docs/architecture/adr/` -> 0001-0018 contiguous) before
  creating the file. Wrote `docs/architecture/adr/0019-loop-ledgers.md`.
  Also synced `README.md`, `QUICKSTART.md`, `QUICKSTART.ja.md`'s registered
  ADR-range statements (0018 -> 0019) — the same mechanical step every prior
  ADR-adding commit in this repository's history made, needed to keep
  `scripts/check-contract-consistency.py` passing; `.github/workflows/ci.yml`'s
  ADR check is dynamic/contiguous-sequence based (LISS-0035) and needed no
  edit. Committed as `e35ab74` on `process/adr-0019-loop-ledgers`. Self-review
  below (short form, per `docs/templates/self-review.md`, planning size `S`).

### Self-review (short form)

```
Phase / finding: Architecture Path — new ADR document (single new file,
  entry-document ADR-range sync)
Command run: python3 scripts/check-contract-consistency.py
Result:
  contract consistency: all checks passed
Risks considered:
  1. ADR restates a source document's own operational content instead of
     pointing at it (falsification criterion 1 in DA-2026-08-19-02).
  2. ADR silently supersedes or contradicts ADR 0012-0015 or 0016-0018
     (falsification criterion 2).
  3. ADR number collides with a concurrently in-flight work plan's own claim
     (falsification criterion 3).
  4. Contract-consistency drift (dangling reference, or ADR-range mismatch
     in entry documents) introduced by adding the new file.
  5. ADR wrongly treated as exempt from, or wrongly subjected to, ADR-0006
     contract-file trace/review requirements.
Why each does not occur:
  1. Each of the five ledger sections is a 2-5 sentence summary naming what
     the source document governs, with a "See the source document for..."
     pointer; no status vocabulary, numbering scheme, or field list is
     duplicated verbatim — confirmed by direct read-through of all five
     source documents against the ADR text.
  2. Read ADR 0012, 0015, and 0016 in full: ADR 0012 governs the
     review-finding lifecycle only (cited, not restated, via the
     findings-must-apply ledger); ADR 0015 governs self-review/Preflight
     record sizing; ADR 0016 governs session topology. None states the five
     ledger rules this ADR formalizes. ADR 0019's own Decision section
     states explicitly it supersedes nothing in 0012-0015/0016-0018, with
     the "different subject matter" grounds spelled out.
  3. `ls docs/architecture/adr/` run before file creation showed 0001-0018
     contiguous with no 0019; re-run after the commit shows 0001-0019
     contiguous with no gap or collision.
  4. First `check-contract-consistency.py` run failed on two points: (a) an
     illustrative `docs/backlog/item-NNNN-short-slug.md` string in prose,
     resolved as a dangling file reference — fixed by switching to this
     repository's own established `item-NNNN-*.md` wildcard convention
     (used in ADR 0016, `ai-human-scheme.md`, `design-agreement.md`, etc.,
     which the wildcard-aware path matcher skips); (b) the expected
     ADR-range drift in `README.md`/`QUICKSTART.md`/`QUICKSTART.ja.md`
     caused by adding a 19th ADR file — fixed by syncing those three
     files' registered range statements, the same step commit `b1a49c1`
     (ADR 0018) made for the same reason. Final run passes clean.
  5. Cross-checked `docs/collaboration/prompt-instruction-change-control.md`'s
     "Agent Operating Contract Files" list: `docs/architecture/adr/*.md`,
     `README.md`, and `QUICKSTART*.md` are not on it (only `AGENTS.md`,
     `CLAUDE.md`, `.github/copilot-instructions.md`, `.grok/rules/*.md`,
     `.cursor/rules/*.mdc`, `docs/at-tdd/process.md`,
     `docs/collaboration/*.md` except record dirs, `docs/templates/*.md`
     are) — so no trace is required, matching the design agreement's own
     "not an ADR-0006 contract file" statement.
```

## Verification

- `ls docs/architecture/adr/` re-confirmed `0019` free before creation and
  contiguous 0001-0019 after.
- `python3 scripts/check-contract-consistency.py` — `all checks passed`
  (see self-review above for the two intermediate failures found and fixed).
- Read-through against ADR 0012-0015/0016-0018 for no supersession
  conflict — see self-review risk 2 above.
- Work-plan-level Reviewer approval — pending (separate context, Design &
  Review group).
