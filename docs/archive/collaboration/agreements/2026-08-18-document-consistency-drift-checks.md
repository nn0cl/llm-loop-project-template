# Design Agreement: Catch Document-Consistency Drift Deterministically

## Identity

- Agreement ID: DA-2026-08-18-06
- Date: 2026-08-18
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code, Design & Review group standing session
- Supersedes agreement (if any): none.

## Direction

Per `docs/backlog/item-0009-document-consistency-drift-on-completion.md`
(`Status: promoted`), whose Promotion notes are this agreement's Director
authorization under ADR 0016 Rule 2: extend
`scripts/check-contract-consistency.py` (and, where the gap is actually
outside that script, the relevant CI step) so the five drift patterns
observed across WP-0002 through WP-0006 are caught deterministically
instead of by an agent noticing manually.

## Spike Result (run by the Design & Review group before this agreement)

Full read of `scripts/check-contract-consistency.py`'s actual structure and
its own extensive self-documented history of failed approaches (its module
docstring records four prior rounds of review finding meaning-inference
heuristics that were evaded — connective-word parsing for ADR ranges,
proximity-window matching — before the current anchored-registration design
was adopted). This spike's job was to place each of item-0009's five
patterns against that structure precisely, not generically:

1. **ADR-range checks.** `check_adr_range` does NOT hardcode a number range
   — it computes `last`/`next` dynamically from `adr_numbers(repo)` (an
   `os.listdir` over `docs/architecture/adr/`), then verifies each
   *registered, anchored* sentence in `README.md`/`QUICKSTART.md`/
   `QUICKSTART.ja.md` states the current bound. This already works as
   designed. **The actual hardcoded gap item-0009 points at is a separate
   file this script does not touch at all**: `.github/workflows/ci.yml`'s
   "Check architecture decision records" step, `for n in 0001 ... 0016`, a
   literal number list with no dynamic source. This is why ADR 0017 landing
   required a manually-spawned follow-up (`task_76618661`) instead of
   passing automatically. The durable fix is to make that CI step glob
   `docs/architecture/adr/` instead of listing numbers, which eliminates
   the recurring manual-bump problem at its source rather than adding
   another check that itself would need updating.
2. **ID-range collisions with retired history.** No existing check compares
   currently-live numbered files (`LISS-*`, `WP-*`, `item-*`,
   ADR `NNNN-*`) against numbers used by since-deleted history. This is a
   genuinely new, purely mechanical check: `git log --all --diff-filter=A
   --name-only` already gives every number ever assigned; a live file
   reusing one that belonged to a different, deleted file is a real
   structural fact, not a meaning judgment.
3. **Issue-status double bookkeeping.** No existing check cross-references
   a `docs/issues/LISS-*.md` file's own `Status:` field against its row in
   the owning work plan's Issue Graph table. Both are plain text with a
   fixed shape (`- Status: <word>` and a markdown table cell); this is
   mechanical, not meaning-inference.
4. **Superseding-phrasing propagation.** This is the one pattern that looks
   most like the "meaning" problem the script's docstring explicitly
   disclaims (a mirror keeping a phrase while inverting the rule under it).
   The right model is not a new meaning-inference heuristic — it is the
   *same anchored-registration technique* `ENTRY_DOCUMENT_ADR_STATEMENTS`
   already uses for ADR ranges: when an ADR supersedes another document's
   specific clause, it registers exactly which file(s) and which anchor
   phrase must appear in each; the check verifies presence, and fails
   closed (reports, does not silently pass) if a registered anchor stops
   matching. This is presence-of-a-registered-string, the same category of
   check `check_adr_range` already performs — not prose-meaning inference.
5. **Template-copy exclusion-list gaps.** WP-0005 (item-0005, already
   dispatched and independently confirmed to have found and fixed the
   missing `docs/work-plans/WP-*.md` exclusion) already addresses the
   specific instance item-0009 cites, and its own Implementation session
   spawned a further follow-up task (`task_cdbaa1ce`,
   "`check-contract-consistency.py` failing against a copied target because
   excluded paths are still referenced") for a second, adjacent gap. Per
   item-0009's own explicit instruction not to duplicate already-spawned
   follow-up tasks, this pattern is **out of scope for this work plan**;
   `task_cdbaa1ce` is the tracked vehicle for it.

## Scope

- In scope:
  - `.github/workflows/ci.yml`'s "Check architecture decision records" step:
    replace the hardcoded `for n in 0001 ... 0016` loop with a glob over
    `docs/architecture/adr/*.md`, so it never needs manual bumping again.
    Not an ADR-0006 contract file.
  - A new check function in `scripts/check-contract-consistency.py`,
    `check_id_range_collisions`, comparing currently-live numbered files
    (`docs/issues/LISS-*.md`, `docs/work-plans/WP-*.md`,
    `docs/backlog/item-*.md`, `docs/architecture/adr/NNNN-*.md`) against
    every number `git log --all --diff-filter=A --name-only` shows was ever
    assigned under the same prefix, flagging a live file whose number
    matches a *different*, now-deleted file's number.
  - A new check function, `check_issue_status_sync`, cross-referencing each
    `docs/issues/LISS-*.md`'s `Status:` field against its row's status
    column in the work plan named in its own metadata or found by scanning
    `docs/work-plans/*.md` Issue Graph tables for that issue ID.
  - A new registration mechanism, modeled exactly on
    `ENTRY_DOCUMENT_ADR_STATEMENTS`, for superseding-phrase propagation —
    name and structure fixed in "Settled Ambiguities" below — plus a new
    check function, and registering ADR 0016's own already-known
    supersession instances (`design-agreement.md`, `ai-human-scheme.md`,
    `docs/at-tdd/process.md`) as the first real entries, so the mechanism
    is proven against a real, already-fixed case, not left empty.
  - `scripts/check-contract-consistency.py`'s own module docstring updated
    to document the two new checks in its numbered list (currently 1-5),
    consistent with how every existing check is documented there.
  - `scripts/check-contract-consistency.py` is not an ADR-0006 contract
    file (not in `docs/collaboration/*.md` or the other listed files), so
    these additions do not require a trace.
- Explicitly out of scope:
  - Pattern 5 (template-copy exclusion gaps) — tracked by `task_cdbaa1ce`,
    per item-0009's own explicit instruction.
  - Any new meaning-inference heuristic (connective-word parsing,
    proximity-window matching) — the script's own documented history
    already rejects that approach three times over; this work plan must
    not reopen it.
  - item-0006's own scope (application-code quality gates for adopting
    projects) — this item is specifically about this template's own
    collaboration-document consistency, per item-0009's explicit boundary
    note.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Make `.github/workflows/ci.yml`'s ADR-existence check dynamic | Implementer | Architecture Path | Glob-based, no hardcoded number list; passes against the current ADR set including any ADR landed by a concurrent work plan (0017 and/or 0018) | `bash -n` on the workflow's embedded script where applicable; local reproduction of the step's logic against the actual `docs/architecture/adr/` directory |
| 2 | Add `check_id_range_collisions` | Implementer | Architecture Path | Detects a live file whose number was already used by a different, deleted file (verified with a synthetic before/after test); passes clean on the current repository | run the new check against current `HEAD` (must pass) and against a constructed synthetic collision case (must fail with a clear message) |
| 3 | Add `check_issue_status_sync` | Implementer | Architecture Path | Detects a live LISS `Status:`/work-plan Issue Graph mismatch (verified with a synthetic case); passes clean on the current repository | same pattern: clean pass on `HEAD`, clear failure on a constructed mismatch |
| 4 | Add the superseding-phrase registration mechanism and its check function | Implementer | Architecture Path | Named and structured per Settled Ambiguities; registers ADR 0016's three already-known real instances; passes clean on current `HEAD`; fails closed (reports, not silently passes) when a registered anchor is removed from its target file (verified with a synthetic case) | same pattern as Task 2/3 |
| 5 | Update the module docstring's numbered check list | Implementer | Architecture Path | Lists all seven checks (five existing plus two new — Task 1's CI fix is not a check in this script, so only Tasks 2-4 add script-level checks; confirm the exact count before writing the docstring number) | read-through |
| 6 | Self-review | Implementer | Architecture Path | Full form per `docs/templates/self-review.md` (planning size `M`, multiple new check functions) | self-review record in the relevant issue's Work Notes |
| 7 | Preflight Validation | Implementer / deterministic tool | Architecture Path | `pass` recorded with command output, including each new check's clean-pass-on-`HEAD` and synthetic-failure evidence | Preflight section in WP-0007 |
| 8 | Separate-context Reviewer pass | Reviewer (Design & Review group, separate context) | Architecture Path | Review record independently re-runs each new check's synthetic failure case, not just trusts the Implementer's report | review record under `docs/collaboration/reviews/` |

Sequencing: Task 1 is independent of 2-5 (different file, no shared code) and
may run first or in parallel. Tasks 2-4 add independent functions to the
same script; do them in the listed order to keep the diff reviewable. Task 5
follows 2-4. Task 6 follows 1-5. Task 7 follows 6. Task 8 follows 7.

## Specifications

- None. Tooling/process change; no application specification.

## Boundaries

- No new meaning-inference heuristic (connective-word or proximity
  parsing).
- Pattern 5 stays with `task_cdbaa1ce`; not duplicated here.
- No change to `docs/collaboration/findings-reuse.md` or item-0006's own
  scope.
- No push, PR, or merge to `main`; nothing marked `done`/`closed` until the
  Director's own work-plan-close action.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Is `check_adr_range` itself broken (pattern 1)? | No — it already computes the range dynamically; the actual hardcoded gap is `.github/workflows/ci.yml`'s separate, unrelated ADR-existence loop. Fixing that CI step (Task 1) is the correct, minimal, durable fix — not adding a new script-level check for something the script does not own. | Design & Review group (Planner), via direct code read rather than assuming the backlog item's own framing was the literal implementation location |
| Registration mechanism name/structure for superseding-phrase propagation | `SUPERSEDING_PHRASE_REQUIREMENTS: dict[str, list[tuple[str, str]]]`, keyed by target file path, each entry `(pattern, originating_adr)` — same shape as `ENTRY_DOCUMENT_ADR_STATEMENTS`. A new function `check_superseding_phrases` iterates it exactly the way `check_adr_range` iterates its own table: read the target file, search for the pattern, fail if absent. First real entries: `docs/collaboration/design-agreement.md`, `docs/collaboration/ai-human-scheme.md`, and `docs/at-tdd/process.md`, each anchored on the ADR-0016-qualification phrase already present in each (confirm the exact current wording before writing the anchor pattern — do not guess it from memory). | Design & Review group (Planner), modeling the existing `ENTRY_DOCUMENT_ADR_STATEMENTS` design exactly rather than inventing a new shape |
| Does pattern 5 need any acknowledgment in this work plan at all? | Only a boundary note (this section and Scope) — no task, no code. `task_cdbaa1ce` already exists as its tracked vehicle; this agreement must not create a second, competing fix. | item-0009's own explicit instruction |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should `check_issue_status_sync` also check `docs/backlog/item-*.md` and `docs/work-plans/WP-*.md` status fields against any other cross-referencing table, beyond the one LISS/work-plan pair this item's own evidence names? | A future finding, if the same class of drift is observed for backlog items or work plans specifically, not assumed present now |
| Should the CI dynamic-ADR-check fix (Task 1) make `task_76618661` (the manually-spawned follow-up to bump the CI list for ADR 0017) moot? | Yes, in effect — once Task 1 lands, the Design & Review group should dismiss `task_76618661` as superseded rather than leave a redundant chip pending; recorded here so the dismissal has a stated reason on the record, not done silently |

## Verification

- Each new check function: a clean pass against current `HEAD`, and a
  demonstrated failure against a constructed synthetic violation, both with
  pasted command output.
- `python3 scripts/check-contract-consistency.py` (full run) passes.
- CI's ADR-existence step reproduced locally against the current
  `docs/architecture/adr/` directory.
- Separate-context Reviewer approval, independently re-running at least one
  synthetic-failure case per new check rather than trusting the report.

## Falsification Criteria

- Any new check uses connective-word or proximity-window meaning-inference
  instead of exact anchoring or plain structural comparison.
- A new check's synthetic-failure case is asserted but not actually
  reproduced independently by the Reviewer.
- Pattern 5 is duplicated here instead of left to `task_cdbaa1ce`.
- `.github/workflows/ci.yml`'s ADR-existence step still contains a
  hardcoded number list after this work plan.
- Any contract-file change is claimed for this work plan (none are in
  scope; if the Implementer finds one is actually required, that is a
  reopening trigger, not a silent addition).

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. Recorded basis:
      `docs/backlog/item-0009-document-consistency-drift-on-completion.md`,
      `Status: promoted`, Promotion notes, per ADR 0016 Rule 2.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Made fresh by the Design & Review group
      against this actual plan and the spike result above.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
