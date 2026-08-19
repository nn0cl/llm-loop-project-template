# LISS-0046: Contract-sync diff records and per-agent-tool rule registry (item-0012 facet 4)

## Metadata

- Local issue ID: LISS-0046
- GitHub issue: none
- Status: ready
- Phase: docs-only
- Type: process
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A — first attempt, no reclassification.
- Owner/agent: Design & Review group (Planner/Specifier) for design;
  Implementation group for file creation/edits.
- Related branch: process/contract-sync-diff-records

## Summary

- item-0012 facet 4 ("Single-source multi-agent contract sync") asks for
  two things: (a) an explicit Template-owned vs Target-owned split, and
  (b) syncing that produces a diff record naming the template's own
  change, the target's own change, any conflict, and the adopt/reject/
  defer decision for each — plus recording per-agent-tool intentional
  differences in a canonical document.
- Research finding, before designing anything new: this template already
  has (a) — `docs/architecture/adr/0008-template-update-propagation.md`'s
  Tiered Sync Policy (Tier 1: template-owned, template wins outright;
  Tier 2: the five agent-persona contract files, adopter-owned
  placeholders, AI-assisted reconciliation via
  `docs/templates/contract-file-sync-prompt.md`) already implements this
  split. This issue does not rebuild it — it confirms and cross-references
  it, and closes the two genuinely missing pieces:
  1. A structured, durable **Sync Diff Record** — `docs/templates/sync-diff-record.md`
     (new) — produced every time the Tier 2 reconciliation process runs,
     naming the template's own change, the target's own change, each
     conflict, and the adopt/reject/defer decision, distinct from (and in
     addition to) the general-purpose AI work trace already required.
  2. A canonical **Per-Agent-Tool Rule Applicability Registry** — a new
     section in `docs/collaboration/prompt-instruction-change-control.md`
     — formalizing the Cursor union-vs-literal-mirror fact (currently
     prose buried in one bullet) into an explicit, extensible table, so a
     future intentional per-agent-tool difference has an obvious place to
     be recorded instead of scattered prose.
- No new ADR judged necessary (see "Settled Ambiguities" in the covering
  design agreement) — this refines an already-Accepted ADR's (0008)
  mechanism rather than introducing a new architectural concept, matching
  item-0013's own precedent (a process-rule addition, no new ADR).

## Acceptance Notes

- `docs/templates/sync-diff-record.md` exists with the exact content
  specified in `DA-2026-08-19-07`'s "Exact Content to Produce."
- `docs/collaboration/prompt-instruction-change-control.md` gains the new
  "Per-Agent-Tool Rule Applicability Registry" section, and its existing
  Review Rule bullet is shortened to cross-reference it instead of
  restating the Cursor union-vs-mirror explanation inline.
- `docs/templates/contract-file-sync-prompt.md` gains: one new paragraph
  cross-referencing ADR 0008's Tier 1/Tier 2 split as the
  Template-owned/Target-owned answer, and Step 6 now requires producing a
  Sync Diff Record (using the new template) in addition to the AI work
  trace.
- No edit to `docs/architecture/adr/0008-template-update-propagation.md`
  itself, `CLAUDE.md`, or any of its four mirrors.
- `scripts/check-contract-consistency.py` passes.
- AI work trace recorded — all three touched/created files are ADR-0006
  contract files (`docs/templates/*.md`, `docs/collaboration/*.md`).

## Review Finding Record

N/A — not a review-finding issue.

## Dependencies

- Parent: none
- Depends on: none (does not depend on WP-0014/ADR 0020 — facet 4 is
  independent of facets 1-3's document-lifecycle model)
- Blocks: none
- Related: `docs/backlog/item-0012-document-and-log-lifecycle-management.md`,
  `docs/architecture/adr/0008-template-update-propagation.md`,
  `docs/templates/contract-file-sync-prompt.md`

## Decisions Not Settled by the Design Agreement

- None — the covering design agreement's Settled Ambiguities section
  resolves the "new ADR or not" question and the exact placement of both
  new pieces.

## Context

- Included: `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
  (facet 4 only), `docs/architecture/adr/0008-template-update-propagation.md`
  in full, `docs/templates/contract-file-sync-prompt.md` in full,
  `docs/collaboration/prompt-instruction-change-control.md` in full,
  `docs/collaboration/adoption-guide.md` (referenced by ADR 0008, not
  re-read in full — only its cited relevance to the push/pull sync model
  was needed).
- Omitted: `scripts/update-ai-collaboration-files.sh` and
  `scripts/copy-ai-collaboration-files.sh`'s own implementation (this
  issue does not change script behavior, only the documentation/template
  layer around Tier 2 reconciliation) — not read in full.
- Assumptions: none beyond what ADR 0008 and item-0012 state directly.

## AI Planning Records

Required — planning size `M`. See below.

### AIP-0046-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI, Design & Review group standing
    session
  - Model as displayed: claude-sonnet-5
  - Reasoning setting as displayed: N/A (not surfaced to this session)
  - N/A reason: not surfaced by this harness
- Created at: 2026-08-19
- Planning size: M
- Intended execution route: Design & Review group authors the exact
  content for all three files in the design agreement's "Exact Content to
  Produce" (Specifier output); Implementation group transcribes exactly,
  in its own worktree/branch, with a required AI work trace; Design &
  Review group runs Preflight, then a separate-context Reviewer pass.
- Compatibility state: N/A (no dependency/version claim)
- Intended scope: one new template file, two edited contract files. No
  existing repository document beyond those two is touched.
- Estimated token range: N/A — not tracked in this environment
- Estimated token midpoint: N/A
- Token metric: N/A
- Estimation basis: N/A — harness does not surface token counts
- Assumptions: content is fully specified by this planning record's
  covering design agreement, leaving the Implementation group only
  file-creation/transcription work.
- Confidence: high — this issue extends an already-Accepted, already
  well-understood mechanism (ADR 0008) rather than designing something
  new from first principles; the main risk is scope creep into rebuilding
  parts of ADR 0008 that already work, explicitly fenced off in the
  design agreement's Boundaries.
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
- `docs/architecture/adr/0008-template-update-propagation.md`
- `docs/templates/contract-file-sync-prompt.md`
- `docs/collaboration/prompt-instruction-change-control.md`
- `docs/spike/case-0001-document-log-lifecycle-management/case.md`
  (its own "Decomposition and sequencing" table names this as the
  facet-4 work plan)

## Work Notes

- 2026-08-19 — Design & Review group (Planner/Specifier): local issue,
  work plan (`WP-0015`), and design agreement (`DA-2026-08-19-07`)
  drafted directly on a fresh branch off `main` (`process/item-0012-remaining-facets`),
  since PR #17 (WP-0013 + WP-0014) merged into `main` and the prior
  shared branch was deleted per LISS-0041 self-directed cleanup. Research
  confirmed ADR 0008's Tiered Sync Policy already satisfies facet 4's
  Template-owned/Target-owned split — this work plan closes only the two
  genuinely missing pieces (Sync Diff Record, Per-Agent-Tool Rule
  Applicability Registry) rather than rebuilding the existing mechanism.
- 2026-08-19 — Implementer, self-review (short form, planning size `M`, no
  ADR 0015 escalation criteria apply — a single cohesive doc-only change):

  ```markdown
  Phase / finding: Architecture Path, verbatim transcription (Implementer)
  Command run: python3 scripts/check-contract-consistency.py
  Result:
  contract consistency: all checks passed
  Risks considered:
  - (a) transcribed content in the 3 files does not match DA-2026-08-19-07's
    "Exact Content to Produce" verbatim, including exact insertion points
  - (b) the shortened Review Rule bullet in File 2 loses information rather
    than just relocating it via cross-reference
  - (c) some other part of `prompt-instruction-change-control.md` or
    `contract-file-sync-prompt.md`, beyond the two specified insertion
    points in each, was touched
  - (d) `docs/architecture/adr/0008-*.md`, a sync script, `CLAUDE.md`, or a
    mirror file was touched
  Why each does not occur:
  - (a) `git diff` of both edited files, read side by side against
    DA-2026-08-19-07's "File 2"/"File 3" code blocks, and the new
    `docs/templates/sync-diff-record.md` read side by side against "File
    1" — all three are character-for-character identical to the specified
    text; insertion points match the named anchors ("immediately after ##
    Review Rule's bullet list and before ## Traceability Rule";
    "immediately after the intro paragraph ... before 'Do not run this as
    a mechanical text merge.'"; Step 6 replaced exactly)
  - (b) the new registry table's "Literal full mirror" and "Union" rows
    restate the exact same facts the deleted prose stated (the
    `.cursor/rules/*.mdc` union-with-native-`AGENTS.md`-auto-apply
    mechanism, and `CLAUDE.md`'s 2026-07-25 `@AGENTS.md`-import removal) —
    a direct sentence-by-sentence comparison of the deleted bullet text
    against the new table + shortened bullet confirms no fact is dropped,
    only relocated and cross-referenced
  - (c) `git diff` of each edited file shows exactly one bullet replacement
    and one section insertion per file (File 2), and exactly one paragraph
    insertion and one Step 6 replacement (File 3) — no other line in either
    diff
  - (d) `git status --porcelain` after all edits lists only:
    `docs/templates/sync-diff-record.md` (new),
    `docs/collaboration/prompt-instruction-change-control.md` (modified),
    `docs/templates/contract-file-sync-prompt.md` (modified), this trace
    file (new), and this Work Notes edit (modified) — no ADR, script, or
    `CLAUDE.md`/mirror file appears in that list
  ```

## Verification

- `scripts/check-contract-consistency.py` — recorded in WP-0015's
  Preflight Validation section.
- Read-through diff confirming all three changes match the design
  agreement's "Exact Content to Produce" verbatim, and that no other
  repository file changed.
- Work-plan-level Reviewer approval, separate context, per ADR 0006.
